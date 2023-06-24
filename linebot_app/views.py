from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage, QuickReply, QuickReplyButton, MessageAction

from dialogue_process_app.views import gateway

Line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

from .tasks import async_func


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):

                # 如果為單人聊天室
                if event.source.type == 'user':
                    if isinstance(event.message, TextMessage):
                        mtext = event.message.text

                        if mtext == '！我的ID':
                            try:
                                user_id = event.source.user_id
                                profile = get_user_info(user_id)
                                reply_text = profile.display_name + ": " + user_id
                                print(str(events))
                                Line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))
                            except:
                                Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Get user_id err"))
                        else:
                            return HttpResponse()
                            # Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="僅支援多人群組，閉嘴"))

                # 如果為群組聊天室
                if event.source.type == 'group':
                    if isinstance(event.message, TextMessage):
                        mtext = event.message.text

                        # 指令訊息
                        if str.startswith(mtext, '！'):
                            if mtext == '！我的ID':
                                try:
                                    user_id = event.source.user_id
                                    display_name = get_user_info(user_id).display_name
                                    reply_text = display_name + ": " + user_id
                                    Line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))
                                except:
                                    Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Get user_id error"))

                            if mtext == '！群組ID':
                                try:
                                    group_id = event.source.group_id
                                    group_name = get_group_info(group_id).group_name
                                    reply_text = group_name + ": " + group_id
                                    Line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))
                                except:
                                    Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Get group_id error"))

                        # 一般文字訊息
                        else:
                            # Line_bot_api.reply_message(event.reply_token, TextSendMessage(text=gateway(mtext)))
                            async_func.delay()  # 呼叫 async_func
                            print("async_func called")
                            return HttpResponse('OK', status=200)
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
    

def get_user_info(user_id):
    try:
        profile = Line_bot_api.get_profile(user_id)
        # print(profile.display_name)
        # print(profile.user_id)
        # print(profile.picture_url)
        # print(profile.status_message)
    except LineBotApiError as e:
        print(e.status_code)
        print(e.error.message)
        print(e.error.details)
    return profile

def get_group_info(group_id):
    try:
        group_summary = Line_bot_api.get_group_summary(group_id)
        # print(group_summary.group_id)
        # print(group_summary.group_name)
        # print(group_summary.picture_url)
        # print(group_summary.count)
    except LineBotApiError as e:
        print(e.status_code)
        print(e.error.message)
        print(e.error.details)
    return group_summary
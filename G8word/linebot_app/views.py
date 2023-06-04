from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage, QuickReply, QuickReplyButton, MessageAction

import openai

Line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


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
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text

                    if mtext == '@資料來源':
                        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text='中央氣象局提供'))
                    if mtext == '@網站':
                        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text='網站'))
                    if mtext == '@歷年淹水範圍':
                        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text='淹水'))

                    if mtext == '我的ID':
                        try:
                            Line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.source.user_id))
                        except:
                            Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Get user_id err"))

                    else:
                        #Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="all else"))
                        pass #掛上去就500 "message": "Invalid reply token"

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
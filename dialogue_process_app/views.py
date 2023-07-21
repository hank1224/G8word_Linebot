from django.shortcuts import render
from django.conf import settings

from linebot import LineBotApi
from linebot.models import MessageEvent, TextSendMessage, TextMessage
from linebot.exceptions import LineBotApiError
Line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


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

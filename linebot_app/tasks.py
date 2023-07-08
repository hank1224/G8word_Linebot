from celery import shared_task

from django.utils import timezone

from .models import chat_record, chat_record_mention

import time, datetime
import re

@shared_task
def async_func():
    # 非同步操作
    print('start sleep')
    time.sleep(5)
    print('end sleep')
    return 'Hello, world!'

@shared_task
def save_chat_record(event_dict):
    mention = bool(event_dict['message'].get('mention', []))

    if str.startswith(event_dict['message']['text'], 'http'):
        # 網址訊息，不存入不處理
        return False

    # 處理訊息
    filtered_message = event_dict['message']['text']

    # # 刪除從@字元開頭到空格結尾的文字 ，方法太粗暴已棄用
    # regex = r"@\S+\s?"
    # filtered_message = re.sub(regex, "", event_dict['message']['text']).strip()

    # 處理 @標註
    if mention:
        mentionees = event_dict['message']['mention']['mentionees']
        filtered_message_list = list(filtered_message)

        for mentionee in mentionees:
            start_index = mentionee['index']
            end_index = start_index + mentionee['length']

            # 將被提及用戶名替換為空字串
            for i in range(start_index, end_index):
                filtered_message_list[i] = " "

        filtered_message = "".join(filtered_message_list).strip()
        # 訊息是:@名字 444 @名字 555
        # 輸出是:444     555

    # 處理表情貼
    regex_emoji = r"\([\w\s]+\)"
    filtered_message = re.sub(regex_emoji, "", filtered_message).strip()

    # Line給的timestamp是以毫秒表示的，要轉換成datetime
    timestamp = datetime.datetime.fromtimestamp(event_dict['timestamp'] / 1000.0)
    # 掛上Django設定的位置時區
    aware_timestamp = timezone.make_aware(timestamp)

    created_chat_record = chat_record.objects.create(
        userId=event_dict['source']['userId'],
        groupId=event_dict['source']['groupId'],
        message=event_dict['message']['text'],
        filtered_message=filtered_message if filtered_message else None,
        mention=mention,
        timestamp=aware_timestamp
    )

    if mention:
        for event_mention in event_dict['message']['mention']['mentionees']:
            chat_record_mention.objects.create(
                chat_record=created_chat_record,
                mentioned_userId=event_mention.get('userId', None)
            )
    return True


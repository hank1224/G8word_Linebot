from celery import shared_task

from .models import chat_record, chat_record_mention
import time
import re

@shared_task
def async_func():
    # 非同步操作
    print('start sleep')
    time.sleep(5)
    print('end sleep')
    return 'Hello, world!'

@shared_task
def save_chat_record(event):

    mention = bool(event.message.mentions)

    if str.startswith(event.message.text, 'http'):
        # 網址訊息，不存入不處理
        return True

    # 正則表達式處理訊息
    # 處理 @標註
    regex = r"@\S+\s?"
    filtered_message = re.sub(regex, "", event.message.text).strip()
    
    # 處理表情貼
    regex_emoji = r"\([\w\s]+\)"
    filtered_message = re.sub(regex_emoji, "", filtered_message).strip()

    created_chat_record = chat_record.objects.create(
        userId=event.source.user_id,
        groupId=event.source.group_id,
        message=event.message.text,
        filtered_message=filtered_message if filtered_message else None,
        mention=mention,
        timestamp=event.timestamp
    )

    if mention:
        for event_mention in event.message.mentions:
            chat_record_mention.objects.create(
                chat_record=created_chat_record,
                mentioned_userId=event_mention.user_id
            )
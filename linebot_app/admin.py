from django.contrib import admin

from .models import chat_record, chat_record_mention

@admin.register(chat_record)
class ChatRecordAdmin(admin.ModelAdmin):
    list_display = ['userId', 'groupId', 'message', 'filtered_message', 'mention', 'created_at', 'timestamp']
    search_fields = ['userId', 'groupId']
    list_filter = ['created_at']
    readonly_fields = ['id']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

@admin.register(chat_record_mention)
class ChatRecordMentionAdmin(admin.ModelAdmin):
    list_display = ['id', 'mentioned_userId', 'created_at']
    search_fields = ['chat_record__userId', 'mentioned_userId']
    list_filter = ['created_at']
    readonly_fields = ['id']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

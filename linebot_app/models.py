from django.db import models
import uuid

class chat_record(models.Model):
    userId = models.CharField(max_length=33)
    groupId = models.CharField(max_length=33)
    message = models.TextField()
    filtered_message = models.TextField()
    mention = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField()

    def create(self, *args, **kwargs):
        self.id = f'chat-record-{uuid.uuid4()}'
        return super().create(*args, **kwargs)
    
class chat_record_mention(models.Model):
    chat_record = models.ForeignKey(chat_record, on_delete=models.CASCADE)
    mentioned_userId = models.CharField(max_length=33)
    created_at = models.DateTimeField(auto_now_add=True)

    def create(self, *args, **kwargs):
        self.id = f'chat-mention-{uuid.uuid4()}'
        return super().create(*args, **kwargs)
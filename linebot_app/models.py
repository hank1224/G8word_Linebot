from django.db import models
import uuid

class chat_record(models.Model):
    id = models.CharField(max_length=48, primary_key=True)
    userId = models.CharField(max_length=33)
    groupId = models.CharField(max_length=33)
    message = models.TextField()
    filtered_message = models.TextField(null=True)
    mention = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = f'chat_record_{uuid.uuid4()}'
        return super().save(*args, **kwargs)
    
class chat_record_mention(models.Model):
    id = models.CharField(max_length=56, primary_key=True)
    chat_record = models.ForeignKey(chat_record, on_delete=models.CASCADE)
    mentioned_userId = models.CharField(max_length=33, null=True) # null代表是@All
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = f'chat_record_mention-{uuid.uuid4()}'
        return super().save(*args, **kwargs)
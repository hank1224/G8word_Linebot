from django.db import models
# import uuid

# class chat_record(models.Model):
#     user_id = models.CharField(max_length=33)
#     group_id = models.CharField(max_length=33)
#     raw_message = models.TextField()
#     message = models.TextField()
#     mention = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     timestamp = models.DateTimeField()

#     def create(self, *args, **kwargs):
#         self.id = f'chat-{uuid.uuid4()}'
#         return super().create(*args, **kwargs)
    
# class chat_record_mention(models.Model):
#     chat_record = models.ForeignKey(chat_record, on_delete=models.CASCADE)

#     def create(self, *args, **kwargs):
#         self.id = f'chat-mention-{uuid.uuid4()}'
#         return super().create(*args, **kwargs)
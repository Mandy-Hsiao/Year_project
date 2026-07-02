from django.db import models

class ChatbotFAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name='問題')
    answer = models.TextField(verbose_name='答案')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
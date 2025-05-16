from django.db import models

class Topic(models.Model):
    """사용자가 학습하고 있는 주제."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """모델의 문자열 표현을 반환."""
        return self.text


class Entry(models.Model):
    """주제에 대한 특정 학습 내용."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """엔트리의 간단한 문자열 표현을 반환."""
        return f"{self.text[:50]}..."
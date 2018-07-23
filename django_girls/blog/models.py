from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# models.CharField - 글자 수가 제한된 텍스트를 정의. 글 제목같이 짧은 문자열 정보를 저장할 때 사용.
# models.TextField - 글자 수에 제한이 없는 긴 텍스트를 위한 속성.
# models.DateTimeField - 날짜와 시간을 의미.
# models.ForeignKey - 다른 모델에 대한 링크를 의미

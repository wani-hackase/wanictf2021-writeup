from app.master.models import User

from django.db import models


class Memo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=255)
    content = models.TextField("内容")

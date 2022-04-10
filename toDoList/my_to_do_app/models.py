from django.db import models

# Create your models here.

# 장고에서 하나의 모델은 하나의 클래스로 나타낸다.
# 클랙스 이름이 곧 모델의 이름이다.
class Todo(models.Model):
    content = models.CharField(max_length = 255)

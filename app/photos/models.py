from django.db import models

# Create your models here.
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Photo(models.Model):
    file = models.ImageField(upload_to='photo', blank=True)


# signal 을 받음
# receiver connect 여러개 받으려면 리스트로
# sender가 없으면 모든 모델에서 적용이된다.
# sender외 요소들은 키워드 인자로 받는다.

@receiver(post_delete, sender=Photo)
def photo_delete(sender, instance, **kwargs):
    # sender - 모델 객체가 옴
    # instance - 시그널이 발생된 모델 인스턴스가 온다.
    instance.file.delete(False)


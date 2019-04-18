from django.db import models
from django . contrib. auth.models. import User


# Create your models here.
class Photo(models.Model)
    photo=models.FileField()
    user=models.ForeighnKey(User, on_delete=models.CASCADE)
    description=models.TextField()


class Comment(models.Model)
    photo=models.ForeighnKey(Photo, on_delete=models.CASCADE)
    user=models.ForeighnKey(User, on_delete=models.CASCADE)
    comment=models.TextField()

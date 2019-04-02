from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# Create your models here.
class UserOfApp(AbstractUser):
    gamingname= models.CharField(max_length=100,default=False)

    def __str__(self):
        # return f"uid={self.uid}, uname={self.uname}, upass={self.upass}"
        return self.username

class Answer(models.Model):
    uid= models.ForeignKey(UserOfApp, on_delete=models.CASCADE, db_column='uid')
    question_number= models.IntegerField(default=False)
    selected_answer= models.IntegerField(default=False)
    time= models.FloatField(default=False)

    def __str__(self):
        return str(self.selected_answer)

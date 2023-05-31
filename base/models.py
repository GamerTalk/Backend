from django.db import models

# Create your models here.

class Users(models.Model):
    uid = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    about_me = models.TextField()
    languages = models.JSONField(default=dict)

class english(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE)
    level = models.IntegerField()

class spanish(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE)
    level = models.IntegerField()

class japanese(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE)
    level = models.IntegerField()

class korean(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE)
    level = models.IntegerField()

class chinese(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE)
    level = models.IntegerField()

class german(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE)
    level = models.IntegerField()

class french(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE)
    level = models.IntegerField()

class systems(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE)
    system = models.TextField()

class genre(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE)
    genre = models.TextField()

class messages(models.Model):
    sender = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='sender_uid')
    receiver = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='receiver_uid')
    time_of_message = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return f"From: {self.sender.uid} | To: {self.receiver.uid}"


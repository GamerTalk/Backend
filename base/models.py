from django.db import models

# Create your models here.

class Users(models.Model):
    uid = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    about_me = models.TextField()
    languages = models.JSONField(default=dict)
    currently_playing = models.TextField(default=str)
    user_systems = models.JSONField(default=list)
    user_genre = models.JSONField(default=list)
    user_region = models.TextField(default=str)
    profile_picture_url = models.TextField(default=str)
    
    def __str__(self):
        return self.uid

class English(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='uid')
    level = models.IntegerField()

class Spanish(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='uid')
    level = models.IntegerField()

class Japanese(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='uid')
    level = models.IntegerField()

class Korean(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='uid')
    level = models.IntegerField()

class Chinese(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='uid')
    level = models.IntegerField()

class German(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='uid')
    level = models.IntegerField()

class French(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='uid')
    level = models.IntegerField()

class Systems(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='uid')
    system = models.TextField()

class Genre(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='uid')
    genre = models.TextField()

class Region(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='uid')
    region = models.TextField()

class Messages(models.Model):
    sender = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='uid', related_name='sender_uid')
    receiver = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='uid', related_name='receiver_uid')
    time_of_message = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return f"From: {self.sender.uid} | To: {self.receiver.uid}"

class Posts(models.Model):
    sender = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='uid')
    time_of_message = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"From: {self.sender.uid} | message: {self.message}"

class Flashcards(models.Model):
    user_uid = models.ForeignKey(Users, on_delete=models.CASCADE, to_field='uid')
    front = models.TextField()
    back = models.TextField()

    def __str__(self):
        return f"Created by: {self.user_uid} | front: {self.front} | back: {self.back}"

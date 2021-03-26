from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Personal_info(models.Model):
    name=models.CharField(blank=True,max_length=30)
    picture=models.ImageField(blank=True,upload_to='images/')
    motivational_description=RichTextUploadingField(blank=True)
    birth_date=models.DateField(blank=True)
    phone=models.IntegerField(blank=True,max_length=15)
    email=models.CharField(blank=True,max_length=30)
    address=models.TextField(blank=True,max_length=255)
    social_media_link=models.CharField(blank=True,max_length=400)

    def __str__(self):
        return self.name


class About(models.Model):
    name=models.ForeignKey(Personal_info,on_delete=models.CASCADE)
    about_yourself=RichTextUploadingField()
    total_project=models.IntegerField(blank=True,max_length=5)
    total_volunteer=models.IntegerField(blank=True,max_length=5)


class Skill(models.Model):
    name=models.ForeignKey(Personal_info,on_delete=models.CASCADE)
    python=models.IntegerField(blank=True,max_length=3)
    javascript=models.IntegerField(blank=True,max_length=3)
    c=models.IntegerField(blank=True,max_length=3)
    jquery=models.IntegerField(blank=True,max_length=3)
    django=models.IntegerField(blank=True,max_length=3)
    bootstrap=models.IntegerField(blank=True,max_length=3)
    html=models.IntegerField(blank=True,max_length=3)
    css=models.IntegerField(blank=True,max_length=3)

class Experience(models.Model):
    name=models.ForeignKey(Personal_info,on_delete=models.CASCADE)
    company_name=models.CharField(blank=True,max_length=50)
    position=models.CharField(blank=True,max_length=50)
    address=models.CharField(blank=True,max_length=255)
    starting_date=models.DateField(blank=True)
    ending_date=models.DateField(blank=True)


class Work(models.Model):
    name=models.ForeignKey(Personal_info,on_delete=models.CASCADE)
    title=models.CharField(blank=True,max_length=150)
    description=RichTextUploadingField(blank=True)
    demo_picture=models.ImageField(blank=True,upload_to='images/')
    url=models.CharField(blank=True,max_length=400)




# Generated by Django 3.1.7 on 2021-03-25 15:17

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('picture', models.ImageField(blank=True, upload_to='images/')),
                ('motivational_description', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('birth_date', models.DateField(blank=True)),
                ('phone', models.IntegerField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=30)),
                ('address', models.TextField(blank=True, max_length=255)),
                ('social_media_link', models.CharField(blank=True, max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('demo_picture', models.ImageField(blank=True, upload_to='images/')),
                ('url', models.CharField(blank=True, max_length=400)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.personal_info')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('python', models.IntegerField(blank=True, max_length=3)),
                ('javascript', models.IntegerField(blank=True, max_length=3)),
                ('c', models.IntegerField(blank=True, max_length=3)),
                ('jquery', models.IntegerField(blank=True, max_length=3)),
                ('django', models.IntegerField(blank=True, max_length=3)),
                ('bootstrap', models.IntegerField(blank=True, max_length=3)),
                ('html', models.IntegerField(blank=True, max_length=3)),
                ('css', models.IntegerField(blank=True, max_length=3)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.personal_info')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=50)),
                ('position', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('starting_date', models.DateField(blank=True)),
                ('ending_date', models.DateField(blank=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.personal_info')),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_yourself', ckeditor_uploader.fields.RichTextUploadingField()),
                ('total_project', models.IntegerField(blank=True, max_length=5)),
                ('total_volunteer', models.IntegerField(blank=True, max_length=5)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.personal_info')),
            ],
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-14 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='cover/%Y/%m/%D'),
        ),
    ]

# Generated by Django 3.1.6 on 2021-03-08 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/photoshare/media/default.jpg', upload_to='photoshare/media'),
        ),
    ]

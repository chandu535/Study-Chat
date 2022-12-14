# Generated by Django 4.0.6 on 2022-10-23 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_bio_user_name_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-09 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Your avatar'),
        ),
    ]

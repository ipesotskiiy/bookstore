# Generated by Django 4.1.4 on 2022-12-22 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_rename_favorites_user_bookid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='User role'),
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0046_alter_rating_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='name',
        ),
        migrations.AddField(
            model_name='rating',
            name='rating',
            field=models.PositiveIntegerField(default=1, verbose_name='rating'),
            preserve_default=False,
        ),
    ]

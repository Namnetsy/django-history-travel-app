# Generated by Django 2.1.3 on 2018-12-04 16:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('history_wiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-30 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_like_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('programming', 'programming'), ('cyber security', 'cyber security'), ('mathematics', 'mathematics'), ('physics', 'physics'), ('electronics', 'electronics'), ('other', 'other')], default='other', max_length=30),
            preserve_default=False,
        ),
    ]
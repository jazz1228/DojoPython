# Generated by Django 2.0.3 on 2018-03-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='iconourl',
            field=models.CharField(default='Es jose un balde?', max_length=200),
            preserve_default=False,
        ),
    ]

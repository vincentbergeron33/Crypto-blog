# Generated by Django 3.2.19 on 2023-06-10 13:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230610_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scam',
            old_name='body',
            new_name='content',
        ),
        migrations.AddField(
            model_name='scam',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='scam',
            name='media',
            field=models.CharField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
    ]

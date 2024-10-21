# Generated by Django 5.0.7 on 2024-08-04 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0007_comment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

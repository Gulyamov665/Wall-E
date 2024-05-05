# Generated by Django 5.0.4 on 2024-05-05 12:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_task_comments'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(model_name)ss', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_comments', to='tasks.task')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(model_name)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='comment_photo/')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(model_name)ss', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(model_name)ss', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_image', to='tasks.taskcomments')),
            ],
            options={
                'ordering': ('id',),
                'abstract': False,
            },
        ),
    ]
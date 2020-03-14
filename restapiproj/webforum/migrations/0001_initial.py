# Generated by Django 3.0.3 on 2020-03-12 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('answerer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['create_time'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('body', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('questioner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['create_time'],
            },
        ),
        migrations.CreateModel(
            name='QuestionBookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmarked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_bookmarks', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_bookmarks', to='webforum.Question')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerBookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_bookmarks', to='webforum.Answer')),
                ('bookmarked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_bookmarks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='webforum.Question'),
        ),
        migrations.AddConstraint(
            model_name='questionbookmark',
            constraint=models.UniqueConstraint(fields=('bookmarked_by', 'question'), name='unique_question_bookmarks'),
        ),
        migrations.AddConstraint(
            model_name='answerbookmark',
            constraint=models.UniqueConstraint(fields=('bookmarked_by', 'answer'), name='unique_answer_bookmarks'),
        ),
    ]

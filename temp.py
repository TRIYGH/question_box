# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 23:15
from __future__ import unicode_literals
from django.db import migrations
import csv


def load_data(apps, schema_editor):
    Question = apps.get_model('slack_app', 'Question')
    Answer = apps.get_model('slack_app', 'Answer')
    Comment = apps.get_model('slack_app', 'Comment')

    with open('../../questions.txt') as questions:
        reader = csv.reader(questions, delimiter='+')
        for row in reader:
            temp = Question(title=row[0], description=row[1], tags=row[2], user_id=row[3])
            temp.save()

    with open('../../answers.txt') as answers:
        reader = csv.reader(answers, delimiter='+')
        for row in reader:
            temp = Answer(answer_text=row[0], question_id=row[1], user_up_vote=int(row[2]), user_down_vote=int(row[3]), user_id=row[4])
            temp.save()

    with open('../../comments.txt') as comments:
        reader = csv.reader(comments, delimiter='+')
        for row in reader:
            temp = Comment(comment_text=row[0], answer_id=row[1], user_id=row[2])
            temp.save()


class Migration(migrations.Migration):

    dependencies = [
        ('slack_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]

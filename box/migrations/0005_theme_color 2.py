# Generated by Django 4.0.5 on 2022-06-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0004_alter_idea_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='color',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

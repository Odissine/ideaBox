# Generated by Django 4.0.5 on 2022-06-22 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0003_alter_idea_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='last_modified',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]

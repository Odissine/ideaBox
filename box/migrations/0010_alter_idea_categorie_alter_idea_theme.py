# Generated by Django 4.0.5 on 2022-06-23 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0009_idea_modified_user_alter_idea_categorie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ideas', to='box.categorie'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ideas', to='box.theme'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-19 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='theme',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Categories', to='box.theme'),
            preserve_default=False,
        ),
    ]
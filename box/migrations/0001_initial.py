# Generated by Django 4.0.5 on 2022-06-19 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(editable=False)),
                ('last_modified', models.DateTimeField(editable=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('like', models.IntegerField(default=0)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ideas', to='box.categorie')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ideas', to='box.theme')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
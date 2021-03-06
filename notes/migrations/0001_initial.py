# Generated by Django 4.0.5 on 2022-07-04 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=20)),
                ('note_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notes.note')),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='owner_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notes.user'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('owner_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notes.user')),
            ],
        ),
    ]

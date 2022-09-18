# Generated by Django 3.2 on 2022-09-18 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('short_desciption', models.CharField(blank=True, max_length=400, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('content', mdeditor.fields.MDTextField(blank=True, verbose_name='Content')),
                ('live', mdeditor.fields.MDTextField(blank=True, verbose_name='Live')),
                ('downloadOrView', mdeditor.fields.MDTextField(blank=True, verbose_name='downloadorView')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('visit_num', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_posts', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(related_name='works', to='works.Category_work')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]

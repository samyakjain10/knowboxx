# Generated by Django 3.1 on 2020-09-20 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('class1', models.IntegerField()),
                ('board', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('duration', models.CharField(max_length=20)),
                ('featuredImage', models.ImageField(upload_to='images/')),
            ],
        ),
    ]

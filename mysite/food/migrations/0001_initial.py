# Generated by Django 4.2.8 on 2024-01-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of store', max_length=20)),
                ('address', models.CharField(max_length=50, null=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-11 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message_date',
            field=models.DateField(verbose_name='Message Date'),
        ),
    ]
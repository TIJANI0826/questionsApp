# Generated by Django 3.0 on 2020-02-01 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ischolar', '0003_delete_anwser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.CharField(choices=[('Mathematics', 'Mathematics'), ('English', 'English'), ('Civiv', 'Civic'), ('Data processing', 'Data Processing'), ('Fishery', 'Fishery')], max_length=1),
        ),
    ]

# Generated by Django 4.1.2 on 2023-02-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_add_files_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_files',
            name='file_name',
            field=models.FileField(null=True, upload_to='user_files'),
        ),
    ]
# Generated by Django 4.1.2 on 2023-02-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_contct_name_contact_list_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_files',
            name='file_name',
            field=models.ImageField(null=True, upload_to='user_files'),
        ),
    ]

# Generated by Django 4.1 on 2022-09-12 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApi', '0007_rename_category_categoryold_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categoryOld',
        ),
        migrations.DeleteModel(
            name='categoryOld',
        ),
    ]
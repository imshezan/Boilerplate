# Generated by Django 4.1 on 2022-08-14 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseApi', '0003_rename_question_post_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='details',
            new_name='detail',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='baseApi.category'),
        ),
    ]

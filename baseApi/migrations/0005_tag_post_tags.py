# Generated by Django 4.1 on 2022-08-14 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApi', '0004_alter_category_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='baseApi.tag'),
        ),
    ]
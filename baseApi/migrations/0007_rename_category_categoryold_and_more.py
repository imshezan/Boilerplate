# Generated by Django 4.1 on 2022-09-12 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseApi', '0006_rename_details_category_detail_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='categoryOld',
        ),
        migrations.AlterModelOptions(
            name='categoryold',
            options={'verbose_name': 'Category old', 'verbose_name_plural': 'Categories old'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='categoryOld',
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='baseApi.node')),
            ],
            options={
                'verbose_name_plural': 'Nodes',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Categories',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('baseApi.node',),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Sub categories',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('baseApi.node',),
        ),
        migrations.AddField(
            model_name='post',
            name='subcategory',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='baseApi.subcategory'),
            preserve_default=False,
        ),
    ]

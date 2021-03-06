# Generated by Django 4.0.4 on 2022-06-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_category_delete_rightpost_post_view_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

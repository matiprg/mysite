# Generated by Django 4.2 on 2023-05-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_created_date_alter_post_published_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(null=True),
        ),
    ]
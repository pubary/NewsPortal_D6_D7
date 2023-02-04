# Generated by Django 4.1.5 on 2023-01-15 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_post_type_rename_type_post_p_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='p_type',
            field=models.CharField(choices=[('AT', 'Статья'), ('NW', 'Новость')], max_length=7, verbose_name='Тип'),
        ),
    ]
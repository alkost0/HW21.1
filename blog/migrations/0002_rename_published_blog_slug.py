# Generated by Django 4.2.4 on 2023-09-10 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='published',
            new_name='is_published',
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='views',
            field=models.IntegerField(default=0, verbose_name='просмотры'),
        ),
    ]
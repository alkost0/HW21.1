# Generated by Django 4.2.4 on 2023-09-10 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=100, verbose_name='slug')),
                ('content', models.TextField(blank=True, null=True, verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='превью')),
                ('date_of_creation', models.DateTimeField(blank=True, null=True, verbose_name='дата создания')),
                ('published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('views', models.IntegerField(verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
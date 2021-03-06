# Generated by Django 3.0.4 on 2020-04-25 12:11

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',), 'verbose_name': 'Коментар', 'verbose_name_plural': 'Коментар'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-updated',), 'verbose_name': 'Публікація', 'verbose_name_plural': 'Публікації'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ('-updated',), 'verbose_name': 'Тема', 'verbose_name_plural': 'Теми'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='Текст коментаря'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='posts.Comment', verbose_name='Коментар'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.Post', verbose_name='Публікація'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата оновлення'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Текст публікації'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/images/', verbose_name='Зображення'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Статус публікації'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата редагування'),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(blank=True, default=0, verbose_name='Кількість переглядів'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='closed',
            field=models.BooleanField(blank=True, default=False, verbose_name='Закрита'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/images/', verbose_name='Зображення'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата редагування'),
        ),
    ]

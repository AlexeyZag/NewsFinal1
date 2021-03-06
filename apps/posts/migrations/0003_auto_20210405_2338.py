# Generated by Django 3.1.7 on 2021-04-05 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210405_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='postphoto',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.author', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='postphoto',
            name='categories',
            field=models.ManyToManyField(default=None, to='posts.Category', verbose_name='категории'),
        ),
        migrations.AddField(
            model_name='postphoto',
            name='headline',
            field=models.CharField(default=None, max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='postphoto',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='files'),
        ),
    ]

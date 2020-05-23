# Generated by Django 2.1.7 on 2020-05-21 23:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertising',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_name', models.CharField(max_length=100, verbose_name='广告名称')),
                ('ad_url', models.URLField(max_length=225, verbose_name='广告链接')),
                ('img_url', models.URLField(max_length=225, verbose_name='展示图片URL')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否推广')),
            ],
            options={
                'verbose_name': '广告链接',
                'verbose_name_plural': '广告链接',
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='站点名称')),
                ('url', models.URLField(max_length=225, verbose_name='站点链接')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('body', mdeditor.fields.MDTextField(verbose_name='正文')),
                ('created_time', models.DateTimeField(verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读数')),
                ('is_top', models.BooleanField(default=False, verbose_name='顶置文章')),
                ('is_show', models.BooleanField(default=True, verbose_name='发布状态')),
                ('sort_level', models.PositiveIntegerField(blank=True, null=True, verbose_name='排序级别')),
                ('post_type', models.CharField(choices=[('post', '博客文章'), ('about', '关于页面'), ('project', '我的项目')], default='post', max_length=20, verbose_name='类型')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '博客文章',
                'verbose_name_plural': '博客文章',
                'ordering': ['-is_top', '-sort_level', '-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='标签'),
        ),
    ]

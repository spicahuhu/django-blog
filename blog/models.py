from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', null=True, blank=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    tags = models.ManyToManyField('Tag', blank=True)
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)
    abstract = models.CharField(max_length=255, blank=True)

    category = models.ForeignKey('Category', verbose_name='分类',
                                 null=True,
                                 on_delete=models.SET_NULL)
    uid = models.ForeignKey(User)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_time']

    def get_absolute_url(self):
        return reverse('blog:content', kwargs={'pk':self.id})

"""
分类
"""
class Category(models.Model):
    STATUS_CHOICES = (
        ('0', '有效'),
        ('-1', '无效'),
    )
    name = models.CharField('类名', max_length=20)
    pid = models.ForeignKey('self', null=True, blank=True)
    status = models.CharField('是否启用', max_length=1, choices=STATUS_CHOICES, default=0)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name

# class User(models.Model):
#     name = models.CharField('用户名', max_length=20)
#     nick = models.CharField('昵称', max_length=50)
#     phone = models.CharField('手机号', max_length=11, blank=True)
#     desc = models.TextField('简介', blank=True)
#     created_time = models.DateTimeField('创建时间', auto_now_add=True)
#     updated_time = models.DateTimeField('更新时间', auto_now=True)
#     user_tags = models.ManyToManyField('Tag', blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    created_time = models.DateTimeField('创建时间',null=True, blank=True)

    def __str__(self):
        return self.name
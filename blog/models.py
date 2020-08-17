from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    name = models.CharField('分类名称',max_length=100)
    
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('标签名称',max_length=70)
    
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('标题',max_length=70)
    body = models.TextField('正文')
    created_time = models.DateField('创建时间',default=timezone.now)
    modified_time = models.DateField('修改时间',auto_now=True)
    excerpt = models.CharField('摘要',max_length=200,blank=True)
    category = models.ForeignKey(Category,verbose_name='分类',on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,verbose_name='标签',blank=True)
    author = models.ForeignKey(User,verbose_name='作者',on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.title
    
    #自定义 get_absolute_url方法
    #记得从django.urls中导入reverse函数
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

if __name__=='__main__':
    print(timezone.now()) 

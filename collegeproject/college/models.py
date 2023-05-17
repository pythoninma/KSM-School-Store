from django.db import models
from django.urls import reverse

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)



    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'

    def get_url(self):
            return  reverse('college:streams_by_department',args=[self.slug])

    def __str__(self):
            return  '{}'.format(self.name)

class Stream(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)



    def get_url(self):
        return  reverse('college:streamDeptdetail',args=[self.department.slug,self.slug])


    class Meta:
        ordering=('name',)
        verbose_name='stream'
        verbose_name_plural='streams'

        def __str__(self):
            return '{}'.format(self.name)
class College(models.Model):
    username=models.CharField(max_length=250)
    password=models.TextField()


    def __str__(self):
        return self.name



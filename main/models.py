from django.db import models

# Create your models here
class tags(models.Model):
  name = models.CharField(max_length=30)
  
  def __str__(self):
    return self.name
  
class Project(models.Model):
  project_name = models.CharField(max_length=30)
  project_title = models.CharField(max_length=30)
  project_description = models.TextField()
  creation_date = models.DateTimeField(auto_now_add=True)
  tags = models.ManyToManyField(tags)
  project_image = models.ImageField(upload_to = 'projects/',default='image')
  preview_url = models.URLField(max_length=50,default='')
  
  
  def __str__(self):
    return self.project_name
  
  @classmethod
  def my_projects(cls):
    project = Project.objects.all()
    return project


class About(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30,default='')
  profession = models.CharField(max_length=30)
  details = models.TextField()
  profile_image=models.ImageField(upload_to = 'abouts/',default='image')
  email = models.EmailField(max_length=50,unique=True,default='')
  
  def __str__(self):
    return self.first_name
  
  @classmethod
  def my_abouts(cls):
    abouts = About.objects.all()
    return abouts
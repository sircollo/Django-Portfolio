from django.test import TestCase
from .models import *
# Create your tests here.
class ProjectTestCase(TestCase):
  #new project and save
  def setUp(self):
    
    self.new_project = Project(project_name='pithced',project_title='pitchs-flask',project_description='Flask application')
    self.new_project.save()
    
    self.new_tag = tags(name = 'testing')
    self.new_tag.save()
    
    self.new_project.tags.add(self.new_tag)
    
  def tearDown(self):
    Project.objects.all().delete()
    tags.objects.all().delete()
    
  # def test_get_project(self):
  #   projects = Project.my_projects()
  #   self.assertTrue(len(projects)>0)
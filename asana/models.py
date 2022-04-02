from django.db import models


#--------------------------------------------------- class Sprint(models.Model):
    #---------------------------- sprint_name = models.CharField(max_length=999)
#------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------ 
#-------------------------------------------------- class Project(models.Model):
    #--------------------------- project_name = models.CharField(max_length=999)
#------------------------------------------------------------------------------ 
#------------------------------------------------- class Assignee(models.Model):
    #---------------------------- person_name = models.CharField(max_length=999)
    
class Task(models.Model):
    PRIORITIES_COMPLEXITIES = [
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High')
    ]
    TASK_SECTION = [
    ('T', 'To do'),
    ('I', 'In Progress'),
    ('C', 'Completed'),
    ('A', 'approved')
    ]
    id = models.IntegerField(primary_key=True, default=None)
    name = models.CharField(max_length=999, default='')
    notes = models.CharField(max_length=999)
    assignee = models.CharField(max_length=999)
    project = models.CharField(max_length=999)  
    sprint = models.CharField(max_length=999)    
    start_date = models.DateField(null=True, default = None)
    end_date = models.DateField(null=True, default = None)
    worked_hours = models.IntegerField(null=True, default = None)
    estimated_hours = models.IntegerField(null=True, default = None)
    priority = models.CharField(max_length=1, choices=PRIORITIES_COMPLEXITIES, null=True, default = None)
    complexity = models.CharField(max_length=1, choices=PRIORITIES_COMPLEXITIES, null=True, default = None)

    


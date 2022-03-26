from django.db import models


class Sprint(models.Model):
    sprint_name = models.CharField(max_length=999)

    
class Project(models.Model):
    project_name = models.CharField(max_length=999)
    
class Assignee(models.Model):
    person_name = models.CharField(max_length=999)
    
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
    task_name = models.CharField(primary_key=True, max_length=999)
    task_notes = models.CharField(max_length=999)
    start_date = models.DateField()
    end_date = models.DateField()
    worked_hours = models.IntegerField()
    estimated_hours = models.IntegerField()
    priority = models.CharField(max_length=1, choices=PRIORITIES_COMPLEXITIES)
    complexity = models.CharField(max_length=1, choices=PRIORITIES_COMPLEXITIES)
    assignee = models.ForeignKey(Assignee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)    
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    


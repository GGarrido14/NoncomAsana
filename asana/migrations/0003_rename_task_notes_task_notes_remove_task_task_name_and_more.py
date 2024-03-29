# Generated by Django 4.0.2 on 2022-04-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asana', '0002_alter_task_task_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_notes',
            new_name='notes',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_name',
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(default='TASK NAME', max_length=999, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.CharField(max_length=999),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.CharField(max_length=999),
        ),
        migrations.AlterField(
            model_name='task',
            name='sprint',
            field=models.CharField(max_length=999),
        ),
        migrations.DeleteModel(
            name='Assignee',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Sprint',
        ),
    ]

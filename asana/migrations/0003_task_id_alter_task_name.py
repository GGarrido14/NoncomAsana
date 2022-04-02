# Generated by Django 4.0.2 on 2022-04-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asana', '0002_remove_task_id_alter_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='id',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(default='', max_length=999),
        ),
    ]

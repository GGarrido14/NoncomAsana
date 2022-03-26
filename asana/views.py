from django.shortcuts import render
from django.http import HttpResponse
import json
from jsonpath_ng import jsonpath, parse
import requests
from asana import models

personal_access_token = '1/1201795604903663:b6a600a630ec92e971f05b50429f8094'

headers = {"Authorization": "Bearer 1/1201795604903663:b6a600a630ec92e971f05b50429f8094"}

endpoint = 'https://app.asana.com/api/1.0'
workspace_gid_value = '1201795461843442'

# r = requests.get(endpoint,headers=headers)
# print(r.json())

jsonpath_expr_gid = parse('data[*].gid')

teams_organization_endpoint = endpoint + '/organizations/' + workspace_gid_value + '/teams'
teams_organization_json = requests.get(teams_organization_endpoint, headers=headers).json()
#print("Team gid json ", teams_organization_json)
teams_organization_json_data = json.loads(json.dumps(teams_organization_json))

#DatamInContext
team_gid_data = jsonpath_expr_gid.find(teams_organization_json_data)
#print("Team gid data ", team_gid_data)
team_gid_value = team_gid_data[0].value
#Valor del gid
#print("Team gid ", team_gid_value)




team_projects_endpoint = endpoint + '/teams/' + team_gid_value + '/projects'
team_projects_json = requests.get(team_projects_endpoint, headers=headers).json()
team_projects_json_data = json.loads(json.dumps(team_projects_json))
projects_gid = jsonpath_expr_gid.find(team_projects_json_data)

teams_gid = jsonpath_expr_gid.find(team_projects_json_data)



# Get teams project
for team_gid in teams_gid:
    #   print(f'Get multiple tasks by project teams gid: {teams_gid.value}')  
    for projects_gid in {team_gid.value}:
        multiple_tasks_endpoint = endpoint + '/tasks?project=' + projects_gid
        multiple_tasks_json = requests.get(multiple_tasks_endpoint, headers=headers).json()
        multiple_tasks_json_data = json.loads(json.dumps(multiple_tasks_json))           
        #print(f'Get a tasks by project gid: ', jsonpath_expr_gid.find(multiple_tasks_json_data))        
        for task in jsonpath_expr_gid.find(multiple_tasks_json_data):               
            for task_gid in {task.value}: 
                task = models.Task()    
                get_task_endpoint = endpoint + '/tasks/' + task_gid
                get_task_json = requests.get(get_task_endpoint, headers=headers).json()
                get_task_json_data = json.loads(json.dumps(get_task_json))                                
                #print("task_json_data ", get_task_json_data)
                jsonpath_expr_a_name= parse('$.name')

                jsonpath_expr_project = parse('data[*].projects')
                task_project = jsonpath_expr_project.find(get_task_json_data)                
                task_project_data = task_project[0].value
                #print("Proyecto data", task_project_data)
                for data in task_project_data:
                    project_json_data = json.loads(json.dumps(data))
                    #print("Json del proyecto ", project_json_data)
                    project_name = jsonpath_expr_a_name.find(project_json_data)                   
                    #print("Nombre del proyecto ", project_name[0].value)
                    
                #Busca en el json el grupo que representa a la persona asignada
                jsonpath_expr_assignee = parse('data[*].assignee')                
                task_assignee  = jsonpath_expr_assignee.find(get_task_json_data)
                #print("Persona asignada ", task_assignee)
                task_assignee_data = task_assignee[0].value
                #Si la persona asignada existe para la tarea
                if (task_assignee_data is not None):
                    
                    #print("Persona asignada data ", task_assignee_data)
                    
                    #Convierte el dato encontrado en json para que entonces
                    assignee_json_data = json.loads(json.dumps(task_assignee_data))
                    
                    #print("Persona asignada json data ", assignee_json_data)                    
                    #Encontrarlo con el patron definido y definir una variable que almacene el nombre
                    assignee_name = jsonpath_expr_a_name.find(assignee_json_data)                    
                    #print("Nombre persona asignada ", assignee_name[0].value)
                    #task.assignee.person_name = assignee_name[0].value
                    
                    jsonpath_expr_name = parse('data[*].name')
                    task_name  = jsonpath_expr_name.find(get_task_json_data)                    
                    print('Nombre tarea: ', task_name[0].value)
                    task.task_name = task_name[0].value

                    jsonpath_expr_note = parse('data[*].notes')
                    task_note  = jsonpath_expr_note.find(get_task_json_data)                    
                    print('Descripcion tarea: ', task_note[0].value)
                    task.task_note = task_note[0].value
                                        

                



                    

                


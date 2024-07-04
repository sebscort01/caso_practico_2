'''
Diplomado Python
Alumno : Sebastian Cortes
Caso Practico Modulo 2
'''


#Base de datos de los Alumnos
Base_Alumnos = {1:{'Nombre':'Juan Perez','calificaciones':[9.5,8.0,6.5,9.0]},2:{'Nombre':'Raul Lopez','calificaciones':[8.0,8.0,7.5,7.0]},3:{'Nombre':'Jose Gutierrez','calificaciones':[10.0,9.0,9.0,10.0]},4:{'Nombre':'Juan Martinez','calificaciones':[8.5,9.5,8.0,10.0]},5:{'Nombre':'Maria Perez','calificaciones':[6.5,7.5,7.0,8.0]},6:{'Nombre':'Santiago Santos','calificaciones':[7.0,8.0,10.0,7.5]}}

#Activacion de While
no_lista = int(input('Ingrese el numero de lista que desea consultar: '))

#Funcion para imprimir nombre y promedio
def datos_alumno(llave):
    print(Base_Alumnos[llave]['Nombre'])
    print(round((sum(Base_Alumnos[llave]['calificaciones'])/len(Base_Alumnos[llave]['calificaciones'])),2))

#Ciclo While que termina si el usuario introduce una llave que no existe en el diccionario
while no_lista in Base_Alumnos:
    datos_alumno(no_lista)
    no_lista = int(input('Ingrese el numero de lista que desea consultar: '))


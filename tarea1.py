from functools import reduce
#----------------TAREA----------------
lista_reg = [
    {"nombre": "sebastian", "notas": [5.0, 3.5, 4.7], "edad": 25},
    {"nombre": "valentina", "notas": [3.0, 3.8, 4.3], "edad": 22},
    {"nombre": "daniela", "notas": [5.0, 3.5, 4.7], "edad": 23}
]

#1)Calcular promedio de cada estudiante con el "map"
#2)filtrar estudiantes con edad>N  "filter"
#3)promedio general con "reduce"




# Calcular promedio de notas de cada estudiante usando map
promedios_estudiantes = list(map(lambda estudiante: sum(estudiante["notas"]) / len(estudiante["notas"]), lista_reg))
print("Promedio de notas de cada estudiante:", promedios_estudiantes)

# Filtrar estudiantes con edad mayor a N usando filter
N = 23
estudiantes_mayores_a_N = list(filter(lambda estudiante: estudiante["edad"] > N, lista_reg))
print("Estudiantes con edad mayor a", N, ":", estudiantes_mayores_a_N)

# Calcular promedio general de todas las notas usando reduce
notas_totales = reduce(lambda notas, estudiante: notas + sum(estudiante["notas"]), lista_reg, 0)
total_notas = sum(len(estudiante["notas"]) for estudiante in lista_reg)
promedio_general = notas_totales / total_notas
print("Promedio general de todas las notas:", promedio_general)

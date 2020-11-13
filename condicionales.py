#IF
print("--------------------Programa de evaluación de notas de alumnos---------------------")

nota_alumno=int(input("Introduce la nota del alumno: "))

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion
    
print(evaluacion(nota_alumno))

#IF-ELSE-ELIF
print("----------------------Verificación de acceso--------------")
edad_usuario=int(input("Introduce tu edad, por favor: "))

if edad_usuario<18:
    print("No puedes pasar")
elif edad_usuario>100:
    print("Edad Incorrecta")
else:
    print("Puedes pasar")
print("El programa ha finalizado")
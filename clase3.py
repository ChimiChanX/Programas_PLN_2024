semana=["lunes", "martes", "miercoles", "jueves", "viernes", ]
print(" semana laboral", semana)
print("dia 1= ", semana[4] )
semana[4]= "sabado"
print("semana laboral = ", semana)
semana[4] = "viernes"
longitud_lista=len(semana)
print("longitud lista", longitud_lista)
posicion=semana.index("miercoles")
print("posicion miercoles = ", posicion)
semana.append("sabado")
print("semana laboral = ", semana)
del semana [4]
print("semana laboral = ", semana)
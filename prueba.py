import numpy as np

otp=np.array([[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
     [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
     [0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,],
     [0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,],
     [0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
     [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,],
     [0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0],
     [0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,],
     [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,],
     [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,],
     [0,0,0,0,0,0,0,0,1,0,0,0,0,10,0,0,0,0,0,0,],
     [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,],
     [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,1000,0,0,0,0,0,0,0,0,],
     [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
     [0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,],
     [0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,]])

# Configuración de los parámetros gamma y alfa para el Q-Learning
gamma = 0.75
alpha = 0.9
# Inicialización de los valores Q
Q = np.zeros([20, 20])

# Implementación del proceso de Q-Learning
for i in range(1000):
    estado_actual = np.random.randint(0, 20)
    acciones_realizables = [j for j in range(20) if otp[estado_actual, j] > 0]
    estado_siguiente = np.random.choice(acciones_realizables)
    TD = otp[estado_actual, estado_siguiente] + gamma * Q[estado_siguiente, np.argmax(Q[estado_siguiente, :])] - Q[estado_actual, estado_siguiente]
    Q[estado_actual, estado_siguiente] += alpha * TD

# Definición de la función ruta
def ruta(estado_inicial, estado_final):
    ruta_optima = [estado_inicial]
    while estado_inicial != estado_final:
        estado_siguiente = np.argmax(Q[estado_inicial, :])
        ruta_optima.append(estado_siguiente)
        estado_inicial = estado_siguiente
    return ruta_optima

# Entrada de datos desde el teclado para el estado inicial y final
estado_inicial = int(input("Ingrese el estado inicial (0-19): "))
estado_final = int(input("Ingrese el estado final (0-19): "))

# Llamada a la función ruta y muestra de la ruta óptima
ruta_resultante = ruta(estado_inicial, estado_final)
print("Ruta óptima a seguir:", ruta_resultante)

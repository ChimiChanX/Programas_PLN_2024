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
epsilon = 0.2  # Porcentaje de exploración

# Inicialización de los valores Q
Q = np.zeros([20, 20])

# Implementación del proceso de Q-Learning
for i in range(1000):
    estado_actual = np.random.randint(0, 20)
    
    # Selección de la siguiente acción con exploración epsilon-greedy
    if np.random.rand() < epsilon:
        estado_siguiente = np.random.choice(20)
    else:
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

estado_inicial = int(input("Ingresa el estado inicial (0-19): "))
estado_final = int(input("Ingresa el estado final (0-19): "))
ruta_resultante = ruta(estado_inicial, estado_final)




print(acciones_realizables)
print("Ruta óptima a seguir:", ruta_resultante)

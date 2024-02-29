import socket

# Configuración del cliente
host = 'localhost'
puerto = 12345

# Crear un socket del cliente
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
cliente_socket.connect((host, puerto))
print(f"Conectado al servidor en {host}:{puerto}")

while True:
    # Enviar un mensaje al servidor
    mensaje = input("Cliente: ")
    cliente_socket.send(mensaje.encode())

    # Recibir la respuesta del servidor
    datos_recibidos = cliente_socket.recv(1024)
    print(f"Servidor: {datos_recibidos.decode()}")

# Cerrar la conexión
cliente_socket.close()

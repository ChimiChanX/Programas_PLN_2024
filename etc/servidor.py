import socket

# Configuración del servidor
host = 'localhost'
puerto = 12345

# Crear un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket a la dirección y el puerto
server_socket.bind((host, puerto))

# Esperar a que el cliente se conecte
server_socket.listen(1)
print(f"El servidor está escuchando en {host}:{puerto}")

# Aceptar la conexión entrante
cliente_socket, direccion_cliente = server_socket.accept()
print(f"Conexión entrante desde {direccion_cliente}")

while True:
    # Recibir datos del cliente
    datos_recibidos = cliente_socket.recv(1024)
    if not datos_recibidos:
        break

    print(f"Cliente: {datos_recibidos.decode()}")

    # Enviar una respuesta al cliente
    respuesta = input("Servidor: ")
    cliente_socket.send(respuesta.encode())

# Cerrar la conexión
cliente_socket.close()
server_socket.close()

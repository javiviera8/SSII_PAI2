#!/usr/bin/env python
# -*- coding: UTF8 -*-
#Variables
host = 'localhost'
port = 8050
clave="1234"
#Se importa el módulo
import socket
import hmac
import hashlib
import time
 
#Creación de un objeto socket (lado cliente)
obj = socket.socket()
 
#Conexión con el servidor. Parametros: IP (puede ser del tipo 192.168.1.1 o localhost), Puerto
obj.connect((host, port))
print("Conectado al servidor")
 
#Creamos un bucle para retener la conexion
while True:
    #Instanciamos una entrada de datos para que el cliente pueda enviar mensajes
    mens = raw_input("Mensaje desde Cliente a Servidor >> ")
    mens = "La fecha y hora de envio: " + time.strftime("%d/%m/%y") + " " + time.strftime("%H:%M:%S")+ ": " + mens
    
    cifrado = hmac.new(bytes(clave),bytes(mens),hashlib.sha512,)


    mensCifrado = cifrado.hexdigest()
    
    cadenaFinal= mensCifrado + mens
 
    #Con el método send, enviamos el mensaje
    obj.send(cadenaFinal)

#Cerramos la instancia del objeto servidor
obj.close()

#Imprimimos la palabra Adios para cuando se cierre la conexion
print("Conexión cerrada")

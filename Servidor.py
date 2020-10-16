#!/usr/bin/env python
# -*- coding: UTF8 -*-
#Se importa el módulo
import socket
import hmac
import hashlib
#FUNCIONES

def hmacIguales(hmacRecibida, mensaje, clave):
    
    cifrado = hmac.new(bytes(clave),bytes(mensaje),hashlib.sha512,)
    
    mensCifrado = cifrado.hexdigest()
   
    
    result=""
    
    if (hmacRecibida == mensCifrado):
        result = "La integridad es correcta"
    else:
        result = "La integridad no es correcta"
    return result

def escribeFechaHora(fechaHora, nombreFichero):
    f = open (nombreFichero, "a")
    f.write(fechaHora + "\n")
    f.close()


def compruebaRepply(fechaHora, nombreFichero):
    f = open (nombreFichero)
    
    lista= []
    for linea in f:
        lista.append(linea[0:len(linea)-1])
    
    f.close()
    result=""
    #print lista
    
    for i in range(len(lista)):
        #print lista[i]
        if(fechaHora == lista[i]):
            result="ES UN REPPLY!!!"
            break
           
        else:
            result="No es un repply"
    
  
    return result

        
#instanciamos un objeto para trabajar con el socket
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Instanciar aqui la clave
clave="1234"
 
#Puerto y servidor que debe escuchar
ser.bind(("", 8050))
 
#Aceptamos conexiones entrantes con el metodo listen. Por parámetro las conexiones simutáneas.
ser.listen(1)
 
#Instanciamos un objeto cli (socket cliente) para recibir datos
cli, addr = ser.accept()

while True:

    #Recibimos el mensaje, con el metodo recv recibimos datos. Por parametro la cantidad de bytes para recibir
    recibido = cli.recv(1024)

    #Si se reciben datos nos muestra la IP y el mensaje recibido
    #pruebaRep= "La fecha y hora de envio: 27/10/19 02:10:10"
    #print "Mi hmac es " + recibido[0:128]
    print "Recibido: " + recibido[128:len(recibido)]
    print "Recibo conexion de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1])
    
    verificacion= hmacIguales(recibido[0:128],recibido[128:len(recibido)],clave)
    
    print  verificacion
   
    print compruebaRepply(recibido[128:171],"Registro.txt")
    #print compruebaRepply(pruebaRep,"Registro.txt")
    
    escribeFechaHora(recibido[128:171],"Registro.txt")
   

    #Devolvemos el mensaje al cliente
    cli.send(recibido)

#Cerramos la instancia del socket cliente y servidor
cli.close()
ser.close()

print("Conexiones cerradas")


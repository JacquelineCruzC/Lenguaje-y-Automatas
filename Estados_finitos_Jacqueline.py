
# -*- coding: utf-8 -*-
"""Cruz Campos Jacqueline Adriana.
Ejecutar un programa informatico en Python, que ejecute la implementacion dde un automata finito
"""
import sys
import winsound
from time import sleep
from random import randint

#Variable púlica y global
estado = 'i'

def progreso(veces,frecuencia,duracion):
    """imprime asteriscos en progreso"""
    for i in range(1,veces+1):
        if i <= veces:
            print(' * ',end="")
            winsound.Beep(frecuencia, duracion)  # 1000 Hz, duración de 500 ms
            
    print("\n")

#Estado inicial
def EDOi(entrada): #lee
    global estado
    sleep(2)
    if entrada == "":
        print("Gracias por comunicarse.")
        estado = 'f'
    elif entrada == "#":
        estado = 'i'
    elif entrada == "0":
        estado = 0
    elif entrada == "1":
        estado = 1
    elif entrada == "2":
        estado = 2
    elif entrada == "3":
        estado = 3
    else:
        print("Gracias por comunicarse.")
        estado = 'f'

        
#define estados
def EDO0(entrada):
    global estado
    #Transiciones
    progreso(5, 1000, 300)
    opc=int(input("Para conocer los planes de internet tenemos varias opciones.\n1  Planes con telefonia e internet \n2  Planes con solo internet \n3  Planes con solo telefonia\nSeleccione la opcion\n"))
        
    if opc==1:
        print("Nuestros planes van desde 299 a 899 dependiendo de la velocidad del internet que quiera y su telefonia se le proporcionara un numero telefonico")
    elif opc==2:
        print("Los planes con solo internet van desde 199 a 499 dependiendo de la velocidad que quiera")
    elif opc==3:
        print("Se le proporcionara un modem donde el aparato telefonico ira conectado")
    else:
        print("Ingreso un numero incorrecto")
    estado='f'
       
           
        
def EDO1(entrada):
    global estado
    #print('Estado: uno', "entrada:",entrada,"estado:",estado)
    #Transiciones
    des=input("Usted tiene problemas con el internet o cableado. Por favor describanos su problema.\n")
    print("------------------------------------------------------------------------------------")
    print(des+"\nEspere a que se cree un numero de orden y en breve se le atendera por WhatsApp")
    print("------------------------------------------------------------------------------------")
    progreso(5, 1000, 300)
    estado='f'

def EDO2(entrada):
    global estado
    #print('Estado: dos', "entrada:",entrada,"estado:",estado)
    #Transiciones
    sleep(2) 
    print("Por favor, ayudame a contestar este breve cuestionario")
    dir=input("Ingrese su direccion:\n")
    tel=int(input("Ingrese su numero de telefono\n"))
    desc=input("Describanos de nuevo cual es su problema con su instalacion\n")
    progreso(5, 1000, 300)
    estado='f'

def EDO3(entrada):
    global estado
    #print('Estado: tres', "entrada:",entrada,"estado:",estado)
    #Transiciones
    
    print("En breve sera atendido por un asistente tecnico, por favor espere")
    progreso(5, 1000, 300)
    print( "---------------------------- por favor espere\n Finalizo la llamada")
    estado='f'
        
   
#Finite State Machine (FSM)   
def FSM(entrada):
    """gestor de estados"""
    global estado
    #print(type(estado))
    switch = {
       'i':EDOi,#define condiciones iniciales
        0 :EDO0,#
        1 :EDO1,#
        2 :EDO2,#
        3 :EDO3#            
    }
    
    func = switch.get(estado, lambda: None)
    return func(entrada)

def main()->int:
    global estado
    estado='i'
    print("================================================")
    print("Bienvenido a asistente telefonico Telmex\n Seleccione una opción: \n0  Quiere conocer de planes de internet y nuevos paquetes. \n1  Problemas con su internet o cableado. \n2  Si su falla no ha sido atendida. \n3  Hablar con un tecnico.\nPresione cualquier otra letra o numero para salir ")
    print("================================================")

    while estado != 'f':
        entrada = input("Seleccione una opción: ")
        FSM(entrada)

    print("Finalizo la llamada. Fue un gusto atenderle, espero haber resolvido sus dudas.")
    return 0

if __name__ == '__main__':
    try:
        while True:
            main()  # Ejecuta una llamada
            input("\nPresione ENTER para realizar otra llamada o Ctrl+C para salir.\n")
    except KeyboardInterrupt:
        print("\nGracias por utilizar el asistente telefonico")
        sys.exit(0)
    

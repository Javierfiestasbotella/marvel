import os
import getpass import io
with open('marvel\\secreto.cfg','r') as secreto:
    usuario = secreto.readline().strip()
    password = secreto.readline().strip()

intentos=-1
while intentos==-1:
    user=input('Escribe usuario: ')
    if user!=usuario:
        print('Usuario no existe')
    else:
        intentos=0
        paswd=getpass.getpass('Introduce contraseña: ')
        while intentos>=0:
            if paswd!=password and intentos<=3:
                print('Contraseña erronea')
                intentos+=1
                print(f'{intentos=}')
                user=usuario
                paswd=getpass.getpass('Introduce contraseña: ')
            elif paswd!=password and intentos>3:
                print('Demasiados intentos, activando grabacion y envio a Policía Nacional')
                break
            else:
                print(f'Bienvenido {user}')
                intentos=-2
                
        

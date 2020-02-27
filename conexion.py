import os
hostname = "www.itmorelia.edu.mx"

respuesta = os.system("ping -c 1 " + hostname)

if respuesta ==0:
    print (hostname + ": esta funcionamiento!")
else:
    print (hostname + ": NO funciona!")

#deteccion de computadoras

red= "192.168.0.0/24"
os.system("nmap -sP "+red)

#deteccion de puertos abiertos
computadora="192.168.0.6"
os.system("nmap -sT "+computadora)

#Detectar sistema operativo
os.system("nmap -O "+computadora)
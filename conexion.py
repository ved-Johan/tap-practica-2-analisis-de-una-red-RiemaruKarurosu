import os
red= "200.33.71.0/24"
hostname = red

respuesta = os.system("ping -c 1 " + hostname)

if respuesta ==0:
    print (hostname + ": esta funcionamiento!")
else:
    print (hostname + ": NO funciona!")

#deteccion de computadoras

red= "200.33.71.0/24"
os.system("nmap -sP "+red)

#deteccion de puertos abiertos
computadora=red
os.system("nmap -sT "+computadora)

#Detectar sistema operativo
os.system("nmap -O "+computadora)
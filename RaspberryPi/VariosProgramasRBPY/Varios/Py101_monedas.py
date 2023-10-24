# -*- coding: cp1252 -*-
#------------------------------------------------------------------------
#Programa...: Py101_monedas.py
#Autor......: Enrique Rodriguez
#Descripción: Pide el numero de monedas que llevo
#------------------------------------------------------------------------
import time 

print("------------------------------")
print("Programa...: Py101_monedas.py")
print("Autor......: Enrique Rodriguez")
print("-------------------------------")


m_euro   = int(input("Monedas de Euro..: "))
m_10cent = int(input("Monedas de 10cent: "))

total_monedas = m_euro + m_10cent
total_cent = m_euro*100 + m_10cent

time.sleep(1)
print("Total Monedas....: " +str(total_monedas) +" monedas de euro")
print("Total Centimos...: " +   str(total_cent) +" monedas de centimos")

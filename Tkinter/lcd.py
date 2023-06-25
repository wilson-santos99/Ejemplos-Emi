"""
Autor original de la biblioteca I2C LCD 16x2
Usuario de Github: T-622
Version: 1.0.0
Fuente: https://github.com/T-622/RPI-PICO-I2C-LCD.git

Autor del codigo: Cadena Campos Luis
Fecha de creacion: 01/11/2022
Version de codigo: 1.0.0
Correo:luis14oriente@gmail.com

""" 
#Traemos nuestras bibliotecas
from machine import Pin,I2C,ADC
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import time

#Indicamos la direccion del i2c
I2C_ADDR   = 0x27
#Declaramos el numero de renglones y columnas
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
#Se declaran los pins que se usaran para el I2C
i2c = I2C(0,sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c,I2C_ADDR,I2C_NUM_ROWS,I2C_NUM_COLS)

#Declaramos el pin del ADC con el que trabajaremos
lm35 = ADC(Pin(28))
# 3.3 voltios entre 65535 porque usaremos 2^16 
conversion = 3.3/65535

while True:
    #Leemos la temperatura con un voltaje de 16 bits
    temperatura_voltaje = lm35.read_u16()
    #Hacemos una multiplicacion para obtener una conversion de voltaje
    conversion_voltaje = temperatura_voltaje*conversion
    centigrados = conversion_voltaje/(10.0 / 1000)
    #Escribimos los valores en el LCD
    lcd.clear()
    lcd.move_to(0,0)
    #Escribimos el texto "Temperatura"
    lcd.putstr("Temperatura: ")
    lcd.move_to(0,1)
    lcd.putstr(str(centigrados))
    #Actualizamos el valor cada 2 segundos
    time.sleep(2)
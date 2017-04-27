#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import json
import time
import os
import MySQLdb
import ast
import datetime


def run_query(query=''):
    estacion = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", db="estacion")
    cursor = estacion.cursor()
    cursor.execute(query)

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()  # Traer los resultados de un select
    else:
        estacion.commit()  # Hacer efectiva la escritura de datos
        data = None

    cursor.close()  # Cerrar el cursor
    estacion.close()  # Cerrar la conexión

    return data





#ADMINISTRADOR
def menu_2():
    lista = ["BIENVENIDO COMO ADMINISTRADOR ","Estacion Gasolina ", "1. Alertas", "2. Gasolina",
             "3. Ventas", "4. Usuarios",
             "5. Log Usuarios", "Salir"]
    cadena = json.dumps(lista)
    return cadena

def menu_gasolina():
    lista = ["1. Tipos de Gasolina", "2. Agregar Gasolina",
             "3. Actualizar Tipo gasolina"]
    cadena = json.dumps(lista)
    return cadena

def nueva_gasolina():
    lista = ["Ingrese Nuevo Tipo Gasolina y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def precio_gaso():
    lista = ["Ingrese el Precio de la Gasolina>>"]
    cadena = json.dumps(lista)
    return cadena


def ingre_gasolina(gasolina, precio):
    query = "INSERT INTO gasolina(nombre_gasolina, precio_gasolina) VALUES ('%s','%s')" % (gasolina, precio)
    run_query(query)
    lista = ["Tanqueo Listo"]
    cadena = json.dumps(lista)
    return cadena


def nueva_act():
    lista = ["Ingrese el Tipo de gasolina a Actualizar >>"]
    cadena = json.dumps(lista)
    return cadena

def nueva_gaso():
    lista = ["Ingrese el tipo de Gasolina Actualizado >>"]
    cadena = json.dumps(lista)
    return cadena

def actualizar_gasolina(act, actualizada):
    query = "UPDATE gasolina SET nombre_gasolina ='%s',precio_gasolina='%s'  WHERE id_gasolina =%i" % (act, actualizada, int(id_gasolina))
    run_query(query)
    lista = ["Tipo Gasolina Actualizada Correctamente, Presione enter >>"]
    cadena = json.dumps(lista)
    return cadena




def menu_ventas():
    lista = ["1. Listado Facturas", "2. Detalle Facturas",
             "3. Total Ventas Del Dia"]
    cadena = json.dumps(lista)
    return cadena

def menu_usuarios():
    lista = ["1. Listado Usuarios", "2. Listado Usuario Por Puntos"]
    cadena = json.dumps(lista)
    return cadena

def ver_usuarios():
    query = "SELECT nombre, identificacion FROM usuarios"
    result = run_query(query)
    cadena = json.dumps(result)
    lista = json.loads(cadena)
    for i in lista:
        print i

def fact(tabla):
    query = "create table ('%s') (Nombre varchar(20),identificacion varchar(20),tipo_gasolina varchar(20),cantidad int(20),puntos int(20),total int (20))" %tabla
    run_query(query)
    lista = ["factura Creada por USuario"]
    cadena = json.dumps(lista)
    return cadena


def ver_usuarios_puntos():
    query = "SELECT * FROM usuarios"
    result = run_query(query)
    cadena = json.dumps(result)
    lista = json.loads(cadena)
    for i in lista:
        print i

def ing_usu( nombre,identificacion):
    query = "INSERT INTO usuarios(nombre, identificacion) VALUES ('%s','%s')" % (nombre,identificacion)
    run_query(query)
    lista = ["usuario Ingresado"]
    cadena = json.dumps(lista)
    return cadena

def menu_log_usuarios():
    lista = ["1. Reportes"]
    cadena = json.dumps(lista)
    return cadena


def menu_puntos():
    lista = ["Puntos", "1. Ver Puntos", "2. Cambiar Puntos * Productos"]
    cadena = json.dumps(lista)
    return cadena


#CLIENTE

def menu_1():
    lista = ["BIENVENIDO COMO CLIENTE","Estacion", "1. Comprar Gasolina", "2. Puntos",
             "3. factura", "4. Salir"]
    cadena = json.dumps(lista)
    return cadena


def menu_comprar_gasolina():
    lista = ["1. Tipos de Gasolina", "2. Cantidad a Tanquear", "3. Generar Factura", "4. Pagar"]
    cadena = json.dumps(lista)
    return cadena

def ver_tipogasolina():
    query = "SELECT * FROM gasolina"
    result = run_query(query)
    cadena = json.dumps(result)
    lista = json.loads(cadena)
    for i in lista:
        print i

def pedir_cantidad_gasolina():
    lista = ["Ingrese la Cantidad a Tanquear >>"]
    cadena = json.dumps(lista)
    return cadena

def pedir_tipo_gasolina():
    lista = ["Ingrese el tipo de gasolina >>"]
    cadena = json.dumps(lista)
    return cadena

def cant_gasolina(dato, gas, nombre,identificacion):
    query = "INSERT INTO factura(cantidad, tipo_gasolina,nombre,identificacion) VALUES ('%s','%s','%s','%s')" % (dato, gas,nombre,identificacion)
    run_query(query)
    lista = ["Tanqueo Listo"]
    cadena = json.dumps(lista)
    return cadena


def pedir_nombre():
    lista = ["Ingrese Nombre >>"]
    cadena = json.dumps(lista)
    return cadena

def pedir_ident():
    lista = ["Ingrese Numero de Identificacion >>"]
    cadena = json.dumps(lista)
    return cadena


def ing_nombre(nombre):
    query = "INSERT INTO factura(nombre) VALUES ('%s')" % nombre
    run_query(query)
    lista = ["factura Creada >>"]
    cadena = json.dumps(lista)
    return cadena

def pedir_nombre_fact():
    lista = ["Ingrese Nombre de la factura >>"]
    cadena = json.dumps(lista)
    return cadena

def genera_factura():
    query = "SELECT * FROM factura"
    result = run_query(query)
    cadena = json.dumps(result)
    lista = json.loads(cadena)
    for i in lista:
        print i


def menu_factura():
    lista = ["1.Ver Listado Facturas", "2. Detalles de las Facturas", "Elija la opcion >>"]
    cadena = json.dumps(lista)
    return cadena


def pedir_dinero():
    lista = ["Ingrese Monto a tanquear y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena


def pago_gasolina():
    lista = ["Ingrese Valor del Billete y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena


def pagar_gasolina(numero1, numero2):
    resultado = numero2-numero1
    lista = ["Dinero Entregado :           " + str(numero2) +'\n'+
             "Valor a Tanquear :           " + str(numero1) + '\n' +
             "Devolucion al  Cliente:      " + str(resultado)]
    cadena = json.dumps(lista)
    return cadena



def imprimir(cadena):
    lista = json.loads(cadena)
    for i in lista:
        #print i
        print ast.literal_eval(json.dumps(i))

def iniciar_sesion():
    pass


def usuarios():
    lista = ["INGRESE CORREO ELECTRONICO>>"]
    cadena = json.dumps(lista)
    return cadena

def validar_usuario1(cadena):
    if(cadena == "a"):
        return True

    elif (cadena == "p"):
        return False

def validar_usuario(cadena):
    x = [[cadena]]
    query = "SELECT correo FROM usuarios WHERE correo = '%s'" % cadena
    result = run_query(query)
    user = json.dumps(x)
    y = json.dumps(result)
    if(y == user):
        creartxt()
        archivo = open('archivos.txt', 'a')
        fecha = time.strftime("%x")
        hora = time.strftime("%X")
        archivo.write("Usuario " + cadena + '\n')
        #archivo.write("Ip " + str(ip) + '\n')
        archivo.write("Fecha " + fecha + '\n')
        archivo.write("Hora " + hora + '\n')
        archivo.close()
        return True

    else:
        creartxt()
        archivo = open('archivoss.txt', 'a')
        fecha = time.strftime("%x")
        hora = time.strftime("%X")
        archivo.write("Usuario " + cadena + '\n')
       # archivo.write("Ip " + str(ip) + '\n')
        archivo.write("Fecha " + fecha + '\n')
        archivo.write("Hora " + hora + '\n')
        archivo.close()
        return True


def creartxt():
    archivo=open('archivos.txt','w')
    archivo.close()

def contrasena():
    lista = ["Ingrese su contrasena y presione enter >>"]
    k = json.dumps(lista)
    return k

def pedir_usuario():
    lista = ["Ingrese su nombre y presione enter >>"]
    k = json.dumps(lista)
    return k

def validar_contrasena(cliente, cadena):
        x = [[cliente, cadena]]
        query = "SELECT correo,contrasena FROM usuarios WHERE correo = '%s' and contrasena = '%s' " % (cliente, cadena)
        result = run_query(query)
        user = json.dumps(x)
        y = json.dumps(result)
        if (y == user):

            return True
        else:
            return False


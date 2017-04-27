#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import socket, error
from threading import Thread
import funciones
import json


class Cliente(Thread):

    '''funcion que genera hilos'''
    def __init__(self, con, dire):
        Thread.__init__(self)
        self.conexion = con
        self.direccion= dire


    def run(self):
        while True:
            try:
                a=False
                b=False
                while (a!= True):
                    while (b!=True):
                        mensaje_cliente=self.conexion.recv(1024)
                        mensaje_cliente = funciones.validar_usuario1(mensaje_cliente)
                        usuario=mensaje_cliente
                        menu = False
                        b=True
                    while (usuario == True):
                        while (menu != True):
                            mensaje_cliente = funciones.menu_1()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = int(self.conexion.recv(1024))
                            operacion = mensaje_cliente
                            if operacion == 1:
                                mensaje_cliente = funciones.menu_comprar_gasolina()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = int(self.conexion.recv(1024))
                                tipo = mensaje_cliente
                                if tipo == 1:
                                    mensaje_cliente = funciones.ver_tipogasolina()
                                    # self.conexion.send(mensaje_cliente)
                                    # mensaje_cliente = int(self.conexion.recv(1024))

                                if tipo == 2:
                                    mensaje_cliente = funciones.pedir_cantidad_gasolina()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = int(self.conexion.recv(1024))
                                    dato = mensaje_cliente
                                    mensaje_cliente = funciones.pedir_tipo_gasolina()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = str(self.conexion.recv(1024))
                                    gas = mensaje_cliente
                                    mensaje_cliente = funciones.pedir_nombre()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = str(self.conexion.recv(1024))
                                    nombre = mensaje_cliente
                                    mensaje_cliente = funciones.pedir_ident()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = str(self.conexion.recv(1024))
                                    identificacion = mensaje_cliente
                                    # mensaje_cliente = funciones.ing_nombre(nombre)
                                    # self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = funciones.cant_gasolina(dato, gas, nombre, identificacion)
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = funciones.ing_usu(nombre, identificacion)
                                    self.conexion.send(mensaje_cliente)

                                if tipo == 3:
                                    # mensaje_cliente = funciones.pedir_nombre_fact()
                                    # self.conexion.send(mensaje_cliente)
                                    # mensaje_cliente = str(self.conexion.recv(1024))
                                    # tabla = mensaje_cliente
                                    # mensaje_cliente = funciones.fact(tabla)
                                    mensaje_cliente = funciones.genera_factura()
                                    #self.conexion.send(mensaje_cliente)

                                if tipo == 4:
                                    mensaje_cliente = funciones.pedir_dinero()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = int(self.conexion.recv(1024))
                                    numero1 = mensaje_cliente
                                    mensaje_cliente = funciones.pago_gasolina()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = int(self.conexion.recv(1024))
                                    numero2 = mensaje_cliente
                                    mensaje_cliente = funciones.pagar_gasolina(numero1, numero2)
                                    self.conexion.send(mensaje_cliente)

                            if operacion == 3:
                                mensaje_cliente = funciones.menu_factura()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = int(self.conexion.recv(1024))
                                tipo2 = mensaje_cliente



                            if operacion == 7:
                                  pass

 # A D M I N I S T R A D O r
                    menu_1 = False
                    while (menu_1 != True):
                        mensaje_cliente = funciones.menu_2()
                        self.conexion.send(mensaje_cliente)
                        mensaje_cliente = int(self.conexion.recv(1024))
                        operacion = mensaje_cliente

                        if operacion == 1:
                                mensaje_cliente = funciones.alertas()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = int(self.conexion.recv(1024))
                                dato = mensaje_cliente

                        if operacion == 2:
                                mensaje_cliente = funciones.menu_gasolina()
                                self.conexion.send(mensaje_cliente)
                                mensaje_cliente = int(self.conexion.recv(1024))
                                dato4 = mensaje_cliente

                                if dato4 == 1:
                                    mensaje_cliente = funciones.ver_tipogasolina()
                                    self.conexion.send(mensaje_cliente)

                                if dato4 == 2:
                                    mensaje_cliente = funciones.nueva_gasolina()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = str(self.conexion.recv(1024))
                                    gasolina = mensaje_cliente
                                    mensaje_cliente = funciones.precio_gaso()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = int(self.conexion.recv(1024))
                                    precio = mensaje_cliente
                                    mensaje_cliente = funciones.ingre_gasolina(gasolina, precio)
                                    self.conexion.send(mensaje_cliente)
                                    # mensaje_cliente = (self.conexion.recv(1024))
                                if dato4 == 3:
                                    mensaje_cliente = funciones.nueva_act()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = str(self.conexion.recv(1024))
                                    act = mensaje_cliente
                                    mensaje_cliente = funciones.nueva_gaso()
                                    self.conexion.send(mensaje_cliente)
                                    mensaje_cliente = str(self.conexion.recv(1024))
                                    actualizada = mensaje_cliente
                                    mensaje_cliente = funciones.actualizar_gasolina(act, actualizada)
                                    self.conexion.send(mensaje_cliente)

                        if operacion == 3:
                            mensaje_cliente = funciones.menu_ventas()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = int(self.conexion.recv(1024))
                            dato5 = mensaje_cliente

                        if operacion == 4:
                            mensaje_cliente = funciones.menu_usuarios()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = int(self.conexion.recv(1024))
                            dato6 = mensaje_cliente

                            if dato6 == 1:
                                mensaje_cliente = funciones.ver_usuarios()
                                # self.conexion.send(mensaje_cliente)
                            if dato6 == 2:
                                mensaje_cliente = funciones.ver_usuarios_puntos()

                        if operacion == 5:
                            mensaje_cliente = funciones.menu_log_usuarios()
                            self.conexion.send(mensaje_cliente)
                            mensaje_cliente = int(self.conexion.recv(1024))
                            dato7 = mensaje_clientes




                            # mensaje_cliente = funciones_servidor2.getnum_2()
                            # self.conexion.send(mensaje_cliente)

                        if operacion == 4:
                            pass
                            # mensaje_cliente = funciones_servidor2.usuarios()
                            # self.conexion.send(mensaje_cliente)
                            # mensaje_cliente = self.conexion.recv(1024)
                            # menu_1 = True
                            # usuario=True
                            # menu= False

            except error:
                print("[%s] Error de lectura " % self.name)
                break

            else:
                if mensaje_cliente:
                        self.conexion.send(mensaje_cliente)


def main():
    server = socket()
    server.bind(("localhost", 80))
    server.listen(1)

    while True:
        con, dire = server.accept()
        hilo = Cliente(con, dire)
        hilo.start()
        print("conexion de %s:%d " % dire)
        # hilo =Thread(target=funciones_servidor2.menu,args=())
        # hilo.start()


if __name__ == '__main__':
    main()

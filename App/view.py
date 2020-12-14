"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import config
from App import controller
from DISClib.DataStructures import listiterator as it

import timeit
assert config   

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________

service_file = "taxi-trips-wrvz-psew-subset-"
recursionLimit = 20000

# ___________________________________________________
#  Funciones para imprimir la información
# ___________________________________________________

def printOptionTwo(cont):
    """
    Imprime la carga de datos.
    """
    print('\nSe cargaron con éxito los datos.')

def printOptionThree(info,criteria1,criteria2):
    """
    Proyecto Final | Req 1
    Imprime la infomación sobre las compañías.
    """
    NumCabs, NumCompanies, TOPNumCabs, TOPNumServices = info
    
    print("\nNúmero total de compañías con al menos un taxi inscrito: " + str(NumCompanies) + ".")
    iterator = it.newIterator(TOPNumCabs)
    print("\nTOP "+str(criteria1) + " de compañías con más taxis afiliados.")
    while it.hasNext(iterator):
        company = it.next(iterator)
        print('Compañía: ' + str(company['key']) + '    Número de taxis afiliados: '+ str(company['value']['NumCabs']) + "." )


    print("\nNúmero total de taxis en los servicios reportados: "+ str(NumCabs) +".")
    iterator2 = it.newIterator(TOPNumServices)
    print("\nTOP "+str(criteria2) + " de compañías con más servicios prestados.")
    while it.hasNext(iterator2):
        company = it.next(iterator2)
        print('Compañía: ' + str(company['key']) + '    Número de servicios prestados: '+ str(company['value']['NumServices']) + "." )
    


# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información del Sistema de Taxis de Chicago.")
    print("3- Requerimento 1: Reporte de Información Compañias y Taxis.")
    print("4- Requerimento 2: Sistema de Puntos y Premios.")
    print("5- Requerimento 3: Mejor horario Community Areas.")

    print("0- Salir")
    print("*******************************************")

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')   

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # catalog es el controlador que se usará de acá en adelante
        catalog = controller.init()

    elif int(inputs[0]) == 2:
        
        size = input("Elija el tamaño del archivo CSV que quiere cargar (small,medium,large): ")
        print("\nCargando información sistema de Taxis Chicago ...")
        controller.loadTrips(catalog,service_file,size)
        printOptionTwo(catalog)
       
    elif int(inputs[0]) == 3:
        print("\nRequerimiento No. 1 del Proyecto Final: ")
        criteria1 = int(input('\nIngrese el número de compañías que quiere ver en el TOP más taxis inscritos: '))
        criteria2 = int(input('\nIngrese el número de compañías que quiere ver en el TOP más servicios prestados: '))
        info = controller.CompaniesInfo(catalog,criteria1,criteria2)
        printOptionThree(info,criteria1,criteria2)

    elif int(inputs[0] ==4):
        print("\nRequerimiento No. 2 del Proyecto Final: ")


    else:
        sys.exit(0)
sys.exit(0)


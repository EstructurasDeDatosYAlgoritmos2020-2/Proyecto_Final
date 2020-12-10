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

import config as cf
import os
from App import model
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def init():
    """
    Llama la funcion de inicialización  del modelo.
    """
    analyzer = model.newAnalyzer()
    return analyzer

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadTrips(catalog,taxis_file,size):
    """
    Se carga el archivo CSV solicitado por el usuario.

    Llama a la función en model para contar 
    el total de viajes en Taxi realizados.
    """

    tripsfile = taxis_file + size + '.csv'
    tripfile = cf.data_dir + tripsfile
    input_file = csv.DictReader(open(tripfile,encoding ="utf-8"),delimiter=",")

    num_trips = 0
    for trip in input_file:
        model.AddCabTrip(catalog,trip)
        num_trips = num_trips + 1
    model.addNumTripsToTotal(catalog,num_trips)  
# ___________________________________________________
#  Funciones para consultas de requerimientos
# ___________________________________________________

def CompaniesInfo(catalog,criteria1,criteria2):
    """
    Proyecto Final | Req 1 
    Llama a la función en model que retorna
    información general sobre las compañías.
    """
    return model.CompaniesInfo(catalog,criteria1,criteria2)


# ___________________________________________________
#  Funciones para consultas generales
# ___________________________________________________

def numStations(citibike):
    """
    Llama la función en model que retorna
    el número de estaciones (vértices).
    """
    return model.numStations(citibike)

def numConnections(citibike):
    """
    Llama la función en model que retorna
    el número de conexiones (arcos) entres
    estaciones.
    """
    return model.numConnections(citibike)


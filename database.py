"""
 * Crea un programa que simule el mecanismo de participación:
 * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
 *   participantes, mostrarlos, lanzar el sorteo o salir.
 * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
 * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
 *   (Y no lo duplicarás)
 * - Si seleccionas mostrar los participantes, se listarán todos.
 * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
 *   (Avisando de si lo has eliminado o el nombre no existe)
 * - Si seleccionas realizar el sorteo, elegirás una persona al azar 
 *   y se eliminará del listado.
 * - Si seleccionas salir, el programa finalizará.
"""

########################
import random
########################

def mostrar_menu():
  print("----------------------")
  print("1. Añadir Participante")
  print("2. Borrar Participante")
  print("3. Mostrar Participantes")
  print("4. Lanzar Sorteo !")
  print("5. Salir del programa")
  print("----------------------")

lista_participantes = []

#===================================================

def añadir():
  participante = str(input("Ingrese nombre del participante: "))
  lista_participantes.append(participante)
  print("¿Quiere agregar otro participante? - S/N")
  respuesta = str(input("Ingrese respuesta: "))
  if respuesta.upper() == "S":
    añadir()

#===================================================

def borrar():
  delete = str(input("Ingrese nombre del participante: "))
  if delete in lista_participantes:
    lista_participantes.remove(delete)
    print("Participante Borrado correctamente !")
  else:
    print(f"El Participante {delete} no esta en la lista")

#===================================================

def mostrar():
  print(f"Lista de participantes completa:{lista_participantes}")

#===================================================

def sorteo():
  mi_lista = lista_participantes
  elemento_seleccionado = random.choice(mi_lista)
  print("Ganador del sorteo:", elemento_seleccionado)

#===================================================

while True:
  mostrar_menu()

  opcion = input("Seleccione Opcion (1-5) > ")

  if opcion == "1":
    añadir()
  elif opcion == "2":
    borrar()
  elif opcion == "3":
    mostrar()
  elif opcion == "4":
    sorteo()
  elif opcion == "5":
    print("Saliendo del programa")
    break
  else:
    print("Opcion no valida")
    
########################
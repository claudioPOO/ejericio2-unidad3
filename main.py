import os

from claseManejadorSabor import ManejaSabores
from claseManejadorHelado import ManejaHelado

from claseMenu import Menu

if __name__ == '__main__':
   
    sabores=ManejaSabores()
    sabores.cargarSabores()
    helados=ManejaHelado()
    os.system('cls')
    menu = Menu()
    salir = False
    while not salir:
        print("\n------------Menu------------\n1. Inciso 1\n2. Inciso 2\n3. Inciso3\n4 Inciso4\n0. Salir")
        op = int(input('Ingrese una opcion: '))
        os.system('cls')
        menu.opcion(op,sabores,helados)
        salir = op == 0
    

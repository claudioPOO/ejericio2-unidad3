import  os
class Menu :
    __switcher = None
    def  __init__ ( self ):
        self.__switcher  = { 1 : self.opcion1 ,
                            2 : self. opcion2 ,
                            3: self. opcion3,
                            4 : self .opcion4,
                            5: self.opcion5,
                            0: self. salir
                         }
    def  getSwitcher ( self ):
        return self. __switcher
    def  opcion ( self , op , sabores,helados ):
        func = self . __switcher . get ( op , lambda : print ( "Opción no válida" ))
        func ( sabores,helados )
    def  salir ( self,sabores,helados):
        print ( 'Salir' )
    def  opcion1 (self, sabores,helados):
        helados.cargarPedido(sabores)
        print('PEDIDOS  |')
        print('        \/')
        helados.mostrarPedidos()
    def  opcion2 ( self , sabores,helados ):
        ls=sabores.GuardarLista()
        print(ls)
        print('-------HELADOS MAS VENDIDOS-------\n')
        sabores.ordena(ls)
       
        
    def opcion3(self,sabores,helados):
        sabor=int(input('Numero sabor para conocer total de gramos'))
        total=int(helados.buscaporNumero(sabor))
        print('Total de gramos vendidos {} Gr'.format(total))
    def opcion4(self,sabores,helados):
        tipoHelado=int(input('Tipo de helado (gr) '))
        print('Sabores Vendidos En {} Gramos'.format(tipoHelado))
        helados.BuscaGR(tp)
    def opcion5(self,sabores,helados):##comprueba si es agregacion o composicion
        p=int(input('Pedido a borrar '))
        helados.__del__(p-1)
        sabores.MostrarSabores()
        helados.mostrarPedidos()
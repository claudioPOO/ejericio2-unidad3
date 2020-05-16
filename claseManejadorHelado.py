from claseHelado import Helado
from claseSabor import Sabor
class ManejaHelado:
    __pedido=[]
    def __init__(self):
        self.__pedido=[]
    def cargarPedido(self,sabores):
        i=0
        print('Carga de pedidos(finalice con 0)-------')
        pedido=int(input('Numero de pedido: '))
        while(pedido!=0):
            gramos=int(input('Gramos del helado: '))
            unHelado=Helado(gramos)
            self.__pedido.append(unHelado)
            sabor=str(input('Sabores: (termine con nada) '))
            while(sabor!='nada'):
                sa=sabores.buscaSabor(sabor)
                if(sa!=0):
                    self.__pedido[i].agregarSabor(sa)
                    sabores.buscas(sabor)
                else:
                    print('Sabor no encontrado')
                sabor=str(input('Sabores: (termine con nada) '))
            i=i+1
            pedido=int(input('Numero de pedido: '))
            
    def mostrarPedidos(self):
        for i in range(len(self.__pedido)):
            print(self.__pedido[i].getGramos())
     
    def Particion(self):
        i=0
        while(i<len(self.__pedido)):
            cant=self.__pedido[i].cGramos()
            sab=self.__pedido[i].cSabores()
            total=cant/sab
            self.__pedido[i].setGramosxS(total)
            i=i+1
    def buscapN(self,numero):
        i=0
        total=0
        while(i<len(self.__pedido)):
            gr=int(self.__pedido[i].Buscaxn(numero))
            total=total+gr
            i=i+1
        return total    
    def BuscaGR(self,gr):
        i=0
        while(i<len(self.__pedido)):
            
            if(self.__pedido[i].cGramos()==int(gr)):
                print('Pedido Nro: {}'.format(i+1))
                self.__pedido[i].getGramos()
            i=i+1
    def __del__(self,i):
        print('Borrando pedido nro {}...'.format(i+1)) 
        del self.__pedido[i]
        print('Pedido Borrado')          
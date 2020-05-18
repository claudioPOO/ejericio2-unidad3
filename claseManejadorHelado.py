from claseHelado import Helado
from claseSabor import Sabor
class ManejaHelado:
    __pedido=[]
    def __init__(self):
        self.__pedido=[]
    def cargarPedido(self,sabores):
        i=len(self.__pedido)
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
                else:
                    print('Sabor no encontrado')
                sabor=str(input('Sabores: (termine con nada) '))
            i=i+1
            pedido=int(input('Numero de pedido: '))
            
    def mostrarPedidos(self):
        for i in range(len(self.__pedido)):
            print(self.__pedido[i].getGramos())
     
    def buscaporNumero(self,numero):
        i=0
        gramosVendidos=0
        while(i<len(self.__pedido)):
            total=0
            if(int(self.__pedido[i].Buscaxnumero(numero)==1)):
                cant=self.__pedido[i].cGramos()
                sab=self.__pedido[i].cSabores()
                total=cant/sab
                gramosVendidos=gramosVendidos+total
            i=i+1
        return gramosVendidos 
    def BuscaGR(self,gr):
        i=0
        while(i<len(self.__pedido)):
            if(self.__pedido[i].cGramos()==int(gr)):
                self.__pedido[i].getGramos()
            i=i+1
    def __del__(self,pedido):
        print('Borrando pedido nro {}...'.format(pedido+1)) 
        del self.__pedido[pedido]
        print('Pedido Borrado')          
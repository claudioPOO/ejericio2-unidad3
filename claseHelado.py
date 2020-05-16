from claseSabor import Sabor

class Helado:
    __gramos=0
    __sabores=[]
    __gramosxsabor=0
    def __init__(self,gramos,gxs=0):
        self.__gramos=int(gramos)
        self.__sabores=[]
        self.__gramosxsabor=int(gxs)
    def agregarSabor(self,sabor):
        self.__sabores.append(sabor)
    def getGramos(self):
        print('GRAMOS: {}'.format(self.__gramos))
        for i in range(len(self.__sabores)):
            print(self.__sabores[i].mostrarD())
    def setGramosxS(self,cant):
        self.__gramosxsabor=int(cant)
    def cGramos(self):
        return self.__gramos
    def cSabores(self):
        s=len(self.__sabores)
        return s            
    def Buscaxn(self,numero):
        i=0
        band=0
        while(i<len(self.__sabores))and band==0:
            if(int(numero)==self.__sabores[i].getN()):
                band=1
            else:
                i=i+1
        if(band==1):
            return self.__gramosxsabor
        else:
            return 0
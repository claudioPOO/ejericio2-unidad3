from claseSabor import Sabor
import csv
class ManejaSabores:
    __Sabores=[]
    def __init__(self):
        self.__Sabores=[]
    def cargarSabores(self):
        sab=open('Sabores.csv')
        r=csv.reader(sab,delimiter=';')
        for fila in r:
            Unsabor=Sabor(fila[0],fila[1],fila[2])
            self.__Sabores.append(Unsabor)
        sab.close()    
    def MostrarSabores(self):
        for i in range(len(self.__Sabores)):
            print(self.__Sabores[i].mostrarD())
    def buscaSabor(self,sabor):
        i=0
        band=False
        while(not band)and(i<len(self.__Sabores)):
            if(self.__Sabores[i].getNombre()==sabor):
                band=True
            else:
                i=i+1
        if band==True:
            return Sabor(self.__Sabores[i].getN(),self.__Sabores[i].getNombre(),self.__Sabores[i].getDesc())
        else:
            return 0
   
    def muestra(self,lis):
        i=0
        while(i<3):
            j=0
            band=0
            while(j<len(self.__Sabores)and(band==0)):
                if(self.__Sabores[j].getCp()==lis[i]):
                    print(self.__Sabores[j].getNombre())
                    band=1
                else:
                    j=j+1
            i=i+1        
    def total(self):
        lis=[0,0,0]
        total=0
        anterior=0
        for i in range(len(self.__Sabores)):
            if(self.__Sabores[i].getCp()>total):
                total=self.__Sabores[i].getCp()
                anterior=lis[0]
                lis[0]=total
                lis[1]=anterior
            else:
                if(self.__Sabores[i].getCp()>lis[1]):
                    anterior=lis[1]
                    lis[1]=self.__Sabores[i].getCp()
                    lis[2]=anterior
                else:
                    if(self.__Sabores[i].getCp()>lis[2]):
                        lis[2]=self.__Sabores[i].getCp()
        return lis
   
    def mostrar3(self,lista):
        i=0
        while(i<len(self.__Sabores)):
            j=0
            band=True
            while(j<3)and(band==True):
                if(self.__Sabores[i].getCp()==lista[j]):
                    print(self.__Sabores[i].getNombre())
                    band=False
                else:
                    j=j+1
            i=i+1    
    def buscas(self,sabor):
        i=0
        band=False
        while(not band)and(i<len(self.__Sabores)):
            if(self.__Sabores[i].getNombre()==sabor):
                band=True
            else:
                i=i+1
        if band==True:
            self.__Sabores[i].setcP()
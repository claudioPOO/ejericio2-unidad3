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
            self.__Sabores[i].setcP()
            return Sabor(self.__Sabores[i].getN(),self.__Sabores[i].getNombre(),self.__Sabores[i].getDesc(),self.__Sabores[i].getCp())
        else:
            return 0
   
    def GuardarLista(self):
        lista=[]
        for i in range(len(self.__Sabores)):
            if(self.__Sabores[i].getCp()!=0):
                c=int(self.__Sabores[i].getCp())
                lista.append(c)
        l=sorted(lista,reverse=True)
        return l        
    def ordena(self,lis):
      for i in range(len(lis)):
           j=0
           band=0
           while(j<len(self.__Sabores)and (band==0)):
                 if(self.__Sabores[j].getCp()==lis[i]):       
                            print(self.__Sabores[j].getNombre())
                            band=1
                 else:          
                     j=j+1 
       
     
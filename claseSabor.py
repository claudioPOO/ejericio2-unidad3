class Sabor:
    __numero=0
    __nombre=''
    __descripcion=''
    __cantP=0
    def __init__(self,numero,nombre,desc,cantP=0):
        self.__numero=int(numero)
        self.__nombre=nombre
        self.__descripcion=desc
        self.__cantP=cantP
    def getN(self):
        return self.__numero
    def getNombre(self):
        return self.__nombre
    def getDesc(self):
        return self.__descripcion
    def mostrarD(self):
        return ('NUMERO: {}'.format(self.__numero),
               'Nombre: {}'.format(self.__nombre),
               'Descripcion: {}'.format(self.__descripcion))
    def setcP(self):
        self.__cantP+=1
    def getCp(self):
        return self.__cantP
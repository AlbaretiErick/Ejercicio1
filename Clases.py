class Email:
    __idC = ''
    __Dom = ''
    __TipoDom = ''
    __Contra = ''
    def __init__(self, idC, Dom, TipoDom, Contra):
        self.__idC = idC
        self.__Dom = Dom
        self.__TipoDom = TipoDom
        self.__Contra = Contra

    def retornaEmail (self):
        return self.__idC+'@'+self.__Dom+'.'+self.__TipoDom
    
    def getDom (self):
        return self.__Dom
    
    def crearCuenta (self, correo, contra):
        self.nID, self.nDom = correo.split("@")
        self.nDom, self.nTD = self.nDom.split(".")
        self.idC = self.nID
        self.Dom = self.nDom
        self.TipoDom = self.nTD
        self.Contra = contra
        #print ('ID: ', self.__idC, 'Dominio: ', self.__Dom, 'Tipo de dominio: ', self.__TipoDom, '\n')

    def ModfContra (self, VContra):
        while VContra!=self.__Contra:
            VContra = input ('La constraseña ingresada es incorrecta.\nColoque de nuevo la contraseña: ')
        self.__Contra = input ('Ingrese nueva contraseña: ')
        #print ('Nueva Contraseña:', self.__Contra, '\n')

    def verificar (self, ID, D, TD):
        band = False
        if ID!='' and D!='' and TD!='':
            band = True
        return band
    
    def getBool (self, dominio):
        bool = False
        if dominio==self.__Dom:
            bool = True
        return bool
from Clases import Email

if __name__=='__main__':
    unNombre = input ('Ingrese su nombre: ')
    unEmail = Email(input('Ingrese ID de la cuenta: '), input('Ingrese dominio: '), input('Ingrese tipo de dominio: '), input('Ingrese contraseña: '))
    print ('Estimado', unNombre, 'te enviaremos tus mensajes a la dirección', unEmail.retornaEmail (), '\n')
    unEmail.ModfContra (input ('Ingrese su actual contraseña: '))
    otroEmail = Email(None, None, None, None)
    otroEmail.crearCuenta(input ('Ingrese Correo: '), None)
    Emails = []
    with open ("Correos.txt", "r") as archi:
        i = -1
        for line in archi:
            i = i+1
            Emails.append(Email(None, None, None, None))
            ID, D, TD, C = line.split(',')
            #print (ID+'@'+D+'.'+TD, 'contra:', C)
            bool = Emails[i].verificar(ID, D, TD)
            if bool==False:
                print ('Error: El correo', ID+'@'+D+'.'+TD, 'es incorrecto.\n')
            else:
                Emails[i].crearCuenta(ID+'@'+D+'.'+TD, C)
    Emails.append(unEmail)
    Emails.append(otroEmail)
    domi = input ('Ingrese dominio a buscar: ')
    i = -1
    cont=0
    for j in Emails:
        i=i+1
        bool = Emails[i].getBool(domi)
        if bool==True:
            cont=cont+1
    print ('La cantidad usada del dominio ingresado es:', cont)
    print ("\nFin del Programa.")
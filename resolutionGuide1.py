#primer guia de programacion3

#El usuario nos indica la operacion a realizar y capturamos el error al ingresar cualquier trcla y cerramos el programa
try:
    opcion = int(input("Por favor ingrese el numero de la operacion que desea realizar\n1.Piramide\n2.\n#.cualquier tecla para salir\nopcion: "))

except:
    print("Adios")
    quit()

#Construimos las funciones

#Funcion piramide
def piramide(bloques):
    contador = 0
    #variable para llevar el numero de bloques puestos
    bloquesPuestos= int(bloques) 


    if bloques > 0:

        for i in range(1, bloques):
            if  bloquesPuestos < i:
                if bloquesPuestos > 0:
                    print(f"Le han sobrado {bloquesPuestos} bloques")
                else:
                    print("Le han quedado 0 bloques")
                break
            else:
                bloquesPuestos = bloquesPuestos - i
                print(' ' * (bloques - i), '* ' * (i))

    else:
        print("El numero tiene que ser mayor a 0")


#elegimos la funcion a utilizar y enviamos los valores de sus parametros
if(opcion==1):
    nBloques = int(input("Por favor ingrese el numero de bloques de su piramide:"))
    piramide(nBloques)
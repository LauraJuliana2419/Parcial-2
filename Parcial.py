##Autora Laura Juliana Rodriguez
##Ejercicio 1 Determinar si en una lista no existen elementos repetidos
print("#########################################################")
print("Determinar si en una lista no existen elementos repetidos")
##Lo primero que hago es declrar las listas 
##Una con elementos repetidos para probar
##Y otra que no tiene elementos repetidos 
Lista_repetidos=["Juana","Milena","Juana","Andrea","Olga","Milena"]
Lista_norepetidos=["Andres","Jose","Carlos","David"]
##Ahora creo una funcion con un ciclo for
##Para que me recorra todos los elementos
##en la lista,despues si en la lista
##al usar el metodo.count se ve que tiene mas 
##de un elemento(puesto que arroja numeros,el metodo count)
##entonces imprimira que hay elementos repetidos y cuales son
##Si no simplemente imprimira que no los hay
def Elementos_repetidos(Lista_repetidos):
    for elemento in Lista_repetidos:
        if Lista_repetidos.count(elemento)>1:
            print(elemento)
    print("Hay elementos repetidos y son: ",elemento)

    print("No hay elementos repetidos")
##Llamo las funciones y como parametro ingreso ambas listas
print(Elementos_repetidos(Lista_repetidos))
print(Elementos_repetidos(Lista_norepetidos))
##Ejercicio 2 Determinar si en una lista se encuentra una cadena de caracteres con 2 o mas vocales si existe imprimir si no imprimir que no existe
print("#########################################################")
print("Determinar si en una lista hay 2 o mas vocales")
##Inicio declarando 2 listas una con vocales y otra sin
Lista_vocales=["Hola","Adios","Amigo","Casa","Perro"]
Lista_vocales_inexistentes=["hjhj","kkkkl","Poñ","Gfgfd"]
##Creo una funcion que con un for me recorra elemento x elemento
##en la lista de vocales y tambien inicializo un contador en 0
##para poder guardar ahi lo que recorre el siguiente for
##el cual recorre todas las letras en el elemento y si esa esta en 
##las vocales en minusculas o mayusculas 
##se le suma 1 al contador y si al final tiene un numero mayor al 2 
##en su contador imprime que hay mas de 2 vocales,si no imprime que no existe 
def Vocales(Lista_vocales):
    for elemento in Lista_vocales:
        contador=0
        for letra in elemento:
            if letra in "aeiouAEIOU":
                contador+=1
        if contador>=2:
            print("Hay mas de 2 vocales en la lista: ",Lista_vocales)
    print ("NO EXISTE")
print(Vocales(Lista_vocales)) 
print(Vocales(Lista_vocales_inexistentes))
##Ejercicio 3
print("#########################################################")
print("Determinar si en 2 listas se encuentran elementos que tiene la primera que no tiene la segunda: ")
##Inicializo ambas listas con numeros repetidos y sin ellos 
Lista_1=[1,2,3,4,5,6,7]
Lista_2=[1,2,4,5,6]
##Creo una funcion y le ingreso ambas listas como parametro
##Ahora con un for las recorro y si el elemento no esta en la lista 2 
##Se imprime que si hay elementos en la lista 1 que no estan en la lista 2 
def Elementos_primera(Lista_1,Lista_2):
    for elemento in Lista_1:
        if elemento not in Lista_2:
            print("Si hay elementos que estan en la primera y no en la segunda y son : ",elemento)
print(Elementos_primera(Lista_1,Lista_2))  
##Ejercicio 4 Promedio de reales
print("#########################################################")
print("Calcular el promedio de los elementos de la lista: ")
##Nuevamente inicializo primero ambas listas 
Lista_reales=[1.2,2.3,4.5,6.7,8.9]
Lista_reales_2=[3.3,9.9,8.7,6.4]
##Creo una funcion y creo un contador llamado suma
##creo un for en el que el elemento me recorre la lista de los reales
##Y a ese contador le sumo el elemento actual que vaya iterando
##creo una nueva variable en la cual guardo la division de esa suma entre
##la longitud de la lista para lo que utilizo el metodo len que me arroja
##la longitud
##Al final del ciclo se imprime el promedio calculado
def Promedio_reales(Lista_reales):
    suma=0
    for elemento in Lista_reales:
        suma+=elemento
    promedio=suma/len(Lista_reales)
    print("el promedio es: ",promedio) 
print(Promedio_reales(Lista_reales))
print(Promedio_reales(Lista_reales_2))
##Ejercicio 5 Algoritmo que determine la mediana de un arreglo de enteros
print("#########################################################")
print("Determinar la mediana de los elementos de un arreglo de enteros: ")
##Primero declaro el arreglo
Arreglo_enteros=[1,2,3,4,5,6,7,8,9]
##Creo una funcion que como parametro me recibe mi arreglo
##creo un if en el que si la longitud de mi arreglo sacandole el modulo
##es mayor a 0(porque quiere decir que si existe al ser mayor) entonces 
##una variable que creo llamada mediana guarda la longitud de mi arreglo y 
##eso lo divido en 2 para hallar la mitad(que es la mediana de mi arreglo)
def Mediana_enteros(Arreglo_enteros):
    if len(Arreglo_enteros)%2>=0:
        mediana=([len(Arreglo_enteros)//2])
    else:
        print("La mediana no existe por que es menor a numero 0: ")
    print("La mediana es: ", mediana)
print(Mediana_enteros(Arreglo_enteros))

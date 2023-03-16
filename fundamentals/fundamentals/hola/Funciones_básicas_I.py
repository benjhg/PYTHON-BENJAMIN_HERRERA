'''
#1
def número_de_grupos_alimentarios():
    return 5
print(número_de_grupos_alimentarios())
# lo que retorna es 5 ya que en el retorno de la variable "número_de_grupos_alimentarios" es igual a 5 

#2
def número_de_ramas_militares():
    return 5
print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo() + número_de_ramas_militares())
# daria error ya que "número_de_días_en_una_semana_silicona_o_lados_del_triángulo" no esta definido previamente en algun arreglo

#3
def número_de_libros_en_espera():
    return 5
    return 10
print(número_de_libros_en_espera())

# dara como resultado 5 ya que el 2°do return no lo tendra en cuenta al ser una repuesta 2° en una funcion

#4
def número_de_dedos():
    return 5
    print(10)
print(número_de_dedos())

# imprimira el valor de 5 ya que el print que hay esta dentro de de la funcion "número_de_dedos"
#5
def número_de_lagos_grandes():
    print(5)
x = número_de_lagos_grandes()
print(x)

#lo que imprime es "5" seguido de "none" ya que "print(x)" ya que la variable x no tiene una declaracion de retorno 

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

# dara los resultados de 1+2 y 2+3 y luego dara un TyoeError ya  que no podemos sumar 2 funciones que no retornan ningun valor
'''
#7
def concatenar(b,c):
    return str(b)+str(c)
="función de soporte python from-rainbow">print(concatenar(2,5))

#esta dara error porque esta mal la sintaxis de este fragmento de codigo


#8
def número_de_océanos_o_dedos_o_continentes():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(número_de_oceános_o_dedos_o_continentes())
 #no imprimira nada ya que "número_de_oceános_o_dedos_o_continentes" no es lo mismo que "número_de_océanos_o_dedos_o_continentes" y al no estar bien definido da un error de nombre


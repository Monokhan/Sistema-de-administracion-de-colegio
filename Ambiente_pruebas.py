
campos = ('uno', '2', 'tres') #tupla
bosques = ('arboles','rocas','ardillas','4')
text = ",".join(bosques) # no funciona como se espera, concadenando con metodo f ambas var.

print(text) # imprime todos los elementos de la tupla, separados por comas.

#en caso de tener un solo elemento
campos = ('uno') #tupla

text = ",".join(campos) 

print(text)   #en caso de tener un solo elemento la tupla, deletrea el argumento de la tupla separanhdo por ',' cada letra.

""".
con la funcion .join  
si le damos un dato y/o un conjunto de datos, o un subconjunto de datos
esta la separara y la agrupara en un solo grupo, separando por ','
"""
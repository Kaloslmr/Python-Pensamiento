#Differents type of scope 


#---------- GLOBAL SCOPE: Puedes usar la variable donde quieras! ----------
x = 'Esta es una variable global'


#Funcion en variable LOCAL
def globalScope():
    print(x)


#Imprimimos la variable global en la funcion y en el codigo global
globalScope()
print(x)


#---------- LOCAL SCOPE: Si creas la variable en una función sólo pertenece ahí ----------
def localScope():
    x = 'Esta es una variable local'
    print(x)


localScope()


#---------- KEYWORD GLOBAL: Puedes crear variable global usando una keywoard ----------
x = 'Esta es una variable global sin cambiar valor'
def keywoardGlobal():
    global x
    x = 'Esta es una variable global por keywoard, cambiamos su valor!'


keywoardGlobal()
print(x)



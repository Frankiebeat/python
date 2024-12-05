# el tipado en python es dinamico, es decir, no es necesario declarar el tipo de variable que se va a utilizar
# en el siguiente ejemplo se muestra como se puede cambiar el tipo de variable en una misma variable
# en python se puede hacer lo siguiente:

x = 5
x = "hola"
x = 5.0
x = True
x = [1,2,3,4]

# en este caso si imprimo x, me va a mostrar el ultimo valor que se le asigno a la variable x

# para conocer que tipo de variable es, se puede utilizar la funcion type()

print(type(x))

# en este caso, la salida va a ser <class 'list'>, ya que el ultimo valor que se le asigno a x fue una lista
class mi_boton():
    def __init__(self, color,ancho,alto):
        self.color = color
        self.ancho = ancho
        self.alto = alto

    def to_string(self):
        mensaje = "El color del boton es {}. El ancho es {} y el alto {}."
        print(mensaje.format(self.color,self.ancho,self.alto))

boton1 = mi_boton("rojo",43,55)

boton1.to_string()


class Agregarelemento(list): #Creamos una clase Agregarelemento heredando atributos de clase list (clase incorporada)
    def append(self, alumno): #Definimos que el método append (de listas) añadirá el elemento alumno
        print (("Añadido el alumno"), (alumno)) #Imprimimos el resultado del método
        super().append(alumno) #Incorporamos la función super SIN INDICAR LA CLASE ACTUAL, seguida
                                                    #del método append para la variable alumno

Lista1 = Agregarelemento() #Definimos la clase de nuestra lista llamada "Lista1"
Lista1.append ('Matias') #Añadimos un elemento a la lista como lo haríamos normalmente
print (Lista1) #Imprimimos la lista para corroborar que se añadió el alumno
import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Bot�n A y Bot�n B")
        
        self.pulsador_presionado = False

        # Crear el bot�n A
        self.boton_A = tk.Button(self.root, text="Bot�n A", command=self.presionar_A)
        self.boton_A.pack(pady=20, padx=50)

        # Crear el bot�n B
        self.boton_B = tk.Button(self.root, text="Bot�n B", command=self.restaurar_A)
        self.boton_B.pack(pady=20)

    def presionar_A(self):
        # Al presionar el bot�n A, se mantendr� presionado
        self.pulsador_presionado = True
        self.boton_A.config(relief=tk.SUNKEN)

    def restaurar_A(self):
        # Restaurar el bot�n A a su estado normal
        self.pulsador_presionado = False
        self.boton_A.config(relief=tk.RAISED)

# Crear la ventana principal de la aplicaci�n
root = tk.Tk()
app = App(root)

# Ejecutar el bucle principal
root.mainloop()
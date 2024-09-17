import tkinter as tk
import random
import time
from threading import Thread

# Funci�n para generar un valor aleatorio entre 6.4 y 7 con dos decimales
def generar_valor_aleatorio():
    return round(random.uniform(6.4, 7), 2)

# Funci�n para incrementar el valor en 0.08 unidades
def incrementar_valor():
    global valor_display
    global botones
    global current_index

    # Obtener el �ndice del bot�n actualmente marcado de amarillo
    index_anterior = current_index

    # Cambiar color del bot�n Q1 a amarillo durante 2 segundos
    pintar_Q1_amarillo()

    time.sleep(2)  # Esperar 2 segundos

    # Incrementar el valor y actualizar el display
    valor_display += 0.08
    actualizar_display()

    # Obtener el siguiente bot�n a marcar de amarillo
    current_index += 1
    if current_index > 8:
        current_index = 0
    
    # Cambiar color del pr�ximo bot�n a amarillo y restaurar color del anterior
    botones[current_index].config(bg='yellow')
    botones[index_anterior].config(bg='SystemButtonFace')

# Funci�n para decrementar el valor en 0.08 unidades
def decrementar_valor():
    global valor_display
    global botones
    global current_index

    # Obtener el �ndice del bot�n actualmente marcado de amarillo
    index_anterior = current_index

    # Cambiar color del bot�n Q1 a amarillo durante 2 segundos
    pintar_Q1_amarillo()

    time.sleep(2)  # Esperar 2 segundos

    # Decrementar el valor y actualizar el display
    valor_display -= 0.08
    actualizar_display()

    # Obtener el bot�n anterior a marcar de amarillo
    current_index -= 1
    if current_index < 0:
        current_index = 8
    
    # Cambiar color del bot�n anterior a amarillo y restaurar color del siguiente
    botones[current_index].config(bg='yellow')
    botones[index_anterior].config(bg='SystemButtonFace')

# Funci�n para actualizar el texto del display con el nuevo valor
def actualizar_display():
    display.config(text=f"{valor_display:.2f}")

# Funci�n para cambiar el color del bot�n Q1 a amarillo
def pintar_Q1_amarillo():
    Q1.config(bg='yellow')
    # Iniciar un hilo para restaurar el color de Q1 despu�s de 2 segundos
    Thread(target=restaurar_color_Q1).start()

# Funci�n para restaurar el color del bot�n Q1 despu�s de 2 segundos
def restaurar_color_Q1():
    time.sleep(2)
    Q1.config(bg='SystemButtonFace')

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Display con Valor Aleatorio")

# Generar un valor aleatorio inicial con dos decimales
valor_display = generar_valor_aleatorio()

# Crear un widget de etiqueta para mostrar el valor
display = tk.Label(ventana, text=f"{valor_display:.2f}", font=("Arial", 24))
display.pack(pady=20)

# Crear botones del 1 al 9
botones = []
for i in range(1, 10):
    if i == 5:
        botones.append(tk.Button(ventana, text=str(i), width=5, height=2, bg='yellow'))
    else:
        botones.append(tk.Button(ventana, text=str(i), width=5, height=2))
    botones[-1].pack(side=tk.LEFT, padx=5)

# �ndice del bot�n actualmente marcado de amarillo (inicia en el 5)
current_index = 4

# Bot�n Q1
Q1 = tk.Button(ventana, text="Q1", width=5, height=2)
Q1.pack(side=tk.RIGHT, padx=5)

# Crear botones para incrementar y decrementar el valor
boton_mas = tk.Button(ventana, text="+ 0.08", command=incrementar_valor, width=10)
boton_mas.pack(side=tk.LEFT, padx=20)

boton_menos = tk.Button(ventana, text="- 0.08", command=decrementar_valor, width=10)
boton_menos.pack(side=tk.RIGHT, padx=20)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
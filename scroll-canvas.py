import tkinter as tk

# Función para crear una interfaz con desplazamiento vertical y horizontal
def create_scrollable_canvas_with_buttons():
    root = tk.Tk()
    root.geometry("600x400")

    # Crear un Frame contenedor
    container = tk.Frame(root)
    container.pack(fill=tk.BOTH, expand=True)

    # Crear el Canvas
    canvas = tk.Canvas(container)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Crear las scrollbars (vertical y horizontal)
    v_scrollbar = tk.Scrollbar(container, orient=tk.VERTICAL, command=canvas.yview)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    h_scrollbar = tk.Scrollbar(container, orient=tk.HORIZONTAL, command=canvas.xview)
    h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    # Configurar el Canvas para usar ambas scrollbars
    canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    # Crear un Frame dentro del Canvas (este es el que se desplazará)
    scrollable_frame = tk.Frame(canvas)

    # Añadir el Frame al canvas (con create_window) y configurar el scrollregion
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Ajustar el tamaño del scrollable_frame después de agregar widgets
    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    # Vincular la función de actualización del scrollregion al cambio de tamaño
    scrollable_frame.bind("<Configure>", update_scrollregion)

    # Agregar botones al Frame desplazable
    for i in range(20):
        button = tk.Button(scrollable_frame, text=f"Botón {i+1}")
        button.pack(pady=10)

    # Forzar un widget ancho para activar el desplazamiento horizontal
    wide_button = tk.Button(scrollable_frame, text="Botón muy largo para scroll horizontal", width=50)
    wide_button.pack(pady=10)

    # Asegurarse de que el canvas sea suficientemente ancho para desplazarse
    scrollable_frame.update_idletasks()  # Actualizar inmediatamente el tamaño del frame

    root.mainloop()

# Llamar a la función para crear la interfaz
create_scrollable_canvas_with_buttons()

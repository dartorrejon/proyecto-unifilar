
# Crear una ventana en donde se sinule la conmutación de barras 6,6 KV de GUE13

import tkinter as tk

# Creamos la ventana principal que llamaremos root
root = tk.Tk()
#root.geometry("1200x1900")
root.title("CONMUTACION DE BARRAS 6,6 KV")

# Creamos un lienzo para dibujar
canvas = tk.Canvas(root, height=1020, width=1800)

#Cambiar el color de fondo de la ventana
#https://developer.mozilla.org/es/docs/Web/CSS/CSS_colors/Color_picker_tool
colorfondo='#E4DD9E'
canvas.configure(background=colorfondo)
#canvas.configure(background='#CDBB78')
#canvas.configure(background='#D0D033')


# Draw horizontal lines.
#canvas.create_line(0, 20, 300, 20, width=2, fill='blue')
#canvas.create_line(0, 40, 300, 40, width=4, fill='red')
#canvas.create_line(0, 60, 300, 60, width=6, fill='green')
#canvas.create_line(0, 80, 300, 80, width=8, fill='purple')
#canvas.create_line(0, 100, 300, 100, width=10, fill='orange')
#canvas.create_line(0, 120, 300, 120, width=12, fill='brown')
#canvas.create_line(0, 140, 300, 140, width=14, fill='black')

# Draw vertical lines.
#canvas.create_line(20, 0, 20, 250, width=2, fill='blue')
#canvas.create_line(40, 0, 40, 250, width=4, fill='red')
#canvas.create_line(60, 0, 60, 250, width=6, fill='green')
#canvas.create_line(80, 0, 80, 250, width=8, fill='purple')
#canvas.create_line(100, 0, 100, 250, width=10, fill='orange')

X=0
Y=0

xI02=-50  # Para bara 3BA
xI05=-100 # Para barra 3OBB
x3OAT=1430

y3OAT=Y+100
yg=Y+250
y66=Y+450

linea='#039520'
linea132='blue'
linea13='red'
barra='green'

#Intentando mi propio dibujo de esquema unifilar eléctrico. Lineas horizontales
canvas.create_line(X+150, y3OAT, X+xI02+400, y3OAT, width=6, fill=linea)
canvas.create_line(X+800, y3OAT, X+xI05+1350, y3OAT, width=6, fill=linea)

canvas.create_line(X+570, y3OAT-45, X+650, y3OAT-45, width=6, fill=linea13)

canvas.create_line(X+xI02+450, yg, X+750, yg, width=6, fill=linea)

canvas.create_line(X+100, y66, X+xI02+500, y66, width=10, fill=barra)
canvas.create_line(X+700, y66, X+xI02+1100, y66, width=10, fill=barra)
canvas.create_line(X+xI05+1300, y66, X+xI05+1600, y66, width=10, fill=barra)

#Lineas verticales
canvas.create_line(X+150, y3OAT-3, X+150, y66-5, width=6, fill=linea)
canvas.create_line(X+xI02+1050, y3OAT-3, X+xI02+1050, y66-5, width=6, fill=linea)
canvas.create_line(X+xI05+1350, y3OAT-3, X+xI05+1350, y66-5, width=6, fill=linea)

canvas.create_line(X+570, y3OAT-45-3, X+570, y3OAT+52, width=6, fill=linea13)
canvas.create_line(X+570, yg-20, X+570, yg-3, width=6, fill=linea)

canvas.create_line(X+xI02+450, yg-3, X+xI02+450, y66-5, width=6, fill=linea)
canvas.create_line(X+750, yg-3, X+750, y66-5, width=6, fill=linea)

canvas.create_line(X+x3OAT, y3OAT-3-50, X+x3OAT, y3OAT+52, width=6, fill=linea132)
canvas.create_line(X+x3OAT, yg-20, X+x3OAT, y66-5, width=6, fill=linea)

circleGen = canvas.create_oval(X+700-50, y3OAT-80, X+770-50, y3OAT-10, width=2, outline="red")
canvas.create_text(X+735-50, y3OAT-45, text="G", font=("Arial", 30, "bold"), fill="black")
circle3BT1= canvas.create_oval(X+570-25, y3OAT+50, X+620-25, y3OAT+100, width=3, outline="red")
circle3BT2= canvas.create_oval(X+570-25, y3OAT+80, X+620-25, y3OAT+130, width=3, outline="green")
circle3OAT1= canvas.create_oval(X+x3OAT-25, y3OAT+50, X+x3OAT+25, y3OAT+100, width=3, outline=linea132)
circle3OAT2= canvas.create_oval(X+x3OAT-25, y3OAT+80, X+x3OAT+25, y3OAT+130, width=3, outline="green")
#canvas.create_oval(X+x3OAT-25, y3OAT+50, X+x3OAT+25, y3OAT+100, width=3, outline="red")
#canvas.create_oval(X+x3OAT-25, y3OAT+80, X+x3OAT+25, y3OAT+130, width=3, outline="green")


#Interruptores 1 2 3 4 5 despues le ponemos los nombres correctos
canvas.create_rectangle(X+130, y66-60, X+170, y66-20, width=2, outline="black", fill=colorfondo)
canvas.create_oval(X+130, y66-60, X+170, y66-20, width=2, outline="black")
Interruptor01 = canvas.create_rectangle(X+145, y66-55, X+155, y66-25, width=2, fill="red")
canvas.create_rectangle(X+170, y66-60, X+210, y66-20, width=2, outline="black")
mimico01 = canvas.create_polygon(X+184, y66-55, X+196, y66-55, X+184, y66-25, X+196, y66-25, fill="red")

canvas.create_rectangle(X+xI02+430, y66-60, X+xI02+470, y66-20, width=2, outline="black", fill=colorfondo)
canvas.create_oval(X+xI02+430, y66-60, X+xI02+470, y66-20, width=2, outline="black")
Interruptor02 = canvas.create_rectangle(X+xI02+435, y66-45, X+xI02+465, y66-35, width=2, fill="green")
canvas.create_rectangle(X+xI02+470, y66-60, X+xI02+510, y66-20, width=2, outline="black")
mimico02 = canvas.create_polygon(X+xI02+484, y66-55, X+xI02+496, y66-55, X+xI02+484, y66-25, X+xI02+496, y66-25, fill="green")

canvas.create_rectangle(X+730, y66-60, X+770, y66-20, width=2, outline="black", fill=colorfondo)
canvas.create_oval(X+730, y66-60, X+770, y66-20, width=2, outline="black")
Interruptor03 = canvas.create_rectangle(X+735, y66-45, X+765, y66-35, width=2, fill="green")
canvas.create_rectangle(X+770, y66-60, X+810, y66-20, width=2, outline="black")
mimico03 = canvas.create_polygon(X+784, y66-55, X+796, y66-55, X+784, y66-25, X+796, y66-25, fill="green")

canvas.create_rectangle(X+xI02+1030, y66-60, X+xI02+1070, y66-20, width=2, outline="black", fill=colorfondo)
canvas.create_oval(X+xI02+1030, y66-60, X+xI02+1070, y66-20, width=2, outline="black")
Interruptor04 = canvas.create_rectangle(X+xI02+1045, y66-55, X+xI02+1055, y66-25, width=2, fill="red")
canvas.create_rectangle(X+xI02+1070, y66-60, X+xI02+1110, y66-20, width=2, outline="black")
mimico04 = canvas.create_polygon(X+xI02+1084, y66-55, X+xI02+1096, y66-55, X+xI02+1084, y66-25, X+xI02+1096, y66-25, fill="red")

canvas.create_rectangle(X+xI05+1330, y66-60, X+xI05+1370, y66-20, width=2, outline="black", fill=colorfondo)
canvas.create_oval(X+xI05+1330, y66-60, X+xI05+1370, y66-20, width=2, outline="black")
canvas.create_rectangle(X+xI05+1345, y66-55, X+xI05+1355, y66-25, width=2, fill="red")
#canvas.create_rectangle(X+xI05+1370, y66-60, X+xI05+1410, y66-20, width=2, outline="black")
#canvas.create_polygon(X+xI05+1384, y66-55, X+xI05+1396, y66-55, X+xI05+1390, y66-40, fill="red")
#canvas.create_polygon(X+xI05+1384, y66-25, X+xI05+1396, y66-25, X+xI05+1390, y66-42, fill="red")

canvas.create_rectangle(X+xI05+1530-20, y66-60, X+xI05+1570-20, y66-20, width=2, outline="black", fill=colorfondo)
canvas.create_oval(X+xI05+1530-20, y66-60, X+xI05+1570-20, y66-20, width=2, outline="black")
canvas.create_rectangle(X+xI05+1545-20, y66-55, X+xI05+1555-20, y66-25, width=2, fill="red")


#Hacer botones de los interruptores
button01 = tk.Button(root, text="0", width=5, height=2)
button01.place(x=X+83, y=y66-60)

button02 = tk.Button(root, text="1", width=5, height=2)
button02.place(x=X+211, y=y66-60)

button03 = tk.Button(root, text="0", width=5, height=2)
button03.place(x=X+xI02+383, y=y66-60)

button04 = tk.Button(root, text="1", width=5, height=2)
button04.place(x=X+xI02+511, y=y66-60)

buttonfas01 = tk.Button(root, text="FAS", width=5, height=2)
buttonfas01.place(x=X+xI02+470, y=y66-100)

button05 = tk.Button(root, text="0", width=5, height=2)
button05.place(x=X+683, y=y66-60)

button06 = tk.Button(root, text="1", width=5, height=2)
button06.place(x=X+811, y=y66-60)

buttonfas02 = tk.Button(root, text="FAS", width=5, height=2)
buttonfas02.place(x=X+770, y=y66-100)

button07 = tk.Button(root, text="0", width=5, height=2)
button07.place(x=X+xI02+983, y=y66-60)

button08 = tk.Button(root, text="1", width=5, height=2)
button08.place(x=X+xI02+1111, y=y66-60)

#button09 = tk.Button(root, text="0", width=5, height=2)
#button09.place(x=X+xI05+1283, y=y66-60)

#button10 = tk.Button(root, text="1", width=5, height=2)
#button10.place(x=X+xI05+1411, y=y66-60)

buttonSel3BB01 = tk.Button(root, text="1", width=4, height=2)
buttonSel3BB01.place(x=X+170, y=y66+60)

buttonSel3BB02 = tk.Button(root, text="0", width=4, height=2)
buttonSel3BB02.place(x=X+170+40, y=y66+60)

buttonSel3BB03 = tk.Button(root, text="1", width=4, height=2)
buttonSel3BB03.place(x=X+xI02+470, y=y66+60)

buttonSel3BB04 = tk.Button(root, text="0", width=4, height=2)
buttonSel3BB04.place(x=X+xI02+470+40, y=y66+60)

buttonSel3BA01 = tk.Button(root, text="1", width=4, height=2)
buttonSel3BA01.place(x=X+780, y=y66+60)

buttonSel3BA02 = tk.Button(root, text="0", width=4, height=2)
buttonSel3BA02.place(x=X+780+40, y=y66+60)

buttonSel3BA03 = tk.Button(root, text="1", width=4, height=2)
buttonSel3BA03.place(x=X+1000, y=y66+60)

buttonSel3BA04 = tk.Button(root, text="0", width=4, height=2)
buttonSel3BA04.place(x=X+1000+40, y=y66+60)

buttonL01 = tk.Button(root, text="L", width=5, height=2)
buttonL01.place(x=X+83, y=y66+60)

buttonL01 = tk.Button(root, text="L", width=5, height=2)
buttonL01.place(x=X+x3OAT+100, y=y66+60)

#Hacer botones de conmutacion de puntos de 3BT

button3BT00 = tk.Button(root, text="0", width=4, height=2)
button3BT00.place(x=X+xI02+430+80, y=y3OAT+10)

button3BT01 = tk.Button(root, text="-1", width=4, height=2)
button3BT01.place(x=X+xI02+430+40, y=y3OAT+10)

button3BT02 = tk.Button(root, text="-2", width=4, height=2)
button3BT02.place(x=X+xI02+430, y=y3OAT+10)

button3BT03 = tk.Button(root, text="-3", width=4, height=2)
button3BT03.place(x=X+xI02+430+80, y=y3OAT+10+40)

button3BT04 = tk.Button(root, text="-4", width=4, height=2)
button3BT04.place(x=X+xI02+430+40, y=y3OAT+10+40)

button3BT05 = tk.Button(root, text="-5", width=4, height=2)
button3BT05.place(x=X+xI02+430, y=y3OAT+10+40)

button3BT06 = tk.Button(root, text="-6", width=4, height=2)
button3BT06.place(x=X+xI02+430+80, y=y3OAT+10+80)

button3BT07 = tk.Button(root, text="-7", width=4, height=2)
button3BT07.place(x=X+xI02+430+40, y=y3OAT+10+80)

button3BT08 = tk.Button(root, text="-8", width=4, height=2)
button3BT08.place(x=X+xI02+430, y=y3OAT+10+80)



button3BT11 = tk.Button(root, text="1", width=4, height=2)
button3BT11.place(x=X+xI02+770-80, y=y3OAT+10)

button3BT12 = tk.Button(root, text="2", width=4, height=2)
button3BT12.place(x=X+xI02+770-40, y=y3OAT+10)

button3BT13 = tk.Button(root, text="3", width=4, height=2)
button3BT13.place(x=X+xI02+770, y=y3OAT+10)

button3BT14 = tk.Button(root, text="4", width=4, height=2)
button3BT14.place(x=X+xI02+770-80, y=y3OAT+10+40)

button3BT15 = tk.Button(root, text="5", width=4, height=2)
button3BT15.place(x=X+xI02+770-40, y=y3OAT+10+40)

button3BT16 = tk.Button(root, text="6", width=4, height=2)
button3BT16.place(x=X+xI02+770, y=y3OAT+10+40)

button3BT17 = tk.Button(root, text="7", width=4, height=2)
button3BT17.place(x=X+xI02+770-80, y=y3OAT+10+80)

button3BT18 = tk.Button(root, text="8", width=4, height=2)
button3BT18.place(x=X+xI02+770-40, y=y3OAT+10+80)

button3BT19 = tk.Button(root, text="I-O", width=4, height=2)
button3BT19.place(x=X+xI02+770, y=y3OAT+10+80)

#Botones de conmutaciones de trafo 3OAT

button3OAT00 = tk.Button(root, text="0", width=4, height=2)
button3OAT00.place(x=X+x3OAT-150+80, y=y3OAT+10)

button3OAT01 = tk.Button(root, text="-1", width=4, height=2)
button3OAT01.place(x=X+x3OAT-150+40, y=y3OAT+10)

button3OAT02 = tk.Button(root, text="-2", width=4, height=2)
button3OAT02.place(x=X+x3OAT-150, y=y3OAT+10)

button3OAT03 = tk.Button(root, text="-3", width=4, height=2)
button3OAT03.place(x=X+x3OAT-150+80, y=y3OAT+10+40)

button3OAT04 = tk.Button(root, text="-4", width=4, height=2)
button3OAT04.place(x=X+x3OAT-150+40, y=y3OAT+10+40)

button3OAT05 = tk.Button(root, text="-5", width=4, height=2)
button3OAT05.place(x=X+x3OAT-150, y=y3OAT+10+40)

button3OAT06 = tk.Button(root, text="-6", width=4, height=2)
button3OAT06.place(x=X+x3OAT-150+80, y=y3OAT+10+80)

button3OAT07 = tk.Button(root, text="-7", width=4, height=2)
button3OAT07.place(x=X+x3OAT-150+40, y=y3OAT+10+80)

button3OAT08 = tk.Button(root, text="-8", width=4, height=2)
button3OAT08.place(x=X+x3OAT-150, y=y3OAT+10+80)



button3OAT11 = tk.Button(root, text="1", width=4, height=2)
button3OAT11.place(x=X+x3OAT+110-80, y=y3OAT+10)

button3OAT12 = tk.Button(root, text="2", width=4, height=2)
button3OAT12.place(x=X+x3OAT+110-40, y=y3OAT+10)

button3OAT13 = tk.Button(root, text="3", width=4, height=2)
button3OAT13.place(x=X+x3OAT+110, y=y3OAT+10)

button3OAT14 = tk.Button(root, text="4", width=4, height=2)
button3OAT14.place(x=X+x3OAT+110-80, y=y3OAT+10+40)

button3OAT15 = tk.Button(root, text="5", width=4, height=2)
button3OAT15.place(x=X+x3OAT+110-40, y=y3OAT+10+40)

button3OAT16 = tk.Button(root, text="6", width=4, height=2)
button3OAT16.place(x=X+x3OAT+110, y=y3OAT+10+40)

button3OAT17 = tk.Button(root, text="7", width=4, height=2)
button3OAT17.place(x=X+x3OAT+110-80, y=y3OAT+10+80)

button3OAT18 = tk.Button(root, text="8", width=4, height=2)
button3OAT18.place(x=X+x3OAT+110-40, y=y3OAT+10+80)

button3OAT19 = tk.Button(root, text="I-O", width=4, height=2)
button3OAT19.place(x=X+x3OAT+110, y=y3OAT+10+80)

buttonRes04 = tk.Button(root, text="C", width=4, height=2)
buttonRes04.place(x=X+170+40, y=y3OAT+10+40)

buttonRes05 = tk.Button(root, text="D", width=4, height=2)
buttonRes05.place(x=X+170, y=y3OAT+10+40)

buttonRes07 = tk.Button(root, text="1", width=4, height=2)
buttonRes07.place(x=X+170+40, y=y3OAT+10+80)

buttonRes08 = tk.Button(root, text="0", width=4, height=2)
buttonRes08.place(x=X+170, y=y3OAT+10+80)


#La barra invertida se hace con ALT+92, usamos \n para hacer texto multilinea

button3BT21 = tk.Button(root, text="0", width=4, height=2)
button3BT21.place(x=X+xI02+550, y=yg+60)

texto3BT22 = "REG\n+"
button3BT22 = tk.Button(root, text=texto3BT22, width=4, height=2)
button3BT22.place(x=X+xI02+590, y=yg+60)

texto3BT23 = "REG\n-"
button3BT23 = tk.Button(root, text=texto3BT23, width=4, height=2)
button3BT23.place(x=X+xI02+630, y=yg+60)

button3BT24 = tk.Button(root, text="Q1", width=4, height=2)
button3BT24.place(x=X+xI02+670, y=yg+60)

button3OAT21 = tk.Button(root, text="0", width=4, height=2)
button3OAT21.place(x=X+x3OAT-80, y=yg+60)

texto3OAT22 = "REG\n+"
button3OAT22 = tk.Button(root, text=texto3BT22, width=4, height=2)
button3OAT22.place(x=X+x3OAT-40, y=yg+60)

texto3OAT23 = "REG\n-"
button3OAT23 = tk.Button(root, text=texto3BT23, width=4, height=2)
button3OAT23.place(x=X+x3OAT+3, y=yg+60)

button3OAT24 = tk.Button(root, text="Q1", width=4, height=2)
button3OAT24.place(x=X+x3OAT+43, y=yg+60)

# Pack the canvas y empieza the main loop (bucle principal).
canvas.pack()
root.mainloop()
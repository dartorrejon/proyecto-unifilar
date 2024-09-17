from prueba import rect_bg

def when_clicked():
    global rect_bg
    if rect_bg == "red":
        rect_bg = "green"
    else:
        rect_bg = "red"
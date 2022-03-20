from tkinter import *

W, H = 10, 20
TILE = 45
GAME_RES = W * TILE, H * TILE
RES = 600, 400
FPS = 6

tk = Tk()

tk.title("Tank")

canvas = Canvas(tk, width=RES[0], height=RES[1], bg="white", highlightthickness=0)
canvas.pack()


class border:
    def __init__(self):
        canvas.create_rectangle(0, 0, 10, RES[1], fill="black")
        canvas.create_rectangle(0, 0, RES[0], 10, fill="black")
        canvas.create_rectangle(RES[0] - 10, 0, RES[0], RES[1], fill="black")
        canvas.create_rectangle(RES[0] - 10, RES[1] - 10, 0, RES[1], fill="black")

class Tank:
    pass
tank = Tank()
tank.pos1_X = 50
tank.pos1_Y = 50
tank.pos2_X = 70
tank.pos2_Y = 70
tank.speed = 10
tank.holder = "pl"
tank.cl = "green"
tank.shap = canvas.create_rectangle(tank.pos1_X, tank.pos1_Y, tank.pos2_X, tank.pos2_Y, fill=tank.cl)

brd = border()

#class Motion()
#    pass

tk.mainloop()

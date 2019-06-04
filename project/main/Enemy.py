import tkinter as tk
import os
import random
import string
import math

class Enemy(object):
    def __init__(self, *args, **kwargs):
        self.canvas_width = 1920
        self.canvas_height = 1080

        self.item_id = ''
        self.filename = ''
        self.image = None
        self.canvas = None
        self.speed_var = .005
        self.direction_var = 1
        self.img1_direction = 1
        self.curve_radius = 110
        # Initializes Windows 10 center coordinates
        self.x_var = 0.0
        self.y_var = 0.0
        self.angle = 0
        self.x_dist = 0
        self.y_dist = 0

    def create(self, filename, canvas):
        self.filename = os.getcwd() + filename
        self.image = tk.PhotoImage(file=self.filename)
        self.canvas = canvas
        self.item_id = canvas.create_image(self.x_var, self.x_var, image=self.image, tag=self.item_id, state="hidden")
        self.arc_id = self.canvas.create_arc((self.canvas_width / 2 + self.curve_radius,
                                              self.canvas_height / 2 + self.curve_radius,
                                              self.canvas_width / 2 - self.curve_radius,
                                              self.canvas_height / 2 - self.curve_radius),
                                             outline="#FF0000", style="arc", width=1, extent=5,
                                             start=self.angle)

    def set_canvas_height(self, tuple):
        self.canvas_width = tuple[0]
        self.canvas_height = tuple[1]

    def spawn(self):

        self.canvas.delete(self.item_id)
        self.x_var = 0
        self.y_var = 0

        self.item_id = self.canvas.create_image(self.x_var, self.x_var, image=self.image, tag=self.item_id, state="hidden")
        h_width = self.canvas_width/2
        h_height = self.canvas_height/2

        self.angle = float(random.randint(0, 480) % 360 )
        edge = random.randint(1,4)
        if edge == 1:
            self.move(0, random.randint(0,self.canvas_height))
        if edge == 2:
            self.move(random.randint(0,self.canvas_width),0)
        if edge == 3:
            self.move(self.canvas_width, random.randint(0,self.canvas_height))
        if edge == 4:
            self.move(random.randint(0,self.canvas_width),self.canvas_height)

        self.angle = (90 + math.degrees(math.atan2((h_width - self.x_var),(h_height-self.y_var))))

        self.canvas.itemconfig(self.item_id, state="normal")
        self.canvas.itemconfig(self.arc_id, start=self.angle)
        self.x_dist = self.canvas_width/2 - self.x_var
        self.y_dist = self.canvas_height/2 - self.y_var


    def move(self, x, y):
        self.x_var += x
        self.y_var += y
        self.canvas.move(self.item_id, x, y)

    def move_towards_center(self):
        self.move(self.x_dist*self.speed_var, self.y_dist*self.speed_var)

    def update_speed(self, val):
        self.speed_var *= val
        #print(self.speed_var)

    def reset_speed(self):
        self.speed_var = .005
import tkinter as tk
import os
import random
import string
import math
import PIL
from PIL import Image

class Enemy(object):
    def __init__(self, *args, **kwargs):
        self.canvas_width = 1920
        self.canvas_height = 1080

        self.item_id = ''
        self.filename = ''
        self.image = None
        self.canvas = None
        self.speed_var = .008

        self.curve_radius = 110
        # Initializes Windows 10 center coordinates
        self.x_var = 0.0
        self.y_var = 0.0
        self.angle = 0.0
        self.x_dist = 0.0
        self.y_dist = 0.0
        self.imglist, self.filelist = self.get_images()

    def create(self, filename, canvas):
        self.filename = os.getcwd() + filename
        self.image = tk.PhotoImage(file=self.filename)
        self.canvas = canvas
        self.item_id = canvas.create_image(self.x_var, self.x_var, image=self.image, tag=self.item_id, state="hidden")


    def set_canvas_height(self, tuple):
        self.canvas_width = tuple[0]
        self.canvas_height = tuple[1]

    def spawn(self):

        self.canvas.delete(self.item_id)
        self.x_var = 0
        self.y_var = 0

        self.image = self.imglist[random.randint(0, len(self.imglist)-1)]
        self.item_id = self.canvas.create_image(self.x_var, self.x_var, image=self.image, tag=self.item_id, state="hidden")

        h_width = self.canvas_width/2
        h_height = self.canvas_height/2

        self.angle = float(random.randint(0, 480) % 360 )
        edge = random.randint(1,4)
        if edge == 1:
            self.move(0, random.randint(0,self.canvas_height))
        if edge == 2:
            self.move(random.randint(0,self.canvas_width/4),0)
        if edge == 3:
            self.move(self.canvas_width, random.randint(0,self.canvas_height))
        if edge == 4:
            self.move(random.randint(0,self.canvas_width/4),self.canvas_height)

        self.angle = (90 + math.degrees(math.atan2((h_width - self.x_var),(h_height-self.y_var))))

        self.canvas.itemconfig(self.item_id, state="normal")
        self.x_dist = self.canvas_width/2.0 - self.x_var
        self.y_dist = self.canvas_height/2.0 - self.y_var


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
        self.speed_var = .008

    def get_images(self, directory=None):
        """ Returns PIL.Image objects for all the images in directory.

        If directory is not specified, uses current directory.
        Returns a 2-tuple containing
        a list with a  PIL.Image object for each image file in root_directory, and
        a list with a string filename for each image file in root_directory
        """

        if directory is None:
            directory = os.getcwd() + "\modified_img" # Use working directory if unspecified

        image_list = []  # Initialize aggregators
        file_list = []

        directory_list = os.listdir(directory)  # Get list of files
        for entry in directory_list:
            absolute_filename = os.path.join(directory, entry)
            try:
                print(absolute_filename)
                image = tk.PhotoImage(file=absolute_filename)
                file_list += [entry]
                image_list += [image]
            except IOError:
                pass  # do nothing with errors tying to open non-images
        return image_list, file_list

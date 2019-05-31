import tkinter as tk

import math

from functools import partial
import os
#from Pillow import Image, ImageTk


root = tk.Tk()


class Main(tk.Frame):
    canvas_width = 1920

    canvas_height = 1080

    score_increase = 1

    x, y = (0, 90)

    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        root.bind("<F11>", self.toggle_fullscreen)

        root.bind("<Escape>", self.end_fullscreen)

        self.state = True

        root.attributes("-fullscreen", self.state)

        master.wm_state("zoomed")

        self.curve_radius = 105

        self.angle_start = 90

        self.score = 20

        self.angle_length = self.score / 100.0 * 360.0

        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, border=0, relief="raised")

        self.canvas.config(bg="#000000")

        self.canvas.pack_propagate(False)

        self.canvas.pack(side="top", fill="both", expand=True)

        self.percent_id = self.canvas.create_text(self.canvas_width / 2, self.canvas_height / 2,

                                                  text=str(int(self.angle_length / 360 * 100)) + "%", fill="#FFFFFF",

                                                  justify="center", font=("Microsoft JhengHei Light", 40),

                                                  anchor="center")

        self.installing_id = self.canvas.create_text(self.canvas_width / 2, (self.canvas_height / 2 - 270),

                                                     text="Installing Windows 10",

                                                     fill="#FFFFFF", justify="center",

                                                     font=("Microsoft JhengHei Light", 36))

        self.restart_id = self.canvas.create_text(self.canvas_width / 2, (self.canvas_height / 2 - 200),

                                                  text="Your PC will restart several times. Sit back and relax.",

                                                  fill="#999999", justify="center", font=("Microsoft YaHei UI", 11),

                                                  anchor="center")

        self.copying_files = self.canvas.create_text((self.canvas_width / 2) - 210, (self.canvas_height - 40),

                                                     text="Copying Files",

                                                     fill="#12498F", justify="center", font=("Microsoft YaHei UI", 11),

                                                     anchor="center")

        self.installing_features_id = self.canvas.create_text((self.canvas_width / 2 - 8), (self.canvas_height - 40),

                                                              text="Installing features and drivers",

                                                              fill="#999999", justify="center",

                                                              font=("Microsoft YaHei UI", 11), anchor="center")

        self.configuring_settings_id = self.canvas.create_text((self.canvas_width / 2) + 220, (self.canvas_height - 40),

                                                               text="Configuring Settings",

                                                               fill="#999999", justify="center",

                                                               font=("Microsoft YaHei UI", 11), anchor="center")

        self.oval_id3 = self.canvas.create_oval(self.canvas_width / 2 + self.curve_radius,

                                                self.canvas_height / 2 + self.curve_radius,

                                                self.canvas_width / 2 - self.curve_radius,

                                                self.canvas_height / 2 - self.curve_radius, outline="#888888",

                                                width=3.3)

        self.oval_id2 = self.canvas.create_oval(self.canvas_width / 2 + self.curve_radius,

                                                self.canvas_height / 2 + self.curve_radius,

                                                self.canvas_width / 2 - self.curve_radius,

                                                self.canvas_height / 2 - self.curve_radius, outline="#555555",

                                                width=3.9)

        self.oval_id = self.canvas.create_oval(self.canvas_width / 2 + self.curve_radius,

                                               self.canvas_height / 2 + self.curve_radius,

                                               self.canvas_width / 2 - self.curve_radius,

                                               self.canvas_height / 2 - self.curve_radius, outline="#666666", width=3.5)

        self.arc_id = self.canvas.create_arc((self.canvas_width / 2 + self.curve_radius,

                                              self.canvas_height / 2 + self.curve_radius,

                                              self.canvas_width / 2 - self.curve_radius,

                                              self.canvas_height / 2 - self.curve_radius),

                                             outline="#12498F", style="arc", width=4.6, extent=-self.angle_length,

                                             start=self.angle_start)

        root.bind('<Motion>', partial(self.motion))

        # Ian's Place
        x_intvar = tk.IntVar()
        x_intvar.set(150)
        y_intvar = tk.IntVar()
        y_intvar.set(150)

        speed_intvar = tk.IntVar()
        speed_intvar.set(15)
        W10Direction_intvar = tk.IntVar()
        W10Direction_intvar.set(1)

        W10Direction = 1

        # Initializes Windows 10 center coordinates
        W10x_var = tk.IntVar()
        W10x_var.set(300)
        W10y_var = tk.IntVar()
        W10y_var.set(500)

        self.image10 = os.getcwd() + ".\windows10.png"
        self.photo10 = tk.PhotoImage(file=self.image10)

        self.w10item = self.canvas.create_image(550, 550, image=self.photo10)  # <--- Save the return value of the create_* method.

    def toggle_fullscreen(self, event=None):
        self.state = not self.state

        root.attributes("-fullscreen", self.state)

        return "break"

    def end_fullscreen(self, event=None):
        self.state = False

        root.attributes("-fullscreen", False)

        return "break"

    def update_bar(self):
        self.angle_length = self.score / 100.0 * 360.0

    def increase_score(self):
        self.score += self.score_increase

        self.update_bar()

        self.canvas.itemconfig(self.arc_id, extent=-self.angle_length)

        self.canvas.itemconfig(self.percent_id, text=str(int(self.angle_length / 360 * 100)) + "%")

    def update_rotation(self, x, y):
        self.angle_start = math.degrees(
            math.atan2((x - self.canvas_width / 2), (y - self.canvas_height / 2))) - 15 - self.angle_length / 2

        self.canvas.itemconfig(self.arc_id, start=self.angle_start)

    def motion(self, event):
        global x, y

        x, y = event.x, event.y

        self.update_rotation(x, y)


if __name__ == "__main__":
    view = Main(root)

    view.pack(side="top", fill="both", expand=True)

    root.mainloop()

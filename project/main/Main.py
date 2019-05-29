import tkinter as tk
import math
from functools import partial

root = tk.Tk()
class Main(tk.Frame):
    canvas_width = 1920
    canvas_height = 1000
    score_increase = 1
    x, y = (0, 90)


    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.curve_radius = 125
        self.angle_start = 90
        self.score = 20
        self.angle_length = self.score/100.0*360.0

        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height)
        self.canvas.config(bg="#000000")
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
                                                     fill="#3479D7", justify="center", font=("Microsoft YaHei UI", 11),
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
                                                self.canvas_height / 2 - self.curve_radius, outline="#666666",
                                                width=3.9)
        self.oval_id = self.canvas.create_oval(self.canvas_width / 2 + self.curve_radius,
                                               self.canvas_height / 2 + self.curve_radius,
                                               self.canvas_width / 2 - self.curve_radius,
                                               self.canvas_height / 2 - self.curve_radius, outline="#999999", width=3.5)

        self.arc_id = self.canvas.create_arc((self.canvas_width / 2 + self.curve_radius,
                                              self.canvas_height / 2 + self.curve_radius,
                                              self.canvas_width / 2 - self.curve_radius,
                                              self.canvas_height / 2 - self.curve_radius),
                                             outline="#3479D7", style="arc", width=4.6, extent=-self.angle_length,
                                             start=self.angle_start)
        self.increase_score()
        root.bind('<Motion>', partial(self.motion))
    def update_bar(self):
        self.angle_length = self.score/100.0*360.0

    def increase_score(self):
        self.score += self.score_increase
        self.update_bar()
        self.canvas.itemconfig(self.arc_id, extent=-self.angle_length)
        self.canvas.itemconfig(self.percent_id, text=str(int(self.angle_length / 360 * 100)) + "%")

    def update_rotation(self, x, y):
        self.angle_start = math.degrees(math.atan2((x-self.canvas_width/2),(y-self.canvas_height/2)))-15-self.angle_length/2
        self.canvas.itemconfig(self.arc_id, start=self.angle_start)
        print(self.angle_start)

    def motion(self, event):
        global x, y
        x, y = event.x, event.y
        self.update_rotation(x, y)




if __name__ == "__main__":

    view = Main(root)
    view.pack(side="top", fill="both", expand=True)

    root.mainloop()

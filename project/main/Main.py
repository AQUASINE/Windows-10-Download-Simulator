import tkinter as tk

class Main(tk.Frame):
    canvas_width = 1800
    canvas_height = 900
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height)
        self.canvas.config(bg="#000000")
        self.canvas.pack(side="top", fill="both", expand=True)

        self.percent_id = self.canvas.create_text(self.canvas_width/2, self.canvas_height/2, text="0%", fill="#FFFFFF", justify="center", font=("Microsoft JhengHei Light", 40))
        self.installing_id = self.canvas.create_text(self.canvas_width / 2, (self.canvas_height / 2 - 250), text="Installing Windows 10",
                                               fill="#FFFFFF", justify="center", font=("Microsoft JhengHei Light", 32))
        self.installing_id = self.canvas.create_text(self.canvas_width / 2, (self.canvas_height / 2 - 180), text="Your PC will restart several times. Sit back and relax.",
                                               fill="#999999", justify="center", font=("Microsoft YaHei UI", 10))

    def on_change_text(self):
        self.canvas.itemconfig(self.text_id, text="Goodbye, world")

if __name__ == "__main__":
    root = tk.Tk()
    view = Main(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()
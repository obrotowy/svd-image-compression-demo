import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import compression
import numpy as np

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = "SVD Image Compression Demo"
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        self.img = None
        self.canvas = tk.Label(self)
        self.canvas.pack()
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open image file", command=self.open_file)
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.slider = tk.Scale(self, orient="horizontal", label="Threshold", command=self.update_image)

    def open_file(self):
        filepath = filedialog.askopenfilename()
        if not filepath:
            return
        
        try:
            self.img = Image.open(filepath)
        except:
            messagebox.showerror("Error", f"Failed to load {filepath}")
        else:
            self.display_photo(self.img)
            self.slider.configure(from_=1, to=np.min(np.array(self.img).shape[:1]))
            self.slider.pack()

    def display_photo(self, img: Image):
        self.img_tk = ImageTk.PhotoImage(img)
        self.canvas.configure(image=self.img_tk)
    
    def update_image(self, threshold):
        img = compression.compress_image(np.array(self.img), int(threshold))
        self.display_photo(Image.fromarray(img))


if __name__ == "__main__":
    w = App()
    w.mainloop()
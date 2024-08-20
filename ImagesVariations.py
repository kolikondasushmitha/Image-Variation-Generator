import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageEnhance, ImageTk
import numpy as np
import os

class ImageVariationApp:
    def __init__(self, root):  # Corrected __init__ method
        self.root = root
        self.root.title("Image Variation Generator")
        self.root.geometry("800x600")
        
        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=20)
        
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()
        
        self.save_btn = tk.Button(root, text="Save Selected Image", command=self.save_image, state=tk.DISABLED)
        self.save_btn.pack(pady=20)
        
        self.variations = []
        self.current_image = None
        
    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.original_image = Image.open(file_path)
            self.generate_variations()
            self.display_images()
            self.save_btn.config(state=tk.NORMAL)
        
    def generate_variations(self):
        self.variations = []
        saturations = np.linspace(0.5, 1.5, 5)
        contrasts = np.linspace(0.5, 1.5, 5)
        colors = np.linspace(0.5, 1.5, 5)
        
        for saturation in saturations:
            for contrast in contrasts:
                for color in colors:
                    enhancer_sat = ImageEnhance.Color(self.original_image)
                    img_sat = enhancer_sat.enhance(saturation)
                    
                    enhancer_contrast = ImageEnhance.Contrast(img_sat)
                    img_contrast = enhancer_contrast.enhance(contrast)
                    
                    enhancer_color = ImageEnhance.Brightness(img_contrast)
                    img_color = enhancer_color.enhance(color)
                    
                    self.variations.append(img_color)
                    
    def display_images(self):
        self.canvas.delete("all")
        self.thumbnails = []
        for idx, img in enumerate(self.variations):
            thumbnail = img.copy()
            thumbnail.thumbnail((100, 100))
            tk_img = ImageTk.PhotoImage(thumbnail)
            self.thumbnails.append(tk_img)
            x_pos = 10 + (idx % 10) * 60
            y_pos = 10 + (idx // 10) * 60
            img_id = self.canvas.create_image(x_pos, y_pos, image=tk_img)
            self.canvas.tag_bind(img_id, "<Button-1>", lambda e, i=idx: self.select_image(i))
    
    def select_image(self, index):
        self.current_image = self.variations[index]
        messagebox.showinfo("Image Selected", f"Selected variation {index + 1}")
    
    def save_image(self):
        if self.current_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                self.current_image.save(save_path)
                messagebox.showinfo("Saved", "Image saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageVariationApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageEnhance, ImageTk
import numpy as np
import seaborn as sns
from tkinter.ttk import Progressbar, Style

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % tuple(int(x * 255) for x in rgb)

class ImageVariationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Variation Generator")
        self.root.geometry("1000x800")

        # Use a Seaborn color palette for UI colors and convert to hex
        palette = sns.color_palette("Blues")
        upload_btn_color = rgb_to_hex(palette[2])
        save_btn_color = rgb_to_hex(palette[3])

        # Enhance buttons with style
        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image, bg=upload_btn_color, fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
        self.upload_btn.pack(pady=20)

        self.progress = Progressbar(root, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress.pack(pady=10)

        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, width=1000, height=600)
        self.scrollbar = tk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.save_btn = tk.Button(root, text="Save Selected Image", command=self.save_image, state=tk.DISABLED, bg=save_btn_color, fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
        self.save_btn.pack(pady=20)

        self.variations = []
        self.current_image = None

        self.root.bind("<Configure>", self.on_resize)

    def upload_image(self):
        # Reset canvas and progress bar
        self.canvas.delete("all")
        self.progress['value'] = 0
        self.progress.update()

        # Simulate upload progress
        for i in range(100):
            self.progress['value'] += 1
            self.root.update_idletasks()
            self.root.after(10)  # Simulate a delay for visual effect

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

                    self.variations.append((img_color, saturation, contrast, color))

    def display_images(self):
        self.canvas.delete("all")
        self.thumbnails = []
        thumbnail_size = (150, 150)  # Thumbnail size
        padding = 20  # Padding between images
        canvas_width = self.canvas.winfo_width()
        columns = max(1, canvas_width // (thumbnail_size[0] + padding))

        for idx, (img, saturation, contrast, color) in enumerate(self.variations):
            thumbnail = img.copy()
            thumbnail.thumbnail(thumbnail_size)
            tk_img = ImageTk.PhotoImage(thumbnail)
            self.thumbnails.append(tk_img)
            x_pos = 10 + (idx % columns) * (thumbnail_size[0] + padding)
            y_pos = 10 + (idx // columns) * (thumbnail_size[1] + padding + 40)  # Adjust y position to accommodate text
            img_id = self.canvas.create_image(x_pos, y_pos, image=tk_img, anchor=tk.NW)
            self.canvas.create_text(x_pos + thumbnail_size[0] // 2, y_pos + thumbnail_size[1] + 10,
                                    text=f"Saturation: {saturation:.2f}\nContrast: {contrast:.2f}\nBrightness: {color:.2f}",
                                    anchor=tk.N)
            self.canvas.tag_bind(img_id, "<Button-1>", lambda e, i=idx: self.select_image(i))

        self.canvas.config(scrollregion=self.canvas.bbox("all"))  # Update scroll region

    def on_resize(self, event):
        self.display_images()

    def select_image(self, index):
        self.current_image = self.variations[index][0]
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




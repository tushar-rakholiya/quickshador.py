import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from PIL import ImageTk, Image
from quickshador.core import QuickShador


class QuickShadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QuickShador GUI")
        self.qs = QuickShador()

        self.original_image = None
        self.processed_image = None
        self.display_image = None
        self.shadow_color = (0, 0, 0, 150)

        # UI
        self.label = tk.Label(root, text="QuickShador GUI", font=("Arial", 14, "bold"))
        self.label.pack(pady=10)

        self.canvas = tk.Canvas(root, width=400, height=400, bg="gray")
        self.canvas.pack()

        self.load_btn = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_btn.pack(pady=5)

        self.shadow_btn = tk.Button(root, text="Apply Shadow", command=self.apply_shadow, state=tk.DISABLED)
        self.shadow_btn.pack(pady=5)

        self.save_btn = tk.Button(root, text="Save Image", command=self.save_image, state=tk.DISABLED)
        self.save_btn.pack(pady=5)

        # Shadow settings
        self.settings_frame = tk.Frame(root)
        self.settings_frame.pack(pady=10)

        tk.Label(self.settings_frame, text="Blur:").grid(row=0, column=0)
        self.blur_slider = tk.Scale(self.settings_frame, from_=0, to=50, orient="horizontal")
        self.blur_slider.set(10)
        self.blur_slider.grid(row=0, column=1)

        tk.Label(self.settings_frame, text="Offset X:").grid(row=1, column=0)
        self.offset_x = tk.Scale(self.settings_frame, from_=-100, to=100, orient="horizontal")
        self.offset_x.set(10)
        self.offset_x.grid(row=1, column=1)

        tk.Label(self.settings_frame, text="Offset Y:").grid(row=2, column=0)
        self.offset_y = tk.Scale(self.settings_frame, from_=-100, to=100, orient="horizontal")
        self.offset_y.set(10)
        self.offset_y.grid(row=2, column=1)

        tk.Label(self.settings_frame, text="Opacity (%):").grid(row=3, column=0)
        self.opacity_slider = tk.Scale(self.settings_frame, from_=0, to=100, orient="horizontal")
        self.opacity_slider.set(60)
        self.opacity_slider.grid(row=3, column=1)

        self.color_btn = tk.Button(self.settings_frame, text="Pick Shadow Color", command=self.pick_color)
        self.color_btn.grid(row=4, column=0, columnspan=2, pady=5)

    def pick_color(self):
        color = colorchooser.askcolor(title="Choose Shadow Color")[0]
        if color:
            r, g, b = map(int, color)
            a = int(self.opacity_slider.get() * 2.55)
            self.shadow_color = (r, g, b, a)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
        if file_path:
            self.original_image = self.qs.extractor.load_image(file_path)
            self.show_image(self.original_image)
            self.shadow_btn.config(state=tk.NORMAL)

    def apply_shadow(self):
        if self.original_image:
            blur = self.blur_slider.get()
            offset = (self.offset_x.get(), self.offset_y.get())
            color = self.shadow_color
            shadowed = self.qs.creator.create_drop_shadow(
                self.original_image,
                offset=offset,
                shadow_color=color,
                blur_radius=blur
            )
            self.processed_image = shadowed
            self.show_image(shadowed)
            self.save_btn.config(state=tk.NORMAL)

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path and self.processed_image:
            self.processed_image.save(file_path)
            messagebox.showinfo("Saved", f"Image saved to {file_path}")

    def show_image(self, image):
        preview = image.copy().resize((400, 400), Image.Resampling.LANCZOS)
        self.display_image = ImageTk.PhotoImage(preview)
        self.canvas.create_image(0, 0, anchor="nw", image=self.display_image)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuickShadorApp(root)
    root.mainloop()

import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
from PIL import Image
import cv2
import os
from html_export import export_file
import pytesseract


class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OCRApp - Text Recognition")
        self.root.geometry("600x600")
        self.root.resizable(False,False)

        self.image_path = None
        self.processed_cv2 = None

        self.init_ui()


    def init_ui(self):
        frame_top = tk.Frame(self.root)
        frame_top.pack(pady=10)

        tk.Button(frame_top, text="Load Image", command=self.load_image).grid(row=0, column=0, padx=5)
        tk.Button(frame_top, text="Save Text", command=self.save_text).grid(row=0, column=1, padx=5)
        tk.Button(frame_top, text="Export as HTML", command=self.save_as_html).grid(row=0, column=2, padx=5)
        tk.Button(frame_top, text="Show processed", command=self.show_processed).grid(row=0, column=3, padx=5)
        tk.Button(frame_top, text="Reset", command=self.reset).grid(row=0, column=4, padx=5)

        tk.Label(frame_top, text="Language:").grid(row=0, column=5, padx=5)
        self.lang_var = tk.StringVar(value="eng")
        self.combo_lang=ttk.Combobox(frame_top, textvariable=self.lang_var, values=["eng", "srp","deu", "fra"], width=5)
        self.combo_lang.grid(row=0, column=6)

        self.text_output = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=25)
        self.text_output.pack(padx=10,pady=10)

    
    def preprocess_image(self, filepath):
        try:
            img = cv2.imread(filepath)
            if img is None:
                raise ValueError("Invalid or unsupported iamge format")
            
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5,5),0)
            thres = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,2)

            self.processed_cv2 = thres
            return Image.fromarray(thres)
        except Exception as e:
            messagebox.showerror("Error", f"Image preprocessing failed:\n{e}")
            return None
        
    
    def load_image(self):
        filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff")])
        if not filepath:
            return
        
        self.image_path=filepath
        processed=self.preprocess_image(filepath)
        if not processed:
            return
        
        try:
            lang = self.lang_var.get()
            text = pytesseract.image_to_string(processed, lang=lang)
            self.text_output.delete(1.0, tk.END)
            self.text_output.insert(tk.END, text)

        except Exception as e:
            messagebox.showerror("Error", f"OCR failed\n{e}")

    
    def save_text(self):
        text = self.text_output.get(1.0, tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "No text to save")
            return
        
        file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file:
           file.write(text)
           file.close()
           messagebox.showinfo("Success", "Text successfully saved")

           

    def save_as_html(self):
        text = self.text_output.get(1.0, tk.END).strip()
        if not text or not self.image_path:
            messagebox.showwarning("Warning", "Image and text are required")
            return
        
        html_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML Files", "*.html")])
        if not html_path:
            return
        
        image_name = os.path.basename(self.image_path)
        copy_path = os.path.join(os.path.dirname(html_path), image_name)

        if os.path.abspath(self.image_path)!=os.path.abspath(copy_path):
            shutil.copy(self.image_path, copy_path)

        html = f"""<!DOCTYPE html>
        
    <html>
    <head>
        <meta charset="utf-8">
        <title>OCR Result</title>

    </head>
    <body>
        <h2>Original iamge:</h2>
        <img src={image_name} alt="OCR Image" style="max-width:100%;">
        <h2>Recognized Text:</h2>
        <pre>{text}</pre>
    </body>
    </html>
    """
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        
        messagebox.showinfo("Success", "HTML file saved successfully")

    def show_processed(self):
        if self.processed_cv2 is not None:
            cv2.imshow("Processed image", self.processed_cv2)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        else:
            messagebox.showinfo("Info", "No processed image available")

    
    def reset(self):
        self.text_output.delete(1.0, tk.END)
        self.image_path=None
        self.processed_cv2 = None
        self.lang_var.set("eng")


if __name__=="__main__":
    root=tk.Tk()
    app = OCRApp(root)
    root.mainloop()

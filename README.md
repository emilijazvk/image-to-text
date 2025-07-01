**OCRApp – Image to Text with GUI**

OCRApp is a desktop application built with Python that uses Tesseract OCR to extract text from images. The application features a graphical interface (Tkinter) and offers options to load an image, extract and save text, preview processed image, and export results as HTML.

---

✨ **Features**

- 📂 Load image (`.png`, `.jpg`, `.jpeg`, `.bmp`, `.tiff`)
- 🔤 Extract text using Tesseract OCR
- 🔧 Image preprocessing with OpenCV (grayscale, blur, thresholding)
- 🌐 Language selection (`eng`, `srp`, `deu`, `fra`)
- 💾 Save text as `.txt`
- 🌐 Export HTML with original image and recognized text
- 👁️ Show preprocessed image
- ♻️ Reset interface


---

⚙️ **Requirements**

- Python 3.8 or newer
- Tesseract OCR engine

 📦 **Python dependencies**

Install required packages:

```bash
pip install -r requirements.txt
```

🧠 **Installing Tesseract OCR**
🪟 Windows
Download the Tesseract installer from UB Mannheim GitHub

Install it (recommended path: C:\Program Files\Tesseract-OCR)  
Add it to the system PATH:

Open Start → "Environment Variables"

Edit the Path variable and add:  
C:\Program Files\Tesseract-OCR

🌍 **Language Support**  
By default, only English (eng) is installed.

To add more languages:

Visit: https://github.com/tesseract-ocr/tessdata

Download the .traineddata files (e.g., srp.traineddata, deu.traineddata, etc.)

Copy them to the folder:  
C:\Program Files\Tesseract-OCR\tessdata

🚀 **Running the Application** 
After installing dependencies and Tesseract, run the app:  
python ocr_app.py

📸 **Screenshot**
![image](https://github.com/user-attachments/assets/7ca54975-ec86-4843-a54b-227a34f0bac5)


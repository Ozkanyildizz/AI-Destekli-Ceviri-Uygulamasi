from PIL import Image
import pytesseract
from tkinter import filedialog, messagebox

class OCRReader:
    def __init__(self, tesseract_path=None):
        if tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
    
    def extract_text(self, image_path):
        try:
            # Görüntüyü yükle
            img = Image.open(image_path)

            # OCR ile metni çıkar
            text = pytesseract.image_to_string(img)
            # text = pytesseract.image_to_string(img, lang='tur') # spesfik bir dil tercihi yapabilisiniz
            return text
        except Exception as e:
            messagebox.showerror("Hata", f"Yapay zeka hatası: {e}")
    
    def save_text(self, text, output_file):
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(text)
            print(f"Metin {output_file} dosyasına kaydedildi.")
        except Exception as e:
            print(f"Dosya kaydetme hatası: {e}")

if __name__ == "__main__":
    tesseract_path = "C:\Program Files\Tesseract-OCR\\tesseract.exe" # yolu belirtmeniz gerekir
    reader = OCRReader(tesseract_path)
    file_path = filedialog.askopenfilename(
    title="Bir resim dosyası seçin",
    filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
        
    # Metni çıkar ve dosyaya yazdır

    extracted_text = reader.extract_text(file_path)

    # output_file = "sonuc.txt"
    # print("Çıkarılan Metin:\n", extracted_text)
    # reader.save_text(extracted_text, output_file)

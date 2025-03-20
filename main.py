import customtkinter as ctk
import pyperclip
import threading
import time
from googletrans import Translator, LANGUAGES
from tkinter import  messagebox, filedialog
import geminiai
import asyncio
from extractText import OCRReader

class TranslatorApp:
    def __init__(self, root):
        self.app = root
        self.app.title("AI Destekli Çeviri")
        self.app.geometry("900x700")

        # self.app.iconbitmap("/Directory/icon.ico")

     
        # CustomTkinter temasını ayarla
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Scrollable Content Frame oluşturma
        self.scrollable_frame = ctk.CTkScrollableFrame(self.app, corner_radius=10, fg_color="#2b2b2b")
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Başlık
        self.title = ctk.CTkLabel(self.scrollable_frame, text="AI Destekli Çeviri", font=("Arial", 24))
        self.title.pack(pady=10)

        # Metin kutusu
        self.text_box = ctk.CTkTextbox(self.scrollable_frame, width=800, height=250, font=("Arial", 16))
        self.text_box.pack(pady=10)

        # Dil Seçiminde Kaydırma Ekleme
        self.important_languages = ['english', 'french', 'german', 'spanish', 'turkish', 'italian', 'russian', 'chinese', 'arabic', 'japanese']  # Dilleri isimlerine göre sırala
        self.languages = {lang: lang_code for lang_code, lang in LANGUAGES.items() if lang in self.important_languages}
        # Dil Seçiminde Kaydırma Ekleme
        self.lang_combobox = ctk.CTkComboBox(self.scrollable_frame, values=list(self.languages.keys()), font=("Arial", 14), width=800, height=40)
        self.lang_combobox.set("turkish")  # Varsayılan olarak Türkçe seçildi
        self.lang_combobox.pack(padx=5, pady=5)

        
        
        # Yapay Zeka Soru Alanı
        self.question_entry = ctk.CTkEntry(self.scrollable_frame, width=800, height=40, placeholder_text="Yapay zekaya sorun...", font=("Arial", 14))
        self.question_entry.pack(pady=5)

        # Yapay Zeka Sorusu butonu
        self.ask_button = ctk.CTkButton(
            self.scrollable_frame, 
            text="AI Sor", 
            command=self.handle_ask, 
            corner_radius=10, 
            font=("Arial", 14), 
            fg_color="#4b4b4b", 
            hover_color="#333333"
        )
        self.ask_button.pack(pady=10)

        # Çeviri butonu
        self.translate_button = ctk.CTkButton(self.scrollable_frame, text="Metni Çevir", command=self.handle_translate, corner_radius=10, font=("Arial", 14), fg_color="#4b4b4b", hover_color="#333333")
        self.translate_button.pack(pady=10)

        #text extract buton
        self.text_extract_button = ctk.CTkButton(self.scrollable_frame, text="Resimden metin kopyala", command=self.handle_extract, corner_radius=10, font=("Arial", 14), fg_color="#4b4b4b", hover_color="#333333")
        self.text_extract_button.pack(pady=10)

        # Yapay zeka cevabını gösteren kutu
        self.result_box = ctk.CTkTextbox(self.scrollable_frame, width=800, height=300, font=("Arial", 16))
        self.result_box.pack(pady=10)

        # Alt bilgi
        footer = ctk.CTkLabel(self.scrollable_frame, text="© 2025 Özkan AI Destekli Uygulama", font=("Arial", 12))
        footer.pack(pady=5)

        # Clipboard izleme fonksiyonu için thread başlatma
        clipboard_thread = threading.Thread(target=self.update_clipboard, daemon=True)
        clipboard_thread.start()


    def update_clipboard(self):
        last_text = ""
        while True:
            try:
                current_text = pyperclip.paste()
                if current_text != last_text:
                    last_text = current_text
                    self.text_box.delete("1.0", ctk.END)
                    self.text_box.insert(ctk.END, current_text)
            except Exception as e:
                messagebox.showerror("Hata", f"Clipboard hatası: {e}")
            time.sleep(0.5)

    def ask_ai(self):
        question = self.question_entry.get()
        text = self.text_box.get("1.0", ctk.END).strip()

        if not question or not text:
            messagebox.showerror("Hata", "Lütfen metin girin ve soru sorun!")
            return
        
        try:
            prompt = geminiai.Ask(text=text, question=question)
            answer = prompt.ask()
            self.result_box.delete("1.0", ctk.END)
            self.result_box.insert(ctk.END, answer)
            self.question_entry.delete(0, ctk.END)

        except Exception as e:
            messagebox.showerror("Hata", f"Yapay zeka hatası: {e}")

    async def translate_text(self, text):
        target_lang = self.languages[self.lang_combobox.get().lower()]

        if not text:
            messagebox.showerror("Hata", "Çevrilecek metin bulunamadı!")
            return

        try:
            translator = Translator()
            translated = await translator.translate(text, src="auto", dest=target_lang)
            self.result_box.delete("1.0", ctk.END)
            self.result_box.insert(ctk.END, translated.text)
        except Exception as e:
            messagebox.showerror("Hata", f"Çeviri hatası: {e}")

    def extract(self):
        tesseract_path = "C:\Program Files\Tesseract-OCR\\tesseract.exe"

        try:
            reader = OCRReader(tesseract_path)
            file_path = filedialog.askopenfilename(
            title="Bir resim dosyası seçin",
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
            extracted_text = reader.extract_text(file_path)

            self.text_box.delete("1.0", ctk.END)
            self.text_box.insert(ctk.END, extracted_text)
        except Exception as e:
            messagebox.showerror("Hata", f"Metin alınamadı: {e}")

    def handle_extract(self):
        threading.Thread(target=self.extract).start()
    def handle_ask(self):
        threading.Thread(target=self.ask_ai).start()

    def handle_translate(self):
        text = self.text_box.get("1.0", ctk.END).strip()
        threading.Thread(target=self.translate_in_thread, args=(text,)).start()

    def translate_in_thread(self, text):
        asyncio.run(self.translate_text(text))  # Burada asyncio kullanımı güncellendi

# Ana uygulamayı başlatma
if __name__ == "__main__":
    root = ctk.CTk()
    app = TranslatorApp(root)
    root.mainloop()

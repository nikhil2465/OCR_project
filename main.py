'''from kivymd.app import MDApp
from ocr_manager import extract_from_image
from pdf_reader import extract_from_pdf
from tts_manager import save_audio
from file_exporter import save_as_pdf, save_as_docx

class BlindOCRApp(MDApp):
    extracted_text = ""

    def read_image(self):
        self.extracted_text = extract_from_image("sample.jpg")
        print(self.extracted_text)

    def read_pdf(self):
        self.extracted_text = extract_from_pdf("sample.pdf")
        print(self.extracted_text)

    def export_audio(self):
        save_audio(self.extracted_text)
        print("Audio Saved")

    def export_pdf(self):
        save_as_pdf(self.extracted_text)
        print("PDF Saved")

    def export_docx(self):
        save_as_docx(self.extracted_text)
        print("DOCX Saved")

BlindOCRApp().run()
'''

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup

from ocr_manager import extract_from_image
from pdf_reader import extract_from_pdf
from tts_manager import save_audio
from file_exporter import save_as_pdf, save_as_docx


class BlindOCRApp(MDApp):
    extracted_text = ""

    def build(self):
        return Builder.load_file("ui.kv")

    # Generic file chooser
    def open_file(self, callback):
        chooser = FileChooserIconView(
            on_submit=lambda c, s, t: self.handle_selection(s, callback, chooser.popup)
        )
        popup = Popup(title="Select File", content=chooser, size_hint=(0.9, 0.9))
        chooser.popup = popup
        popup.open()

    def handle_selection(self, selection, callback, popup):
        popup.dismiss()
        if selection:
            path = selection[0]
            self.extracted_text = callback(path)
            print(self.extracted_text)

    def read_image(self):
        self.open_file(extract_from_image)

    def read_pdf(self):
        self.open_file(extract_from_pdf)

    def export_audio(self):
        save_audio(self.extracted_text)
        print("Audio saved.")

    def export_pdf(self):
        save_as_pdf(self.extracted_text)
        print("PDF saved.")

    def export_docx(self):
        save_as_docx(self.extracted_text)
        print("DOCX saved.")

    def test_audio(self):
        self.extracted_text="Hello! This is a test audio message."
        self.export_audio()

BlindOCRApp().run()

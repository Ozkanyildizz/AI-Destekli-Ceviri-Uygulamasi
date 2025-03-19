# AI Destekli Çeviri Uygulaması

Bu proje, metin çevirisi ve yapay zeka tabanlı sorulara yanıtlar almak için bir uygulama geliştirilmesini sağlar. Uygulama, **CustomTkinter** ile tasarlanmış bir arayüze sahiptir ve **Google Translate API** ve **Geminiai AI** ile güçlendirilmiştir.

## Özellikler

- **Metin Çeviri:** Kullanıcı, seçilen bir dile metin çevirisi yapabilir.
- **Yapay Zeka Sorusu:** Kullanıcı, yapay zekaya sorular sorarak, metin veya belirli konularda yanıtlar alabilir.
- **Clipboard İzleme:** Uygulama, panoya kopyalanan metni algılar ve metin kutusunda otomatik olarak gösterir. Sizin manuel olarak yapıştımanıza gerek yok.

## Teknolojiler

- Python 3
- CustomTkinter
- Googletrans (Google Translate API)
- Geminiai (AI tabanlı soru-cevap)
- Pyperclip (Clipboard izleme)
- Threading & Asyncio (Verimli işlem yönetimi)

## Gereksinimler

Bu projeyi çalıştırabilmek için aşağıdaki Python kütüphanelerinin yüklü olması gerekir:

- `customtkinter`
- `pyperclip`
- `googletrans`
- `geminiai`
- `threading`
- `asyncio`

### Kütüphaneleri Yüklemek İçin:

```bash
pip install customtkinter pyperclip googletrans geminiai

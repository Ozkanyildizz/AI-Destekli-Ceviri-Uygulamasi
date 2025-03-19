# AI Destekli Çeviri Uygulaması

Bu proje, herhangi bir web sitesi veya belgeden kopyaladığınız metni otomatik olarak alarak çevirisini yapmanızı ve bu metinle ilgili yapay zeka tarafından yanıtlar almanızı sağlamak üzere tasarlanmıştır. Uygulama, **CustomTkinter** kullanılarak şık bir arayüze sahip olup, **Google Translate API** ve **Geminiai AI** teknolojileriyle güçlendirilmiştir.

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

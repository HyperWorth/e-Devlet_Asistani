````markdown
# 🧭 e-Devlet Asistanı

**e-Devlet Asistanı**, vatandaşların kamu hizmetlerine yönelik başvuru süreçlerini daha kolay anlamalarını sağlamak için geliştirilmiş yapay zeka destekli bir rehber uygulamasıdır.

Uygulama, kullanıcının yazdığı başvuru isteğini analiz eder ve ona:
- Gerekli belgeler
- İlgili kurumlar
- Başvuru adımları
- Uyarılar ve tavsiyeler

başlıklarıyla net ve sade bir yönlendirme sunar.

---

## 🔧 Kullanılan Teknolojiler

| Katman | Teknoloji |
|--------|-----------|
| Backend | Python (Flask) |
| Yapay Zeka | Google Gemini (gemini-2.5-flash) |
| UI | HTML, CSS, JS |
| Markdown İşleme | Python markdown paketi |
| Güvenlik | .env ile API anahtarı yönetimi |

---

## 💡 Özellikler

- ✅ Serbest metin analiz yeteneği (örneğin: "Engelli maaşı almak istiyorum")
- ✅ Gemini modeli ile yapılandırılmış yanıt üretimi
- ✅ Belge, kurum ve adım adım açıklama
- ✅ Markdown biçimlendirmesini HTML'ye dönüştürme
- ✅ Kullanıcı deneyimi için loading (spinner) animasyonu

---

## 🖥️ Kurulum ve Çalıştırma

1. Projeyi klonlayın:
```bash
git clone https://github.com/HyperWorth/e-Devlet_Asistani.git
cd e-Devlet_Asistani
````

2. Ortamı kurun:

```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
```

3. `.env` dosyasını oluşturun:

```
GEMINI_API_KEY=senin_gemini_api_anahtarın
```

4. Uygulamayı çalıştırın:

```bash
flask run
```

5. Tarayıcıda aç:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)


## 📁 Proje Yapısı

```
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── gemini_api.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
├── run.py
├── requirements.txt
├── .env (gizli)
├── README.md
```

---

## 📄 Lisans

Bu proje MIT lisansı ile paylaşılmıştır. Detaylar için `LICENSE` dosyasını inceleyin.

---

## 👤 Geliştirici

* Kullanıcı Adı: \[HyperWorth]
* GitHub: [github.com/HyperWorth](https://github.com/HyperWorth)

---

## ✍️ Örnek Kullanım Senaryoları

* “KYK yurt başvurusu nasıl yapılır?”
* “Evlilik yardımı almak istiyorum.”
* “Aile destek programı başvurusu için ne gerekli?”
* “Vergi borcu yapılandırması nasıl yapılır?”


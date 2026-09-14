# 🎓 Akademik Sınav Hazırlık & İnteraktif Soru Çözüm Platformu (PWA)

Bu proje; üniversite lisans/yüksek lisans dönemi **İş Sağlığı ve Güvenliği (İSG)**, **Makine Öğrenmesi (ML)**, **Üretken Yapay Zeka (Generative AI - GAI)** ve **Veri Yapıları (Data Structures - DS)** final sınavlarına çalışma, konu kavrama ve soru tekrarı amacıyla geliştirilmiş **Progressive Web App (PWA)** destekli yerel soru çözüm platformudur.

---

## 🚀 Öne Çıkan Özellikler

* 📱 **PWA & Mobil Cihaz Entegrasyonu:** main.py çalıştırıldığında terminalde otomatik IP ve dinamik QR kod üretir. Telefondan QR kod taranarak aynı yerel ağ üzerinden uygulama mobil tarayıcıda veya ana ekrana eklenerek (PWA) tam ekran kullanılabilir.
* 📚 **Çoklu Ders & Final Modülleri:**
  * 🛡️ **İSG (İş Sağlığı ve Güvenliği):** Mevzuat, risk değerlendirmesi ve iş güvenliği soru setleri.
  * 🤖 **ML (Machine Learning):** Denetimli/denetimsiz öğrenme, regresyon, sınıflandırma ve metrik analiz soruları.
  * 🎨 **GAI (Generative AI):** LLM mimarileri, prompt mühendisliği, difüzyon modelleri ve üretken yapay zeka kavramları.
  * 🌳 **DS (Data Structures):** Ağaçlar, graflar, yığınlar, kuyruklar ve zaman karmaşıklığı analiz soruları.
* ⚡ **İnteraktif Çözüm Modları:** Konu testleri, karışık deneme sınavları, yanlış yapılan soruların analizi ve anlık cevap geribildirimi.
* 📶 **%100 Çevrimdışı (Offline) Desteği:** Service Worker (sw.js) ve yerel statik mimari sayesinde internet bağlantısı olmadan da kesintisiz çalışır.

---

## 🛠️ Teknik Altyapı & Mimarî

* **Arka Yüz (Local Server):** Python http.server, socket, qrcode (Otomatik LAN IP çözümleme ve QR kod konsol render motoru).
* **Ön Yüz (PWA Client):** Vanilla JavaScript (ES6+), Modern CSS3 (Dark/Light Responsive Design), HTML5 Semantic.
* **Depolama & Önbellek:** Service Worker Cache API & LocalStorage.

---

## 💻 Kurulum ve Çalıştırma

1. **Gereksinimler:** Python 3.8+
2. **Uygulamayı Başlatma:**
`ash
python main.py
`
3. **Kullanım:**
   * Bilgisayardan: http://localhost:8000
   * Telefondan: Terminalde beliren QR kodu telefon kamerasıyla okutarak veya gösterilen yerel IP adresine giderek bağlanabilirsiniz.

---

## 👤 Geliştirici
* **Oğuz Taşdemir** — [GitHub](https://github.com/oguztasdemir) • [LinkedIn](https://www.linkedin.com/in/oguz-tasdemir-846889353/)

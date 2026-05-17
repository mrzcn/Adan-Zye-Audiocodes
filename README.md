# 📘 A'dan Z'ye AudioCodes SBC Akademi

![AudioCodes Banner](https://img.shields.io/badge/AudioCodes-v7.20-blue?style=for-the-badge&logo=audiocodes)
![Status](https://img.shields.io/badge/Status-Complete-green?style=for-the-badge)
![Type](https://img.shields.io/badge/Type-Educational%20Book-orange?style=for-the-badge)
![Target](https://img.shields.io/badge/Target-L1_to_L3_Engineers-purple?style=for-the-badge)

Ses teknolojileri dünyasına hoş geldiniz! Bu depo, bir sistem veya ağ mühendisinin sıfırdan başlayıp **AudioCodes Mediant 800 SBC** (v7.20) uzmanı (L3 Seviyesi) olmasına yardımcı olacak şekilde tasarlanmış, yaşayan bir saha eğitim kitabıdır.

---

## 📖 Kitap Hakkında

Bu proje, AudioCodes'un binlerce sayfalık resmi dökümanlarının (User Manual) özetlenmiş hali **değildir.** 

Aksine, resmi kılavuzlarda yer almayan; 
*   **"Gerçekte bu parametre ne işe yarar?"**, 
*   **"Sahada hangi ayar baş ağrıtır?"**, 
*   **"Müşteri şikayeti geldiğinde logda nereye bakmalıyım?"** 

gibi soruların cevaplarını veren, AudioCodes Türkiye Partneri olan **Nolto Teknoloji Anonim Şirketi**'nin 10 yılı aşkın saha tecrübelerinden süzülmüş bir mühendislik rehberidir.

### 🎯 Hedef Kitle
*   **Junior Mühendisler:** VoIP dünyasına yeni giren, "SIP nedir?", "SBC neden firewall'dan farklıdır?" sorularının cevaplarını arayanlar.
*   **Mid-Level Sistem Yöneticileri:** Kurumundaki AudioCodes cihazının bakımını üstlenmiş, Teams entegrasyonu yapmak veya yönlendirme (routing) kuralları yazmak isteyenler.
*   **Senior Ses Mühendisleri:** Karmaşık Regex manipülasyonları yazan, DSP/Transcoding hesaplamaları yapan ve derinlemesine (Wireshark/Ladder Diagram) paket analizi (Troubleshooting) yapanlar.

---

## 🗺️ Eğitim Müfredatı

Eğitim setini modüler bir yapıda, sırasıyla takip etmeniz önerilir:

### 🟢 Modül 1: Temeller ve Sektörel Giriş
VoIP ekosistemini ve AudioCodes'un bu ekosistemdeki yerini anlama.
*   [SBC Nedir ve B2BUA Mimarisi](docs/01-temeller/01-sbc-nedir-ve-b2bua-mimarisi.md) - *Güvenlik duvarı neden sesi geçirmez?*
*   [Neden AudioCodes Seçmeliyiz?](docs/00-sektorel-bakis/02-neden-audiocodes.md) - *Sektörel konumlandırma.*
*   [Teams Direct Routing Dünyası](docs/00-sektorel-bakis/03-teams-direct-routing.md) - *Microsoft Teams ile entegrasyon.*

### 🔵 Modül 2: Ürün Ailesi ve Ekosistem
Donanımları tanıma ve lisans/destek operasyonlarını yönetme.
*   [MediaPack vs Mediant Ailesi](docs/01-audiocodes-urun-ailesi/01-mediapack-vs-mediant.md) - *Hangi donanım nerede kullanılır?*
*   [Donanım, Kapasite ve Lisanslama](docs/01-audiocodes-urun-ailesi/02-mediant-donanim-ve-kapasite.md) - *DSP kapasitesi nasıl hesaplanır?*
*   [OVOC ve CHAMPS Süreçleri](docs/02-ekosistem-ve-operasyon/01-ovoc-nedir-nasil-calisir.md) - *Merkezi yönetim ve teknik destek biletleri.*

### 🟡 Modül 3: Teknik Yapılandırma ve Güvenlik (Core)
SBC'nin kalbine inip konfigürasyon yapma.
*   [IP Arayüzleri ve VLAN Mimarisi](docs/03-cekirdek-yapilandirma/01-ip-interfaces-ve-vlan.md) - *OAMP ve Medya izolasyonu.*
*   [IP-to-IP Yönlendirme Mantığı](docs/04-sinyallesme-ve-yonlendirme/03-ip-to-ip-routing.md) - *Klasifikasyon, Failover ve Yük dengeleme.*
*   [NAT Traversal ve Media Anchoring](docs/05-guvenlik-ve-medya/08-nat-traversal-ve-media-anchoring.md) - *Symmetric NAT ve One-way audio çözümleri.*
*   [Güvenlik (Hardening & DoS)](docs/05-guvenlik-ve-medya/04-hardening-ve-dos-korumasi.md) - *IDS/IPS kuralları ve Access List yönetimi.*
*   [Medya Kaynakları ve DSP Yönetimi](docs/05-guvenlik-ve-medya/06-medya-kaynak-yonetimi-ve-dsp.md) - *Transcoding senaryoları ve DTMF çevirisi.*
*   [Saha Kurulum Standartları (Best Practices)](docs/09-en-iyi-uygulamalar/01-saha-kurulum-standartlari.md) - *Projeyi canlıya almadan önceki kontrol listesi.*

### 🔴 Modül 4: İleri Düzey Analiz ve Referanslar (Uzmanlık)
Sorun giderme ve karmaşık kural setleri yazma.
*   [Syslog ve Message Log Okuma](docs/07-bakim-ve-sorun-giderme/01-syslog-ve-message-log-okuma.md) - *Hata analizi, SIP akışı okuma ve Wireshark kullanımı.*
*   [Message Manipulation (SIP Headers)](docs/06-ileri-duzey-manipulasyon/01-message-manipulation.md) - *SIP başlıklarıyla oynama sanatı.*
*   [Regex Kütüphanesi ve Numara Manipülasyonu](docs/08-ekler-ve-referanslar/02-regex-kutuphanesi.md) - *Sahada hayat kurtaran Regex kalıpları.*
*   [SIP Terimler Sözlüğü](docs/08-ekler-ve-referanslar/01-sip-terimler-sozlugu.md) - *Tüm SIP yanıt kodları ve medya terimleri.*
*   [Faydalı Araçlar (Utilities)](docs/08-ekler-ve-referanslar/05-faydali-araclar-ve-utility.md) - *Syslog Viewer, DConvert ve BootP kurtarma operasyonları.*

---

## 🤝 Katkıda Bulunma

Bu dökümantasyon sürekli gelişen, yaşayan bir organizmadır. Sahada karşılaştığınız ilginç bir sorunu, yazdığınız muhteşem bir Regex kalıbını veya pratik bir çözümü bu rehbere eklemek isterseniz, lütfen [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını okuyun.

## 📈 Öğrenme Yol Haritası
Kendi ilerlemenizi takip etmek için [ROADMAP.md](ROADMAP.md) dosyasını kullanabilirsiniz.

## 🛡️ Telif Hakkı ve Kullanım
Bu içerik **mrzcn** tarafından hazırlanmıştır ve tüm hakları saklıdır. İçerik dijital filigranlar ile korunmaktadır. Detaylar için [LICENSE](LICENSE) dosyasını inceleyiniz.

---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>

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

### 🏁 Bölüm 0: Sektörel Bakış ve Temel Kavramlar
*   [SBC Nedir ve Sektörel Konumu?](docs/00-sektorel-bakis/01-sbc-nedir-ve-sektorel-konumu.md)
*   [Neden AudioCodes? Liderlik Özellikleri](docs/00-sektorel-bakis/02-neden-audiocodes.md)
*   [Microsoft Teams Direct Routing Dünyası](docs/00-sektorel-bakis/03-teams-direct-routing.md)

### 📚 Bölüm 1: Temeller
*   [SBC Nedir ve B2BUA Mimarisi](docs/01-temeller/01-sbc-nedir-ve-b2bua-mimarisi.md) - *Güvenlik duvarı neden sesi geçirmez?*
*   [SIP ve RTP Protokolleri](docs/01-temeller/02-sip-ve-rtp-protokolleri.md)

### 📦 Bölüm 2: AudioCodes Ürün Ailesi & Ekosistem
*   [MediaPack vs. Mediant: Hangisi, Ne Zaman?](docs/01-audiocodes-urun-ailesi/01-mediapack-vs-mediant.md)
*   [Mediant Donanım Ailesi ve Kapasite Rehberi](docs/01-audiocodes-urun-ailesi/02-mediant-donanim-ve-kapasite.md) - *DSP kapasitesi nasıl hesaplanır?*
*   [Software (Sanal) vs. Hardware SBC Karşılaştırması](docs/01-audiocodes-urun-ailesi/03-software-vs-hardware-sbc.md)
*   [Sanal Cihaz Kurulumu ve Lisanslama](docs/02-audiocodes-giris/01-donanim-sanal-ve-lisans.md)
*   [İlk Erişim ve Yönetim Arayüzü](docs/02-audiocodes-giris/02-ilk-erisim-ve-yonetim.md)
*   [OVOC (Merkezi Yönetim) Nedir, Nasıl Çalışır?](docs/02-ekosistem-ve-operasyon/01-ovoc-nedir-nasil-calisir.md)
*   [CHAMPS: Destek ve Garanti Modelleri](docs/02-ekosistem-ve-operasyon/02-champs-destek-modelleri.md)
*   [Lisanslama ve Güncelleme (Firmware) Mantığı](docs/02-ekosistem-ve-operasyon/03-lisanslama-ve-guncelleme.md)

### 🛠 Bölüm 3: Çekirdek Teknik Yapılandırma
*   [IP Interfaces ve VLAN İzolasyonu](docs/03-cekirdek-yapilandirma/01-ip-interfaces-ve-vlan.md) - *OAMP ve Medya izolasyonu.*
*   [Media Realms (RTP Port Yönetimi)](docs/03-cekirdek-yapilandirma/02-media-realms.md)
*   [SIP Interfaces (Sinyalleşme Uçları)](docs/03-cekirdek-yapilandirma/03-sip-interfaces.md)

### 🚀 Bölüm 4: Sinyalleşme ve Yönlendirme
*   [Proxy Sets ve Keep-Alive Mekanizması](docs/04-sinyallesme-ve-yonlendirme/01-proxy-sets-ve-keep-alive.md)
*   [IP Groups: Mantıksal Gruplama](docs/04-sinyallesme-ve-yonlendirme/02-ip-groups.md)
*   [IP-to-IP Routing: Çağrı Trafik Yönetimi](docs/04-sinyallesme-ve-yonlendirme/03-ip-to-ip-routing.md) - *Klasifikasyon ve Yük dengeleme.*
*   [High Availability (HA): Yedeklilik Senaryoları](docs/04-sinyallesme-ve-yonlendirme/04-high-availability-ha.md)

### 🛡 Bölüm 5: Güvenlik ve Medya
*   [IP Profiles: Şeffaflık ve Başlık Ayarları](docs/05-guvenlik-ve-medya/01-ip-profiles.md)
*   [Transcoding ve Codec Yönetimi](docs/05-guvenlik-ve-medya/02-transcoding-ve-coder-rules.md)
*   [SBC Güvenliği ve Sertifika Yönetimi](docs/05-guvenlik-ve-medya/03-guvenlik-tls-ve-sertifika.md)
*   [Hardening ve DoS Koruması](docs/05-guvenlik-ve-medya/04-hardening-ve-dos-korumasi.md) - *IDS/IPS kuralları ve Access List yönetimi.*
*   [ACL ve Firewall Kuralları](docs/05-guvenlik-ve-medya/05-acl-ve-firewall-kurallari.md)
*   [Medya Kaynak Yönetimi ve DSP](docs/05-guvenlik-ve-medya/06-medya-kaynak-yonetimi-ve-dsp.md) - *Transcoding senaryoları ve DTMF çevirisi.*
*   [Ses Kalitesi İzleme ve RTCP-XR](docs/05-guvenlik-ve-medya/07-ses-kalitesi-izleme-rtcp-xr.md)
*   [NAT Traversal ve Media Anchoring](docs/05-guvenlik-ve-medya/08-nat-traversal-ve-media-anchoring.md) - *Symmetric NAT ve One-way audio çözümleri.*

### 🔀 Bölüm 6: İleri Düzey Manipülasyon
*   [Message Manipulation (SIP Header Ezme)](docs/06-ileri-duzey-manipulasyon/01-message-manipulation.md) - *SIP başlıklarıyla oynama sanatı.*
*   [Number Manipulation (Numara Formatlama)](docs/06-ileri-duzey-manipulasyon/02-number-manipulation.md)

### 🔍 Bölüm 7: Bakım ve Sorun Giderme
*   [Syslog ve Message Log Okuma Teknikleri](docs/07-bakim-ve-sorun-giderme/01-syslog-ve-message-log-okuma.md) - *Hata analizi, SIP akışı okuma ve Wireshark kullanımı.*
*   [Firmware Güncelleme ve Yedekleme Prosedürleri](docs/07-bakim-ve-sorun-giderme/02-firmware-guncelleme-yedek.md)

### 🛡️ Bölüm 8: En İyi Uygulamalar (Best Practices)
*   [Saha Kurulum Standartları ve Güvenlik](docs/09-en-iyi-uygulamalar/01-saha-kurulum-standartlari.md) - *Projeyi canlıya almadan önceki kontrol listesi.*

### 📚 Bölüm 9: Ekler ve Referanslar
*   [SIP Terimler Sözlüğü](docs/08-ekler-ve-referanslar/01-sip-terimler-sozlugu.md) - *Tüm SIP yanıt kodları ve medya terimleri.*
*   [Regex (Düzenli İfadeler) Kütüphanesi](docs/08-ekler-ve-referanslar/02-regex-kutuphanesi.md) - *Sahada hayat kurtaran Regex kalıpları.*
*   [INI Dosyası ve CLI Referansı](docs/08-ekler-ve-referanslar/03-ini-dosyasi-referansi.md)
*   [Faks (T.38) Yapılandırma Rehberi](docs/08-ekler-ve-referanslar/04-faks-t38-yapilandirma.md)
*   [Faydalı Araçlar ve Yardımcı Yazılımlar (Utilities)](docs/08-ekler-ve-referanslar/05-faydali-araclar-ve-utility.md) - *Syslog Viewer, DConvert ve BootP.*

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

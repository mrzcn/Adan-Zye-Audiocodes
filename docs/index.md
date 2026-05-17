<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# AudioCodes SBC Akademi: Yeni Mezunlar İçin Eğitim ve Başvuru Rehberi

Bu dökümantasyon, ses teknolojileri dünyasına yeni adım atan mühendisler için bir "SBC El Kitabı" olarak tasarlanmıştır. AudioCodes ekosistemini, ürün ailesini ve teknik yapılandırmaları sıfırdan öğrenmek için aşağıdaki sırayı takip edebilirsiniz.

---

## 📂 Eğitim Müfredatı

### 🏁 Bölüm 0: Sektörel Bakış ve Temel Kavramlar
*   [SBC Nedir ve Sektörel Konumu?](00-sektorel-bakis/01-sbc-nedir-ve-sektorel-konumu.md)
*   [Neden AudioCodes? Liderlik Özellikleri](00-sektorel-bakis/02-neden-audiocodes.md)
*   [Microsoft Teams Direct Routing Dünyası](00-sektorel-bakis/03-teams-direct-routing.md)

### 📦 Bölüm 1: AudioCodes Ürün Ailesi
*   [MediaPack vs. Mediant: Hangisi, Ne Zaman?](01-audiocodes-urun-ailesi/01-mediapack-vs-mediant.md)
*   [Mediant Donanım Ailesi ve Kapasite Rehberi](01-audiocodes-urun-ailesi/02-mediant-donanim-ve-kapasite.md)
*   [Software (Sanal) vs. Hardware SBC Karşılaştırması](01-audiocodes-urun-ailesi/03-software-vs-hardware-sbc.md)

### 🌐 Bölüm 2: Ekosistem ve Operasyon
*   [OVOC (Merkezi Yönetim) Nedir, Nasıl Çalışır?](02-ekosistem-ve-operasyon/01-ovoc-nedir-nasil-calisir.md)
*   [CHAMPS: Destek ve Garanti Modelleri](02-ekosistem-ve-operasyon/02-champs-destek-modelleri.md)
*   [Lisanslama ve Güncelleme (Firmware) Mantığı](02-ekosistem-ve-operasyon/03-lisanslama-ve-guncelleme.md)

### 🛠 Bölüm 3: Çekirdek Teknik Yapılandırma
*   [IP Interfaces ve VLAN İzolasyonu](03-cekirdek-yapilandirma/01-ip-interfaces-ve-vlan.md)
*   [Media Realms (RTP Port Yönetimi)](03-cekirdek-yapilandirma/02-media-realms.md)
*   [SIP Interfaces (Sinyalleşme Uçları)](03-cekirdek-yapilandirma/03-sip-interfaces.md)
*   [SRD Mimarisi ve Ağ Sanallaştırma](03-cekirdek-yapilandirma/04-srd-mimarisi.md)


### 🚀 Bölüm 4: Sinyalleşme ve Yönlendirme
*   [Proxy Sets ve Keep-Alive Mekanizması](04-sinyallesme-ve-yonlendirme/01-proxy-sets-ve-keep-alive.md)
*   [IP Groups: Mantıksal Gruplama](04-sinyallesme-ve-yonlendirme/02-ip-groups.md)
*   [IP-to-IP Routing: Çağrı Trafik Yönetimi](04-sinyallesme-ve-yonlendirme/03-ip-to-ip-routing.md)
*   [High Availability (HA): Yedeklilik Senaryoları](04-sinyallesme-ve-yonlendirme/04-high-availability-ha.md)

### 🛡 Bölüm 5: Güvenlik ve Medya
*   [IP Profiles: Şeffaflık ve Başlık Ayarları](05-guvenlik-ve-medya/01-ip-profiles.md)
*   [Transcoding ve Codec Yönetimi](05-guvenlik-ve-medya/02-transcoding-ve-coder-rules.md)
*   [SBC Güvenliği ve Sertifika Yönetimi](05-guvenlik-ve-medya/03-guvenlik-tls-ve-sertifika.md)
*   [Hardening ve DoS Koruması](05-guvenlik-ve-medya/04-hardening-ve-dos-korumasi.md)
*   [ACL ve Firewall Kuralları](05-guvenlik-ve-medya/05-acl-ve-firewall-kurallari.md)
*   [Medya Kaynak Yönetimi ve DSP](05-guvenlik-ve-medya/06-medya-kaynak-yonetimi-ve-dsp.md)
*   [Ses Kalitesi İzleme ve RTCP-XR](05-guvenlik-ve-medya/07-ses-kalitesi-izleme-rtcp-xr.md)
*   [NAT Traversal ve Media Anchoring](05-guvenlik-ve-medya/08-nat-traversal-ve-media-anchoring.md)

### 🔀 Bölüm 6: İleri Düzey Manipülasyon
*   [Message Manipulation (SIP Header Ezme)](06-ileri-duzey-manipulasyon/01-message-manipulation.md)
*   [Number Manipulation (Numara Formatlama)](06-ileri-duzey-manipulasyon/02-number-manipulation.md)

### 🔍 Bölüm 7: Bakım ve Sorun Giderme
*   [Syslog ve Message Log Okuma Teknikleri](07-bakim-ve-sorun-giderme/01-syslog-ve-message-log-okuma.md)
*   [Firmware Güncelleme ve Yedekleme Prosedürleri](07-bakim-ve-sorun-giderme/02-firmware-guncelleme-yedek.md)

### 🛡️ Bölüm 9: En İyi Uygulamalar (Best Practices)
*   [Saha Kurulum Standartları ve Güvenlik](09-en-iyi-uygulamalar/01-saha-kurulum-standartlari.md)
*   [İsimlendirme ve İndeks Standartları](09-en-iyi-uygulamalar/02-isimlendirme-ve-indeks-standartlari.md)


### 📚 Bölüm 8: Ekler ve Referanslar
*   [SIP Terimler Sözlüğü](08-ekler-ve-referanslar/01-sip-terimler-sozlugu.md)
*   [Regex (Düzenli İfadeler) Kütüphanesi](08-ekler-ve-referanslar/02-regex-kutuphanesi.md)
*   [INI Dosyası ve CLI Referansı](08-ekler-ve-referanslar/03-ini-dosyasi-referansi.md)
*   [Faks (T.38) Yapılandırma Rehberi](08-ekler-ve-referanslar/04-faks-t38-yapilandirma.md)
*   [Faydalı Araçlar ve Yardımcı Yazılımlar (Utilities)](08-ekler-ve-referanslar/05-faydali-araclar-ve-utility.md)

---

> [!IMPORTANT]
> Bu dökümantasyon, **AudioCodes v7.20** sürümü baz alınarak hazırlanmıştır. Modern ses mühendisliğinde uzmanlaşmak için konuları sırasıyla takip etmeniz önerilir.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


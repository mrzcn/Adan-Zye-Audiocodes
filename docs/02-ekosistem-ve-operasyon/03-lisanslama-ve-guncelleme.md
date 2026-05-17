<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# Lisanslama ve Güncelleme Mantığı

AudioCodes SBC'ler "Kullandığın kadar öde" mantığıyla çalışan, yazılım tanımlı kapasiteye sahip cihazlardır. 

## 📌 Lisans Tipleri

Cihazın üzerinde hangi özellikleri kullanabileceğinizi lisans anahtarı belirler. Ana lisans kalemleri şunlardır:

1.  **SBC Sessions:** Aynı anda kaç eş zamanlı çağrı yapılabileceği. (Örn: 20 sessions).
2.  **Transcoding Sessions:** Kaç çağrıda codec dönüşümü yapılabileceği.
3.  **Security (TLS/SRTP):** Şifreleme özelliğinin açık olup olmadığı.
4.  **Advanced Features:** Teams Direct Routing, Voice Quality Monitoring gibi ek özellikler.

## 📌 Lisans Nasıl Yüklenir?

1.  Cihazın seri numarasını (MAC) AudioCodes'a iletirsiniz.
2.  Size uzun bir metin dizisi (License Key) gönderilir.
3.  **Setup > Device > License** menüsünden bu anahtarı yapıştırıp "Load" dersiniz.
4.  Cihazı yeniden başlatmanız (Burn & Reset) gerekebilir.

## 📌 Sürümler Arasındaki Major Farklar (v6.6 - v7.0 - v7.2 - v7.4)

AudioCodes firmware sürümleri geliştikçe sadece arayüz değil, güvenlik yetenekleri ve bulut mimarileri de baştan aşağı değişti. Saha mühendisleri için sürümlerin getirdiği temel farklar şunlardır:

| Özellik / Sürüm | v6.6 ve Öncesi (Legacy) | v7.0 (Geçiş Dönemi) | v7.2 (Modern Standart) | v7.4 (Bulut ve Yapay Zeka) |
| :--- | :--- | :--- | :--- | :--- |
| **Web Arayüzü (GUI)** | Eski HTML/Java tabanlı, yavaş ve hantal yapı. | HTML5 tabanlı, tamamen yenilenmiş modern tasarım. | Daha hızlı filtreleme ve entegre troubleshoot menüleri. | Gelişmiş arama kutuları, modern grafik kartları. |
| **Microsoft Teams** | Lync/Skype entegrasyonu (Teams desteği kısıtlı). | İlk Teams Direct Routing desteği eklendi. | **Sertifikalı Teams Direct Routing**, Media Bypass ve SILK codec. | Cloud-native Teams entegrasyonları ve gelişmiş uyumluluk. |
| **API ve Otomasyon** | Sadece CLI ve SNMP üzerinden yönetim. | İlk REST API desteği (Read-only). | Tam fonksiyonlu **REST API** ve OVOC entegrasyonu. | Dinamik REST API Routing, Webhook bildirimleri. |
| **Güvenlik & Kripto** | Zayıf TLS 1.0/1.1 sürümleri, yavaş şifreleme. | TLS 1.2 desteği, ilk donanımsal kripto optimizasyonları. | **TLS 1.3** ve gelişmiş IDS/IPS anomali tespiti. | OAuth2 token tabanlı SIP yetkilendirmesi, yüksek güvenlik. |
| **Medya & Codec** | Standart G.711, G.729. | AMR, Opus codec destekleri. | **Opus ve SILK** ses codec transcoding optimizasyonları. | AI tabanlı ses filtreleme, dinamik gürültü engelleme. |

---

## 📌 Kapsamlı Major Sürüm Geçiş Rehberi

Eski bir sürümden (Örn: v6.6) en yeni sürüme (Örn: v7.4) doğrudan yükseltme yapmak **cihazın kilitlenmesine (brick) veya konfigürasyonun tamamen bozulmasına** yol açar. Bu yüzden major geçişlerde aşağıdaki disiplin ZORUNLU uygulanmalıdır.

### 1. Güvenli Sürüm Geçiş Yolu (Upgrade Path)
Sürümler arasında parametre adları ve yapısal kurgular değiştiği için geçiş her zaman kademeli yapılmalıdır:
```
[v6.6] ──> [v7.0] ──> [v7.2.202 (Önerilen Ara Sürüm)] ──> [v7.4]
```
*Her adım sonrası cihaz yeniden başlatılmalı ve en az 1 test çağrısı yapılarak konfigürasyonun bozulmadığı doğrulanmalıdır.*

### 2. Geçiş Öncesi Kontrol Listesi (Pre-Upgrade Checklist)
*   **[ ] Lisans Geçerliliği:** Mevcut lisans anahtarınızın yeni major sürümü desteklediğinden emin olun. (Setup > Device > License altından "Grace Period" veya lisans bitiş tarihini kontrol edin).
*   **[ ] Yedekleme:** Cihazdan hem **`.ini`** (ASCII metin formatında konfigürasyon) hem de **`.dat`** (Sertifikaları da içeren tam ikili yedek) dosyalarını bilgisayarınıza indirin.
*   **[ ] Log Kaydı:** Çalışır durumdaki stabil çağrılara ait bir Syslog veya Wireshark kaydı alın (Geçiş sonrası olası ses sorunlarında referans olacaktır).

### 3. Uygulama Adımları (Standalone Cihazlar İçin)
1.  Target sürümün `.cmp` dosyasını AudioCodes portalından indirin.
2.  `Setup > Device > Maintenance > Software Update` menüsünden dosyayı yükleyin.
3.  Yükleme bittikten sonra **"Compare"** aracı varsa eski ve yeni konfigürasyon arasındaki farkları inceleyin (v7.2 ile bazı parametreler otomatik dönüştürülür).
4.  **"Reset"** butonuna basarak cihazı yeni sürümle açın.
5.  İlk çağrıyı başlatıp SIP/RTP loglarını kontrol edin.

### 4. Geri Dönüş Planı (Rollback Strategy)
Eğer geçiş sonrası çözülemeyen bir ses veya sinyalleşme arızası yaşanırsa hızlıca geri dönmek için:
1.  Cihaza eski `.cmp` yazılımını tekrar yükleyin ve Resetleyin.
2.  Yazılım açıldıktan sonra konfigürasyon bozulmuşsa, geçiş öncesi aldığınız yedek `.ini` (veya `.dat`) dosyasını sisteme yükleyip cihazı son bir kez daha resetleyin.

> [!WARNING]
> **Dangling Config Uyarısı:** v6.6'dan v7.2'ye geçerken bazı eski yönlendirme (Routing) parametreleri yeni veritabanı şemasına uyum sağlayamaz ve "Dangling" (havada asılı/tanımsız) kalır. Geçiş sonrası özellikle `IP-to-IP Routing` tablonuzu satır satır gözle kontrol edin.

> [!IMPORTANT]
> Cihazınızın garanti/CHAMPS desteği yoksa yeni major firmware dosyalarını yüklemeniz lisans engeline takılabilir. Güncellemeye başlamadan önce Nolto Partner ekibinden destek durumunuzu teyit edin.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


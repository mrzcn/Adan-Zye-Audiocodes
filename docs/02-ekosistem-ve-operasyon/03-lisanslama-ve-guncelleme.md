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

## 📌 Kapsamlı Lisanslama Modelleri

AudioCodes SBC donanımları veya sanal sürümleri (Mediant VE), üzerinde çalışan yazılım lisansları ile yetenek kazanır. Lisanslama temel olarak iki ana kategoriye ayrılır:

### 1. Kapasite Lisansları (Capacity Licenses)
*   **SBC Sessions:** Cihazın aynı anda aktif olarak işleyebileceği maksimum eş zamanlı çağrı sayısıdır (SIP-to-SIP Session). Lisans sınırına ulaşıldığında, yeni gelen çağrılar SBC tarafından `503 Service Unavailable` veya `480 Temporarily Unavailable` koduyla reddedilir.
*   **Transcoding (DSP) Sessions:** İki uç nokta arasındaki ses codec uyuşmazlığını (Örn: G.711 PCMA konuşan iç santral ile G.729 konuşan operatör) aşmak için ses sinyalinin çözülüp yeniden kodlanması (Transcoding) gerekir. Bu işlem donanımsal DSP veya sanal transcoding lisansı tüketir.

### 2. Özellik Lisansları (Feature Flags)
*   **Security (TLS/SRTP):** Cihazın sinyalleşmeyi TLS (Port 5061) ile şifrelemesi ve medyayı SRTP ile güvenli hale getirmesini aktifleştirir. Bu lisans olmadan cihaz kriptolu çağrı kabul etmez.
*   **High Availability (HA):** İki cihazın yedekli (Active-Standby) çalışabilmesini sağlar. **Kural:** HA mimarilerinde her iki cihaz da birebir aynı SBC Session ve HA lisansına sahip olmak zorundadır.

---

## 📌 Microsoft Teams Direct Routing Lisans Gereksinimleri

Bir AudioCodes SBC'yi Microsoft Teams ortamına entegre etmek istiyorsanız, standart bir SBC lisansı yeterli değildir. Teams Direct Routing mimarisi, yapısı gereği **zorunlu olarak** şu 4 lisans bileşeninin tamamını lisans anahtarınızda (License Key) aktif olarak bulundurmalıdır:

1.  **SW/TEAMS (Microsoft Teams Feature Flag):** SBC'nin Microsoft Teams FQDN'leri ile konuşabilmesini, Teams'e özel SIP header manipülasyonlarını yapabilmesini ve Teams onaylı sinyalleşme protokollerini çalıştırmasını sağlayan **zorunlu** anahtardır.
2.  **SBC Sessions (Eş Zamanlı Çağrı):** Teams üzerinden dış dünyaya (PSTN/Operatör) çıkacak veya iç santrale bağlanacak her aktif çağrı için 1 adet SBC session lisansı yüklü olmalıdır.
3.  **Security (TLS/SRTP):** Microsoft Teams, standart dışı güvensiz SIP (UDP/TCP 5060) ve çıplak RTP ses paketlerini **kesinlikle kabul etmez**. Teams entegrasyonu için sinyalleşmede TLS (5061) ve medyada SRTP şifrelemesi zorunludur. Dolayısıyla şifreleme/güvenlik lisansının aktif olması şarttır.
4.  **Transcoding / DSP Sessions (Opsiyonel ama Şiddetle Önerilen):** 
    *   Microsoft Teams, WAN bacağında ve mobil istemcilerde yüksek ses kalitesi ve bant genişliği tasarrufu sağlamak için **SILK** veya **Opus** (HD Codec) kullanır.
    *   Ancak iç ağdaki IP-PBX veya operatör bacağı genellikle **G.711** veya **G.729** kullanır.
    *   Bu uyuşmazlığı aşmak ve çağrının sorunsuz kurulmasını sağlamak için sesin SBC üzerinde dönüştürülmesi (Transcoding) gerekir. Cihazda yeterli donanımsal DSP chip ve transcoding lisansı olmalıdır.

---

## 📌 Lisans Dağıtım ve Teslimat Yöntemleri

AudioCodes, mimarinize göre iki farklı lisanslama dağıtımı sunar:

### 1. Node-Locked (Cihaza Bağlı Lisans)
Geleneksel lisanslama yöntemidir. Satın alınan lisans anahtarı, cihazın fiziksel **MAC adresine** kilitlenir. 
*   **Taşınabilirlik:** Bu lisans başka bir donanıma veya sanal cihaza aktarılamaz. Donanım arızası durumunda AudioCodes RMA (Değişim) süreci üzerinden yeni cihazın MAC adresine özel lisansın yeniden üretilmesi gerekir.

### 2. Floating / Flex Licensing (Merkezi Havuz)
Bulut (AWS, Azure) veya sanal veri merkezlerinde (Mediant VE) çalışan geniş ölçekli projeler için geliştirilmiştir.
*   **Çalışma Mantığı:** Tüm lisanslar merkezi **OVOC (One Voice Operations Center)** üzerinde toplanır. Sahadaki veya buluttaki sanal SBC'ler açıldığında OVOC'a bağlanarak ihtiyaçları kadar lisansı (Örn: 50 session) havuzdan çeker. 
*   **Avantajı:** Bir SBC kapatıldığında veya silindiğinde, lisanslar otomatik olarak merkezi havuza geri döner ve başka bir SBC tarafından kullanılabilir hale gelir.

---

## 📌 Lisans Nasıl Yüklenir?

1.  Cihazın seri numarasını (MAC veya Product Key) `Status & Diagnostics > Device Info` altından kopyalayıp AudioCodes veya distribütörünüz Nolto'ya iletirsiniz.
2.  Size uzun bir metin dizisi (License Key) gönderilir.
3.  **Setup > Device > License** menüsünden bu anahtarı yapıştırıp **"Load"** dersiniz.
4.  Yeni özellikleri aktif etmek için sağ üstten **"Burn"** butonuna basarak ayarları kalıcı hafızaya kaydedip cihazı yeniden başlatmanız (Reset) gerekir.

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


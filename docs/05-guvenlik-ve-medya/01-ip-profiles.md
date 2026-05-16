<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# IP Profiles

IP Profile, bir IP Group'un sahip olması gereken davranışları (Codec kısıtlamaları, SIP başlık manipülasyonları, şeffaflık ayarları vb.) belirlediğiniz kural setidir.

## 📌 IP Profile Neden Kullanılır?

Her ses sistemi (Genesys, PBX, Operatör) kendine has SIP özellikleri bekler. Örneğin bir sistem `P-Asserted-Identity` başlığı beklerken diğeri bunu reddedebilir. IP Profile bu farklılıkları gidermek (Interworking) için kullanılır.

## 📌 Yapılandırma Adımları (v7.20)

**Menü:** `Setup > Signaling & Media > Coders & Profiles > IP Profiles`

En kritik v7.20 parametreleri:

### 1. SBC Routing & Media Sekmesi
*   **SBC Media Security Mode:** 
    *   `Symmetric`: Bir taraftan SRTP (şifreli) geliyorsa diğer tarafa da SRTP gönderilir.
    *   `Prefer`: Karşı taraf destekliyorsa şifreli, desteklemiyorsa şifresiz devam eder.
    *   `Force`: Mutlaka şifreli olmalı, yoksa çağrıyı sonlandırır.
*   **Extension Coders:** `None` olarak seçilirse SBC codec dönüşümü yapmaz (Transparan geçiş). Eğer transcoding gerekiyorsa buraya ilgili codec'ler eklenmelidir.
*   **SBC Media:** `SBC (Media Anchor)` seçilerek sesin SBC üzerinden geçmesi (Anchor) garanti edilir. NAT senaryolarında bu ayar hayat kurtarıcıdır.
*   **RTCP-XR:** Ses kalitesi analizi için `Enable` yapılmalıdır. Bu sayede MOS skorları üretilir.

### 2. SBC SIP Headers Sekmesi
*   **Remote Representation Mode:** `P-Asserted-Identity` veya `Diversion` başlıklarını yönetir.
    *   `Replace From`: Giden çağrıda 'From' başlığını PAI bilgisiyle değiştirir.
    *   `Add P-Asserted-Identity`: Eğer başlık yoksa yenisini ekler.
*   **Host Part in To/From Header:** Çağrı giderken başlıkların domain kısmına (IP veya Domain) ne yazılacağını belirler. 

### 3. SBC Signaling Sekmesi
*   **Pass-through Unknown Headers:** `Yes` seçilirse, SBC anlamadığı özel SIP başlıklarını silmeden karşı tarafa aktarır. (Örn: `X-` ile başlayan özel CRM başlıkları).
*   **Early Media Transparency:** 183 Session Progress mesajlarının transparan geçişini sağlar.
*   **SBC Signaling QoS Priority:** Sinyalleşme paketlerinin network önceliği (DSCP) buradan belirlenir. (Örn: `CS5` veya `40`).

## 📌 Ses Kalitesi ve QoS
v7.20 sürümünde IP Profile üzerinden **DSCP (Differentiated Services Code Point)** değerlerini hem sinyalleşme hem de medya (RTP) için bacak bazlı ezebilirsiniz. Bu, ses trafiğinin yoğun networklerde kesilmemesi için kritik bir ayardır.

## 📌 Topoloji Gizleme (Topology Hiding)

IP Profile ayarları sayesinde iç ağdaki sunucuların IP adresleri giden paketlerden temizlenir ve yerine SBC'nin IP'si yazılır. Bu, güvenlik için temel bir gerekliliktir.

> [!TIP]
> Eğer "Ses tek taraflı geliyor" veya "Çağrı kurulduktan 30 saniye sonra düşüyor" gibi sorunlar yaşıyorsanız, IP Profile içindeki **SBC Media** ve **Symmetric NAT** ayarlarını kontrol edin.

> [!NOTE]
> IP Profile'da yaptığınız bir değişiklik, o profile bağlı olan **tüm IP Group'ları** anında etkiler.


---
> [!CAUTION]
> **Yasal Uyarı:** Bu dökümantasyon içeriği dijital filigran ve izleme sistemleri ile korunmaktadır. İçeriğin izinsiz kopyalanması, çoğaltılması veya başka platformlarda paylaşılması durumunda yasal süreç işletilecektir.

<div style="display:none">
Source: Adan-Zye-Audiocodes Repository
Owner: mrzcn
Partner: Nolto Teknoloji Anonim Şirketi (AudioCodes Turkey Partner)
Security ID: NLT-800-SBC-SEC-2026
</div>


---
> [!NOTE]
> **Doğrulama Bilgisi:** Bu döküman [Nolto-Internal-DB/verify/mrzcn-800-SBC](http://docs.nolto.com.tr/verify/mrzcn-800-SBC) üzerinden kayıtlıdır. İzinsiz kopyalar bu referans üzerinden takip edilmektedir.

<div style="opacity: 0.01; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>

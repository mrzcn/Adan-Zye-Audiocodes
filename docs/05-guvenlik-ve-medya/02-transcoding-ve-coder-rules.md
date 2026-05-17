<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# Transcoding ve Coder Rules

Transcoding, bir ses bacağından gelen ses formatının (Codec), diğer bacağa gönderilirken anlık olarak başka bir formata dönüştürülmesidir.

## 📌 Codec (Sıkıştırma) Nedir ve Bant Genişliği Matematiği

Ses verisinin nasıl dijitalleştirileceğini ve paketleneceğini belirleyen algoritmadır. 
*   **G.711 (PCMA/PCMU):** Sıkıştırma yapmaz. Saf ses payload'u 64 kbps'dir. Ancak IP/UDP/RTP başlıkları da (header overhead) eklenince networkte kanal başı yaklaşık **80-87 kbps** bant genişliği tüketir. En yüksek (ISDN kalitesinde) ses kalitesini sunar.
*   **G.729 (G.729A/B):** Ses frekanslarını ciddi oranda sıkıştırır. Payload 8 kbps'dir, header ile birlikte kanal başı sadece **24-30 kbps** tüketir. Ses kalitesi biraz düşüktür (robotik veya boğuk gelebilir).

## 📌 Transcoding Ne Zaman Gerekir?

*   Kurum içi Genesys santrali yüksek kalite (G.711) destekliyor, ancak Telekom Operatörü internet hattındaki bant genişliğinden tasarruf etmek için G.729 dayatıyorsa.
*   Bu durumda SBC, Genesys'ten G.711 (87 kbps) aldığı sesi G.729'a (30 kbps) çevirerek operatöre gönderir (Transcoding).
*   **AEC (Acoustic Echo Cancellation) & VAD (Voice Activity Detection):** Transcoding sırasında yankı önleme ve sessizlik anlarında paket göndermeyi durdurma (VAD) özellikleri de DSP üzerinden tetiklenir.

## 📌 Yapılandırma Adımları (v7.20)

**1. Coder Group Oluşturma:**
**Menü:** `Setup > Signaling & Media > Coders & Profiles > Coder Groups`
*   Burada desteklenmesini istediğiniz Codec'leri öncelik sırasına göre eklersiniz (Örn: 1. G.711A, 2. G.729).

**2. IP Profile'a Atama:**
**Menü:** `Setup > Signaling & Media > Coders & Profiles > IP Profiles`
*   İlgili profilde **Extension Coders Group** alanından oluşturduğunuz Coder Group seçilir.

## 📌 DSP Kaynakları

Transcoding işlemi cihaz üzerindeki **DSP (Digital Signal Processor)** donanım kaynağını tüketir. 
*   Eğer cihazda yeterli DSP lisansı veya donanımı yoksa, transcoding gerektiren çağrılar başarısız olur.
*   **Best Practice:** Mümkünse her iki bacağı da aynı codec (Örn: G.711) üzerinde konuşturarak transcoding yükünden (ve gecikmeden) kaçınmaktır.

> [!IMPORTANT]
> AudioCodes SBC'de sesin şeffaf geçmesi isteniyorsa (No Transcoding), her iki IP Group'un profilinde de aynı Coder Group seçilmeli ve "Extension Coders" ayarı `None` tutulmalıdır.

> [!WARNING]
> G.729 codec kullanımı bazı senaryolarda ek lisans gerektirebilir. Lisans durumunuzu kontrol etmeden yoğun transcoding kurgusu yapmayın.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


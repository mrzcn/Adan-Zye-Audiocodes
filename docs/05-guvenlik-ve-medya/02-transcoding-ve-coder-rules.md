# Transcoding ve Coder Rules

Transcoding, bir ses bacağından gelen ses formatının (Codec), diğer bacağa gönderilirken anlık olarak başka bir formata dönüştürülmesidir.

## 📌 Codec Nedir?

Ses verisinin nasıl dijitalleştirileceğini ve sıkıştırılacağını belirleyen algoritmadır. 
*   **G.711 (PCMA/PCMU):** Sıkıştırma yapmaz, yüksek bant genişliği tüketir, en yüksek ses kalitesini sunar.
*   **G.729:** Yüksek sıkıştırma yapar, düşük bant genişliği tüketir, ses kalitesi biraz daha düşüktür.

## 📌 Transcoding Ne Zaman Gerekir?

*   Genesys tarafı sadece G.711 destekliyor ancak Operatör tarafı bant genişliğinden tasarruf etmek için G.729 dayatıyorsa.
*   Bu durumda SBC, Genesys'ten G.711 aldığı sesi G.729'a çevirerek operatöre gönderir.

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

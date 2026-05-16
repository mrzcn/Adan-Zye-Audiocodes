# MediaPack vs. Mediant: Hangisi, Ne Zaman?

AudioCodes dünyasına yeni giren birinin en çok karıştırdığı iki ürün ailesi **MediaPack (MP)** ve **Mediant**'tır. Bu ikisi arasındaki farkı anlamak, doğru projede doğru cihazı seçmek için kritiktir.

## 📌 1. MediaPack (MP) Serisi: "Safkan Gateway"

MediaPack cihazları temel olarak **Analog-IP dönüşümü** yaparlar. Akıllı bir yönlendirme veya güvenlik (SBC) katmanları yoktur.

*   **MP-114/118/124:** Küçük ölçekli analog cihazlardır.
*   **Görev:** Analog telefonları, faks makinelerini veya analog santral hatlarını (FXS/FXO) sadece SIP'e dönüştürür.
*   **Ne Zaman Kullanılır?** Bir şirkette sadece 24 tane eski analog telefonu IP santrale bağlamak istiyorsanız MediaPack 124 (24 FXS) işinizi görür.

## 📌 2. Mediant Serisi: "Akıllı SBC ve Multiservice Gateway"

Mediant ailesi çok daha güçlüdür. Hem analog/dijital dönüşüm yapabilir hem de tam teşekküllü bir **SBC** olarak çalışabilir.

*   **Görev:** Sadece port dönüştürmekle kalmaz; güvenlik sağlar, çağrıları manipüle eder (Message Manipulation), farklı operatörleri birbirine bağlar ve Teams Direct Routing yapar.
*   **Akıllı Yönlendirme:** IP-to-IP yönlendirme yeteneği Mediant serisinin kalbidir.

## 📌 Temel Karşılaştırma Tablosu

| Özellik | MediaPack (MP) | Mediant (SBC/Gateway) |
| :--- | :--- | :--- |
| **SBC Özellikleri** | Yok | Var |
| **Güvenlik (IDS/IPS)** | Temel Seviye | Gelişmiş Seviye |
| **IP-to-IP Routing** | Yok | Var |
| **Teams Desteği** | Sadece Analog Gateway olarak | Tam Destek (SBC & Gateway) |
| **Transcoding** | Sınırlı | Güçlü (Donanımsal DSP) |

## 📌 Özet Karar Rehberi

*   **Senaryo A:** "Sadece 4 tane analog faks makinesini IP santrale kaydedeceğim." 
    *   👉 **Seçim:** MediaPack 114 (4 FXS).
*   **Senaryo B:** "Operatörden gelen SIP Trunk hattımı hem güvenliğe alacağım hem de Teams'e bağlayacağım."
    *   👉 **Seçim:** Mediant 800 veya Mediant 1000 SBC.
*   **Senaryo C:** "Hem 30 tane analog telefonum var hem de dış hatlarım PRI (E1). Bunları tek bir kutuda çözüp SBC yapmalıyım."
    *   👉 **Seçim:** Mediant 1000 (Modüler yapısı sayesinde).

> [!TIP]
> Bir projede "SBC" kelimesi geçiyorsa, MediaPack serisini seçeneklerden eleyebilirsiniz. SBC yetenekleri sadece Mediant ailesinde bulunur.

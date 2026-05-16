<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# Mediant Donanım Ailesi ve Kapasite Rehberi

"Hangi projede hangi Mediant cihazı kullanılmalı?" sorusunun cevabı, ihtiyaç duyulan **SBC Session (eş zamanlı çağrı)** sayısı ve fiziksel port (FXS/FXO/E1) ihtiyacına göre değişir.

## 📌 Mediant Serisi Ürün Gamı

AudioCodes Mediant ailesi, küçük bir ofisten devasa operatör merkezlerine kadar ölçeklenebilir:

### 1. Mediant 500 / 500L
*   **Kapasite:** Maksimum 30-60 SBC Session.
*   **Kullanım:** Küçük ofisler, şubeler.
*   **Özellik:** Küçük, fanless (sessiz) modelleri vardır.

### 2. Mediant 800
*   **Kapasite:** Maksimum 60-125 SBC Session (Donanım revizyonuna göre).
*   **Kullanım:** Orta ölçekli işletmeler ve şubeler.
*   **Özellik:** Üzerinde sabit analog portlar (FXS/FXO) veya 1 adet E1 portu barındırabilir. En çok tercih edilen "Swiss Army Knife" (İsviçre Çakısı) modelidir.

#### Mediant 800 Teknik Detay Tablosu (v7.20)
| Bileşen | Detay / Kapasite |
| :--- | :--- |
| **Ethernet Portları** | 4 x 10/100/1000 Base-T (GE) |
| **DSP Modülleri** | Maksimum 2 slot (Transcoding için) |
| **Maksimum SBC Session** | 125 (G.711 -> G.711) / ~60 (G.711 -> G.729) |
| **Analog Port Desteği** | 4, 8, 12 FXS veya FXO seçenekleri |
| **Güç Kaynağı** | Single veya Dual (Opsiyonel) AC/DC |

### 3. Mediant 1000
*   **Kapasite:** Maksimum 150-200 SBC Session.
*   **Kullanım:** Modülerlik gereken orta-büyük işletmeler.
*   **Özellik:** **Modülerdir.** Üzerindeki slotlara ihtiyaca göre FXS, FXO veya E1 modülleri takılıp çıkarılabilir.

### 4. Mediant 2600 / 4000
*   **Kapasite:** 600 - 4000 SBC Session.
*   **Kullanım:** Büyük kurumlar, çağrı merkezleri.
*   **Özellik:** 1U boyutunda, yüksek performanslı safkan SBC cihazlarıdır.

### 5. Mediant 9000
*   **Kapasite:** 30.000+ SBC Session.
*   **Kullanım:** Telekom operatörleri (Core Network).

## 📌 Kapasite Neye Göre Belirlenir?

Bir cihazın kapasitesini sadece üzerindeki etiket değil, şu faktörler belirler:
1.  **Lisans:** Cihazın donanımı 100 çağrıyı desteklese bile, lisansınız 20 ise 21. çağrı geçmez.
2.  **Transcoding:** Ses codec dönüşümü yapılıyorsa işlemci (DSP) yükü artar, bu da toplam kapasiteyi düşürebilir.
3.  **Security (TLS/SRTP):** Şifreli görüşmeler CPU tüketir.

## 📌 Hangi Projede Hangisi?

| Senaryo | Önerilen Cihaz | Nedeni |
| :--- | :--- | :--- |
| **Küçük Şube (10 Kişi)** | Mediant 500L | Düşük maliyet, yeterli kapasite. |
| **Fabrika (50 Analog Tel + SIP Trunk)** | Mediant 800 veya 1000 | Analog port desteği ve SBC gücü. |
| **Büyük Çağrı Merkezi (500 Müşteri Temsilcisi)** | Mediant 2600 | Yüksek eş zamanlı çağrı ve kararlılık. |
| **Sadece Teams Direct Routing (Donanım istenmiyor)** | Mediant VE (Virtual) | Sanallaştırma konforu. |

> [!TIP]
> Proje tasarlarken her zaman "Gelecek 3-5 yılın ihtiyacı ne olur?" diye düşünerek %20-30 kapasite payı bırakmak mühendislik açısından en güvenli yoldur.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


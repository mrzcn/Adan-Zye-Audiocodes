<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# Regex (Düzenli İfadeler) Kütüphanesi

## 📌 Türkiye Numaralandırma Planı İçin Özel Regexler

Türkiye'deki operatör (TT, Turkcell, Vodafone vb.) ve santral (Avaya, Cisco, Teams) entegrasyonlarında en çok kullanılan kalıplar:

| Senaryo | Regex Kalıbı | Replacement | Örnek Girdi | Sonuç |
| :--- | :--- | :--- | :--- | :--- |
| **0'sız Numarayı +90 Yapma** | `^([2-5][0-9]{9})$` | `+90$1` | `5321234567` | `+905321234567` |
| **0 ile Başlayanı +90 Yapma** | `^0([2-5][0-9]{9})$` | `+90$1` | `02123334455` | `+902123334455` |
| **+90'lı Numaradan +90 Silme** | `^\+90([0-9]+)$` | `$1` | `+90532...` | `532...` |
| **Dahili No Yakalama (4 hane)** | `^([0-9]{4})$` | `$1` | `1001` | `1001` |
| **Bilinmeyen No Maskeleme** | `^anonymous$` | `0000` | `anonymous` | `0000` |

## 📌 SIP URI ve Host Manipülasyonu

Message Manipulation katmanında sadece numaraları değil, domain ve port bilgilerini de Regex ile yönetebilirsiniz.

### 1. Host Bilgisini Değiştirme
Gelen paketteki IP adresini veya domaini sabit bir değerle değiştirmek için:
*   **Target:** `Header.To.URL.Host`
*   **Regex:** `^(.*)$`
*   **Value:** `'nolto.com.tr'`

### 2. User-Part ve Parameters Ayıklama
SIP URI içindeki `user=phone` gibi parametreleri temizlemek veya eklemek için:
*   **Regex:** `^sip:(.*);.*$`
*   **Value:** `'sip:' + $1` (Noktalı virgülden sonrasını atar).

## 📌 İleri Düzey Gruplama ve Karakter Sınıfları

*   **Opsiyonel Karakterler (`?`):** `^0?([0-9]{10})$` -> Baştaki '0' olsa da olmasa da sonraki 10 haneyi yakalar.
*   **Negatif Eşleşme:** `^(?!+90).*$` -> +90 ile **başlamayan** tüm numaraları yakalar.
*   **Veya (`|`) Kullanımı:** `^(0212|0216)[0-9]{7}$` -> Sadece İstanbul Avrupa veya Anadolu yakası numaralarını yakalar.

## 📌 Regex Performans İpucu

SBC üzerinde binlerce kural olduğunda Regex işlemcisi CPU tüketebilir.
*   **Öneri:** Mümkün olduğunca spesifik olun. `.*` kullanmak yerine `[0-9]+` kullanmak, SBC'nin paketi daha hızlı işlemesini sağlar.
*   **Wildcard:** Sadece numara başında/sonunda değişiklik yapacaksanız `Prefix` ve `Suffix` alanlarını kullanın, ağır Regex işlemlerini sadece karmaşık dönüşümler için saklayın.

> [!TIP]
> **Regex Test Aracı:** Regex kalıplarınızı cihaz üzerinde denemeden önce [regex101.com](https://regex101.com) gibi araçlarda (PCRE modunda) test edebilirsiniz. AudioCodes PCRE (Perl Compatible Regular Expressions) kütüphanesini baz alır.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


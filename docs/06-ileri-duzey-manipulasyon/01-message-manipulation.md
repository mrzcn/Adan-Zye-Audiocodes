<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

## 📌 Ne Zaman Kullanılır?

Message Manipulation, mrzcn-expert dökümantasyon serisinin önceki bölümlerinde (Sinyalleşme Temelleri) anlatılan protokol uyumsuzluklarını gidermek için kullanılan en gelişmiş araçtır.

*   **Interworking:** İki sistemin SIP başlıkları birbiriyle uyumsuz olduğunda (Örn: Bir taraf `From` başlığında isim beklerken diğer tarafın sadece numara göndermesi).
*   **Gizlilik:** Belirli başlıkların (Örn: `User-Agent`) silinmesi istendiğinde.
*   **Header Ekleme:** Karşı tarafa özel bir başlık (Örn: `X-Nolto-ID`) gönderilmesi gerektiğinde.

## 📌 Yapılandırma Adımları (v7.20)

**Menü:** `Setup > Signaling & Media > Message Manipulation > Message Manipulations`

v7.20 kılavuzundaki kritik bileşenler:

1.  **Manipulation Set ID:** Kuralları gruplamak için kullanılır. Bu ID daha sonra `IP Group` ayarları altındaki **Inbound/Outbound Message Manipulation Set** alanına bağlanır.
2.  **Message Type:** Müdahale edilecek mesaj tipi (Örn: `Invite.Request`, `Any.Response`, `18x.Response`).
3.  **Condition:** (Opsiyonel) Kuralın tetiklenme şartı. (Örn: `Header.User-Agent Contains 'Cisco'`).
4.  **Action Subject:** Hedef alan (Örn: `Header.PAI.URL.User`, `Body.SDP.Media.IP`).
5.  **Action Type:** `Modify`, `Add`, `Remove`, `Copy`.

## 📌 Regex ve Değişken (Variables) Kullanımı

AudioCodes, başlıklar içindeki verileri parçalayıp yeniden birleştirmek için **Regex** gruplarını destekler.
*   **Örnek:** `Header.From.URL.User` içindeki numaranın başına `0` eklemek.
*   **Regex:** `^(.*)$`
*   **Value:** `'0' + $1`
*   **Açıklama:** `$1` değişkeni, parantez içindeki yakalanan tüm grubu temsil eder.

## 📌 İleri Düzey Senaryolar

### 1. P-Asserted-Identity (PAI) Ekleme
Operatörler genellikle kimlik doğrulama için PAI başlığı bekler. Eğer santraliniz bunu göndermiyorsa:
*   **Action Subject:** `Header.P-Asserted-Identity`
*   **Action Type:** `Add`
*   **Value:** `'<sip:' + Header.From.URL.User + '@' + Header.From.URL.Host + '>'`

### 2. Microsoft Teams: Port Bilgisini Temizleme
Teams bazen `To` başlığında port bilgisi (`:5060`) geldiğinde çağrıyı reddedebilir. Bunu temizlemek için:
*   **Action Subject:** `Header.To.URL.Port`
*   **Action Type:** `Remove`

### 3. SDP Body Manipülasyonu (Ses Sorunları İçin)
Eğer karşı taraf SDP içinde yanlış bir medya IP'si gönderiyorsa, SBC bunu paket gövdesinde de değiştirebilir:
*   **Action Subject:** `Body.SDP.Connection.IP`
*   **Action Type:** `Modify`
*   **Value:** `'212.x.x.x'`

## 📌 Koşullu (Conditional) Manipülasyon

Sadece belirli hata kodları geldiğinde çalışan kurallar yazabilirsiniz.
*   **Senaryo:** Sadece `404 Not Found` cevabı geldiğinde bir başlık eklemek.
*   **Message Type:** `404.Response`
*   **Action:** `Add Header...`

## 📌 Güvenlik: Sistem Bilgilerini Gizleme
SBC'nin markasını ve sürümünü dış dünyaya sızdırmamak için `User-Agent` ve `Server` başlıklarını silmek en iyi uygulamadır (Hardening).
*   **Action Subject:** `Header.User-Agent`
*   **Action Type:** `Remove`

> [!CAUTION]
> **Sıralama Kritiktir:** Bir Set ID içindeki kurallar yukarıdan aşağıya çalışır. Bir kuralda değiştirdiğiniz başlık, bir sonraki kuralın "Condition" kısmını etkileyebilir.

> [!TIP]
> **Message Log Analizi:** Yaptığınız manipülasyonun sonucunu görmek için `Status & Diagnostics > Message Log` ekranını kullanın. "Before Manipulation" ve "After Manipulation" farkını görmek için log seviyesini `Detailed` yapmanız gerekebilir.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


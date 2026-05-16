<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# IP-to-IP Routing

## 📌 Sınıflandırma (Classification): İlk Adım

SBC'ye bir INVITE geldiğinde, SBC'nin bu paketi kimin gönderdiğini (Hangi IP Group) anlaması gerekir. Buna **Inbound Classification** denir.
*   **Eşleşme Kriterleri:** Kaynak IP adresi, SIP Interface, Proxy Set veya `Request-URI` gibi alanlara bakılır.
*   **Neden Önemli?** Eğer SBC paketi sınıflandıramazsa, hangi Routing kuralını uygulayacağını bilemez ve çağrıyı `404 Not Found` veya `Discard` ile sonlandırır.

## 📌 Yapılandırma Adımları (v7.20)

**Menü:** `Setup > Signaling & Media > SBC > Routing > IP-to-IP Routing`

Yeni bir kural eklerken v7.20 kılavuzundaki kritik alanlar:

1.  **Name:** Kuralın ismi (Örn: `Route_Genesys_to_TT`).
2.  **Source IP Group:** Çağrının geldiği grup.
3.  **Destination Type:** 
    *   **IP Group:** Doğrudan bir gruba gönderir.
    *   **Request URI:** Paketin üzerindeki hedefe dokunmadan iletir.
    *   **Alternative Routing Table:** Yedekli yönlendirme tablolarını kullanır.
4.  **Match Criteria:** 
    *   `Destination Username Prefix`: Aranan numara maskesi.
    *   `Internal Dial Plan Index`: Karmaşık numara planları için Dial Plan kullanımı.

## 📌 İleri Düzey Yönlendirme Senaryoları

### 1. Alternative Routing (Yedeklilik/Failover)
Birincil operatör veya sunucu yanıt vermediğinde (SIP 5xx hatası veya Timeout) çağrının otomatik olarak ikinci bir hedefe gönderilmesidir.
*   **Ayar:** Routing kuralında `Destination Type` olarak `Alternative Routing Table` seçilir. Bu tabloda `Status` kolonu `Primary` ve `Alternative` olarak hedefleri belirler.

### 2. Load Balancing (Yük Dengeleme)
Çağrıların iki veya daha fazla hedef (Örn: İki farklı PBX) arasında dağıtılmasıdır.
*   **Yöntem:** Aynı kriterlere sahip birden fazla routing kuralı yazılır veya `IP Group` içindeki `Proxy Set` üzerinden "Round Robin" seçilir.

### 3. Forking (Eş Zamanlı Çaldırma)
Gelen bir çağrının aynı anda birden fazla hedefe (Örn: Hem IP Telefon hem Cep Telefonu) gönderilmesidir. AudioCodes SBC, 1'e 10 oranına kadar forking destekler.

## 📌 Yönlendirme Sıralaması ve Öncelik (Cost)

Tablodaki kurallar **yukarıdan aşağıya** taranır. 
*   **Golden Rule:** Her zaman spesifik kuralları (Örn: `Destination Prefix: +90212`) en üste, genel kuralları (Örn: `Destination Prefix: ANY`) en alta yazın.
*   **Cost:** Aynı kriterli kurallarda düşük maliyetli (Cost) olan kural önceliklidir.

> [!IMPORTANT]
> **Simetri Kuralları:** İki yönlü görüşme için mutlaka iki ayrı kural yazılmalıdır:
> 1. `Inside -> Outside`
> 2. `Outside -> Inside` (Eğer dışarıdan çağrı bekleniyorsa).

> [!TIP]
> **Dial Plan Search:** Yapılandırmanız karmaşıklaştığında, `Troubleshoot > Test Tools > Dial Plan Search` aracını kullanarak bir numaranın hangi kuraldan geçip nereye gittiğini saniyeler içinde simüle edebilirsiniz.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# Number Manipulation

Number Manipulation, arayan (Calling) veya aranan (Called) numaraların formatını değiştirmek için kullanılır. (Örn: Numara başına `0` eklemek veya `+90`'ı silmek).

## 📌 Neden Kullanılır?

*   **Format Uyumu:** Genesys numaraları `+90` formatında gönderirken, operatör Gateway'i numaraları başında `0` olacak şekilde bekleyebilir.
*   **Gizleme:** Arayan numaranın son 4 hanesini maskelemek için kullanılabilir.
*   **Yönlendirme:** Gelen numarayı manipüle ederek farklı bir hedefe yönlendirilmesini sağlamak için.

## 📌 Yapılandırma Adımları (v7.20)

AudioCodes'ta numara manipülasyonu genellikle iki yerde yapılır:

### 1. Inbound/Outbound IP-to-IP Manipulation
**Menü:** `Setup > Signaling & Media > SBC > Manipulation > Outbound Manipulation` (Veya Inbound)

Parametreler:
1.  **Name:** İsim.
2.  **Source IP Group:** Hangi gruptan gelen çağrılar için geçerli.
3.  **Destination IP Group:** Hangi gruba giden çağrılar için geçerli.
4.  **Destination Username Prefix:** Hangi numara ile başlarsa (Örn: `+90`).
5.  **Remove From Left:** Soldan kaç hane silinecek (Örn: `3` hane silinirse `+90` gider).
6.  **Prefix to Add:** Başa ne eklenecek (Örn: `0`).

### 2. Destination/Source Phone Number Map Tables
SBC üzerinde binlerce numara için tek tek kural yazmak yerine, bir tablo (Map) oluşturup bu tabloyu manipülasyon kuralına bağlayabilirsiniz.
*   **Kullanım:** Örneğin tüm bölge müdürlüklerinin prefix'lerini bir tabloda toplayıp, tek bir kural ile hepsinin başına kurumsal kod ekleyebilirsiniz.
*   **Menü:** `Setup > Signaling & Media > SBC > Manipulation > Destination Phone Number Map`

## 📌 Regex (Düzenli İfadeler) Kullanımı

AudioCodes, numara manipülasyonunda gelişmiş Regex kurallarını destekler. Örneğin:
*   `^(.*)$` -> `0$1` (Tüm numaraların başına 0 ekle).

> [!TIP]
> Numara manipülasyonunun çalışıp çalışmadığını test etmek için **Troubleshoot > Test Tools > Dial Plan Search** aracını kullanabilirsiniz. Girdiğiniz bir numaranın kurallardan geçtikten sonra neye dönüştüğünü size simüle eder.

> [!NOTE]
> IP-to-IP Routing kurallarından **önce** mi yoksa **sonra** mı manipülasyon yapılacağı önemlidir. Genellikle Inbound manipülasyon routing'den önce, Outbound manipülasyon ise routing'den sonra uygulanır.


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

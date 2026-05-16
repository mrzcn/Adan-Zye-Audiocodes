<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# Syslog ve Message Log Okuma

SBC üzerinde bir sorun oluştuğunda (Çağrı düşmesi, ses gelmemesi vb.) en önemli yardımcınız cihazın ürettiği loglardır.

## 📌 Message Log (SIP Log) Nedir?

Cihazın üzerinden geçen tüm SIP paketlerini (INVITE, 200 OK, BYE vb.) anlık olarak görmenizi sağlar. Sorun gidermede **ilk bakılması gereken** yerdir.

### Message Log Nasıl Alınır? (v7.20)
**Menü:** `Troubleshoot > Message Log`
1.  **Log Type:** `SBC` seçilir.
2.  **Start:** Butonuna basıldığında loglar akmaya başlar.
3.  **Stop:** Kaydı durdurur.
4.  **Save:** Logları bilgisayarınıza indirir (Genellikle `.txt` formatında).

## 📌 Syslog Nedir?

Cihazın iç dünyasında neler olup bittiğini (Donanım hataları, lisans uyarıları, routing kararları) gösteren daha detaylı bir log türüdür.

### Örnek Syslog Satırı
`12:05:01 SBC-Nolto-Partner-800 user.notice: call_id 102 established by mrzcn-expert-session`

### Syslog Ayarları
**Menü:** `Setup > Device > Troubleshooting > Syslog Settings`
*   **Syslog Server:** Logların gönderileceği bilgisayarın IP adresi. (Harici bir Syslog Viewer yazılımı kullanılması önerilir).
*   **Debug Level:** Genellikle `5` veya sorun derinleşirse `6` yapılır.

## 📌 Hata Kodlarını Anlamak

SBC üzerinde sıkça karşılaşacağınız SIP hata kodları:

*   **404 Not Found:** Routing tablosunda eşleşen bir kural bulunamadı veya hedef sunucu numarayı tanımıyor.
*   **403 Forbidden:** IP Group veya Classification kuralı tarafından çağrı reddedildi (Güvenlik engeli).
*   **488 Not Acceptable Here:** Codec uyumsuzluğu (Örn: Bir taraf sadece G.729 istiyor ama SBC sadece G.711 gönderiyor).
*   **503 Service Unavailable:** Lisans kapasitesi dolmuş veya hedef sunucu kapalı.

> [!TIP]
> AudioCodes loglarını daha rahat okumak için AudioCodes'un ücretsiz **"Syslog Viewer"** yazılımını kullanabilirsiniz. Bu yazılım SIP paketlerini bir akış diyagramı (Ladder Diagram) şeklinde gösterir.

> [!IMPORTANT]
> Log alırken filtreleme (Filter) özelliğini kullanarak sadece belirli bir IP'den veya numaradan gelen çağrıları takip edebilirsiniz. Bu, yoğun trafikli cihazlarda karmaşayı önler.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# SBC Nedir ve Sektörel Konumu?

Yeni mezun bir mühendis için ses teknolojileri dünyasına girerken sorulacak ilk soru şudur: "Neden sadece bir router veya firewall yetmiyor da SBC kullanıyoruz?"

## 📌 SBC (Session Border Controller) Nedir?

SBC, IP tabanlı ses (VoIP) ağlarının sınırında (border) duran ve bu ağlar arasındaki oturumları (session) kontrol eden (controller) cihazdır. 

### Sektörel Benzetme
Bir şirketin binasını düşünün:
*   **Router:** Binaya giden yolları ve tabelaları yönetir.
*   **Firewall:** Binanın girişindeki güvenlik görevlisidir; kimlik kontrolü yapar (Port bazlı).
*   **SBC:** Binanın içindeki **resepsiyonist ve tercümandır.** Gelen misafirin dilini (Codec) anlar, kime geldiğini teyit eder, gerekirse form doldurtur (Manipulation) ve içeri öyle alır.

## 📌 Sektördeki Ana Üreticiler

SBC pazarı, telekomünikasyon dünyasının en kritik segmentlerinden biridir. Önde gelen üreticiler:

1.  **AudioCodes:** Özellikle kurumsal pazarda ve Microsoft ekosisteminde dünya lideridir. Kullanıcı dostu arayüzü ve geniş ürün yelpazesiyle bilinir.
2.  **Oracle (Acme Packet):** Daha çok büyük servis sağlayıcı (Service Provider) seviyesindeki devasa trafikler için tercih edilir.
3.  **Ribbon (Sonus/Genband):** Hem operatör hem kurumsal tarafta güçlü bir oyuncudur.
4.  **Cisco:** CUBE (Cisco Unified Border Element) ile kendi ekosisteminde çözüm sunar.

## 📌 Neden SBC'ye İhtiyaç Duyarız? (Derin Bakış)

Ses trafiği (VoIP), veri trafiğinden farklı olarak iki katmanlıdır:
1.  **Sinyalleşme (SIP):** Telefonun çalması, kimin aradığının belirlenmesi.
2.  **Medya (RTP):** Gerçek ses verisinin taşınması.

Normal bir Firewall, SIP paketinin başlığını (Header) görebilir ama içindeki SDP (Session Description Protocol) bilgisini okuyup değiştiremez. SBC ise paketlerin içine girerek IP adreslerini ve portları değiştirir (NAT Traversal), böylece "ses gitmiyor" veya "tek taraflı ses" gibi kronik VoIP sorunlarını çözer.

> [!NOTE]
> Sektöre yeni giren biri için SBC öğrenmek; sadece network değil, aynı zamanda protokol analizi, güvenlik ve ses kalitesi yönetimi konularında uzmanlaşmak demektir.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


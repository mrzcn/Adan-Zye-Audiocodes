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

## 📌 Neden Firewall Yetmiyor? (SIP ALG Problemi)

Ses trafiği (VoIP), standart internet trafiğinden (HTTP/HTTPS) farklı olarak iki katmanlıdır:
1.  **Sinyalleşme (SIP):** Telefonun çalması, kimin aradığının belirlenmesi (genelde Port 5060).
2.  **Medya (RTP):** Gerçek ses verisinin taşınması (genelde Port 6000-60000 arası rastgele UDP portları).

Normal bir Firewall, sadece 5060 portunu açar ve paketi geçirir. Ancak paketin gövdesinde (SDP - Session Description Protocol) yazan iç IP adreslerini göremez. Çoğu modern Firewall, ses trafiğine yardımcı olmak için **SIP ALG (Application Layer Gateway)** denilen bir özellik barındırır. Ancak SIP ALG, paketleri "körlemesine" değiştirmeye çalıştığı için %90 oranında paketlerin bozulmasına ve aramaların düşmesine sebep olur.

**SBC'nin Farkı:** SBC gerçek bir B2BUA (Back-to-Back User Agent) olarak çalışır. Gelen SIP paketini Firewall gibi sadece "geçirmez"; paketi tamamen sonlandırır, içini açar, IP ve port bilgilerini ağ topolojisine göre **yeniden yazar** ve yeni bir paket olarak içeri/dışarı gönderir.

## 📌 SBC'nin Temel Görevleri

SBC'lerin varoluş amacı 4 ana başlıkta toplanabilir:
1.  **Güvenlik ve Topology Hiding (Topoloji Gizleme):** Dışarıdan gelen bir hacker, şirket içindeki IP PBX sunucusunun IP adresini asla öğrenemez. SBC, dış dünyaya sadece kendi IP adresini gösterir.
2.  **NAT Traversal:** Karmaşık NAT yapılarındaki "Tek taraflı ses" sorunlarını çözer.
3.  **Interoperability (Uyum Sağlama):** SIP standardı esnektir; Cisco'nun SIP dili ile Avaya'nın SIP dili farklı olabilir. SBC, araya girerek başlık manipülasyonu yapar (SIP Normalization).
4.  **Transcoding:** Operatör G.729 beklerken, içerideki sistem G.711 kullanıyorsa anlık ses çevirisi yapar.

## 📌 Enterprise vs. Service Provider (Operatör) SBC

Sektörde SBC'ler konumlarına göre ikiye ayrılır:
*   **Enterprise SBC (Kurumsal):** Şirketlerin kendi santralleri ile Telekom operatörleri arasına koydukları (Örn: Mediant 800) veya Microsoft Teams gibi bulut sistemlerle (Direct Routing) konuşturan cihazlardır.
*   **Service Provider SBC (Peering):** Telekom operatörlerinin kendi omurgalarında (Core Network) veya diğer operatörlerle bağlantı (Interconnect) noktalarında kullandıkları, binlerce kanal kapasiteli devasa cihazlardır (Örn: Mediant 4000 veya Oracle Acme Packet).

> [!NOTE]
> Sektöre yeni giren biri için SBC öğrenmek; sadece network değil, aynı zamanda protokol analizi, güvenlik (IDS/IPS) ve ses kalitesi yönetimi konularında uçtan uca uzmanlaşmak demektir. Ses paketlerinin milisaniyeler içinde yönlendirilmesi, IT dünyasının en zorlu ve prestijli alanlarından biridir.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


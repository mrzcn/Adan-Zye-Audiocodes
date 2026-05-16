<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# SIP ve RTP Protokolleri

SBC (Session Border Controller) yapılandırmasına geçmeden önce, yönettiği iki ana protokole (SIP ve RTP) kısaca değinmek sorun giderme (Troubleshooting) süreçlerinde hayati önem taşır.

## 📌 SIP (Session Initiation Protocol)

SIP, internet üzerinden ses, video ve anlık mesajlaşma oturumlarını **başlatmak, değiştirmek ve sonlandırmak** için kullanılan bir Sinyalleşme protokolüdür. 

* **Port ve Taşıyıcı:** Genellikle UDP veya TCP **5060** portunu kullanır. Şifrelenmiş SIP (SIPS veya TLS) kullanıldığında **5061** portu kullanılır.
* **Ne İş Yapar?** SIP, telefonun çalmasını, meşgule düşmesini, çağrının kabul edilmesini (Cevaplama) sağlar. Ancak SIP, sesin kendisini taşımaz! Sadece iki ucun birbiriyle tanışmasına aracılık eder.
* **Format:** HTTP protokolüne çok benzer (Request/Response mimarisi). Düz metin (Plain Text) tabanlıdır. `INVITE`, `ACK`, `BYE`, `200 OK` gibi metodlarla çalışır.

> [!TIP]  
> AudioCodes üzerinde Message Log aldığınızda gördüğünüz tüm metin blokları SIP protokolünün mesajlarıdır. Eğer telefon hiç çalmıyorsa veya 4xx/5xx hatası alıyorsanız sorun SIP katmanındadır.

## 📌 RTP (Real-Time Transport Protocol)

RTP, SIP aracılığıyla tanışan iki uç nokta arasında **gerçek ses (medya)** verilerini taşımak için kullanılan protokoldür.

* **Port ve Taşıyıcı:** Her zaman **UDP** protokolünü kullanır. Dinamik bir port aralığı kullanır (Örneğin, AudioCodes'da Media Realm bölümünde belirlenen 6000-6999 aralığı).
* **Ne İş Yapar?** Mikrofonunuzdan çıkan sesi paketlere böler, karşı tarafa iletir ve karşıdan gelen paketleri birleştirerek hoparlörünüze verir.
* **RTCP (RTP Control Protocol):** RTP'nin kalitesini (Jitter, Packet Loss, Delay) ölçen yardımcı bir protokoldür. 

> [!WARNING]  
> Telefonlar çalıyor, karşı taraf telefonu açıyor ancak ses gelmiyorsa (veya tek taraflı ses geliyorsa), sorun SIP ile değil, **RTP portlarının Firewall'da kapalı olması** veya NAT/SBC üzerindeki Media Realm / IP Routing ayarlarındaki bir sorundan kaynaklanmaktadır.

---

### SIP ve RTP'nin Birlikte Çalışma Mantığı (SDP)

SIP paketlerinin içinde taşıdığı özel bir "zarf" vardır; buna **SDP (Session Description Protocol)** denir. 
SDP, tarafların birbirine "*Benim IP adresim X, RTP ses paketlerini benim UDP Y portuma göndermelisin, ayrıca desteklediğim Ses Codec'leri şunlar (G.711, G.729 vs.)*" diyerek anlaştıkları bölümdür.

AudioCodes cihazı, B2BUA olarak çalıştığı için SDP mesajındaki bu lokal IP ve portları siler, yerine kendi IP ve RTP port aralığını yazar. Bu işleme **Media Anchoring (Medya Demirleme)** denir ve sesin her zaman SBC üzerinden geçmesini garanti altına alır.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


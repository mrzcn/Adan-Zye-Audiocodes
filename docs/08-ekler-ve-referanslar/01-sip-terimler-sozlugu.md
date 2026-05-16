<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# SIP Terimler Sözlüğü

AudioCodes SBC dünyasında sıkça karşılaşacağınız teknik terimlerin detaylı açıklamaları:

## 📌 Temel Protokoller ve Kavramlar

*   **SIP (Session Initiation Protocol):** Oturum başlatma protokolü. Telefonun çalması, kimin aradığı ve çağrının sonlandırılması gibi sinyalleşme işlemlerini yönetir. Text tabanlıdır (HTTP'ye benzer).
*   **RTP (Real-time Transport Protocol):** Gerçek zamanlı taşıma protokolü. SIP bir çağrıyı kurduktan sonra, ses veya video verisinin (medya) asıl taşındığı kanaldır.
*   **RTCP (RTP Control Protocol):** RTP'nin "kalite kontrol" versiyonudur. Giden ses paketlerinin ne kadarının ulaştığını, gecikmeleri ve kayıpları istatistiksel olarak raporlar.
*   **SDP (Session Description Protocol):** SIP paketinin gövdesinde (body) bulunan ve "Benim IP adresim şu, portum bu, şu ses formatlarını (codec) destekliyorum" şeklinde iki cihaz arasındaki "medya pazarlığını" sağlayan metin yapısıdır.
*   **B2BUA (Back-to-Back User Agent):** SBC'nin çalışma mimarisidir. Çağrıyı kendi üzerinde sonlandırıp, hedefe doğru yepyeni bir çağrı başlatır. Araya girerek her iki bacağı birbirinden izole eder.
*   **FQDN (Fully Qualified Domain Name):** Bir sunucunun ağ üzerindeki tam adı (Örn: `sip.nolto.com.tr`). IP yerine isimle yönlendirme yapmayı sağlar.

## 📌 SIP Mesajları ve Yanıt Kodları

*   **INVITE:** Yeni bir çağrı (oturum) başlatma talebi.
*   **REGISTER:** Bir IP telefonun veya santralin "Ben buradayım, IP adresim bu" diyerek sisteme kayıt olma talebi.
*   **OPTIONS (Keep-Alive):** Hedef sistemin ayakta (canlı) olup olmadığını kontrol etmek için atılan "Ping" benzeri SIP mesajı.
*   **100 Trying:** "Talebini aldım, işleme koydum" anlamına gelen ilk yanıt.
*   **180 Ringing:** "Hedefteki telefon şu an çalıyor" bilgisi.
*   **183 Session Progress:** Karşı taraf cevap vermeden önce ses iletiminin başlaması (Örn: "Aradığınız kişiye şu an ulaşılamıyor" anonsunun duyulması). Buna **Early Media** denir.
*   **200 OK:** Talebin başarıyla gerçekleştiği onay mesajı (Telefon açıldı veya Register başarılı).
*   **ACK:** 200 OK yanıtını aldıktan sonra, "Görüşmeyi başlatıyorum" diyen son teyit mesajı.
*   **BYE:** Görüşmenin sonlandırılması (Telefonun kapatılması).

## 📌 Kritik SIP Başlıkları (Headers)

*   **From:** Çağrıyı başlatan tarafın (Arayan) adresi.
*   **To:** Çağrının kime (Aranan) gitmekte olduğu adresi.
*   **Contact:** Bir cihazın "Bana bir dahaki sefere bu IP ve porttan doğrudan ulaşabilirsin" dediği adres.
*   **Via:** SIP paketinin o ana kadar geçtiği tüm durakların (proxy'lerin) sırasıyla yazıldığı log başlığı.
*   **Diversion:** "Bu çağrı aslında X numarasına gelmişti ama Y numarasına yönlendirildi" bilgisini taşıyan başlık.
*   **P-Asserted-Identity (PAI):** Operatörlerin, "Bu abonenin kimliğini doğruladım, bu arayan numara (Caller ID) gerçektir" demek için kullandığı güvenilir kimlik başlığı.

## 📌 Medya (Ses) ve Kalite (QoS) Terimleri

*   **Codec (Coder-Decoder):** Sesin mikrofondan alınıp dijital paketlere çevrilme ve karşı tarafta tekrar sese dönüştürülme algoritması.
    *   `G.711 (PCMA/PCMU):` Sıkıştırmasız, en yüksek kaliteli ama en çok bant genişliği (64 kbps) tüketen standart codec.
    *   `G.729:` Sıkıştırılmış, kalite olarak bir miktar düşük ama çok az bant genişliği (8 kbps) tüketen codec.
*   **Transcoding:** A noktasının codec'i ile B noktasının codec'i uyuşmadığında, SBC'nin araya girerek "anlık çeviri" yapması işlemi (Örn: G.711'den G.729'a çevirme).
*   **DSP (Digital Signal Processor):** Transcoding gibi ağır ses işleme operasyonlarını yapmak için SBC üzerinde bulunan donanımsal ses yongası.
*   **Jitter:** Ses paketlerinin hedefe varış süreleri arasındaki düzensizlik (dalgalanma). Seste robotikleşmeye veya kesilmelere neden olur.
*   **MOS (Mean Opinion Score):** İnsan kulağının ses kalitesini nasıl algıladığını 1 ile 5 arasında puanlayan standart. 4.0 ve üzeri "mükemmel", 3.0 altı "kötü" kabul edilir.
*   **Latency (Gecikme):** Sesin bir uçtan diğer uca gitme süresi. İnsan beyni 150ms üzerindeki gecikmeleri fark eder ve telsiz gibi (yankılı) konuşmalar başlar.
*   **NAT Traversal:** Özel (Private) IP kullanan bir ağdaki telefonun, internet (Public) üzerindeki bir sunucuyla ses trafiğini, güvenlik duvarına takılmadan yürütebilmesi tekniği.
*   **SRTP (Secure RTP):** Ses veri paketlerinin AES algoritmalarıyla şifrelenmesi. Dinlenmeyi (Wiretapping) imkansız hale getirir.
*   **TLS (Transport Layer Security):** SIP sinyalleşme metinlerinin okunmasını engelleyen taşıma katmanı şifrelemesi.



---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


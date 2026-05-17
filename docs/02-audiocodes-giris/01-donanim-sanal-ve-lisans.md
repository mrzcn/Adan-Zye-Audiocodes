<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# Donanım, Sanal (VE) ve Lisanslama

AudioCodes Mediant serisi, ihtiyaca göre fiziksel donanım veya sanal sunucu üzerinde çalışan esnek bir mimari sunar. Bu bölümde Mediant 800 özelinde donanım yapısını ve lisanslama mantığını inceleyeceğiz.

## 📌 Donanım ve Platform Seçenekleri

AudioCodes SBC çözümleri üç ana formda karşımıza çıkar:

1.  **Fiziksel SBC (Mediant Hardware):** Mediant 500, 800, 1000, 2600, 4000 ve 9000 serileri. 
    *   **Mediant 800:** Küçük ve orta ölçekli işletmeler için idealdir. Hem SBC hem de Gateway (Analog/Dijital portlar) özelliklerini tek kutuda sunabilir.
2.  **Sanal SBC (Mediant VE - Virtual Edition):** VMware, Hyper-V, KVM gibi sanallaştırma platformları üzerinde çalışır.
3.  **Bulut SBC (Cloud Edition):** AWS, Azure ve Google Cloud üzerinde hazır imajlar olarak sunulur.

## 📌 Mediant 800 Fiziksel Yapısı ve Modülerlik

Mediant 800 cihazı (1U boyutunda) genellikle aşağıdaki port gruplarına sahiptir:
*   **Ethernet Portları (GE):** Sinyalleşme ve medya trafiği için kullanılır. İzolasyon için LAN (İç Ağ) ve WAN (Dış Ağ) ayrımı VLAN'lar ile veya fiziksel farklı kablolarla yapılır.
*   **OAMP Portu (Front Panel):** Cihazın yönetimi (Web arayüzü, SSH, SNMP) için ayrılmış izole yönetim portudur.
*   **Analog/Dijital Slotlar (Gateway Modu):** İhtiyaca göre FXS (analog telefon), FXO (Türk Telekom bakır hat) veya E1/T1 (PRI Dijital hat) modülleri takılarak PSTN ağlarına doğrudan çıkış sağlanabilir.

## 📌 Lisanslama Mantığı ve Kapasite Sınırları

AudioCodes cihazlarında "Aldığın kadar öde" mantığı geçerlidir. Donanım 400 çağrıyı kaldırabilecek güçte olsa bile lisansınız kadar çağrı yapabilirsiniz.

1.  **SBC Sessions (Concurrent Calls):** Aynı anda aktif olabilecek maksimum çağrı sayısıdır. Örneğin 100 Session lisansınız varsa, 101. çağrı cihaz tarafından `503 Service Unavailable` veya `480 Temporarily Unavailable` hatasıyla nazikçe reddedilir.
2.  **Transcoding Sessions:** Ses formatı dönüşümü (Örn: G.711 ↔ G.729) gerektiren çağrıların lisansıdır. Transcoding, cihazın içindeki DSP (Digital Signal Processor) çipini tüketir. DSP kapasitesi donanımsal olduğu için sadece lisans almak yetmez, cihazda uygun donanım modülünün olması gerekir.
3.  **Security (TLS/SRTP) Lisansı:** Bankalar veya çağrı merkezleri gibi sesi şifreli iletmek isteyen kurumlar için SIPS ve SRTP aktivasyon lisansıdır.
4.  **Floating License (Yüzer Lisans):** Birden fazla AudioCodes SBC'niz varsa, OVOC üzerinden tek bir lisans havuzu oluşturup, cihazların ihtiyaç duydukça bu havuzdan lisans çekip bırakmalarını sağlayan esnek mimaridir.

> [!TIP]
> Cihazınızın mevcut lisans durumunu görmek için Web arayüzünde **Setup > Device > License** menüsünü kullanabilirsiniz. "Maximum Number of SBC Sessions" satırı cihazınızın anlık kapasitesini gösterir.

> [!IMPORTANT]
> AudioCodes lisansları genellikle cihazın seri numarasına (MAC adresine) bağlıdır. Sanal (VE) sürümlerde ise "Hardware ID" veya Cloud Instance ID üzerinden lisanslama yapılır.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


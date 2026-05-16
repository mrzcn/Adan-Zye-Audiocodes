# Donanım, Sanal (VE) ve Lisanslama

AudioCodes Mediant serisi, ihtiyaca göre fiziksel donanım veya sanal sunucu üzerinde çalışan esnek bir mimari sunar. Bu bölümde Mediant 800 özelinde donanım yapısını ve lisanslama mantığını inceleyeceğiz.

## 📌 Donanım ve Platform Seçenekleri

AudioCodes SBC çözümleri üç ana formda karşımıza çıkar:

1.  **Fiziksel SBC (Mediant Hardware):** Mediant 500, 800, 1000, 2600, 4000 ve 9000 serileri. 
    *   **Mediant 800:** Küçük ve orta ölçekli işletmeler için idealdir. Hem SBC hem de Gateway (Analog/Dijital portlar) özelliklerini tek kutuda sunabilir.
2.  **Sanal SBC (Mediant VE - Virtual Edition):** VMware, Hyper-V, KVM gibi sanallaştırma platformları üzerinde çalışır.
3.  **Bulut SBC (Cloud Edition):** AWS, Azure ve Google Cloud üzerinde hazır imajlar olarak sunulur.

## 📌 Mediant 800 Fiziksel Yapısı

Mediant 800 cihazı üzerinde genellikle aşağıdaki port grupları bulunur:

*   **Ethernet Portları (GE):** Sinyalleşme ve medya trafiği için kullanılır. Genellikle LAN ve WAN ayrımı için farklı fiziksel portlar veya VLAN'lar tanımlanır.
*   **OAMP Portu:** Cihazın yönetimi (Web arayüzü, SSH, SNMP) için ayrılmış özel porttur.
*   **Analog/Dijital Slotlar:** İhtiyaca göre FXS (analog telefonlar), FXO (Türk Telekom analog hatlar) veya E1/T1 (PRI hatlar) modülleri takılabilir.

## 📌 Lisanslama Mantığı (SBC Capacity)

AudioCodes cihazlarında kapasite lisansla belirlenir. En kritik lisans kalemleri şunlardır:

*   **SBC Sessions:** Aynı anda aktif olabilecek maksimum çağrı sayısıdır. Lisans limitine ulaşıldığında cihaz yeni çağrıları `503 Service Unavailable` hatasıyla reddeder.
*   **Transcoding Sessions:** Ses codec dönüşümü (örneğin G.711'den G.729'a) gerektiren çağrıların sayısıdır. Her transcoding işlemi donanım kaynağı (DSP) tüketir.
*   **Security (TLS/SRTP):** Şifreli sinyalleşme ve medya için ek lisanslar gerekebilir.

> [!TIP]
> Cihazınızın mevcut lisans durumunu görmek için Web arayüzünde **Setup > Device > License** menüsünü kullanabilirsiniz. "Maximum Number of SBC Sessions" satırı cihazınızın anlık kapasitesini gösterir.

> [!IMPORTANT]
> AudioCodes lisansları genellikle cihazın seri numarasına (MAC adresine) bağlıdır. Sanal (VE) sürümlerde ise "Hardware ID" veya Cloud Instance ID üzerinden lisanslama yapılır.


---
> [!CAUTION]
> **Yasal Uyarı:** Bu dökümantasyon içeriği dijital filigran ve izleme sistemleri ile korunmaktadır. İçeriğin izinsiz kopyalanması, çoğaltılması veya başka platformlarda paylaşılması durumunda yasal süreç işletilecektir.

<div style="display:none">
Source: Adan-Zye-Audiocodes Repository
Owner: mrzcn
Partner: Nolto Teknoloji Anonim Şirketi (AudioCodes Turkey Partner)
Security ID: NLT-800-SBC-SEC-2026
</div>

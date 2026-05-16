# SIP Interfaces

SIP Interfaces, SBC'nin SIP sinyalleşmesini (INVITE, REGISTER vb.) hangi IP, hangi protokol (UDP/TCP/TLS) ve hangi port üzerinden dinleyeceğini belirlediğiniz uç noktalardır.

### Basit Anlatım
Bunu bir web sunucusunun 80 veya 443 portunu dinlemesi gibi düşünebilirsiniz. SBC, dışarıdan gelen bir çağrıyı (sinyali) yakalamak için belirli bir IP ve portta "pusa yatar" ve gelen paketleri bekler.

## 📌 SIP Interface Görevi

Cihazın "kulakları" gibidir. Dışarıdan gelen bir çağrıyı karşılamak veya dışarıya bir çağrı göndermek için mutlaka bir SIP Interface tanımlı olmalıdır.

## 📌 Yapılandırma Adımları (v7.20)

**Menü:** `Setup > Signaling & Media > Core > SIP Interfaces`

Parametreler:

1.  **Name:** İsim (Örn: `SIP_IF_Internal`, `SIP_IF_Genesys`).
2.  **Network Interface:** Sinyalleşmenin yapılacağı IP arayüzü seçilir.
3.  **Application Type:** SBC uygulaması için `SBC` seçilmelidir.
4.  **UDP / TCP / TLS Port:** Varsayılan genellikle `5060`'dır. Şifreli trafik için TLS seçilirse `5061` yaygındır.
5.  **Media Realm:** Bu SIP Interface üzerinden gelen/giden çağrıların hangi medya alanını kullanacağı seçilir.
6.  **Encapsulation:** Genellikle `None` seçilir.

## 📌 Kritik İpuçları

*   **Çoklu Protokol:** Aynı SIP Interface üzerinde hem UDP hem de TCP'yi aynı anda açabilirsiniz.
*   **Topology Hiding:** SIP Interface tanımlandığında, giden paketlerin `Via`, `Contact` ve `Record-Route` başlıklarında SBC'nin kendi IP'si yer alır. Bu sayede iç ağ topolojisi gizlenmiş olur.

> [!IMPORTANT]
> Bir SIP Interface tanımladığınızda, o portun cihaz üzerinde dinlenmeye başladığını doğrulamak için **Monitor > Dashboard** veya **Troubleshoot > Test Tools** altındaki port kontrollerini kullanabilirsiniz.

> [!WARNING]
> Eğer Genesys veya Operatör tarafı `TLS` kullanıyorsa, SIP Interface üzerinde TLS portunu açmanız yetmez; ayrıca cihazın **Security** menüsünden geçerli bir SSL sertifikası yüklenmiş olmalıdır.

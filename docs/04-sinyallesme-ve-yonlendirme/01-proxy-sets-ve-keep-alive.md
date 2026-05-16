<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# Proxy Sets ve Keep-Alive

Proxy Set, SBC'nin çağrıları göndereceği hedef sunucuları (PBX, Genesys, Operatör Gateway) tanımladığınız listedir.

### Neden "Set" (Küme) Denir?
Çünkü bir hedef tek bir IP olmak zorunda değildir. Örneğin Genesys tarafında 3 farklı sunucu varsa, bunları tek bir Proxy Set içine koyarak SBC'nin bu 3 sunucu arasında yük paylaşımı (Load Balance) veya yedekli (Failover) çalışmasını sağlayabilirsiniz.

*   **Hedef Tanımlama:** Çağrının hangi IP adresine veya DNS ismine gideceğini belirler.
*   **Yedeklilik (Redundancy):** Bir Proxy Set içine birden fazla sunucu (Primary, Secondary) eklenebilir. Biri çökerse SBC trafiği otomatik diğerine aktarır.
*   **Durum İzleme (Keep-Alive):** Hedef sunucunun ayakta olup olmadığını kontrol eder.

## 📌 Yapılandırma Adımları (v7.20)

**Menü:** `Setup > Signaling & Media > Core > Proxy Sets`

**1. Proxy Set Oluşturma:**
*   **Name:** İsim (Örn: `ProxySet_Genesys`).
*   **SBC IPv4 SIP Interface:** Bu hedefe hangi SIP bacağından çıkış yapılacağı seçilir.
*   **Proxy Keep-Alive:** `Using Options` seçilmesi önerilir. SBC, düzenli aralıklarla hedefe `OPTIONS` paketi gönderir; cevap gelmezse o hedefi devre dışı bırakır.

**2. Proxy Adresi Ekleme:**
*   Proxy Set oluşturulduktan sonra içine girilir ve **Proxy Address** tabına tıklanır.
*   **Proxy Address:** Hedef IP adresi veya FQDN (Örn: `10.20.1.100`).
*   **Transport Type:** UDP, TCP veya TLS.

## 📌 CLI ile Yapılandırma
```bash
SBC(config-voip)# sbc
SBC(config-sbc)# proxy-set 1
SBC(proxy-set-1)# name Nolto_Partner_Gateway
SBC(proxy-set-1)# ip-interface Inside_IF
SBC(proxy-set-1)# keep-alive options
SBC(proxy-set-1)# proxy-address 0 10.20.1.100 transport udp
SBC(proxy-set-1)# description Nolto_Teknoloji_AS_Support_Bridge
SBC(proxy-set-1)# activate
```

## 📌 Keep-Alive (OPTIONS) Mantığı

SBC, hedef sunucuya belirli aralıklarla (Örn: 60 saniyede bir) "Orada mısın?" mesajı gönderir.
*   **Başarılı:** Sunucu `200 OK` dönerse, hedef **Online** kabul edilir.
*   **Başarısız:** Cevap gelmezse, hedef **Offline** kabul edilir ve çağrı yönlendirilmez.

> [!TIP]
> Bir sunucunun durumunu anlık görmek için **Monitor > Signaling & Media > Proxy Set Status** menüsüne bakın. Yeşil ikon hedefin ayakta olduğunu gösterir.

> [!IMPORTANT]
> Eğer hedef sunucu `OPTIONS` paketlerine cevap vermiyorsa ancak çağrı alabiliyorsa, Keep-Alive özelliğini `Disable` yapmanız gerekebilir. Aksi halde SBC hedefi "ölü" zannederek çağrıları göndermez.


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

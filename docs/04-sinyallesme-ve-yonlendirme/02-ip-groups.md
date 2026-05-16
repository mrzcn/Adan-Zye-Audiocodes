<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# IP Groups

IP Group, AudioCodes SBC yapılandırmasının "kalbi" sayılabilir. Bir SIP Interface, bir Proxy Set ve bir IP Profile'ı bir araya getirerek mantıksal bir "Uç Nokta" (Entity) oluşturur.

## 📌 IP Group Neden Önemlidir?

Tüm yönlendirme kuralları (IP-to-IP Routing) IP Group'lar üzerinden yapılır. "Genesys'ten gelen çağrıları VoIP Gateway'e gönder" derken aslında "Genesys IP Group'undan gelenleri VoIP_GW IP Group'una gönder" demiş oluruz.

## 📌 Yapılandırma Adımları (v7.20)

**Menü:** `Setup > Signaling & Media > Core > IP Groups`

Yeni bir IP Group eklerken şu eşleştirmeler yapılır:

1.  **Name:** İsim (Örn: `IPG_Genesys`, `IPG_Operator`).
2.  **Type:** 
    *   **Server:** Genellikle santral, gateway veya operatör için seçilir.
    *   **User:** Kayıt olan (Registration) IP telefonlar için seçilir.
3.  **Proxy Set:** Bu grubun hangi sunucu listesine gideceği seçilir.
4.  **IP Profile:** Bu grubun uyması gereken kurallar seti seçilir (Codec, Başlık ayarları vb.).
5.  **Media Realm:** Bu gruptan gelen/giden sesin hangi medya alanını kullanacağı seçilir.
6.  **SIP Interface:** Bu grubun hangi sinyalleşme ucunu kullanacağı seçilir.

## 📌 CLI ile Yapılandırma
```bash
SBC(config-sbc)# ip-group 1
SBC(ip-group-1)# name IPG_Nolto_Partner
SBC(ip-group-1)# type server
SBC(ip-group-1)# proxy-set 1
SBC(ip-group-1)# ip-profile 1
SBC(ip-group-1)# media-realm MR_LAN
SBC(ip-group-1)# sip-interface 1
SBC(ip-group-1)# description Nolto_Teknoloji_AS_Enterprise_Trunk
SBC(ip-group-1)# activate
```

## 📌 Kritik Parametreler

*   **SIP Group Name:** Eğer karşı taraf SBC'den belirli bir domain ismi bekliyorsa buraya yazılır (Örn: `genesys.local`).
*   **Inbound/Outbound Message Manipulation:** Bu IP Group'a özel SIP başlık değişiklikleri yapılacaksa buradan set seçilir.

> [!TIP]
> IP Group tanımlarken seçtiğiniz **Media Realm** ile **SIP Interface**'in Media Realm ayarının birbiriyle uyumlu olduğundan emin olun. Karışıklık yaşanmaması için genellikle her bacak için tek bir Media Realm kullanılır.

> [!NOTE]
> IP Group oluşturduğunuzda cihaz otomatik olarak bu gruptan gelen çağrıları kabul etmeye başlar (Eğer Classification kuralı doğruysa). Bu, güvenlik için ilk savunma hattıdır.


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

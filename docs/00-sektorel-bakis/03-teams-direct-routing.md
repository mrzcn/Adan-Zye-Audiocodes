<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# Teams Direct Routing Nedir?

Modern iş dünyasında iletişim Microsoft Teams üzerinden dönüyor. Ancak Teams'in dış dünyayı (GSM veya Sabit Hatlar) araması için bir "köprüye" ihtiyacı vardır. İşte bu köprüye **Teams Direct Routing** diyoruz ve bu köprünün tam ortasında **AudioCodes SBC** durur.

## 📌 Temel Kavram

Normalde Teams kullanırken dış hatları aramak için Microsoft'tan "Calling Plan" almanız gerekir (Pahalı ve her ülkede yok). **Direct Routing** ise şirketin mevcut operatörünü (Örn: Türk Telekom) Teams'e bağlamanıza izin verir.

## 📌 AudioCodes SBC Burada Ne Yapar?

1.  **Protokol Uyumu:** Teams, bulut üzerinden sadece **TLS (Şifreli SIP)** ve **SRTP (Şifreli Ses)** kabul eder. Operatörler ise genellikle UDP/TCP ve şifresiz RTP kullanır. AudioCodes bu iki farklı dünyayı birbirine bağlar (Transcoding & Trans-shaping).
2.  **Sertifika Yönetimi:** Teams ile konuşmak için SBC üzerinde geçerli bir SSL sertifikası (Public CA) olması gerekir.
3.  **Güvenlik:** Teams sunucularından gelen trafiği doğrular ve iç ağa güvenli bir şekilde aktarır.
4.  **Media Bypass:** Eğer kullanıcı ve SBC aynı ağdaysa, ses trafiğinin buluta gidip gelmesine gerek kalmadan doğrudan (local) akmasını sağlar.

## 📌 Neden Önemlidir?

Bir yeni mezun için Teams Direct Routing öğrenmek, "Cloud Communications" (Bulut Haberleşme) dünyasına giriş anahtarıdır. AudioCodes, Microsoft tarafından bu iş için en çok tavsiye edilen (Certified for Microsoft Teams) markadır.

---

### Yapılandırma Akış Diyagramı

```mermaid
graph LR
    A[Microsoft Teams Bulutu] --(TLS/SRTP)--> B((AudioCodes SBC))
    B --(UDP/RTP)--> C[Yerel Operatör / PSTN]
    
    subgraph Credits
    D[Prepared by mrzcn for Nolto Partner Projects]
    end
    
    style B fill:#6264A7,stroke:#333,stroke-width:2px,color:#fff
```

> [!IMPORTANT]
> Teams Direct Routing kurulumu yaparken SBC'nin FQDN adresinin (Örn: `sbc.nolto.com`) internete açık olması ve 5061 portunun Microsoft IP'lerine izin verecek şekilde ayarlanmış olması gerekir.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


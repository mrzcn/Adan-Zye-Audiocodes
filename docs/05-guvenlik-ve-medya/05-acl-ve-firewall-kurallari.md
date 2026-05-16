<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# ACL ve Firewall Kuralları

SBC üzerindeki en güçlü güvenlik katmanlarından biri Erişim Kontrol Listeleri (ACL) ve SIP Firewall mekanizmasıdır.

## 📌 ACL (Access Control List) Nedir?

ACL, SBC'nin yönetim arayüzlerine (Web, SSH, SNMP) hangi IP adreslerinden erişilebileceğini belirleyen beyaz listedir (Whitelist).

**Yapılandırma:** `Setup > Device > Security > Management ACL`

*   **Action:** `Permit` (İzin ver) veya `Deny` (Reddet).
*   **Source IP:** İzin verilen mühendislik bilgisayarının veya yönetim sunucusunun IP'si.
*   **Service:** Web (HTTPS), SSH, Telnet vb.

> [!IMPORTANT]
> ACL kuralı yazarken kendi IP adresinize izin vermeden "Deny All" kuralı eklerseniz cihazın erişimini tamamen kaybedersiniz! Her zaman önce kendinize izin verin.

## 📌 SIP Firewall

SIP Firewall, sadece sinyalleşme paketlerini (Port 5060/5061) denetler.

**Yapılandırma:** `Setup > Signaling & Media > SBC > Firewall`

1.  **Classification kuralları:** Eğer bir IP adresi herhangi bir IP Group ile eşleşmiyorsa SBC bu paketi direkt çöpe atar.
2.  **Blacklist:** Manuel olarak engellemek istediğiniz IP'leri buraya ekleyebilirsiniz.

## 📌 CLI ile ACL Kuralı Ekleme
```bash
SBC(config-device)# security
SBC(config-security)# management-acl 1
SBC(mgmt-acl-1)# ip-address 192.168.1.50
SBC(mgmt-acl-1)# prefix-length 32
SBC(mgmt-acl-1)# service-type https
SBC(mgmt-acl-1)# action permit
SBC(mgmt-acl-1)# activate
```

## 📌 Brute Force Koruması

**Menü:** `Setup > Device > Security > Web/CLI Access Control`
*   Buradan hatalı giriş denemesi sınırını (Örn: 3 deneme) ve bloklama süresini (Örn: 30 dakika) ayarlayabilirsiniz.


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

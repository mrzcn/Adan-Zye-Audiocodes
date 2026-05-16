<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# Hardening ve DoS Koruması

SBC'nin güvenliğini en üst seviyeye çıkarmak için yapılması gereken "sıkılaştırma" (Hardening) işlemleri ve saldırı önleme teknikleri.

## 📌 20 Maddelik Hardening Kontrol Listesi

Bir SBC'yi yayına almadan önce mutlaka bu listeyi kontrol edin:

1.  [ ] Varsayılan `Admin` şifresini değiştirin.
2.  [ ] Gereksiz servisleri (Telnet, FTP, HTTP) kapatın. Sadece HTTPS ve SSH kullanın.
3.  [ ] Web arayüzü oturum zaman aşımını (Session Timeout) 5 dakikaya düşürün.
4.  [ ] SSH için varsayılan 22 portunu değiştirin.
5.  [ ] SNMP kullanmıyorsanız kapatın, kullanıyorsanız `Community String` değerini karmaşıklaştırın.
6.  [ ] `Unregistered Calls` ayarını `Restrict` yapın.
7.  [ ] Sadece izinli IP'lerden yönetim erişimine izin verin (Access Control List).
8.  [ ] Ping (ICMP) isteklerine yanıt vermeyi kapatın.
9.  [ ] Cihaz üzerindeki tüm boş IP Interface'leri pasife çekin.
10. [ ] `SBC Media Security` modunu her zaman en az `Symmetric` yapın.
11. [ ] SIP portlarını (5060/5061) sadece ilgili Proxy IP'lerine açın.
12. [ ] Kullanılmayan Codec'leri Coder Group'tan çıkarın.
13. [ ] Yazılım güncellemelerini (Security Patches) düzenli takip edin.
14. [ ] Başarısız giriş denemeleri için bloklama (Brute Force Protection) aktif edin.
15. [ ] TLS sertifikalarını güncel ve güvenilir otoritelerden alın.
16. [ ] `Topology Hiding` özelliğinin tüm bacaklarda aktif olduğunu doğrulayın.
17. [ ] `Pass-through Unknown Headers` ayarını sadece ihtiyaç varsa açın.
18. [ ] Log seviyesini üretim ortamında `Warning` veya `Notice` seviyesinde tutun (CPU koruması için).
19. [ ] Cihazın fiziksel güvenliğini (Kilitli kabin) sağlayın.
20. [ ] Konfigürasyon yedeklerini şifreli bir ortamda saklayın.

## 📌 DoS (Denial of Service) Koruması

AudioCodes SBC, saniyede gelen paket sayısını izleyerek saldırıları engelleyebilir.

**Yapılandırma:** `Setup > Device > Security > IDS Rules`

*   **SIP Method Threshold:** Örneğin bir IP'den saniyede 100'den fazla `INVITE` gelirse o IP'yi otomatik olarak karantinaya (Blacklist) alabilir.
*   **Max Number of SIP Dialogs:** Sistem kapasitesini aşan eş zamanlı çağrı taleplerini reddederek sistemin çökmesini engeller.

> [!WARNING]
> DoS ayarlarını çok agresif yapmak (Örn: Saniyede 5 paket sınırı), yoğun trafik anında gerçek kullanıcıların da engellenmesine neden olabilir. Bu değerleri projenin çağrı yoğunluğuna göre belirleyin.


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

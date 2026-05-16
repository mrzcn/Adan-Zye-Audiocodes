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

## 📌 Yönetim Katmanı Güvenliği (Management Hardening)

SBC'nin kontrol paneline erişimi kısıtlamak, saldırıların %90'ını durdurur.
*   **Access Control List (ACL):** `Setup > Device > Security > Management ACL` menüsünden sadece belirli bir IP bloğuna (Örn: `10.10.1.0/24`) SSH ve Web erişimi izni verin. Diğer tüm IP'lerden gelen talepler sessizce düşürülecektir.
*   **Service Restriction:** Web yönetim portunu (443) ve SSH portunu (22) standart dışı yüksek portlara (Örn: 8443, 2222) taşımak, otomatik scanner araçlarının işini zorlaştırır.

## 📌 IDS/IPS ve Anomaly Detection (Derin Analiz)

AudioCodes v7.20, sinyalleşme paketlerini gerçek zamanlı olarak analiz eden bir **IDS (Intrusion Detection System)** barındırır.

**Menü:** `Setup > Device > Security > IDS Rules`

### 1. SIP Method Thresholds
Saniyede gelen SIP mesaj sayısını limitler.
*   **Senaryo:** Bir saldırgan saniyede binlerce `OPTIONS` veya `INVITE` göndererek cihazın CPU'sunu kilitlemeye çalışabilir.
*   **Öneri:** Normal çağrı yoğunluğunuzun 3-4 katı bir eşik değer (Threshold) belirleyin.

### 2. Anomaly Detection (Anormallik Tespiti)
SBC, standart dışı SIP paketlerini (Örn: Bozuk başlıklar, çok uzun paketler) tespit edebilir.
*   **Malformed Packet:** SIP standartlarına uymayan paketleri anında drop eder.
*   **Max Header Length:** Çok uzun (Buffer overflow saldırısı amaçlı) başlıkları engeller.

### 3. Dinamik Kara Liste (Dynamic Blacklist)
Bir kural ihlal edildiğinde SBC saldırgan IP'yi otomatik olarak kara listeye alır.
*   **Duration:** Saldırganın ne kadar süreyle bloklanacağını belirler (Örn: 3600 saniye).
*   **Threshold:** Kaç ihlalden sonra kara listeye alınacağını belirler.

## 📌 SIP TLS Zorunluluğu

İnternet bacağından gelen trafiği şifrelemek sadece bir seçenek değil, bir zorunluluktur.
*   **SIPS:** Port 5061 üzerinden sertifikalı bağlantı.
*   **Mutual TLS:** Sadece SBC'nin karşı tarafı değil, karşı tarafın da SBC'yi sertifika ile doğruladığı en üst düzey güvenlik modu.

## 📌 Güvenlik Olaylarını İzleme ve Alarm

Bir saldırı anında haberdar olmak için:
*   **SNMP Traps:** IDS kuralı tetiklendiğinde izleme sunucusuna alarm gönderir.
*   **Security Logs:** `Status & Diagnostics > Logs > Security Logs` altından hangi IP'nin neden engellendiğini görebilirsiniz.

> [!WARNING]
> **DoS Yanlış Pozitifler:** Eğer ağınızda çok sayıda SIP cihazı varsa (Örn: IP Telefonlar), bu cihazların eş zamanlı kayıt (Register) olma talepleri DoS koruması tarafından bir "saldırı" olarak algılanabilir. Kuralları yazarken `Registration Rate` değerlerini dikkate alın.

> [!IMPORTANT]
> **Ping (ICMP) Kapatma:** Bir saldırganın ilk yapacağı şey cihazın "canlı" olup olmadığını anlamak için ping atmaktır. `Setup > Network > Core > IP Interfaces` altından her arayüz için Ping (ICMP) yanıtını kapatmak cihazı internette "görünmez" kılar.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


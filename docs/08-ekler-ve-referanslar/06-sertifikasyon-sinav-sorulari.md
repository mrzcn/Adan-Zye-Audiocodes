<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# AudioCodes ACP (Certified Professional) Sertifikasyon Sınav Soru ve Cevapları

Bu kılavuz, AudioCodes resmi sertifikasyon sınavlarında (ACP - AudioCodes Certified Professional ve ACA - Certified Associate) çıkan soru tiplerini, senaryoları ve L3 seviyesinde teknik açıklamaları içermektedir. Sınava hazırlanan veya saha yetkinliklerini test etmek isteyen mühendisler için bir referans kaynağıdır.

---

## 📝 ACP Sınavı Soru ve Kök Neden Analizleri

### ❓ Soru 1: Inbound Classification Hiyerarşisi
**Gelen bir SIP INVITE paketinin sınıflandırılması (Inbound Classification) sırasında, SBC eşleşmeyi hangi öncelik sırasına göre gerçekleştirir?**

*   **A)** SIP Interface ──> Source IP ──> Request-URI ──> Source Port
*   **B)** Source IP ──> SIP Interface ──> Request-URI ──> Source Port
*   **C)** Source IP ──> Request-URI ──> SIP Interface ──> Source Port
*   **D)** SIP Interface ──> Request-URI ──> Source IP ──> Source Port

>   **🔑 Doğru Cevap: A**
>
>   **🧠 Derinlemesine Açıklama:**
>   AudioCodes SBC, gelen paketi sınıflandırırken her zaman **fiziksel/mantıksal giriş kapısından** başlar. İlk olarak çağrının ulaştığı **SIP Interface** kontrol edilir. Ardından gelen paketin **Source IP** (Kaynak IP) adresi sorgulanır. Eğer hala benzersiz bir eşleşme sağlanamadıysa paket üzerindeki **Request-URI** (hedef SIP adresi/domain) ve son olarak **Source Port** (Kaynak Port) parametreleri analiz edilerek ilgili mantıksal **IP Group** eşleşmesi tamamlanır.

---

### ❓ Soru 2: Alternative Routing Tetikleyicileri
**Aşağıdaki SIP yanıt kodlarından hangisi, IP-to-IP Routing tablosunda tanımlanan "Alternative Routing Table" (Yedek Hat) mekanizmasını varsayılan olarak TETİKLEMEZ?**

*   **A)** SIP 503 Service Unavailable
*   **B)** SIP 408 Request Timeout
*   **C)** SIP 486 Busy Here
*   **D)** SIP 500 Server Internal Error

>   **🔑 Doğru Cevap: C**
>
>   **🧠 Derinlemesine Açıklama:**
>   Alternative Routing, **sistem veya ağ seviyesindeki kesintilerde** (failover) çağrının kurtarılması için tasarlanmıştır. `503` (Sunucu kapalı), `408` (Zaman aşımı) ve `500` (Sunucu hatası) gibi yanıtlar yedek yönü tetikler. Ancak **`486 Busy Here` (Meşgul)** veya `480 Temporarily Unavailable` gibi son kullanıcı meşguliyet veya hat meşguliyeti belirten kullanıcı bazlı SIP yanıtları, hattın arızalı olduğunu göstermediği için yedek yönü tetiklemez; çağrı doğrudan sonlandırılır.

---

### ❓ Soru 3: Media Anchoring (RTP Kilitleme) Gereksinimi
**SBC arkasındaki (LAN) bir IP-PBX'ten, internet üzerindeki (WAN) bir operatöre çağrı gönderildiğinde ses paketlerinin tek taraflı (One-way Audio) gitmesinin veya hiç iletilmemesinin en olası nedeni ve IP Profile çözüm ayarı nedir?**

*   **A)** Media Realm atanmaması / IP Profile içindeki `SBC Media` parametresini `Transcoding` yapmak.
*   **B)** NAT arkası çakışma / IP Profile içindeki `SBC Media` parametresini `SBC (Media Anchor)` yapmak.
*   **C)** SIP Interface port uyuşmazlığı / IP Profile içindeki `SBC Media` parametresini `Bypass` yapmak.
*   **D)** Donanımsal DSP arızası / IP Profile içindeki `SBC Media` parametresini `Force` yapmak.

>   **🔑 Doğru Cevap: B**
>
>   **🧠 Derinlemesine Açıklama:**
>   One-way audio (tek yönlü ses) sorunlarının %90'ı, ses paketlerinin (RTP) uç noktaların kendi yerel IP adreslerini doğrudan pakete yazması ve aradaki NAT cihazının bu paketleri geçirmemesinden kaynaklanır. Çözüm, SBC'nin ses bacaklarını kendi üzerine kilitlemesidir. IP Profile altındaki **`SBC Media` = `SBC` (yani Media Anchor/RTP Latching)** yapıldığında, SBC hem Leg A hem de Leg B ses paketlerini kendi arayüzleri üzerinden geçirerek NAT/Firewall engellerini aşar.

---

### ❓ Soru 4: SRD (Signaling Routing Domain) İzolasını Aşma
**Aynı AudioCodes SBC üzerinde yapılandırılmış `SRD_LAN` ve `SRD_WAN` adında iki ayrı SRD bulunmaktadır. Varsayılan olarak bu iki alan arasındaki çağrı geçişi engellenmiştir. Bu iki bağımsız ağ arasında çağrı yönlendirmesine izin vermek için ne yapılmalıdır?**

*   **A)** İki SRD'nin ID'lerini aynı yapmak.
*   **B)** IP Interfaces menüsünde iki bacağa da aynı ağ maskesini tanımlamak.
*   **C)** `IP-to-IP Routing` tablosunda kaynak ve hedef SRD parametrelerini açıkça belirtip kural yazmak.
*   **D)** Cihazı "Global Bridge" moduna almak.

>   **🔑 Doğru Cevap: C**
>
>   **🧠 Derinlemesine Açıklama:**
>   Farklı SRD'ler (Sinyalleşme Yönlendirme Alanları) VRF gibi çalışırlar ve aralarında varsayılan olarak kesinlikle geçiş yoktur. Ancak iki ağ arasında kontrollü bir köprü kurmak istiyorsanız, **`IP-to-IP Routing`** tablosunda yeni bir kural ekleyip `Source SRD` ve `Destination SRD` alanlarını açıkça atayarak SBC B2BUA katmanında bu iki dünyayı birbirine güvenle konuşturabilirsiniz.

---

### ❓ Soru 5: Sinyalleşme ve Manipülasyon İşlem Sırası (Pipeline)
**Bir çağrı SBC'ye ulaştığında ve dışarı gönderildiğinde, uygulanan manipülasyon ve yönlendirme işlemlerinin doğru sırası aşağıdakilerden hangisidir?**

*   **A)** Inbound SIP Msg Manipulation ──> Inbound Classification ──> Inbound Number Manipulation ──> IP-to-IP Routing ──> Outbound Number Manipulation ──> Outbound SIP Msg Manipulation
*   **B)** Inbound Number Manipulation ──> Inbound SIP Msg Manipulation ──> Inbound Classification ──> IP-to-IP Routing ──> Outbound SIP Msg Manipulation ──> Outbound Number Manipulation
*   **C)** Inbound Classification ──> Inbound Number Manipulation ──> IP-to-IP Routing ──> Outbound Number Manipulation ──> Outbound SIP Msg Manipulation
*   **D)** Inbound SIP Msg Manipulation ──> IP-to-IP Routing ──> Inbound Number Manipulation ──> Outbound Number Manipulation ──> Outbound SIP Msg Manipulation

>   **🔑 Doğru Cevap: A**
>
>   **🧠 Derinlemesine Açıklama:**
>   Çağrı işleme boru hattı (Pipeline) sırasıyla şöyledir:
>   1.  SBC gelen ham SIP paketini parse eder ve **Inbound SIP Message Manipulation** kurallarını çalıştırır.
>   2.  Ham paket işlendikten sonra çağrı bir IP Group ile eşleştirilir (**Inbound Classification**).
>   3.  Eşleşen grubun numara kuralları çalıştırılır (**Inbound Number Manipulation**).
>   4.  Dönüştürülmüş numara ile yönlendirme tablosu taranır (**IP-to-IP Routing**).
>   5.  Hedef grubun çıkış numara kuralları çalıştırılır (**Outbound Number Manipulation**).
>   6.  Son olarak, paket hattan çıkmadan hemen önce giden bacak manipülasyonları uygulanır (**Outbound SIP Msg Manipulation**).

---

### ❓ Soru 6: Unregistered Calls Parametresi
**Güvenlik sıkılaştırması (Hardening) sırasında, internet bacağından (WAN) gelen tarama (SIP Scanner / Bruteforce) saldırılarını CPU'yu yormadan doğrudan engellemek için `SBC General Settings` altındaki hangi parametre `Restrict` yapılmalıdır?**

*   **A)** `Anonymous Calls`
*   **B)** `Unregistered Calls`
*   **C)** `NAT Traversal`
*   **D)** `Direct Media`

>   **🔑 Doğru Cevap: B**
>
>   **🧠 Derinlemesine Açıklama:**
>   **`Unregistered Calls`** parametresi `Restrict` yapıldığında SBC; sistemde kayıtlı olmayan, kimliği doğrulanmamış veya `Inbound Classification` tablosundaki hiçbir IP Group ile eşleşmeyen kaynaklardan gelen tüm SIP `INVITE` veya `REGISTER` isteklerini anında bloklar. Bu sayede cihaz internetten gelen brute-force (saldırı) taramalarını işleme alıp CPU tüketmeden en dış sınırda keser.

---

### ❓ Soru 7: Microsoft Teams TLS ve SRTP Uyumluluğu
**Bir AudioCodes SBC'yi Microsoft Teams Direct Routing altyapısına bağlamak için lisans anahtarında (License Key) kesinlikle bulunması gereken minimum iki özellik flag'i nedir?**

*   **A)** `SBC Sessions` ve `Transcoding`
*   **B)** `SW/TEAMS` ve `Security (TLS/SRTP)`
*   **C)** `High Availability` ve `SBC Sessions`
*   **D)** `Floating License` ve `Voice Quality`

>   **🔑 Doğru Cevap: B**
>
>   **🧠 Derinlemesine Açıklama:**
>   Microsoft Teams Direct Routing bulut altyapısı, güvenli olmayan standart SIP (UDP/TCP 5060) bağlantılarını kesinlikle kabul etmez. Teams entegrasyonu için sinyalleşmenin zorunlu TLS (5061) ve ses paketlerinin SRTP ile şifrelenmesi şarttır. Bu yeteneklerin aktif olması için lisans anahtarında **`Security` (TLS/SRTP)** şifreleme motorunun ve Teams'e özel SIP başlıklarını çalıştıran **`SW/TEAMS`** özelliğinin aktif olması zorunludur.

---

### ❓ Soru 8: Donanımsal DSP ve Transcoding Limiti
**SBC donanımında (Örn: Mediant 800) ses codec dönüşümü (G.711'den G.729'a Transcoding) yapılmaktadır. Transcoding kapasitesi neye göre sınırlandırılır ve donanım yetersiz kaldığında ne olur?**

*   **A)** Tamamen RAM kapasitesine / Çağrılar G.711 olarak kurulmaya devam eder.
*   **B)** Lisanslı SBC Sessions miktarına / Cihaz kilitlenir.
*   **C)** Donanımsal DSP Chip sayısına ve Transcoding Lisansına / Uyuşmayan çağrı `488 Not Acceptable Here` ile sonlanır.
*   **D)** IP Interface bant genişliğine / Ses tek taraflı gider.

>   **🔑 Doğru Cevap: C**
>
>   **🧠 Derinlemesine Açıklama:**
>   Codec transcoding (dönüştürme) işlemi yüksek işlem gücü gerektirir ve bu işlem donanım üzerindeki **DSP (Digital Signal Processor) çiplerinde** gerçekleştirilir. Cihazın transcoding kapasitesi, donanımdaki fiziksel DSP chip sayısı ve lisanslanan `Transcoding Sessions` limiti ile sınırlıdır. Bu limit aşıldığında veya DSP kaynakları tükendiğinde, SBC uyuşmayan yeni çağrıları codec anlaşması yapamadığı için **`488 Not Acceptable Here`** SIP hata koduyla sonlandırır.

---

### ❓ Soru 9: SIP OPTIONS Ping (Keep-Alive) ve Durum Geçişleri
**Bir Proxy Set içindeki sunucuların aktiflik durumunu (Keep-Alive) denetlemek için SIP OPTIONS ping mesajları gönderilmektedir. Bir sunucunun "Inoperative" (Çevrimdışı) olarak işaretlenmesi için varsayılan tolerans nedir?**

*   **A)** Üst üste 5 adet OPTIONS pingine yanıt alınamaması.
*   **B)**OPTIONS pingine 30 saniye boyunca hiç yanıt gelmemesi.
*   **C)** Sunucunun `503 Service Unavailable` dönmesi veya ping isteklerine ardışık olarak yanıt vermemesi.
*   **D)** Sunucunun IP adresinin ağdan (Ping/ICMP) düşmesi.

>   **🔑 Doğru Cevap: C**
>
>   **🧠 Derinlemesine Açıklama:**
>   SBC, Proxy Set içindeki her hedefe periyodik OPTIONS mesajları gönderir. Eğer hedef sunucu bu isteklere yanıt veremezse veya ardışık olarak başarısızlık (Timeout / 503) dönerse, SBC sunucuyu **"Inoperative"** olarak işaretler ve o yöne çağrı göndermeyi durdurarak Alternative Route'a sapar. Ağ seviyesindeki ICMP ping (Ping/Echo) istekleri SIP OPTIONS yerine kullanılamaz; denetim mutlaka uygulama (SIP) katmanında olmalıdır.

---

### ❓ Soru 10: CLIR (Arayan Gizleme) Manipülasyon Başlığı
**Outbound Manipulation kuralında arayan numara kimliğini gizlemek (CLIR - Calling Line Identification Restriction) amacıyla `Calling Presentation` parametresi `Restricted` yapıldığında, SBC giden SIP INVITE mesajına hangi başlığı ekler?**

*   **A)** `Privacy: id`
*   **B)** `P-Asserted-Identity: anonymous`
*   **C)** `From: private`
*   **D)** `Remote-Party-ID: restrict`

>   **🔑 Doğru Cevap: A**
>
>   **🧠 Derinlemesine Açıklama:**
>   Arayan numara gizleme (Restricted) aktif edildiğinde, AudioCodes SBC standart RFC 3323 uyumluluğuna göre SIP INVITE paketinin içerisine **`Privacy: id`** (veya `Privacy: user;id`) başlığını ekler ve `From` başlığını `anonymous@anonymous.invalid` olarak maskeler. Bu sayede çağrının geçtiği diğer operatörler numaranın son kullanıcıya gösterilmesini engeller.

---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>

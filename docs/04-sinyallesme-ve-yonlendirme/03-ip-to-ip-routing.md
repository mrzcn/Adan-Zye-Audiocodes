<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# IP-to-IP Routing ve Arama Yönlendirme Mimarisi

Bir AudioCodes SBC'nin en temel görevi, farklı ağlardan (Leg A) gelen çağrıları doğru hedef ağlara (Leg B) güvenli ve kesintisiz yönlendirmektir. Bu süreç, sadece basit bir "IP yönlendirmesi" değildir. SBC bir B2BUA olarak çalıştığı için, sinyalleşme parametrelerini, numaraları ve başlıkları (Headers) analiz ederek dinamik kararlar verir.

---

## 📌 1. Arayüz Sınıflandırma (Inbound Classification) Mimarisi

SBC'ye bir `INVITE` mesajı ulaştığında, cihazın bu çağrıyı hangi güvenlik kuralları ve yönlendirme tablosuyla işleyeceğini bilmesi gerekir. Bu eşleştirme işlemine **Inbound Classification (Giriş Sınıflandırması)** denir.

### Sınıflandırma Nasıl Çalışır?
SBC, gelen SIP paketindeki şu parametreleri analiz eder ve öncelik sırasına göre eşleştirmeye çalışır:
1.  **Kaynak IP Adresi (Source IP Address):** Paketin hangi IP adresinden geldiği (Örn: `195.175.x.x` operatör IP'si).
2.  **SIP Interface:** Çağrının hangi fiziksel veya mantıksal ağ arayüzünden girdiği (Örn: `WAN_Interface` veya `LAN_Interface`).
3.  **Source Port:** Çağrının geldiği port (Örn: 5060, 5061).
4.  **Request-URI:** Gelen paketin kime gittiği veya hangi sunucu adresiyle geldiği.

```
+------------------+      +---------------------------+      +---------------------------+
| Gelen SIP INVITE | ===> | Inbound Classification    | ===> | IP Group Ataması          |
| (IP, Port, URI)  |      | (Eşleşme Kriterleri Test) |      | (Örn: Operator_IPGroup)   |
+------------------+      +---------------------------+      +---------------------------+
```

> [!CAUTION]
> **Sınıflandırma Hatası (Classification Failure):** Eğer SBC, gelen çağrıyı tanımlanmış herhangi bir **IP Group** ile eşleştiremezse, çağrıyı güvenlik gerekçesiyle anında drop eder veya `404 Not Found` / `488 Not Acceptable` hatası döner. Bu hata Syslog'da *"Failed to classify call"* şeklinde görünür.

---

## 📌 2. IP-to-IP Routing Tablosu Parametreleri (v7.20)

Eşleşen giriş grubu belirlendikten sonra, SBC **IP-to-IP Routing** tablosunu yukarıdan aşağıya doğru taramaya başlar.

**Arayüz Yolu:** `Setup > Signaling & Media > SBC > Routing > IP-to-IP Routing`

Yeni bir kural oluştururken yapılandırılması gereken kritik kolonlar ve teknik anlamları şunlardır:

*   **Name:** Kuralın ne iş yaptığını belirten açıklayıcı isim (Örn: `Route_Teams_to_Operator` veya `Route_PBX_to_Teams`).
*   **Source IP Group:** Çağrının hangi gruptan geldiği (Örn: `Genesys_IPGroup`).
*   **Source Username Prefix:** Arayan numara maskesi. Belirli bir arayan numaraya göre yönlendirmek için kullanılır (Örn: `+90212*`).
*   **Destination Username Prefix:** Aranan numara maskesi. Çağrının hedefini belirleyen en kritik alandır (Örn: `*` her şey, `00*` uluslararası aramalar).
*   **Destination Type:** Çağrının nasıl yönlendirileceğini seçer:
    *   **IP Group:** Çağrıyı doğrudan belirli bir SIP Trunk veya santral IP grubuna gönderir.
    *   **Request URI:** Paketin üzerindeki orijinal hedefe dokunmadan aynen iletir.
    *   **Alternative Routing Table:** Birincil hedefe ulaşılamadığında yedek yolları dener.
*   **Destination IP Group:** Çağrının gönderileceği hedef grup (Örn: `TürkTelekom_Trunk`).
*   **Cost:** Aynı kriterleri taşıyan kurallar arasında öncelik sırasını belirler. **Düşük maliyetli (düşük Cost) kural her zaman önceliklidir.**

---

## 📌 3. İleri Düzey Yönlendirme ve Yedeklilik Senaryoları

### A. Alternative Routing (Otomatik Failover / Yedek Hat)
Operatör devrelerinde veya santrallerde yaşanan kesintilerde çağrıların düşmemesi için yedek yollar kurgulanmalıdır.
*   **Çalışma Mantığı:** SBC, birincil yöne (Primary Route) çağrıyı gönderir. Eğer karşı taraftan `503 Service Unavailable`, `408 Request Timeout` veya `500 Server Internal Error` yanıtı gelirse (veya SIP Keep-Alive başarısız olursa), çağrıyı kesmeden anında listedeki ikinci yedek hatta (Alternative Route) yönlendirir.
*   **Uygulama:** Yönlendirme kuralında `Destination Type` alanı `Alternative Routing Table` olarak yapılandırılır. `Alternative Routing` tablosunda hedefler `Primary` ve `Alternative` olarak rollerine göre dizilir.

### B. Load Balancing (Yük Dengeleme)
Yüksek trafikli çağrı merkezlerinde veya birden fazla bulut sunucusu olan yapılarda çağrıyı eşit dağıtmak gerekir.
*   **Proxy Set Tabanlı Yük Dengeleme:** IP Group'a bağlı olan **Proxy Set** menüsünden `Proxy Load Balancing Method` seçeneği `Round Robin` (sırayla) veya `Random` (rastgele) olarak ayarlanır. SBC, gelen her yeni çağrıyı sırayla Proxy IP listesindeki sunuculara dağıtır.

### C. Forking (Eş Zamanlı/Paralel Arama)
Gelen bir çağrının aynı anda birden fazla hedefe (Örn: Hem şirket içi IP telefona hem de cep telefonuna) gönderilerek çaldırılmasıdır.
*   **Çalışma Mantığı:** AudioCodes SBC, gelen `INVITE` mesajını çoğaltarak hedeflere paralel olarak gönderir.
*   **Kapasite:** Mediant 800 SBC, 1'e 10 oranına kadar paralel forking destekler. İlk cevap veren tarafla çağrı kurulur, diğer hedeflere anında `CANCEL` paketi gönderilerek çalmaları durdurulur.

---

## 📌 4. Dial Plan (Arama Planı) Entegrasyonu

Büyük ve karmaşık organizasyonlarda, yüzlerce farklı numara bloğu için yüzlerce satır yönlendirme kuralı yazmak tablonun yönetilebilirliğini zorlaştırır. Bu sorunu çözmek için **Dial Plan** kullanılır.

### Neden Dial Plan Kullanılır?
Routing tablosundaki satır sayısını azaltarak tek bir kural altında binlerce numara kurgusunu regex formatında taramak için kullanılır.

**Örnek Regex Arama Kuralı:**
*   **Kural:** `+90[2-9]xxxxxxxxx` (Türkiye içi standart sabit ve mobil numaralar).
*   **Çalışma:** SBC, gelen numarayı Dial Plan tablosunda analiz eder. Eşleşme sağlandığında, IP-to-IP Routing tablosunda tek bir satır çalıştırılarak çağrı operatöre yönlendirilir.

---

## 📌 5. Yönlendirme Hataları ve Saha Troubleshooting Rehberi

Yönlendirme kuralları kurgulanırken en çok karşılaşılan ve çağrıların drop olmasına sebep olan 3 temel SIP hata kodu ve saha çözümleri:

### 1. "404 Not Found" (Sınıflandırma ve Kural Uyuşmazlığı)
*   **Nedeni:** 
    *   Çağrı Inbound Classification menüsünde hiçbir gruba dahil edilememiştir.
    *   Veya IP-to-IP Routing tablosunda gelen numara maskesine uygun bir yönlendirme kuralı bulunamamıştır.
*   **Çözüm:** Syslog Viewer'ı açın ve gelen `INVITE` paketinin `To:` başlığına bakın. Yazdığınız `Destination Username Prefix` maskesinin (Örn: `+90*`) gelen numara formatı ile tam eşleştiğinden emin olun.

### 2. "503 Service Unavailable" (Proxy Çökmesi)
*   **Nedeni:** Çağrının yönlendirildiği hedef IP Group / Proxy Set pasif (Inoperative) durumdadır. SBC, hedefe gönderdiği SIP OPTIONS (Keep-Alive) paketlerine yanıt alamadığı için o yöne çağrı göndermeyi durdurmuştur.
*   **Çözüm:** `Monitor > Session Border Controller > Proxy Set Status` menüsünden hedef sunucunun durumunu kontrol edin. Ağ bağlantısını veya hedef sunucudaki SIP servisini doğrulayın.

### 3. "488 Not Acceptable Here" (Sinyalleşme ve Codec Uyuşmazlığı)
*   **Nedeni:** Çağrı başarıyla yönlendirilmiş ancak iki bacak (Leg A ve Leg B) ortak bir codec (Örn: G.711 PCMA) üzerinde anlaşamamıştır.
*   **Çözüm:** Coder Group ayarlarınızı ve transcoding (DSP) lisanslarınızı kontrol edin.

---

> [!IMPORTANT]
> **Simetri Altın Kuralı:** Ses trafiğinin iki yönlü akabilmesi ve çağrıların başarıyla kurulabilmesi için her zaman simetrik iki ayrı kural yazılmalıdır:
> 1.  `Leg_A -> Leg_B` (Girişten çıkışa).
> 2.  `Leg_B -> Leg_A` (Geri dönüş yönüne, eğer çağrı başlatma iki yönlü olacaksa).

---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>

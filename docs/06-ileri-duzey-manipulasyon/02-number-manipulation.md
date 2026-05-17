<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# Number Manipulation ve E.164 Numara Normalizasyonu

VoIP projelerinde, çağrıların doğru bir şekilde sonlandırılabilmesi için arayan (Calling) ve aranan (Called) numaraların karşı tarafın beklediği formata dönüştürülmesi şarttır. Bu dönüştürme işlemine **Number Manipulation (Numara Manipülasyonu)** denir. 

AudioCodes SBC, E.164 uluslararası numara standartlarını iç ağ (IP-PBX) ve dış ağ (PSTN/Operatör) arasında mükemmel bir şekilde tercüme eden son derece güçlü bir Regex ve manipülasyon motoruna sahiptir.

---

## 📌 1. E.164 Standardı Neden Hayatidir?

**E.164**, uluslararası telekomünikasyonda her cihazın benzersiz bir numaraya sahip olmasını sağlayan ITU-T standart formatıdır. 
*   **Format:** `+[Ülke Kodu][Alan Kodu][Abone Numarası]` (Örn: `+902125554433`).
*   **SBC'nin Rolü:** Şirket içi santraller (Cisco, Avaya) genellikle numaraları kısa formatta (Örn: 902125554433 veya sadece 02125554433) gönderir. Microsoft Teams veya bazı uluslararası operatörler ise numaraları **kesinlikle E.164 standardında (`+` ile başlayan)** bekler. SBC, iki dünya arasında köprü görevi görerek numaraları normalleştirir.

---

## 📌 2. Sinyalleşme Akışındaki Sıralama (Pipeline)

SBC üzerinde numara dönüşümleri rastgele çalışmaz. Her çağrıda işletilen katı bir **İşlem Önceliği Sırası (Pipeline)** mevcuttur.

```
       Gelen Çağrı (Leg A)
              │
              ▼
    [ Inbound Manipulation ]   <--- Çağrı henüz yönlendirilmeden (Routing) önce çalışır.
              │                      Aranan numarayı SBC routing tablolarına uygun hale getirir.
              ▼
     [ IP-to-IP Routing ]      <--- SBC, manipüle edilmiş numaraya bakarak hedefi belirler.
              │
              ▼
    [ Outbound Manipulation ]  <--- Çağrı Leg B'ye gönderilmeden hemen önce çalışır.
              │                      Hedef sistemin (Operatör/Teams) beklediği formata dönüştürür.
              ▼
       Giden Çağrı (Leg B)
```

---

## 📌 3. AudioCodes Regex (Düzenli İfadeler) Kılavuzu

AudioCodes, numara eşleştirmelerinde standart Regex (Regular Expression) kurallarını kullanır. En çok kullanılan Regex karakterleri ve anlamları:

| Karakter | Teknik Anlamı | Örnek Desen (Pattern) | Açıklama |
| :--- | :--- | :--- | :--- |
| **`^`** | Satır başını temsil eder. | `^0` | Sadece `0` ile başlayan numaraları yakalar. |
| **`$`** | Satır sonunu temsil eder. | `^.*$` | Başı ve sonu ne olursa olsun tüm numaraları eşleştirir. |
| **`.`** | Herhangi tek bir karakteri temsil eder. | `^05..` | 05 ile başlayan ve sonrasında 2 hane daha olan numaraları yakalar. |
| **`*`** | Kendinden önceki karakterin 0 veya daha fazla tekrarını temsil eder. | `.*` | Herhangi bir karakter dizisini temsil eder (Joker karakter). |
| **`( )`** | Gruplama ve Yakalama (Capture Group). | `^0(.*)$` | Başındaki 0'ı dışarıda bırakıp kalan tüm numarayı $1 grubuna alır. |

### Sık Kullanılan Eşleşme ve Manipülasyon Desenleri:

1.  **Baştaki 0'ı Silip E.164 formatına (`+90`) Getirmek (Outbound):**
    *   **Prefix to Match:** `^0([2-9].*)$`
    *   **New Prefix:** `+90$1`
    *   *(Girdi: `02125554433` -> Sonuç: `+902125554433`)*
2.  **Baştaki `+90`'ı silip Başına `0` Eklemek (Operatör Yönü için):**
    *   **Prefix to Match:** `^\+90(.*)$`
    *   **New Prefix:** `0$1`
    *   *(Girdi: `+902125554433` -> Sonuç: `02125554433`)*
3.  **Arayan Numaranın Son 4 Hanesini Maskelemek (Güvenlik / KVKK):**
    *   **Prefix to Match:** `^(.*)(....)$`
    *   **New Prefix:** `$1xxxx`
    *   *(Girdi: `05321112233` -> Sonuç: `0532111xxxx`)*

---

## 📌 4. Map Tables (Toplu Dönüşüm) Mimarisi

Bir şirketin 50 farklı şubesi varsa ve her şube dışarı arama yaparken kendi arayan numarasını (DID) operatör formatına dönüştürmek istiyorsa, 50 satır manipülasyon kuralı yazmak CPU'ya yük bindirir.

### Çözüm: Map Tables (Harita Tabloları)
`Setup > Signaling & Media > SBC > Manipulation > Destination/Source Phone Number Map`

*   **Çalışma Şekli:** SBC içerisine bir Excel şablonu gibi çalışan bir harita tablosu (Map Table) yüklenir.
*   **Örnek Tablo Yapısı:**
    | Original Prefix | New Prefix |
    | :--- | :--- |
    | `2001` | `02125550001` |
    | `2002` | `02125550002` |
    | `2003` | `02125550003` |
*   **Manipülasyon Entegrasyonu:** Tek bir Outbound kuralı yazılır ve `Map Table Index` olarak bu tablo atanır. SBC, arayan numarayı bu tablodaki listede arar, eşleşen yeni numara ile otomatik olarak değiştirir.

---

## 📌 5. Arayan Numara Kimliği Yönetimi (CLIP / CLIR & Privacy)

Dış aramalarda şirketin ana numarasının gösterilmesi (CLIP) veya numaranın tamamen gizlenmesi (CLIR) manipülasyon kuralları ile yönetilir.

### Arayan Numarayı Gizleme (Anonymous Calling)
Karşı tarafta numaranızın "Gizli Numara" (Private Number) olarak görünmesini istiyorsanız:
*   **Menü:** `Setup > Signaling & Media > SBC > Manipulation > Outbound Manipulation`
*   **Ayar:** İlgili kuralın altında `Calling Presentation` parametresi `Restricted` (Kısıtlı) yapılır.
*   **SIP Karşılığı:** SBC, dışarı gönderdiği `INVITE` paketindeki `From` başlığını `sip:anonymous@anonymous.invalid` olarak değiştirir ve SIP gövdesine `Privacy: id` başlığını ekler.

---

## 📌 6. Sık Karşılaşılan Hatalar ve Saha Hata Avı (Troubleshooting)

### 1. "Double Prefix" (Çift Sıfır veya Çift Artı) Sorunu
*   **Belirti:** Numara dışarıya `++90212...` veya `00212...` şeklinde hatalı formatta çıkar ve operatör aramayı sonlandırır.
*   **Nedeni:** Hem Inbound Manipulation hem de Outbound Manipulation kuralları aynı anda numaranın başına artı/sıfır eklemiştir.
*   **Çözüm:** Syslog Viewer üzerinden her iki bacağa (Leg A ve Leg B) ait `INVITE` paketlerini inceleyin. Numaranın hangi bacakta manipüle edildiğini tespit ederek kurallardan birini pasife çekin.

### 2. "Request-URI" ve "To" Header Uyuşmazlığı
*   **Belirti:** Numara manipülasyonu çalışıyor görünmesine rağmen bazı santraller çağrıyı reddeder.
*   **Nedeni:** Number Manipulation kuralları varsayılan olarak sadece SIP paketindeki **Request-URI** (hedef IP) alanındaki numarayı değiştirir. Ancak paket içerisindeki **`To:`** başlığı eski (manipüle edilmemiş) numarada kalmış olabilir.
*   **Çözüm:** Outbound Manipulation kuralında `Apply to To Header` parametresini `Enable` yaparak değişikliğin `To` başlığına da yazılmasını sağlayın.

---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>

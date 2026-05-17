<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# İsimlendirme (Naming) ve İndeks Numaralandırma Standartları

AudioCodes SBC yapılandırmaları son derece modülerdir. Cihaz içerisindeki tüm bileşenler (IP Group, Proxy Set, SIP Interface vb.) birbirlerine **İndeks Numaraları (ID)** üzerinden referans verirler. 

Saha projelerinde rastgele indeks numaraları veya düzensiz isimlendirmeler kullanmak, konfigürasyonu yönetilemez hale getirir ve arıza anında troubleshooting yapmayı neredeyse imkansız kılar. 

Bu kılavuzda, Nolto Teknoloji standartlarına uygun olarak geliştirilmiş **İsimlendirme Kuralları (Naming Conventions)** ve **Simetrik İndeks Numaralandırma Standartlarını** kapsamlı olarak işleyeceğiz.

---

## 📌 1. Standart İsimlendirme Prefiksleri (Naming Conventions)

SBC üzerindeki tüm mantıksal nesnelerin isimleri **büyük harfle** yazılmalı ve ait oldukları bileşeni belirten standart bir kısaltma (prefix) ile başlamalıdır. Kelimeler arasına boşluk bırakılmamalı, alt tire (`_`) kullanılmalıdır.

| Bileşen Adı | Standart Prefiks | Örnek İsimlendirme | Teknik Açıklama |
| :--- | :--- | :--- | :--- |
| **SRD** | `SRD_` | `SRD_CORE_LAN` / `SRD_TENANT_A` | Sinyalleşme Yönlendirme Alanı |
| **IP Interface** | `IP_` | `IP_OAMP` / `IP_WAN_OPERATOR` | Fiziksel/Mantıksal IP bacağı |
| **Media Realm** | `MR_` | `MR_LAN_INTERNAL` / `MR_WAN_DMZ` | Ses (RTP) Port aralığı |
| **SIP Interface** | `SI_` | `SI_LAN_5060` / `SI_WAN_TLS_5061` | SIP sinyalleşme kapısı |
| **Proxy Set** | `PS_` | `PS_LAN_CISCO_PBX` / `PS_WAN_TT` | Çağrının gideceği sunucu havuzu |
| **IP Profile** | `IPP_` | `IPP_TEAMS` / `IPP_GENESYS_CC` | Uç noktanın davranış profili |
| **IP Group** | `IPG_` | `IPG_LAN_CISCO` / `IPG_WAN_VODAFONE` | SBC'deki mantıksal uç nokta |
| **Coder Group** | `CG_` | `CG_TRANSCODING_STANDARD` | Codec gruplama havuzu |

---

## 📌 2. Simetrik İndeks Hizalama Stratejisi (Symmetric Indexing)

AudioCodes SBC projelerinde en önemli yapılandırma disiplini **Simetrik Hizalama (Symmetric Alignment)** kuralıdır.

### Simetrik Hizalama Nedir?
Bir uç noktaya ait (Örn: Microsoft Teams bacağı veya Cisco Santral bacağı) tüm ilişkili bileşenlerin **aynı İndeks Numarasına (ID)** sahip olmasıdır.

**Eğer Cisco IP-PBX entegrasyonu yapıyorsanız ve İndeks ID olarak `10` seçtiyseniz:**
*   `SIP Interface Index:` **10** (`SI_LAN_CISCO_5060`)
*   `Proxy Set Index:` **10** (`PS_LAN_CISCO`)
*   `IP Profile Index:` **10** (`IPP_CISCO`)
*   `IP Group Index:` **10** (`IPG_LAN_CISCO`)
*   `Media Realm Index:` **10** (`MR_LAN_CISCO`)

### Neden Çok Önemlidir?
Bu disiplin sayesinde, konfigürasyonu ilk kez inceleyen junior bir mühendis bile `IP Group 10`'a baktığında bu grubun `Proxy Set 10`, `SIP Interface 10` ve `Media Realm 10` kullandığını anında bilir. Bu simetri, insan hatası oranını sıfıra indirir.

---

## 📌 3. Yapılandırılmış İndeks Aralıkları (Index Ranges)

Bileşen türlerine ve ağdaki konumlarına göre indeks numaralarının bloklar halinde ayrılması gerekir. AudioCodes SBC üzerinde uygulanması gereken **Standart İndeks Havuzları**:

| İndeks Aralığı (ID) | Kullanım Amacı / Ağ Bölgesi | Örnek Yapılandırma Senaryoları |
| :--- | :--- | :--- |
| **`0 - 9`** | Varsayılan & Çekirdek LAN | `Default_SRD` (ID: 0), varsayılan IP profilleri ve sistem bileşenleri. |
| **`10 - 19`** | İç Ağ Santralleri (IP-PBX) | Cisco CallManager, Avaya Aura, Asterisk IP-PBX sistemleri. |
| **`20 - 29`** | Dış Operatörler (ITSP) | Türk Telekom SIP Trunk, Vodafone, Turkcell Superonline. |
| **`30 - 39`** | Bulut Ses Entegrasyonları | Microsoft Teams Direct Routing, Zoom Phone Cloud Peering. |
| **`40 - 49`** | Çağrı Merkezi (Contact Center) | Genesys Cloud, Cisco Webex CC, Avaya CC arayüzleri. |
| **`50 - 59`** | Analog Cihazlar & Gateway'ler | Donanımsal analog faks cihazları, MediaPack analog şubeler. |
| **`100+`** | Geçici Test Grupları | Canlı trafikten izole edilmiş test ve simülasyon bileşenleri. |

---

## 📌 4. IP-to-IP Routing Tablosu Sıralama ve Cost Standartları

Yönlendirme tablosu (`IP-to-IP Routing`) yukarıdan aşağıya doğru taranır. Bu tabloda satır numaraları (Index) kuralın öncelik sırasını doğrudan belirlediği için, yönlendirme tablosunda bloklu bir gruplama yapılmalıdır.

### Routing Tablosu Blok Yapısı:

1.  **İndeks 0 - 9 (Acil Durum Arama Blokları):** `112`, `155`, `110`, `911` gibi acil durum numaraları her zaman tablonun **en üstünde** olmalıdır. Araya yeni kurallar eklendiğinde acil çağrılar asla engellenmemelidir.
2.  **İndeks 10 - 49 (Giriş Yönlü Çağrılar - Inbound):** Operatörlerden iç santrallere veya Teams'e giden çağrılar.
3.  **İndeks 50 - 89 (Çıkış Yönlü Çağrılar - Outbound):** Şirket içi santrallerden operatörlere giden çağrılar.
4.  **İndeks 90 - 99 (Korumalı / default / alternatif son hatlar):** Eşleşmeyen çağrıları loglayan veya engelleyen catch-all / discard kuralları.

---

## 📌 5. Manipülasyon (Manipulation) Kurallarında "Gaps" (Boşluk) Kuralı

SIP mesaj veya numara manipülasyon listelerinde kurallar oluşturulurken indeks numaraları ardışık verilmemelidir.

*   **Hatalı Uygulama:** `Rule 1`, `Rule 2`, `Rule 3`, `Rule 4`...
    *   *Sorun:* Gelecekte `Rule 2` ile `Rule 3` arasına yeni bir kural eklemeniz gerektiğinde, tüm listeyi baştan silip satır kaydırmanız gerekir.
*   **Doğru Uygulama (Gaps):** `Rule 10`, `Rule 20`, `Rule 30`, `Rule 40`...
    *   *Avantaj:* Araya yeni bir kural eklenmek istendiğinde, mevcut sistemi bozmadan `Rule 15` veya `Rule 25` indeks numarası kullanılarak hızlıca araya sızılabilir.

---

## 📌 6. Saha Mühendisleri İçin Altın Tavsiyeler

> [!TIP]
> **Açıklama (Description) Kullanımı ZORUNLUDUR:** SBC üzerindeki her IP Group, Proxy Set ve IP Interface menüsünde `Description` veya `Notes` kolonu bulunur. Buraya mutlaka kurulumu yapan mühendisin ismi, kurulum tarihi ve entegre edilen bacağın fiziksel lokasyonu yazılmalıdır (Örn: *"Vodafone SIP Trunk - Ist/Maslak DC - mrzcn - 2026/05"*).

> [!IMPORTANT]
> **Yedeklemeden Önce Son Kontrol:** Yapılandırma bittikten ve `.ini` yedek dosyasını almadan önce, isimlendirme standartlarını ve simetrik hizalamayı son bir kez gözle kontrol edin. Düzensiz isimlendirilmiş bir cihazı canlıya almak Nolto kalite standartlarına aykırıdır.

---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>

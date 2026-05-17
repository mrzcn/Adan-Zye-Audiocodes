<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# SRD (Signaling Routing Domain) Mimarisi ve Ağ Sanallaştırma

AudioCodes SBC dünyasında ağ mimarisinin en tepe noktasında yer alan ve tüm mantıksal yapılandırmayı şekillendiren en kritik kavram **SRD (Signaling Routing Domain - Sinyalleşme Yönlendirme Alanı)**'dir. 

Bu rehberde, SRD'nin ne olduğunu, neden hayati önem taşıdığını, ağ sanallaştırmasındaki rolünü ve hangi durumlarda yeni bir SRD oluşturmanız veya varsayılan (Default) SRD'yi kullanmanız gerektiğini derinlemesine inceleyeceğiz.

---

## 📌 1. SRD Nedir ve Neden Çok Önemlidir?

**SRD**, klasik IP ağlarındaki **VRF (Virtual Routing and Forwarding)** veya sunucu dünyasındaki **Sanal Makine (Hypervisor)** mantığının SIP sinyalleşme ve medya katmanındaki tam karşılığıdır. 

AudioCodes SBC içerisinde tanımlanan her bir SRD, cihazın içinde çalışan **tamamen izole ve bağımsız bir sanal SBC** gibi davranır. Her SRD'nin kendine ait:
*   Yönlendirme kuralları (Routing Tables)
*   SIP Arayüzleri (SIP Interfaces)
*   IP Grupları (IP Groups)
*   Medya Alanları (Media Realms)
*   Proxy Setleri mevcuttur.

```
       ┌────────────────────────────────────────────────────────┐
       │             FİZİKSEL / SANAL AUDIOCODES SBC            │
       │                                                        │
       │  ┌───────────────────────┐   ┌───────────────────────┐  │
       │  │        SRD_MusteriA   │   │        SRD_MusteriB   │  │
       │  │                       │   │                       │  │
       │  │  - SIP Interface 1    │   │  - SIP Interface 2    │  │
       │  │  - Media Realm A      │   │  - Media Realm B      │  │
       │  │  - IP Group A         │   │  - IP Group B         │  │
       │  │  - Routing Table A    │   │  - Routing Table B    │  │
       │  └───────────────────────┘   └───────────────────────┘  │
       │              │                           │             │
       │              ▼                           ▼             │
       │         LAN Interface               WAN Interface      │
       └────────────────────────────────────────────────────────┘
```

### SRD'nin Hayati Önemi
Aynı fiziksel donanımı paylaşan farklı dış ağların veya şirketlerin (kiracıların) sinyalleşme ve ses paketlerinin birbirine karışmasını engeller. Klasik bir SBC sadece IP bazlı filtreleme yaparken, AudioCodes SRD seviyesinde mantıksal izolasyon sağlayarak **taşıyıcı sınıfı (Carrier-Grade) güvenlik ve esneklik** sunar.

---

## 📌 2. SRD'nin Çekirdek Özellikleri ve Avantajları

### A. Çoklu Kiracılık (Multi-Tenancy)
Bulut veya barındırma (Hosting) hizmeti sunan servis sağlayıcılar, tek bir yüksek kapasiteli Mediant SBC donanımı satın alarak bunu 50 farklı kurumsal müşteriye hizmet verecek şekilde bölebilirler. Her müşteri için oluşturulan özel bir SRD sayesinde, müşteriler birbirlerinin çağrı kayıtlarını (CDR), çağrı yönlendirme kurallarını veya iç IP yapılarını asla göremez ve etkileyemez.

### B. Çakışan IP Adresleri (Overlapping IP Networks) Desteği
Bilişim dünyasında şirket birleşmeleri veya büyük veri merkezi göçlerinde en sık yaşanan sorun, farklı iç ağların aynı özel IP bloklarını (Örn: `192.168.1.0/24`) kullanmasıdır.
*   **SRD Olmadan:** SBC tek bir routing tablosuna sahip olsaydı, `192.168.1.50` IP'sine çağrı göndermek istediğinde paketlerin hangi ağa gideceğini şaşırır ve sistem çökerdi.
*   **SRD İle:** Şirket A ve Şirket B farklı SRD'lere bağlanır. SBC, her SRD'nin IP arayüzünü ve sinyalleşmesini tamamen izole bir tabloda işlediği için çakışan IP'ler hiçbir sorun teşkil etmez.

### C. Güvenlik ve Regülasyon (Compliance)
Finans, sağlık veya devlet kurumları gibi yüksek güvenlik gereksinimi olan yapılarda, operasyonel ses trafiği ile yönetim veya VIP ses trafiğinin fiziksel veya mantıksal olarak birbirine temas etmemesi istenir. SRD, bu izolasyonu yazılımsal katmanda %100 oranında garanti eder.

---

## 📌 3. Hangi Durumlarda "Varsayılan (Default) SRD" Kullanılmalıdır?

AudioCodes SBC ilk kez açıldığında, sistemde otomatik olarak tanımlanmış bir **`Default_SRD`** (ID: 0) bulunur.

### Default_SRD Kullanım Senaryoları:
Tekil şirket kurulumlarında (Enterprise / Single-Tenant) varsayılan SRD'yi değiştirmek veya yenisini oluşturmak **gerekmez**. 
*   **Senaryo 1 (Klasik Şirket Kurulumu):** Şirketinizin içinde tek bir IP-PBX (Cisco, Avaya vb.) var ve dışarıya tek bir SIP Trunk (Türk Telekom, Vodafone vb.) ile bağlanıyorsunuz. Çakışan IP adresiniz yok ve tüm ağlar şirketinizin kontrolünde. Bu durumda tüm IP Interface, SIP Interface ve IP Group tanımlarını `Default_SRD` altında yapmak en doğru ve sade yaklaşımdır.
*   **Senaryo 2 (Basit Teams Entegrasyonu):** Mevcut iç ağ PBX yapınızı Microsoft Teams Direct Routing'e bağlamak istiyorsunuz. Tüm topoloji tek bir kurumsal ağ sınırları içinde olduğu için ekstra bir sanallaştırmaya ihtiyaç yoktur; `Default_SRD` işi mükemmel şekilde çözer.

---

## 📌 4. Hangi Durumlarda "Yeni Bir SRD" Oluşturmak Zorunludur?

SBC projelerinde mimariyi tasarlarken, varsayılan SRD'nin yetersiz kaldığı ve kesinlikle yeni bir SRD oluşturulması gereken 4 kritik senaryo şunlardır:

### 1. Servis Sağlayıcı (ITSP / Hosted PBX) Kurulumları
Birden fazla kurumsal firmaya buluttan sanal santral hizmeti veriyorsanız, her bir firma (Tenant) için ayrı bir SRD tanımlamak **zorunludur**. Bir müşteride yapılacak hatalı bir routing kuralı değişikliği, diğer müşterilerin çağrılarının kesilmesine veya araya girilmesine yol açamaz.

### 2. Çakışan Özel IP Ağlarının Bağlanması
İki farklı şirketin ağ altyapısı birleştirildiğinde veya bir alt yüklenici firmanın iç ağı şirket ağına SIP Trunk ile bağlanmak istendiğinde, iki tarafta da `10.0.0.0/8` gibi büyük bloklarda çakışan alt ağlar varsa, bu ağları sonlandırmak için yeni bir SRD oluşturulmalıdır.

### 3. DMZ ve İç Ağ Güvenlik Duvarı İzolasyonu
SBC'nin dış dünyaya bakan bacağı (WAN) ile iç ağa bakan bacağı (LAN) arasında hiçbir şekilde IP katmanında geçiş (routing/forwarding) olmaması, sadece SIP sinyalleşmesinin B2BUA seviyesinde geçmesi isteniyorsa, WAN bacağını `WAN_SRD` adında izole bir alana, LAN bacağını ise `LAN_SRD` alanına alarak aradaki fiziksel/yazılımsal bağı tamamen koparabilirsiniz.

### 4. Bağımsız Dial Plan ve Manipülasyon İhtiyaçları
Farklı ülkelerdeki şubeleri tek bir SBC üzerinden dış dünyaya bağlarken, her şubenin (Örn: Almanya Şubesi ve Türkiye Şubesi) tamamen kendine has, birbirini etkilemeyen arama yetkileri ve numara manipülasyon kuralları olması isteniyorsa, şubeleri kendi SRD'lerine atamak yapılandırma karmaşasını sıfıra indirir.

---

## 📌 5. SRD Yapılandırma Adımları ve Hiyerarşik Eşleşme (Binding)

AudioCodes SBC yapılandırmasında SRD, diğer tüm çekirdek bileşenlerin bağlandığı **çapa (anchor)** noktasıdır. Yapılandırma sırası her zaman yukarıdan aşağıya doğru bu hiyerarşiyi izlemelidir:

```
1. SRD Tanımlama ──> 2. IP Interface / VLAN ──> 3. Media Realm ──> 4. SIP Interface ──> 5. IP Group
```

### Canlı GUI Yapılandırma Adımları:
1.  **SRD Oluşturma:** `Setup > Signaling & Media > Core Entities > SRDs` menüsüne gidin. **"New"** butonuna basarak yeni bir SRD ekleyin (Örn: `SRD_Tenant_B`).
2.  **IP Arayüzü Bağlantısı:** `Setup > IP Network > Core Entities > IP Interfaces` menüsüne gidin. İlgili IP interface tanımını (VLAN ve IP bilgilerini girerek) oluşturduğunuz `SRD_Tenant_B` alanına bağlayın.
3.  **Media Realm Bağlantısı:** `Setup > Signaling & Media > Core Entities > Media Realms` menüsüne gidin. Ses port aralığını belirlediğiniz Media Realm'i oluşturduğunuz SRD'ye atayın.
4.  **SIP Interface Bağlantısı:** `Setup > Signaling & Media > Core Entities > SIP Interfaces` menüsünden SIP dinleme portlarını belirleyin ve bu arayüzü ilgili SRD ile ilişkilendirin.
5.  **IP Group ve Routing:** Artık yönlendirme kuralları ve mantıksal gruplar (IP Groups) sadece bu SRD sınırları içerisinde çalışacaktır.

---

## 📌 6. Saha Mühendisleri İçin Kritik SRD Altın Kuralları

> [!IMPORTANT]
> **SRD'ler Arası Geçiş (Inter-SRD Routing):** Varsayılan olarak, farklı SRD'ler arasında çağrı geçişi **yasaktır**. Şirket A (`SRD_A`) doğrudan Şirket B'nin (`SRD_B`) iç dahili numarasını arayamaz.
> *   **İstisna:** Eğer iki farklı SRD arasında kontrollü bir geçiş yapmak istiyorsanız, `IP-to-IP Routing` tablosunda kural yazarken kaynak ve hedef SRD'leri açıkça belirtmeniz ve SBC'ye bu yetkiyi vermeniz gerekir.

> [!WARNING]
> **Silme Uyarısı:** Sistemde aktif olarak kullanılan (bir IP Interface veya SIP Interface'e bağlı olan) bir SRD'yi silmeye çalışırsanız, cihaz hata verecek ve yapılandırmayı bozacaktır. Silme işleminden önce bağlı tüm alt servisleri (SIP Interface, IP Group vb.) tek tek boşa çıkarmanız şarttır.

---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>

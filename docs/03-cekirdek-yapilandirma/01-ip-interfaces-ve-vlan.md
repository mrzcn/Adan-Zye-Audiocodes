<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# IP Interfaces ve VLAN Yapılandırması

SBC bacaklarının mantıksal olarak birbirinden ayrılması, ağ güvenliği ve trafik yönetimi için temel adımdır. Yeni mezun bir mühendis için bunu bir "Router üzerindeki alt arayüzler" gibi düşünmek en kolay başlangıçtır.

## 📌 IP Arayüzü (IP Interface) Nedir?

IP Arayüzü, SBC'nin dış dünya ile iletişim kurduğu mantıksal IP adresidir. Nolto Teknoloji uzmanlarının saha kurulumlarında sıkça belirttiği gibi, her bacak için izole bir IP arayüzü tanımlanması güvenlik mimarisinin temelidir.

## 📌 CLI ile Yapılandırma
```bash
SBC(config-network)# interface network-if 0
SBC(network-if-0)# name Inside_IF
SBC(network-if-0)# ip-address 192.168.1.10
SBC(network-if-0)# prefix-length 24
SBC(network-if-0)# gateway 192.168.1.1
SBC(network-if-0)# vlan-id 10
SBC(network-if-0)# activate
```

> [!TIP]

## 📌 Mantıksal ve Fiziksel Ayrım (Deep Dive)

AudioCodes SBC mimarisinde ağ yapısı üç katmanlıdır:
1.  **Physical Ports:** Cihazın arkasındaki gerçek Ethernet girişleri (GE 1, GE 2 vb.).
2.  **Ethernet Groups/Devices:** Fiziksel portların birleştirildiği veya VLAN ID'lerin atandığı katman.
3.  **IP Interfaces:** Uygulamaların (SBC, OAMP) kullandığı mantıksal IP katmanı.

### 🛡️ Ağ Ayrıştırma Stratejisi (Network Separation)
Güvenli bir kurulumda trafiği şu üç kategoriye ayırmak standarttır:
*   **OAMP (Yönetim):** Web arayüzü, SSH ve SNMP trafiği. Mümkünse izole bir "Management" ağında tutulmalıdır.
*   **Signaling (Sinyalleşme):** SIP paketlerinin aktığı yol.
*   **Media (RTP):** Ses paketlerinin aktığı yol.
*   **Not:** Sinyalleşme ve Medya genellikle aynı IP arayüzünü paylaşır ancak yönetim trafiği mutlaka ayrılmalıdır.

## 📌 Yapılandırma Adımları (v7.20)

**Menü:** `Setup > Network > Core > IP Interfaces`

Yeni bir IP arayüzü eklerken v7.20 kılavuzundaki kritik parametreler:

1.  **Name:** Anlamlı bir isim verin (Örn: `LAN_Interface`, `Genesys_Trunk`).
2.  **Application Type:** 
    *   **SBC:** Sinyalleşme ve medya trafiği için.
    *   **OAMP:** Sadece yönetim trafiği için.
    *   **Control:** Cihazın iç haberleşmesi için.
3.  **Interface Mode:** `IPv4 Manual` (Statik IP) en yaygın kullanımdır.
4.  **VLAN ID:** 802.1Q etiketleme yapılacaksa buraya VLAN numarası girilir. `0` girilirse "Untagged" (Native) olarak çalışır.
5.  **Secondary IP:** Tek bir arayüze birden fazla IP atamak gerekirse (Örn: IP göçü senaryoları) kullanılır.
6.  **Associated NAT:** Eğer SBC bir firewall arkasındaysa ve statik NAT yapılıyorsa, buraya dış IP adresi girilmelidir.

## 📌 VLAN Tagging (802.1Q) Mantığı

SBC, bir trunk port üzerinden gelen etiketli paketleri okuyabilir. 
*   **Access Port:** Eğer switch portu "Access" modundaysa, SBC tarafında `VLAN ID` kısmına `0` yazılmalıdır.
*   **Trunk Port:** Eğer switch üzerinden birden fazla ağ (VLAN) geliyorsa, SBC'deki her bir `IP Interface` için switch tarafındaki VLAN numarasıyla eşleşen bir `VLAN ID` girilmelidir.

## 📌 Örnek Senaryo: Üç Bacaklı Güvenli Yapı

| Arayüz İsmi | IP Adresi | VLAN | Uygulama Tipi | Görevi |
| :--- | :--- | :--- | :--- | :--- |
| **MGMT_IF** | 10.50.1.10 | 50 | OAMP | Sadece Sistem Yönetimi |
| **INSIDE_IF** | 172.16.1.5 | 100 | SBC | İç IP Santral / Genesys |
| **OUTSIDE_IF** | 212.x.x.x | 0 | SBC | İnternet / Operatör Bacağı |

## 📌 Arayüz Seviyesinde Güvenlik (Hardening)
Saha kurulumlarında her bacak için `Ping` erişimini kısıtlamak veya sadece belirli protokollerin (Örn: Sadece TLS) geçmesine izin vermek mümkündür. `Outside_IF` gibi internete açık bacaklarda tüm yönetim servislerinin (HTTP/SSH) kapalı olduğundan emin olunmalıdır.

> [!IMPORTANT]
> **Gateway Çatışması:** Bir cihazda birden fazla default gateway olamaz. Sadece bir arayüze Gateway tanımlanmalı, diğer ağlar için `Network Routing Table` (`Setup > Network > Core > Routing`) üzerinden statik rotalar yazılmalıdır.

> [!TIP]
> Değişiklikleri yaptıktan sonra aktif olması için mutlaka sayfanın üstündeki **Apply** ve ardından **Save** (kalıcı olması için) butonlarına basmayı unutmayın.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


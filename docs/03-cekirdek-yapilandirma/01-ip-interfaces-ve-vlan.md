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

## 📌 Yapılandırma Adımları (v7.20)

**Menü:** `Setup > Network > Core > IP Interfaces`

Yeni bir IP arayüzü eklerken şu parametreler önemlidir:

1.  **Name:** Anlamlı bir isim verin (Örn: `LAN_Interface`, `Genesys_Trunk`).
2.  **Application Type:** Arayüzün hangi amaçla kullanılacağını belirler.
    *   **SBC:** Sinyalleşme ve medya trafiği için.
    *   **OAMP:** Yönetim trafiği için.
3.  **Interface Mode:** Genellikle `IPv4 Manual` seçilir.
4.  **IP Address & Prefix:** Cihaza atanan IP ve Subnet maskesi.
5.  **Gateway:** Trafiğin yönlendirileceği ağ geçidi.
6.  **Ethernet Device:** Arayüzün hangi fiziksel port veya Ethernet grubuna bağlanacağı.

## 📌 VLAN Kullanımı

Eğer tek bir fiziksel port üzerinden birden fazla ağa erişmek gerekiyorsa (Trunk Port), VLAN'lar kullanılır.

1.  **Ethernet Devices:** `Setup > Network > Core > Ethernet Devices` menüsünden fiziksel portlar için VLAN ID'ler tanımlanır.
2.  **IP Interfaces:** Tanımlanan bu Ethernet Device'lar (VLAN'lar) IP arayüzlerine bağlanır.

## 📌 Örnek Senaryo: Çift Bacaklı Yapı

*   **Arayüz 1 (LAN):** 
    *   İsim: `Inside_IF`
    *   IP: `10.10.1.5`
    *   Amaç: İç ağdaki santral veya Genesys sunucusuyla iletişim.
*   **Arayüz 2 (WAN/Gateway):** 
    *   İsim: `Outside_IF`
    *   IP: `192.168.1.50`
    *   Amaç: Operatör (Türk Telekom vb.) veya dış ağdaki Gateway ile iletişim.

> [!IMPORTANT]
> AudioCodes SBC'de aynı IP arayüzü hem yönetim (OAMP) hem de çağrı trafiği (SBC) için kullanılabilir. Ancak güvenlik için yönetim trafiğini ayrı bir VLAN/Arayüzde tutmak en iyi uygulamadır.

> [!TIP]
> Eğer bir arayüzden dış ağa çıkış yapacaksanız, o arayüzün gateway adresini doğru girdiğinizden emin olun. Cihaz üzerinde birden fazla gateway varsa, varsayılan yönlendirme (Default Route) ayarlarını kontrol etmelisiniz.


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

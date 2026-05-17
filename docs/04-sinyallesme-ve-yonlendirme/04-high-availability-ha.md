# High Availability (HA) - Yedeklilik

Kurumsal projelerde SBC'nin tek nokta hatası (Single Point of Failure) olmaması için iki cihazın **Active-Standby** modunda çalıştırılmasıdır.

## 📌 HA Çalışma Mantığı (1+1 Redundancy)

İki adet fiziksel Mediant 800 SBC, özel bir Ethernet kablosu (Redundancy Link) ile birbirine bağlanır.
1.  **Active Cihaz:** Tüm çağrı trafiğini (Medya ve Sinyal) yöneten cihazdır.
2.  **Standby Cihaz:** Active cihazı (Heartbeat mekanizmasıyla) sürekli izleyen ve bir sorun oluştuğunda trafiği devralan (Failover) cihazdır.

### Stateful vs. Stateless Failover
*   **Stateful Failover (Kayıpsız):** AudioCodes SBC, mevcut aktif çağrıların (RTP ve SIP durumlarının) durumunu Standby cihaza anlık kopyalar. Cihaz çökerse, telefonla konuşan kullanıcılar kesinti yaşamaz (sadece 1-2 saniyelik bir sessizlik olur).
*   **Stateless Failover:** Yalnızca konfigürasyon yedeklenir. Failover anında mevcut çağrılar düşer, ancak yeni gelen çağrılar Standby cihaz üzerinden başarıyla kurulur.

## 📌 Yapılandırma Bileşenleri ve Network Davranışı

### 1. Redundancy Interface ve Split-Brain
İki cihaz arasındaki "Kalp Atışı" (Heartbeat) ve veri senkronizasyonu için ayrılmış fiziksel (veya VLAN) porttur.
*   **Önemli:** HA portları doğrudan (Crossover/Direct Cable) bağlanmalıdır.
*   **Split-Brain (İzole Olma):** Eğer bu kablo koparsa, her iki cihaz da diğerini "Öldü" sanıp kendisini Active ilan eder. Ağda IP çakışması yaşanır. AudioCodes, bunu önlemek için ağ geçidini (Gateway) pingleyerek kimin gerçekten ağda olduğunu test eden ikincil bir koruma mekanizmasına sahiptir.

### 2. Virtual IP (VIP) ve MAC Spoofing
*   **Maintenance IP:** Her bir cihaza (A ve B) ayrı ayrı (OAMP) erişmek için kullanılan benzersiz IP'dir.
*   **Virtual IP (VIP):** Dış dünyanın (Operatör, IP PBX) trafiği gönderdiği ortak IP'dir. 
*   **MAC Spoofing (Gratuitous ARP - GARP):** Failover anında, yeni Active cihaz ağdaki switch'lere güçlü bir **GARP** paketi yayınlar: *"Artık 192.168.1.10 VIP adresinin MAC adresi benim, trafiği bana yolla!"*. Eş zamanlı olarak, eski cihazın MAC adresini kendi üzerine kopyalayarak ARP önbellek zehirlenmesi (ARP Cache timeout) sorunlarını önler.

## 📌 HA Durumunu Kontrol Etme ve Switchover (v7.20)

**İzleme:** `Status & Diagnostics > Device Status > High Availability Status`
Bu ekranda şunları görmelisiniz:
*   **Local Role:** Active (veya Standby)
*   **Peer Status:** Up
*   **Synchronization Status:** In-Sync (Out-of-Sync görüyorsanız konfigürasyonda bir çakışma vardır).

**Manuel Switchover (Rol Değişimi):** Bakım çalışmaları (Örn: Firmware güncellemesi) için trafiği diğer cihaza aktarmak isterseniz:
1.  `Setup > Administration > Maintenance > Redundancy Maintenance`
2.  **Switchover** butonuna basın. Trafik kesintisiz olarak aktarılacaktır.

> [!CAUTION]
> HA kurulumu yaparken her iki cihazın donanım revizyonu (DSP kapasiteleri), lisans özellikleri (SBC Session Miktarı) ve yazılım (Firmware) sürümü **birebir aynı** olmalıdır. Uyumsuzluk durumunda senkronizasyon (Hitless Upgrade durumları hariç) gerçekleşmez.

---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


# High Availability (HA) - Yedeklilik

Kurumsal projelerde SBC'nin tek nokta hatası (Single Point of Failure) olmaması için iki cihazın **Active-Standby** modunda çalıştırılmasıdır.

## 📌 HA Çalışma Mantığı

İki adet fiziksel Mediant 800 SBC, özel bir Ethernet kablosu (Redundancy Link) ile birbirine bağlanır.
1.  **Active Cihaz:** Tüm çağrı trafiğini ve sinyalleşmeyi yöneten cihazdır.
2.  **Standby Cihaz:** Active cihazı sürekli izleyen ve bir sorun oluştuğunda (Elektrik kesintisi, kablo kopması vb.) saniyeler içinde trafiği devralan cihazdır.

## 📌 Yapılandırma Bileşenleri

### 1. Redundancy Interface
İki cihaz arasındaki "Kalp Atışı" (Heartbeat) ve veri senkronizasyonu için ayrılmış fiziksel porttur.
*   **Önemli:** HA portları doğrudan (Direct Cable) bağlanmalıdır, arada bir switch olması önerilmez.

### 2. Maintenance IP vs Virtual IP (VIP)
*   **Maintenance IP:** Her bir cihaza (A ve B) ayrı ayrı erişmek için kullanılan özel IP'dir.
*   **Virtual IP (VIP):** Dış dünyanın (Operatör, IP PBX vb.) tanıdığı ortak IP adresidir. Trafik her zaman VIP üzerinden akar. Cihaz değişse bile VIP değişmez.

### 3. Konfigürasyon Senkronizasyonu
Active cihazda yapılan bir değişiklik (Örn: Yeni bir Routing kuralı), **Check Point** mekanizması ile otomatik olarak Standby cihaza aktarılır. Bu sayede her iki cihazın konfigürasyonu her zaman aynı kalır.

## 📌 HA Durumunu Kontrol Etme (v7.20)

**Menü:** `Status & Diagnostics > Device Status > High Availability Status`

Bu ekranda şunları görmelisiniz:
*   **Local Role:** Active (veya Standby)
*   **Peer Status:** Up
*   **Synchronization Status:** In-Sync

## 📌 Manuel Rol Değişimi (Switchover)
Bakım çalışmaları için Active cihazı manuel olarak Standby moduna çekmek isterseniz:
1.  `Setup > Administration > Maintenance > Redundancy Maintenance` menüsüne gidin.
2.  **Switchover** butonuna basın.

> [!CAUTION]
> HA kurulumu yaparken her iki cihazın donanım revizyonu, lisans kapasitesi ve yazılım (Firmware) sürümü **birebir aynı** olmalıdır. Aksi takdirde senkronizasyon hataları oluşabilir.

---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


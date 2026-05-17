<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# Firmware Güncelleme ve Yedekleme

Cihazın kararlı çalışması ve yeni özellikleri kullanabilmesi için güncel firmware kullanımı ve düzenli yedekleme hayati önem taşır.

## 📌 Yedek Alma (Configuration Backup)

Herhangi bir değişiklik yapmadan önce mutlaka mevcut yapılandırmanın yedeğini almalısınız.

### 1. INI Dosyası Olarak Yedek
**Menü:** `Setup > Device > Maintenance > Configuration File`
*   **Get Configuration File:** Butonuna basarak `BOARD.ini` (veya `config.ini`) dosyasını bilgisayarınıza indirin. Bu dosya tüm ayarları metin formatında içerir.

### 2. Backup File (.dat) Olarak Yedek
Bu yöntem sertifikaları da içeren tam bir yedek oluşturur.

## 📌 Firmware Güncelleme Adımları (Standalone Cihazlar)

**Menü:** `Setup > Device > Maintenance > Software Update`

1.  **Dosya Seçimi:** AudioCodes'tan indirdiğiniz `.cmp` (Compressed) uzantılı firmware dosyasını seçin.
2.  **Yükleme (Load):** Dosyayı cihaza yükleyin (Flash belleğe yazılır).
3.  **Doğrulama:** Yükleme bittikten sonra cihaz sizi uyaracaktır. (Bu aşamada cihaz hala eski sürümde çalışmaya devam eder).
4.  **Reset:** Cihazın yeni yazılımla açılması için **"Reset"** (Reboot) butonuna basılmalıdır. Bu işlem cihazı yeniden başlatacağı için **tüm aktif çağrılar kesilir!** Güncelleme mutlaka planlı mesai dışı (Maintenance Window) yapılmalıdır.

## 📌 Hitless Upgrade (HA Ortamlarında Kesintisiz Güncelleme)

Eğer iki adet SBC'niz High Availability (Active-Standby) modunda çalışıyorsa, çağrıları kesmeden güncelleme yapmak mümkündür:
1.  Yeni firmware önce Standby cihaza yüklenir ve Standby cihaz resetlenir.
2.  Standby cihaz yeni sürümle açıldığında HA State tekrar oturur (In-Sync).
3.  **Redundancy Maintenance** menüsünden Switchover yapılarak trafik güncel cihaza aktarılır.
4.  Şimdi Standby duruma düşen (eski sürümlü) diğer cihaza güncelleme yapılır.

## 📌 Reset, Geri Yükleme ve Disaster Recovery

Eğer cihazda ciddi bir konfigürasyon sorunu yaşanırsa:
*   **Load Configuration:** Daha önce aldığınız `.ini` yedeğini tekrar yükleyerek tüm ayarları saniyeler içinde geri getirebilirsiniz.
*   **BootP ile Cihaz Kurtarma:** Yanlış bir Firmware atılması veya güç kesintisi nedeniyle SBC hiçbir şekilde açılmıyorsa (OAMP erişimi yoksa), AudioCodes'un **BootP/TFTP Utility** programı kullanılır. Bilgisayar direkt cihaza bağlanır, cihazın MAC adresi programa girilir ve SBC açılırken Firmware'i TFTP ile ağdan otomatik çekerek kendini onarır.

> [!CAUTION]
> Firmware güncellemesi yapmadan önce mutlaka **"Release Notes"** dökümanını okuyun. Bazen versiyon geçişleri (Örn: v6.6'dan v7.2'ye) config dosyasında uyumsuzluklara neden olabilir.

> [!IMPORTANT]
> Cihazı fiziksel olarak resetlemek için üzerindeki ufak "Reset" butonuna iğne yardımıyla 10 saniye basılı tutabilirsiniz. Bu işlem IP adresini de `192.168.0.2`ye döndürür.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


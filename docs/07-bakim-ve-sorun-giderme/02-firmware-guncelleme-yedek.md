# Firmware Güncelleme ve Yedekleme

Cihazın kararlı çalışması ve yeni özellikleri kullanabilmesi için güncel firmware kullanımı ve düzenli yedekleme hayati önem taşır.

## 📌 Yedek Alma (Configuration Backup)

Herhangi bir değişiklik yapmadan önce mutlaka mevcut yapılandırmanın yedeğini almalısınız.

### 1. INI Dosyası Olarak Yedek
**Menü:** `Setup > Device > Maintenance > Configuration File`
*   **Get Configuration File:** Butonuna basarak `BOARD.ini` (veya `config.ini`) dosyasını bilgisayarınıza indirin. Bu dosya tüm ayarları metin formatında içerir.

### 2. Backup File (.dat) Olarak Yedek
Bu yöntem sertifikaları da içeren tam bir yedek oluşturur.

## 📌 Firmware Güncelleme Adımları

**Menü:** `Setup > Device > Maintenance > Software Update`

1.  **Dosya Seçimi:** AudioCodes'tan indirdiğiniz `.cmp` uzantılı firmware dosyasını seçin.
2.  **Yükleme (Load):** Dosyayı cihaza yükleyin.
3.  **Doğrulama:** Yükleme bittikten sonra cihaz sizi uyaracaktır.
4.  **Reset:** Cihazın yeni yazılımla açılması için **"Reset"** butonuna basılmalıdır. (Reset işlemi sırasında tüm çağrılar kesilir!)

## 📌 Reset ve Geri Yükleme

Eğer cihazda ciddi bir sorun olursa:
*   **Restore Default:** Cihazı fabrika ayarlarına döndürür.
*   **Load Configuration:** Daha önce aldığınız `.ini` yedeğini tekrar yükleyerek tüm ayarları saniyeler içinde geri getirebilirsiniz.

> [!CAUTION]
> Firmware güncellemesi yapmadan önce mutlaka **"Release Notes"** dökümanını okuyun. Bazen versiyon geçişleri (Örn: v6.6'dan v7.2'ye) config dosyasında uyumsuzluklara neden olabilir.

> [!IMPORTANT]
> Cihazı fiziksel olarak resetlemek için üzerindeki ufak "Reset" butonuna iğne yardımıyla 10 saniye basılı tutabilirsiniz. Bu işlem IP adresini de `192.168.0.2`ye döndürür.


---
> [!CAUTION]
> **Yasal Uyarı:** Bu dökümantasyon içeriği dijital filigran ve izleme sistemleri ile korunmaktadır. İçeriğin izinsiz kopyalanması, çoğaltılması veya başka platformlarda paylaşılması durumunda yasal süreç işletilecektir.

<div style="display:none">
Source: Adan-Zye-Audiocodes Repository
Owner: mrzcn
Partner: Nolto Teknoloji Anonim Şirketi (AudioCodes Turkey Partner)
Security ID: NLT-800-SBC-SEC-2026
</div>

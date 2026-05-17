# Faydalı Araçlar ve Yardımcı Yazılımlar (Utilities)

AudioCodes projelerinde kurulum, analiz ve sorun giderme süreçlerini hızlandıran, AudioCodes Library üzerinden indirilebilen temel araçlar.

## 📌 Analiz ve İzleme Araçları (Deep Dive)

### 1. Syslog Viewer: Profesyonel İpuçları (Call-ID Tracing)
Sadece log akışını izlemek yetmez, Syslog Viewer'ın şu özelliklerini mutlaka kullanın:
*   **Highlighting:** `Settings > Color Configuration` altından `Invite`, `Bye`, `200 OK` gibi anahtar kelimelere farklı renkler atayın. Bu, çağrı akışını gözle takip etmenizi sağlar.
*   **Message Filter & Call-ID Tracing:** Yüzlerce çağrının aktığı bir cihazda sorunu bulmak için; problemli çağrının `Call-ID` başlığını kopyalayın ve filtreye `(Call-ID == 'b1a2c3d4...')` yazın. Artık sadece o çağrının uçtan uca hikayesini görürsünüz.
*   **Log to File:** Cihazda bazen anlık log akışı çok hızlıdır. `File > Log to File` seçeneğiyle logları diske kaydedip Notepad++ gibi güçlü editörlerle geriye dönük inceleyebilirsiniz.

### 2. Wireshark ve VoIP Calls (Ladder Diagram)
AudioCodes trafik dökümlerini (PCAP) okumak için Wireshark'a eklenti eklemek kritiktir:
1.  AudioCodes'tan `.lua` eklenti dosyasını indirin.
2.  Wireshark içinde `About Wireshark > Folders > Personal Lua Plugins` klasörüne kopyalayın.
3.  Wireshark'ta **Telephony > VoIP Calls** menüsüne tıkladığınızda, SIP mesajlarını bir merdiven diyagramı (Ladder Diagram) olarak görselleştirir. Hangi cihazın `INVITE` attığını, diğerinin ne zaman `180 Ringing` döndüğünü milisaniyesiyle okumak saha mühendisliğinin temelidir.

## 📌 Yapılandırma Araçları

### 4. DConvert: CPT Dosyası Düzenleme Adımları
Türkiye standartlarında ses tonları (Örn: Çevir sesi 425Hz) için `usa_tones.dat` dosyasını `turkey_tones.dat` yapmak için:
1.  `DConvert.exe`'yi açın.
2.  Mevcut `.dat` dosyasını `Load` edin.
3.  `Call Progress Tones` sekmesinden frekansları Türkiye standartlarına göre (Genellikle 425Hz sürekli) güncelleyin.
4.  `Convert` butonuyla yeni ikili (binary) dosyayı üretin ve SBC'ye `Setup > Device > Software Update > Loadable File` menüsünden yükleyin.

## 📌 Bakım ve Kurtarma Araçları

### 5. BootP: Cihaz Kurtarma (Disaster Recovery)
Eğer SBC'ye hiçbir şekilde erişilemiyorsa (Firmware çökmesi):
1.  PC'nize statik bir IP verin (Örn: `192.168.0.10`).
2.  BootP yazılımını açın ve SBC'nin MAC adresini tanımlayın.
3.  Cihaza bir IP adresi (`192.168.0.1`) ve yüklenecek `.cmp` dosyasının yolunu gösterin.
4.  SBC'yi yeniden başlatın. SBC açılırken BootP'den IP alır ve firmware dosyasını otomatik olarak çekip kendini onarır.

### 6. INI Editor
Konfigürasyon dosyalarını (`.ini`) Not defteri yerine INI Editor ile açmak şu avantajları sağlar:
*   **Parametre Doğrulama:** Yanlış yazılan bir parametreyi kırmızı ile işaretler.
*   **Hiyerarşik Görünüm:** Ayarları kategorilere (Network, Signaling vb.) göre gruplar.

> [!IMPORTANT]
> **Versiyon Uyumu:** Kullandığınız araçların versiyonu ile cihazın firmware versiyonu (Örn: v7.20) mutlaka uyumlu olmalıdır. Eski bir Syslog Viewer yeni bir firmware'deki paketleri doğru yorumlayamayabilir.

---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


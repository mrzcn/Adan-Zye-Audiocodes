# Faydalı Araçlar ve Yardımcı Yazılımlar (Utilities)

AudioCodes projelerinde kurulum, analiz ve sorun giderme süreçlerini hızlandıran, AudioCodes Library üzerinden indirilebilen temel araçlar.

## 📌 Analiz ve İzleme Araçları

### 1. Syslog Viewer
SBC'den gelen Syslog paketlerini gerçek zamanlı olarak yakalayan ve görselleştiren araçtır.
*   **Neden Kullanılır?** Hataları farklı renklerde (Kırmızı: Error, Sarı: Warning) göstererek binlerce satır arasından sorunu saniyeler içinde bulmanızı sağlar.
*   **Kritik Özellik:** "Filter" özelliği ile sadece belirli bir çağrı ID'sine veya IP adresine odaklanabilirsiniz.

### 2. Wireshark Plugins
SBC'den alınan trafik dökümlerini (Packet Capture) Wireshark üzerinde daha detaylı görebilmek için kullanılan eklentilerdir.
*   **Görevi:** AudioCodes'un tescilli protokollerini ve özel SIP başlıklarını Wireshark'ın anlamasını sağlar.

## 📌 Yapılandırma Araçları

### 3. SBC Configuration Wizard
Yeni başlayanlar için hayat kurtarıcı bir araçtır.
*   **Görevi:** Teams, Avaya, Cisco gibi popüler santraller ve global operatörler için hazır şablonlar sunar. Sizin girdiğiniz IP bilgilerine göre çalışan bir `.ini` dosyası üretir.

### 4. DConvert Utility
SBC'ye özel dosya formatlarını (Binary) yönetmek için kullanılır.
*   **Call Progress Tones (CPT):** Türkiye'ye özel çevir sesi, meşgul sesi gibi frekansların olduğu `usa_tones.dat` dosyasını düzenlemek ve cihaza yüklemek için kullanılır.
*   **Voice Prompts:** Cihazın çaldığı sesli anonsları (Örn: "Lütfen bekleyiniz") dönüştürmek için kullanılır.

## 📌 Bakım ve Kurtarma Araçları

### 5. BootP Utility
Cihaza ağ üzerinden ilk erişimi sağlamak için kullanılır.
*   **Senaryo:** Cihazın IP adresi bilinmiyorsa veya yazılımı (Firmware) çökmüşse, BootP üzerinden cihaza geçici bir IP atanır ve yeni yazılım yüklenerek cihaz kurtarılır.

### 6. License Key Manager (LKM)
Cihazın seri numarasını girerek sahip olduğunuz lisans anahtarlarını indirebileceğiniz portal ve yardımcı araçtır.

### 7. AudioCodes Coverage Tool
Cihazın **CHAMPS** destek süresinin devam edip etmediğini, garantisinin durumunu seri numarasından sorgulamanıza yarayan web tabanlı araçtır.

---

> [!TIP]
> Bu araçların çoğu **AudioCodes Services Portal** üyeliği gerektirir. Bir AudioCodes mühendisi olarak ilk yapmanız gereken bu portala kayıt olup en güncel utility versiyonlarını bilgisayarınızda hazır bulundurmaktır.

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

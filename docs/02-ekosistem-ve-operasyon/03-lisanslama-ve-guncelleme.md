<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# Lisanslama ve Güncelleme Mantığı

AudioCodes SBC'ler "Kullandığın kadar öde" mantığıyla çalışan, yazılım tanımlı kapasiteye sahip cihazlardır. 

## 📌 Lisans Tipleri

Cihazın üzerinde hangi özellikleri kullanabileceğinizi lisans anahtarı belirler. Ana lisans kalemleri şunlardır:

1.  **SBC Sessions:** Aynı anda kaç eş zamanlı çağrı yapılabileceği. (Örn: 20 sessions).
2.  **Transcoding Sessions:** Kaç çağrıda codec dönüşümü yapılabileceği.
3.  **Security (TLS/SRTP):** Şifreleme özelliğinin açık olup olmadığı.
4.  **Advanced Features:** Teams Direct Routing, Voice Quality Monitoring gibi ek özellikler.

## 📌 Lisans Nasıl Yüklenir?

1.  Cihazın seri numarasını (MAC) AudioCodes'a iletirsiniz.
2.  Size uzun bir metin dizisi (License Key) gönderilir.
3.  **Setup > Device > License** menüsünden bu anahtarı yapıştırıp "Load" dersiniz.
4.  Cihazı yeniden başlatmanız (Burn & Reset) gerekebilir.

## 📌 Güncelleme (Firmware Upgrade) Mantığı

AudioCodes, cihazlarını sürekli günceller. Güncellemeler ikiye ayrılır:

*   **Maintenance Release (Yamalar):** Örn: 7.20A.202.105 -> 7.20A.202.203. Güvenlik açıklarını kapatır ve hata düzeltmeleri (Bug fix) içerir.
*   **Major Release (Ana Sürümler):** Örn: 7.20 -> 7.40. Yeni özellikler ve tamamen değişmiş bir arayüz getirebilir.

### Güncelleme Yaparken Dikkat Edilmesi Gerekenler
1.  **Release Notes:** Mutlaka okunmalıdır. Bazı versiyon geçişleri için arada bir "hop" versiyon yüklemek gerekebilir.
2.  **Backup:** Güncellemeden önce mutlaka `.ini` ve `.dat` yedeklerini alın.
3.  **Reset:** Yazılım yüklendikten sonra cihazın yeni yazılımla ayağa kalkması için "Reset" (Yeniden başlatma) şarttır. Bu sırada çağrılar kesilir.

> [!CAUTION]
> Çok eski bir firmware'den (Örn: v6.6) doğrudan en yeni sürüme (Örn: v7.4) geçmek genellikle risklidir. Konfigürasyon dosyası uyumsuzlukları nedeniyle cihaz açılmayabilir. Bu tip "büyük sıçramalar" için kademeli geçiş önerilir.

> [!IMPORTANT]
> Cihazın CHAMPS desteği aktif değilse, AudioCodes portalından yeni firmware indirmenize sistem izin vermeyebilir.


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

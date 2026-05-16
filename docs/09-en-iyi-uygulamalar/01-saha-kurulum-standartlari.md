# Saha Kurulum Standartları ve Best Practices

Bir AudioCodes SBC projesini başarıyla tamamlamak ve ileride çıkabilecek sorunları en aza indirmek için uygulanan altın kurallar.

## 🛡️ Güvenlik Standartları

1.  **Servis İzolasyonu:** Gereksiz tüm servisleri (Telnet, FTP, HTTP) kapatın. Sadece HTTPS (Port 443) ve SSH (Port 22) kullanın.
2.  **Management ACL:** Cihazın yönetim arayüzüne sadece belirli IP adreslerinden (IT departmanı, yönetim sunucusu) erişilmesine izin verin.
3.  **Unregistered Calls:** `SBC General Settings` altındaki bu ayarı mutlaka `Restrict` yapın. Bu, internetten gelen rastgele SIP saldırılarını (Scanner) anında engeller.
4.  **VLAN Ayırımı:** Yönetim trafiğini (Management) ve ses trafiğini (Media/Signaling) farklı VLAN'larda tutun.

## ⚙️ Yapılandırma Standartları

1.  **Media Anchoring:** NAT ve ses sorunlarını önlemek için IP Profile içinde `SBC Media` ayarını `SBC (Media Anchor)` olarak işaretleyin.
2.  **Symmetric NAT:** Sesin tek taraflı gelmesini önlemek için her zaman aktif edin.
3.  **İsimlendirme Standartları (Naming Convention):**
    *   IP Group: `IG_[YÖN]_[İSİM]` (Örn: `IG_LAN_PBX`)
    *   Proxy Set: `PS_[YÖN]_[İSİM]` (Örn: `PS_WAN_TT`)
    *   IP Profile: `IP_[İSİM]` (Örn: `IP_Teams`)
4.  **Keep-Alive:** SIP OPTIONS mesajlarını 60 saniyelik periyotlarla gönderin. Çok sık (Örn: 5 sn) gönderim yapmak networkte gereksiz yük oluşturur.

## 📈 Operasyonel Standartlar

1.  **Yedekleme (Backup):** Her başarılı yapılandırma sonrası `.ini` dosyasını yedekleyin ve dosya ismine tarih/versiyon ekleyin (Örn: `SBC_Config_2026_05_16_v1.ini`).
2.  **Log Yönetimi:** Cihazın kendi hafızası sınırlıdır. Tüm Syslog ve Message Logları harici bir sunucuya (Örn: AudioCodes OVOC veya ücretsiz bir Syslog Server) yönlendirin.
3.  **Firmware Politikası:** Kritik bir güvenlik açığı yoksa, her zaman "N-1" kuralını izleyin. (En yeni sürümden bir önceki stabil sürümü kullanın).
4.  **Test Araçları:** Yayına almadan önce mutlaka `Test Tools > Dial Plan Search` ile yönlendirme kurallarını simüle edin.

## 🎓 Proje Teslim Kontrol Listesi (Checklist)

- [ ] Admin şifresi değiştirildi mi?
- [ ] Yedekleme yapıldı ve müşteriye teslim edildi mi?
- [ ] Logların harici sunucuya gittiği doğrulandı mı?
- [ ] Acil durum (911/112/155) aramaları test edildi mi?
- [ ] Ses kalitesi (MOS) değerleri normal mi?

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

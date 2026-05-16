# Ses Kalitesi İzleme ve RTCP-XR

AudioCodes SBC, her bir çağrının ses kalitesini gerçek zamanlı olarak ölçebilir ve raporlayabilir. Bu, "Ses kesiliyor" veya "Ses robotik geliyor" gibi şikayetlerin teknik nedenini bulmak için kullanılır.

## 📌 MOS (Mean Opinion Score) Nedir?

Ses kalitesini 1 (en kötü) ile 5 (en iyi) arasında puanlayan bir standarttır.
*   **4.0 - 4.5:** Mükemmel (Kayıpsız ses).
*   **3.5 - 4.0:** Kabul edilebilir (Hafif parazit).
*   **3.0 altı:** Kötü (İletişim kurmak zor).

## 📌 RTCP-XR (Extended Reports)

Normal RTCP paketleri sadece temel istatistikleri verirken, **RTCP-XR** şu detayları sağlar:
*   **Packet Loss (Paket Kaybı):** Network üzerindeki veri kayıpları.
*   **Jitter:** Paketlerin varış süreleri arasındaki düzensizlik (Seste titreme/kopma).
*   **Delay (Gecikme):** Sesin git-gel süresi (Latency).

## 📌 Yapılandırma ve İzleme (v7.20)

**Aktivasyon:** `IP Profile` ayarları altındaki **RTCP-XR** parametresi `Enable` yapılmalıdır.

**İzleme Ekranı:** `Status & Diagnostics > Voice Quality > Active Calls`
Bu ekran üzerinden aktif çağrıların o anki MOS değerlerini, gecikme (delay) sürelerini ve hangi codec'i kullandıklarını görebilirsiniz.

## 📌 Quality of Experience (QoE)

AudioCodes v7.20, ses kalitesi belirli bir eşiğin altına düştüğünde (Örn: MOS < 3.0) Syslog veya SNMP Trap üzerinden uyarı gönderebilir. Bu sayede sistem yöneticisi, şikayet gelmeden önce networkte bir sorun olduğunu fark edebilir.

> [!TIP]
> Ses kalitesi sorunlarını analiz ederken her iki bacağı (Ingress ve Egress) ayrı ayrı inceleyin. Genellikle sorun internet bacağındaki (ISP) dalgalanmalardan kaynaklanır.

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

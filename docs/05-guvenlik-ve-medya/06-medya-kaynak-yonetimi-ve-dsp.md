# Medya Kaynak Yönetimi ve DSP

AudioCodes SBC'de ses sinyallerinin işlenmesi (Transcoding, DTMF algılama, Ses tonu üretimi) **DSP (Digital Signal Processor)** adı verilen donanım çipleri tarafından gerçekleştirilir.

## 📌 Transcoding (Codec Dönüşümü) Nedir?

Bir taraftan gelen ses paketinin (Örn: G.711), diğer tarafa farklı bir formatta (Örn: G.729) iletilmesi işlemidir. 
*   **Neden Gereklidir?** Operatör bant genişliğinden tasarruf etmek için G.729 isterken, dahili santraliniz (PBX) sadece G.711 destekleyebilir. SBC burada "tercüman" görevi görür.

## 📌 DSP Kaynakları ve Kapasite

Transcoding işlemi yoğun bir CPU/DSP gücü gerektirir. 
*   **Donanım Limitleri:** Her Mediant 800 modelinin belirli bir DSP kanal kapasitesi vardır. 
*   **Transcoding Faktörü:** Bir transcoding çağrısı, transparan (bypass) bir çağrıya göre çok daha fazla kaynak tüketir. 
*   **Kapasite Planlama:** Proje aşamasında kaç eş zamanlı çağrının (Concurrent Calls) transcoding yapılacağı mutlaka hesaplanmalıdır.

## 📌 Coder Group Yapılandırması (v7.20)

**Menü:** `Setup > Signaling & Media > Coders & Profiles > Coder Groups`

1.  **Coder Name:** Kullanılacak codec seçilir (G.711Alaw, G.729 vb.).
2.  **Packetization Time (p-time):** Ses paketlerinin ne sıklıkla gönderileceği (Genellikle 20ms).
3.  **VAD (Voice Activity Detection):** Sessiz anlarda paket gönderilmemesini sağlayarak bant genişliği tasarrufu yapar (Ancak bazı sistemlerde sorun çıkarabilir).

## 📌 DTMF ve Ses Tonları

DSP'ler aynı zamanda tuş seslerini (DTMF) yakalar. 
*   **In-band:** Tuş sesi normal ses kanalından (RTP) gönderilir.
*   **Out-of-band (RFC 2833):** Tuş sesi özel bir RTP paketi olarak gönderilir (SBC'lerde en sağlıklı yöntemdir).

> [!IMPORTANT]
> Eğer cihazın DSP kaynakları tükenirse, yeni gelen çağrılar "No resources" hatası ile reddedilir. Bu durumu `Status & Diagnostics > Voice Quality > DSP Status` menüsünden izleyebilirsiniz.

---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


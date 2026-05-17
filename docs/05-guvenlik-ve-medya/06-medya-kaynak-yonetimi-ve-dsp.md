# Medya Kaynak Yönetimi ve DSP

AudioCodes SBC'de ses sinyallerinin işlenmesi (Transcoding, DTMF algılama, Ses tonu üretimi) **DSP (Digital Signal Processor)** adı verilen donanım çipleri tarafından gerçekleştirilir.

## 📌 Transcoding (Codec Dönüşümü) Nedir?

Bir taraftan gelen ses paketinin (Örn: G.711), diğer tarafa farklı bir formatta (Örn: G.729) iletilmesi işlemidir. 
*   **Neden Gereklidir?** Operatör bant genişliğinden tasarruf etmek için G.729 isterken, dahili santraliniz (PBX) sadece G.711 destekleyebilir. SBC burada "tercüman" görevi görür.

## 📌 DSP Kaynakları ve Kapasite (Weight Factor)

Transcoding işlemi yoğun bir CPU/DSP gücü gerektirir. 
*   **Donanım Limitleri:** Her Mediant 800 modelinin belirli bir DSP kanal kapasitesi (Örn: 120, 250, 400 kanal) vardır. 
*   **Weight Factor:** Her codec'in bir "ağırlık" puanı vardır. G.711'den G.711'e (Bypass) geçiş 1 DSP kanalı tüketirken, Opus veya AMR-WB gibi ağır codeclere transcoding yapmak 4 veya 8 DSP kanalı tüketebilir.
*   **Kapasite Planlama:** Proje aşamasında sadece "Eş zamanlı çağrı sayısı" değil, hangi codeclerin çevrileceği hesaplanarak DSP kapasitesi belirlenmelidir.

## 📌 Coder Group Yapılandırması (v7.20)

**Menü:** `Setup > Signaling & Media > Coders & Profiles > Coder Groups`

1.  **Coder Name:** Kullanılacak codec seçilir (G.711Alaw, G.729, Opus, AMR-NB vb.).
2.  **Packetization Time (p-time):** Ses paketlerinin ne sıklıkla gönderileceği (Genellikle 20ms). P-time uyuşmazlığı (Örn: Bir taraf 20ms, diğeri 30ms gönderiyorsa) transcoding gerektirir.
3.  **VAD (Voice Activity Detection):** Sessiz anlarda (kimse konuşmazken) paket gönderilmemesini sağlayarak bant genişliği tasarrufu yapar. Ancak bazı sistemlerde arka plan gürültüsü birden kesildiği için "hat düştü" hissi yaratabilir; genellikle kapatılması (Disable) önerilir.

## 📌 Media Transcoding Mode ve Uzantılar (Extension Profiles)

IP Profile içinde bulunan `Media Transcoding Mode` parametresi kritik bir davranışı belirler:
*   **Bypass:** Transcoding kapalıdır. Uç noktalar kendi aralarında codec pazarlığı yapar (SBC müdahale etmez).
*   **Force:** SBC, Coder Group'taki kendi codec listesini dikte eder ve ne olursa olsun o formata çeviri yapar.
*   **Extension Profiles:** Farklı operatörlerin AMR veya Opus gibi karmaşık codeclere eklediği özel parametreleri (Format-parameters) eşleştirmek için kullanılır. 

## 📌 DTMF (Tuş Sesi) Çevirisi ve Translation

DSP'ler aynı zamanda tuş seslerini (DTMF) algılar ve çevirir (Translation). IVR (Sesli Yanıt Sistemi) senaryolarında DTMF uyuşmazlığı sık yaşanır.
*   **In-band:** Tuş sesi (Dıt) normal insan sesiyle aynı frekansta (RTP) gönderilir. G.729 sıkıştırmasında bu tonlar bozulur ve IVR tuşlamaları tanımaz.
*   **Out-of-band (RFC 2833 / RFC 4733):** Tuş sesi dijital bir "olay" (Event) olarak RTP paketi içinde flag ile gönderilir. SBC'lerde her zaman tercih edilmesi gereken yöntemdir.
*   **SIP INFO:** Tuşlamanın RTP yerine SIP sinyalleşme mesajı (INFO) olarak gönderilmesidir.
*   **SBC'nin Rolü:** Bir taraf In-Band, diğer taraf RFC 2833 istiyorsa, SBC araya girip "DTMF Translation" yaparak In-band sesi dijital sinyale (veya tam tersine) çevirir.

> [!IMPORTANT]
> Eğer cihazın DSP kaynakları tükenirse, yeni gelen çağrılar "503 Service Unavailable" veya "No resources" hatası ile reddedilir. Bu durumu `Status & Diagnostics > Voice Quality > DSP Status` menüsünden izleyebilirsiniz. Bu sayfada hangi DSP çekirdeğinin ne kadar yük altında olduğu (Utilization) grafiksel olarak görünür.

---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


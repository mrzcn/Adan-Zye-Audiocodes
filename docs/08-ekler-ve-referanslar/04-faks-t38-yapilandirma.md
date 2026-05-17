<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# Faks (T.38) Yapılandırması

IP ağları üzerinden faks gönderimi (FoIP), paket gecikmelerine karşı çok hassastır. AudioCodes SBC'de faks trafiğini başarılı bir şekilde yönetmek için temel kavramlar:

## 📌 Faks İletim Modları ve T.38 Fallback

1.  **T.38 (Relay):** En güvenilir yöntemdir. Faks sinyalini (analog) yakalar, IP paketlerine (IFP) dönüştürür ve karşı tarafta tekrar analog faks sinyaline çevirir. Paket kayıplarına karşı (Redundancy sayesinde) oldukça dayanıklıdır.
2.  **G.711 Pass-through:** Faks sesini normal bir insan sesiymiş gibi G.711 codec ile taşır. Çok kaliteli ve 0 paket kayıplı bir network gerektirir. Sıkıştırmalı (G.729) bağlantılarda KESİNLİKLE çalışmaz.
3.  **T.38 Fallback to G.711:** SBC, önce T.38 ile anlaşmaya (Negotiation) çalışır. Karşı taraf (Operatör veya PBX) "Ben T.38 desteklemiyorum" derse (Örn: 488 Not Acceptable Here dönerse), SBC otomatik olarak G.711 Pass-through moduna düşer (Fallback).

## 📌 CNG/CED Ton Algılama (Tone Detection)

Faks çağrısı normal bir ses çağrısı (G.711/G.729) olarak başlar. 
*   **CNG (Calling Tone):** Faks makinesinin ahizesini kaldırdığınızda duyduğunuz 1100 Hz'lik sinyaldir.
*   **CED (Called Terminal Identification):** Karşıdaki faks makinesinin açıldığında verdiği 2100 Hz'lik ince tiz sestir.
*   **SBC'nin Rolü:** DSP, bu tonlardan birini duyduğu an çağrının ses değil Faks olduğunu anlar ve çağrıyı kesmeden anında T.38 için **re-INVITE** mesajı tetikler.

## 📌 Yapılandırma Adımları (v7.20)

**Menü:** `Setup > Signaling & Media > Coders & Profiles > IP Profiles`

1.  **Fax Transport Mode:** `T.38 Relay` olarak seçilmelidir.
2.  **V.34 Fax Transfer:** V.34 çok hızlı (33.6 kbps) faks iletimidir (Super G3). Ancak T.38 ile her zaman uyumlu çalışmayabilir. Eski/sorunlu ağlarda `Disable` yapılıp hız V.17'ye (14.4 kbps) düşürülerek stabilite artırılabilir.
3.  **Fax Error Correction Mode (ECM):** T.38 ile faks giderken kaybolan paketlerin tekrar istenmesidir. Kalitesiz hatlarda Kapatılması (Disable) önerilebilir (Çünkü faksın çok uzun sürüp zaman aşımına uğramasını engeller).

## 📌 Sık Karşılaşılan Sorunlar ve Çözümler

*   **Faks Başlıyor Ama Yarıda Kesiliyor:** Network üzerindeki Jitter değerini kontrol edin. IP Profile içindeki **Jitter Buffer** ayarlarını `Dynamic` yapın veya **V.34'ü kapatın**.
*   **Hiç Faks Gitmiyor:** Karşı tarafın T.38 destekleyip desteklemediğini Message Log üzerinden (re-INVITE paketlerine bakarak) teyit edin. 
*   **Operatör Reddediyor:** Bazı Türk operatörler re-INVITE T.38 isteklerini reddeder. Bu durumda IP Profile üzerinden "SBC Fax Fallback" açılmalıdır.

## 📌 CLI ile Faks Ayarı
```bash
SBC(config-voip)# ip-profile 1
SBC(ip-profile-1)# fax-modem-transport-mode t38-relay
SBC(ip-profile-1)# activate
```

> [!TIP]
> Eğer T.38 ile sorun yaşıyorsanız, geçici bir çözüm olarak her iki uçta da `G.711 Pass-through` modunu deneyebilirsiniz. Bu modda codec her zaman G.711 olmalı, Echo Canceller (AEC) ve VAD (Voice Activity Detection) KESİNLİKLE kapalı olmalıdır. Aksi halde faks tonları kesintiye uğrar.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


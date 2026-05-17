# Ses Kalitesi İzleme ve RTCP-XR

AudioCodes SBC, her bir çağrının ses kalitesini gerçek zamanlı olarak ölçebilir ve raporlayabilir. Bu, "Ses kesiliyor" veya "Ses robotik geliyor" gibi şikayetlerin teknik nedenini bulmak için kullanılır.

## 📌 MOS (Mean Opinion Score) Nedir?

Ses kalitesini 1 (en kötü) ile 5 (en iyi) arasında puanlayan bir standarttır.
*   **4.0 - 4.5:** Mükemmel (Kayıpsız ses).
*   **3.5 - 4.0:** Kabul edilebilir (Hafif parazit).
*   **3.0 altı:** Kötü (İletişim kurmak zor).

## 📌 RTCP-XR (Extended Reports) Detayları

Normal RTCP paketleri sadece temel istatistikleri (Giden/Gelen paket sayısı) verirken, **RTCP-XR** VoIP mühendisliğinin röntgenini çeker:
*   **Packet Loss (Paket Kaybı):** Network üzerindeki donanımsal veya kapasitif veri kayıpları. %1'in üzeri sesteki kaliteyi bozmaya başlar.
*   **Jitter:** Paketlerin varış süreleri arasındaki düzensizlik (Seste titreme/kopma).
*   **Delay (Gecikme/Latency):** Sesin git-gel süresi. 150ms üzeri "Telsiz" etkisine (Walkie-talkie effect) neden olur.

## 📌 Jitter Buffer ve Kalite Düzeltme (PLC)

AudioCodes SBC, zayıf internet bağlantılarında (Örn: 4G/LTE, Wi-Fi) bozulan sesi düzeltmek için aktif mekanizmalara sahiptir:

1.  **Dynamic Jitter Buffer:** SBC, paketlerin düzensiz gelişini (Jitter) absorbe etmek için sesi milisaniyeler seviyesinde belleğinde bekletir ve sıraya koyarak gönderir. `IP Profile > Jitter Buffer` ayarından gecikmeye tahammülü artırmak için bu değer dinamik veya statik (Örn: 100ms) yapılabilir.
2.  **Packet Loss Concealment (PLC):** Eğer bir ses paketi internette kaybolmuşsa, SBC bir önceki ve bir sonraki pakete bakarak kaybolan sesi "tahmin eder" ve arayı sahte ama gerçeğe çok yakın bir sesle doldurur (Robotikleşmeyi önler).

## 📌 Yapılandırma ve İzleme (v7.20)

**Aktivasyon:** `IP Profile` ayarları altındaki **RTCP-XR** parametresi `Enable` yapılmalıdır.

**İzleme Ekranı:** `Status & Diagnostics > Voice Quality > Active Calls`
Bu ekran üzerinden aktif çağrıların o anki MOS değerlerini, gecikme (delay) sürelerini ve hangi codec'i kullandıklarını görebilirsiniz.

## 📌 Quality of Experience (QoE) ve OVOC Entegrasyonu

AudioCodes v7.20, ses kalitesi belirli bir eşiğin altına düştüğünde proaktif davranabilir.
*   **Threshold Alarmları:** `QoE Profile` altından eşik değerler belirlenir (Örn: MOS < 3.0 ise Alarm Ver). Syslog veya SNMP Trap üzerinden uyarı gönderilir.
*   **OVOC (One Voice Operations Center):** SBC, binlerce çağrının RTCP-XR verisini merkezi yönetim sunucusu OVOC'a gönderir. OVOC bu verileri işleyerek "Son 24 saatte Hangi Operatör Bacağında Kalite Düştü?" gibi grafiksel raporlar sunar.

> [!WARNING]
> **Tuzak:** Ses kalitesi her zaman iki yönlüdür. Eğer müşteri "Sesim gitmiyor/kesik gidiyor" diyorsa sorun Upload yönündedir, "Ses kesik geliyor" diyorsa sorun Download yönündedir. Analiz yaparken her iki bacağı (Ingress ve Egress) ayrı ayrı inceleyin. Genellikle sorun internet bacağındaki (ISP) dalgalanmalardan veya şifreleme/çözme (SRTP) yükünden kaynaklanır.

---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


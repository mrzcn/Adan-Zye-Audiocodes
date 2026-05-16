# NAT Traversal ve Media Anchoring

Network Address Translation (NAT), VoIP trafiğinin en büyük düşmanlarından biridir. SBC, "Tek taraflı ses" (One-way audio) sorunlarını çözmek için gelişmiş NAT yönetim araçları sunar.

## 📌 Media Anchoring (SBC Mode) Nedir?

Media Anchoring, SBC'nin ses paketlerini (RTP) her iki taraftan da üzerine alması ve tekrar iletmesi işlemidir. 
*   **Avantajı:** İki bacak arasındaki IP ve Port karmaşasını gizler.
*   **Güvenlik:** İç ağdaki cihazların IP adresleri asla dışarı sızmaz.
*   **NAT Çözümü:** SBC, ses paketlerinin kendi üzerinden geçmesini zorunlu kılarak güvenlik duvarlarını (Firewall) aşar.

## 📌 Symmetric NAT ve SBC

Symmetric NAT yapılarında, dışarıdan gelen ses paketleri sadece daha önce SBC'nin paket gönderdiği porttan içeri girebilir.
*   **Çözüm:** SBC, karşı tarafın ses göndermesini beklemeden ona küçük bir paket (No-Op) göndererek Firewall üzerinde bir "delik" açar. Bu işleme **NAT Keep-Alive** denir.

## 📌 Far-End NAT (Uzaktan Erişim)

Evden çalışan bir personelin IP telefonu, evdeki modemin (NAT) arkasındadır. 
*   **SBC Davranışı:** SBC, SIP mesajındaki IP adresine değil, paketin **gerçekten geldiği** (Source IP/Port) adrese ses gönderir. Bu ayar `IP Profile > SBC Remote NAT` üzerinden yönetilir.

## 📌 Media Optimization (Latching)

AudioCodes SBC, ses paketlerinin geldiği kaynağı dinamik olarak öğrenir ve ses akışını o adrese sabitler (Latching). Eğer ses bir süre gelmezse, SBC portu kapatarak güvenliği sağlar.

> [!WARNING]
> Eğer "Ses sadece benden gidiyor ama karşıdan gelmiyor" diyorsanız, büyük ihtimalle SBC'nin **Media Realm** yapılandırmasında yanlış bir IP Interface seçilmiştir veya Firewall'da RTP portları (Genellikle 6000-10000 arası) kapalıdır.

---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


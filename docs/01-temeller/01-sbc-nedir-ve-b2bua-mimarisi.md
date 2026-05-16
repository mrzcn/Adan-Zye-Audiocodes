<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# SBC (Session Border Controller) Nedir?

Session Border Controller (SBC), farklı IP ağları arasındaki (örneğin kurumsal LAN ile Servis Sağlayıcı WAN'ı) Sinyalleşme (SIP) ve Medya (RTP) trafiğini güvenli, kesintisiz ve kurallara bağlı bir şekilde birbirine bağlayan özel amaçlı ağ geçitleridir.

Bir SBC, geleneksel bir Firewall (Güvenlik Duvarı) veya NAT (Ağ Adresi Çevirici) cihazından farklı olarak çalışır. Sıradan firewall'lar SIP trafiğinin doğasını anlayamazlar; SIP paketlerinin içindeki IP adreslerini dinamik olarak değiştiremez veya ses trafiğine (RTP) müdahale edemezler. SBC'ler ise SIP paketlerinin "içine bakarak" manipülasyon yapabilme yeteneğine sahiptir.

## 📌 B2BUA (Back-to-Back User Agent) Mimarisi (Derin Bakış)

Standart bir SIP Proxy, paketleri sadece bir duraktan diğerine iletirken (ve sadece başlığa dokunurken), AudioCodes SBC bir **B2BUA** olarak çalışır.

### B2BUA Nasıl Çalışır?
1.  **Ingress Leg (Giriş Bacağı):** A abonesinden gelen `INVITE` paketini SBC karşılar ve burada sonlandırır. SBC, A abonesine göre bir "User Agent Server" (UAS) gibi davranır.
2.  **Egress Leg (Çıkış Bacağı):** SBC, kendi kurallarına (Routing, Manipulation) göre B abonesine yepyeni bir `INVITE` paketi oluşturup gönderir. B abonesine göre SBC bir "User Agent Client" (UAC) gibi davranır.

### Transaction vs Dialog
*   **Transaction:** Bir istek (Request) ve ona gelen yanıtların (Response) bütünüdür (Örn: `INVITE` -> `100 Trying` -> `200 OK`).
*   **Dialog:** İki uç nokta arasında kurulan kalıcı ilişkidir. B2BUA, bir diyaloğu iki ayrı "Transaction" setine bölerek yönetir. Bu sayede bir tarafta yaşanan sinyalleşme hatası diğer tarafı doğrudan çökertmez.

## 📌 SIP Proxy vs B2BUA Karşılaştırması

| Özellik | SIP Proxy | B2BUA (SBC) |
| :--- | :--- | :--- |
| **Paket Gövdesi (SDP)** | Dokunamaz | Tamamen değiştirebilir |
| **Medya (RTP)** | Karışamaz | Kendi üzerinden akıtabilir (Anchoring) |
| **Topoloji Gizleme** | Yapamaz | İç ağ IP'lerini tamamen gizler |
| **Header Manipülasyonu** | Kısıtlı | Sınırsız (Regex desteği) |

## 📌 Topology Hiding (Topoloji Gizleme)

Güvenlik için iç ağdaki sunucuların IP adresleri, port bilgileri ve sistem isimleri asla dış dünyaya sızmamalıdır.
*   **SBC Çözümü:** B2BUA mimarisi sayesinde dış ağdaki bir operatör, çağrının arkasında bir Genesys sunucusu mu yoksa bir Avaya santral mi olduğunu göremez. Sadece SBC'nin IP adresini görür.

## 📌 Media Anchoring (Ses Sabitleme)

Ses paketlerinin (RTP) doğrudan uç noktalar arasında akması yerine SBC üzerinden geçmesine denir.
*   **Neden Önemli?** Eğer ses paketleri SBC üzerinden geçmezse, SBC ses kalitesini (MOS) ölçemez, transcoding yapamaz ve NAT arkasındaki cihazların ses sorunlarını çözemez.
*   **SBC Görevi:** SBC, SDP paketindeki medya IP'sini kendi IP'si ile değiştirerek "ses bana gelsin, ben ileteyim" der.

## 📌 SIP Interworking: "Lezzet" Farklarını Giderme

SIP standart bir protokol olsa da, her üretici (Cisco, Microsoft, Avaya) bu protokolü farklı "lezzetlerde" yorumlar.
*   **SBC'nin Tercümanlığı:** Bir tarafın "zorunlu" tuttuğu bir başlığı diğeri göndermiyorsa, SBC araya girerek o başlığı ekler veya formatını değiştirir. Bu sürece **SIP Interworking** denir.

> [!IMPORTANT]
> AudioCodes SBC'yi sadece bir güvenlik cihazı olarak değil, ağınızdaki farklı ses sistemlerini birbirine bağlayan bir **"Trafik Polisi ve Tercüman"** olarak düşünmelisiniz.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


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

## 📌 SBC'nin Temel Görevleri

1. **Güvenlik ve İzolasyon:** 
   * Ağ yapınızı dış dünyadan gizler (Topology Hiding).
   * DoS/DDoS saldırılarına ve yetkisiz SIP kayıt isteklerine (SIP Vicious Scans) karşı savunma hattı oluşturur.
2. **B2BUA (Back-to-Back User Agent) Mimarisi:**
   * A noktasından gelen çağrıyı B noktasına doğrudan yönlendirmez. Çağrıyı kendi üzerinde "sonlandırır" ve B noktasına doğru "kendi adına yepyeni bir çağrı başlatır". Bu yapıya B2BUA denir.
   * Bu mimari sayesinde her iki bacağın (örneğin Genesys tarafı ve VoIP GW tarafı) birbirinden tamamen bağımsız kalması sağlanır.
3. **Transcoding (Kod Çevrimi):**
   * A noktası G.711 (PCMA) desteklerken, B noktası G.729 destekleyebilir. SBC ortada durarak ses paketlerini anlık (real-time) olarak dönüştürebilir.
4. **NAT Traversal:**
   * Ses paketlerinin tek yönlü gitmesi (One-way audio) sorununu çözmek için SIP başlıklarındaki IP'leri okur ve manipüle eder.

---

## 🛠 Neden Firewall Yerine SBC Kullanmalıyız?

Sıradan bir Firewall üzerinden TCP/UDP 5060 portunu açmak, bir ses sunucusunu dünyaya açmak için yeterli (ve güvenli) değildir. Çünkü:

* SIP paketlerinin içeriğinde (SDP Payload) medyanın (RTP) hangi IP ve porttan akacağı yazılıdır.
* Firewall paketin başlığına (Header) müdahale etse bile, paketin "içine" (Payload) giremez. Bu yüzden SIP karşıya ulaşır ancak telefonlar çaldığında ses gelmez (One-way veya No-way audio).
* SBC, Application Layer (Uygulama Katmanı) seviyesinde çalıştığı için paketi açar, SDP içeriğindeki yerel IP'yi okur, kendi Public/Dış IP'si ile değiştirip kapatır.

> [!NOTE]
> AudioCodes Mediant serisi, B2BUA mimarisini cihazın kalbine yerleştirmiştir. Bir çağrıyı yönlendirirken cihaz her zaman iki ayrı SIP bacağı (Ingress ve Egress) oluşturur.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


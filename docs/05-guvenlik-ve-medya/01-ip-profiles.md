<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# IP Profiles

IP Profile, bir IP Group'un sahip olması gereken davranışları (Codec kısıtlamaları, SIP başlık manipülasyonları, şeffaflık ayarları vb.) belirlediğiniz kural setidir.

## 📌 IP Profile Neden Kullanılır?

Her ses sistemi (Genesys, PBX, Operatör) kendine has SIP özellikleri bekler. Örneğin bir sistem `P-Asserted-Identity` başlığı beklerken diğeri bunu reddedebilir. IP Profile bu farklılıkları gidermek (Interworking) için kullanılır.

## 📌 Yapılandırma Adımları (v7.20)

**Menü:** `Setup > Signaling & Media > Coders & Profiles > IP Profiles`

En kritik v7.20 parametreleri:

### 1. SBC Routing & Media Sekmesi
*   **SBC Media Security Mode:** Şifreleme kullanılmıyorsa `Symmetric` seçilmesi önerilir.
*   **Extension Coders:** `None` olarak seçilirse SBC codec dönüşümü yapmaz (Transparan geçiş).
*   **SBC Media:** `SBC (Media Anchor)` seçilerek sesin SBC üzerinden geçmesi garanti edilir.

### 2. SBC SIP Headers Sekmesi
*   **Remote Representation Mode:** `P-Asserted-Identity` veya `Diversion` gibi başlıkların nasıl yönetileceğini belirler.
*   **Host Part in To Header:** Çağrı giderken To başlığındaki host kısmına ne yazılacağını belirler (Örn: `Dest Proxy IP`).
*   **Host Part in From Header:** (Bu parametre v7.20'de her zaman görünmeyebilir, varsayılan olarak SBC çıkış bacağının IP'sini yazar).

### 3. SBC Signaling Sekmesi
*   **Pass-through Unknown Headers:** `Yes` seçilirse, SBC anlamadığı özel SIP başlıklarını silmeden karşı tarafa aktarır (Transparanlık için kritiktir).

## 📌 Topoloji Gizleme (Topology Hiding)

IP Profile ayarları sayesinde iç ağdaki sunucuların IP adresleri giden paketlerden temizlenir ve yerine SBC'nin IP'si yazılır. Bu, güvenlik için temel bir gerekliliktir.

> [!TIP]
> Eğer "Ses tek taraflı geliyor" veya "Çağrı kurulduktan 30 saniye sonra düşüyor" gibi sorunlar yaşıyorsanız, IP Profile içindeki **SBC Media** ve **Symmetric NAT** ayarlarını kontrol edin.

> [!NOTE]
> IP Profile'da yaptığınız bir değişiklik, o profile bağlı olan **tüm IP Group'ları** anında etkiler.


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

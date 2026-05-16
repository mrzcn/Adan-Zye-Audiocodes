<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# Software vs. Hardware SBC: Avantaj ve Dezavantajlar

Yeni bir projeye başlarken verilmesi gereken en kritik kararlardan biri şudur: "Fiziksel bir kutu (Hardware) mu almalıyız, yoksa sanal sunucuya (Software - Mediant VE) mı kurmalıyız?"

## 📌 1. Donanım (Hardware) SBC

Örn: Mediant 800, Mediant 1000.

### ✅ Avantajlar
*   **Fiziksel Port Desteği:** Analog telefon (FXS) veya dijital hat (E1) bağlamanız gerekiyorsa tek seçenek donanımdır.
*   **DSP Gücü:** Ses işleme (Transcoding) için üzerinde özel çipler bulunur, ana işlemciyi yormaz.
*   **Bağımsızlık:** Şirketin sanal sunucu altyapısı (VMware vb.) çökse bile ses trafiği çalışmaya devam eder.

### ❌ Dezavantajlar
*   **Fiziksel Alan:** Veri merkezinde yer kaplar, elektrik tüketir ve ısınır.
*   **Bakım:** Fan arızası, güç kaynağı bozulması gibi fiziksel riskleri vardır.
*   **Lojistik:** Arızalandığında yenisinin gelmesi kargo süresi demektir.

---

## 📌 2. Yazılım (Software - Virtual Edition) SBC

Örn: VMware, Hyper-V, AWS veya Azure üzerine kurulan Mediant VE.

### ✅ Avantajlar
*   **Hız:** Dakikalar içinde yeni bir SBC kurup ayağa kaldırabilirsiniz.
*   **Esneklik:** İhtiyaç arttığında sanal sunucunun CPU/RAM değerini artırarak kapasiteyi (lisans dahilinde) büyütebilirsiniz.
*   **Donanımsızlık:** Fiziksel yer kaplamaz, donanım arızası riski sanallaştırma katmanına aittir.
*   **Yedeklilik (HA):** Sanal sunucu taşıma (vMotion vb.) özellikleri sayesinde yüksek erişilebilirlik sağlar.

### ❌ Dezavantajlar
*   **Port Yoksunluğu:** Fiziksel hiçbir kablo (FXS/E1) takılamaz. Sadece saf IP (SIP Trunk) projeleri için uygundur.
*   **Sanallaştırma Yükü:** RTP trafiği yoğunlaştığında sanal ağ kartları (vNIC) üzerinde gecikme (Jitter) oluşma riski vardır.
*   **Bağımlılık:** VMware veya host makine çökerse ses de gider.

## 📌 Karşılaştırma Özeti

| Kriter | Donanım (Hardware) | Yazılım (Software VE) |
| :--- | :--- | :--- |
| **Kurulum** | Saatler/Günler | Dakikalar |
| **Fiziksel Port** | Var (E1/FXS/FXO) | Yok |
| **Transcoding** | Çok Başarılı (DSP) | Sınırlı (CPU bağımlı) |
| **Cloud Desteği** | Yok | Var (Azure/AWS/GCP) |
| **Ömür** | 5-7 Yıl (Donanım ömrü) | Sınırsız (Güncelleme ile) |

> [!IMPORTANT]
> Eğer projenizde bakır kabloyla gelen bir E1 hattı veya duvardaki analog telefonlar varsa **Donanım** almak zorundasınız. Eğer her şey SIP üzerinden (Pure IP) dönüyorsa **Software (VE)** modern ve mantıklı tercihtir.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


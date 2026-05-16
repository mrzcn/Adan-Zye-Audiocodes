<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# Number Manipulation

Number Manipulation, arayan (Calling) veya aranan (Called) numaraların formatını değiştirmek için kullanılır. (Örn: Numara başına `0` eklemek veya `+90`'ı silmek).

## 📌 Neden Kullanılır?

*   **Format Uyumu:** Genesys numaraları `+90` formatında gönderirken, operatör Gateway'i numaraları başında `0` olacak şekilde bekleyebilir.
*   **Gizleme:** Arayan numaranın son 4 hanesini maskelemek için kullanılabilir.
*   **Yönlendirme:** Gelen numarayı manipüle ederek farklı bir hedefe yönlendirilmesini sağlamak için.

## 📌 Sinyalleşme Akışındaki Sıralama (Order of Operations)

Bir çağrı SBC'ye geldiğinde numara dönüşümü şu sırayla gerçekleşir:
1.  **Inbound Manipulation:** Çağrı henüz yönlendirilmeden (Routing) önce yapılır. Aranan numarayı (Called) routing tablosuna uygun hale getirmek için kullanılır.
2.  **IP-to-IP Routing:** SBC, manipüle edilmiş numaraya bakarak hedefi belirler.
3.  **Outbound Manipulation:** Çağrı hedefe gönderilmeden hemen önce yapılır. Hedef sistemin (Operatör veya Santral) beklediği formata dönüştürmek için kullanılır.

## 📌 Map Tables (Toplu Dönüşüm) Kullanımı

Eğer 100 farklı bölge kodunu tek tek kural yazarak değiştirmeye çalışırsanız hem hata payı artar hem de CPU yükü yükselir.
*   **Çözüm:** `Setup > Signaling & Media > SBC > Manipulation > Destination Phone Number Map`
*   **Mantık:** Bir Excel tablosu gibi `Original Prefix` ve `New Prefix` eşleşmeleri tanımlanır.
*   **Avantaj:** Tek bir Outbound Manipulation kuralı, bu tabloyu referans alarak binlerce numara dönüşümünü saniyeler içinde yapar.

## 📌 Calling Name (Arayan İsim) Manipülasyonu

Sadece numaraları değil, telefon ekranında görünen ismi de değiştirebilirsiniz.
*   **Action:** `Setup > Signaling & Media > SBC > Manipulation > Outbound Manipulation` menüsünde `Calling Name` alanını kullanın.
*   **Senaryo:** Çağrı merkezinden gelen tüm aramaların ekranda "Müşteri Hizmetleri" olarak görünmesini sağlayabilirsiniz.

## 📌 İleri Düzey Senaryo: CLIP Gizleme (CLIR)

Bazı durumlarda arayan numaranın karşı tarafa gitmesini engellemek isteyebilirsiniz.
*   **Yöntem:** `Calling Presentation` parametresini `Restricted` yaparak numaranın operatör tarafına gizli gitmesini sağlayabilirsiniz.
*   **Regex Örneği:** `^.*$` -> `Restricted` (Tüm arayanları gizle).

## 📌 Dial Plan Tag Entegrasyonu

Manipülasyon kurallarını sadece IP Group bazlı değil, **Dial Plan Tag**'lerine göre de tetikleyebilirsiniz.
*   **Senaryo:** Dial Plan'da "Uluslararası" olarak etiketlenen çağrılara farklı, "Şehir İçi" olarak etiketlenenlere farklı numara dönüşümü uygulayabilirsiniz.

> [!IMPORTANT]
> **Simetri:** Unutmayın, giden çağrıda yaptığınız `+90` -> `0` dönüşümünü, gelen çağrıda (Inbound) tersine çevirmelisiniz ki içerdeki sistemler numarayı tanıyabilsin.

> [!TIP]
> **Dial Plan Search:** Karmaşık manipülasyon setlerinde hangi kuralın önce çalıştığını görmek için `Dial Plan Search` aracında "Call Details" kısmını inceleyin. Orada "Manipulation Applied" başlığı altında her iki bacakta yapılan değişiklikler listelenir.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


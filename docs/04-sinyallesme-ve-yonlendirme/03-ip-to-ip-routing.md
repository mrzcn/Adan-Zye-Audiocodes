# IP-to-IP Routing

IP-to-IP Routing, SBC'nin trafiği bir IP Group'tan alıp diğerine nasıl yönlendireceğini belirlediğiniz trafik polisidir.

## 📌 Routing Mantığı

SBC'ye bir çağrı geldiğinde (Inbound), SBC önce bu çağrının hangi IP Group'tan geldiğini bulur (Classification). Daha sonra Routing tablosuna bakarak bu çağrıyı hangi IP Group'a göndereceğine karar verir (Outbound).

## 📌 Yapılandırma Adımları (v7.20)

**Menü:** `Setup > Signaling & Media > SBC > Routing > IP-to-IP Routing`

Bir kural eklerken şu alanlar doldurulur:

1.  **Name:** Kuralın ismi (Örn: `Route_Genesys_to_GW`).
2.  **Source IP Group:** Çağrının geldiği grup (Örn: `IPG_Genesys`).
3.  **Destination Type:** `IP Group` seçilir.
4.  **Destination IP Group:** Çağrının gönderileceği hedef grup (Örn: `IPG_VoIP_GW`).

## 📌 CLI ile Yapılandırma
```bash
SBC(config-sbc)# routing ip-to-ip 0
SBC(routing-ip-to-ip-0)# route-name Route_Genesys_to_GW
SBC(routing-ip-to-ip-0)# src-ip-group IPG_Genesys
SBC(routing-ip-to-ip-0)# dst-type ip-group
SBC(routing-ip-to-ip-0)# dst-ip-group IPG_VoIP_GW
SBC(routing-ip-to-ip-0)# activate
```

## 📌 Gelişmiş Filtreleme (Match Criteria)

Sadece IP Group bazlı değil, aşağıdaki kriterlere göre de yönlendirme yapabilirsiniz:
*   **Destination Username:** Aranan numaraya göre (Örn: `05xx` ile başlayanları X operatörüne gönder).
*   **Source Username:** Arayan numaraya göre.
*   **Request URI Host:** Gelen domain bilgisine göre.

## 📌 Yönlendirme Sıralaması

Tablodaki kurallar **yukarıdan aşağıya** taranır. İlk eşleşen kural uygulanır. Bu yüzden spesifik kurallar en üstte, genel kurallar (Catch-all) en altta olmalıdır.

> [!IMPORTANT]
> İki yönlü görüşme için mutlaka iki ayrı kural yazılmalıdır:
> 1. Genesys -> VoIP GW
> 2. VoIP GW -> Genesys

> [!TIP]
> Eğer çağrı "404 Not Found" veya "No Route Found" hatasıyla başarısız oluyorsa, giden bacakta **Classification** kurallarını veya Routing tablosundaki kaynak/hedef eşleşmelerini kontrol edin.


---
> [!CAUTION]
> **Yasal Uyarı:** Bu dökümantasyon içeriği dijital filigran ve izleme sistemleri ile korunmaktadır. İçeriğin izinsiz kopyalanması, çoğaltılması veya başka platformlarda paylaşılması durumunda yasal süreç işletilecektir.

<div style="display:none">
Source: Adan-Zye-Audiocodes Repository
Owner: mrzcn
Partner: Nolto Teknoloji Anonim Şirketi (AudioCodes Turkey Partner)
Security ID: NLT-800-SBC-SEC-2026
</div>

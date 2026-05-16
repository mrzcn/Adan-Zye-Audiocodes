# Message Manipulation

Message Manipulation, SIP paketlerinin içindeki herhangi bir satırı (Başlık veya Gövde) kurallar dahilinde değiştirmenize, silmenize veya yeni satırlar eklemenize olanak tanıyan son derece güçlü bir araçtır.

## 📌 Ne Zaman Kullanılır?

*   **Interworking:** İki sistemin SIP başlıkları birbiriyle uyumsuz olduğunda (Örn: Bir taraf `From` başlığında isim beklerken diğer tarafın sadece numara göndermesi).
*   **Gizlilik:** Belirli başlıkların (Örn: `User-Agent`) silinmesi istendiğinde.
*   **Header Ekleme:** Karşı tarafa özel bir başlık (Örn: `X-Nolto-ID`) gönderilmesi gerektiğinde.

## 📌 Yapılandırma Adımları (v7.20)

**Menü:** `Setup > Signaling & Media > Message Manipulation > Message Manipulations`

Bir manipülasyon kuralı şu bileşenlerden oluşur:

1.  **Manipulation Set ID:** Kuralları gruplamak için kullanılır (Örn: 1, 2, 3...). Bu ID daha sonra IP Group'a bağlanır.
2.  **Message Type:** Hangi SIP mesajına müdahale edileceği (Örn: `Invite.Request`, `Any.Response`).
3.  **Condition:** (Opsiyonel) Kuralın hangi durumlarda çalışacağı (Örn: `Header.From.URL.User == '100'`).
4.  **Action Subject:** Hangi başlığın hedef alındığı (Örn: `Header.To.URL.Host`).
5.  **Action Type:** `Modify`, `Add`, `Remove` veya `Copy`.
6.  **Action Value:** Yeni değer (Örn: `'10.10.1.20'`).

## 📌 Örnek: From Başlığındaki Host Kısmını Değiştirme

Eğer giden çağrılarda From başlığına sabit bir IP yazmak isterseniz:
*   **Action Subject:** `Header.From.URL.Host`
*   **Action Type:** `Modify`
*   **Action Value:** `'192.168.1.10'`

## 📌 Kuralın Aktif Edilmesi

Oluşturduğunuz **Manipulation Set ID**'yi ilgili IP Group'un içine girerek **Inbound Message Manipulation Set** veya **Outbound Message Manipulation Set** alanına seçmelisiniz.

> [!IMPORTANT]
> Message Manipulation kuralları çok tehlikeli olabilir. Yanlış bir kural tüm SIP trafiğini bozabilir ve çağrıların düşmesine neden olabilir.

> [!TIP]
> Bir kuralın çalışıp çalışmadığını anlamanın en iyi yolu **Troubleshoot > Message Log** üzerinden giden paketi incelemektir. Değişiklik anında orada görünecektir.


---
> [!CAUTION]
> **Yasal Uyarı:** Bu dökümantasyon içeriği dijital filigran ve izleme sistemleri ile korunmaktadır. İçeriğin izinsiz kopyalanması, çoğaltılması veya başka platformlarda paylaşılması durumunda yasal süreç işletilecektir.

<div style="display:none">
Source: Adan-Zye-Audiocodes Repository
Owner: mrzcn
Partner: Nolto Teknoloji Anonim Şirketi (AudioCodes Turkey Partner)
Security ID: NLT-800-SBC-SEC-2026
</div>

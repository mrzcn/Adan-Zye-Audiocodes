# Regex (Düzenli İfadeler) Kütüphanesi

AudioCodes SBC üzerinde **Number Manipulation** yaparken en çok ihtiyaç duyacağınız Regex kalıpları ve kullanım örnekleri:

## 📌 Temel Karakterler
*   `^` : Satır başlangıcı.
*   `$` : Satır sonu.
*   `.` : Herhangi bir karakter.
*   `*` : 0 veya daha fazla tekrar.
*   `+` : 1 veya daha fazla tekrar.
*   `()` : Gruplama (Capture group).
*   `[0-9]` : Rakam aralığı.

## 📌 Sık Kullanılan Kalıplar

| Senaryo | Regex Kalıbı | Değiştirme (Replace) | Açıklama |
| :--- | :--- | :--- | :--- |
| **Başa 0 Ekleme** | `^(.*)$` | `0$1` | Gelen tüm numaraların başına '0' ekler. |
| **+90 Silme** | `^\+90(.*)$` | `$1` | Numara başında +90 varsa siler, kalanı bırakır. |
| **+90'ı 0'a Çevirme** | `^\+90(.*)$` | `0$1` | +90 ile başlayan numarayı 0 ile başlayan formata sokar. |
| **Hane Silme** | `^0212(.*)$` | `$1` | Alan kodunu (0212) silerek sadece lokal numarayı bırakır. |
| **Numara Maskeleme** | `^([0-9]{7})([0-9]{4})$` | `$1XXXX` | Numaranın son 4 hanesini 'X' ile gizler. |
| **Sadece 10 Hane İzni** | `^[0-9]{10}$` | - | Sadece tam 10 haneli numaraların geçmesine izin verir. |
| **Özel Prefix Ekleme** | `^([5][0-9]{9})$` | `90$1` | 5 ile başlayan 10 haneli numaraların başına 90 ekler. |

## 📌 Gruplama Mantığı ($1, $2)

Regex içinde parantez `()` kullandığınızda, AudioCodes bu grupları hafızaya alır:
*   `^([0-9]{3})([0-9]{7})$`
    *   `$1` : İlk 3 hane (Örn: 212)
    *   `$2` : Sonraki 7 hane (Örn: 1234567)

Değiştirme kısmına `$2$1` yazarsanız numara `1234567212` halini alır.

> [!TIP]
> AudioCodes'ta Regex yazarken büyük/küçük harf duyarlılığına ve boşluk bırakmamaya dikkat edin. Test etmek için cihazın **Troubleshoot > Test Tools > Dial Plan Search** aracını kullanabilirsiniz.

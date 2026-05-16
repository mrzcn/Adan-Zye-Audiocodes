# SIP Terimler Sözlüğü

AudioCodes SBC dünyasında sıkça karşılaşacağınız teknik terimlerin detaylı açıklamaları:

*   **SIP (Session Initiation Protocol):** Oturum başlatma protokolü. Telefonun çalması, kimin aradığı ve çağrının sonlandırılması gibi sinyalleşme işlemlerini yönetir.
*   **RTP (Real-time Transport Protocol):** Gerçek zamanlı taşıma protokolü. SIP bir çağrıyı kurduktan sonra, ses verisinin (medya) taşındığı asıl kanaldır.
*   **B2BUA (Back-to-Back User Agent):** SBC'nin çalışma mimarisidir. SBC, bir tarafa karşı "alıcı" (User Agent Server), diğer tarafa karşı "arayıcı" (User Agent Client) gibi davranarak çağrıyı iki ayrı bacak halinde yönetir.
*   **Codec (Coder-Decoder):** Sesin dijitalleşme algoritması. (Örn: G.711, G.729).
*   **Transcoding:** Bir codec türünden diğerine (Örn: G.711'den G.729'a) anlık ses dönüşümü yapılması.
*   **Jitter:** Ses paketlerinin varış süreleri arasındaki düzensizlik. Seste kopmalara ve robotikleşmeye neden olur.
*   **MOS (Mean Opinion Score):** Ses kalitesini 1-5 arasında puanlayan standart. 4.0 ve üzeri "mükemmel" kabul edilir.
*   **Latency (Gecikme):** Sesin bir uçtan diğer uca gitme süresi. 150ms üzeri gecikmeler konuşma konforunu bozar.
*   **NAT Traversal:** Özel IP ağındaki bir cihazın, internet üzerindeki bir cihazla ses trafiğini yürütebilmesi için IP/Port eşleşmelerinin SBC tarafından yönetilmesi.
*   **SDP (Session Description Protocol):** SIP paketinin içinde bulunan ve hangi IP/Port/Codec üzerinden ses gönderileceğini belirten "pazarlık" metni.
*   **Keep-Alive (OPTIONS):** Sunucunun ayakta olup olmadığını kontrol etmek için gönderilen periyodik SIP mesajları.
*   **FQDN (Fully Qualified Domain Name):** Bir sunucunun tam adı (Örn: `sbc.nolto.com`).
*   **SRTP (Secure RTP):** Ses verisinin AES algoritması ile şifrelenmiş halidir.
*   **TLS (Transport Layer Security):** SIP sinyalleşmesinin şifrelenmesi için kullanılan protokol.
*   **Diversion Header:** Çağrı yönlendirme bilgisini taşıyan SIP başlığı.
*   **P-Asserted-Identity (PAI):** Arayan kişinin kimliğinin doğrulandığını belirten SIP başlığı.

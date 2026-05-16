# Faks (T.38) Yapılandırması

IP ağları üzerinden faks gönderimi (FoIP), paket gecikmelerine karşı çok hassastır. AudioCodes SBC'de faks trafiğini başarılı bir şekilde yönetmek için temel kavramlar:

## 📌 Faks İletim Modları

1.  **T.38 (Relay):** En güvenilir yöntemdir. Faks sinyalini yakalar, dijital paketlere dönüştürür ve karşı tarafta tekrar faks sinyaline çevirir. Paket kayıplarına karşı dayanıklıdır.
2.  **G.711 Pass-through:** Faks sesini normal bir insan sesiymiş gibi G.711 codec ile taşır. Çok kaliteli bir network gerektirir.

## 📌 Yapılandırma Adımları

**Menü:** `Setup > Signaling & Media > Coders & Profiles > IP Profiles`

1.  **Fax Transport Mode:** `T.38 Relay` olarak seçilmelidir.
2.  **V.34 Fax Transfer:** Eğer modern hızlı faks makineleri kullanılıyorsa `Enable` yapılmalıdır.
3.  **Fax Error Correction Mode (ECM):** Hatalı paketlerin tekrar gönderilmesi için `Enable` önerilir.

## 📌 Sık Karşılaşılan Sorunlar ve Çözümler

*   **Faks Başlıyor Ama Yarıda Kesiliyor:** Network üzerindeki Jitter değerini kontrol edin. IP Profile içindeki **Jitter Buffer** ayarlarını `Dynamic` yapın.
*   **Hiç Faks Gitmiyor:** Karşı tarafın (Operatör veya Gateway) T.38 destekleyip desteklemediğini Message Log üzerinden (re-INVITE paketlerine bakarak) teyit edin.
*   **Faks Sinyali Alınamıyor:** Cihaz üzerindeki **Fax Modem Transport Mode** ayarının `T.38` olduğundan emin olun.

## 📌 CLI ile Faks Ayarı
```bash
SBC(config-voip)# ip-profile 1
SBC(ip-profile-1)# fax-modem-transport-mode t38-relay
SBC(ip-profile-1)# activate
```

> [!TIP]
> Eğer T.38 ile sorun yaşıyorsanız, geçici bir çözüm olarak her iki uçta da `G.711 Pass-through` modunu deneyebilirsiniz. Bu modda codec her zaman G.711 olmalı ve VAD (Voice Activity Detection) kapalı olmalıdır.

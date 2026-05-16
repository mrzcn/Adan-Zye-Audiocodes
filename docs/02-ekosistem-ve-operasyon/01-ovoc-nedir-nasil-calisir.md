# OVOC (One Voice Operations Center) Nedir?

Bir şirketin sadece 1 tane SBC'si varken onu yönetmek kolaydır. Peki ya 50 farklı şubesinde 50 tane SBC'si varsa? İşte burada devreye AudioCodes'un merkezi yönetim ve izleme platformu olan **OVOC** girer.

## 📌 OVOC Nedir?

OVOC, tüm AudioCodes ekosistemini (SBC'ler, Gateway'ler, IP Telefonlar) tek bir merkezden yönetmenizi, izlemenizi ve sorun gidermenizi sağlayan bir "Şemsiye" yazılımdır.

## 📌 Temel Özellikleri

1.  **Merkezi Yönetim (Configuration Management):**
    *   Tüm cihazlara aynı anda firmware yükleyebilir veya konfigürasyon dosyası (INI) gönderebilirsiniz.
    *   Sıfır kutudan çıkan bir cihazı (Zero Touch Provisioning), sadece internete bağlayarak OVOC üzerinden otomatik yapılandırabilirsiniz.
2.  **Kalite İzleme (Quality of Experience - QoE):**
    *   Yapılan her çağrının ses kalitesini (MOS skoru, Jitter, Gecikme) anlık izler.
    *   "Dün saat 14:00'te Ahmet Bey'in çağrısı neden cızırtılıydı?" sorusuna grafiklerle yanıt verir.
3.  **Alarm ve Bildirimler:**
    *   Bir Proxy Set çöktüğünde veya bir cihaz internetten düştüğünde size anında e-posta veya SNMP uyarısı gönderir.
4.  **Cihaz Envanteri:**
    *   Hangi cihazda hangi firmware var, lisans süresi ne zaman bitiyor gibi bilgileri tek ekranda listeler.

## 📌 Nasıl Çalışır?

OVOC genellikle bir sanal sunucuya (Linux tabanlı) kurulur. Sahadaki SBC'ler, HTTP/HTTPS üzerinden OVOC'ye "kalp atışı" (Keep-alive) ve log verilerini gönderirler.

## 📌 Neden Gereklidir?

Yeni mezun bir mühendis için OVOC kullanmak, "Reactive" (Sorun çıkınca müdahale eden) yapıdan "Proactive" (Sorun çıkmadan önlem alan) yapıya geçmek demektir. Büyük ölçekli AudioCodes projelerinin vazgeçilmez bir parçasıdır.

> [!TIP]
> OVOC arayüzü modern ve web tabanlıdır. Dashboard üzerindeki "World Map" (Dünya Haritası) özelliği ile global bir şirketin tüm şubelerindeki ses sağlığını anlık olarak görebilirsiniz.

> [!IMPORTANT]
> OVOC'un kendisi de lisanslı bir üründür. Yönetilecek cihaz sayısına ve istenen özelliklere göre lisanslanır.

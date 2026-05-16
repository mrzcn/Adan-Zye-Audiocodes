# Güvenlik, TLS ve Sertifika Yönetimi

SBC'nin en önemli görevlerinden biri ses altyapısını dış saldırılara karşı korumaktır. Bu bölümde temel güvenlik önlemlerini ve şifreli sinyalleşmeyi (TLS) inceleyeceğiz.

## 📌 Temel Güvenlik Sıkılaştırması

İnternete açık bir SBC saniyeler içinde SIP tarama botlarının (Örn: SIP Vicious) hedefi haline gelir.

### 1. Unregistered Calls Kısıtlaması
**Menü:** `Setup > Signaling & Media > SBC > SBC General Settings`
*   **Unregistered Calls:** Bu ayarı `Restrict` yapın. Böylece sadece Proxy Set'lerinizde IP'si kayıtlı olan güvenilir sunuculardan gelen çağrılar kabul edilir.

### 2. IP Group Bazlı Filtreleme
Gelen her çağrı mutlaka bir **Classification** kuralına çarpar. Eğer gelen çağrının kaynak IP'si hiçbir IP Group ile eşleşmiyorsa, SBC çağrıyı reddeder.

## 📌 TLS (Transport Layer Security) ve Sertifikalar

Genesys veya bazı modern operatörler SIP sinyalleşmesinin şifreli (TLS - Port 5061) olmasını isteyebilir.

### 1. Sertifika Yükleme
**Menü:** `Setup > Device > Security > TLS Contexts`
*   AudioCodes'un dış dünya ile güvenli konuşabilmesi için bir **Server Certificate**'e ihtiyacı vardır.
*   Genellikle bir **CSR (Certificate Signing Request)** oluşturulur, bir sertifika otoritesine imzalatılır ve geri yüklenir.

### 2. SIP Interface Yapılandırması
*   `Setup > Signaling & Media > Core > SIP Interfaces` menüsünden ilgili bacak için protokol `TLS` ve port `5061` olarak ayarlanır.
*   **TLS Context:** Oluşturduğunuz sertifika grubu burada seçilir.

### 3. Şifreleme Simetrisi (Media Security Symmetry)
AudioCodes v7.20'de medyanın şifreli olup olmayacağı bacak bazlı belirlenir.
*   **Symmetric:** Bir taraftan SRTP (şifreli) geliyorsa diğer tarafa da SRTP gönderilir.
*   **Prefer:** Mümkünse şifreli, değilse şeffaf.
*   **Force:** Mutlaka şifreli olmalı, yoksa çağrıyı düşür.

## 📌 TLS 1.3 ve Modern Şifreleme
v7.20 sürümünün son yamaları ile birlikte TLS 1.3 desteği gelmiştir. Güvenlik için `TLS Context` ayarlarında **Minimum TLS Version** değerini `TLS 1.2` veya `TLS 1.3` olarak set etmeniz, eski ve güvensiz (SSLv3, TLS 1.0) protokollerin kullanılmasını engeller.

## 📌 DoS ve IDS Koruması

**Menü:** `Setup > Device > Security > IDS Rules`
*   SBC, belirli bir IP'den çok kısa sürede çok fazla hatalı INVITE gelirse o IP'yi otomatik olarak bloklayabilir (Blacklist).

> [!CAUTION]
> Sertifika süresi dolduğunda TLS bacağı anında çöker ve çağrılar kesilir. Sertifika geçerlilik tarihlerini mutlaka bir takvime not edin.

> [!TIP]
> Test aşamasında sertifika hatalarını (Self-signed certificate vb.) göz ardı etmek için TLS Context ayarlarında **Verify Remote Certificate** seçeneğini `No` yapabilirsiniz. Ancak canlı ortamda güvenlik için bu `Yes` olmalıdır.

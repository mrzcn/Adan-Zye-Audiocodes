# İlk Erişim ve Yönetim

Yeni bir AudioCodes cihazını kutusundan çıkardığınızda veya fabrika ayarlarına döndürdüğünüzde yönetime başlamak için izlemeniz gereken standart adımlar mevcuttur.

## 📌 Fabrika Varsayılan Ayarları

AudioCodes cihazları genellikle aşağıdaki varsayılan ağ ayarlarıyla gelir:

*   **Default IP Adresi:** `192.168.0.2`
*   **Subnet Mask:** `255.255.255.0`
*   **Default Gateway:** `0.0.0.0`
*   **Kullanıcı Adı:** `Admin` (Büyük 'A' harfi ile)
*   **Şifre:** `Admin` (Büyük 'A' harfi ile)

## 📌 Cihaza İlk Bağlantı

1.  Bilgisayarınızın Ethernet kartına manuel olarak `192.168.0.x` bloğundan bir IP verin (Örn: `192.168.0.10`).
2.  Bilgisayarınızı cihazın **LAN** veya **OAMP** portuna bağlayın.
3.  Tarayıcınızdan `http://192.168.0.2` adresine gidin.
4.  Varsayılan kullanıcı bilgileri ile giriş yapın.

## 📌 Web Arayüzü (GUI) Yapısı

AudioCodes v7.20 arayüzü üç ana bölüme ayrılmıştır:

1.  **Setup (Kurulum):** Cihazın tüm konfigürasyonunun (Network, SIP, SBC) yapıldığı ana bölümdür.
2.  **Monitor (İzleme):** Aktif çağrılar, Proxy Set durumları ve istatistiklerin görüldüğü bölümdür.
3.  **Troubleshoot (Sorun Giderme):** Syslog, Message Log ve test araçlarının bulunduğu bölümdür.

## 📌 Temel Yönetim Araçları

*   **Web GUI:** En yaygın kullanılan grafik arayüzdür.
*   **CLI (Command Line Interface):** SSH veya Konsol portu üzerinden erişilir. Toplu ayarlar ve otomasyon için uygundur.
*   **INI Dosyası:** Cihazın tüm konfigürasyonu tek bir metin dosyasında (`config.ini`) saklanır. Bu dosyayı bilgisayarınıza indirip düzenleyebilir ve tekrar cihaza yükleyebilirsiniz.
*   **OVOC (One Voice Operations Center):** AudioCodes'un merkezi yönetim yazılımıdır. Çok sayıda cihazı tek bir merkezden izlemek ve yönetmek için kullanılır.

> [!CAUTION]
> Yapılandırmada yaptığınız değişikliklerin cihaz yeniden başladığında kaybolmaması için mutlaka sağ üst köşedeki **"Burn"** butonuna tıklayarak ayarları kalıcı hafızaya kaydetmelisiniz.

> [!TIP]
> Şifreleri değiştirmek için **Setup > Device > Web & CLI User Accounts** menüsünü kullanabilirsiniz. Güvenlik için varsayılan `Admin` şifresini ilk kurulumda mutlaka değiştirin.

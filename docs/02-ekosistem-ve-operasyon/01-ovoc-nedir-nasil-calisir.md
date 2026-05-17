<!-- 
  _   _       _ _             _    ____  
 | \ | | ___ | | |_ ___      / \  / ___| 
 |  \| |/ _ \| | __/ _ \    / _ \ \___ \ 
 | |\  | (_) | | || (_) |  / ___ \ ___) |
 |_| \_|\___/|_|\__\___/  /_/   \_\____/ 
 AudioCodes Partner Training - mrzcn 2026
-->

# OVOC (One Voice Operations Center) Nedir?

Bir şirketin sadece 1 tane SBC'si varken onu yönetmek kolaydır. Peki ya 50 farklı şubesinde 50 tane SBC'si varsa? İşte burada devreye AudioCodes'un merkezi yönetim ve izleme platformu olan **OVOC** girer.

## 📌 OVOC Nedir?

OVOC, tüm AudioCodes ekosistemini (SBC'ler, Gateway'ler, IP Telefonlar) tek bir merkezden yönetmenizi, izlemenizi ve sorun gidermenizi sağlayan bir "Şemsiye" yazılımdır.

## 📌 Temel Özellikleri ve Operasyonel Faydaları

1.  **Configuration Management ve Zero Touch Provisioning (ZTP):**
    *   Yüzlerce cihaza aynı anda firmware paketi gönderebilir veya yedeklerini tek tıkla alabilirsiniz.
    *   **ZTP:** Sahaya gönderilen kutusundan yeni çıkmış bir cihaz, internete bağlandığı an otomatik olarak OVOC'a ulaşır. Önceden hazırladığınız şablon (Template) anında cihaza itilir ve mühendis sahaya gitmeden cihaz devreye alınır.
2.  **Topology View ve Cihaz Envanteri:**
    *   Ağınızdaki tüm cihazları (SBC, Gateway, IP Telefon) bir topoloji haritası üzerinde görselleştirir. Hangi cihazın hangi firmware sürümünde olduğunu, lisans kapasitelerinin yüzde kaçının dolduğunu canlı renklerle (Yeşil/Kırmızı) takip edersiniz.
3.  **Kalite İzleme (Quality of Experience - QoE):**
    *   OVOC, uç noktalardan gelen RTCP-XR verilerini işler. "Dün saat 14:00'te Ahmet Bey'in çağrısı neden cızırtılıydı?" sorusunu analiz ederek; sorunun Jitter'dan mı, ISP kaynaklı bir paket kaybından mı yoksa DSP yetersizliğinden mi kaynaklandığını bulur.
4.  **Alarm Yönetimi ve Northbound Entegrasyonu:**
    *   Cihazlardan gelen SNMP Trap'leri (Örn: "HA Failover oldu", "Ethernet portu düştü") okur. Bu hataları e-posta ile IT ekibine iletir. Ayrıca OVOC, verileri üst katmandaki kurumun ana izleme sistemine (Örn: SolarWinds, Zabbix) Northbound API ile paslayabilir.

## 📌 Nasıl Çalışır?

OVOC genellikle bir sanal sunucuya (Linux tabanlı) kurulur. Sahadaki SBC'ler, HTTP/HTTPS üzerinden OVOC'ye "kalp atışı" (Keep-alive) ve log verilerini gönderirler.

## 📌 Neden Gereklidir?

Yeni mezun bir mühendis için OVOC kullanmak, "Reactive" (Sorun çıkınca müdahale eden) yapıdan "Proactive" (Sorun çıkmadan önlem alan) yapıya geçmek demektir. Büyük ölçekli AudioCodes projelerinin vazgeçilmez bir parçasıdır.

> [!TIP]
> OVOC arayüzü modern ve web tabanlıdır. Dashboard üzerindeki "World Map" (Dünya Haritası) özelliği ile global bir şirketin tüm şubelerindeki ses sağlığını anlık olarak görebilirsiniz.

> [!IMPORTANT]
> OVOC'un kendisi de lisanslı bir üründür. Yönetilecek cihaz sayısına ve istenen özelliklere göre lisanslanır.


---
<p align="center">
  <small>Ref: NLT-800-SBC-2026 | mrzcn © 2026</small>
</p>
<div style="opacity: 0; font-size: 1px;">m‌r‌z‌c‌n‌-‌n‌o‌l‌t‌o‌-‌a‌u‌d‌i‌o‌c‌o‌d‌e‌s‌-‌t‌r‌a‌i‌n‌i‌n‌g‌-‌2‌0‌2‌6‌</div>


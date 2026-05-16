# Media Realms

Media Realms, ses (RTP) trafiğinin hangi IP bacağından akacağını ve hangi port aralıklarını kullanacağını belirleyen mantıksal bölümlerdir. 

### Yeni Mezunlar İçin Mantık
Bir SBC'ye hem internetten hem de yerel ağdan ses geliyorsa, SBC bu iki sesi birbirinden nasıl ayırır? İşte Media Realm burada devreye girer. Bir ses bacağını LAN IP Interface'ine, diğerini WAN IP Interface'ine bağlayarak sesin yollarının karışmasını engeller.

## 📌 Media Realm Neden Gereklidir?

SBC üzerinde birden fazla ağ bacağı olduğunda, cihazın hangi bacağa hangi UDP portlarını ayıracağını bilmesi gerekir. Media Realm sayesinde:
1.  **Güvenlik:** RTP portları sadece ilgili ağa açılır.
2.  **Yönetim:** Farklı bacaklar için farklı port aralıkları (Örn: LAN için 6000-6999, WAN için 7000-7999) belirlenebilir.
3.  **İzolasyon:** Her Media Realm kendine ait bir IP arayüzüne bağlanır.

## 📌 Yapılandırma Adımları (v7.20)

**Menü:** `Setup > Signaling & Media > Core > Media Realms`

Yeni bir Media Realm eklerken şu parametreler girilir:

1.  **Name:** Anlamlı bir isim (Örn: `MR_LAN`, `MR_Operator`).
2.  **IPv4 Interface Name:** Bu medyanın hangi IP arayüzü üzerinden akacağı seçilir. (Örn: `Inside_IF`).
3.  **Port Range Start:** Başlangıç portu (Genellikle `6000`'den başlar).
4.  **Number of Media Session Legs:** Bu realm üzerinden geçecek maksimum eş zamanlı ses bacağı sayısı. (Lisans kapasitesine göre belirlenir).

## 📌 Media Anchoring (Medya Demirleme)

AudioCodes SBC varsayılan olarak medyanın kendi üzerinden geçmesini sağlar. SIP sinyalleşmesi sırasında SBC, SDP paketindeki uç noktanın IP'sini siler ve yerine Media Realm'de tanımlanan IP arayüzünü ve boş bir RTP portunu yazar. Bu sayede ses akışı her zaman SBC üzerinden geçer.

> [!TIP]
> Ses gitmiyor veya gelmiyorsa (No Audio), ilk kontrol etmeniz gereken yer Media Realm'deki **IP Interface** eşleşmesidir. Eğer yanlış arayüz seçilirse, SBC sesi yanlış bacağa göndermeye çalışır.

> [!NOTE]
> RTP port aralıklarının her zaman **çift sayı** (Örn: 6000, 6002...) üzerinden ilerlediğini unutmayın. Her ses görüşmesi bir RTP (ses taşıma) ve bir RTCP (kontrol) portu kullanır.

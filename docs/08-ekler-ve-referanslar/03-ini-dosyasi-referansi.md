# INI Dosyası ve CLI Referansı

AudioCodes SBC konfigürasyonu, arka planda bir metin dosyası olan `BOARD.ini` üzerinde tutulur. Bu dosyayı veya CLI'yı (SSH) kullanarak toplu işlem yapabilirsiniz.

## 📌 Temel CLI Komutları (v7.20)

SSH üzerinden bağlandığınızda en çok kullanacağınız komutlar:

| Komut | Açıklama |
| :--- | :--- |
| `show status` | Cihazın genel durumunu gösterir. |
| `conf t` | Yapılandırma moduna girer. |
| `write` | Yapılan değişiklikleri kalıcı hafızaya yazar (Save). |
| `show voip status` | Aktif çağrıları ve SIP durumunu gösterir. |
| `reboot` | Cihazı yeniden başlatır. |
| `get config` | Mevcut konfigürasyonu ekrana basar. |

## 📌 Örnek INI Blokları

Yapılandırmayı INI dosyası ile yapmak isterseniz şu formatı kullanmalısınız:

### IP Interface Ekleme
```ini
[ InterfaceTable ]
FORMAT InterfaceTable_Index = InterfaceTable_InterfaceName, InterfaceTable_IPAddress, InterfaceTable_PrefixLength, InterfaceTable_Gateway, InterfaceTable_VlanID, InterfaceTable_InterfaceMode;
InterfaceTable 0 = "Inside_IF", 192.168.1.10, 24, 192.168.1.1, 10, 10;
[\InterfaceTable]
```

### Proxy Set Ekleme
```ini
[ ProxySet ]
FORMAT ProxySet_Index = ProxySet_ProxySetName, ProxySet_SbcIPv4SipInterfaceName, ProxySet_ProxyKeepAliveMode;
ProxySet 1 = "Genesys_Proxy", "Inside_IF", 1;
[\ProxySet]
```

## 📌 CLI ile Yapılandırma Örneği

SSH üzerinden bir IP Group oluşturma adımları:
```bash
SBC# configure voip
SBC(config-voip)# sbc
SBC(config-sbc)# ip-group 1
SBC(ip-group-1)# name IPG_Genesys
SBC(ip-group-1)# proxy-set 1
SBC(ip-group-1)# sip-interface 1
SBC(ip-group-1)# activate
SBC(ip-group-1)# exit
SBC(config-sbc)# exit
SBC(config-voip)# exit
SBC# write
```

> [!IMPORTANT]
> INI dosyası üzerinde manuel değişiklik yapmak risklidir. Bir sütun hatası tüm tabloyu bozabilir. Her zaman değişiklik öncesi çalışan bir yedek bulundurun.

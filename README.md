# AmazonJP_Scraper
日本版Amazonを指定した商品の検索結果を多重リストで、「商品名」「値段」「URL」「画像」の四つを出力します。

# 使用方法

Amazon_Scraperを指定し、引数で検索したいキーワードを指定して実行すると結果を返します。

実行例↓
py "Amazon_Scraper.py" ゲーミングキーボードLogicool

出力↓
[('Logicool G ゲーミングキーボード 有線 G512 GXスイッチ クリッキー メカニカルキーボード 日本語配列 LIGHTSYNC RGB G512-CK 国内正規品', '￥11,900', 'https://www.amazon.co.jp/dp/B07DLQ38PW', 'https://m.media-amazon.com/images/I/51y8-ho0rQL._AC_UL320_.jpg'), ('Logicool G ゲーミングキーボード 有線 G910r タクタイル メカニカルキーボード 日本語配列 LIGHTSYNC RGB パ ームレスト G910 Spectrum 国内正規品', '￥13,100', 'https://www.amazon.co.jp/dp/B01MQ4RNBH', 'https://m.media-amazon.com/images/I/61Vajr8NjLL._AC_UL320_.jpg'), ('Logicool G テンキーレス ゲーミングキーボード 無線 G913 GLスイッチ タクタイル 日本語配列 LIGHTSPEED ワイヤレス Bluetooth LIGHTSYNC RGB G913-TKL-TCBK 国内正規品', '￥27,500', 'https://www.amazon.co.jp/dp/B088BS3YY4', 'https://m.media-amazon.com/images/I/61msA-lwCPL._AC_UL320_.jpg'), ('Logicool G ゲーミングキーボード 有 線 G213 パームレスト 日本語配列 メンブレン キーボード 静音  LIGHTSYNC RGB  国内正規品', '￥6,182', 'https://www.amazon.co.jp/dp/B01LYI06RT', 'https://m.media-amazon.com/images/I/51mY-UeIncL._AC_UL320_.jpg'), ('Logicool G PRO X ゲーミングキ ーボード テンキーレス 有線 GXスイッチ クリッキー 日本語配列 LIGHTSYNC RGB 着脱式ケーブル G-PKB-002 国内正規品', '￥12,700', 'https://www.amazon.co.jp/dp/B07YWXDP8W', 'https://m.media-amazon.com/images/I/51xGLSmJ0eL._AC_UL320_.jpg'), ('Razer BlackWidow Lite JP Mercury White メカニカルキーボード 静音 オレンジ軸 テンキーレス 日本語配列 【日本正規代理店保証品】 RZ03-02640800-R3J1', '￥12,980', 'https://www.amazon.co.jp/dp/B086Z1FXLK', 'https://m.media-amazon.com/images/I/61PmF-ypRCL._AC_UL320_.jpg'), ('Logicool G テンキーレス ゲーミングキーボード 無線 G913 GLスイッチ クリッキー 日本語配列 LIGHTSPEED ワイヤレス Bluetooth LIGHTSYNC RGB G913-TKL-CKBK 国内正規品', '￥27,500', 'https://www.amazon.co.jp/dp/B088BYC54C', 'https://m.media-amazon.com/images/I/61msA-lwCPL._AC_UL320_.jpg'), ('Logicool G ゲーミングキーボード 有線 G213 パームレスト 日本語配列 メンブレン キーボード 静音  LIGHTSYNC RGB  国内正規品', '￥6,182', 'https://www.amazon.co.jp/dp/B01LYI06RT', 'https://m.media-amazon.com/images/I/51mY-UeIncL._AC_UL320_.jpg'), ('Logicool G ゲーミングキーボード テンキーレス G-PKB-001 ブラック メカニカルキーボード タクタイル 日本語配列 RGB 着脱式ケーブル  G Pro  国内正規品 2年間メーカー保証', '￥29,000', 'https://www.amazon.co.jp/dp/B06XHGP2TT', 'https://m.media-amazon.com/images/I/61CiVFFeh0L._AC_UL320_.jpg'), ('Logicool G ゲーミングキーボード 有線 G512 GXスイッチ クリッキー メカニカルキーボード 日本語配列 LIGHTSYNC RGB G512-CK 国内正規品', '￥11,900', 'https://www.amazon.co.jp/dp/B07DLQ38PW', 'https://m.media-amazon.com/images/I/51y8-ho0rQL._AC_UL320_.jpg'), ('Logicool G ゲーミングキーボード 有線 G910r タクタイル メカニカルキーボード 日本語配列 LIGHTSYNC RGB パームレスト G910 Spectrum 国内正規品', '￥13,100', 'https://www.amazon.co.jp/dp/B01MQ4RNBH', 'https://m.media-amazon.com/images/I/61Vajr8NjLL._AC_UL320_.jpg'), ('Logicool G ゲーミングキーボード 有線 G610BL 日本語配列 青軸 メカニカルキーボード 専用メディアコントロール カスタムボタンマクロ 国内正規品', '￥9,800', 'https://www.amazon.co.jp/dp/B01H4ZRBAU', 'https://m.media-amazon.com/images/I/51pt-oNJ7zL._AC_UL320_.jpg'), ('Logicool G ゲーミングキーボード 有線 G813 GLスイッチ リニア  メカニカルキーボード 静音 日本語配列 LIGHTSYNC RGB USBパススルー G813-LN 国内正規品', '￥17,809', 'https://www.amazon.co.jp/dp/B07VVJ9PQN', 'https://m.media-amazon.com/images/I/51lORh8fIhL._AC_UL320_.jpg'), ('Logicool G ゲーミングキーボード 無線 G613 LIGHTSPEED ワイヤレス Bluetooth接続対応 タクタイル メカニカルキーボード 日本語配列 パームレスト 国内正規品', '￥8,588', 'https://www.amazon.co.jp/dp/B0752BLYZN', 'https://m.media-amazon.com/images/I/515PrFFjGwL._AC_UL320_.jpg'), ('HyperX Alloy FPS Pro ゲーミングキーボード 赤軸 テンキーレス FPSゲーム向け LEDバックライト 2年保証 HX-KB4RD1-US/R1', ' ￥12,785', 'https://www.amazon.co.jp/dp/B074F5L8GQ', 'https://m.media-amazon.com/images/I/71B9lOrwqVL._AC_UL320_.jpg'), ('Logicool G ゲーミングマウス 有線 G203 LIGHTSYNC RGB 6個プログラムボタン 85g軽量 G203-BK 国内正規品', '￥3,608', 'https://www.amazon.co.jp/dp/B087BTXHX4', 'https://m.media-amazon.com/images/I/61eElLlfVDL._AC_UL320_.jpg'), ('Logicool G ゲーミングマウスパット G240t クロス表面 標準サイズ 国内正規品', '￥1,418', 'https://www.amazon.co.jp/dp/B01D45U732', 'https://m.media-amazon.com/images/I/41JLX9NhTyL._AC_UL320_.jpg'), ('NPET ゲーミングキーボード LED バックライト 7色 防水 usb 26キー防衝突 キーボード 角度調節可能 2年間無償品質保証 キーキャッププーラー付き K10 更新版 (日本語配列(106キー))', '￥2,099', 'https://www.amazon.co.jp/dp/B075WQYC4Y', 'https://m.media-amazon.com/images/I/71-pI+DouiL._AC_UL320_.jpg'), ('【日 本語配列】HyperX Alloy Origins Core RGB メカニカルゲーミングキーボード テンキーレス HyperXスイッチ ゲーマー向け 2年保証 HX-KB7RDX-JP', '￥11,980', 'https://www.amazon.co.jp/dp/B081VR349C', 'https://m.media-amazon.com/images/I/71QSt58mwfL._AC_UL320_.jpg'), ('Logicool G ゲーミングマウス 有線 G300Sr 左右対称 軽量 プログラムボタン9個 高精度dpi 国内正規品', '￥2,400', 'https://www.amazon.co.jp/dp/B07HYR7PNP', 'https://m.media-amazon.com/images/I/518L57F5ZUL._AC_UL320_.jpg'), ('Logicool G ゲーミングキーボード G512-TC ブラック メカニカルキーボード タクタイル 日本語配列 LIGHTSYNC RGB 静音 G512 Carbon 国内正規品 2年間メーカー保証', '￥13,300', 'https://www.amazon.co.jp/dp/B07CL42YK6', 'https://m.media-amazon.com/images/I/61Uy0UakY6L._AC_UL320_.jpg'), ('Logicool G ゲーミングマウス GPRO ワイヤレス FPS向け 80g 軽量 左右対称 HEROセンサー POWERPLAY無線充電対応 LIGHTSYNC RGB G-PPD-002WLr 国内正規品 2年間メーカー保証 ブラック', '￥16,800', 'https://www.amazon.co.jp/dp/B08CKZNCPP', 'https://m.media-amazon.com/images/I/41yHprHE16L._AC_UL320_.jpg'), ('Logicool G ゲーミングヘッドセット ワイヤレス 無線 G933s Dolby 7.1ch 3.5mm usb LIGHTSYNC ノイズキャンセリング 単一性 折り畳み式マイク PC/PS4/Switch/スマホ 国内正規品', '￥13,300', 'https://www.amazon.co.jp/dp/B07NDNWBD8', 'https://m.media-amazon.com/images/I/61x-rjxe8aL._AC_UL320_.jpg'), ('Logicool G ゲーミングマウス 無線 G502 HEROセンサー LIGHTSPEED ワイヤレス 11個プログラムボタン LIGHTSYNC RGB POWERPLAY ワイヤレス充電 G502WL 国内正規品', '￥14,900', 'https://www.amazon.co.jp/dp/B07RR94VQT', 'https://m.media-amazon.com/images/I/51wEAqspqTL._AC_UL320_.jpg'), ('Logicool G ゲーミングキーボード 有線 G610BL 日本語配列 青軸 メカ ニカルキーボード 専用メディアコントロール カスタムボタンマクロ 国内正規品', '￥9,800', 'https://www.amazon.co.jp/dp/B01H4ZRBAU', 'https://m.media-amazon.com/images/I/51pt-oNJ7zL._AC_UL320_.jpg'), ('Logicool G ゲーミングキーボード 無線 G613 LIGHTSPEED ワイヤレス Bluetooth接続対応 タクタイル メカニカルキーボード 日本語配列 パームレスト 国内正規品', '￥8,588', 'https://www.amazon.co.jp/dp/B0752BLYZN', 'https://m.media-amazon.com/images/I/515PrFFjGwL._AC_UL320_.jpg'), ('Logicool G ゲーミングキーボード 無線 G913 GLスイッチ リニア メカニカルキーボード 静音 日本語配列 LIGHTSPEED ワイヤレス Bluetooth 接続対応 LIGHTSYNC RGB G913-LN 国内正規品', '￥28,000', 'https://www.amazon.co.jp/dp/B07VXNR2H8', 'https://m.media-amazon.com/images/I/51wbdbcS45L._AC_UL320_.jpg'), ('Logicool G ゲーミングマウス 無線 G304 HEROセンサー LIGHTSPEED ワイヤレス 99g軽量 G304rWH 国内正規品', '￥3,827', 'https://www.amazon.co.jp/dp/B07D3GRQC8', 'https://m.media-amazon.com/images/I/41mKpFIRAZL._AC_UL320_.jpg'), ('Logicool G ゲーミングキーボード G413rSV シルバー メカニカルキーボード タクタイル 日本語配列 USBパススルー G413 国内正規品 2年間メーカー保証', '￥10,900', 'https://www.amazon.co.jp/dp/B072DWJ848', 'https://m.media-amazon.com/images/I/6185UYxegDL._AC_UL320_.jpg'), ('ゲーミングキーボード 有線 106キー日本語配列 25キー防衝突 PC用キ ーボード\xa0LED バックライト防水 仕事用/ゲーム用 防水仕様\u3000Windows/Mac OS対応\u300012ヶ月間品質保証', '￥1,799', 'https://www.amazon.co.jp/dp/B07MKSV83F', 'https://m.media-amazon.com/images/I/71T9yPDMC6L._AC_UL320_.jpg'), ('Logicool G  ゲーミングマウス 無線 G604 MMO 15ボタン HEROセンサー LIGHTSPEED ワイヤレス Bluetooth 接続対応 国内正規品', '￥9,900', 'https://www.amazon.co.jp/dp/B07YWX4MHR', 'https://m.media-amazon.com/images/I/615LzenkfGL._AC_UL320_.jpg'), ('GOFREETECH ゲーミングキーボード メカニカル104キー 茶軸 全キーロールオーバー アルミニウム キーボード 1680万色RGBバックライト/13種ラ イトモード/7色LEDライト オフィス/ゲーミング用', '￥5,095', 'https://www.amazon.co.jp/dp/B07CBWFF5G', 'https://m.media-amazon.com/images/I/71q-eTbjviL._AC_UL320_.jpg'), ('【PUBG JAPAN SERIES 2018推奨ギア】LOGICOOL ロジクール コンパクト メカ ニカル ゲーミング キーボード G310', '￥19,800', 'https://www.amazon.co.jp/dp/B011O614AI', 'https://m.media-amazon.com/images/I/81fc5O3VCZL._AC_UL320_.jpg'), ('Logicool G ゲーミングマウス 無線 G304 HEROセンサー LIGHTSPEED ワイヤレス 99g軽量 G304 国内正規品', '￥3,800', 'https://www.amazon.co.jp/dp/B07DVC25R2', 'https://m.media-amazon.com/images/I/51uIMsNFRHL._AC_UL320_.jpg'), ('e元素ゲーミングキーボード 茶軸81キーアンチゴーストキー メカニカル式LOLゲーム用キーボード RGB発光LED バックライト付き 英語配列USB有線高速反応 防水ゲーム用パソコンキーボード (茶軸ーホワイト) [並行輸入品]', '￥4,799', 'https://www.amazon.co.jp/dp/B07DGNV51H', 'https://m.media-amazon.com/images/I/71t9mYmFbnL._AC_UL320_.jpg'), ('【PUBG JAPAN SERIES 2018推奨ギア】ゲーミングキーボード ロジクール G810 RGB メカニカル ROMER-G', '￥19,800', 'https://www.amazon.co.jp/dp/B01BBKYM3I', 'https://m.media-amazon.com/images/I/71+kZcJFezL._AC_UL320_.jpg'), ('Logicool G ゲーミングマウス 有線 G600t MMO ゲーム用 20個 多ボタン RGB 国内正規品', '￥7,382', 'https://www.amazon.co.jp/dp/B01D45U6LA', 'https://m.media-amazon.com/images/I/512d6wIqnNL._AC_UL320_.jpg'), ('Logicool G ゲーミングマウス 無線 G703h HEROセンサー LIGHTSPEED ワイヤ レス エルゴノミクス LIGHTSYNC RGB POWERPLAY ワイヤレス充電 国内正規品', '￥7,900', 'https://www.amazon.co.jp/dp/B07SYKKP47', 'https://m.media-amazon.com/images/I/51PFaaMj60L._AC_UL320_.jpg'), ('【ロジクール RGBゲーミングキーボード/ FPS ゲーミングマウスセット】 G213 +  G402', '￥10,437', 'https://www.amazon.co.jp/dp/B078JGFXYT', 'https://m.media-amazon.com/images/I/31dNfPqnclL._AC_UL320_.jpg'), ('【日本語配列】HyperX Alloy Core RGB ゲーミングキーボード ゲーマー向け LEDバックライト 耐水性 2年保証 HX-KB5ME2-JP', '￥4,936', 'https://www.amazon.co.jp/dp/B07L4XGCFH', 'https://m.media-amazon.com/images/I/61VMsTLPaNL._AC_UL320_.jpg'), ('【PUBG JAPAN SERIES 2018推奨ギア】LOGICOOL ゲーミングキーボード G105', '￥13,500', 'https://www.amazon.co.jp/dp/B08D38CCX4', 'https://m.media-amazon.com/images/I/81qqVqXUM9L._AC_UL320_.jpg'), ('ロジクー ル MX MASTER 3 アドバンスド ワイヤレスマウス for Mac MX2200sSG Bluetooth 高速スクロールホイール 充電式 FLOW 7ボタン iPad 無線 ワイヤレス マウス MX2200 スペースグレー Unifying非対応 国内正規品 2年間無償保証', '￥41,780', 'https://www.amazon.co.jp/dp/B00CHF5HWC', 'https://m.media-amazon.com/images/I/61qITGm5YIL._AC_UL320_.jpg'), ('【PUBG JAPAN SERIES 2018推奨 ギア】LOGICOOL ロジクール アドバンス ゲームボード G13r [並行輸入品]', '￥1,900', 'https://www.amazon.co.jp/dp/B00CDG799E', 'https://m.media-amazon.com/images/I/71o9KOHkpXL._AC_UL320_.jpg'), ('Logicool G ゲームパッド F310r 有線 usb PCゲーム 用 FF14 Windows版推奨 国内正規品', '￥25,140', 'https://www.amazon.co.jp/dp/B07CMD5J5S', 'https://m.media-amazon.com/images/I/519-CQdsB+L._AC_UL320_.jpg'), ('Logicool G ゲーミングキーボード G512-LN ブラック メカニカルキーボード リニア 日本 語配列 LIGHTSYNC RGB G512 Carbon 国内正規品 2年間メーカー保証', '￥13,500', 'https://www.amazon.co.jp/dp/B07XQ6XD8J', 'https://m.media-amazon.com/images/I/61Uy0UakY6L._AC_UL320_.jpg'), ('ロジクール アドバンスド ワイヤレスマウス MX Master 3 MX2200sGR Unifying Bluetooth 高速スクロールホイール 充電式 FLOW 7ボタン windows Mac iPad OS 対応 無線 マウス MX2200 グラファイト 国内正規品 2年間無償保証', '￥20,000', 'https://www.amazon.co.jp/dp/B0158F7GV2', 'https://m.media-amazon.com/images/I/61PBIoWr1-L._AC_UL320_.jpg'), ('ゲーミングヘッドセット Logicool ロジクール G633 ブラック Dolby DTS 7.1ch 臨場感 RGB ノイズキャンセリングマイク Pro-Gオーディオ ドライバー PS4/PC/Xbox/Switch/スマホ 国内正規品 2年間メーカー保証', '￥14,740', 'https://www.amazon.co.jp/dp/B01J3G3GR0', 'https://m.media-amazon.com/images/I/61+4bXhcHqL._AC_UL320_.jpg'), ('Corsair K65 RAPIDFIRE CherryMX Speed RGB COMPACT-日本語 ゲーミングキーボード- KB356 CH-9110014-JP', '￥5,999', 'https://www.amazon.co.jp/dp/B07DNMFFXV', 'https://m.media-amazon.com/images/I/81FTJRVF0yL._AC_UL320_.jpg'), ('エレコム ゲーミングキーボード メカニカル 茶軸 5000万回耐久スイッチ 日本語配列 ゲーミングキーキャップ付属 全キーロールオーバー対応 LED搭載 ブ ラック ECTK-G01UKBK', '￥4,980', 'https://www.amazon.co.jp/dp/B07T4BHZ7J', 'https://m.media-amazon.com/images/I/71L1tbdQ5wL._AC_UL320_.jpg'), ('Logicool G ゲーミングマウス 有線 G403h HEROセンサー エルゴノミクスLIGHTSYNC RGB 6個プログラムボ タン 国内正規品', '￥8,582', 'https://www.amazon.co.jp/dp/B07L2Z97GH', 'https://m.media-amazon.com/images/I/5125TOdKL-L._AC_UL320_.jpg'), ('Logicool ロジクール G300Sr オプティカル ゲーミングマウス + ゲーミングキーボード ロジクール G213 RGB セット', '￥8,709', 'https://www.amazon.co.jp/dp/B0722XWTFR', 'https://m.media-amazon.com/images/I/31HJPaT2FdL._AC_UL320_.jpg'), ('ロジクール ワイヤレスマウス 無線 マウス ANYWHERE 2S MX1600sGR Unifying Bluetooth 高速充電式 FLOW対応 7ボタン windows mac iPad OS 対応 MX1600s グラファイト 国内正規品 2年間無償保証', '￥6,680', 'https://www.amazon.co.jp/dp/B07WC141LZ', 'https://m.media-amazon.com/images/I/51nqd45MTAL._AC_UL320_.jpg'), ('\xa0HAVIT メカニカルキーボード ゲーミングキーボード ゲーム マウス 50mm 高音質 マイク付き ヘッドホン セット LED有線 RGB ユニバーサル キーボードPCゲーマー コンピューターデスクトップ用 多色のバックライト US Layout HV-KB380L', '￥18,964', 'https://www.amazon.co.jp/dp/B081JNDZV5', 'https://m.media-amazon.com/images/I/71e3QsLLmmL._AC_UL320_.jpg'), ('SteelSeries ゲーミングキーボード テンキーレス Apex 7 TKL Blue Switch JP 青軸 有機ELディスプレイ 日本語配列 64756 【国内正規品】1年保証', '￥2,398', 'https://www.amazon.co.jp/dp/B07SQWJJRS', 'https://m.media-amazon.com/images/I/61H7yOU7BgL._AC_UL320_.jpg'), ('ゲーミングキーボード RGB1680万色 8種類LED色変え 3つライティングモード 最大9000万回使用寿命 106キー日本語配列 有線キーボード 25キー防衝突 防水仕様 Windows/Mac OS対応 仕事PC用/自宅ゲーム用 日本語説明書付き メーカー保証', '￥3,800', 'https://www.amazon.co.jp/dp/B078YH856D', 'https://m.media-amazon.com/images/I/718qiEFKlAL._AC_UL320_.jpg'), ('ロジクール M705m ワイヤレスマウス 無線 マウス Unifying 7ボ タン 高速スクロール 電池寿命最大36ケ月 チャコール windows mac chrome 国内正規品 3年間無償保証', '￥4,799', 'https://www.amazon.co.jp/dp/B07DGNV51H', 'https://m.media-amazon.com/images/I/51CMd7VvQ3L._AC_UL320_.jpg'), ('e元素ゲーミングキーボ ード 茶軸81キーアンチゴーストキー メカニカル式LOLゲーム用キーボード RGB発光LEDバックライト付き 英語配列USB有線高速反応  防水ゲーム用パソコンキーボード (茶軸ーホワイト) [並行輸入品]', '￥2,180', 'https://www.amazon.co.jp/dp/B083FCWGHX', 'https://m.media-amazon.com/images/I/71t9mYmFbnL._AC_UL320_.jpg'), ('ゲーミングキーボード 108キー日本語配列キーボード 有線キーボード 26キー防衝突 変換/無変換キー付き LEDキーボード ３つ色変えモード 虹色バックライトキーボード 防水仕様 仕事/自宅用 メーカー保証', '￥13,300', 'https://www.amazon.co.jp/dp/B07NDNWBD8', 'https://m.media-amazon.com/images/I/61YvtNLpU5L._AC_UL320_.jpg'), ('Logicool G ゲーミングヘッドセット ワイヤレス 無線 G933s Dolby 7.1ch 3.5mm usb LIGHTSYNC ノイズキャン セリング 単一性 折り畳み式マイク PC/PS4/Switch/スマホ 国内正規品', '￥2,380', 'https://www.amazon.co.jp/dp/B07YTWF2PL', 'https://m.media-amazon.com/images/I/61x-rjxe8aL._AC_UL320_.jpg')]

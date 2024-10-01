Proje Amacı

Proje, FİBERFLON Teknik Tekstil A.Ş fabrikasının depo bölümündeki iş süreçlerinin hızlandırılması ve kolaylaştırılması amaçlanarak geliştirildi.

Fabrikada yanmaz kumaş üretimi yapılmaktadır, üretimden gelen farklı büyüklüklerde ve ağırlıklardaki top halindeki kumaşlar depo da bulunan raflarda ve kumaş arabalarında stoklanmaktadır. Sipariş üzerine depoda stoklanmış bir kumaşı kalite kontrol yapmak üzere almak isteyen bir personel kumaşı ararken bulmakta zorluk veya zaman kaybı yaşabilmekte ve bu durum problem oluşturmaktadır. Bu projede geliştirilen stok takip sistemi bu probleme çözüm olmuştur.

Projenin İşlevleri

Projenin anlaşılabilirliği açısından “Ekranlar” klasöründe projenin ekranları mevcuttur, aşağıda her bir ekranın işlevselliği açıklanmıştır.

a) Giriş Ekranı : Veri tabından yapılan sorgu ile sisteme giriş yapılır ve “Depo Ekranı” açılır.

b) Depo Ekranı : “Arabalar” ve “Raflar” butonları bulunur, kullanıcı personel işlem yapmak istediği arabaya veya rafa erişmek üzere bu butonları kullanır, butonlar aracılığı ile “Arabalar Ekranı” veya “Raflar Ekranı” na ulaşır. Ekranda bulunan diğer butonlar ise “Kumaş Ara” ve “Kumaş Kayıt” butonlarıdır, bu butonlar aracılığı ile de kullanıcı personel aradığı kumaşı bulmak üzere “Kumaş Ara Ekranına”, yeni bir kumaş kayıt etmek üzere de “Kumaş Kayıt Ekranına” erişim sağlar.

c) Arabalar Ekranı : İşlem yapılmak istenen arabanın butonuna tıklamak suretiyle ilgili arabaya erişim sağlanır.

d) Raflar Ekranı : İşlem yapılmak istenen rafın butonuna tıklanmak suretiyle ilgili rafa erişim sağlanır.

e) Kumaş Kayıt Ekranı : Her bir kumaş “ID” alanı yerine geçen “Lot” numarasına sahiptir, bu ekranda kayıt işlemi yapılırken kullanıcı personel ilgili kumaşın “Lot” numarasını, kumaşın türünü belirten “Kalite” sini ve kumaşın boyutunu belirten “Genişlik” boyutunun veri girişini yapar ve bu kumaşı eklemek istediği arabayı veya rafı seçer ve “Kaydet” butonuna tıklamak suretiyle veri tabanına kayıt eder.

f) Kumaş Ara Ekranı : Kullanıcı personel aradığı kumaşı kalitesini üzerinden filtreleyerek “Listele” butonu üzerinden kumaşın hangi araba veya rafda bulunduğu bilgisine erişir.Depoda bulunan tüm kumaşların bilgisinede “Tümünü Listele” butonundan erişebilir.

g) Örnek Araba Ekranı : Kullanıcı personel kalite kontrole götürmek üzere ilgili arabadan aldığı kumaşı bulunduğu arabanın veri tabanından siler,İlgili arabadaki bulunan kumaşlara erişebilir.

h) Örnek Raf Ekranı : Kullanıcı personel kalite kontrole götürmek üzere ilgili raftan aldığı kumaşı bulunduğu arabanın veri tabanından siler,İlgili arabadaki bulunan kumaşlara erişebilir.

Proje Programının Çalıştırılması :

Proje, python yazılım dili ile programlanmış, pyqt5 kitaplığı ile kullanıcı arayüzü tasarlanmış ve veri tabanı için sqlite sistemi kullanıldı.

a) Python, SQLite, PyQt5 programlarını yükle. 

b) SQLite da klasörde bulunan “admin.db” veri tabanını aç. 

c) Herhangi bir python IDE sinde klasörü aç. 

d) Klasördeki “Giris2.py” dosyasını aç ve çalıştır.

Sisteme Giriş : Güncel kullanıcı adı “özkan” ve şifre “123” dir.

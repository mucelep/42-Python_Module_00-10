# General Notes

* fonksiyonları bir degiskene atayabilirsin ör
  ```
  * def printhello():
      print("hello"):
    
    x = printhello
    x()
  ```
* return edebilirsin ve liste dict gibi yapılarda saklayabilirsin

# EX0 Notes
### Lambda Notes

lambda seçme sebebimiz kısa ve tek kullanımlık fonksiyonları daha kolay yazmak
`sorted()` `filter()` `map()` ile kullanulır genelde belli bi kurala göre sıralamak için

* lambda bir ananonim fonksiyon olusturma yapısı
  * kullanım lambda 'parametre': 'işlem'
  * `lambda x: x * 2`

### Sorted() Notes
* sorted()
  * 3 parametresi var 1. sıralanacak veri
  * 2. hangi kurala göre
  * 3. reverse=false (defult) küçükten büyüğe =ture büyükten küçüğe

### Filter Notes
* filter()
  * 2 parametresi var 1. hangi kurala göre fonksiyon bekler
  * 2. filtrelenicek veri

# EX1 Notes
 fonksiyonları normal bir veri gibi kullanmayı ögretiyor
 ### callable()
* bir şeyin fonksiyon gibi çağrılıp çağrılamadığını kontrol eder. true false döner
 ### Callable
* bir type hint dir
* Bir parametrenin fonksiyon olması gerektiğini belirtmek için kullanılır.
  * `Callable[[int], None]` int alır none döndürür

# EX2 Notes

### nonlocale Notes
* iç içe fonksiyon kullanıdıgımızda dış/çevreleyen (outer/enclosing) fonksiyonun bir degiskenini
 iç fonksiyon (inner) hatırlar okur AMA degistiremez degistirme izni vermek için 
 `nonelocal` kullanılır 
  * **bir bakıma bu degisken çevreleyen fonksiyonun değişkeni demektir**
#### Lexical Scoping
* Lexical Scoping ise bir degiskenin hangi scope içinde erişlebilir oldugunu runtime dan önce 
kodun yapısına bakarak belirlemesidir 
#### Closure
* closure ise inner fonksiyonun outer fonksiyonun degiskenlerini hatirlaması olayidir
— dış fonksiyon çoktan çalışıp bitmiş olsa bile. paket hafıza python inner'in ihtiyac duydugu degiskeni inner ile paketler
outer fonksiyonun inner fonksiyonu return etmesi beklenir 


# EX3 Notes

### functools
#### reduce()
  * Bir listedeki elemanları tek bir sonuca indirger.
  * 2 ser 2 ser hareket eder | 3 parametre alir
    * 1- fonksiyon 2-iterable (islem yapılıcak değerler) 3- initializer(opsiyonel) baslangıc degeri 
    * `reduce(lambda x, y: x + y, [1, 2, 3], 10)`
        10 + 1 → 11 |
        11 + 2 → 13...
#### partial()
  * bir fonksiyona daha az argüman girerek aynı islevi yaptıran yeni bir fonksiyon üretmek için kullanulır 
  * bir fonksiyonun bazı parametrelerini/argümanlarını sabitlersin

  * `def guc_uygula(power, element, target):`
  * `ates = partial(guc_uygula, 50, "ateş")`
    `ates("Ejderha")`

#### @functools.lru_cache(maxsize=None) | Sonuç önbellekleme (memoization)
 Bir fonksiyonun daha önce hesapladığı sonuçları hatırlar, aynı girdiyle tekrar çağrılırsa yeniden hesaplamaz. Özellikle rekürsif fonksiyonlarda performansı ciddi artırır.


####  @functools.singledispatch 
bir fonksiyonun aldıgı ilk parametrenin tipine göre farklı davranmasını sağlar 
* @process.register ile kullanılır
* if else yapısına benzer 


# EX4 Notes


## @functools.wraps(spell_func)
 decorator yazarken orjinal fonksiyonun bilgilerini(metadata (__name __ | __doc __ gibi) ) wrapper fonksiyona aktarmak için kullanulır

 decorator yapmamızın sebebi Bir fonksiyonu alıp, onu başka bir fonksiyonla sararak (wrap ederek) davranışını değiştirmek veya geliştirmek.

## *args ve **kwargs

* decorator e parametre vermek istiyosan min_power gibi iç içe yapı kurmak gerekir
* 
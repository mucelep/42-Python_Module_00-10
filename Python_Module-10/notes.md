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

# Ex0 Notes
#prefix suan calısan python un(python3) ortam dizinlerini / base ise ana python un ortam dizinlerini gösterir
#şuan calısmakta olan python yorumlayıcısının tam dosya yolu  {sys.executable}
# Ex1 Notes
* __Pandas__
  * veri yapısı olusturur 
  * `.datafreame()` verileri indeksler
  * `.read_csv()` dısarıdan csv dosyası okur excel gibi
  * `.head()` defult olarak ilk 5 elemanı basar 3 verirsen 3 tane
  * `.columns` tüm kolonları basar
  * `.describe()` min max vb verilerini verir kolon sayılarını verir
  * `.dtypes` kolonların veri tiplerini gösterir
  * `.tail()` head in tersten basan versiyonu
  * `df[df['kolonadı'] > 400]` gibi 400 den yüksek olanları basabilirsin

# Ex2 Notes
load_dotenv() çağrıldığında, proje klasöründeki .env dosyasını bulur ve içindeki değişkenleri os.environ'a yükler — ama önemli: eğer o değişken zaten sistemde

* __matplotlib__
  * `.figure` veri basmak için grafik penceresi olusturur
  * `.plot()` verileri çizgi grafik olarak çizmek için kullanılır yani grafik penceresine verileri basar
  * `.tight_layout()` grafikteki veriler isimler etiketler vb birbirine girmesin diye otomatik düzünleme yapar
  *  `.savefig("grafik.png")` olusturdugun grafiği dosya olarak kaydetmene yarar
  * `.show()` grafiği yeni pencere olarak ekranda açar
  * `.subplot(<kac satır> <kac kolon> <hani alana bassın>)` birden fazla grafiği yan yana yazabilmek için kullanılır `.subplot(1, 2, 1)` gibi ardından alt satıra plot ile veriler basılır
  * `.scatter` line degil dot grafiği
  * `.pie()` pasta grafiği
  * `plt.title("Matrix Signal")`
    `plt.xlabel("Index")`
    `plt.ylabel("Value")` aabisi belli zaten ayık olcan

# Pip Notes
 **paket kurmak ve yönetmek**

* `pip list`
  * kurulu paketleri listeler insan okuması için daha kolay
* `pip freeze` 
  * requirements.txt formatında gösterir
  * pip freeze > ---.txt olarak baska dosyaya aktarılabilir
  ve daha sonra baska bilgiasayardan pip install ile kurulabilir 
* `pip show` 
  * bağımlılıklarını gösterir
* `pip install`
  * pip ile paket indirmek için kullanılır
  * `pip install -r (--reqierment) requierments.txt`
    ile gereklilikler dosyası indirilebilir -r gereklidir


# Poetry Notes
 **paketleri, bağımlılıkları ortamı ve proje ayarlarını daha kapsamlı yönetir**

* `poetry install`
  * .toml dosyasını okur ve gereklilikleri indirir
* `poetry new my_project`
  * yeni proje olusturur
  * .toml readme içinde otomatik gelir
* `poetry show`
  * bağımlılıkları gösterir 
* `poetry env info`
  * base ve aktif enviroment hakkında bilgi verir
* `poetry add` and `remove`
  * paket ekler ve siler yanına paket ismi ile kullanılır
  * otomatik pyproject.toml dependencies kısmına ekler
* `poetry run python main.py`
  * venv içindekilerle programı çalıstırırsın

# .toml Notes
 **config dosyaları için tasarlanmış bir format**

* authors = ["Senin Adın <mail@ornek.com>"]
  * bu kısım poetry 2.0 ve üstüne zorunlu degil
* [build-system]

  * "Bu projeyi build etmek (paket haline getirmek) için hangi araç kullanılacak, ve o aracın kendisi nasıl kurulacak?"
    * requires = [...]	Build işlemi için hangi paket(ler) gerekli, onu söyler
    * build-backend = "..."	Build işini gerçekten hangi Python modülü yürütecek, onu söyler


  * bu kısımı da poetry init kendi hallediyor elle ugrasmaya gerek yok
  * ama eski sürümlerde sıkıntı yasanabiliyor yapmak güvenli olan
* pacgakes mode
  * defult olarak ture dir ture oldugunda istedikleri:
  * name: paket adı. Küçük harf, tire veya alt çizgi olabilir. Paket-modu açıksa (default) dosyaklasör adıyla eşleşmesi lazım
    version: semver formatında (0.1.0 gibi).
    description: kısa açıklama, boş olamaz (paket modundaysa).
  * paket modu açıkken poetry projeyi de paket gibi indirme davranısını gösterir bunun sebebi
    import o venv içinde loading yapabilmek için
  * tool. toml in tasarım felsefi ile ilgili iç içe liste seklinde tutuyor 
   iki araç da name kullanırsa çakışma olurdu bunun önüne geçiyor
* poetry.lock
  * poetry.lock, pyproject.toml'da belirttiğin (^2.5 gibi esnek) sürüm aralıklarının, tam olarak hangi kesin sürümde çözüldüğünü kaydeden dosya.
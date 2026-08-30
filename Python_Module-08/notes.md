
# Pip Notes
 paket kurmak ve yönetmek

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
 paketleri, bağımlılıkları ortamı ve proje ayarlarını daha kapsamlı yönetir

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

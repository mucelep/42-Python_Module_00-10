# pydentic notes
* Pydantic'in kendi metotları var
  * kullanici = KullaniciKaydi.model_validate(json_veri)   # dict'ten
  * kullanici_json = kullanici.model_dump_json()           # nesneden JSON'a
  * kullanici_dict = kullanici.model_dump()
# field() notes
* gt / ge	greater than / greater or equal (büyüktür / büyük eşit)
* lt / le	less than / less or equal (küçüktür / küçük eşit)
* min_length / max_length	string veya liste uzunluğu sınırı
* default	varsayılan değer
* default_factory	varsayılan değeri üreten bir fonksiyon (mesela boş liste)
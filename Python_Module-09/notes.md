# pydentic notes
* Pydantic'in kendi metotları var
  * kullanici = KullaniciKaydi.model_validate(json_veri)   # dict'ten
  * kullanici_json = kullanici.model_dump_json()           # nesneden JSON'a
  * kullanici_dict = kullanici.model_dump()                # nesneden Dict e
# field() notes
* gt / ge	greater than / greater or equal (büyüktür / büyük eşit)
* lt / le	less than / less or equal (küçüktür / küçük eşit)
* min_length / max_length	string veya liste uzunluğu sınırı
* default	varsayılan değer
* default_factory	varsayılan değeri üreten bir fonksiyon (mesela boş liste)

# validator notes
* Field(gt=0, min_length=2, ...)	Tek bir alana basit sınır/kural koymak
* field_validator("alan_adi")	Tek bir alana özel/karmaşık mantık uygulamak (regex, custom kontrol)
  * value nin kendisini geri retyurn etmeli
* model_validator(mode="after")	Birden fazla alanı birbiriyle karşılaştırmak (tarih aralığı, şifre eşleşmesi)
* model_validator(mode="before")	Ham veri (dict) Pydantic'e girmeden önce ön işleme yapmak
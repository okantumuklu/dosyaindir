import urllib.request
link = input("Url yi giriniz:")
if __import__("requests").get(link).status_code == 200:
  print("Dosya bulundu.")
  print("""uzantılar
  1)mp4    2)mp3
  3)jpg    4)png
  5)Başka bir uzantı için, '5'e basınız 
  """)
  uzantı = input("Uzantıyı giriniz:")

  if uzantı == "1" or uzantı == "mp4":
    isim = input("Dosyanın ismi ne olsun?:")
    urllib.request.urlretrieve(link,f"{isim}.mp4")
    print("Dosyanız indirilmiştir.")
  elif uzantı == "2" or uzantı == "mp3":
    isim = input("Dosyanın ismi ne olsun?:")
    urllib.request.urlretrieve(link,f"{isim}.mp3")
    print("Dosyanız indirilmiştir.")
  elif uzantı == "3" or uzantı == "jpg":
    isim = input("Dosyanın ismi ne olsun?:")
    urllib.request.urlretrieve(link,f"{isim}.jpg")
    print("Dosyanız indirilmiştir.")
  elif uzantı == "4" or uzantı == "png":
    isim = input("Dosyanun ismi ne olsun?:")
    urllib.request.urlretrieve(link,f"{isim}.png")
    print("Dosyanız indirilmiştir.")
  elif uzantı == "5":
    uzantı2 = input("İndirmek istediğiniz uzantı nedir:")
    isim = input("Dosyanın ismi ne oslun?:")
    urllib.request.urlretrieve(link,f"{isim}.{uzantı2}")
    print("Dosyanız indirilmiştir.")

  else:
    print("Yanlış bir işlem yaptınız!")
else:
  print("Dosya Bulunamadı!")
  








"""
kodun bu kısmını yazan Zilla dostuma teşekkür ederim. :)

link = input("Url yi giriniz:")
if __import__("requests").get(link).status_code == 200:
  print("Link sitede var.")
else:
  print("yok")

"""

print("""VÜCUT KİTLE İNDEKS HESABINA GÖRE YAPABİLECEKLER 🥗
        SİSTEMİMİZE HOŞGELDİNİZ
    """)
ad=input("Adınızı giriniz : ")
soyad = input("Soyadınızı giriniz : ")
boy = float(input("Boyunuzu metre cinsinden giriniz (Örn:1.70 m):"))
kilo = float(input("Kilonuzu kg cinsinden giriniz (Örn: 65.5 kg):"))
 
vucut_indeks  = kilo/(boy*boy)
def indeks():
  if vucut_indeks <18:
    return (" Zayıf ; Vücut Kitle İndeks Sonucu:{}".format(vucut_indeks))
  elif vucut_indeks >= 18 and vucut_indeks <25 :
    return (" Normal ; Vücut Kitle İndeks Sonucu:{}".format(vucut_indeks))
  elif vucut_indeks >= 25 and vucut_indeks <30:
    return (" Kilolu ; Vücut Kitle İndeks Sonucu:{}".format(vucut_indeks))
  elif vucut_indeks >= 30 and vucut_indeks <35:
    return (" Obez ; Vücut Kitle İndeks Sonucu:{}".format(vucut_indeks))
  else:
    return (" Ciddi Obez ; Vücut Kitle İndeks Sonucu:{}".format(vucut_indeks))

sonuc=indeks()

def tavsiye():
  if sonuc == "zayıf":
    Z=['Karbonhidratlı Besinler yiyebilirsin','Çok hareket etmemelisin']
    return Z
  elif sonuc == "normal":
    N=['Düzenli beslenmeye devam edebilirsin','Yürüyüş yapabilirsin']
    return N
  elif sonuc == "kilolu":
    K=['Geç vakitte yemek yememen gerekir','Suyu daha fazla tüketibilirsin']
    return K
  elif sonuc == "obez":
    O=['Düzenli spora başlamalısın','Az yemek yemelisin']
    return O
  else:
    C=['Doktora gitmelisin','Sağlığın için daha dikkatli olmalısın']
    return C
sonuc1=tavsiye()
yazdırma={"Sonuçlarım":sonuc ,"Yapabileceklerim":sonuc1}
print(yazdırma)

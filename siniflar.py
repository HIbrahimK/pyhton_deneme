
class calisan:
    zam_orani=1.8
    counter =0
    def __init__(self,isim,soyisim,maas):
        self.isim=isim
        self.soyisim=soyisim
        self.maas =maas
        self.email = isim+soyisim+"@asd.com"
        calisan.counter=calisan.counter+1

    def giveFullname(self):
        return self.isim+ " " + self.soyisim

    def zamYap(self):
        self.maas=self.maas+ self.maas*self.zam_orani

    @classmethod
    def set_raise_amt(cls,amount):
        cls.zamYap =amount


isci1=calisan("ali","veli",100)
isci2=calisan("ayse","veli",200)
isci3=calisan("fatma","veli",200)
isci4=calisan("ahmet","veli",150)
print("hello")
# print(isci1.email)

# print(isci1.giveFullname())
# print(calisan.giveFullname(isci1))

# print(isci1.maas)

# isci1.zamYap()
# print(isci1.maas)
# print(calisan.counter)
# print(isci4.__dict__)
print(isci1.zamYap())
print(isci1.maas)

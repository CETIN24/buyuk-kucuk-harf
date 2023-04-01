def buyuk_kucuk(string):
    new_string = ""
    for i in range(len(string)):
        if i % 2 == 0:
           new_string += string[i].upper()
        else:
            new_string += string[i].lower()
    print(new_string)
buyuk_kucuk("MerHAba Bu bENim Veri BİLimi  İçiN YPTığım ÇalıŞma")

"""
Kullanıcıdan integer bir değer alan ve sayının pozitif-çift sayı olup olmadığını kontrol eden program yazınız. Girilen sayıların muhtemel farklı durumlarını göz önünde bulundurunuz. (negatif, string vs. gibi durumlar)
"""
number = input("gimme a number!: ")
if not number.isdigit():
    print("integer pls!")
elif number.isdigit() and int(number) % 2 == 0:
    print(f"{number} is an even number. ")
        
else:
    print(f"{number} is not an even number. ")
        

    



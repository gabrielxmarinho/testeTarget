# String Inicial
str = input("Digite um Texto:")
# String Final(Retorno)
str2 = ""
for i in range(0,len(str)):
    str2+=str[len(str)-1-i]
print(str2)
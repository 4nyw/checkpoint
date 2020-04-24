lista = ["caiodm088@gmail.com",
        "caiodm8@gmail.com",
        "rm85590@fiap.com.br",
        "biamonteiro@bn.com.br",
        "caio@hotmail.com.br",
        "profalberico.filho@fiap.com.br",
        "testando@hotmail.com",
        "preenchedo@gmail.com",
        "acho@gmail.com",
        "pythonehlegal@gmail.com",
        "gmail@gmail.com",
        "kkkkk@yahoo.com.br",
        "rm00000@fiap.com.br",
        "completandoalista@ig.com.br",
        "ivanexpressecorrier@ig.com.br",
        "vazamento@gmail.com.br",
        "diwajdiw@yahoo.com.br",
        "mae@gmail.com",
        "tenhoideia@yahoo.com.br",
        "mfefie@bn.com.br",
        "miadsj@yandex.com.br",
        "testingpy@bn.com.br",
        "challenge@fiap.com.br",
        "rm00001@fiap.com.br",
        "rm00002@fiap.com.br",
        "rm00003@fiap.com.br",
        "rm00004@fiap.com.br",
        "rm00005@fiap.com.br",
        "rm00006@fiap.com.br",
        "rm00007@fiap.com.br"]

novoEmail = input("Insira um e-mail: ")
lista.append(novoEmail)

emailPraChecar = input("Qual e-mail você quer checar? ")
if emailPraChecar in lista:
    print("E-mail vazado!")
else:
    print("E-mail está seguro!")

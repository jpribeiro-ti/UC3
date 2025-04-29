
# Exemplo de função básica

def saudacao(nome):
    retur f"Olá, {nome}!"

    print(saudacao("Maria"))


    lista = [1, 2, 3, "quatro"]
    tupla = (1, 2, 3) #Imutável, não pode ser alterado
    conjunto = {1, 2, 3} #únicos e não ordenados
    dicionario = {"chave": "valor", "idade": 20} #Salvar em forma de chave e valor

    nota = float(input("Digite a nota: "))
    status = "Aprovado" if nota >= 7 else "Reprovado"
    print(status)

    def calcular_imc():
        peso = float(input("Digite o peso: "))
        altura = float(input("Digite a altura: "))
        imc = peso / (altura ** 2)
        return imc
        print(f"Seu IMC é {calcular_imc()}")
        print(f"Seu IMC é {imc:.2f}")


        def verifica_palindromo(palavra):
            return palavra == palavra[::-1]
        

        def verifica_palindromo():
            palavra = input("Digite uma palavra: ").lower().replace(" ", "")   
            if palavra == palavra[::-1]:
                print("Palíndromo")
            else:
                print("Não é palíndromo")
            return palavra == palavra[::-1]
        verifica_palindromo()
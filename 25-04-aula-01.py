# 1- Cálculo de Média de Notas: Peça ao usuário que insira 4 notas (de 0 a 10). Calcule a média das notas e exiba o resultado.
# Se a média for maior ou igual a 7, exiba "Aprovado". Caso contrário, exiba "Reprovado".

nota1 = float(input("Digite a primeira nota: ")
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("Aprovado")        
else:                
    print("Reprovado")  


nota1 = float
from suds.client import Client

(print("........................Calculadora Python........................"))

print("Digite 1 para Soma: ")
print("Digite 2 para Subtração: ")
print("Digite 3 para Multiplicação: ")
print("Digite 4 para Divisão: ")
op = int(input())

if op < 1 or op > 4:
    print("Opção Inválida!")
    quit()

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if op == 1:

    print(Client('http://localhost:10000/calculadora?wsdl').service.soma(num1, num2))

elif op == 2:

    print(Client('http://localhost:10000/calculadora?wsdl').service.subtrai(num1, num2))

elif op == 3:
    
    print(Client('http://localhost:10000/calculadora?wsdl').service.multiplica(num1, num2))

elif op == 4:

    print(Client('http://localhost:10000/calculadora?wsdl').service.duvide(num1, num2))



from suds.client import Client

(print("........................Calculadora Python........................"))

print("Digite 1 para Soma: ")
print("Digite 2 para Subtra��o: ")
print("Digite 3 para Multiplica��o: ")
print("Digite 4 para Divis�o: ")
op = int(input())

if op < 1 or op > 4:
    print("Op��o Inv�lida!")
    quit()

num1 = int(input("Digite o primeiro n�mero: "))
num2 = int(input("Digite o segundo n�mero: "))

if op == 1:

    print(Client('http://localhost:10000/calculadora?wsdl').service.soma(num1, num2))

elif op == 2:

    print(Client('http://localhost:10000/calculadora?wsdl').service.subtrai(num1, num2))

elif op == 3:
    
    print(Client('http://localhost:10000/calculadora?wsdl').service.multiplica(num1, num2))

elif op == 4:

    print(Client('http://localhost:10000/calculadora?wsdl').service.duvide(num1, num2))



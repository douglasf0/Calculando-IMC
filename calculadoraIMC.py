#Calculando IMC

#Variáveis
peso = float(input('Qual é seu peso (KG): '))
altura = int(input('Qual é sua altura (Centimetros): '))

#Calculo IMC
imc = peso / (altura ** 2)
print(f'Seu IMC é {imc:.1f}')

#Verificando ERRO
if any(x <= 0 for x in [imc, altura, peso]):
    print('Por favor, verifique os dados digitados e tente novamente!')
else:
#Mensagem de Resultado
    if imc < 18.5:
        print('Você está abaixo do peso!')
    elif 18.5 <= imc <25:
        print('Parabéns você está no peso ideal!')
    elif 25 <= imc < 30:
        print('Voce está com sobrepeso!')
    elif 30 <= imc < 40:
        print('Cuidado, você esta com obesidade!')
    else:
        print('Cuidado, você está com obesidade morbida!')

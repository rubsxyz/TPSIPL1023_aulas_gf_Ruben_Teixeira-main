"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. 
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. 
Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. 
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
"""
def converter_horario(horas, minutos):
    # Verifica se é A.M. ou P.M. e ajusta as horas
    periodo = 'A.M.'
    if horas >= 12:
        periodo = 'P.M.'
        horas -= 12
    if horas == 0:  # Se for meia-noite, ajusta para 12 A.M.
        horas = 12
    return horas, minutos, periodo

def imprimir_horario(horas, minutos, periodo):
    print(f"{horas}:{minutos:02d} {periodo}")

# Loop para permitir que o usuário faça várias conversões
while True:
    try:
        hora_24 = input("Digite o horário no formato HH:MM (24 horas), ou 'sair' para encerrar: ")
        if hora_24.lower() == 'sair':
            break
        horas, minutos = map(int, hora_24.split(':'))

        if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
            print("Por favor, insira um horário válido.")
            continue

        horas_convertidas, minutos_convertidos, periodo = converter_horario(horas, minutos)
        imprimir_horario(horas_convertidas, minutos_convertidos, periodo)
    except ValueError:
        print("Formato inválido. Por favor, insira o horário no formato HH:MM.")

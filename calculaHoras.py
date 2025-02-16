from datetime import datetime, timedelta

def calcular_saida():
    # Solicita o horário de entrada
    entrada_str = input("Digite o horário de entrada (HH:MM): ")
    try:
        entrada = datetime.strptime(entrada_str, "%H:%M")
    except ValueError:
        print("Formato inválido! Use HH:MM.")
        return

    # Solicita a quantidade de horas a trabalhar no formato HH:MM
    horas_trabalho_str = input("Digite a quantidade de horas que deseja trabalhar (HH:MM): ")
    try:
        horas, minutos = map(int, horas_trabalho_str.split(":"))
        horas_trabalho = timedelta(hours=horas, minutes=minutos)
    except ValueError:
        print("Entrada inválida! Use o formato HH:MM.")
        return

    # Solicita o tempo de almoço em minutos
    try:
        almoco_min = int(input("Digite o tempo de almoço em minutos: "))
    except ValueError:
        print("Entrada inválida! Use um número inteiro válido.")
        return

    # Calcula o horário de saída
    tempo_almoco = timedelta(minutes=almoco_min)
    saida = entrada + horas_trabalho + tempo_almoco

    # Exibe o horário de saída
    print(f"Você deverá sair da empresa às {saida.strftime('%H:%M')}")

if __name__ == "__main__":
    calcular_saida()

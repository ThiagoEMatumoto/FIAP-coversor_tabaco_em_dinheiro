# Nome: Thiago Eiji Matumoto
# RM: 97711

import time
import os

txt_tempo = "Tempo como fumante (anos)"
txt_valor = "Valor do maço"
txt_quantidade = "Quantidade de maços por dia"

espaco = 34

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_valor(tempo_fumando, valor_maco, qtd_maco_por_dia):
  dias_fumando = tempo_fumando*360
  maços_fumados = dias_fumando*qtd_maco_por_dia
  gastos_totais = maços_fumados * valor_maco
  return gastos_totais

def main():
  limpar_tela()
  try:
    anos = float(input(txt_tempo.ljust(espaco, ".") + ": "))
    valor = float(input(txt_valor.ljust(espaco, ".") + ": "))
    quantidade = float(input(txt_quantidade.ljust(espaco, ".") + ": "))
  except:
    print("hey, por favor, apenas números!")
    time.sleep(3)
    limpar_tela()
    main()
    
  gastos_totais = calcular_valor(anos, valor, quantidade)  

  if gastos_totais < 20000:
    print(f"Com o valor R${gastos_totais:.2f}, você poderia ter dado entrada em um carro.")
  elif 20000 <= gastos_totais <= 50000:
    print(f"Com o valor R${gastos_totais:.2f}, você poderia ter comprado um carro popular usado.")
  else:
    print(f"Com o valor R${gastos_totais:.2f}, você poderia ter comprado um carro zero.")
  
  while True:
    try:
      retornar = int(input("Deseja realizar outra consulta [0-não|1-sim]:"))
      if retornar == 1:
        main()
      elif retornar != 0 and retornar != 1:
        print("hey, por favor, coloque uma entrada válida")
        time.sleep(3)
        limpar_tela()
      else:
        break
    except:  
      print("hey, por favor, coloque uma entrada válida")
      time.sleep(3)
      limpar_tela()
      
  print("PARE DE FUMAR!")
  
if __name__ == "__main__":
    main()








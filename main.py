# Nome: Thiago Eiji Matumoto
# RM: 97711

txt_tempo = "Tempo como fumante (anos)"
txt_valor = "Valor do maço"
txt_quantidade = "Quantidade de maços por dia"


anos = float(input(txt_tempo.ljust(34, ".") + ": "))
valor = float(input(txt_valor.ljust(34, ".") + ": "))
quantidade = float(input(txt_quantidade.ljust(34, ".") + ": "))


ano = 12
mes = 30

valor_total = (ano*mes*anos) * valor * quantidade

print(f"R${valor_total:.2f} ano")












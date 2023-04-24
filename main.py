print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)

# Coloque o código para resolver o problema nessa parte do programa
import math
cobertura = float(metros_quadrados / 3)
lata = float(18)
litros_necessarios = cobertura / lata
if litros_necessarios != int:
    litros_necessarios = math.ceil(litros_necessarios)


valor_unitario = float(80)

# As duas variáveis qtd_de_latas e valor_total devem guardar a resposta do problema
# Troque os zeros pelos valores corretos.
qtd_de_latas = litros_necessarios
valor_total = qtd_de_latas * valor_unitario

print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")
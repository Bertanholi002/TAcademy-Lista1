from .input import pega_hora_trabalhada, ganho_hora

def execucao_rotina():
    money_all = ganho_hora() * pega_hora_trabalhada()
    desconto_ir = money_all * 0.11
    inss = money_all * 0.08
    sindicato = money_all * 0.05
    liquid = money_all - (desconto_ir + inss + sindicato)
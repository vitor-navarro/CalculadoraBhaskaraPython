from interface import cria_janela
from math import sqrt

def desenvolvimento_delta(valor_a,valor_b,valor_c,delta,label_desenvolvimento_delta):
    '''

    :param a_entry: Valor do A, já tratado.
    :param b_entry: Valor do B, já tratado.
    :param c_entry: Valor do C, já tratado.
    :param delta: Valor de Delta, já tratado.
    :param label_desenvolvimento_delta: é onde será exibido todoo o desenvolvimento do delta da bhaskara.
    :return: any, imprimido na janela.
    '''
    label_desenvolvimento_delta["text"] = \
        f'''Desenvolvimento DELTA:
    \u0394 = (b)\u00b2 - 4xAxC
    \u0394 =  ({valor_b})\u00b2 - 4x{valor_a}x{valor_c}
    \u0394 = {valor_b ** 2} {-4 * valor_a * valor_c}
    \u0394 = {delta}
                '''

def desenvolvimento_x(valor_a,valor_b,valor_c,delta,raiz_delta,x_linha,x_2_linha,label_desenvolvimento_x):
    '''

    :param a_entry: Valor do A, já tratado.
    :param b_entry: Valor do B, já tratado.
    :param c_entry: Valor do C, já tratado.
    :param delta: Valor de Delta, já tratado.
    :param raiz_delta: Valor da raíz de Delta, já tratado.
    :param x_linha: É o primeiro valor final da equação, resultado da conta positiva da bhaskara.
    :param x_2_linha: É o segundo valor final da equação, resultado da conta negativa da bhaskara.
    :param label_desenvolvimento_x:  é onde será exibido todoo o desenvolvimento do x´ e x´´ da bhaskara.
    :return: any, imprimido na janela.
    '''
    label_desenvolvimento_x["text"] = \
        f'''Desenvolvimento X:
    x = (-b ±√\u0394)/2xA
    x =  (-{valor_b}±√{delta})/2x{valor_a}
    x =  ({-valor_b}±{round(raiz_delta,3)})/{2 * valor_a}
    x´ = ({-valor_b} + {round(raiz_delta,3)})/{2 * valor_a}
    x´ = ({round(-valor_b + raiz_delta,3)})/{2 * valor_a}
    x´ = {round(x_linha,3)}

    x´´ = ({-valor_b} - {round(raiz_delta,3)})/{2 * valor_a}
    x´´ = ({round(-valor_b - raiz_delta,3)})/{2 * valor_a}
    x´´ = {round(x_2_linha,3)}
                        '''

def calcula(a_entry,b_entry,c_entry,label_resposta,label_desenvolvimento_delta,label_desenvolvimento_x):
    '''
    Válida, Cálcula e exibe na tela com base nós valores A, B e C recebidos.
    Tratamentos:
    ZeroDivisionError, impede que o valor A seja Zero o que poderia acarretar em erro.
    ArithmeticError, erro manuamente posto quando o valor de delta for 0. (Quando o valor do delta é 0 é impossível cálcular).
    ValueError, impede que o usuário coloque letras por exemplo nos entry´s o que poderia acarretar em quebra da aplicação.
    :param a_entry: Valor do A, será tratado.
    :param b_entry: Valor do B, será tratado.
    :param c_entry: Valor do C, será tratado.
    :param label_resposta: É o label onde será exibida a resposta do cálculo resulmido.
    :param label_desenvolvimento_delta: É o label onde será exibida a resolução completa do cálculo do delta.
    :param label_desenvolvimento_x: É o label onde será exibida a resolução completa do cálculo dos X´ e X´´.
    :return: any
    '''
    label_resposta["text"] = ""
    label_desenvolvimento_delta["text"] = ""
    label_desenvolvimento_x["text"] = ""

    valor_a = a_entry().replace(",", ".")
    valor_b = b_entry().replace(",", ".")
    valor_c = c_entry().replace(",", ".")

    try:
        valor_a = float(valor_a)
        valor_b = float(valor_b)
        valor_c = float(valor_c)

        delta = (valor_b**2) - (4*valor_a*valor_c)
        if delta < 0:
            desenvolvimento_delta(valor_a, valor_b, valor_c, delta, label_desenvolvimento_delta)
            raise ArithmeticError
        else:
            raiz_delta = sqrt(delta)
            x_linha =  (-(valor_b) + (raiz_delta))/(2*valor_a)
            x_2_linha = (-(valor_b) - (raiz_delta))/(2*valor_a)

            label_resposta["text"] = f'''X´ = {round(x_linha,3)}
    X´´ = {round(x_2_linha,3)}'''
            desenvolvimento_delta(valor_a,valor_b,valor_c,delta,label_desenvolvimento_delta)
            desenvolvimento_x(valor_a,valor_b,valor_c,delta,raiz_delta,x_linha,x_2_linha,label_desenvolvimento_x)

    except ZeroDivisionError as e:
        print(e)
        label_resposta["text"] = "O valor de A não pode ser 0"
    except ArithmeticError as e:
        print(e)
        label_resposta["text"] = "O valor de Delta é negativo"
    except ValueError as e:
        print(e)
        label_resposta["text"] = "Os valores devem ser números"

if __name__ == '__main__':
    cria_janela()
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

#avaliação
restaurante_praca.avaliar('Gui', 10)
restaurante_praca.avaliar('Lais', 8)
restaurante_praca.avaliar('Emy', 5)
#itens cardapio
bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_paozinho = Prato('Paozinho',2.00, 'O melhor pão da cidade')

# itens no cardapio
restaurante_praca.adicionar_card(bebida_suco)
restaurante_praca.adicionar_card(prato_paozinho)
bebida_suco.aplicar_desconto
prato_paozinho.aplicar_desconto
#outro restaurante
restaurante_mexicano.mudar_status()

def main():
    restaurante_praca.exibir_cardapio
    # Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
from modelos.avaliação import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):    
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao= []
        self._cardapio =[]
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} |{'Avaliação'.ljust(25)} | {'Status'}\n')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} |{restaurante.media} | {restaurante.ativo}')
    
    @property 
    def ativo(self):
        return '✔️' if self._ativo else '✖️'
    
    def mudar_status(self):
        self._ativo = not self._ativo

    def avaliar(self, cliente, nota):
        if 0 <nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media(self):
        if not self._avaliacao:
            return '-'
        soma= sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade = len(self._avaliacao)
        media = round(soma / quantidade,1)
        return media
    
    def adicionar_card(self,item):
        if isinstance (item, ItemCardapio):
            self._cardapio.append(item)
    # código omitido

    @property
    def exibir_cardapio(self):
            print(f'Cardapio do restaurante {self._nome}\n')
            for i,item in enumerate(self._cardapio,start=1):
                    if hasattr(item,'descricao'):
                            mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                            print(mensagem_prato)
                    else:
                            mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                            print(mensagem_bebida)


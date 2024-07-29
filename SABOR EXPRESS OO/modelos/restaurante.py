from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() # title() transforma a primeira letra maiuscula
        self._categoria = categoria.upper() # upper transforma tudo em maiusculo
        self._ativo = False # '_' deixa como protegido
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'NOME RESTAURANTE'.ljust(25)} | {'CATEGORIA'.ljust(25)} | {'AVALIAÇÃO'.ljust(25)} | {'ATIVO'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')

    @property #mudar como o atributo vai ser lido
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alterar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        
    @property       
    def media_avaliacao(self):
        if not self._avaliacao:
            return f' - '
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) #para cada avaliacao pega somente o valor das notas e soma
        quantidade_notas = len(self._avaliacao) #calcula quantas notas tem pelo tamanho do vetor
        media_notas = round(soma_das_notas/quantidade_notas, 1) #round utiliza-se para escolher quantas casas decimais quer depois da virgula
        return media_notas
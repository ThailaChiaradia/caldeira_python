from modelos.restaurante import Restaurante 

restaurante_tokiomaki = Restaurante('tokiomaki', 'japonesa')
restaurante_tokiomaki.receber_avaliacao('Thaila', 10)
restaurante_tokiomaki.receber_avaliacao('patricia', 4)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
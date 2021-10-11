import random


class Anagramas:
    def __init__(self, caminho, posicao):
        self.posicao = posicao
        self._arquivo = caminho
        self.imprimir_cabecalho(self.posicao)
        self.executar_rodadas()

    @staticmethod
    def imprimir_linha(tamanho):
        print('=' * tamanho)

    @staticmethod
    def embaralha(palavra):
        a = random.sample(palavra, len(palavra))  # randomiza a palavra
        d = ''.join(a).upper()  # insere como string
        return d  # retorna o string da palavra randomizada

    @staticmethod
    def fazer_leitura(caminho):
        arquivo = open(caminho, mode='r', encoding='utf-8')  # abre e lê o arquivo
        palavras = arquivo.readlines()  # após a leitura, transforma todas as linhas em um list
        arquivo.close()  # fecha o arquivo
        return palavras

    @staticmethod
    def mostrar_anagrama(anagrama, tamanho):
        print(f'Anagrama: {anagrama}'.center(tamanho))

    @staticmethod
    def mostra_resultado(chance, tentativas, pontuacao):
        print(f'Chances: {chance} de {tentativas}.')
        print(f'Pontuação: {pontuacao} pontos.')

    @staticmethod
    def mostrar_fim_do_programa(pontuacao):
        print('Acabaram suas chances!')
        print(f'A sua pontuação foi de {pontuacao} pontos.')
        print('Fim do jogo :)')

    def imprimir_cabecalho(self, posicao):
        self.imprimir_linha(posicao)
        print("Descubra a qual palavra o anagrama abaixo se refere!".center(posicao))
        print('A cada rodada é gerado um novo anagrama!'.center(posicao))
        print('Você tem 5 chances para acertar as palavras!'.center(posicao))
        print('A cada acerto você ganha 1 ponto!'.center(posicao))
        print('E a cada erro perde 1 chance e 1 ponto!'.center(posicao))
        self.imprimir_linha(posicao)

    def escolher_palavrar(self):
        palavras = self.fazer_leitura(self._arquivo)
        palavra_escolhida = palavras[random.randint(0, len(palavras) - 1)]  # .upper()
        return palavra_escolhida.strip()  # strip() para remover o '\n' das palavras

    def gerar_anagrama(self, palavra):
        anagrama = self.embaralha(palavra)
        return anagrama

    def novo_anagrama(self):
        palavra_escolhida = self.escolher_palavrar()
        anagrama = self.gerar_anagrama(palavra_escolhida)
        return palavra_escolhida, anagrama

    def jogar_novamente(self):
        entrada = input('Deseja jogar novamente? (S / N): ').strip().upper()
        if entrada == 'S': Anagramas(self._arquivo, self.posicao)
        else: print('Obrigado por jogar! :)')

    def executar_rodadas(self):
        tentativas = 5
        chance = 5
        pontuacao = 0

        while chance != 0:
            palavra_escolhida, anagrama = self.novo_anagrama()  # escolhe a palavra e gera o anagrama

            self.mostrar_anagrama(anagrama, self.posicao)  # imprime o anagrama centralizado na posição desejada
            self.imprimir_linha(self.posicao)

            entrada = input('Descubra a qual palavra o anagrama se refere e insira aqui: ').strip()
            self.imprimir_linha(self.posicao)

            if entrada.upper() == palavra_escolhida.upper():  # acertou
                pontuacao += 1

                print('Parabéns! Você acertou!')
                self.mostra_resultado(chance, tentativas, pontuacao)
                self.imprimir_linha(self.posicao)
            else:  # errou
                chance -= 1
                if pontuacao > 0: pontuacao -= 1
                print(f'Você errou a palavra! A palavra era {palavra_escolhida.upper()}.')
                self.mostra_resultado(chance, tentativas, pontuacao)
                self.imprimir_linha(self.posicao)

            if (chance == 0):  # acabaram as chances
                self.mostrar_fim_do_programa(pontuacao)
                self.imprimir_linha(self.posicao)
                self.jogar_novamente()


def main():
    Anagramas('palavras.txt', 75)


if __name__ == '__main__':
    main()

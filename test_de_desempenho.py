import time
import tipos_de_ordenacao
import random

class Test_de_desempenho:

    def caminho(self):
        return tipos_de_ordenacao.Tipos_de_ordenacao()

    def geracao_de_valores(self, tamanho_da_lista):
        lista = [random.randrange(1000) for i in range(tamanho_da_lista)]
        return lista

    def test_selecao_direta(self, tamanho_da_lista):
        lista = self.geracao_de_valores(tamanho_da_lista)
        tempo_de_inicio = time.time()
        self.caminho().selecao_direta(lista)
        tempo_final = time.time()
        print("Tempo necessário para ordenar a lista usando o seleção direta:", tempo_final - tempo_de_inicio,"segundos.")

    def test_insertion_sort(self, tamanho_da_lista):
        lista = self.geracao_de_valores(tamanho_da_lista)
        tempo_de_inicio = time.time()
        self.caminho().insertion_sort(lista)
        tempo_final = time.time()
        print("Tempo necessário para ordenar a lista usando o insertion sort:", tempo_final - tempo_de_inicio,"segundos.")

    def test_bubble_sort(self, tamanho_da_lista):
        lista = self.geracao_de_valores(tamanho_da_lista)
        tempo_de_inicio = time.time()
        self.caminho().bubble_sort(lista)
        tempo_final = time.time()
        print("Tempo necessário para ordenar a lista usando o bubble sort:", tempo_final - tempo_de_inicio,"segundos.")

o = Test_de_desempenho()
o.test_selecao_direta(5000)
o.test_bubble_sort(5000)
o.test_insertion_sort(5000)
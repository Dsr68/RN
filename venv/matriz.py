from random import randint

class Matriz:
    def __init__(self, linhas, colunas):
        self.__linhas = linhas
        self.__colunas = colunas


    def setLinhas(self, linhas):
        self.__linhas = linhas


    def setColunas(self, colunas):
        self.__colunas = colunas

    @property
    def getLinhas(self):
        return self.__linhas

    @property
    def getColunas(self):
        return self.__colunas




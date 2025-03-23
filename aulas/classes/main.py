# # Formas de fazer sistemas complexos

# # Para criar outro vendedor você precisaria criar outras variáveis
# # Vendedores são instâncias do mesmo objeto
# vendedor = "Lira"
# vendas = 400
# meta = 500
 
# if vendas >= meta:
#     print("Bateu a meta")
# else:
#     print("Não bateu a meta")


# Programação orientada a objetos
class ControleRemoto(): # Objeto
    def __init__(self, cor, altura, profundidade, largura):
        """
        __init__ = inicializa a classe
        Caracteristicas do objeto dentro da função init
        Em outras palavras tudo que precisa estar presente na \
        criação do objeto vai ser declarado dentro da função __init__
        self = Faz referência a instância do objeto 
        """
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
    # Métodos
    def passar_de_canal(self, botao):
        if botao == "+":    
            return "Próximo canal"
        elif botao == "-":
            return "Canal anterior"
        else:
            return 1
# Instâncias da classe ControleRemoto
controle_remoto = ControleRemoto("Preto", 22, 6.8, 15)
controle_remoto2 = ControleRemoto("cinza", 22, 6.8, 151)

print(controle_remoto.passar_de_canal("+"))
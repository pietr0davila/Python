import sys
"""
Classe para clientes da netflix
    Caracteristicas
        - Nome
        - Email
        - Senha
        - Cartão de crédito
        - Número de telefone
    Métodos
        - Pagar a mensalidade
        - Assistir a um filme
        - Assistir a uma série    
"""
 
class Clients():
    def __init__(self, name, plan, balance):
        # Função para criar as caracteristicas do cliente
        self.name = name
        self.monthly_fee_active = False
        try:
            self.plans_list = ["default", "premium"]
            if plan not in self.plans_list:
                raise ValueError("O Plano solicitado não existe! Consulte nosso suporte")
            self.plan = plan
            self.balance = balance
            self.pay_monthly_fee()
        except ValueError as e:
            print("ERRO: ", e)
    
    def pay_monthly_fee(self):
        try:
            if self.balance < 120:
                raise ValueError("Você não tem saldo o suficiente para assinar!")        
            print("Mensalidade paga!")
            self.balance -= 120
            self.monthly_fee = True
        except ValueError as e: 
            print("ERRO: ", e)
            sys.exit(1)
    
    def watch_movie(self, movie):
        try:     
            if self.monthly_fee == False:
                raise ConnectionError("Não conseguimos estabelecer conexão com o servidor")
            print(f"Dando play no filme {movie}")  
        except ConnectionError as e:
            print("ERRO: ", e)

    def watch_serie(self, serie):
        try: 
            if self.monthly_fee == False:
                raise ConnectionError("Não conseguimos estabelecer conexão com o servidor")
            print(f"Dando o play na série {serie}")
        except ConnectionError as e:
            print("ERRO: ", e)
    
    def change_plan(self, new_plan):
        try:
            if new_plan in self.plans_list:
                if new_plan == self.plan or self.monthly_fee == False:
                    raise ValueError("Ocorreu um erro ao trocar seu plano, verifique as informações")
                self.plan = new_plan
                print(f"Plano atualizado para {self.plan}")
        except ValueError as e:
            print("ERRO: ", e)
netflix_client_1 = Clients("Letícia", "default", 200)
netflix_client_1.change_plan("premium")
 
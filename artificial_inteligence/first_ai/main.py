import pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot

# No geral: 
# Independente -> features (entradas / atributos variáveis)
# Dependente -> target (saída / atributo fixo)

dataset = {
    # Os padrões que a IA conhece sobre casas
    # A IA usa esses dados para prever o preço de uma casa com outros atributos
    "Size (sq ft)": [1500, 2000, 2500, 3000, 3500],
    "Bedrooms": [2, 3, 4, 5, 6],
    "Age (years)": [10, 15, 20, 25, 30],
    "Price (USD)": [300000, 400000, 500000, 600000, 700000]
}

# Transcrição do dataset para dataframe
df = pandas.DataFrame(dataset)


independent_vars = df[["Size (sq ft)", "Bedrooms", "Age (years)"]] # Os atributos independentes podem variar e são usados para prever o preço 
# OBS: Normalmente chamada de X (Maiúsculo)
dependent_var = df["Price (USD)"] # O preço depende dos atributos independentes, tendo em vista que o preço de uma casa muda de acordo com diferentes tipos de casas
# OBS: Normalmente chamada de y (minúsculo)
# df[...] -> cria um novo dataframe com as colunas selecionadas
independent_train, independent_test, dependent_train, dependent_test = train_test_split(independent_vars, dependent_var, test_size=0.2, random_state=42)
# test_size=0.2 - 20% dos dados redirecionados para teste
# random_state=42 - define embaralhamento o embaralhamento e msm resultado em todas as execuções
# print("Treino independente: ") 
# print(independent_train) # Ensina a IA a reconhecer padrões de atributos (usa 80% dos dados)
# print("Treino dependente: ")
# print(dependent_train) # Treina a IA a reconhecer padrões de preço correspondentes aos dados
# print("Teste independente: ")
# print(independent_test) # Um teste com 20% dos dados para verifiar se a IA consegue generalizar dados (generalizar: aplicar o que aprendeu em novos dados)
# print("Teste dependente: ")
# print(dependent_test) # Um teste para comparar posteriormente com as previsões

model = LinearRegression() # Cria um modelo de IA que testa uma fórmula que relacione entrada -> saída com base no dataset 

model.fit(independent_train, dependent_train) # treina o modelo calculando e ajustando o coeficiente e intercepto
# coeficiente = o quanto cada entrada influencia o preço
# intercepto = Valor base do preço quando todos os atributos forem 0
# preco = coef1 * size + coef2 * bedrooms + coef3 * age + intercepto
print("Modelo treinado com sucesso!")

predict = model.predict(independent_test)

print("Preços esperados: ")
print(predict)
print("Preço atual: ")
print(dependent_test.values)
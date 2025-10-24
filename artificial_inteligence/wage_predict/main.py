import numpy as npy
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
def main():
    X_train, X_test, y_train, y_test = train_tests()
    print("[1] Adicionar trabalhador")
    option = int(input("> "))
    model = create_model(X_train, y_train)
    choose(option, model, y_test)
    
def create_dataset():
    dataset = {
        "exp": [1, 3, 5, 7, 10],
        "education": [1, 2, 2, 3, 3],
        "age": [22, 25, 30, 35, 40],
        "wage": [30000, 45000, 60000, 80000, 100000]
    }
    df = pd.DataFrame(dataset)
    independent_vars = df[["exp", "education", "age"]]
    dependent_var = df["wage"]
    return [independent_vars, dependent_var]


def choose(option, model, dependent_test):
    match option:
        case 1:
            person = new_employee()
            predict = make_prediction(model, person)
            calc_errors(predict, dependent_test)
            print_predict(predict)

def calc_errors(predicts, y_test):
    mse = mean_squared_error(predicts, y_test)
    print("A taxa de erro quadrádico é de: ", mse)
def new_employee():
    print("Experiência do contratado: ")
    exp = int(input("> "))
    print("Nível de escolaridade: ")
    scholarity = int(input("> "))
    print("Idade: ")
    age = int(input("> "))
    data = pd.DataFrame([[exp, scholarity, age]], columns=["exp", "education", "age"])
    return data
    
    


def train_tests():
    X, y = create_dataset()
    independent_train, independent_test, dependent_train, dependent_test = train_test_split(X, y, train_size=0.8, random_state=42)
    return [independent_train, independent_test, dependent_train, dependent_test]

def create_model(ind_train, dep_train):
    model = LinearRegression()
    model.fit(ind_train, dep_train)
    return model

def make_prediction(model, values):
    return model.predict(values)

def print_predict(predict):
    print("Tendo em vista os dados, imagino que: ")
    print(predict)
    
if __name__ == "__main__":
    main()
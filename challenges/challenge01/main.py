# -*- coding: utf-8 -*-
"""
-Um número será gerado pra AI 1 e AI 2 cada roda;
-Se o número de AI 1 for igual a AI 2 é empate
-Se o número de AI 1 for maior que AI 2, ela ganha 1 ponto
-Se for o contrário AI 2 ganha 1 ponto
-No final de cada rodada deve mostrar a pontuação dos 2
-No final do jogo deve mostrar a pontuação final dos 2 
"""
from random import randint

bot_1_points = 0
bot_2_points = 0

def create_game():
    for i in range (0, 3):
        number_1 = randint(1, 10)
        number_2 = randint(1, 10)
        treatment(number_1, number_2)

def treatment(AI_1, AI_2):
    global bot_1_points, bot_2_points
    print(f"Numero escolhido por bot 1: {AI_1}")
    print(f"Numero escolhido por bot 2: {AI_2}")
    if AI_1 == AI_2:
        print("Empate")
        print("Os pontos permanecem iguais")
    elif AI_1 > AI_2:
        print("O bot 1 venceu a rodada!")
        print("Bot 1 ganhou um ponto!")
        bot_1_points = bot_1_points + 1
    else:
        print("O bot 2 venceu a rodada!")
        print("O bot 2 ganhou um ponto!")
        bot_2_points = bot_2_points + 1
    print(f"Pontuacao bot 1: {bot_1_points}")
    print(f"Pontuacao bot 2: {bot_2_points}\n")
create_game()

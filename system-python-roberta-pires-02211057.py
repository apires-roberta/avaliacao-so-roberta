# Roberta Pires - 02211057
# Avaliação SO
from mysql-python.py import *
nObs = 0
i = 0

print("Bem vindo a pesquisa do Blank Paper!\n Uma pesquisa feita para me ajudar como artista :) ")
print("------------------------------------------------------------")
nome = input("Primeiramente, qual o seu nome?")
print("------------------------------------------------------------")
cpf = input("Qual o seu CPF?")
print("Escolha qual a sua preferência artística: ")
opcao_selec = input("1 - Arte Tradiconal\n2 - Arte Digital\n\n")
if opcao_selec == "1":
    nObs = int(input("Quantos desenhos você quer ver?:\n"))
    for i in range(nObs):
        if i == nObs:
            break
        print("---------------", i+1, "° Desenho - (Para vizualizar com cores acesse https://www.instagram.com/p/CRmjqHBhyLK/)------------------")
        print("    ⠂⠀⠀⠀⠄⠀⠱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⣰⡤⠀⠀⠁⢀⠀⠈⠉⠀⠰⠟⠉⠀⠀⠀⠂⠀⡀⠀⠀⠀⠀")
        print("     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⡀⢳⡄⠀⠸⡁⠀⠀⣴⣾⠁⠀⠀⠀⠀⠀⠀⠀⠐⠒⠀⠟⠁⠀⣶⠀⠀")
        print("     ⠀⠀⠀⠀⠀⢠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣦⠀⠀⠑⢾⣿⣄⣠⣿⣶⣿⣿⠃⠀⠀⠀⣀⣐⣦⠀⠀⠀⠀⢀⣜⣁⠀⠀⠤⠤")
        print("     ⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣦⡀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠑⠋⠉⠁⠀⠀⠀")
        print("     ⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⣧⡄⠀⠀⠀⢸⣷⣾⣿⣿⣿⣷⣴⣿⣿⣿⣿⡿⠛⠉⠉⠀⣠⢸⣿⣿⣇⣠⣤⣶⣤⣤⣤⠀⠀⠀⢠⣄⠀")
        print("     ⠀⠀⠀⠀⠡⠄⠀⠀⠀⠀⣧⣾⣿⣦⡀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⢳⢰⣶⣾⣿⣫⣶⣶⣝⠿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠸⠋⠀")
        print("     ⠀⠀⠀⠀⠀⠀⠲⣤⣄⣴⣿⣿⣿⣿⣷⣀⣼⣿⣿⣿⣿⣿⣿⡿⠟⣩⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⠻⣿⣿⣿⣿⣿⣧⡀⠄⠀⠀")
        print("     ⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣡⣴⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣉⡛⠿⠙⢿⣷⣌⡛⢿⣿⣿⣿⡄⠀⠀⠀")
        print("     ⠀⢀⣠⣤⣾⣿⣿⣿⣿⡿⠛⠛⠛⣋⣉⣉⠉⠉⣥⣶⣶⣿⡿⠟⢉⣡⡄⢿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠈⢹⣿⡷⢼⣿⣿⣿⣷⡀⠀")
        print("     ⠈⠉⢿⣿⣿⠿⠟⠋⠅⠾⢛⣛⣛⣛⣛⣛⣠⣀⣛⣛⣋⣡⣴⣾⣿⣿⣷⢸⣿⣿⣿⣿⣿⣿⣿⣿⢇⣙⡇⣚⣩⣶⣿⣟⡋⠉⠁⠀⠀")
        print("    ⠀⠀⠀⠹⣿⣀⣠⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⡟⣸⣿⣿⣿⣿⣿⠿⠟⠛⠀⠀⠠⠀⠀")
        print("     ⠀⠀⠀⠀⠈⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡜⣿⣿⣿⣿⣿⣿⣿⠁⣿⣿⣿⣿⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("    ⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡙⠛⠿⠿⠿⠟⠃⣸⣿⢿⠿⠛⡛⠋⠀⠀⢀⣀⠀⠀⠀⠀")
        print("   ⠒⠣⠆⠀⠀⠀⠘⠻⡿⣿⣿⣿⠟⣫⣴⣶⣶⣶⣮⣙⡛⠿⢿⣿⣿⣿⣿⠟⠛⠉⣥⣀⡐⠛⠻⣿⣧⣤⣄⡀⠘⠀⠀⠀⠀⠈⠀⠀⠀⠀")
        print("     ⠀⠀⠀⢀⠀⠀⠀⢀⣴⣿⡿⠿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣬⡛⠿⢋⣼⣷⣶⣦⣤⣴⣶⡆⢹⣿⣿⣿⣿⣷⣦⡀⠀⠀⡠⠀⠠⠆⠀")
        print("     ⠀⡀⡀⠀⢃⣠⣶⣿⡟⣴⣶⣶⡇⢹⣿⣿⣿⡙⣿⣿⣿⣿⣿⣿⣿⣶⣌⡛⢿⣿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⡀")
        print("     ⠀⣈⡃⠀⠀⠙⣿⣿⡇⣿⣿⣿⣿⠈⢿⣿⡿⠧⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠙⠿⢇⣿⣿⣿⡇⢻⣿⣿⣿⣿⣿⣿⣷⣤⣀⣄⠀⠀⠁")
        print("     ⣄⠀⠀⠀⢀⣀⢹⣿⣷⣜⠿⣿⣿⣿⠖⠀⠀⠀⠙⣦⡙⠿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣻⣿⣿⣿⡇⣸⣿⣿⣿⣿⣿⣿⠿⠟⠛⢹⢤⠀⢴")
        print("    ⠨⡿⢖⣶⣿⣿⣿⣿⣿⣿⣶⣌⠻⣿⡆⢲⣿⣿⠆⠻⢿⣦⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⣿⣿⣿⣿⣿⠉⠁⠀⠀⠀⠈⠀⠀⠈")
        print("      ⠀⠀⠀⠉⠁⠸⣻⣿⣿⣿⣿⣿⣷⣤⡙⠘⣿⣿⢠⠘⣶⣌⣙⠢⠉⠻⣿⣿⣿⣿⣿⣿⠿⢋⣠⣿⣿⣿⡏⠛⢻⠷⣶⣦⢄⣠⠀⠀⡀⠀")
        print("      ⡶⠅⢀⣤⠂⠀⠋⠀⠙⠻⣿⣿⣿⣿⣿⣆⢻⣿⢸⣷⡈⢻⣿⣿⣶⣶⣤⣬⣭⣭⣥⣴⣶⣿⣿⣿⣿⣿⣷⡄⠀⠀⠹⣧⠀⠉⠀⠀⢠⠤")
        print("      ⠀⠀⠉⠀⠀⣀⠄⠀⢀⣴⣿⣿⣿⣿⣿⡇⣾⣿⡌⠻⣿⣦⡙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠁⠀⠀⠀⠀⠀⠀")
        print("     ⣴⠾⠖⠒⠐⠁⣠⣴⠿⠋⣹⣿⣿⣿⣿⠃⣿⣿⢇⣷⠹⣿⣿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⠟⠻⠄⠀⠀⠀⠀⠀⢠⠀⠀")
        print("     ⠀⣀⠀⠀⠀⠿⠏⠈⢀⣀⣿⣿⣿⣿⡟⢰⣿⠁⣿⣿⡇⣿⡇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠂⠉⠿⠿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀")
        print("     ⣡⠘⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣅⣈⣉⣴⣿⣿⠰⠿⠇⣿⣿⣿⣿⠟⠻⠋⠀⠀⠿⠛⢿⡀⢰⡆⠀⠀⠀⠀⠀⠸⠟⠆⠀⢀⠀⠀")
        print("     ⠃⠀⣴⠆⠐⠃⠀⣀⠀⡀⠙⣿⣿⣿⣿⣿⠿⣿⣿⣿⣷⣾⣿⣿⣿⠋⠀⠀⠀⢂⠀⠀⠀⢀⡀⠁⠀⠀⡐⠀⠈⠀⡀⠁⢠⡦⠀⠀⢰⡇")
        print("     ⠀⠾⠃⠀⠀⠀⠀⠀⠰⡀⠀⠈⠿⠟⠁⠀⠀⠘⠛⢿⣿⠿⠛⠙⠛⠐⠀⠀⠀⠚⢧⡀⠀⠈⠉⠀⠀⠀⢠⠀⠀⡔⠀⠀⠻⠁⢠⠀⠺⠃")
        print("     ⡔⠃⣠⡖⠀⠀⠂⠀⠀⡀⠀⣆⠀⠠⠞⠁⠀⠀⠀⠈⠁⢀⡀⠀⠀⠁⠀⠀⠀⠀⢠⣇⠀⠰⣄⣀⡀⠀⠘⠀⠀⡀⠀⢠⠀⠀⡟⠀⠀⠀")
        print("---------------------------------\n\n")
elif opcao_selec == "2":
    nObs = int(input("Quantas desenhos você quer ver?:\n"))
    for i in range(nObs):
        if i == nObs:
            break
        print("---------------", i+1, "° Desenho - (Para vizualizar com cores acesse https://www.instagram.com/p/CTrvO24gSV-/)------------------")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡛⠛⣛⣋⡐⠛⠛⠿⠟⠿⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠍⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠔⣴⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠜⠁⢱⣽⣿⠀⠻⣿⣿⣿⣮⣿⣯⣿⣿⣿⣿⣿⣷⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣘⢡⣿⣿⠏⠀⠀⠈⠛⠻⢿⣿⣽⠿⣿⡿⣿⣿⣿⣧⠸⣿⠿⢛⡛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⣄⣿⡿⠁⠀⠀⠀⠀⠀⠀⠁⠙⠙⠻⢮⢟⢯⢿⣿⡿⡇⠐⠚⣩⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⡟⠤⣹⡟⡁⠀⠀⠀⠀⠀⡤⡒⠄⠀⠀⠀⠀⠀⠀⠟⢩⢠⣿⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡶⢆⣿⠀⡀⠀⠀⠀⠀⠀⠋⠀⠀⠠⠀⠀⠀⠀⠀⠐⠋⣾⣿⣆⢘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢾⣏⣦⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⣿⣿⣷⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣧⣺⣟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡈⣿⣿⣸⣇⠀⠀⠀⠒⠀⠀⠀⠀⠀⠀⠀⠀⡰⢠⣿⣿⣿⣿⡟⣰⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢣⣿⣿⣿⣿⣆⠀⠀⢤⠦⠀⠀⠀⠀⠀⠀⠰⠁⢺⣿⣿⣿⢟⡂⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⡒⢝⣿⣿⣮⣿⣦⡀⠀⠀⠀⠀⠀⣀⡤⠂⠀⢐⣿⠿⠋⡱⠎⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣱⣽⣿⣪⢻⡿⣦⣄⣴⣶⠿⠋⠀⠀⠀⠃⠀⢪⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣶⡿⢿⣿⣻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢽⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠹⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠙⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠄⠀⠀⠀⠀⠀⠀⢀⠄⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⡛⣿⠁⠀⠀⠀⢘⢲⣬⣥⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠲⠶⠶⣘⣿⣿⠀⠀⠀⢼⣿⠀⠀⠀⠀⠀⣲⡟⠀⠀⠀⠀⠈⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣴⣶⣿⣿⡏⠀⠀⠀⢹⡎⠀⠀⢀⣀⠀⡾⠀⠀⠀⠀⠀⠀⢰⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠈⣏⣢⣉⣉⣩⣺⣿⡄⢀⣀⣀⣤⡮⣮⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣯⣿⣯⣛⣛⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠢⣤⣤⣴⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣭⣭⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")

    insert_db(nome, cpf)

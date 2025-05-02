import random
import time

print("=========================================")
print("          CORRIDA DE CARROS.            " )
print("=========================================")

jogador1 = input("Jogador 1: ")
jogador2 = input("Jogador 2: ")

print("O jogo vai começar em:") 

for contador in range(3, 0, -1):
       time.sleep(1.2)
       print(contador) 

pos1 = 0
pos2 = 0

linha_de_chegada = 30


carro1 = """       
       ____ 
   __/      \__ 
  [  @ ____ @  ]"""

carro2 = """     
       ____ 
   __/      \__ 
  [  @ ____ @  ] """

while pos1 < linha_de_chegada and pos2 < linha_de_chegada:
        time.sleep(0.5)

        #bibliotecas
    
        mov1 = random.randint(1, 5)
        mov2 = random.randint(1, 5)
    

        pos1 += mov1
        pos2 += mov2 

if pos1 >= linha_de_chegada and pos2 < linha_de_chegada:
       print(f"{jogador1} foi campeão")
elif pos2 >= linha_de_chegada and pos1 < linha_de_chegada 
       print (f"{jogador2} foi campeão")
elif pos1 == linha_de_chegada and pos2 == linha_de_chegada 
       print("A corrida empatou!")


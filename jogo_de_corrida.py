import random
import time
import os
                            #parte inicial de menu e seleçãoo de jogadores 

print("=========================================") 
print("          CORRIDA DE CARROS.            " )
print("=========================================")

jogador1 = input("Jogador 1: ")
jogador2 = input("Jogador 2: ")

print("O jogo vai começar em:") 

for contador in range(3, 0, -1):
       print(contador) 
       time.sleep(1.2)  #essa biblioteca de tempo, ela vai controlar o tempo do while
                        #exemplo, enquanto não chegar no 0, printa o contador com 1.2 segundos de atraso entre cada numero  
pos1 = 0
pos2 = 0

linha_de_chegada = 100


carro1 = """       
       ____ 
   __/      \__ 
  [  @ ____ @  ]"""

carro2 = """     
       ____ 
   __/      \__ 
  [  @ ____ @  ] """

carro1_linhas = carro1.splitlines() 
carro2_linhas = carro2.splitlines() #splitlines vai cortar o carro em varias linhas, como meu carro tem varias quebras de linhas 
                                    #é interessante cortar pra ele não fizer zuado

while pos1 < linha_de_chegada and pos2 < linha_de_chegada:
        time.sleep(0.5) 
        


       #bibliotecas usadas
        
        os.system('cls')                  #essa biblioteca vai apagar tudo do terminal quando a corrida começar 
        mov1 = random.randint(1, 5)       #random = bliblioteca faz com que o numero de espaços de cada carro seja aleatorio 
        mov2 = random.randint(1, 5)       #random.ranit(a,b) = retora um numero aleatorio entre a e b, que for maior vence 
    

        pos1 += mov1 
        pos2 += mov2 


#
        for linha in carro1_linhas:  
            print(" " * pos1 + linha)
        print(" " * pos1 + jogador1)

        print("="*linha_de_chegada)

    
        for linha in carro2_linhas:        
            print(" " * pos2 + linha)
        print(" " * pos2 + jogador2)      #a lógica aqui foi o seguinte, enquato um não chegar, limpa o terminal e printa 
                                          #um espaço * a posição (que foi gerada no random) + concatenado com o carro, o espaço vai "andar" junto com o carro 



#no caso aque ele decide quem é o maior do numero gerado lá no random 

    
if pos1 >= linha_de_chegada and pos2 < linha_de_chegada: 
       print(f"{jogador1} foi campeão")

elif pos2 >= linha_de_chegada and pos1 < linha_de_chegada:

       print (f"{jogador2} foi campeão")

else:

       print("A corrida empatou!")


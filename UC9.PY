from random import randint
 
print("seja bem-vindo ao jogo de advinhação!")
print("você tem 10 tentativas para acertar o número aleatório.")

random = randint(1, 100)
chute = 0;
chances = 10;

while chute != random:
    chute = input("Chute um número entre 1 a 100: ")
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1
        if chute == random:
            
            print("Parabéns, você venceu! O número era {}.".format(random, chances))
            break;
        
        else:
            if chute > random:
                print("Você errou! Dica: É um número menor.")
            else:
                print("Você errou! Dica: É um número maior.")
            print("Você ainda possui {} chances.".format(chances))
        if chances == 0:
            print("Suas chanches acabaram, você perdeu!")
            
            break;
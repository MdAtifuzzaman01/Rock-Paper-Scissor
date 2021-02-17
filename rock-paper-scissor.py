import random

def play():
    user = input("What's your choice? : 'r' for rock, 's' for scissors 'p' for papers\n")
    computer = random.choice(['r','p','s'])
    if user== computer:
        return "tie"

    if is_win(user,computer):
        return "You won"
    return "You lost!"
def is_win(player,opponent):

    if (player =="r" and opponent =="s") or (player == "s" and opponent =="p")\
        or (player =="p" and opponent == "r"):
        return True
print(play())        





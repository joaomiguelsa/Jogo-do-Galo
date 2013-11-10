import turtle
import math

def go_to(x,y,orient):
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(orient)
    turtle.pendown()
    #print(turtle.position())
      
def board():
    go_to(-100,100,0)
    board_maker()
    go_to(-100,-100,0)
    board_maker()    
    go_to(100,100,0)
    board_maker()
    go_to(100,-100,0)
    board_maker()

def board_maker():
    for i in range(4):
        turtle.right(90)
        turtle.forward(150)
        turtle.backward(150)

def check(board_ac):
    if board_ac[0] == board_ac[1] == board_ac[2] or board_ac[0] == board_ac[3] == board_ac[6] or board_ac[0] == board_ac[4] == board_ac[8] or board_ac[1] == board_ac[4] == board_ac[7] or board_ac[2] == board_ac[5] == board_ac[8] or board_ac[3] == board_ac[4] == board_ac[5] or board_ac[6] == board_ac[7] == board_ac[8] or board_ac[2] == board_ac[4] == board_ac[6]:
        return True
    else:
        return False

def player_turn(n_jogada, board_ac):
    jogada_valida=0
    if (-1)**n_jogada == -1:
        while jogada_valida!=1:
            jogada=int(eval(input("Player 1 Turn:\t")))

            if board_ac[jogada-1]==1 or board_ac[jogada-1]==-1:
                print('Introduze a valid coord!')
                continue     
            
            
            if int(jogada) ==1 or int(jogada) ==2 or int(jogada) ==3 or int(jogada) ==4 or int(jogada) ==5 or int(jogada) ==6 or int(jogada) ==7 or int(jogada) ==8 or int(jogada) ==9:
                jogada_valida=1
            else:
                print('Introduze a valid coord!')
    else:
        while jogada_valida!=1:
            jogada=int(input("Player 2 Turn:\t"))
            
            if board_ac[jogada-1]==1 or board_ac[jogada-1]==-1:
                print('Introduze a valid coord!')
                continue            
            
            if int(jogada) ==1 or int(jogada) ==2 or int(jogada) ==3 or int(jogada) ==4 or int(jogada) ==5 or int(jogada) ==6 or int(jogada) ==7 or int(jogada) ==8 or int(jogada) ==9:
                jogada_valida=1
            else:
                print('Introduze a valid coord!')
    atri((-1)**n_jogada,int(jogada), board_ac)
    return board_ac

def player1_symbol(jogada):
    if jogada == 1:
        go_to(-200,200,45)
    elif jogada==2:
        go_to(0,200,45)
    elif jogada==3:
        go_to(200,200,45)
    elif jogada==4:
        go_to(-200,0,45)
    elif jogada==5:
        go_to(0,0,45)
    elif jogada==6:
        go_to(200,0,45)
    elif jogada==7:
        go_to(-200,-200,45)
    elif jogada==8:
        go_to(0,-200,45)
    elif jogada==9:
        go_to(200,-200,45)
        
    turtle.pencolor('green')
    for i in range(4):
        turtle.forward(75)
        turtle.backward(75)
        turtle.right(90)
    
def player2_symbol(jogada):
    if jogada == 1:
        go_to(-275,200,-90)
    elif jogada==2:
        go_to(-75,200,-90)
    elif jogada==3:
        go_to(125,200,-90)
    elif jogada==4:
        go_to(-275,0,-90)
    elif jogada==5:
        go_to(-75,0,-90)
    elif jogada==6:
        go_to(125,0,-90)
    elif jogada==7:
        go_to(-275,-200,-90)
    elif jogada==8:
        go_to(-75,-200,-90)
    elif jogada==9:
        go_to(125,-200,-90)
        
    turtle.pencolor('red')
    turtle.circle(75)    

#Atribui a jogada ao tabuleiro
def atri(player,jogada, board_ac):
    board_ac[jogada-1]= player
    if player==-1:
        player1_symbol(jogada)
    else:
        player2_symbol(jogada)
    
    return board_ac
    
def main():
    board_ac=[10,2,3,4,5,6,7,8,9]
    turtle.screensize(300,300)
    turtle.hideturtle()    
    go_to(0,0,0)
    board()
    #players()
    win=0
    n_jogada=0
    
    player1=input('Player 1:\t')
    player2=input('Player 2:\t')     
    
    while win!=1:
        n_jogada += 1
        if check(board_ac) == True:
            if (-1)**n_jogada == -1:
                win=1
                print(player2, 'Ganhou!')
                
            else:
                win=1
                print(player1, 'Ganhou!')
        else:
            player_turn(n_jogada, board_ac)
    turtle.exitonclick()
    
main()

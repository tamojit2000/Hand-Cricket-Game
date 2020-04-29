from random import *

def bat():
    global runs,L1
    
    print'\nYou are batting.'
    print
    a=input('>>> Throw (0-6) ')
    L1.append(a)
    
    b=L1[randint(0,len(L1)-1)]
    print"Computer's Throw ",b
    if a==0:
        runs+=b
        return True
    
    elif a==b:
        print '\nYou are OUT.'
        return False
    
    else:
        runs+=a
        return True
        
    
def bowl():
    global c_runs,L2
    
    print '\nYou are bowling.'
    print
    a=input('>>> Throw (0-6) ')
    for aa in range(0,7):
        if aa!=a:
            L2.append(aa)
    
    b=L2[randint(0,len(L2)-1)]
    print"Computer's Throw ",b
    if b==0:
        c_runs+=a
        return True
    
    elif a==b:
        print'\nComputer OUT.'
        return False
    else:
        
        c_runs+=b
        return True   
    
    
def display(x):
    global c_runs,runs,wickets,c_wickets
    print
    print'''
===================================
| COMPUTER |
------------
RUNS\t\tWICKETS'''
    print c_runs,'\t\t',c_wickets,'/',x
    print'''
| PLAYER |
----------
RUNS\t\tWICKETS'''
    print runs,'\t\t',wickets,'/',x
    print'==================================='    


def menu():
    print'''
MENU
====

1. NEW GAME
2. INSTRCUCTIONS
3. EXIT

'''
def instructions():
    print'''
INSTRUCTIONS
============

Game rules as usual.
0 means defence.

'''



        
        
def batbowl(x):
    global wickets,c_wickets,runs,c_runs
    c=0
    while True:
        a=bat()
        display(x)
        if a==False:
            c+=1
            wickets+=1
            if c==x:
                break
            
            display(x)
    display(x)
    raw_input()
    c=0    
    while True:
        
        a=bowl()
        
        display(x)
        if c_runs>runs:
            display(x)
            print'\n>>> YOU LOSE <<<'
            raw_input()
            break
        if a==False:
            c+=1
            c_wickets+=1
            if c==x:
                break
            
            display(x)

    if c_runs==runs:
        display(x)
        print'\n>>> MATCH TIED <<<'
        raw_input()
    if c_runs<runs:
        display(x)
        print'\n>>> YOU WON <<<'
        raw_input()
    

def bowlbat(x):
    global wickets,c_wickets
    c=0    
    while True:
        a=bowl()
        display(x)
        if a==False:
            c+=1
            c_wickets+=1
            if c==x:
                break
            
            display(x)

    display(x)
    raw_input()
    c=0
    while True:
        
        a=bat()
        
        display(x)
        if runs>c_runs:
            display(x)
            print'\n>>> YOU WON <<<'
            raw_input()
            break
        if a==False:
            c+=1
            wickets+=1
            if c==x:
                break
            
            display(x)

    if c_runs==runs:
        display(x)
        print'\n>>> MATCH TIED <<<'
        raw_input()
    if runs<c_runs:
        display(x)
        print'\n>>> YOU LOST <<<'
        raw_input()

###############################################main#####################################

  
print'''
HAND-CRICKET GAME
=================
'''
while True:
    menu()
    a=input('>>> ')
    if a==3:
        print'\nGetting Out.'
        print'\n<tamojitdas>'
        
        raw_input()
        exit()
    elif a==2:
        instructions()
        raw_input('<= BACK')
    elif a==1:
        
        runs=0
        c_runs=0
        wickets=0
        c_wickets=0
        L1=[0,1,2,3,4,5,6]
        L2=[0,1,2,3,4,5,6]

        print'\nStarting new game.'.upper()
        wicket=input('Enter Number of Wickets - ')
        print
        b=input('1. Odd or 2. Even - ')
        c=input('>>> Throw (0-6) ')
        d=randint(0,6)
        print"Computer's Throw ",d
        print
        if (d+c)%2==0:
            if b==2:
                print'>>> You won the toss.'
                c=input('1. Bat or 2. Bowl - ')
                if c==1:
                    batbowl(wicket)
                
                else:
                    bowlbat(wicket)
                
            else:
                print'>>> You lost the toss.'
                c=randint(1,2)
                if c==1:
                    print'\nComputer choose to bowl first.'
                    batbowl(wicket)
                else:
                    print'\nComputer choose to bat first.'
                    bowlbat(wicket)
            
        else:
            if b==1:
                print'>>> You won the toss.'
                c=input('1. Bat or 2. Bowl - ')
                if c==1:
                    batbowl(wicket)
                
                else:
                    bowlbat(wicket)
            
            else:
                print'>>> You lost the toss.'
                c=randint(1,2)
                if c==1:
                    print'\nComputer choose to bowl first.'
                    batbowl(wicket)
                else:
                    print'\nComputer choose to bat first.'
                    bowlbat(wicket)
            
            
            
    
    
    

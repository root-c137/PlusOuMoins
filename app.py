import random;
import os


Title = "\n========== NOMBRE MYSTERE ==========\n";
SubTitle = "Devine le nombre mystère en 10 coups !\n";
Proposition = 0;

#Pour clear la console.. 
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def NumberGenerator():
    return random.randint(1, 100);

def Menu():
    MenuList = """
    1. PLAY (1)
    2. QUIT (2)
    """
    return print(Title+SubTitle+MenuList);


def MenuEndGame():
    MenuEndGameList = """
    1. RECOMMENCER (1)
    2. MENU PRINCIPAL (2)
    """

    print(MenuEndGameList)
    try:
        choice = int(input(""));
    except:
        print("\n# Pas compris...")
        MenuEndGame();

    if int(choice) == 1:
        Play();
    elif int(choice) == 2:
        cls();
        Main();
    else:
        cls();
        print("Pas compris dsl...");
        print(MenuEndGame);
   
    
def LifeAndProposition(Life):
        global Proposition; #global pour dire à python qu'on veut modifier la variable global Proposition déclarée plus haut.. 
        CoupTxt = "coup";
        if Life > 1:
            CoupTxt = "coups";

        print(f"\n# Il vous reste {Life} "+CoupTxt+" #\n");
        print("Quel est le nombre mystère ?");

        try:
            #Si y pas d'erreur par rapport à la converstion d'un string en int..
            Proposition = int(input("Ta proposition (entre 1 et 100 inclus) : "));
        except:
            #Sinon...
            cls();
            print("\n=== Il faut entrer un nombre entre 1 et 100 ! ===\n");
            LifeAndProposition(Life);


def Play():
    cls();
    Life = 10;
    NombreMystere = NumberGenerator();
    LifeAndProposition(Life);

    while Life > 0:
        cls();

        if Proposition < NombreMystere:
             print("\n\n*** C'est plus ! ***")
        elif Proposition > NombreMystere:
            print("\n\n*** C'est moins ! ***")
        else:
            print("\n\n********** BRAVOOO **********\n\n Le nombre mystère était bien : ", NombreMystere);
            print("\n\n");
            MenuEndGame();

        Life-=1;
        if Life > 0:
            LifeAndProposition(Life);
                
        if Life == 0:
            cls();
            print("\n\n********** PERDU **********\n\n Le nombre mystère était : ", NombreMystere);
            MenuEndGame();
    

def Main():
    Menu();

    try: # Si y pas d'erreur par rapport à la converstion d'un string en int..
        Choice = int(input(""));
    except: # Sinon...
        cls();
        print("\n# Pas compris...")
        Main();

    print(Choice);

    if int(Choice) == 1:
        Play();
    if int(Choice) == 2:
        exit(0);

# Tout commence ici...
Main();



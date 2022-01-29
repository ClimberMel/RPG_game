# action.py
# define the acction functions here
# str and int are reserved words
# strength str will be stg
# intelligence int will be inl

import event

class character():
    def __init__(self):
        self.charclass = "Human"

    def __str__(self):
        print("You are a ", self.charclass)

    def characteristics(self):
        stg = self.stg
        con = self.con
        dex = self.dex
        inl = self.inl
        hp = self.hp
        mp = self.mp




def intro():
    print(event.e0)
    act1()

def act1():
    print(event.e1)
    act263()

def act2():
    print(event.e2)
    
def act3():
    event.showevent('e3')
    print('a: Do you ask Ruth about what she said?')
    print('b: Do you ask May about what Ruth said?')
    print('c: Do you say nothing?')
    '''If you ask Ruth about what she said, go to 9.
        If you ask May about what Ruth said, go to 15.
        If you say nothing, go to 22'''
    inp = input('Enter your choice')
    while inp not in ('abc'):
        print(inp)
        print('You must enter a, b or c')
        inp = input('Enter your choice')

def act4():
    print(event.e4)

def act5():
    print(event.e5)

def act6():
    print(event.e6)

def act7():
    print(event.e7)

def act8():
    print(event.e8)

def act262():
    print(event.e262)
'''Conduct close-quarters combat using pages 12-13 of the Quick-
Start Rules. You may need to refer to page 7 first to look up your
damage bonus.
The combatant with the higher DEX acts first. You and the artisan
will take one action each combat round. You may fight back (rolling
your Fighting (Brawl) or dodge (using Dodge) against each attack.
Combat rolls are opposed rolls: whoever gets the best level of success wins.
The artisan has a DEX of 41 and a Fighting (Brawl) skill of 35%
(17% half / 7% one-fifth). He has 12 hit points. He will attack you
every combat round, and his successful hits do 1D3 + 1D4 damage.
If you have a knife or similar weapon, each successful hit you make
does 1D4 plus your damage bonus. If you are unarmed, the damage
is 1D3 plus your damage bonus.
After three rounds, you may attempt to circle round behind the
man and escape. This requires a Hard roll, and if you do not achieve
a success on the roll, he may land another blow.
If you reduce the man to 6 or fewer hit points, go to 268.
If you are reduced to 0 hit points, go to 2.
If you successfully escape, go to 12'''



def act263():
    print(event.e263)
    '''Look at your investigator sheet. At the top, you have spaces for eight
    characteristics: Strength (STR), Constitution (CON), Power (POW),
    Dexterity (DEX), Appearance (APP), Size (SIZ), Intelligence
    (INT), and Education (EDU). Allocate the following values among
    them, writing in the large square beside each: 40, 50, 50, 50, 60,
    60, 70, 80. If you would like more information about what these
    characteristics mean, read page 6 of the Quick-Start Rules.
    When you have done that, go to 8.'''

    


act3()

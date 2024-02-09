# action.py
# define the acction functions here
# str and int are reserved words
# strength str will be stg
# intelligence int will be inl

# Turns out that I need to keep track of original stats e263
# and also calc 
import event  # theis is a local module event.py

#---------------------------------------------------------------------------------------
#    CREATE CHARACTER
#---------------------------------------------------------------------------------------
class character():
    def __init__(self):
        self.name = input("What is your name?")
        self.charclass = "Human"
        self.stats = {
            "stg" : [0, 0, 0, 0],        
            "con" : [0, 0, 0, 0],
            "siz" : [0, 0, 0, 0],
            "dex" : [0, 0, 0, 0],
            "app" : [0, 0, 0, 0],
            "edu" : [0, 0, 0, 0],
            "inl" : [0, 0, 0, 0],
            "pwr" : [0, 0, 0, 0],
            "hp" : [0, 0],
            "mp" : [0, 0]}

    def __str__(self):
        # the __str__ function returns a string if you print the class
        # .format(self=self) means that where self occurs inside {} in the format string, 
        # it refers to object referenced by the self variable.
        return '{self.name}, you are a {self.charclass}'.format(self=self)

    def printStats(self):
        #str_stats = 'Your stats are: \nStr: {self.stg} \nCon: {self.con} \nDex: {self.dex} \nInt {self.inl} \nHP: {self.hp} \nMP: {self.mp}'.format(self=self)
        str_stats = '{self.name}, your stats are: \nStr: {self.stats[stg]} \
        \nCon: {self.stats[con]} \
        \nSiz: {self.stats[siz]} \
        \nDex: {self.stats[dex]} \
        \nApp: {self.stats[app]} \
        \nEdu: {self.stats[edu]} \
        \nInt: {self.stats[inl]} \
        \nPwr: {self.stats[pwr]} \
        \nHP: {self.stats[hp]} \
        \nMP: {self.stats[mp]}'.format(self=self)
        #print('Your stats are: \nStr: {self.stg} \nCon: {self.con}'.format(self=self))
        print(str_stats)

#---------------------------------------------------------------------------------------
#    ACTIONS
#---------------------------------------------------------------------------------------
def intro(hero):
    print(event.e0)
    input("press key to cont.")
    act1(hero)
    
def act1(hero):
    print(event.e1)
    input("press key to cont.")
    act263(hero)

def act2(hero):
    print(event.e2)
    
def act3(hero):
    print(event.e3)
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
    if inp == 'a':
        act9(hero)
    elif inp == 'b':
        act15(hero)
    else:
        act22(hero)

def act4(hero):
    print(event.e4)

def act5(hero):
    print(event.e5)

def act6(hero):
    print(event.e6)

def act7(hero):
    print(event.e7)

def act8(hero):
    print(event.e8)
    '''If your SIZ is 40, go to 23. If your SIZ is higher than this, go to 38.'''
    if hero.stats["siz"][1] == 40:
        print('Going to 23')
        act23(hero)
    elif hero.stats["siz"][1] > 40:
        print('Going to 38')
        act38(hero)
    else:
        print('There seems to be a problem in act8, SIZ is: ', hero.stats["siz"][1])
        act270(hero)

def act9(hero):
    print(event.e9)
    act22(hero)

def act15(hero):
    print('Temporary exit')
    print(hero.printStats())

def act22(hero):
    print(hero.name, ' This is the END!!!')

def act23(hero):
    print('Made it to act23')
    print('act23 test', hero.printstats())

def act38(hero):
    print(event.e38)
    act233(hero)

def act134(hero):
    print(event.e134)
    '''Add SIZ and CON together, then divide the total by 10, rounding 
        down. This is the starting value for your hit points.'''
    hero.stats["hp"][0] = (hero.stats["siz"][0] + hero.stats["con"][0]) / 10
    act15(hero)  # temporary exit

def act233(hero):
    print(event.e233)
    '''You will see two smaller boxes to the right of each characteristic 
        value. Halve each value, rounding down, and write the result in the 
        upper right box. Also, divide each value by 5, again rounding down, 
        and write the result in the lower right box. We will use these numbers 
        later. If you are using the interactive PDF version of the investigator 
        sheet, you’ll see it does all of the math for you!
        In the strip below, you will see tracks that record Sanity and 
        magic points. Beginning Sanity is equal to your original POW, and 
        beginning magic points are the same as the value you’ve just assigned 
        for POW divided by 5. Mark these on the tracks.

        Then go to 134'''
    hero.stats["stg"][2] = hero.stats["stg"][0] / 2

    act134(hero)
    
def act262(hero):
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



def act263(hero):
    print(event.e263)
    '''Look at your investigator sheet. At the top, you have spaces for eight
    characteristics: Strength (STR), Constitution (CON), Power (POW),
    Dexterity (DEX), Appearance (APP), Size (SIZ), Intelligence
    (INT), and Education (EDU). Allocate the following values among
    them, writing in the large square beside each: 40, 50, 50, 50, 60,
    60, 70, 80. If you would like more information about what these
    characteristics mean, read page 6 of the Quick-Start Rules.
    When you have done that, go to 8.'''
    hero.stats["stg"] = [80,80,0,0]
    hero.stats["con"] = [70,70,0,0]
    hero.stats["pwr"] = [60,60,0,0]
    hero.stats["dex"] = [60,60,0,0]
    hero.stats["app"] = [50,50,0,0]
    hero.stats["siz"] = [50,50,0,0]
    hero.stats["inl"] = [50,50,0,0]
    hero.stats["edu"] = [40,40,0,0]
    
    #act8(hero)

def act270(hero):
    print(event.e263)
    print(hero.name, ', You have single-handedly destroyed a section of New Hampshire \
        about sixteen miles in diameter! \nThis also killed you')


#---------------------------------------------------------------------------------------
#    MAIN Program
#---------------------------------------------------------------------------------------

if __name__ == "__main__":
    Max = character()
    #Mel.printStats()
    #intro(Mel)
    act263(Max)
    #Mel.printStats()
    #Max.stats["stg"][2] = 15
    Max.printStats()
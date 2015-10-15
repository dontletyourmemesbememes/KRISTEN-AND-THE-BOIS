# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init python:
    class Stats:
        def __init__(self):
            self.stats = {
                "str":0,
                "int":0,
                "cha":0
            }
            self.days = 0

        def add_stats(self,stat,amount):
            self.stats[stat]
            if stat in self.stats:
                self.stats[stat] += amount
            else:
                self.stats[stat] = 0

        def get_stats(self,stat):
            if stat in self.stats:
                return self.stats[stat]
            else:
                return None
                
    class Girl:
        def __init__(self, name):
            self.name = name
            self.character = Character(name)
            self.closeness = 0

        def add_closeness(self,amount):
            self.closeness += amount


# Declare characters used by this game.
image bg placeholderbg = "background.png"

define p = Character("grill", color="#c8ffc8")
define m = DynamicCharacter("player_name")
image placeholder normal = "placeholder.png"


# The game starts here.
# Initialize stuff here and shove all the tutorial intro stuff here as well.
label start:
    scene bg placeholderbg
    "get name"

    $ player_name = renpy.input("name plrease")
    $ stats = Stats()
    $ girl1 = Girl("grill")

    m "my name is %(player_name)s !"
    show placeholder normal at left
    with moveinbottom
    girl1.character "and this is our placeholder grill"

    jump daytime
    

    return

#the main daytime routine.
label daytime:
    $ stats.days += 1
    $ temp = stats.days
    "this is the daytime routine (Day %(temp)d)"
    call raisestat #go to raisestat routine

    if stats.days < 5:
        jump daytime #jump to daytime again

    "ya out of time"

    return #end game

#routine for raising stats
label raisestat:
    menu:
        "What Stat to raise"

        "Strength":
            $ stats.add_stats("str",1)
            $ temp = stats.get_stats("str")
            "strength is now [temp]."
        "Intelligence" if stats.get_stats("str") > 1: 
            $ stats.add_stats("int",1)
            $ temp = stats.get_stats("int")
            "intelligence is now [temp]."
        "Charm" if stats.get_stats("str") + stats.get_stats("int") > 3:
            $ stats.add_stats("cha",1)
            $ temp = stats.get_stats("cha")
            "charm is now [temp]."
    return 
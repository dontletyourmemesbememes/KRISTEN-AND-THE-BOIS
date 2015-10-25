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
define principal = Character("Principal", color="#c8ffc8")

# The game starts here.
# Initialize stuff here and shove all the tutorial intro stuff here as well.
label start:

    $ player_name = renpy.input("Can I get you to repeat your name please?")
    $ stats = Stats()
    $ girl1 = Girl("")

    m "My name is %(player_name)s !"
    
    #show placeholder normal at left
    #with moveinbottom
    
    jump intro

    return

label intro:
    
    principal "Welcome to <insert school name here>. This school consists of the brightest students from all over the city, so congratulations for making it! In order to foster independence and individual growth in each of our students, we’re extremely flexible in what classes you attend. So you’ll be able to choose which class to show up to and what area of study you wish to upgrade in a sense. But be choose wisely. Once you set your classes today, it’ll be permanent for the rest of the year. 
If you’re ready, I can take you on a tour of the school and some of the club rooms. Do you want me to repeat anything?"
    
    menu: 
    
        "I think I'm good.":
            principal "Please follow me, %(player_name)s."
            jump school_tour
        "Can you go over how this works again?":
            jump intro
    
label school_tour:
    
    #show image of economics room
    principal "This is the home economics room. Students come here to learn essential life skills like cooking. Keep in mind that the most sophisticated dishes require an amount of stamina and some creative style."
    
    #show image of girl cooking
    #fade out
    
    #show image of music room
    principal "This is the music room. If you ever want to develop your musical capabilities, then this  the perfect spot to practice! Keep in mind that music is an expression of your personality, but also requires a lot of thought process."
    
    #show tsundere playin piano
    #fade out
    
    #show image of the gym
    principal "This is our fitness centre. We have the newest equipment for any kind of workout. Remember to keep fit during the year, because it will help you psychologically when you are doing homework and are studying for your midterms."
    
    #show other girl
    #fade out
    
    #go to general image, office or something
    principal "Well those are just examples of the many facilities this school provides. Make use of your time and be sure to work hard on your academics. Remember that although this is an elite school and your studies are very important, your social life and extra curriculars are crucial in a healthy high school experience too. Good luck on your first day!"
    
    jump make_schedule

label make_schedule:
    
    "It looks like I have to make my year schedule now. These are the classes that this school is offering right now:"

    menu:
        "Gym":
            "Guess I'll choose Gym for one choice, I still need to pick another."
            #choose again without gym
            menu: 
                "Biology":
                    jump gym_biology
                "Drama":
                    jump gym_drama
        "Biology":
            "Guess I'll choose Biology for one choice, I still need to pick another."
            #choose again without Biology
            menu: 
                "Gym":
                    jump gym_biology
                "Drama":
                    jump biology_drama
        "Drama":
            "Guess I'll choose Drama for one choice, I still need to pick another."
            #choose again without Drama
            menu: 
                "Biology":
                    jump biology_drama
                "Gym":
                    jump gym_drama
            
label gym_biology:
    #chose gym and biology
    $ stats.add_stats("str", 1)
    $ stats.add_stats("int", 1)

    jump extracurricular
    
label gym_drama:
    #chose gym and drama
    $ stats.add_stats("str", 1)
    $ stats.add_stats("cha", 1)
    
    jump extracurricular
   
label biology_drama:
    #chose biology and drama
    $ stats.add_stats("int", 1)
    $ stats.add_stats("cha", 1)
    
    jump extracurricular
   
label extracurricular:
    "So this is what an elite school is like? Classes seem ridiculously hard. Maybe I should check out those extracurriculars the principal mentioned."
    
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

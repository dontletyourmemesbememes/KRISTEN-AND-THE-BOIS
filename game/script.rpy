﻿# You can place the script of your game in this file.

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

            self.classes = {"Biology":"biology",
                            "Drama":"drama",
                            "Gym":"gym"}

            self.picked_classes = []
            self.max_classes = 2
            self.food_choice = 0
            self.chosen_girl = 0
            
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
    
        def get_days(self):
            return self.days
            
        def increment_days(self):
            self.days += 1

        def pick_classes(self,class_type):
            self.picked_classes.append(class_type)

        def reset_classes(self):
            self.picked_classes = []

        def get_available_classes(self):
            choices = []
            for class_type,class_desc in self.classes.items():
                if not(class_type in self.picked_classes):
                    choices.append((class_type,class_desc))
            return choices

        def get_picked_classes(self):
            return self.picked_classes
            
        def get_food_choice(self):
            return self.food_choice
        
        def set_food_choice(self, value):
            self.food_choice = value
        
        def get_chosen_girl(self):
            return self.chosen_girl
            
        def set_chosen_girl(self, girl):
            self.chosen_girl = girl
               
    class Girl:
        def __init__(self, name):
            self.name = name
            self.character = Character(name)
            self.closeness = 3

        def add_closeness(self,amount):
            self.closeness += amount
            
        def get_closeness(self,name):
            return self.closeness
            
        def set_name(self,name):
            self.name = name
            
    def rng_roll(chance): #chance should be between [0,1]
        return chance > renpy.random.random()


# Declare characters used by this game.
image bg placeholderbg = "background.png"

define p = DynamicCharacter("unknown_name", color="#c8ffc8")
define m = DynamicCharacter("player_name")
define principal = Character("Principal", color="#c8ffc8")

# The game starts here.
# Initialize stuff here and shove all the tutorial intro stuff here as well.
label start:

    $ player_name = renpy.input("Can I get you to repeat your name please?")
    $ stats = Stats()
    $ girl1 = Girl("Mary")
    $ unknown_name = "???"

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
    
    $ stats.reset_classes()
    jump make_schedule

label make_schedule:
    
    if len(stats.get_picked_classes()) == 0:
        "It looks like I have to choose 2 classes to attend."
    $choices = stats.get_available_classes()
    $result = renpy.display_menu(choices)

    call expression result

    if len(stats.picked_classes) < stats.max_classes:
        jump make_schedule
    else:
        $ day = stats.get_days()
        if day == 0: # end the day
            jump end_day_0
        else:
            jump extracurricular
                    
label end_day_0:
    "Phew... That was a long day, I'll head home for today..."
    $ stats.increment_days()
    
    #fade to show end of day 
    
    
    "Time to go to class..."
    $ stats.reset_classes()
    jump make_schedule
    
label gym:
    $ stats.pick_classes("Gym")
    $ stats.add_stats("str", 1)
    if len(stats.get_picked_classes()) < stats.max_classes:
        "Guess I'll choose Gym for one choice, I still need to pick another."
    return
    
label drama:
    $ stats.pick_classes("Drama")
    $ stats.add_stats("cha", 1)
    if len(stats.get_picked_classes()) < stats.max_classes:
        "Guess I'll choose Drama for one choice, I still need to pick another."
    return 
    
label biology:
    $ stats.pick_classes("Biology")
    $ stats.add_stats("int", 1)
    if len(stats.get_picked_classes()) < stats.max_classes:
        "Guess I'll choose Biology for one choice, I still need to pick another."
    return

label extracurricular:
    "So this is what an elite school is like? Classes seem ridiculously hard. Maybe I should check out those extracurriculars the principal mentioned."
    $ chosen_girl = stats.get_chosen_girl()
    
    if chosen_girl == 0:
        menu:
            "Home Economics Room":
                jump home_ec_room
            "Music Room":
                jump music_room
            "Fitness Centre":
                jump fitness_room
    
    elif chosen_girl == 1: # Mary is chosen
        
        jump home_ec_day_2

label home_ec_room:
    # show image of room
    # play sound of sizzling noise
    
    # you have chosen Mary as the girl 
    $ stats.set_chosen_girl(1)
    
    "> As you enter the room, you hear a sizzling noise. The fragrances tickle your nose as you enter the room. Your sight is drawn to the centre of the room, to a girl. She looks up to acknowledge you, and she gives a friendly but shy smile."
    
    p "Hello, I haven’t seen your face around, are you new?"
    
    m "Yeah, I just transferred here recently. Is this the cooking club?"
    
    p "Yes! you’ve come to the right place."
    
    m "Where do I sign up?"
    
    p "Well… you kind of need to cook in this club. Show me what you can do first, and then we can talk about your membership."
    
    "You realize that you’ve only been here for a day, and the only culinary experience you have comes from instant ramen."
    
    p "Hello? You blanked out for a second, haha. what do you plan on making for me?"
    
    $ str_check = stats.get_stats("str")
    $ int_check = stats.get_stats("int")
    $ cha_check = stats.get_stats("cha")
    
    menu: 
        "Chocolate chip cookies":
            if str_check >= 1 and cha_check >= 1:
                "Miraculously, you remember a recipe for chocolate cookies, and manage to put them together. You put them aside to cool, and as you wait there is a silent moment. When you make eye contact you realize that you could probably use this time to get to know her, or would that be too awkward right now?"
                $ girl1.add_closeness(1)
                $ stats.set_food_choice(0)
                jump girl_1_convo
            else:
                "I don't remember how to make this, time to guess!"
                $ girl1.add_closeness(-1)
                $ stats.set_food_choice(1)
                jump girl_1_convo
        
        "Instant Ramen":
            "This is easy to make."
            $ girl1.add_closeness(-1)
            $ stats.set_food_choice(2)
            jump girl_1_convo
        
        "Beef Carpaccio":
            # add/decrease closeness
            $ stats.set_food_choice(3)
            jump girl_1_convo
            
label girl_1_convo:
    
    m "Soooo… I actually never caught your name, my names %(player_name)s."
    
    p "Oh, sorry about that! I’m Mary, I am president of the cooking club. I’m in my senior year, just like you."
    # change the name of p to Mary
    $ unknown_name = "Mary"
    
    "You try to carry the conversation as you realize it’s not really going anywhere"
    
    m "Nice, why cooking?"
    
    p "It is a good way to release stress, but I’m not anything like a master chef"
    
    $ get_food = stats.get_food_choice()
    if get_food == 0 or get_food == 1:
        $ food = "cookies are"
    elif get_food == 2:
        $ food = "instant ramen is"
    else:
        $ food = "beef carpaccio is"
    m "Looks like the %(food)s done!"
    
    "> Mary takes a bite"
    
    $ get_food = stats.get_food_choice()
    if get_food == 0:
        jump made_good_food
    elif get_food == 1:
        jump made_bad_food
    elif get_food == 2:
        jump made_bad_food
    else:
        jump made_bad_food
        
label made_bad_food:
    
    p "It was... uh... not bad... "
    
    "she forces a smile and pushes your food a few inches away"
    
    m "Sorry about that, maybe you can teach me some basics?"
    
    p "mmm… that sounds okay i suppose...come by tomorrow and I’ll teach you a little of what I know."
    
    jump end_day_1
    
label made_good_food:
    
    p "It was good!"
    
    "she gives a warm smile"
    
    p "I’ll let you into the club! I need a sous chef to help me with a project. If you’re free come by tomorrow after class"
    
    jump end_day_1
    
label end_day_1:
    
    # show image of bedroom at night?
    m "That was a long day, time to hit the sack."
    $ stats.increment_days()
    
    jump start_day_2
    
label start_day_2:
    
    "Another day at school..." 
    $ stats.reset_classes()
    jump make_schedule
    
label home_ec_day_2:
    
    # DO STUFF HERE
    # cake cafe (need +1 closeness)
    # HIGH END RESTAURANT (need +8 closeness?)
    # home cooked meal (need + 1000000000 closeness) 

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

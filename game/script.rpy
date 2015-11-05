# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init python:
    import random

    class QuestionManager:
        def __init__(self):
            self.question_list = []
        def get_random_question(self):


    class Question:
        def __init__(self,desc,choices,answer):
            self.description = desc
            self.choices = choices
            self.answer = answer

        def get_description(self):
            return self.description

        def get_choices(self):
            random.shuffle(self.choices)
            return choice_list

        def check_answer(answer):
            return answer == self.answer

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
define mom = Character("Mom", color="#c8ffc8")

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
        elif day == 1:
            jump extracurricular
        else: 
            return
                    
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
    
    "> You realize that you’ve only been here for a day, and the only culinary experience you have comes from instant ramen."
    
    p "Hello? You blanked out for a second, haha. what do you plan on making for me?"
    
    $ str_check = stats.get_stats("str")
    $ int_check = stats.get_stats("int")
    $ cha_check = stats.get_stats("cha")
    
    menu: 
        "Chocolate chip cookies (Strength 1, Charm 1)":
            if str_check >= 1 and cha_check >= 1:
                "> Miraculously, you remember a recipe for chocolate cookies, and manage to put them together."
                $ girl1.add_closeness(1)
                $ stats.set_food_choice(0)
                jump girl_1_convo_1
            else:
                "> You don't remember how to make this, time to guess!"
                $ girl1.add_closeness(-1)
                $ stats.set_food_choice(1)
                jump girl_1_convo_1
        
        "Instant Ramen (No reqs)":
            "> You decide that it’s would be more efficient to make what you know the best. Conveniently, you remember that you brought along a spare package of instant noodles to school with you. You pull it out of your backpack and proceed to open the plastic wrapping."
            $ girl1.add_closeness(-1)
            $ stats.set_food_choice(2)
            jump girl_1_convo_1
        
        "Beef Carpaccio (Strength 2)":
            "> You decide that it would be best to go big or go home. If you managed to pull this off, she would be incredibly impressed. Unfortunately, you do not have the knowledge of the ingredients or techniques need to put this dish together. You improvise as you go."
                
            if str_check >= 2:
                $ stats.set_food_choice(3)
                jump girl_1_convo_1
            else:
                $ stats.set_food_choice(4)
                jump girl_1_convo_1
            
label girl_1_convo_1:
    
    "> As you’re working, you can’t help notice the awkward silence settling in. You glance over to her and end up making eye contact. You realize that you could probably use this time to get to know her."
    
    menu: 
        "Ask her for her name":
            m "Soooo… I actually never caught your name, my names %(player_name)s."
    
            p "Oh, sorry about that! I’m Mary, I am president of the cooking club. I'm also in my senior year."
            # change the name of p to Mary
            $ unknown_name = "Mary"
            
            menu:
                "Ask her why she joined the cooking club":
                    p "It's just a hobby, nothing that serious."
            
        "Ask her why she joined the cooking club":
            p "It's just a hobby, nothing that serious."
            
            menu:
                "Ask her for her name":
                    m "Soooo… I actually never caught your name, my names %(player_name)s."
    
                    p "Oh, sorry about that! I’m Mary, I am president of the cooking club. I'm also in my senior year."
                    # change the name of p to Mary
                    $ unknown_name = "Mary"
            
    $ get_food = stats.get_food_choice()
    if get_food == 0 or get_food == 1:
        $ food = "cookies are"
    elif get_food == 2:
        $ food = "instant ramen is"
    else:
        $ food = "beef carpaccio is"
    m "Looks like the %(food)s done!"
    
    $ get_food = stats.get_food_choice()
    if get_food == 0 or get_food == 3:
        jump made_good_food_1
    elif get_food == 1:
        jump made_bad_food_1
    elif get_food == 2:
        "> You peek at her eyes to get some idea of what she may be thinking, but it’s not really discernible. You watch nervously as she takes a bite. This is your favorite flavor of instant noodles. After swallowing, she hesitates for a moment, and her eyes bulge. Violently she clasps her mouth and supports herself with the edge of the counter. She spits out your creation."
        jump made_bad_food_1
    else:
        "> You peek at her eyes to get some idea of what she may be thinking, but it’s not really discernible. You watch nervously as she takes a bite, wondering if you put in enough sriracha sauce to mask the overbearing taste of durian. After swallowing, she hesitates for a moment, and her eyes bulge. Violently she clasps her mouth and supports herself with the edge of the counter. She spits out your creation."
        jump made_bad_food_1
        
label made_bad_food_1:
    
    p "It was... uh... not bad... "
    
    "She forces a smile and pushes your food a few inches away"
    
    m "Sorry about that, maybe you can teach me some basics?"
    
    p "mmm… that sounds okay i suppose...come by tomorrow and I’ll teach you a little of what I know."
    
    jump end_day_1
    
label made_good_food_1:
    
    p "It was good!"
    
    "> Mary gives a warm smile"
    
    p "I’ll let you into the club! I need a sous chef to help me with a project. If you’re free come by tomorrow after class"
    
    jump end_day_1
    
label end_day_1:
    
    # show image of bedroom at night?
    m "That was a long day, time to hit the sack."
    $ stats.increment_days()
    
    jump start_day_2
    
label start_day_2:
    
    m "Another day at school..." 
    $ stats.reset_classes()
    call make_schedule
    jump home_ec_day_2
    
label home_ec_day_2:
    
    # DO STUFF HERE
    m "maybe I should drop by the club room, Mary might be there too."
    
    "> You head over to the home ec room. Mary is standing in the centre of the room."
    #should we do something different for the club activities?
    p "You're here! Let's get started then."
    
    "> Mary gives a cheerful look."
    
    "> You spend time cooking with Mary. You manage to follow her orders perfectly!"
    
    p "Hmmm..."
    
    "> Mary stares blankly into space."
    
    m "What's wrong?"
    
    "> Mary's gaze shifts to you."
    
        p "Well... I just feel like I need some inspiration right now. I wish I could try some new food somewhere. Do you have any suggestions %(player_name)s?"
    
    menu:
        "How about a cake cafe?" :
            if girl1.get_closeness("Mary") >= 1 :
                jump cafe_date
            else:
                "Can't do that."
        "Let's go somewhere fancy!" :
            if girl1.get_closeness("Mary") >= 8 :
                jump restaurant_date
            else:
                "Can't do that."
        "I'll make you something at my place." :
            if girl1.get_closeness(girl1) >= 10000000 :
                jump girl1_home_date
            else:
                " > You want to say that, but you don't have enough SELF RESPECT (LOL)" 
    # cake cafe (need +1 closeness)
    # HIGH END RESTAURANT (need +8 closeness?)
    # home cooked meal (need + 1000000000 closeness) 
    # option should none of them qualify

    return
 
label cafe_date :
        
    return

label restaurant_date :
    
    return
    
label girl1_home_date:
    p "I remember you mentioned before that I never tasted your cooking. If it’s okay with you, I’d really like to try some today."

    m "Oh, so you did remember!" 

    "{i}she seems shy but happy{/i}"

    m "Then, why don’t we go back to my house? I have all the ingredients there."

    "You and Mary head back to her place. You feel tenser than usual, despite the fact you’ve recently spent a lot of time with her. In the corner of your eye you catch her peeking slightly in your directly, but she immediately redirects her vision forward after being noticed."

    m "Today is really beautiful, although I don’t know what we’d do if there wasn’t a breeze."

    "As you approach her house, your eyes follow her as she leaps ahead. She moves forward and her hair swings, and pushes a scent towards you, pleasantly resonates with the core of your body"

    "For a second you get hung on the scent for a moment as you’re both entering, and you have a blank stare. She turns to notice you"

    #(o.o) face
    m "You look like you’re lost"

    p "E-ehh "

    "{i}you shake your head, but flustered you don’t know how to recover smoothly{/i}"

    # :) face
    m "hehehe, the kitchen is this way"

    "She leads you into the kitchen, and immediately moves to the different corners of the kitchen, in an a rehearsed efficiency. You pick up some newspapers to attempt helping"

    m "No, not there hahaha"

    "she pulls them out of your hands and sets them aside, then turns to you"

    m "Everything is set! What do you want to eat?"
    call girl1_home_date_choice

    #mom drama stuff
    "{i}Doorbell rings{/i}"

    mom "Hey Mary, I’m home from my business trip!"

    m "Oh crap, my mom is home. Hi mom!"

    "{i}Mom sees you{/i}"

    mom "Who is this, Mary? Why are you guys alone together?"

    m  "Uh, this is my friend, <insert name>. We are just hanging out after school mom. There is nothing to worry about."

    mom "You shouldn’t be inviting people over when I’m on a business trip. Shouldn’t you be studying too? It’s a school night!"

    m "I-I just wanted to relieve some stress, it’s just a little bit of cooking."

    "the discussion gets heated, and you stand there as if you are not even in the room"

    mom "Mary, you should be using your time more wisely. What happen to the money i gave you to buy food with? You should be focusing on getting into university, so you can get a career. You spend too much time in that cooking club, or whatever."

    m "I didn’t use it; it is still in your office. What if I wanted to be a chef? Like dad?"
    "Her mom, is taken back for a moment"

    mom "…Don’t you remember what happened to your father? I can’t let that happen to you, Mary, I can’t lose both of you like that. "

    m "What happen to dad was unfortunate, but.."

    mom "No buts! Don’t try to argue with me. Escort your friend out and then go to your room."

    menu:
        "Leave the house":
            "GG"
            return
            #replace return with jump to game over screen
        "Talk to mom":
            p "Can I speak with you in private?"
            mom "Fine."
            "Mary leaves"
            p "I may not know what happened to your husband and I understand where you are coming from, but I don’t think you are approaching the right way. "
            mom "Are you trying to tell me what to do?"
            p "No, but I just want to tell you about my experience. My parents wanted my older brother to go into medicine and put a lot of pressure and expectations on him. "
            p "Because of this, he unfortunately got a stress induced heart attack and passed away. Even when he was studying medicine, he was not happy and did not feel like he was living life. "
            p "My parents have learnt the hard way that letting your child follow their passion is the best for their lives. "
            p "Letting Mary pursue her passions of cooking will help her de-stress from school and there are plenty of jobs in the food industry! She has the talent for it!"
            "{i}mom is speechless{/i}" 
            "Moments later, she goes upstairs to get Mary"
            mom "Is cooking your passion in life?"
            m "Yes"
            mom "I will let you continue your cooking has a hobby on one condition. You keep your school marks up."
            m "Of course. Thank you mom!"
            mom "Go have fun cooking"
            "Mary goes back in the kitchen; Mom goes into her office"

    "It feels a little weird.What should you do?"
    menu:
        "Sit in the living room and play video games":
            m "Ehhh… I’d be nice if you helped me out" #:S face
            p "Oh! sorry about that"
            "{i}You rush to the kitchen, you aren’t really good at this are you?{/i}"
            #negative
        "Go into the kitchen and offer your assistance":
            label girl1_home_date_kitchen:
                p "Let me help you, Mary."
                m Sure! can you preheat the oven for me?
                #positive
                "you agree and you continue to be on the side and help her where you can."
                "as she carefully measures dry ingredients from a 20kg flour bag, the wet ingredients are your responsibility."
                "{i}The parts start to come together as you both share each other’s presence. once in a while her elbow brushes against yours.{/i}"

                m "Oh sorry <she looks up at you for a brief moment and catches your eye"
                p D"on’t apologize, it’s alright." 
                "{i}Her eyes widen slightly, but immediately both of you look away and refocus on the preparations.{/i}"
                "{i}in the corner of her eye, you see a bead of sweat trailing down from her temple to the front of her neck. You see her cheeks flooded with red.{/i}"
                "{i}This makes you blush too, and your breaths seem shallower{/i}"
                m "WOW! it’s getting hot in here! oh my! how hot did you preheat that oven??"
                "{i}she looks at the temperature{/i}" 
                m "Oh! look 350 degrees, perfect! and wasn’t it hot today?" 
                "{i}frantically she wipes her sweat, but knocks her bowl of flour off the table. Luckily your reactions catch the bowl, but leave the flour across the floor.{/i}"
                m "OH NO! ahhh…."
                menu:
                    "somebody’s got a lot of cleaning to do":
                        #negative
                        m "just get me more flour"
                    "It’s okay, don’t worry! I’ll grab you some more flour.":
                        #positive
                "{i}you struggle with the heavy flour bag, trying to get it level with the counter. You release the weight of the bag in front of her.{/i}"
                "{i}You failed to realize that the top of the bag was open, releasing a shower of flower that covers her face and yours, as you both look up to see the flying ingredients{/i}"

                p "You got some… umm flour all over you"

                "{i}You brush the flower off her shoulders, as you gently avoid making awkward physical contact.{/i}"

                m "Well… I could only assume, but my lenses are completely covered hahaha… I can’t see a thing."
                
                p "Here I got it for you"

                "{i}you lean in, as you lift the frames off her eyes.{/i}" 
                "Her brown eyes fixated on you. unprepared, you find your face lingering mere inches away from her’s."

                menu:
                    "{b}JUST DO IT!!{/b}":
                        "maybe it’s something in the air, besides flour, but you didn’t decide to take the relationship one step further, you want the leap of faith."
                        "{i}you wipe the flour off her cheeks, and find your hands resting on the back of her neck{/i}"
                        "{i}Before you know it, your hand pulls her towards you. Anticipation building, you close your eyes.{/i}"
                        "{i}you feel something press against your lips{/i}"
                        "{i}...{/i}"
                        "{i}something doesn’t feel right. As you open your eyes you find your mouth, cupped by her hand. Mary eye still wide opening, smiling{/i}"

                        m "I may not be able to see that well without glasses, but I’m not blind. Don’t get me wrong, I can’t deny that I have feeling for you, but let’s take it slow. ;) LMAOOO"

                        "{i}she lifts your hands off of her, she holds you palm open and examines it. You both turn slightly towards the counter to face shoulder to shoulder.{/i}"
                        "{i}still examining your hand, she places her hand on top of your’s as if comparing hand sizes{/i}"

                        m "you know, you have pretty soft hands. I think I’ll hold on to them for a while."

                        "{i}both her and your hands begin to offset a little, you decide not to resist, progressing to interlock fingers.{/i}"
                        return #replace with jump to win screen
                    "Go back to baking"
                        "{i} You pull away to avoid embarrassment{/i}"
        "Look around for any photo albums that she may have":
            "you stray away from the kitchen and walk along the line of photos, many of them focused around Mary as a child. "
            "In the photos that you look skim across, many of them almost bleak, she has no expression. Soccer team, School class photos, Academic achievement photos, in none of them she is smiling."
            "You pick one with her flour all over her face as a kid, her glasses caked in powder, but her smile being the only distinguishable thing."

            "{i}Mary glances over{/i}"
            m "Ek! nooo! that’s such an embarrassing picture of me!"
            p "HAHAH, Really? I think it’s pretty cute"
            "{i}Her cheeks grow red from being flushed{/i}"
            m "D-don’t say things like that!" 
            "{i}even with this statement, she holds back a smile{/i}" 
            m "Are you going to help me bake or what?"
            menu:
                "Yes":
                    jump girl1_home_date_kitchen
                "Why is this the only happy photo?"
                    m "I don’t really know. This is the first time when my mom let me bake all by myself, but I ended up dropping the flour bag, and made a huge mess all over the place." 
                    m "Nothing else really excited me that much. I didn’t do that many extra curriculars, and any I ended up signing up for got in the way of school." 
                    m "My parents really wanted me to do get good grades, so I never stayed in an activity for more than a couple months." 
                    m "But I mean, I get where they're coming from, I have to do well in school, or else I can’t get into university, get a job, and marry some guys with a stable job. How will I help support the kids I’ll have?"

                    "{i}you say something supportive{/i}" #replace
                    m "haha… you always have the right thing to say… most of the times :P"
                    "{i}she grabs on to your arm and brings you back to the kitchen{/i}"
                    jump girl1_home_date_kitchen

    jump end_day_1
    #return


label girl1_home_date_choice:
    menu:
        "Chimichurri Rack of Lamb" :
            m "Wow! Your taste is pretty extravagant huh?"
            menu:
                "You don’t have to cook it if you don't want to.":
                    m "You don’t think I can do it?"
                    m "I’ll prove you wrong. "
                    #negative
                " I really want to eat this.":
                    "{i}Mary seems intimidated by the challenge but finds her resolve.{/i}"
                    "I’ll do my best!"
                    #positive/neutral 
        "Instant noodles":
            m "Common..are you taking my offer seriously here?"
            #negative
            call girl1_home_date_choice
            return
        "Triple Layer Chocolate Cake":
            "{i}She seems surprised by your request{/i}"
            m "I thought you’d choose something harder. Why did you choose a cake?"
            menu:
                "I didn’t want you to work too hard.":
                    m "What? Don’t worry so much...I can handle it. But alright, if that’s what you want."
                    #negative
                "So we can share it when you’re done.":
                    m "Are you usually this corny? haha. But alright, if that’s what you want."
                    #neutral 
                "I already know how great your cooking skills are. So i want you to make me something that’s meaningful.":
                    m "Meaningful?"
                    p "Each layer of the cake represents each place we’ve spent time together and how far we’ve come building on our relationship. One layer at a time."
                    m "{i}blushiesssssss{/i} O-oh." 
                    "{i}Mary seems flustered but pleased by your thought.{/i}"
                    m " Alright, I-I’ll get started then" # :) face
                    #positive
    "Mary goes begins cooking the dish and you’re left sitting in her living room alone."
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

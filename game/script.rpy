# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init python:
    import random

    class QuestionManager:
        def __init__(self):
            self.question_list = []
        def get_random_question(self):
            # do something FIX IT
            self.question_list = []

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
            self.event = 0

        def add_closeness(self,amount):
            self.closeness += amount
            
        def get_closeness(self,name):
            return self.closeness
            
        def set_name(self,name):
            self.name = name
            
        def get_event(self,name):
            return self.event
            
        def add_event(self):
            self.event += 1
            
    def rng_roll(chance): #chance should be between [0,1]
        return chance > renpy.random.random()


# Declare characters used by this game.
image bg placeholderbg = "background.png"

define p = DynamicCharacter("unknown_name", color="#c8ffc8")
define m = DynamicCharacter("player_name")
define principal = Character("Principal", color="#c8ffc8")

define mom = Character("Mom", color="#c8ffc8")

#Cafe date variables~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
define cafe_asked_count = 0
define cafe_boyfriend = False #variable for recording whether or not player has asked about a boyfriend yet.
define cafe_before= False #record whether you have asked her if she's been here before
define cafe_asked1 = False    
#Restaurant date variables~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
define rest1_asked2 = False
define rest1_asked3 = False
define rest2_asked1 = False

# The game starts here.
# Initialize stuff here and shove all the tutorial intro stuff here as well.
label start:

    $ player_name = renpy.input("Can I get you to repeat your name please?")
    $ stats = Stats()
    $ girl1 = Girl("Mary")
    $ unknown_name = "???"

    m "My name is %(player_name)s!"
    
    #show placeholder normal at left
    #with moveinbottom
<<<<<<< HEAD

=======
>>>>>>> refs/remotes/origin/master
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

    "> she forces a smile and pushes your food a few inches away"

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
    
    "Another day at school..." 
    $ stats.reset_classes()
    call make_schedule
    jump home_ec_day_2
    
label girl1_check_1:
    
    $ closeness = girl1.get_closeness("Mary")
    $ day = stats.get_days()
    $ event_num = girl1.get_event("Mary")
    
    if day < 5 and closeness > -3 and closeness < 5:
        # continue on with cooking
        return
    elif day > 5:
        # too long trigger failure event
        jump girl1_failure
    elif closeness <= -3:
        # lost too much closeness
        jump girl1_failure
    elif day < 5 and closeness >= 5 and event_num == 0:
        # trigger event 1 of cafe as day < 5 and closess > 5
        # set the event value to 1
        $ girl1.add_event()
        jump cafe_date1
        
label girl1_check_2:
    
    $ closeness = girl1.get_closeness("Mary")
    $ event_num = girl1.get_event("Mary")
    if closeness >= 7 and event_num == 1:
        $ girl1.add_event()
        jump restaurant_date1
    else:
        return
        
label girl1_check_3:
    
    $ closeness = girl1.get_closeness("Mary")
    $ event_num = girl1.get_event("Mary")
    if closeness >= 10 and event_num == 2:
        jump girl1_home_date
    else:
        return
    
label home_ec_day_2:
    
    # check closeness
    call girl1_check_1
    call girl1_check_2
    call girl1_check_3
    
    $ str_check = stats.get_stats("str")
    $ int_check = stats.get_stats("int")
    $ cha_check = stats.get_stats("cha")

    m "maybe I should drop by the club room, Mary might be there too."
    
    menu:
        "Blueberry Muffin (No reqs)":
            "> The muffins looks great!"
            p "Wow! They're so fluffy, but the top is so crisp. Good job!"
            $ girl1.add_closeness(1)
            
        "Creme brule (Intelligence 2, Charm 2)":
            if int_check > 2 and cha_check > 2:
                # sucess
                "> The Creme brule looks great! nice golden caramelize on it! Looks delicious!"
                p "Looks great. I'm impressed."
                $ girl1.add_closeness(3)
            else:
                # failure
                "> The Creme brule turned out completely black... You think that you burnt it..."
                p "Uhh... is this even edible?"
                $ girl1.add_closeness(-3)
                
        "Lasagna (Strength 2, Charm 2)":
            if str_check > 2 and cha_check > 1:
                "> The lasagna looks great! The cheese is perfectly melted."
                p "The Lasagna looks awesome! The layers look so even!"
                $ girl1.add_closeness(2)
            else:
                "> You reach into the oven and pull out what looks like a pile of plain pasta."
                p "I think you didn't use enough tomato sauce... it looks pretty dry."
                $ girl1.add_closeness(-2)
    
    $ stats.increment_days()

label day_3:
    
    "Another day at school..." 
    $ stats.reset_classes()
    call make_schedule
    jump home_ec_day_3

label home_ec_day_3:
    
    call girl1_check_1
    call girl1_check_2
    call girl1_check_3
    
    $ str_check = stats.get_stats("str")
    $ int_check = stats.get_stats("int")
    $ cha_check = stats.get_stats("cha")
    
    menu:
        "Cinnamon Buns (No reqs)":
            "> The Cinnamon Buns turned out great! The icing looks shiny and delicious!"
            p "Looks so good! Can't wait to try it."
            $ girl1.add_closeness(1)
            
        "Assorted Sashimi (Charm 3, Strength 3)":
            if int_check > 3 and str_check > 3:
                "> The sashimi is perfectly sliced."
                p "Wow! Looks so good I almost don't want to eat it!"
                $ girl1.add_closeness(3)
            else:
                "> The slices turned out oddly-shaped and uneven. You see pieces of bones and scales mixed in with the fish."
                p "Uhh... It's okay. We can always get some more expensive fish."
                $ girl1.add_closeness(-3)
                
        "Carbonara (Strength 2, Charm 2)":
            if str_check > 2 and cha_check > 2:
                "> The pasta turned out perfectly cooked! The aroma of the sauce fills the air."
                p "That smells so good!"
                $ girl1.add_closeness(2)
            else:
                "> The pasta looks like a pile of mush..."
                p "I think the pasta is way too overcooked..."
                $ girl1.add_closeness(-2)
            
    $stats.increment_days()

label day_4:
    
    "Another day at school..." 
    $ stats.reset_classes()
    call make_schedule
    jump home_ec_day_4
    
label home_ec_day_4:

    call girl1_check_1
    call girl1_check_2
    call girl1_check_3
    
    $ str_check = stats.get_stats("str")
    $ int_check = stats.get_stats("int")
    $ cha_check = stats.get_stats("cha")

    p "Well... I just feel like I need some inspiration right now. I wish I could try some new food somewhere. Do you have any suggestions %(player_name)s?"

    menu:
        "Mac and Cheese (No reqs)":
            "> The cheese is perfectly melted and crisp on the surface of the casserole dish."
            p "I can't wait to try this! Looks fantastic!"
            $ girl1.add_closeness(1)
            
        "Beef Stroganoff (Strength 4, Charm 4)":
            if str_check > 4 and cha_check > 4:
                "> The pasta turned out perfectly cooked! The aroma of the sauce fills the air."
                p "That smells so good!"
                $ girl1.add_closeness(2)

            else:
                "> The pasta looks like a pile of mush..."
                p "I think the pasta is way too overcooked..."
                $ girl1.add_closeness(-2)
                
        "Lemon Meringue Pie (Intelligence 3, Charm 3)":
            if int_check > 3 and cha_check > 3:
                "> The pie is firm and the meringue keeps it's form."
                p "Congratulations! The browning of the meringue is beautiful!"
                $ girl1.add_closeness(2)
            else:
                "> The filling is too liquidy; it will not hold its shape."
                p "I think that you over baked the pie."
                $ girl1.add_closeness(-2)
                
    $stats.increment_days()


#WHAT I ADDED
#================================================================================================================================================
#Girl 1 - Cafe Date ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

label cafe_date1 :
    if cafe_asked_count == 0 :
        "> You and Mary spend some time casually talking at a local cafe. A warm glow shines through the windows."
    
        "> Mary is looking off to the distance, her face showing little expression."
        
        "> Your orders arrive at the table."
        
        p "Thank you!"
    
        "{i}She seems distracted. Maybe I should be more engaging. What should I ask her?{/i}"
    else:
        "{i}What should I ask her?{/i}"
    menu:
        "Do you have a boyfriend?" if not cafe_boyfriend:
            $ cafe_asked_count += 1
            $ girl1.add_closeness(-1)
            p "Excuse me? Where is this coming from all of a sudden? What does it matter to you anyways?"
            
            "> Mary looks displeased."
                
            "{i} Maybe I should I should drop the topic...{/i}"
            $ cafe_boyfriend = True
            jump cafe_date1
        
        "C'mon, just tell me." if cafe_boyfriend:
            $ cafe_asked_count += 1
            $ girl1.add_closeness(-1)
            p "mmm... you really are persistent."
                
            "> Mary looks very uncomfortable."
                
            p "Oh yeah... I remembered there was something I had to do back home. Sorry to leave you so suddenly. Here's some money for the bill."
            jump cafe_date_badending
                
        
        "What do you want to be?" :
            $ cafe_asked_count += 1
            p "Hmm.. not sure. Medicine? Engineering? Something in those professional fields. What do you think?"
            
            menu :
                "Sounds great!I'll support you if you ever need help." :
                    $ girl1.add_closeness(-1)
                    p "Yeah... It does, doesn't it?"
                    
                    "> Mary forces a smile. She lets out a small sigh."
                    
                    "That's how life is supposed to go, right? That was, I can meet my mom's expectations... I guess that's most important after all.."
                    
                    "> You sense a hint of frustration in her voice. The tension gets to you and things become too awkward for you to say anything else."
                    
                    "> The rest of your date went on without much dialogue."
                    
                    jump cafe_date_badending
                    
                "What about being a chef?" :
                    $ girl1.add_closeness(2)
                    jump mary_backstory1
                    
                    
        "What do you usually come here?" if not cafe_before:
            $ cafe_asked_count += 1
            $ cafe_before = True 
            $ girl1.add_closeness(1)
            p "Yeah! I love coming here for the pastries and desserts!"
            
            " > Mary looks more excited as she rapidly counts her fingers."
            
            p "Everything here is good, black forest cake, gingersnaps, cinnamon buns... "
            
            p "YOU SHOULD TRY THE TIRAMISU HERE!"
            
            p "..."
        
            p "oops.. Haha, sorry. I'm usually more calm."
            
            "> Mary takes a therapeutic breath."
            
            m "Hahaha, don't worry. It's really kind of cute."
            
            "> Mary blushes. Her eyes drop to her latte."
                                     
            jump cafe_date1
            
        "How are classes?" if not cafe_asked1: 
            $ cafe_asked_count += 1
            $ cafe_asked1 = True
            p "Ehhh not bad, classes are same old. Nothing that interesting."
            
            jump cafe_date1

label mary_backstory1 :
    p "Hmm... I don’t know. It’s not the most stable career out there, ahah."
    
    m "So?"
    
    p "Soooo… that’s being pretty unrealistic… It’s too selfish for me to just think about what I want to do… I mean, when I get older I have to think about supporting a family, and taking care of kids, so that they can go to university. At least that’s what my mom thinks."
    
    "> Mary lets out a heavy sigh as her eyes roll back and she leans back into her chair. Her posture sinks and her eyes fall down to her cup."
    menu: 
        "Joke" :
           #$girl1.add_closeness(-1)
           m "Oh... Talk to me about it. Tell Dr.Fill about your problems."
           
           p " Uhmm... I'd rather not talk about it right now."
           
           m "Feel free to talk to me anytime."
           
           p "Yeah, thanks."
           
        "Console" :
            $girl1.add_closeness(1)
            m" That's rough. If you ever want to talk about it sometime, I'll be here."
              
            p "Thanks. Maybe another time."
            
            m "Yeah, anytime!"
    
    p "Ahh.. It's getting pretty late, I should head home."
    
    m "Yeah, same. It was fun hanging out with you today!"
    
    jump cafe_date_goodending


label cafe_date_goodending :
    $ girl1.add_closeness(1)
    "> After a while of more small talk, you guys finish your food. You both stand up and she looks at you."
    
    p "I really enjoyed this. We should get together more often."
    
    "> You hold the door open for her and you guys part ways. as you’re walking, you look back to catch her peeking over her shoulder, as well. You both wave at each other."
    
    "> The date was a success! You managed to get closer to Mary"
    
    jump return_to_which_day
    
label cafe_date_badending :
    $ girl1.add_closeness(-1)
    "> You guys finish your food. Mary stands up and looks away."
            
    p "Well... have a goodnight."
    
    "> Mary leaves first and you are left alone. You sit for a moment to avoid getting in her way. As you leave the cafe, she is no where in sight."
    
    "> You were unsuccessful in this date."
    
    jump return_to_which_day
    
    #cue bad game ending?

    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Girl 1 - Restaurant Date

label restaurant_date1 :
    if not rest1_asked2 and not rest1_asked3 :
        "> The hostess leads you to your table, and both of you get in each other’s way trying to decide where each of you will sit. As you two take your respective seats, you chuckle to each other."
    
        p "Ahah, wow.. this place sure is fancy." 
    
        "> Awkward silence follows."
    
        "> Mary looks a little flustered."
    
        "> QUICK! SAY SOMETHING TO HER YOU FOOL!"
    
    menu:
        "You look very pretty today." if not rest1_asked2 : 
            $ rest1_asked2 = True
            $ girl1.add_closeness(1)
            p "O-Oh."
            
            "> Mary blushes and can’t seem to look you in the eye. You hope this is a good sign? Your compliment doesn’t do anything to spark any conversation, rather, she seems even more flustered. "
            jump restaurant_date1
            
        "What else do you like about cooking?" : 
            jump restaurant_date2 
            
        "We look like a real couple!" if not rest1_asked3 : #no effect
            $ rest1_asked3 = True
            p "Uhm.."
            
            "> Mary looks confused."
            
            p "We're not... sorry, I just don't think we're on the same page.."
            
            "> Mary looks a little shy about it but not annoyed or anything. She seems even more flustered than before."
            
            jump restaurant_date1
            
            
label restaurant_date2:
    if not rest2_asked1:
        "> The corners of her mouth raise ever so slightly, but her eyes wince a little."
            
        p "I’ve been really curious about ever since I was little. Cooking made me feel some sort of wonder and eventually it just grew into a passion."
            
        "> She shifts her glass back and forth. Her eyes follow the glass. She lets out a shallow sigh."
            
        p "Something about cooking makes me feel unique, you know? Haha, sometimes I like to pretend that I’m really good at it. "
        
        "> Her glass slows down, and her smile fades to concern."
            
        p "But... In the end it's just a hobby..."
    
    "> Mary becomes silent, her eyes wander down to her glass."
            
    menu :
        "> Reassure." if not rest2_asked1: #chance to gain closeness
            $ rest2_asked1 = True
            m "Just a hobby? But you're the president of the cooking club!"
            
            p "Titles don’t really mean a whole lot, you haven’t even tried my cooking."
            
            menu :
                "I feel like there’s a pretty easy solution to that." : #stat requirement to say? (+2)
                    $ girl1.add_closeness(2)
                    
                    "> Mary leans forward. Her eyes are on you as she smirks."
                    
                    p "Well, don't expect much if I cook all by myself."
                    
                    m "Haha, I doubt I'll be much help to you. You're on your own!"
                    
                    "> The two of you joke together. Mary playfully punches your shoulder as the two of you roll back laughing in your seats."
                
                "Joke" : #-1
                    $ girl1.add_closeness(-1)
                    m "Yeah I guess. I mean, how many people even ran for president anyway?"
                    
                    p "Yeah, right..?"
                    
                    "> Mary forces a smile."
                
                "You’ve tried mine. We should make something together, and you can teach me a few things.": #(+1)
                    $ girl1.add_closeness(1)
                    p "Sounds like a fun time. Haha, alright then."
                    
                    "> Mary smiles as you two think of things to make together."
                    
            jump restaurant_date2
                
        "> Question." : #backstory opener
            m "It seems like cooking means a lot more to you. You seem upset. What's wrong?"
            
            jump mary_backstory2
            
label mary_backstory2:
    "> Mary rolls her eyes, she sits back in her chair, while letting her posture sink and her sight drops to her glass."
    
    p "I know she means well, and it’s not like she’s being mean about it. I just feel this pressure not to disappoint her? I don’t even know why I’m telling you all of this. I’ve only known you for a couple days, sorry."
    
    m "Honestly Mary, don’t worry I’m completely fine with it. Have you ever told her how you feel about cooking?"
    
    p "I’ve sort of suggested being a chef, but she avoids really talking about it much. she redirects the conversation, or tells me that 
       “It would be better to keep it as a hobby.”... My dad was a chef, and my mom loved him, but she would sometimes get worried that he was a little too invested in his passion for cooking. 
       When he had holidays, brought me into the kitchen, and taught me how to cook. I really loved those moments, and that’s when I fell in love with cooking hehe..."
    
    m "What about your dad? what does he think?"
    
    "> Mary pauses for a moment. She takes a prolonged deep breath."
    
    p " He would have said “do it!” He was the nonchalant character that brought life to the family. 
        My mom and dad were a strange couple, they both worked hard, but it’s funny cause my mom was the bread-winner, my dad baked the bread. hahaha... 
        But he’s not here to say that anymore..."
    
    m "I'm really sorry to hear that..."
    
    p "Thanks. I was about 14 at the time, so I’ve come to accept it… He really loved his work. Sometimes my dad would work 16 hours a day, prepping the restaurant, and working late. "
    
    p "The doctors said that he needed to take more breaks or he may suffer from stress, but my dad is the kind of guy who wouldn’t accept that. He had a heart attack, and it almost seemed out of the blue. 
       It turns out the stressed caused high blood pressure and lead to heart failure."

    p "My mom and I were devastated. Cooking for me lets me keep a memory of him living. I think for my mom, seeing me cook, just reminds her of a passion that took dad away."
    
    m "{i}What should I say to her?{/i}"
   
    menu: # choices should not decrease stats at this point of date
        "Keep cooking a secret." :
            
            m "You should continue pursuing a professional career to keep your mom happy. But try to keep cooking as a secret hobby for as long as possible so you can keep doing what you love."
           
            "> Mary smiles a little, but doesn't seem satisfied."
            
            p "Haha, maybe you're right. But having to keep this a secret forever doesn't seem possible."
            
            "> Mary goes silent for a moment. She doesn't seem to be feeling well." 
            
        "Don't listen to your mom." :
            m "It’s really considerate of you to try and make your mom happy, but I think you deserve to be happy too, even if it means going against her wishes."
            
            p "But how can I have happiness without my mom’s approval? She’s still important to me so her wishes are important as well...."
            
            p "...Sorry. I know you're just trying to help. That means a lot to me. Thanks."
            
            "> Mary goes silent for a moment."
            
        "Talk to your mom about it.":
            $ girl1.add_closeness(2)
            m "It sounds like you’re pretty torn and I think expressing your feelings towards your mom would be a pretty good step forward. She probably wants you to be as happy just as much as you want her to be happy."
            
            "> Mary looks contemplative. Her expression turns sour."
            
            p"No…I can’t. You don’t know my mom. She would never understand. This is important to me. What if I end up losing all of it? I wouldn’t be able to…"
            
            "> Mary looks like she's on the verge of tears."
            
            p "..I'm sorry."
    
    "> You comfort Mary. After a while she seems to recover and insists that she is okay. You both continue talking about different subjects, but she seems distracted."
    
    p "Hey.. thanks for today. I'm glad we got to spend more time with each other. It feels good talking to you about my problems."
    
    p "Well.. Have a goodnight."
    
    m "Goodnight."
    
    "> Mary gives you a warm smile before turning around. The two of you part ways in front of the restaurant."
    
    m "{i}Was she really okay..?{/i}"
    
    jump return_to_which_day
            
#label restaurant_ending:
    
#label restaurant_badending:
    

#==================================================================================================================================================================
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
                m "Sure! can you preheat the oven for me?"
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
                        "IN THIS BLOCK"
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
                    "Go back to baking":
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
                "Why is this the only happy photo?":
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

# -----------------------------------------------------------------------------------------------------------------

label return_to_which_day:
    $ day = stats.get_days()
    if day == 1:
        jump end_day_1
    elif day == 2:
        jump day_2
    elif day == 3:
        jump day_3
    elif day == 4:
        jump day_4
    else:
        jump day_5

label day_5:
    
    "Another day at school..." 
    $ stats.reset_classes()
    call make_schedule
    jump girl1_failure
    
label girl1_failure:
    
    "GAME OVER"
    # failed, end game here
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

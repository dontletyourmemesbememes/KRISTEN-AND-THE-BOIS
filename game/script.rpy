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
    jump restaurant_date1
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
    
    "> You realize that you’ve only been here for a day, and the only culinary experience you have comes from instant ramen."
    
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
    
    m "Soooo… I actually never caught your name, my name's %(player_name)s."
    
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
    
    "> she forces a smile and pushes your food a few inches away"
    
    m "Sorry about that, maybe you can teach me some basics?"
    
    p "mmm… that sounds okay i suppose...come by tomorrow and I’ll teach you a little of what I know."
    
    jump end_day_1
    
label made_good_food:
    
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
    jump make_schedule
    
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
                jump cafe_date1
            else:
                "Can't do that."
        "Let's go somewhere fancy!" :
            if girl1.get_closeness("Mary") >= 8 :
                jump restaurant_date1
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
    
    jump end_day_1
    
label cafe_date_badending :
    $ girl1.add_closeness(-1)
    "> You guys finish your food. Mary stands up and looks away."
            
    p "Well... have a goodnight."
    
    "> Mary leaves first and you are left alone. You sit for a moment to avoid getting in her way. As you leave the cafe, she is no where in sight."
    
    "> You were unsuccessful in this date."
    
    jump end_day_1
    
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
    
    jump end_day_1
            
#label restaurant_ending:
    
#label restaurant_badending:
    

#==================================================================================================================================================================


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

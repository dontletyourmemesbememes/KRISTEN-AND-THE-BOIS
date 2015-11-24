# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg auditorium = "Auditorium.png"
image bg balcony = "Balcony.png"
image bg cafe = "Cafe.png"
image bg classroom = "Classroom.png"
image bg hallway = "Hallway.png"
image bg home_ec_room = "Home_ec_room.png"
image bg house = "House.png"
image bg karaoke = "Karaoke.png"
image bg music_room = "Music_room.png"
image bg office = "Office.png"
image bg outside_house = "Outside_house.png"
image bg restaurant = "Restaurant.png"
image bg home = "Player_home.png"

init python:
    import random

    class Question:
        def __init__(self,desc,choices,answer):
            self.description = desc
            self.choices = choices
            self.answer = choices[answer]

        def get_description(self):
            return self.description

        def get_choices(self):
            random.shuffle(self.choices)
            return self.choices

        def get_menu_choices(self):
            menu_list = []
            choice_list = self.get_choices()
            for choices in choice_list:
                if choices == self.answer:
                    t = (choices,True)
                else:
                    t = (choices,False)
                menu_list.append(t)

            return menu_list

        def check_answer(answer):
            return answer == self.answer

    class QuestionManager:
        def __init__(self):
            self.question_list = []
        def get_random_question(self):
            return self.question_list[renpy.random.randint(0,len(self.question_list)-1)]
        def add_question(self,desc,choices,answer):
            question = Question(desc,choices,answer)
            self.question_list.append(question)


    class Stats:
        def __init__(self):
            self.stats = {
                "str":0,
                "int":0,
                "cha":0
            }
            self.days = 0

            self.classes = {"Biology (+1 Intelligence)":"biology",
                            "Drama (+1 Charm)":"drama",
                            "Gym (+1 Strength)":"gym"}

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
            self.affection = 0
            self.event = 0

        def add_closeness(self,amount):
            self.closeness += amount
            
        def get_closeness(self,name):
            return self.closeness
            
        def add_affection(self,amount):
            self.affection += amount

        def get_affection(self,name):
            return self.affection

        def set_name(self,name):
            self.name = name
            
        def get_event(self,name):
            return self.event
            
        def add_event(self):
            self.event += 1
            
    def rng_roll(chance): #chance should be between [0,1]
        return chance > renpy.random.random()


# Declare characters used by this game.

define p = DynamicCharacter("unknown_name", color="#c8ffc8")
define m = DynamicCharacter("player_name")
define principal = Character("Principal", color="#c8ffc8")

define mom = Character("Mom", color="#c8ffc8")
define cookies_baked = False
#Cafe date variables~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
define cafe_trigger = 0
define cafe_asked_count = 0
define cafe_boyfriend = False #variable for recording whether or not player has asked about a boyfriend yet.
define cafe_before= False #record whether you have asked her if she's been here before
define cafe_asked1 = False    
#Restaurant date variables~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
define rest1_asked2 = False
define rest1_asked3 = False
define rest2_asked1 = False
define reassure = False

#Music girl variables~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
define girl2_event1_asked1 = False
define girl2_music_choice = 0

# The game starts here.
# Initialize stuff here and shove all the tutorial intro stuff here as well.
label start:
    
    play music "Background Music.mp3"
    
    scene bg office
    with fade
    $ bio_qman = QuestionManager()
    $ gym_qman = QuestionManager()
    $ drama_qman = QuestionManager()

    $ bio_qman.add_question("description",["wrong1","wrong2","wrong3","correct"],3)
    $ gym_qman.add_question("description",["wrong1","wrong2","wrong3","correct"],3)
    $ drama_qman.add_question("description",["wrong1","wrong2","wrong3","correct"],3)


    $ player_name = renpy.input("Most of the documents seem to be in order. Can I get you to sign your name below please?")
    $ stats = Stats()
    $ girl1 = Girl("Mary")
    $ girl2 = Girl("Catherine")
    $ unknown_name = "???"
    principal "Alright %(player_name)s, I believe we're good to go now!"
    
    #show placeholder normal at left
    #with moveinbottom
    
    principal "Allow me to officially welcome to Gouglas Private Academy. This school consists of the brightest students from all over the city, so congratulations for making it!" 
    jump intro

    return

label intro:
    
    
    principal "As this is an elite school, our curriculum is a tad different than other schools in the country."
    principal "Required classes will all be covered during your morning lessons, while {i}optional classes{/i} are held throughout the afternoon. Our most popular ones that we offer are {i}Drama, Biology, and Phys Ed{/i}." 
    principal "In order to foster independence and individual growth in each of our students, we’re extremely flexible in what classes you decide to attend each day." 
    principal "Keep in mind that each class will affect {i}how you grow as a person{/i}."
    principal "Whatever person you decide to become can help or harm any choices you make in the future, so choose your classes wisely."
    # "But be choose wisely. Once you set your classes today, it’ll be permanent for the rest of the year. 
    principal "Now, If you’re ready, I can take you on a tour of the school and some of the club rooms. Do you want me to repeat anything?"
    menu: 
    
        "I think I'm good.":
            principal "Please follow me, %(player_name)s."
            jump school_tour
        "Can you go over how this works again?":
            principal "Certainly."
            jump intro
    
label school_tour:
    
    scene bg hallway
    with fade
    "> The principal shows you through most of the building and classrooms. Nothing about this school seems particulary unusual." 
    "> Nothing the principal is saying seems particulary important..."
    
    principal "...and here we have the {b}club room building{/b}..."
    
    "> Oh. Time to pay attention."
    
    scene bg home_ec_room
    with fade
    #show image of economics room
    principal "This is the home economics room. Students come here to learn essential life skills like cooking." 
    "> You notice there's someone in the room. Let's take a look!"
    #show image of girl cooking
    principal "Keep in mind that the most sophisticated dishes require a certain amount of stamina as well as some creative style."
    principal "Moving on..."
    
  
    #fade out
    scene bg music_room
    with fade
    #show image of music room
    principal "This is the music room. If you ever want to develop your musical capabilities, then this is the perfect spot to practice!"
    "> You hear someone playing inside. Let's take a peek!"
    #show tsundere playin violin
    principal "Keep in mind that music is an expression of your personality, but also requires a lot of thought process."
    
    
    #fade out

    
    #show image of the gym
    #JUST THE TWO CLUBS FOR NOW
    #principal "This is our fitness centre. We have the newest equipment for any kind of workout. "
    #principal "Remember to keep fit during the year, because it will help you psychologically when you are doing homework and are studying for your midterms."
    #show other girl
  
    principal "Moving on to the next club..."
    #fade out
    "> The other club rooms didn't seem to interest you at all..."

    #go to general image, office or something
    scene bg office
    with fade
    principal "Well those are just examples of the many facilities this school provides."# Make use of your time and be sure to work hard on your academics."
    principal "So... Did you enjoy checking out some of the female students instead of paying attention to what I was saying?"
    principal "Haha, don't worry, you're a young man, so I understand."
    principal "Some words of advice if you're aiming for a relationship. I'm only going to say this once."
    principal "Don't cheat. It's not cool. If you choose someone you're stuck with it. It's how this world works."
    principal "Don't wait. If too much time passes before you make a significant move, any girl is going to think you have no intention to be in a relationship."
    principal "Follow these rules and you won't end up lonely and single for the {b}REST OF YOUR HIGH SCHOOL LIFE.{/b}"
    principal "Remember that this is an elite school and your studies are very important. However, your social life and extra curriculars are crucial for a healthy high school experience too." 
    principal "Best wishes to you!"
    
    $ stats.reset_classes()

    jump make_schedule

label make_schedule:
    
    scene bg classroom
    with fade
    
    if len(stats.get_picked_classes()) == 0:
        m "It looks like I have to choose 2 classes to attend this afternoon."
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
    
    m "Phew... That was a long day, I'll head home for today..."
    $ stats.increment_days()
    
    scene bg home
    with fade
    #fade to show end of day 
    
    "> Next morning."
    
    m "Time to go to class."
    
    "> You somehow manage to stay awake through the intense morning lessons."
    m "Finally done the morning lessons, I was ready to pass out at any moment. So which classes should I take this afternoon?"

    $ stats.reset_classes()
    jump make_schedule
    
label gym:
    $ stats.pick_classes("Gym (+1 Strength)")

    #$ stats.pick_classes("Gym")
    $ question = gym_qman.get_random_question()
    $ desc = question.get_description()
    "Question: %(desc)s"
    $ choices = question.get_menu_choices()
    $ result = renpy.display_menu(choices)
    if result == True:
        $ stats.add_stats("str", 1)
        "Stat raised"
    else:
        "No Stats raised"

    if len(stats.get_picked_classes()) < stats.max_classes:
        m "Guess I'll choose Gym for one choice, I still need to pick another."
    return
    
label drama:

    $ stats.pick_classes("Drama (+1 Charm)")

    #$ stats.pick_classes("Drama")
    $ question = drama_qman.get_random_question()
    $ desc = question.get_description()
    "Question: %(desc)s"
    $ choices = question.get_menu_choices()
    $ result = renpy.display_menu(choices)
    if result == True:
        $ stats.add_stats("cha", 1)
        "Stat raised"
    else:
        "No Stats raised"

    if len(stats.get_picked_classes()) < stats.max_classes:
        m "Guess I'll choose Drama for one choice, I still need to pick another."
    return 
    
label biology:

    $ stats.pick_classes("Biology (+1 Intelligence)")

    #$ stats.pick_classes("Biology")
    $ question = bio_qman.get_random_question()
    $ desc = question.get_description()
    "Question: %(desc)s"
    $ choices = question.get_menu_choices()
    $ result = renpy.display_menu(choices)
    if result == True:
        $ stats.add_stats("int", 1)
        "Stat raised"
    else:
        "No Stats raised"

    if len(stats.get_picked_classes()) < stats.max_classes:
        m "Guess I'll choose Biology for one choice, I still need to pick another."
    return

label extracurricular:
    m "So this is what an elite school is like? Classes seem ridiculously hard. Maybe I should check out those extracurriculars that the principal mentioned."
    $ chosen_girl = stats.get_chosen_girl()
    
    if chosen_girl == 0:
        menu:
            "Home Economics Room":
                jump home_ec_room
            "Music Room":
                "I heard there was a music room. I should go check it out."
                jump music_room 

    
    elif chosen_girl == 1: # Mary is chosen
        
        jump home_ec_day_2
        
    elif chosen_girl == 2: # music girl chosen
        
        jump music_day_2

#-----------------------------START OF MUSIC GIRL---------------------------------------------#

label music_room:
    stop music fadeout 1.0
    
    # play violin music
    
    scene bg hallway
    with fade
    
    "> As you get closer to the music room, you notice the door cracked open an inch. As you approach, you hear sustained instrument that cuts through the opening."
    # fade to show entering room
    scene bg music_room
    with fade
    "> Upon entering, you find a girl drawing her bow flawlessly across the strings. She faces the opposite direction, displaying her hair that follows the dynamics of her playing. You’re compelled to sit down at the piano bench, as your eyes and ears perked up to witness her welcoming and mellow style."
    "> The song grows in depth, as the notes create an atmosphere, sustained in emotion. Her upper body sways intimately with the music, while the hair on the back of your neck rise gradually. you find yourself enveloped by her music."
    
    "Wow… she’s pretty amazing, I need to know this girl’s name."
    "> Her playing approaches the end. You feel anxiety rising up as you stand to attempt talking to her."
    "Now’s my chance to talk to her!"
    
    m "Hey, I just heard you playing and you were pretty awesome!"
    "> She looks back to be slightly surprised, not knowing you were there. Her expression instantly reads 'who the hell are you?'"
    p "I thought I closed the door, how did you get in?"
    m "Oh no, it was opened. Sorry I didn’t know know you wanted to be alone."
    p "I’m practicing, so if you don’t mind, I have a concert to prepare for."
    "> Immediately she gets back to playing, but this time. Her playing loses its warmth, and immediately has an air of superiority."
    
    m "I never caught your name, by the way."
    "> The violin lets out a shriek, and she turns to you in frustration."
    p "Did you not hear me earlier?"
    m "I did, but I don't want to."
    "> Looking frustrated and agitated, she clenches the neck of the violin and stick."
    p "Ugh! Who do you think you are anyways!?"
    m "I’m %(player_name)s. Your playing was pretty inspiring to listen to. What’s your name?"
    "> She holds a frown."
    p "Catherine… I suppose it’s not a HUGE inconvenience if you listen, just try to keep quiet, and don’t do anything to distract me or I am going to kick you out."
    $ unknown_name = "Catherine"
    "This girl’s scary."
    "> She moves to her music stand again raising her bow into position. This time she continues to play, but still not as welcoming and warm as the first time."
    "> You start to get into the music, leaning back while tapping your feet."
    "> Noticing the dust on your elbows after sitting back, you notice the piano."
    "Oh man, this piano’s pretty dusty. I also haven’t touched one of these in a couple years. Now let’s see what we have here..."
    "> You lift the key covering."
    
    $ int_check = stats.get_stats("int")
    menu:
        "Play with her":
            jump play_with_her
        
        "Just sit and listen to her play the violin":
            "> You stay seated and simply listen to her playing."
            menu:
                "Play with her":
                    jump play_with_her
                
                "Attempt to talk to Catherine as shes playing":
                    m "How did you get into playing violin?"
                    "> She plays louder and more aggressively."
                    $ girl2.add_closeness(-1)
                    menu:
                        "Play with her":
                            jump play_with_her
                            
        "Attempt to talk to Catherine as shes playing":
            m "How did you get into playing violin?"
            "> She plays louder and more aggressively."
            $ girl2.add_closeness(-1)
            
            menu: 
                "Play with her":
                    jump play_with_her
                
                "Just sit and listen to her play the violin":
                    "> You stay seated and simply listen to her playing."
                    menu:
                        "Play with her":
                            jump play_with_her         
   
label play_with_her:
    # play with piano
    if int_check >= 1:
        $ girl2.add_closeness(1)
        "> You pick up where there’s an opening, and accompany her. The first few moments feel sluggish and your hands feel clumsy, but after a few bars you’re able to familiarize yourself. You peek over your shoulder to notice that Catherine’s posture is rigid; she doesn’t seem like she’s used to someone playing with her. Her playing begins to become harsher and her facial expression suddenly becomes unimpressed."
        "Hmm... She hasn’t stopped playing yet... I’ll just keep going to see where this takes me."
        "> You listen to her carefully and do your best to follow her, trying to avoid taking over or not supporting her enough. You remember the feeling from before: the chill in your spine, hair upright, and heightened senses."
        "> You can’t see her now, but you’d like to imagine she also is feeling the same way you do."
        "> You listen carefully, and end the song."
        "I think my finish was coordinated with her pretty well. Granted not perfect, but pretty good I think."
        p "That was terrible."
        "> Catherine crosses her arms again and turns her back on you with a puff of air."
        p "But..not bad for an impromptu."
        "> You can’t see the expression on her face but her response makes you smile."
        
        play music "Background Music.mp3" fadein 1.0
        menu:
            "Lightly joke":
                m "You’re amazing at the violin. But yeah, thanks, Cathy!"
                $ girl2.add_closeness(-1)
                p "That’s not my name, I hate being called Cathy."
                m "I’m sorry. It’s nice to meet you Catherine!"
            "Be humble":
                m "Thanks Catherine, but I’m still pretty rusty. I haven’t played since junior high. Your playing earlier inspired me!"
                "> Catherine looks flustered but trying keep an exaggerated mature composure." # guess image here instead of description
                p "..."
                p "Of course! I’m training to be the best you know. It’s nice to meet you too I guess."
        
        m "Well, I think i might take another shot at playing the piano."
        p "What!? what do you mean?"
        m "I’ll be around the music room more often, I like listening to you play and the way you played the violin has inspired me to get back into playing the piano."
        p "Who said you could be in here?"
        m "Would you be opposed? I need to practice a little more, and you could tell me how I’m doing."
        p "I don’t have time to deal with an amateur like you. Ugh....but I guess it’s sort of useful having an accompanist. JUST FOR PRACTICE. Come by tomorrow, don’t be late or else I’ll kick you out."  
        
        # end day
        
    else:
        "> You try to think of what to play, but the keys starts to look more and more like a puzzle. You play the keys but it just makes a loud obstruction to The girl’s music."
        "> She stops midway, pointing the violin bow at you."
        
        play music "Background Music.mp3" fadein 1.0
        p "What did I just say? Why are you even touching the piano, if you don’t have the capacity to play it?"
        "Oh crap."
        m "W-well I haven’t played since junior high, so I’m rusty, I mean just a little rusty or maybe a lot depending on who’s judging that is. I’m usually better I just need to brush up. Actually, I think I might take another shot at playing the piano if you’ll give me a chance."
        p "What? what do you mean?"
        m "I want to be around the music room more often, I like listening to you play and the way you played the violin has inspired me to get back into playing the piano."
        p "You’re terrible. Why should I even give you another chance."
        "> Catherine's eyes look hard and unforgiving."
        m "Please give me another chance! I won’t disappoint you. I’ll leave you alone if I do not meet your standards next time!"
        "> Catherine’s eyes suddenly soften but turns cold again so fast that you’re not sure if you were seeing right."
        p "I..Fine. I’ll give you a shot. Be here tomorrow and don’t be late, or else."
        "> She turns her back to you again. You’re not sure what else to say and you take this as your cue to leave. You get up and just about as you exit the room, you hear Catherine say something else."
        p "If you’re really serious about this, you don’t want to waste your chance or you’ll regret it. Believe me."
        "> She immediately lifts her bow again and starts up playing again, ignoring you. You leave."
    
    # show image of bedroom at night?
    scene bg home
    with fade
    m "That was a long day, time to hit the sack."
    $ stats.increment_days()
        
    "Another day at school..." 
    $ stats.reset_classes()
    call make_schedule
    jump music_day_2
        
label music_event_check_1:
    # music room option
    $ closeness = girl2.get_closeness("Catherine")
    $ day = stats.get_days()
    $ event_num = girl2.get_event("Catherine")
    
    if day < 5 and closeness > -3 and closeness < 5:
        # continue on with music
        return
    elif day >= 5:
        # too long trigger failure event
        jump girl2_failure
    elif closeness <= -3:
        # lost too much closeness
        jump girl2_failure
    elif day < 5 and closeness >= 5 and event_num == 0:
        # trigger event 1 as day < 5 and closess > 5
        # set the event value to 1
        $ girl2.add_event()
        jump music_event_1
    
label music_event_check_2:
    
    $ closeness = girl2.get_closeness("Catherine")
    $ event_num = girl2.get_event("Catherine")
    if closeness >= 8 and event_num == 1:
        $ girl2.add_event()
        jump music_event_2
    else:
        return
    
label music_day_2:
    # should not go to events yet for now
    #call music_event_check_1
    #call music_event_check_2
    #call music_event_check_3
    
    scene bg music_room
    with fade
    
    "> You enter the music room to see Catherine already practicing on her violin."
    p "Hey, you actually came. I hope you are prepared."
    m "I think so! I practiced all of last night!"
    $ str_check = stats.get_stats("str")
    $ int_check = stats.get_stats("int")
    $ cha_check = stats.get_stats("cha")
    
    stop music fadeout 1.0
    menu:
        "Classical (no reqs)":
            "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
            play music "Background Music.mp3" fadein 1.0
            p "Wow. I am impressed. Even though there were some errors, that was a huge improvement from yesterday. You have redeemed yourself. You are free to come back anytime you want and I don't mind playing with you again… It was kind of fun."
            $ girl2.add_closeness(1)
            
        "Rock (Strength 2, Charm 2)":
            p "Rock today? okay I’ll give it a try."
            if str_check >= 2 and cha_check >=2:
                "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
                play music "Background Music.mp3" fadein 1.0
                p "That went better than I thought." # she coughs
                p "I meant for you obviously, I knew that I would be great. That was interesting though. Maybe we should experiment like this more."
                $ girl2.add_closeness(2)
            else:
                "> As you begin to play for the first few bars, you are able to stay on beat with Catherine, However, as the song intensifies, you stress out and begin to play fast and louder. The sounds created by piano overpowers the violin and there is dissonance in the music being played. Despite this, Catherine and  you imagine to finish the piece."
                play music "Background Music.mp3" fadein 1.0
                p "That was terrible. The piano is suppose to accompany the violin not the other way around... But I guess this is a huge improvement from yesterday. I guess I will let you continue coming to the music room because you are dedicated to improve and you kind of have potential.."
                $ girl2.add_closeness(-2)
        
        "Jazz (Charm 2, Intelligence 2)":
            p "OH! I LOVE JAZZ!"
            if cha_check >= 2 and int_check >= 2:
                "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
                play music "Background Music.mp3" fadein 1.0
                p "Wow. I am impressed. Even though there were some errors, that was a huge improvement from yesterday. You have redeemed yourself. You are free to come back anytime you want and I don't mind playing with you again… It was kind of fun."
                $ girl2.add_closeness(2)
            else:
                "> As you begin to play for the first few bars, you are able to stay on beat with Catherine, However, as the song intensifies, you stress out and begin to play fast and louder. The sounds created by piano overpowers the violin and there is dissonance in the music being played. Despite this, Catherine and  you imagine to finish the piece."
                play music "Background Music.mp3" fadein 1.0
                p "That was terrible. The piano is suppose to accompany the violin not the other way around... But I guess this is a huge improvement from yesterday. I guess I will let you continue coming to the music room because you are dedicated to improve and you kind of have potential.."
                $ girl2.add_closeness(-2)
                
    scene bg home
    with fade
    m "That was a long day, time to hit the sack."
    $ stats.increment_days()
    
    "Another day at school..." 
    $ stats.reset_classes()
    call make_schedule
    jump music_day_3

label music_day_3:
    # check for events
    if girl2_event1_asked1 == False:
        call music_event_check_1
        call music_event_check_2
    $ girl2_event1_asked1 = False
    
    scene bg music_room
    with fade
    "> You enter the music room to see Catherine already practicing on her violin."
    p "Hey, you actually came. I hope you are prepared."
    m "I think so! I practiced all of last night!"
    $ str_check = stats.get_stats("str")
    $ int_check = stats.get_stats("int")
    $ cha_check = stats.get_stats("cha")
    stop music fadeout 1.0
    
    menu:
        "Classical (no reqs)":
            "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
            play music "Background Music.mp3" fadein 1.0
            p "Wow. I am impressed. Even though there were some errors, that was a huge improvement from yesterday. You have redeemed yourself. You are free to come back anytime you want and I don't mind playing with you again… It was kind of fun."
            $ girl2.add_closeness(1)
            
        "Folk (Strength 2, Charm 3)":
            p "Really? Okay, I’m not very used to folk, but if you want."
            if str_check >= 2 and cha_check >=3:
                "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
                play music "Background Music.mp3" fadein 1.0
                p "Wow. I am impressed. Even though there were some errors, that was a huge improvement from yesterday. You have redeemed yourself. You are free to come back anytime you want and I don't mind playing with you again… It was kind of fun."
                $ girl2.add_closeness(2)
            else:
                "> As you begin to play for the first few bars, you are able to stay on beat with Catherine, However, as the song intensifies, you stress out and begin to play fast and louder. The sounds created by piano overpowers the violin and there is dissonance in the music being played. Despite this, Catherine and  you imagine to finish the piece."
                play music "Background Music.mp3" fadein 1.0
                p "That was terrible. The piano is suppose to accompany the violin not the other way around... But I guess this is a huge improvement from yesterday. I guess I will let you continue coming to the music room because you are dedicated to improve and you kind of have potential.."
                $ girl2.add_closeness(-2)
        
        "Blues (Charm 2, Intelligence 3)":
            p "Alright, if you want."
            if cha_check >= 2 and int_check >= 3:
                "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
                play music "Background Music.mp3" fadein 1.0
                p "Wow. I am impressed. Even though there were some errors, that was a huge improvement from yesterday. You have redeemed yourself. You are free to come back anytime you want and I don't mind playing with you again… It was kind of fun."
                $ girl2.add_closeness(2)
            else:
                "> As you begin to play for the first few bars, you are able to stay on beat with Catherine, However, as the song intensifies, you stress out and begin to play fast and louder. The sounds created by piano overpowers the violin and there is dissonance in the music being played. Despite this, Catherine and  you imagine to finish the piece."
                play music "Background Music.mp3" fadein 1.0
                p "That was terrible. The piano is suppose to accompany the violin not the other way around... But I guess this is a huge improvement from yesterday. I guess I will let you continue coming to the music room because you are dedicated to improve and you kind of have potential.."
                $ girl2.add_closeness(-2)
                
    scene bg home
    with fade            
    m "That was a long day, time to hit the sack."
    $ stats.increment_days()
    
    "Another day at school..." 
    $ stats.reset_classes()
    call make_schedule
    jump music_day_4
    
label music_day_4:    
    
    # check for events, day is 4 here
    if girl2_event1_asked1 == False:
        call music_event_check_1
        call music_event_check_2
    $ girl2_event1_asked1 = False # reset it now that checks are done
    scene bg music_room
    with fade
    
    "> You enter the music room to see Catherine already practicing on her violin."
    p "Hey, you actually came. I hope you are prepared."
    m "I think so! I practiced all of last night!"
    $ str_check = stats.get_stats("str")
    $ int_check = stats.get_stats("int")
    $ cha_check = stats.get_stats("cha")
    
    stop music fadeout 1.0
    menu:
        "Classical (no reqs)":
            "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
            play music "Background Music.mp3" fadein 1.0
            p "Wow. I am impressed. Even though there were some errors, that was a huge improvement from yesterday. You have redeemed yourself. You are free to come back anytime you want and I don't mind playing with you again… It was kind of fun."
            $ girl2.add_closeness(1)
            
        "Latin (Strength 3, Charm 4)":
            p "Very very interesting. I don’t know how to start... ummm... here goes nothing."
            if str_check >= 3 and cha_check >=4:
                "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
                play music "Background Music.mp3" fadein 1.0
                p "Wow. I am impressed. Even though there were some errors, that was a huge improvement from yesterday. You have redeemed yourself. You are free to come back anytime you want and I don't mind playing with you again… It was kind of fun."
                $ girl2.add_closeness(2)
            else:
                "> As you begin to play for the first few bars, you are able to stay on beat with Catherine, However, as the song intensifies, you stress out and begin to play fast and louder. The sounds created by piano overpowers the violin and there is dissonance in the music being played. Despite this, Catherine and  you imagine to finish the piece."
                play music "Background Music.mp3" fadein 1.0
                p "That was terrible. The piano is suppose to accompany the violin not the other way around... But I guess this is a huge improvement from yesterday. I guess I will let you continue coming to the music room because you are dedicated to improve and you kind of have potential.."
                $ girl2.add_closeness(-2)
        
        "J-pop (Charm 3, Intelligence 4)":
            p "Oh great! I have this song from a dating sim game I wanted to play!"
            if cha_check >= 3 and int_check >= 4:
                "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
                play music "Background Music.mp3" fadein 1.0
                p "Wow. I am impressed. Even though there were some errors, that was a huge improvement from yesterday. You have redeemed yourself. You are free to come back anytime you want and I don't mind playing with you again... It was kind of fun."
                $ girl2.add_closeness(2)
            else:
                "> As you begin to play for the first few bars, you are able to stay on beat with Catherine, However, as the song intensifies, you stress out and begin to play fast and louder. The sounds created by piano overpowers the violin and there is dissonance in the music being played. Despite this, Catherine and  you imagine to finish the piece."
                play music "Background Music.mp3" fadein 1.0
                p "That was terrible. The piano is suppose to accompany the violin not the other way around... But I guess this is a huge improvement from yesterday. I guess I will let you continue coming to the music room because you are dedicated to improve and you kind of have potential.."
                $ girl2.add_closeness(-2)
    
    scene bg home
    with fade
    m "That was a long day, time to hit the sack."
    $ stats.increment_days()
    
    "Another day at school..." 
    $ stats.reset_classes()
    call make_schedule
    jump girl2_failure
    
label music_event_1:
    # triggered from closeness
    scene bg music_room
    with fade
    $ day = stats.get_days()
    "> You enter the music room quietly; you see Catherine on the floor curled up in a kneeling position. Sprawled around her are vibrantly coloured posters and unopened markers."
    menu:
        "Hey Catherine… should I come by another time? You look busy right now..":
            p "I am busy at the moment. Leave me alone."
            $ girl2.add_affection(-1)
            "> You decide to leave her alone"
            $ girl2_event1_asked1 = True 
            if day == 3:
                # show home image
                scene bg home
                with fade
                m "That was a long day, time to hit the sack."
                
                "Another day at school..." 
                $ stats.reset_classes()
                call make_schedule
                jump music_day_3
            elif day == 4:
                # show home image
                scene bg home
                with fade
                m "That was a long day, time to hit the sack."
                
                "Another day at school..." 
                $ stats.reset_classes()
                call make_schedule
                jump music_day_4
            
        "Don't say anything yet":
            "> You decide to watch her and see what she’s doing. You notice her tugging on her hair occasionally and letting out fits of frustration."
            "> ring ring ring"
            p "sigh..."
            p "Hi Mom."
            p "... I’m at school still making posters for the concert."
            p "... No, I don’t think I’ll be home in time for dinner."
            p "... I know, I still need to practice, don’t worry I’ll be fine."
            "> Catherine’s tone sounds a little frustrated at this point."
            p "... Don’t worry about it-- I said I’ll be fine!"
            p "... I’m sorry for lashing out, I am just frustrated right now."
            p "... You too, bye..."
            "I wonder why she sounded so angry at the end of her conversation."
            "> You walk nearer to her without her noticing and upon closer inspection, notice that she’s making posters for some sort of concert."
            m "Hey Catherine, what are all these for? Do you need help with something?"
            p "Oh! Hi %(player_name)s."
            "> She seems embarrassed that you’re seeing her like this."
            p "I’m trying to make posters for this concert; I need to promote it. No need for help, I’m perfectly capable of doing this myself."
            m "Of course, of course! If I help you now though we’ll have time to play some music. I’ve been looking forward to it all day."
            p "Hmmm...Fine! Do whatever you want."
            "> She still seems embarrassed for accepting your help but at the same time, satisfied."
            "> You end up kneeling beside her. As you sit she retracts a couple inches away from where you’re sitting."
            "She doesn’t seem that comfortable with me maybe I should try to make some conversation."
            menu:
                "What is the concert for?":
                    $ girl2.add_affection(1)
                    p "This is my opportunity to be the greatest violinist of our time."
                    m "What...?"
                    p "A representative from the most prestigious music schools in the UK was invited to view my performance. Basically I’m being evaluated before actually going there to do my audition for the school."
                    m "Uh huh... congrats, Cathy!"
                    p "Idiot. Don't call me that."
                    m "hahahahaha!"
                    "> She furiously starts sketching her posters."
                    menu:
                        "What do you need me to do?":
                            jump music_event_1_part_2
                    
                "What do you need me to do?":
                    jump music_event_1_part_2
        
label music_event_1_part_2:
    p "Can you just sketch details, in pencil?"
    m "Don’t you want me to do more than that?"
    p "No. I can’t have any clumsy mistakes."
    "> You look at the posters in front of her."
    m "But you didn’t even colour in the lines."
    "> Caterine is flustered."
    p "N-no! That’s for visual effect! I guess it’s hard to appreciate for an uncultured eye."
    m "That is debatable."
    p "Just get to work!"
    
    "> You work for some time, not saying anything to each other."
    "> You look at your clock and notice that the sun is starting to set."
    "> You look towards the window and you see the sunlight give a warm colouring to the surroundings. The chalk dust in the air highlights the sun rays giving the room a calm atmosphere."
    "> Your eye wander the room and lead to Catherine, in the middle of the room and under the sun rays. She’s intently finishing up the final touches on the posters."
    "> She looks like she’s in a spotlight. She looks so natural in it, like she was made to be in a spotlight. Light passes through her hair giving it an ethereal look. It drapes down, and on her shoulders. By observing her alone, you feel unsettled and begin to feel hot. From your chest and back, traveling up to the side of your neck, your body is uncomfortably warm."
    "> She tucks her hair behind her ear, as she finishes up the final touches, but is then surprised catching you staring at her, from the side of her view."
    
    p "...Why are you staring at me?"
    menu:
        "Is it hot in here?":
            $ girl2.add_affection(-1)
            p "No not really, why are you sweating? That’s kinda gross."
            "WHY AM I SWEATING???"
            m "uh gah... don’t worry about it. It’s just hot."
            p "... o--okay..."
            menu:
                "Sorry you just looked really good today":
                    $ girl2.add_affection(-1) 
                    p "Creep."
                    "Uhhh maybe I shouldn’t have said that, she probably thinks I’m weird."
                    "> You don’t really know how to follow up on that response, so you decide to let the awkward space settle for a moment."
                    menu:
                        "Wow, the posters look amazing! We did a good job":
                            jump music_event_1_part_3
                "Wow, the posters look amazing! We did a good job":
                    jump music_event_1_part_3
                    
        "Sorry you just looked really good today":
            $ girl2.add_affection(-1)
            p "Creep."
            "Uhhh maybe I shouldn’t have said that, she probably thinks I’m weird."
            "> You don’t really know how to follow up on that response, so you decide to let the awkward space settle for a moment."
            menu:
                "Is it hot in here?":
                    $ girl2.add_affection(-1) 
                    p "No not really, why are you sweating? That’s kinda gross."
                    "WHY AM I SWEATING???"
                    m "uh gah… don’t worry about it. It’s just hot."
                    p "... o--okay..."
                    menu:
                        "Wow, the posters look amazing! We did a good job":
                            jump music_event_1_part_3
                "Wow, the posters look amazing! We did a good job":
                    jump music_event_1_part_3
                            
        "Wow, the posters look amazing! We did a good job":
            jump music_event_1_part_3

label music_event_1_part_3:
    $ girl2.add_affection(1) 
    "> She looks happy at your comment."
    p "I guess you aren’t that useless."
    m "Thanks?..."
    "At least I’m not ‘super useless’..."
    m "I was thinking we should probably get to practicing soon."
    p "Oh! Of course, I didn’t forget about that---"
    "Sureee..."
    
    scene bg hallway
    with fade
    "> Catherine and you are finished making the posters for the concert and put them around the school."
    
    scene bg music_room
    with fade
    
    m "Do you want to play now?"
    p "Uh. Sure. What do you want to play?"
    stop music fadeout 1.0
    menu: 
        "Beethoven violin Sonata o. 9 Op.47":
            m "Let's play Beethoven." #ADD MUSIC
            $ girl2_music_choice = 1
            play music "Beethoven.mp3" fadein 1.0
            
        "Chopin Tristesse Etudes in E major":
            m "Let's play Chopin." #ADD MUSIC
            $ girl2_music_choice = 2
            play music "Chopin.mp3" fadein 1.0
            
        "Rondo Capriccioso- Saint-Saens":
            m "Let's play Rondo" #ADD MUSIC
            $ girl2_music_choice = 3
            play music "Rondo.mp3" fadein 1.0
            
    # "> After music plays for x time or whatever"
    while(1):
        $ renpy.pause(5.0)
        menu:
            "Finish here?":
                jump outta_girl2_while_loop
            "Keep playing?":
                pass
                
label outta_girl2_while_loop:                
    stop music fadeout 1.0
    play music "Background Music.mp3" fadein 1.0
    
    m "That was fun!"
    p "Yeah.. You're getting better."
    m "Here's an idea... do you think that I could play with you in your concert?"
    p "OF COURSE NOT!!! This is actually important."
    menu:
        "Change your mind":
            $ girl2.add_affection(-1)
            m "Whatever, It’s not like I cared enough to help anyways."
            "> She looks pretty mad at that last comment."
            p "You don’t have to be so butthurt about it."
            "Maybe I shouldn’t have thought out loud."
            
        "Try to convince her":
            $ girl2.add_affection(1)
            m "What?! Why not? I think it would be fine, Cathy! If you ever want an accompanist, I’ll be around."
            "> She avoids eye contact and slightly blushes."
            p "...Thanks, I’ll think about it. BUT I TOLD YOU NOT TO CALL ME THAT."
            
    "> Catherine huffs."
    p "Anyways, I should get going."
    "> She starts to pack up quickly and begins to rush out."
    m "I’ll see you tomorrow then."
    p "...Yeah"
    "Hmm she seems a little off. Was it something I said?"
    $ day = stats.get_days()
    if day == 3:
        jump music_day_3
    elif day == 4:
        jump music_day_4
    
label music_event_2:
    # triggered from closeness
    "> You receive a text from Catherine."
    p "'Come to the music room for a minute'"
    
    scene bg music_room
    with fade
    "> You walk into the music room, no music is being played which is strange."
    "> You see Catherine leaning against the window sill. She’s looking out the window smiling. She’s looking at the trees swaying in the breeze."
    "I guess it’s a good day out."
    "> The warm lighting gives her a glow, where she seems so peaceful. For some reason everything seems so vibrant."
    "> Catherine sees your reflection in the window and turns around to address you with a smile on her face."
    p "Can I ask you for a favour?"
    
    menu:
        "Yeah, of course":
            $girl2.add_affection(1)
        "Sure, if you act a litter nicer to me":
            $girl2.add_affection(-1)
    
    "She looks pretty concerned, I wonder what this about"
    p "So... the concert..."
    m "Yeah?"
    p "Apparently I’m required to have an accompanist."
    m "Oh? and?"
    "> You try not to crack a smile knowing whats coming."
    p "So... I... may need you to play as my accompanist."
    m "I don’t know... I thought I wasn’t good enough?"
    "I’m not sure if I should be teasing her at a situation like this, but I need to milk this opportunity."
    "> She seems surprised at your response like she was expecting you to agree right away. Her face turns mad red and squeezes her eyes shut."
    p "Please! This is my only opportunity! I know I’ve been mean to you this whole time."
    "> Her eyes begin to water."
    p "But I just get so frustrated when I can’t do anything myself because people won’t see me as strong, but now I need someone and I find myself with no one else to lean on. Please..."
    "Oh crap. She’s super serious right now."
    menu:
        "Yeah don’t worry, I said I was going to be around if you needed me, right? Let’s start practicing for it!":
            jump music_event_2_part_2

label music_event_2_part_2:
    
    scene bg music_room
    with fade
    "> You arrive outside of the music room. The suit you’re wearing makes you feel stiff and limited in mobility."
    "I think I look okay, I can’t tell with only the moonlight"
    "> You receive a text from Catherine."
    
    scene bg balcony
    with fade
    p "'Hey, I’m on the balcony'"
    "> You get to the top of the building, and through a wide set of glass double doors you see her in a white dress. As you pass the doors, the scenery opens wide overlooking the city dotted with streetlights and cars."
    "> You lean on the wide railing, next to her. On the side of your vision her dress and skin glow in the moonlight. both of you don’t look at each other, but enjoy the expanded scenery."
    menu:
        "You look good in this lighting":
            $girl2.add_affection(-1)
            p "What about other lightings?"
            "Oops, I guess that came out wrong."
        "It's a beautiful night":
            $girl2.add_affection(1)
            p "Yeah, it is."
            
    m "It’s the big day huh? How are you feeling?"
    p "My palms are a little sweaty and my head is all jumbled with worries."
    m "It will be fine, don’t worry about it. Let’s just try our best!"
    p "I need this to be perfect..."
    menu:
        "Downplay it to make her feel more at ease":
            $girl2.add_affection(-1)
            m "Calm down a little, it’s not a big deal."
            p "Haven’t you been listening at all?"
            "Oh crap that wasn’t smart of me."
            menu:
                "Reassure her":
                    m "Well it’s an important day to you right? You want to get into the school?"
                    p "..."
                    m "What’s with the silence?"
                    
        "Reassure her":
            $girl2.add_affection(1)
            m "Well it’s an important day to you right? You want to get into the school?"
            p "..."
            m "What’s with the silence?"
            
    p "To be completely honest, I couldn’t care less if I went to the music academy or not. Not anymore anyways..."
    m "I thought that was your goal? To become the greatest violinist of our time?"
    p "I mean, excelling at playing the violin is a goal and passion, but I want this to say I was able to do it too."
    m "Sounds like a lot of work for some recognition."
    p "I know... But you don’t know what it’s like, always having people holding your hand while you do anything, not letting you take your own steps, not letting you take any credit... or maybe you do... or you could at least try understanding."
    "> At this moment she turns and looks up at you, with both eyes. The moonlight reflects off of them, for a moment captivating you. At this angle you’re able to see her red lips and rosy cheeks. You feel like a pin went through your chest."
    m "I think I can understand. What if I said that even though I’m here, as your accompanist, I see everything you’ve worked towards, and I think you have definitely proved that you are more than capable of handling yourself?"
    "> She smiles and her eyes look away."
    p "I’d be happy…"
    "> She sees your watch."
    p "Oh! it’s almost time to go! Quick smell my perfume, make sure it smells good!"
    "> She pulls back her hair, and leans forward, exposing her neck to you."
    "> You don’t have time to react smoothly, you quickly lean in to smell."
    "> When you breathe in the scent, it’s like fireworks begin going off your head. This feeling travels down through the rest of your body, but you feel something briefly press against your cheek."
    p "That was for good luck...and for listening to me."
    "> She covers her mouth, and avoids eye contact, blushing."
    m "Thanks..."
    p "D-don’t look at me like that, you’re wasting time."
    "> She grabs your hand and leads you through the doors into the building."
    
    scene bg auditorium
    with fade
    "> You feel like a ragdoll as she makes sharp corners towards back-stage. She stops abruptly and turns around quickly to face you. Her eyes are shining with excitement and nervousness."
    p "Ready?"
    m "Your palms are sweaty"
    "Oh God, I literally could have said anything else."
    "> She pulls her hand quickly away and picks up her violin."
    p "Don’t get full of yourself. Let’s do this."
    "> You walk out onto stage, as you look out you don’t see a single face, but you feel everyone stare. The silence permeates."
    "> You take a seat at the piano and wait for her signal."
    "> You hear her draw her bow across her strings. Her playing is colourful and vibrant, full of expression. As the song progresses, you feel her stage presence is powerful, and you do what you can to support her. You notice your head nodding, and feeling the momentum of the keys. You feel each other’s playing styles as you progress to the end."
    # cue music here
    stop music fadeout 1.0
    if girl2_music_choice == 1:
        play music "Beethoven.mp3" fadein 1.0
    else if girl2_music_choice == 2:
        play music "Chopin.mp3" fadein 1.0
    else:
        play music "Rondo.mp3" fadein 1.0
        
    while(1):
        $ renpy.pause(10.0)
        menu:
            "Skip?":
                jump outta_girl2_while_loop2            
                
label outta_girl2_while_loop2:                
    stop music fadeout 1.0
    play music "Background Music.mp3" fadein 1.0
    
    "> You reach the end of the song, and you get up to stand next to her. When you approach her, she holds out her hand in front of you, you grab it then both of you bow. The audience gives you a large applause."
    "> Both of you walk off stage."
    p "We did it!"
    menu:
        "Hug her":
            $ girl2.add_affection(1)
            m "Yeah, good job!"
            "> You hug her. you intended to have a quick hug, but it lingers for a while longer."
            p "I’m really thankful for you helping me out."
        "Talk about the Academy":
            $ girl2.add_affection(-1)
            m "You did it, you’re sure to get in now! I’m glad it went well."
            p "Oh... yeah right. thanks..."
            
    m "We should celebrate!"
    p "Celebrate? what do you have in mind?"
    m "How about Karaoke?"
    p "Karaoke?"
    m "Yeah, that thing where you sing in a room..."
    p "I know what it is, but why Karaoke?"
    m "Why not? you’ve been so stressed out on music lately, this is a good way to destress with music."
    "> She sighs."
    p "Okay..."
    m "GREAT! LET’S GO"
    jump music_event_3
            
label music_event_3:
    # karaoke event here, success or failure
    scene bg karaoke
    with fade
    m "Here we are."
    p "Y-yeah..."
    m "What’s wrong, Cathy?"
    p "I’ve never sung in front of anyone..."
    m "So wait, you’re telling me that you can get on a stage in front of hundreds of people, but you can’t sing in front of me?"
    p "IT’S DIFFERENT, The violin has a good voice."
    menu:
        "Reassure her":
            $ girl2.add_affection(1)
            m " It can’t be that bad, don’t worry, I’m not here to judge you."
            p "Liar..."
            m "PROMISE."
            "> She rolls her eyes."
            p " Don’t say I didn’t warn you."
            
        "Joke":
            $ girl2.add_affection(-1)
            m "Well that’s a shame, I guess that’s the problem with hiding behind an instrument your whole life."
            p "Aren’t you a tad bit conceited?"
            m "That came out wrong..."
            p "Yeah it did."
    
    p "Well... let’s get this over with."
    "> You place your hands on her shoulders and guide her into the karaoke room."
    m "Come on, don’t worry it’s going to be fun!"
    "> When you sit down, you place songs in the playlist. As one of them is about to begin, you notice out of the corner of your eye, Catherine clutching the mic with both hands. she holds it with her arms retracted close to her chest."
    m "C’mon lighten up! It’s just us. Okay deep breaths."
    "> You take 2 short consecutive breaths out, followed by one drawn out exhale."
    "> She bursts out laughing."
    p "That’s what you do when you’re giving birth!"
    m "THEN YOU HAVE NOTHING TO WORRY ABOUT!"
    "> She laughs."
    p "Alright, alright I’m ready."
    "> Her shoulders relax, and she takes a deep breath."
    "> The music starts playing, You start the song slow. following the lyrics her voice takes you by surprise. You are taken back for moment to the point where you stop singing out of disbelief. Her voice actually is powerful and smooth."
    "SHE LIED TO ME"
    "> You decide to just go with it. You have an almost a deja vu moment, as if you were her accompanist again. Naturally, you begin to harmonize with her. It must be from practising with her. At one point of the song, you both feel each other pushing your diaphragms to their limit. You look at each other trying not to laugh."
    "> You see her under the fluorescent rose lighting of the room, she looks like she’s really having enjoying herself. She looks at you and smiles as the song ends."
    p "That was great!"
    "> She begins laughing uncontrollably while leaning forward."
    "> She beings to lose balance as she falls forward, and falls in your direction. You react by trying to catch her with both arms, but her momentum catches you off guard and pushes you back. You fall directly on your butt."
    p "OH! I’M SO SORRY ARE YOU OKAY?"
    "> She immediately panics and clumsily tries helping you up."
    m "Probably just fractured my tailbone, but I’m fine."
    p "SERIOUSLY?"
    m "Don’t worry... I’m just kidding"
    p "Don’t scare me like that..."
    m "Since when did you start worrying about me so much?"
    "> Her cheeks instantly turn red."
    p "I-I don’t know what you’re talking about... Idiot."
    menu:
        "Hey, if you want to talk about something, I’m listening":
            $ girl2.add_affection(1)
            p "..."
            
        "Oh alright":
            $ girl2.add_affection(-1)
            p "... Why do you have to be so dense all the time?"
            
    "> She sighs."
    p "Look... It’s been really hard for me to be comfortable around you."
    m "What do you mean?"
    p "In the short time I’ve known you, I don’t think I’ve ever felt so close to anyone. At first I couldn’t stand you being around, but you just kept persisting to help me out and to help you out. Then well I guess you just grew on me."
    m "Is that a bad thing?"
    p "No… I’m just a little confused, that’s all… I’ve grown up in a well off family, and I always was given opportunities, as if they were served to me on a silver platter. I never felt like I earned anything. I eventually just hated it when people helped me accomplish tasks, people always checking up on me saying 'Do you need help with that?' As if I couldn’t handle myself, as if I was completely incapable of doing anything. I started to be secluded from people, and refuse people that tried to get close to me."
    m "What about now?"
    p "I don’t know anymore. I guess you could say that you’re now an exception to the rule."
    "> She smiles, leans back into the couch, and stares blankly towards the karaoke lyrics rolling."
    p "You know, it’s funny. I try to push people away, but then one person is just able to push through all the walls I set up. I didn’t want to trust that person, but I end up leaning on them the most, when I’m in need."
    "> She shifts her weight, so that her rests upon your shoulder."
    "> You feel a tension while your beats per minute skyrocket. It’s like your head is going to explode from built up pressure."
    m "H-hey Ca--"
    p "Just be quiet for a moment..."
    "> Neither of you move while the karaoke lyrics roll and the rose lights pulsate in the room. From this atmosphere, you just enjoy each other’s presence."
    menu:
        "Hey Cathy, do you want to go out with me?":
            # check affection level
            $ affection = girl2.get_affection("Catherine")
            # if success:
            if affection > 6: # NUMBER CAN VARY
                p "Does it look like I don’t want to?"
                m "Well maybe you just wanted to be friends."
                p "Sometimes I can’t believe how clueless you can be... So I’ll say it plainly: I want to go out with you."
                "> She wraps her arms around your torso, smiling. You both continue to bask in the emotions until it’s time to go."
                p "Thank you for everything, I’m really glad to have met you in my life..."
                jump music_event_3_part_2
            # if failure:
            else:
                p "Does it look like I don’t want to?"
                m "Well maybe you just wanted to be friends."
                p "Sometimes I can’t believe how clueless you can be... But, I can’t..."
                m "..."
                p "I got into the academy..."
                m "Oh... Congrats..."
                "> She wraps her arms around your torso, and begins to have tears streaming down her face."
                p "I’m so sorry... as much as I want to be with you... this is a really important opportunity."
                m "No of course... I couldn’t expect you to drop everything for me..."
                "> You both sit and try to savour the moment. She latches onto you tight, not wanting to let go. You sit trying to hold on to each other’s presence inevitably comes to an end."
                p "Thank you for everything, I’m really glad to have met you in my life..."
                jump girl2_fail_end
    
label music_event_3_part_2:
    scene bg home
    with fade

    "> A few days have passed since that day."
    "> Your phone rings."
    m "Hello?"
    p "Hi %(player_name)s."
    m "Hey, Cathy!"
    p "I got the results from the evaluation."
    menu:
        "Great! this will be a great opportunity for you!":
            p "It is good..."
            m "I'll see you at the music room then."
            
        "Oh I see, how do you feel about it?":
            p "Hmm... I don’t know if I really want to go anymore."
            m "What about being the greatest violinist ever?"
            p "Well I just wanted to talk to you about it too, wanna meet in the music room?"
            m "Sure."
            
    scene bg music_room
    with fade
    "> You arrive to the music room."
    "> You see her again against the window sill."
    m "Hey, Cathy."
    p "Hey..."
    m "Did you want to talk about it?"
    p "I’ll just get to the point: Do you want me to go or not?"
    m "Wait what? For the Academy? why does my opinion matter?"
    p "Because it matters to me... because you’re important to me."
    m "Oh..."
    p "So tell me, do you want me to stay or not?"
    menu:
        "I want you to stay":
            jump girl2_good_end
            
        "I think you should take the opportunity":
            m "I completely support your decision." 
            p "Ohh... haha... Yeah, thanks for supporting me"
            m "Yeah, of course."
            "> She sighs."
            p "Well I guess this is what I asked for."
            m "Don’t worry, I think you’ll go really far with it. You’ll be able to experience a lot of great things, especially living in the UK independently."
            p "Yeah you’re right..."
            "> She seems frustrated about something."
            p "I don’t get it! I haven’t even known you for that long, but all the sudden you’ll be out of my life. I tried so hard to be independent and do things on my own, and when I finally get the chance, I don’t want it. I end up depending on you anyways. I even said 'yes', when you asked me out!"
            menu:
                "We can still keep in touch":
                    m "Hmm... You didn’t necessarily depend on me, you could always do it by yourself, I was just an accompanist. Besides we can still keep in touch."
                    p "Yeah... that’s a fair argument."
                    "> She shoves her face into your chest and latches around your torso."
                    p "...Will you remember me?"
                    m "What if told you I will?"
                    p "That would make me happy... Well... Goodbye then..."
                    m "This isn’t 'goodbye', it’s just a 'see you later'..."
                    jump girl2_bad_end
                    
                "Change your mind":
                    m "I'm just trying to not be selfish but believe me when I say I really do want you to stay. You're important to me and it would hurt to watch you leave."
                    jump girl2_good_end
                    
        "You should make the decision yourself":
            "> Catherine seems frustrated."
            p "I don't get it! I haven't even known you for that long, but all the sudden you'll be out of my life. I tried so hard to be independent and do things on my own, and when I finally get the chance, I don’t want it. I end up depending on you anyways. I even said 'yes', when you asked me out!"
            m "This is finally your chance to be independent."
            m "This is what you wanted. What you worked for. You made it and you shouldn't let me hold you back."
            p "...Is it so wrong to have someone to lean on at least sometimes...I thought I could depend on you. We’ve been through a lot together...I really had feelings for you."
            m " I didn’t mean it like that..."
            p "Forget it. You’re right. I don’t know what I was thinking. I’ll go ahead with the academy. Thank you for everything. Let’s both work hard on our separate paths."
            "> Catherine starts walking towards the door but stops at your side. She glances up towards you quickly but then looks away and continues out the door, leaving you behind. You’re left alone standing in the silent music room and you have a feeling you won’t be playing the piano for a long time."
            jump girl2_bad_end

label girl2_failure:
    "GAME OVER"
    return
    
label girl2_bad_end:
    "GAME OVER"
    return

label girl2_good_end:
    "> She smiles."
    p "hahaha! You’re funny."
    "> She continues to laugh at you, but you stand there confused at what just happened."
    m "I think I'm lost."
    p "I already declined the offer, so whether you like it or not, looks like you’re going to be stuck with me."
    m "Oh hahaha... I thought you were asking seriously."
    p "Well I was asking, then I could figure out how much you like me hehe..."
    m "charming haha..."
    p "So? what say you? Do I need to make you smell my perfume again?"
    m "Yeah... yeah, I do."
    "> She leans over, then you feel something press against your cheek."
    p "Besides, I already said yes to you. You’re my new dream. You’re mine."
    
    "YOU WIN"
    return
    
label girl2_fail_end:
    "GAME OVER"
    return
    
#-----------------------------END OF MUSIC GIRL---------------------------------------------#

label home_ec_room:
    # show image of room
    # play sound of sizzling noise
    
    # you have chosen Mary as the girl 
    $ stats.set_chosen_girl(1)
    "> In front of the Home-Ec Room."
    "> As you enter the room, you hear a sizzling noise. The fragrances tickle your nose as you enter the room. Your sight is drawn to the centre of the room, to a girl. She looks up to acknowledge you, and she gives a friendly but shy smile."
    
    p "Hello, I haven’t seen your face around, are you new?"
    
    m "Yeah, I just transferred here recently. Is this the cooking club?"
    
    p "Yes! you’ve come to the right place."
    
    m "Where do I sign up?"
    
    p "Well… you kind of need to cook in this club. Show me what you can do first, and then we can talk about your membership."
    
    "> You realize that you’ve only been here for a day, and the only culinary experience you have comes from instant ramen. But how hard could it be?"
    
    p "...Hello? You blanked out for a second, haha. What do you plan on making for me?"
    
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

    "> As you’re working, you can’t help notice the awkward silence settling in. You glance over to her and end up making eye contact. You could probably use this time to get to know her."

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
    "> Next morning."
    m "Another day at school..."
    "> Morning classes don't seem to be getting any easier for you."
    "> Afternoon."
    m "Alright, which classes will I attend today?"
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
        "> Outside home-ec room"
        "> You see Mary standing outside the door."
        p "Hey %(player_name)s! Do you have a minute?"
        
        m "Sure, what's up?"
        
        p "We'll you see.. I was wondering if you would want to grab some coffee after our club today."
        
        m "Of course! Where did you have in mind?"
        
        p "There's this small cafe a couple blocks away from school. It's a nice, quiet place to relax every now and then."
        
        menu: 
            "Sounds great!":
                p "It's a date then!"
                "> Mary looks very excited."
                
            "A cafe... really?":
                p "Is.. that a no?"
                "> Mary starts pouting at you."
                "> You no longer feel any urge to reject her offer."
                p "Heehee.. its a date then!"
        
        jump cafe_date1
        
label girl1_check_2:
    
    $ closeness = girl1.get_closeness("Mary")
    $ event_num = girl1.get_event("Mary")
    if closeness >= 7 and event_num == 1:
        $ girl1.add_event()
        "> Mary is standing outside the club room. It looks like she was waiting for you."
        
        p "Ah! There you are %(player_name)s! Are you free right now?"
        p "You see, my mother had made reservations tonight at this restaurant I've been dying to try."
        p "But, I got a call from her earlier saying she couldn't make it tonight. She suggested I find a friend to go with instead so we don't waste the reservation."
        p "Of course, who better to join me than my new sous-chef. You will join me, right?"
        
        "> You have no power here. To the restaurant!"
        jump restaurant_date1
    else:
        return
        
label girl1_check_3:
    
    $ closeness = girl1.get_closeness("Mary")
    $ event_num = girl1.get_event("Mary")
    if closeness >= 10 and event_num == 2:
        "> You notice Mary doesn't look as cheerful as she normally does when she cooks."
        m "{i}Is she still concerned about what we talked about at the restaurant?{/i}"
        "> You decide to confront her."
        
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

    m "Maybe I should drop by the club room. Mary might be there too."
    
    menu:
        "Blueberry Muffin (No reqs)":
            "> The muffins looks great!"
            p "Wow! They're so fluffy, but the top is so crisp. Good job!"
            $ girl1.add_closeness(1)
            
        "Creme brule (Intelligence 2, Charm 2)":
            if int_check >= 2 and cha_check >= 2:
                # sucess
                "> The Creme brule looks great! nice golden caramelize on it! Looks delicious!"
                p "Looks great. I'm impressed."
                $ girl1.add_closeness(3)
            else:
                # failure
                "> The Creme brule turned out completely black... You think that you burnt it..."
                p "Uhh... is this even edible?"
                $ girl1.add_closeness(-3)
                
        "Lasagna (Strength 2, Charm 1)":
            if str_check >= 2 and cha_check >= 1:
                "> The lasagna turned out great! The cheese is perfectly melted."
                p "The Lasagna looks awesome! The layers look so even!"
                $ girl1.add_closeness(2)
            else:
                "> You reach into the oven and pull out what looks like a pile of plain pasta."
                p "I think you didn't use enough tomato sauce... it looks pretty dry."
                $ girl1.add_closeness(-2)
    
    $ stats.increment_days()

label day_3:
    
    m "Another day at school..." 
    "> You feel you're slowing getting more used to school life."
    "> Afternoon."
    m "Time to pick my afternoon classes."
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
            if int_check >= 3 and str_check >= 3:
                "> The sashimi is perfectly sliced."
                p "Wow! Looks so good I almost don't want to eat it!"
                $ girl1.add_closeness(3)
            else:
                "> The slices turned out oddly-shaped and uneven. You see pieces of bones and scales mixed in with the fish."
                p "Uhh... It's okay. We can always get some more expensive fish."
                $ girl1.add_closeness(-3)
                
        "Carbonara (Strength 2, Charm 2)":
            if str_check >= 2 and cha_check >= 2:
                "> The pasta turned out perfectly cooked! The aroma of the sauce fills the air."
                p "That smells so good!"
                $ girl1.add_closeness(2)
            else:
                "> The pasta looks like a pile of mush..."
                p "I think the pasta is way too overcooked..."
                $ girl1.add_closeness(-2)
            
    $stats.increment_days()

label day_4:
    
    m "Another day at school..." 
    "> Morning lectures weren't anything too difficult for you to understand."
    m "Time to pick my classes"
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
            if str_check >= 4 and cha_check >= 4:
                "> The pasta turned out perfectly cooked! The aroma of the sauce fills the air."
                p "That smells so good!"
                $ girl1.add_closeness(2)

            else:
                "> The pasta looks like a pile of mush..."
                p "I think the pasta is way too overcooked..."
                $ girl1.add_closeness(-2)
                
        "Lemon Meringue Pie (Intelligence 3, Charm 3)":
            if int_check >= 3 and cha_check >= 3:
                "> The pie is firm and the meringue keeps it's form."
                p "Congratulations! The browning of the meringue is beautiful!"
                $ girl1.add_closeness(2)
            else:
                "> The filling is too liquidy; it will not hold its shape."
                p "I think that you over baked the pie."
                $ girl1.add_closeness(-2)
                
    $stats.increment_days()

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
    if stats.get_days == 5:
        "> You feel that too many days have passed and you still haven't gotten any closer to Mary."
        jump mary_bad_end
    else:
        jump mary_bad_end
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



#MARY DATE EVENTS ================================================================================================================================================
#Mary - Cafe Date ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

label cafe_date1 :
    if cafe_trigger == 0: 
        
        if cafe_asked_count == 0 :
            "> You make your way to the cafe with Mary. "
            "> The two of you spend some time casually talking at your table. A warm glow shines through the windows."
        
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
                $ girl1.add_affection(1)
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
    else: 
        return
            

label mary_backstory1 :
    
    $ cafe_trigger = 1
    
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
            $girl1.add_affection(1)
            m" That's rough. If you ever want to talk about it sometime, I'll be here."
              
            p "Thanks. Maybe another time."
            
            m "Yeah, anytime!"
    
    p "Ahh.. It's getting pretty late, I should head home."
    
    m "Yeah, same. It was fun hanging out with you today!"
    
    jump cafe_date_goodending


label cafe_date_goodending :
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
    jump mary_bad_end
    #jump return_to_which_day
    
    #cue bad game ending?

    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Mary - Restaurant Date

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
            $girl1.add_affection(1)
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
            $ reassure = True
            m "Just a hobby? But you're the president of the cooking club!"
            
            p "Titles don’t really mean a whole lot, you haven’t even tried my cooking."
            
            menu :
                "> Be bold" : #stat requirement to say? (+2)
                    $ girl1.add_closeness(2)
                    $ girl1.add_affection(1)
                    m "I feel like there's a pretty easy solution to that." 
                    "> Mary leans forward. Her eyes are on you as she smirks."
                    
                    p "Well, don't expect much if I cook all by myself."
                    
                    m "Haha, I doubt I'll be much help to you. You're on your own!"
                    
                    "> The two of you joke together. Mary playfully punches your shoulder as the two of you roll back laughing in your seats."
                
                "> Joke" : #-1
                    $ girl1.add_closeness(-1)
                    m "Yeah I guess. I mean, how many people even ran for president anyway?"
                    
                    p "Yeah, right..?"
                    
                    "> Mary forces a smile."
                
                "> Be polite":
                    m "You’ve tried mine. We should make something together, and you can teach me a few things."#(+1)
                    $ girl1.add_affection(1)
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
    
#Mary - Home Date~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
label girl1_home_date:

    if reassure:
        m "Hey Mary. I remember before you mentioned that I never tasted your cooking. If it’s okay with you, I’d really like to try some today."

        p "Oh! so you did remember!" 

        "> Mary smiles shyly."
    else:
        m "Hey Mary. After all our conversations about cooking, it's surprising that I haven't actually tried any of your cooking yet."
        m "I'd really like to try some as soon as I can."
        
        "> Mary seems surprised as your sudden request."
        
        p "Hmm.. that is true."
        p "How about today then? You're free right?"
        
        m "Of course."
        
        "> Mary smiles shyly."

    m "I remember you mentioned before that I never tasted your cooking. If it’s okay with you, I’d really like to try some today."

    p "Oh, so you did remember!" 

    "{i}she seems shy but happy{/i}"

    p "Then, why don’t we go back to my house? I have all the ingredients there."

    "> You and Mary head back to her place. You feel tenser than usual, despite the fact you’ve recently spent a lot of time with her. In the corner of your eye you catch her peeking slightly in your directly, but she immediately redirects her vision forward after being noticed."

    p "Today is really beautiful, although I don’t know what we’d do if there wasn’t a breeze."

    p "Then.. Instead of cooking it here, Why don’t we go to my house? There's plenty of ingredients there."
    
    m "S-sure."
    
    "> A nervous tension suddenly fills the air."
    #fade out

    "> You and Mary head back to her place after club activities. You feel tenser than usual, despite the fact you’ve recently spent a lot of time with her." 
    "> In the corner of your eye you catch her peeking slightly in your direction, but she immediately redirects her vision forward after being noticed."

    p "It's a really beautiful day today isn't it?"
    
    "> It seems that Mary's trying her hardest to cope with the awkwardness."
    "> As you approach her house, your eyes follow her as she leaps ahead. She moves forward and her hair swings, pushing its scent towards you."
    "> For a second you get hung on the scent as you’re both entering. She turns to notice you."

    p "You look like you’re lost."

    m "E-ehh. My bad."

    "> You look around her house, a bit flustered that you don’t know how to recover smoothly."
    
    p "Hehehe, the kitchen is this way."

    "> She leads you into the kitchen and immediately moves along the room in a rehearsed efficiency, preparing her supplies." 
    "> You pick up some newspapers in an attempt to help."

    p "No, not there!"

    "> She pulls the papers out of your hands and sets them aside. She turns to you."

    p "Alright! Everything is set! What do you want to eat?"
    call girl1_home_date_choice

    "> You look around the room, it's pretty nice. What should you do?"
    menu:
        "Sit in the living room and play video games.":
            "> ...You look around the room. Not a video game in sight"
            "> Your impatience gets the better of you and you decide to head back into the kitchen."
            jump girl1_home_date_kitchen
        "Go into the kitchen and offer your assistance.":
            jump girl1_home_date_kitchen
        "Look around for any photo albums that she may have.":
            "> You stray into the hall and walk along a line of portraits along the wall, many of them focused around Mary as a child."
            "> Many of the photos appear almost bleak, with little expression on her face." 
            "> Soccer photos, class photos, academic achievement photos, she hardly ever smiles."
            "> You pick one with her flour all over her face as a kid, her glasses caked in powder. Her smile was the only distinguishable feature."
            p "..What are you up to?"
            "> Mary peeks in from the kitchen."
            p "Ah! Nooo! That’s such an embarrassing picture of me! Don't look!"
            m "Hahaha! I think it’s cute."
            "> Her cheeks grow red."
            p "D-don’t say things like that!" 
            "> Despite saying that, it was obvious she was forcing herself to hold back her smile." 
            p "I-I think you should stay put in the kitchen from now on!"
            menu:
                "If you say so.":
                    jump girl1_home_date_kitchen
                "Why is this the only happy photo?":
                    p "I don’t really know. That was the first time my mom let me bake all by myself. I ended up dropping the flour bag and making a huge mess all over the place." 
                    p "As for the other photos, I was just never excited about those things."
                    p "My mom really wanted me to get good grades, so I was told avoid any extra-curricular activity because she felt they would get in the way." 
                    p "'Mary you have to do well so I can get into a good university and find a stable job.'"
                    p "'Marry a good husband, raise a family.' I've heard it all.. "
                    "> Mary seems displeased."
                    menu:
                        "Console.":
                            #Affection up
                            $ girl1.add_affection(1)
                            m "I can tell that your parents really love and care about you. I almost feel like your mom would be more understanding of your current situation if you seriously expressed how passionate you are about cooking."
                            p "Haha, you really do know what to say.. most of the time."
                            p "C'mon. lets get back to the kitchen."
                        "Hug her.": #IDK WHAT TO DO HERE. EXTRA AFFECTION PTS??
                            #Affection up bonus
                            $ girl1.add_affection(2)
                            "> You wrap your arms around her shoulders."
                            p "Wha-?!"
                            "> You pat her head in an attempt to calm her."
                            "> Mary settles down. Her arms slowly wrap around your back."
                            "> The two of you stand silent for a while before finally letting go of each other."
                            p "U-uumm... Thank you. Sorry if I made you feel uncomfortable."
                            m "We should probably head back to the kitchen."
                            P "Y-yeah! Of course!"
                    "> Mary grabs on to your arm and brings you back into the kitchen."
                    jump girl1_home_date_kitchen
            
label girl1_home_date_kitchen:
    "> You watch Mary wander back and forth between different areas of the kitchen. Her smile is an obvious sign she's enjoying herself."
    m "I can't stand just watching! Let me help you, Mary."
    p "Haha. Then.. can you preheat the oven for me?"
    #positive
    "> You accept and decide to help her where you can."
    "> Mary starts measuring dry ingredients from a flour bag."
    p "Ah! Can you handle the wet ingredients while I do this?"
    "> The two of you watch as the parts slowly come together. You feel her elbow brushes against yours every now and then."
    p "Sorry!"
    "> She looks up at you for a brief moment and catches your gaze."
    m "Don’t apologize. It’s alright." 
    "> Her eyes widen slightly, but immediately her face turns back to focus on the preparations."
    "> You notice a bead of sweat trail down from her temple to the front of her neck. Her cheeks flooded with red."
    "> A sense of nervousness and excitement fills your mind. Your breathing becomes shallow."
    p "Uhh.. It’s getting a little warm in here. How hot did you preheat that oven exactly?"
    "> Mary turns to the oven." 
    p "Oh! 350 degrees. Perfect! Uhhm.. I guess the weather is pretty today." 
    "> Frantically, she tries to clear her sweat, however she knocks the bowl of flour off the counter top." 
    p "OH NO!"
    "> You manage save the bowl, however all the flour that was in it is now spread across the floor."
    menu:
        "Somebody’s got a lot of cleaning to do...":
            #negative
            $ girl1.add_affection(-1)
            p "Just get me more flour."
            "> After clearing the mess, you head into the pantry and find an extra-large bag of flour up on the top shelf."
        "Don’t worry! I’ll grab you some more flour.":
            #positive
            $girl1.add_affection(1)
            p "Haha. So dependable."
            "> After clearing the mess, you head into the pantry and find an extra-large bag of flour up on the top shelf."
            
    "> The two of you struggle with the heavy bag as you try to get it. The shifting of the bag causes it to tip over."
    "> Unable to realize that the top of the bag was unsealed, a torrent of flour rains down and covers both your faces."

    m "You got some… Umm.. flour all over you."

    "> You brush the flouer off her shoulders, trying to avoid making awkward physical contact."

    p "Well… I could only assume. My lenses are completely covered. I can’t see a thing."
                
    m "Here I got it for you."

    "> You lean in closer as you lift the frames off her eyes." 
    "> Her brown eyes fixated on you. Unprepared, you find your faces lingering mere inches apart."

    menu:
        "{b}JUST DO IT!!{/b}":
            "> You decide to take the relationship further."
            "> You wipe the flour off her cheeks and find your hands resting on the back of her neck."
            "> Before you know it, your hand pulls her towards you. Anticipation buiilding, you close your eyes."
            "> ..."
            "> ... You feel something press against your lips..."
            "> ..."
            "> Something doesn’t feel right..." 
            "> As you open your eyes you find your mouth, cupped by her hand."
            #SPLIT HERE BASED ON AFFECTION
            if girl1.affection >= 7:
                "> Mary's eyes still wide open, smiling."
                p "I may not be able to see that well without glasses, but I’m not blind."
                p "Don’t get me wrong, I can’t deny that I have feelings for you, but let’s take it slow."
                "> She lifts your hands off of her, she holds you palm open and examines it. You both turn slightly towards the counter to face shoulder to shoulder."
                "> Still examining your hand, she places her hand on top of your’s as if comparing hand sizes."
                p "You know, you have pretty soft hands. I think I’ll hold on to them for a while."
                "> Both your hands begin to offset a little. You decide not to resist and allow your fingers to interlock."
                jump mom_drama
                
            else:
                "> Mary's eyes are half-opened. A look of regret covers her face."
                p "..."
                p "... I can't... I'm sorry..."
                m "..Oh.."
                "> You find yourself lost for words."
                "> Your silence divides you."
                p "Hmm... You see.. I'm really sorry. I can't really find enough reason to see you the same way. That's why I can't return your feelings. We're just not at that level."
                "> You feel your chest compressing, as if the inside of your ribcage is caving in."
                m "Yeah.. I think I understand."
                p "At least we had fun together..."
                m "..."
                p "A relationship right now would be too distracting for me.... "
                p "Also.. I need to focus on other things, like school..." 
                p "...It’s going to be hard to go back to the way things were before."
                m "... Yeah."
                "> You both get up."
                "> You feel as if your legs are about to give out. "
                m "I should probably go..."
                p " ...Yeah."
                "> Mary leads you to the exit. You can’t think of much to say without making it more awkward, so you just keep walking." 
                "> You look back. The door is closed."
                m "{i} I guess that's it, huh...? {/i}"
                #jump bad ending
                return
                
label girl1_home_date_choice:
    menu:
        "Deep-fried sushi" :
            p "Wow! Your taste is pretty extravagant, huh?"
            menu:
                "You don’t have to cook it if you don't want to.":
                    p "You don’t think I can do it?"
                    p "I’ll prove you wrong."
                    "> Mary seems motivateds all of a sudden."
                    #negative
                " I really want to eat this.":
                    "{i}Mary seems intimidated by the challenge but finds her resolve.{/i}"
                    p "I’ll do my best!"
                    "> Mary seems motivateds all of a sudden."
                    #positive/neutral 
        "Instant noodles":
            p "Common..are you taking my offer seriously here?"
            #negative
            call girl1_home_date_choice
            return
        "Triple Layer Chocolate Cake":
            "{i}She seems surprised by your request{/i}"

            p "I thought you’d choose something more difficut. Why did you choose a cake?"
            menu:
                "I didn’t want you to work too hard.":
                    p "What? Don’t worry so much...I can handle it. But alright, I'll make the cake if that’s what you want."
                    #negative
                "So we can share it when you’re done.":
                    p "Haha, Are you usually this corny? But alright, if that’s what you want."
                    #neutral 
                "It has a special meaning.":
                    $ girl1.add_affection(1)
                    p "Meaning?"
                    m "Yeah. Each layer of the cake represents each place we’ve spent time together and how far we’ve come building on our relationship. One layer at a time."
                    "> Mary's face turns red as she tries hard to hold back her laughter."
                    p "Were you always this corny?"
                    "> Mary seems pleased by your thought."
                    p " Alright, I’ll get started then." 

                    #positive
    "> Mary begins cooking the dish and you’re left sitting in her living room alone."
    return 
    
label mom_drama:
    #mom drama stuff
    "> You hear the door bell ring. An unfamiliar voice calls from the door."

    mom "Hey Mary, I’m home from my business trip!"

    p "What?! She's home a day early! Why?!"

    "> Mary looks around at all the cooking equipment and ingredients splayed out on the counters and looks helpless."
    "> She’s visibly panicking and attempts to make a move to put things away but it’s futile. "
    "> You don’t have much time to react before her mom comes into the kitchen."
    "> Her mom spots you."

    mom "Who is this, Mary? Why are you guys alone together?"

    p  "Uh, this is my friend, %(player_name)s. We are just hanging out after school mom. That's all.."

    mom "You shouldn’t be inviting people over when I’m away on a business trip. Shouldn’t you be studying too? It’s a school night!"

    p "I-I just wanted to relieve some stress, it’s just a little bit of cooking."

    "> The tension is getting heavy as you stand there as if you are not even in the room"

    mom "Mary, you should be using your time more wisely. What happen to the money I gave you to buy food with? You should be focusing on getting into university so you can get a career."
    "> Mary's mom's eyes turn to the kitchen counter."
    mom "What is all this doing out here?"
    "> Mary’s mom gestures to all of the equipment and ingredients out in the open."
    "> Mary’s face is flushed of all its color and her voice is small."
    p " I didn’t use the money; it’s still in your office. As for all of this...I-  What if I wanted to be a chef?...Like dad?"
    
    "> Her mom, is taken back for a moment but then her voice is heightened."

    mom "Don’t you remember what happened to your father? Why would you do this? I can’t let that happen to you, Mary, I can’t lose both of you like that." 
    
    p "But.."
    "> Mary looks down and appears defeated."
    mom "No buts! Don’t try to argue with me. Escort your friend out and then go to your room."
    
    "> Mary turns to you with some tears escaping her eyes and falling down her cheeks."
    p "I'm sorry %(player_name)s... I'm sorry about all of this.. Can you please leave?"
    menu:
        "Leave the house":
            "> GG."
            return
            #replace return with jump to game over screen
        "Confront Mary's mom":
            "> You gather all the courage you can muster and take a purposeful step forward, looking at Mary’s mother in the eye."
            m "I'm sorry. I can't leave like this."
            mom "What? How dare you! This is my house."
            "> Mary looks shocked."
            p "%(player_name)s?"
            m"Hear me out, please. Mary told me about what happened with her father. It must’ve been terrible. By the way Mary talks about him, you both must have loved him very much."
            "> Her mom seems agitated by a stranger bringing up family matters and she snaps at you."
            mom "What of it?"
            "> Mary’s mom’s eyes are full of anger and at the same time hurt. You feel beads of sweat forming on your neck as you feel the pressure. "
            "> Your resolve is cracking under the weight of her glare and aura." 
            "> You glance over to Mary, whose eyes are wide and full of tears. "
            "> Seeing Mary strengthens your resolve and you look back to her mom."
            menu: 
                "Ease into it":
                    m "Well..I think there’s a misunderstanding between you and Mary right now...You’re not really on the same page. "
                    mom "What are you saying? You think you know my daughter more than I know her? I’ve raised her and I know what’s best for her." 
                    m "I’m not saying that I know her more..I just mean.."
                    mom "Who do you think you are?"
                    m "{i}This isn’t going so well...{/i}"
                    menu:
                        "Talk about Mary's Dad":
                             m "I’m sure you remember your husband’s passion for cooking! It made him happy and it made Mary happy too!"
                             mom "Don’t act like you know everything. He’s gone now because of that passion. He’s gone so I can only look after Mary and her well-being now."
                             m "..."
                             mom "You might mean well, but please. You’re not helping anyone here. Bringing up past pain will not help Mary now. Just leave." 
                             "> You stand there for a moment and Mary’s look of disappointment and sadness is enough to tell you that you’ve failed."
                             "> You move your legs mechanically out of the kitchen and out of the house."
                             "> You've tried your best but it wasn’t enough." 
                             "> You probably won’t be able to spend as much time with Mary anymore.."
                             return
                             #jump bad ending
                        "Talk about Mary":
                            jump be_blunt
                "Be blunt":
                    jump be_blunt
                
            
label be_blunt:
    m " To be straightforward, Mary’s the president of the cooking club at school and she’s been cooking for a long time behind your back."
    "> Mary’s mom sharply turns to Mary in disbelief and Mary cowers even more."
    p "%(player_name)s!! I-It’s not what you think, mom…"
    m "It's exactly how it looks."
    mom "Mary..Why haven't you been listening to me? You know exactly why I forbid you to cook." 
    m "She does it because it’s her passion." 
    m "A passion that was fostered by your husband. She does it to honor him and ultimately, because it makes her happy. Is that really so bad?"
    "> Mary’s mom stares at you for a moment."
    mom "Do you think I don’t know what’s best for my own daughter?"
    m "Please, I’m not trying to undermine you or your ideals." 
    m "But I think it’d be great for both you and Mary if you would even just consider the idea of letting her cook as a hobby and potentially even going further as a career." 
    mom "She..she can’t. Or else she’ll end up just like her father." 
    "> Her eyes seem less hard now, and more sad."
    m "In some ways. She’ll definitely be happier. More passionate. I can see why you worry about her...I do too." 
    "> You look over at Mary again and your eyes lock. She smiles a little bit."
    m" But you should trust her to know her limits - I know I’ve come to." 
    m "She’s smart, she’s reasonable. she knows her abilities and her talents. Honestly, she’s great. Limiting her is putting on more stress than not. "
    "> Mary’s mom is silent. She then looks over to Mary."
    mom "Is..all of this true?"
    p "Yes, mom...I’ve always loved cooking and I haven't stopped even if dad has died." 
    p "I’m sorry..I never wanted you to find out like this.."
    mom "..."
    p "Please mom..This is what I really want to do. I know you loved dad because he was very passionate as well.."
    "> Mary’s mom looks away from the both you and Mary."
    mom "I didn’t mean to drive a wall between us. You really kept all of this a secret from me?" 
    p "I was too scared..I didn’t want to hurt you too. But this is who I am.."
    "> Mary’s mom turns around and embraces Mary."
    mom "I’m sorry." 
    "> It seems like she’s unable to say anything else as her voice starts wavering. Mary is crying too." 
    "> You decide that you shouldn’t intrude and you leave the room."
    "> ..."
    "> Time passes as you wait outside. You wonder if you could have said anything else, but it’s up to Mary now." 
    "> After a while, the door opens behind you and you turn to see Mary coming out."
    m "Hey. You okay?" 
    "> Mary nods and a huge smile breaks out on her face."
    p "She’s letting me continue to cook! Can you believe it?"
    p "We talked it over and she’s letting me have my shot at being a chef like my dad! She said I had to keep my grades up but that’s all fine."
    p "I’m so glad! It’s all thanks to you, %(player_name)s. You stood up for me." 
    m "I wanted to protect you." 
    "> Mary smiles even more and hugs you."
    p "I’m so thankful for you..thank you so much.."
    "> You give her a hug back and you both relish in each other’s happiness."
    jump mary_good_end


#Endings ================================================================================================================================================================================
label mary_good_end:
    "> The next day you run to the home-ec room, hoping to find your girlfriend."
    "> You open the door to find her making preparations for todays club meeting."
    p "Oh! You scared me. Why are you here so early?"
    m "Haha. I couldn't wait to see you."
    "> The two of you decide to keep each other company until the morning bell rings."
    "> ..."
    "> Days pass and your relationship with Mary continues to prosper."
    "> You enjoy the rest of your high school life together with your girlfriend."
    "> Congratulations %(player_name)s!"
    return #to end game
label mary_bad_end:
    "> The next day you check the home-ec room but there's no sign of Mary."
    "> It seems you weren't too successful in building your relationship..."
    "> ..."
    "> Days pass and you're unable to bring yourself to even see her. Eventually you give up all together."
    "> You spend the rest of your normal high school life single, working hard to secure your future career."
    "> Who knows? Maybe it'll be better after highshool...?"
    "> Better luck next time, %(player_name)s."
    return #to end game

#routine for raising stats
label raisestat:
    call randomquiz
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



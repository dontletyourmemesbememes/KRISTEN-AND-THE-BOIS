#Problems:
#Waiting during question lets you do a question again andf get additional stats
 
 
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
image bg karaoke_lobby = "Karaoke_lobby.png"
image bg karaoke = "Karaoke.png"
image bg music_room = "Music_room.png"
image bg office = "Office.png"
image bg outside_house = "Outside_house.png"
image bg restaurant = "Restaurant.png"
image bg player room = "Player_room.png"
image bg sidewalk = "Sidewalk.png"
image bg home = "Player_room.png"
image credits = "Credits.png"
#Mary images--------------------------------------------------------------------------------------
image mary intro = "MaryIntro.png"
image mary casual smile = "mary_casual_1.png"
image mary casual happy = "mary_casual_2.png"
image mary casual wonder = "mary_casual_3.png"
image mary casual grumpy = "mary_casual_4.png"
image mary casual confused = "mary_casual_5.png"
image mary casual straight = "mary_casual_6.png"
image mary casual laugh = "mary_casual_7.png"
image mary casual shy = "mary_casual_8.png"
image mary casual sigh = "mary_casual_9.png"
image mary casual pout = "mary_casual_10.png"
image mary casual sad = "mary_casual_11.png"
image mary casual flustered1 = "mary_casual_12.png"
image mary casual flustered2 = "mary_casual_13.png"
image mary casual shock = "mary_casual_14.png"
image mary cook smile = "mary_cook_1.png"
image mary cook happy = "mary_cook_2.png"
image mary cook wonder = "mary_cook_3.png"
image mary cook grumpy = "mary_cook_4.png"
image mary cook confused = "mary_cook_5.png"
image mary cook straight = "mary_cook_6.png"
image mary cook laugh = "mary_cook_7.png"
image mary cook shy = "mary_cook_8.png"
image mary cook sigh = "mary_cook_9.png"
image mary cook pout = "mary_cook_10.png"
image mary cook sad = "mary_cook_11.png"
image mary cook flustered1 = "mary_cook_12.png"
image mary cook flustered2 = "mary_cook_13.png"
image mary cook shock = "mary_cook_14.png"
image mary cook cry = "mary_cook_15.png"
image leapsahead = "LeapsAhead.png"
image hands = "HANDS.png"
image mary_kiss = "MaryKISSSSSS.png"
image mary_flour = "MaryFlour.png"
image mary grad = "Grad_mary.png"
#Catherine images---------------------------------------------------------------------------------
image cath casual 1 = "Cath1-1.png"
image cath casual 2 = "Cath1-2.png"
image cath casual 3 = "Cath1-3.png"
image cath casual 4 = "Cath1-4.png"
image cath casual 5 = "Cath1-5.png"
image cath casual 6 = "Cath1-6.png"
image cath casual 7 = "Cath2-1.png"
image cath casual 8 = "Cath2-2.png"
image cath casual 9 = "Cath2-3.png"
image cath casual 10 = "Cath2-4.png"
image cath casual 11 = "Cath2-4blush.png"
image cath casual 12 = "Cath2-5.png"
image cath casual 13 = "Cath2-5blush.png"
image cath casual 14 = "Cath3-1.png"
image cath casual 15 = "Cath3-1blush.png"
image cath casual 16 = "Cath3-2.png"
image cath casual 17 = "Cath3-2blush.png"
image cath casual 18 = "Cath3-3.png"
image cath casual 19 = "Cath3-4.png"
image cath dress 1 = "Cathdress1-1.png"
image cath dress 2 = "Cathdress1-2.png"
image cath dress 3 = "Cathdress1-3.png"
image cath dress 4 = "Cathdress1-3blush.png"
image cath dress 5 = "Cathdress1-4.png"
image cath dress 6 = "Cathdress1-4blush.png"
image cath dress 7 = "Cathdress1-1.png"
image cath dress 8 = "Cathdress2-1.png"
image cath dress 9 = "Cathdress2-1blush.png"
image cath dress 10 = "Cathdress2-2.png"
image cath dress 11 = "Cathdress2-2blush.png"
image cath dress 12 = "Cathdress2-3blush.png"
image cath dress 13 = "Cathdress2-4blush.png"
image cath back = "cathback.png"
image cath violin = "CathIntro.png"
image cath concert = "Concert.png"
image cath drawing = "Drawing.png"
image cath grad = "Grad_cath.png"
image cath talk1:
    "Cath3-1.png"
    pause(1.0)
    "Cath3-2.png"
    pause(1.0)
    repeat
 
#Extra images-------------------------------------------------------------------------------------
image principal 1 = "principal1.png"
image principal 2 = "principal2.png"
image principal 3 = "principal3.png"
image principal 4 = "principal4.png"
image principal 5 = "principal5.png"
image principal 6 = "principal6.png"
image principal 7 = "principal7.png"
image principal 8 = "principal8.png"
image principal 9 = "principal9.png"
image principal 10 = "principal1-4.png"
image principal 11 = "principal1-5.png"
image principal 12 = "principal1-6.png"
image principal 13 = "principal1-7.png"
image thought = "Thought.png"
image mom 1 = "Mom1-1.png"
image mom 2 = "Mom1-2.png"
image mom 3 = "Mom1-3.png"
image mom 4 = "Mom1-4.png"
image mom 5 = "Mom1-5.png"
image mom 6 = "Mom1-6.png"
image mom 7 = "Mom2-1.png"
image mom 8 = "Mom2-2.png"
image mom 9 = "Mom2-3.png"
image mom 10 = "Mom2-4.png"
image mom 11 = "Mom2-5.png"
image mom 12 = "Mom2-6.png"
 
 
 
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
        def add_question(self,desc,choices,answer):
            question = Question(desc,choices,answer)
            self.question_list.append(question)
            return
        def remove_question(self,index):
            self.question_list.pop(index)
            return

        def get_random_question(self):
            index = renpy.random.randint(0,len(self.question_list)-1)
            question = self.question_list[index]
            if len(self.question_list) > 1:
                self.remove_question(index)
            return question
 
 
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
           
        # Why is the name being passed here as the parameter...?
        # It literally does nothing.
        # Added default parameters so you can still call them without the name param.
        # Since it's probably too late at this point to change it back.
        def get_closeness(self,name=""):
            return self.closeness
           
        def add_affection(self,amount):
            self.affection += amount
 
        # same issue here
        def get_affection(self,name=""):
            return self.affection
 
        def set_name(self,name):
            self.name = name
       
        # and here
        def get_event(self,name=""):
            return self.event
           
        def add_event(self):
            self.event += 1
           
    def rng_roll(chance): #chance should be between [0,1]
        return chance > renpy.random.random()
 
    stats = Stats()
    girl1 = Girl("Mary")
    girl2 = Girl("Catherine")
 
    bio_qman = QuestionManager()
    gym_qman = QuestionManager()
    drama_qman = QuestionManager()
 
    bio_qman.add_question("The blood vessels that carry (usually oxygenated) blood away from the heart are called?",["Artery","Vein","Ventricle","Atrium"],0)
    bio_qman.add_question("What is the largest organ in the human body?",["Liver","Lung","Skin","Brain"],2)
    bio_qman.add_question("An example of a waste product of aerobic cellular respiration is:",["carbon monoxide","carbon dioxide","oxygen","methanol"],1)
    bio_qman.add_question("What is the basic unit of all living organisms found on Earth?",["The cell","The atom","Brick","DNA","Tissue","Fecal matter"],0)
    bio_qman.add_question("What describes the movement of molecules from a higher concentration to a lower concentration",["Diffusion","Osmosis","Diffration","Refraction"],0)
    bio_qman.add_question("Plants are typically green because they:",["reflect green light","absorb green light"],0)
    bio_qman.add_question("What is a difference between plant cells and animal cells?",["Presence of a cell wall","Presence of a membrane","Presence of Vacuoles","Presence of feet","There are no differences"],0)
    bio_qman.add_question("What is the study of plants called",["Botany","Mycology","Pathology","Zoology"],0)
    bio_qman.add_question("Which is NOT one of the four nucleobases used in DNA",["Uracil","Thymine","Guanine","Adenine","Cytosine"],0)
    bio_qman.add_question("What is found in the mitochondria?",["The golgi","The cristae","Endoplasmic Reticulum","The Nucleus"],1)
    bio_qman.add_question("When two bacteria exchange genetic information with each other through direct contact, cell to cell, what is the process called?",["Conjunction","Transformation","Euglena","Fuuuuusion Ha!"],0)
    bio_qman.add_question("What is the function of all enzymes?",["Partay","Growing","Facilitate reaction","Hair growth"],2)
    bio_qman.add_question("What is the family name of a cat?",["Lupus","Elephantitis","Patherus","Felidae"],3)
    bio_qman.add_question("What is the process in which plants use to make food?",["Cooking","Filtering","Photosynthesis","Photolysis"],2)
    bio_qman.add_question("What is the scientific name of a dog?",["Much Doge","Tetrapedius mammalian","Canis Familiaris","Equiarus"],2)
    bio_qman.add_question("Animals which eat both plants and animals are known as what?",["Omnitarian","Vegan","Sarcophyte","Omnivore"],3)
    bio_qman.add_question("Can frogs live in salt water?",["Yes","No","Maybe","Only if they're salt water frogs"],1)
    bio_qman.add_question("Lamarck's Theory of evolution is characterised by what concept?",["Survival of the fittest","Natural Selection","Dinosaurs","Heritability of acquired characteristics"],3)
    bio_qman.add_question("Darwin's theory of natural selection developed by observing what animal?",["Finches","Doges","Fish","Bananas"],0)
    bio_qman.add_question("How many feet does a snail have?",["1","2","4","Infinite"],0)
    bio_qman.add_question("What part of the retina allows for coloured vision?",["Rods","Cones","Lens","Mirror"],1)
    bio_qman.add_question("What part of the brain controls balance?",["Frontal Cortex","The wrinkly half","Temporal Lobe","Cerebellum"],3)
 
 
    drama_qman.add_question("How does Hamlet Sr. die in the play, 'Hamlet'?",["Poison","Obesity","Witches","A duel with Ferdinard Sr."],0)
    drama_qman.add_question("What is the name of the role of a person who writes the play?",["Playwright","Actor","Director","Player"],0)
    drama_qman.add_question("When you are on stage, to make sure your audience can understand, you must project your:",["Vision","Breath","Ideas","Voice"],3)
    drama_qman.add_question("In which Shakespeare play does this line appear: 'All the world's a stage and all the men and women merely players'",["Othello","Macbeth","Hamlet","Romeo and Juliet","As You Like It"],4)
    drama_qman.add_question("What are instructions for actors, directors and the stage crew?",["Stage Directions","Dialogue","Soliloquy","Metaphor"],0)
    drama_qman.add_question("What is conversation between characters?",["Small talk","Dialogue","Oxymoron","Monologue"],1)
    drama_qman.add_question("What are people watching a play called?",["Fan girls/boys","Plebs","Audience","4th wallers"],2)
    drama_qman.add_question("Ordinary spoken or written language is called:",["Imagery","Jargon","Poetry","Prose"],3)
    drama_qman.add_question("True or False: In Ancient Greek plays, there were NO women actresses.",["True","False","Unknown","Only when there were female roles"],0)
    drama_qman.add_question("Which of the following refers to talking to the audience?",["Dialogue","Aside","Monologue","Solo"],1)
    drama_qman.add_question("What does a character foil refer to?",["Antagonist","Protagonist","The opposite of the protagonist","The doppelganger of the protagonist"],2)
    drama_qman.add_question("Who is the king of the fairies in 'A Midsummer Night's Dream'?",["King Lear","Othello","Claudius","Oberon"],3)
    drama_qman.add_question("The imaginary wall between the audience and the actor is called:",["The fourth wall","The third wall","The second wall","The first wall"],0)
    drama_qman.add_question("Who tells Macbeth he can kill Duncan to become king?",["Lady Macbeth","The Ghost of Macbeth Sr.","Banquo","The 3 witches"],3)
 
 
    gym_qman.add_question("In a badminton game, how many points are required for a win?",["5","10","11","21","25"],3)
    gym_qman.add_question("What is Canada's national sport?",["Hockey","Lacrosse","Curling","Ice Skating"],1)
    gym_qman.add_question("What body part do you receive a penalty for using in soccer?",["Hands","Head","Feet","Ears"],0)
    gym_qman.add_question("In American football, how many points are rewarded for a touchdown?",["1","6","8","10"],1)
    gym_qman.add_question("Which is a form of exercise?",["Sitting","Laying","Walking","Whining"],2)
    gym_qman.add_question("What is the Olympic event that consists of throwing a metal ball from shoulder height?",["Basketball","Javelin","16th Centry War","Shot Put"],3)
    gym_qman.add_question("What is the average walking speed?",["5 Km/h","20 Km/h","1 Km/h","35 Km/h"],0)
    gym_qman.add_question("How many events are in a triathalon?",["3","4","7","6"],0)
    gym_qman.add_question("What is a Hat trick?",["3 goals by one player","A score made from the other side of the field","An accidental score","A fan running around the field with a hat, doing magic tricks"],0)
    gym_qman.add_question("What is the term when you are tied in tennis?",["Tied","Duck","Goose","Deuce"],3)
    gym_qman.add_question("What is the term when you have zero points in tennis?",["Loser","Zero","Pleb","Love"],3)
    gym_qman.add_question("One stroke less than par in golf is called:",["Not good enough","Eagle","Birdie","Bogey","Hole in one"],2)
    gym_qman.add_question("What sport is the FIFA World cup for?",["Football (soccer)","Tennis","Hockey","Quidditch"],0)
    gym_qman.add_question("Famous player involved in NBA and MLB, and is associated with a shoe brand?",["Michael Jackson","Jeremy Lin","Micheal Jordan","Shaquille O'Neil"],2)
    gym_qman.add_question("What is the most points you can get in a bowling game?",["300","1","2","500"],0)
    gym_qman.add_question("How do you end Quidditch?",["Knock over all of the opposing team","Say the name that cannot be said","Remove your nose","Catch the golden snitch"],3)
 
 
 
    def stats_overlay():
        ui.image("overlay.png")
        #ui.text(("Days Elapsed:"+str(stats.get_days())),size=24)
        ui.image("overlay.png")
        closeness = 0
        if stats.chosen_girl == 1:
            closeness = girl1.get_closeness()
        elif stats.chosen_girl == 2:
            closeness = girl2.get_closeness()
        else:
            closeness = 0
 
        #ui.text(("Closeness:"+str(closeness)),size=24,ypos=96)
        ui.text(("Strength:"+str(stats.get_stats("str"))),size=24)
        ui.text(("Intelligence:"+str(stats.get_stats("int"))),size=24,ypos=24)
        ui.text(("Charm:"+str(stats.get_stats("cha"))),size=24,ypos=48)
       
       
    config.overlay_functions.append(stats_overlay) #add overlay
 
 
# Declare characters used by this game.
 
define p = DynamicCharacter("unknown_name", color="#c8ffc8")
define m = DynamicCharacter("player_name")
define principal = Character("Principal", color="#c8ffc8")
define mom = Character("Mom", color="#c8ffc8")
define cookies_baked = False
#Mary variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
define girl1check1 = False
define girl1check2 = False
define girl1check3 = False
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
    play music "Background Music.mp3" fadein 1.0
    scene bg office
    with fade
 
    $ player_name = renpy.input("Most of the documents seem to be in order. Can I get you to sign your name below please?")
   
    $ unknown_name = "???"
    show principal 3 with fade
    principal "Alright %(player_name)s, I believe we're good to go now!"
   
    #show placeholder normal at left
    #with moveinbottom
    show principal 1
    principal "Allow me to officially welcome you to Gouglas Private Academy. This school consists of the brightest students from all over the city so congratulations for making it!"
    jump intro
 
    return
 
label intro:
   
    show principal 2
    principal "As this is an elite school, our curriculum is a tad different than other schools in the country."
    principal "Required classes will all be covered during your morning lessons, while {i}optional classes{/i} are held throughout the afternoon. Our most popular ones that we offer are {i}Drama, Biology, and Phys Ed{/i}."
    principal "In order to foster independence and individual growth in each of our students, we're extremely flexible in what classes you decide to attend each day."
    show principal 8
    principal "Keep in mind that each class will affect {i}how you grow as a person{/i}."
    show principal 2
    principal "Whoever you choose to be can impact any choices you make in the future so choose your classes wisely."
    # "But be choose wisely. Once you set your classes today, it'll be permanent for the rest of the year.
    show principal 4
    principal "Now, If you're ready, I can take you on a tour of the school and some of the club rooms. Do you want me to repeat anything?"
    menu:
   
        "I think I'm good.":
            principal "Please follow me, %(player_name)s."
            jump school_tour
        "Can you go over how this works again?":
            principal "Certainly."
            jump intro
   
label school_tour:
   
    scene bg hallway with fade
    show principal 5 with dissolve
    show thought with dissolve
    "> The principal shows you through most of the building and classrooms. Nothing about this school seems particularily unusual."
    show principal 4
    "> Nothing the principal is saying seems particularily important..."
   
    principal "...and here we have the {b}club room building{/b}..."
   
    "> Oh. Time to pay attention."
    hide thought with dissolve
   # scene bg home_ec_room with fade
    show principal 5
    #show image of economics room
   
    principal "This is the home economics room. Students come here to learn essential life skills like cooking."
    "> You notice someone in the room. Let's take a look!"
    #ide principal with dissolve
    scene bg home_ec_room with fade
    #show image of Mary cooking
 
    #replace with special scene of mary
    show mary intro with fade
    "> You look through the door and see a girl piling ingredients on one of the counters."
    show thought with dissolve
    m "{i}It looks like she's preparing to cook something.{/i}"
    hide thought with dissolve
    principal "Ahem!"
    # show principal
    hide mary with dissolve
    scene bg hallway with fade
    show principal 7
    principal "Keep in mind that the most sophisticated dishes require a certain amount of stamina as well as some creative style."
    show principal 9
    principal "Moving on..."
    scene bg hallway with fade
 
    #fade out
    show principal 5
    #show image of music room
    principal "This is the music room. If you ever want to develop your musical capabilities then this is the perfect spot to practice!"
    "> You hear someone playing inside. Let's take a peek!"
    #show Catherine playing violin
    scene bg music_room with fade
    show cath violin with fade
    "> Through the door you see a girl standing in the middle of the room playing a violin."
    show thought with dissolve
    m"{i}She looks as if she's performing for a royal audience.{/i}"
    hide thought with dissolve
    principal "Continuing on..."
    hide cath with dissolve
    show principal 7 with dissolve
    principal "Keep in mind that music is an expression of your personality, but requires a lot of thought process as well."
    show principal 4
    principal "Shall we continue with the tour?"
   
    #fade out
 
   
    #show image of the gym
    #JUST THE TWO CLUBS FOR NOW
    #principal "This is our fitness centre. We have the newest equipment for any kind of workout. "
    #principal "Remember to keep fit during the year, because it will help you psychologically when you are doing homework and are studying for your midterms."
    #show other girl
    scene bg hallway with fade
    show principal 5 with dissolve
    principal "Moving on to the next club..."
    #fade out
 
    show thought with dissolve
    scene bg hallway
    with fade
    "> The other club rooms didn't seem to interest you at all..."
    hide thought with dissolve
    #go to general image, office or something
    scene bg office with fade
    show principal 2 with dissolve
    principal "Well those are just examples of the many facilities this school provides."# Make use of your time and be sure to work hard on your academics."
    show principal 1
    principal "So... Did you enjoy checking out some of the female students instead of paying attention to what I was saying?"
    principal "Haha, don't worry! You're a young man, so I understand."
    show principal 3
    principal "Remember that we are an elite school where studies are valued so we restrict students to joining only one club."
    show principal 7
    principal "Keep in mind that your social life and extra curriculars are crucial for a healthy high school experience too."
    show principal 2
    principal "Now then, I think I've said enough."
    show principal 1
    principal "Best wishes to you, %(player_name)s."
   
    $ stats.reset_classes()
    scene bg hallway with fade
    jump make_schedule
 
label make_schedule:
   
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
   
    scene bg player room with fade
    "> Your room."
    #fade to show end of day
    "{i}I'm so tired... I think I'll go to bed early today.{/i}"
    scene bg hallway with fade
    "> Next morning."
   
    m "Time to go to class."
    scene bg classroom with fade
    "> You somehow manage to stay awake through the intense morning lessons."
    scene bg hallway with fade
    m "I'm finally done the morning lessons; I was ready to pass out at any moment. So which classes should I take this afternoon?"
 
    $ stats.reset_classes()
    jump make_schedule
 #Classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
label gym:
    $ stats.pick_classes("Gym (+1 Strength)")
    if len(stats.get_picked_classes()) < stats.max_classes:
        m "Guess I'll choose Gym for one choice, I still need to pick another."
    #$ stats.pick_classes("Gym")
    scene bg classroom with fade
    $ question = gym_qman.get_random_question()
    $ desc = question.get_description()
    "Question: %(desc)s"
    $ choices = question.get_menu_choices()
    $ result = renpy.display_menu(choices)
    if result == True:
        $ stats.add_stats("str", 1)
        "> You answered the question correctly."
        "> Your strength has increased!"
    else:
        "> Incorrect."
        "> No stats were raised."
 
    return
   
label drama:
    $ stats.pick_classes("Drama (+1 Charm)")
    if len(stats.get_picked_classes()) < stats.max_classes:
        m "Guess I'll choose Drama for one choice, I still need to pick another."
    #$ stats.pick_classes("Drama")
    scene bg classroom with fade
    $ question = drama_qman.get_random_question()
    $ desc = question.get_description()
    "Question: %(desc)s"
    $ choices = question.get_menu_choices()
    $ result = renpy.display_menu(choices)
    if result == True:
        $ stats.add_stats("cha", 1)
        "> You answered the question correctly."
        "> Your charm has increased!"
    else:
        "> Incorrect."
        "> No stats were raised."
 
    return
   
label biology:
   
    $ stats.pick_classes("Biology (+1 Intelligence)")
    if len(stats.get_picked_classes()) < stats.max_classes:
        m "Guess I'll choose Biology for one choice, I still need to pick another."
    #$ stats.pick_classes("Biology")
    scene bg classroom with fade
    $ question = bio_qman.get_random_question()
    $ desc = question.get_description()
    "Question: %(desc)s"
    $ choices = question.get_menu_choices()
    $ result = renpy.display_menu(choices)
    if result == True:
        $ stats.add_stats("int", 1)
        "> You answered the question correctly."
        "> Your intelligence has increased."
    else:
        "> Incorrect."
        "> No stats were raised."
 
    return
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
label extracurricular:
    scene bg hallway with fade
    m "So this is what an elite school is like? Classes seem ridiculously hard. Maybe I should check out those extracurricular activities that the principal mentioned."
    "> You recall that you can only join {b}one{/b} club. Which one do you choose?"
   
    $ chosen_girl = stats.get_chosen_girl()
   
    if chosen_girl == 0:
       
        menu:
            "Home Economics Room":
                m "I guess I'll go check out the home-ec room."
                jump home_ec_room
            "Music Room":
                m "I heard there was a music room. I should go check it out."
                jump music_room
 
    elif chosen_girl == 1: # Mary is chosen
       
        jump home_ec_day_2
       
    elif chosen_girl == 2: # music girl chosen
       
        jump music_day_2
 
#-----------------------------START OF MUSIC GIRL---------------------------------------------#
 
label music_room:
    stop music fadeout 1.0
   
    # TODO play violin music
    play music "violin.mp3" fadein 1.0
    scene bg hallway
    with fade
   
    "> As you get closer to the music room, you notice the door cracked open an inch. As you approach, you hear music that cuts through the opening."
    # fade to show entering room
    scene bg music_room
    with fade
    # TODO SHOW VIOLIN
    show cath violin with fade
   
    "> Upon entering, you find a girl drawing her bow flawlessly across the strings. She faces the opposite direction, displaying her hair that follows the dynamics of her playing."
    "> You’re compelled to sit down at the piano bench as your eyes and ears perked up to witness her welcoming and mellow style."
    "> She doesn't notice you as you sit down behind her."
    menu:
        "> Get her attention.":
            hide cath violin with fade
            $ girl2.add_closeness(-1)
            show cath casual 1 with dissolve
            m "Hi!"
            stop music fadeout 1.0
            "> Her enrapturing music screeches to a halt. Before you can say anything else, she spins around quickly with a look of anger on her face."
            show cath casual 2
            p "How. Dare. You."
        "> Wait.":    
            "> She seems so enveloped in her music that you don’t want to interrupt her."
            "> The song grows in depth as the notes create an atmosphere, sustained in emotion. Her upper body sways intimately with the music while the hairs on the back of your neck rise gradually."
            "> You find yourself enveloped by her music."
            m "{i}Wow... she's pretty amazing. I need to know this girl's name.{/i}"
            "> Her playing approaches the end. You feel anxiety rising up as you stand to attempt talking to her."
            hide cath violin with fade
            stop music fadeout 1.0
            show cath back with dissolve
            m "{i}Now's my chance to talk to her!{/i}"
            m "Hey, I just heard you playing and you were pretty awesome!"
            "> She looks back to be slightly surprised, not knowing you were there. Her expression instantly reads 'who the hell are you?'"
            show cath casual 1 with dissolve
   
    show cath casual 12
    p "I thought I closed the door, how did you get in?"
    show cath casual 10
    m "Oh no, it was opened. Sorry I didn't know know you wanted to be alone."
    show cath casual 2
    p "I'm practicing, so if you don't mind, I have a concert to prepare for. If you could leave that would be really great."
    show cath casual 1
    "> You think that she is being sarcastic."
    show cath back 
    "> Immediately she gets back to playing, but this time her playing loses its warmth and immediately has an air of superiority."
    play music "violin.mp3" fadein 1.0
   
    m "I never caught your name, by the way."
    "> The violin lets out a shriek and she turns to you in frustration."
    hide cath with dissolve
    stop music fadeout 1.0
    show cath casual 12 with dissolve
    p "Did you not hear me earlier?"
    show cath casual 10
    m "I did, but I don't want to leave."
    show cath casual 3
    "> Looking frustrated and agitated, she clenches the neck of the violin and stick."
    show cath casual 12
    p "Ugh! Who do you think you are anyways!?"
    show cath casual 10
    m "I'm %(player_name)s. Your playing was pretty inspiring to listen to. What's your name?"
    show cath casual 1
    "> She holds a frown."
    show cath casual 2
    p "Catherine... I suppose it’s not a huge inconvenience if you listen, just try to keep quiet and don’t do anything to distract me or I am going to kick you out."
    $ unknown_name = "Catherine"
    show thought with dissolve
    m "{i}This girl's scary.{/i}"
   
    # TODO SHOW VIOLIN
    hide thougt with dissolve
    show cath back with fade
   
    play music "violin.mp3" fadein 1.0
    "> She moves to her music stand again raising her bow into position. This time she continues to play, but still not as welcoming and warm as the first time."
    "> You start to get into the music as you lean back and tap your feet."
    hide cath with fade
    show thought with dissolve
    "> As you notice the dust on your elbows, you realize you have been sitting beside a piano."
    m "{i}Oh man, this piano’s pretty dusty. I haven’t touched one of these in a couple years. Now let’s see what we have here...{/i}"
    "> You lift the key covering."
    $ int_check = stats.get_stats("int")
    menu:
        "Play along with her":
            hide thought with dissolve
            jump play_with_her
       
        "Just sit and listen to her play the violin":
            "> You stay seated and simply listen to her playing."
            menu:
                "Play with her":
                    hide thought with dissolve
                    jump play_with_her
               
                "Attempt to talk to Catherine as shes playing":
                    hide thought with dissolve
                    m "How did you get into playing violin?"
                    "> She plays louder and more aggressively."
                    $ girl2.add_closeness(-1)
                    menu:
                        "Play with her":
                            jump play_with_her
                           
        "Attempt to talk to Catherine as shes playing":
            hide thought with dissolve
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
    stop music fadeout 1.0
    if int_check >= 1:
        $ girl2.add_closeness(1)
        play music "violinpiano.mp3" fadein 1.0
        "> You pick up where there's an opening, and accompany her. The first few moments feel sluggish and your hands feel clumsy, but after a few bars you're able to familiarize yourself. You peek over your shoulder to notice that Catherine's posture is rigid; she doesn't seem like she's used to someone playing with her. Her playing begins to become harsher and her facial expression suddenly becomes unimpressed."
        m "{i}Hmm... She hasn't stopped playing yet... I'll just keep going to see where this takes me.{/i}"
        "> You listen to her carefully and do your best to follow her, trying to avoid taking over or not supporting her enough. You remember the feeling from before: the chill in your spine, hair upright, and heightened senses."
        "> You can’t see her now, but you’d like to imagine that she is also feeling the same way you do."
        "> You listen carefully and end the song."
        stop music fadeout 1.0
        show thought with dissolve
        m "{i}I think my finish was coordinated with her pretty well. Granted not perfect, but pretty good I think.{/i}"
        hide thought with dissolve
        show cath casual 2 with dissolve
        p "That was terrible."
        show cath casual 3
        "> Catherine crosses her arms again and turns her back on you with a puff of air."
        show cath casual 5
        p "But..not bad for an impromptu."
        "> You can’t see the expression on her face, but her response makes you smile."
        play music "Background Music.mp3" fadein 1.0
        show cath casual 4
        menu:
            "Lightly joke":
                m "You're amazing at the violin. But yeah, thanks, Cathy!"
                $ girl2.add_closeness(-1)
                show cath casual 2
                p "That's not my name, I hate being called Cathy."
                show cath casual 1
                m "Oh, I'll keep that in mind, sorry. It's nice to meet you Catherine!"
            "Be humble":
                $girl2.add_closeness(1)
                m "Thanks Catherine, but I'm still pretty rusty. I haven't played since junior high. Your playing earlier inspired me!"
                show cath casual 14
                "> Catherine looks flustered, but is trying to keep an exaggerated, mature composure." # guess image here instead of description
                p "..."
                show cath casual 16
                p "Of course! I'm training to be the best you know. It's nice to meet you too I guess."
       
        m "Well, I think i might take another shot at playing the piano."
        show cath casual 12
        p "What!? What do you mean?"
        show cath casual 10
        m "I’ll be around the music room more often; I like listening to you play and the way you played the violin has inspired me to get back into playing the piano."
        show cath casual 12
        p "Who said you could be in here?"
        show cath casual 10
        m "Would you be opposed? I need to practice a little more and you could tell me how I'm doing."
        show cath casual 2
        p "I don’t have time to deal with an amateur like you. Ugh... but I guess it’s sort of useful having an accompanist. JUST FOR PRACTICE. Come by tomorrow; don’t be late or else I’ll kick you out."  
        hide cath with dissolve
        # end day
       
    else:
        play music "Piano Fail.mp3" fadein 1.0
        "> You try to think of what to play, but the keys starts to look more and more like a puzzle. You play the keys but it just makes a loud obstruction to The girl's music."
        "> She stops midway, pointing the violin bow at you."
        stop music fadeout 1.0
        show cath casual 10 with dissolve
        play music "Background Music.mp3" fadein 1.0
        show cath casual 12
        p "What did I just say? Why are you even touching the piano, if you don’t have the capacity to play it?"
        show thought with dissolve
        show cath casual 10
        m "{i}Oh crap.{/i}"
        hide thought with dissolve
        m "W-well I haven’t played since junior high, so I’m rusty, I mean just a little rusty or maybe a lot depending on who’s judging that is. I’m usually better I just need to brush up. Actually, I think I might take another shot at playing the piano if you’ll give me a chance."
        show cath casual 2
        p "What? what do you mean?"
        show cath casual 1
        m "I want to be around the music room more often, I like listening to you play and the way you played the violin has inspired me to get back into playing the piano."
        show cath casual 2
        p "You're terrible. Why should I even give you another chance."
        "> Catherine's eyes look hard and unforgiving."
        m "Please give me another chance! I won't disappoint you. I'll leave you alone if I do not meet your standards next time!"
        "> Catherine's eyes suddenly soften but turns cold again so fast that you're not sure if you were seeing right."
        show cath casual 1
        p "I..Fine. I'll give you a shot. Be here tomorrow and don't be late, or else."
        "> She turns her back to you again. You're not sure what else to say and you take this as your cue to leave. You get up and just about as you exit the room, you hear Catherine say something else."
        show cath casual 2
        p "If you're really serious about this, you don't want to waste your chance or you'll regret it. Believe me."
        "> She immediately lifts her bow again and starts up playing again, ignoring you. You leave."
        hide cath with dissolve
   
    # show image of bedroom at night?
    scene bg home
    with fade
    "> Your room."
    m "That was a long day, time to hit the sack."
    $ stats.increment_days()
    scene bg hallway with fade  
    "> Next morning."
    m "Another day at school..."
    scene bg classroom with fade
    "> Morning classes seem to be going well."
    scene bg hallway with fade
    "> Afternoon."
    m "Time for afternoon classes. What should I take today?"
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
    elif day > 5:
        # too long trigger failure event
        jump girl2_failure
    elif closeness <= -3:
        # lost too much closeness
        jump girl2_failure
    elif day <= 5 and closeness >= 4 and event_num == 0:
        # trigger event 1 as day <= 5 and closess >= 4
        # set the event value to 1
        $ girl2.add_event()
        jump music_event_1
   
label music_event_check_2:
   
    $ closeness = girl2.get_closeness("Catherine")
    $ event_num = girl2.get_event("Catherine")
    if closeness >= 6 and event_num == 1:
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
    show cath casual 5:
        xalign 0.8
        linear 1.0 xalign 0.5
    p "Hey, you actually came. I hope you are prepared."
    show cath casual 4
    m "I think so! I practiced all of last night!"
    $ str_check = stats.get_stats("str")
    $ int_check = stats.get_stats("int")
    $ cha_check = stats.get_stats("cha")
    hide cath with dissolve
 
    stop music fadeout 1.0
    "> What will you play today?"
    menu:
        "Classical (no reqs)":
            play music "Classical.mp3" fadein 1.0
            "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
            stop music fadeout 1.0
            play music "Background Music.mp3" fadein 1.0
            show cath casual 4 with dissolve
            show cath casual 5
            p "You have redeemed yourself a little bit. You can come back to the music room if you want. Just don't get in my way."
            $ girl2.add_closeness(1)
           
        "Rock (Strength 1, Charm 2)":
            p "Rock today? okay I'll give it a try."
            if str_check >= 1 and cha_check >=2:
                play music "rock.mp3" fadein 1.0
                "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
                stop music fadeout 1.0
                play music "Background Music.mp3" fadein 1.0
                show cath casual 5 with dissolve
                p "That went better than I thought." # she coughs
                show cath casual 2
                p "I meant for you obviously, I knew that I would be great. That was interesting though. Maybe we should experiment like this more."
                $ girl2.add_closeness(2)
            else:
                play music "Piano Fail.mp3" fadein 1.0
                "> As you begin to play for the first few bars, you are able to stay on beat with Catherine, However, as the song intensifies, you stress out and begin to play fast and louder. The sounds created by piano overpowers the violin and there is dissonance in the music being played. Despite this, Catherine and  you imagine to finish the piece."
                stop music fadeout 1.0
                play music "Background Music.mp3" fadein 1.0
                show cath casual 12 with dissolve
                p "That was terrible. The piano is suppose to accompany the violin not the other way around... But I guess this is a huge improvement from yesterday. I guess I will let you continue coming to the music room because you are dedicated to improve and you kind of have potential.."
                $ girl2.add_closeness(-2)
       
        "Jazz (Charm 1, Intelligence 2)":
            show cath casual 5 with dissolve
            p "OH! I LOVE JAZZ!"
            hide cath with dissolve
            if cha_check >= 1 and int_check >= 2:
                play music "Jazz.mp3" fadein 1.0
                "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
                stop music fadeout 1.0
                play music "Background Music.mp3" fadein 1.0
                show cath casual 5 with dissolve
                p "You have redeemed yourself a little bit. You can come back to the music room if you want. Just don't get in my way."
            else:
                play music "Piano Fail.mp3" fadein 1.0
                "> As you begin to play for the first few bars, you are able to stay on beat with Catherine, However, as the song intensifies, you stress out and begin to play fast and louder. The sounds created by piano overpowers the violin and there is dissonance in the music being played. Despite this, Catherine and  you imagine to finish the piece."
                stop music fadeout 1.0
                play music "Background Music.mp3" fadein 1.0
                show cath casual 1 with dissolve
                p "That was terrible. The piano is suppose to accompany the violin not the other way around... You think you've got skill? That's laughable at the state you're at right now. I pity you too much to leave you like this so come back if you want and I'll get you into at least a DECENT level."
                $ girl2.add_closeness(-2)
               
    hide cath with dissolve
    "> After a while of practicing, the two of you decide to call it a day."
    scene bg home
    with fade
    "> Your room."
    m "That was a long day, time to hit the sack."
    $ stats.increment_days()
    scene bg hallway with fade  
    "> Next morning."
    m "Another day at school..."
    scene bg classroom with fade
    "> You feel morning classes are getting easier."
    scene bg hallway with fade
    "> Afternoon."
    m "Time for afternoon classes. What should I take today?"
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
    show cath casual 5:
        xalign 0.8
        linear 1.0 xalign 0.5
    p "Hey, you actually came. I hope you are prepared."
    show cath casual 4
    m "I think so! I practiced all of last night!"
    $ str_check = stats.get_stats("str")
    $ int_check = stats.get_stats("int")
    $ cha_check = stats.get_stats("cha")
    hide cath with dissolve
 
    "> What will you play today?"
    $ str_check = stats.get_stats("str")
    $ int_check = stats.get_stats("int")
    $ cha_check = stats.get_stats("cha")
    stop music fadeout 1.0
   
    menu:
        "Classical (no reqs)":
            play music "Classical.mp3" fadein 1.0
            "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
            stop music fadeout 1.0
            play music "Background Music.mp3" fadein 1.0
            show cath casual 4 with dissolve
            show cath casual 5
            p "You have redeemed yourself a little bit. You can come back to the music room if you want. Just don't get in my way."
            $ girl2.add_closeness(1)
 
           
        "Folk (Strength 2, Charm 2)":
            show cath casual 2 with dissolve
            p "Really? Okay, I'm not very used to folk, but if you want."
            hide cath with dissolve
            if str_check >= 2 and cha_check >=2:
                "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
                stop music fadeout 1.0
                play music "Background Music.mp3" fadein 1.0
                show cath casual 5 with dissolve
                p "You have redeemed yourself a little bit. You can come back to the music room if you want. Just don't get in my way."
                $ girl2.add_closeness(2)
            else:
                play music "Piano Fail.mp3" fadein 1.0
                "> As you begin to play for the first few bars, you are able to stay on beat with Catherine, However, as the song intensifies, you stress out and begin to play fast and louder. The sounds created by piano overpowers the violin and there is dissonance in the music being played. Despite this, Catherine and  you imagine to finish the piece."
                stop music fadeout 1.0
                play music "Background Music.mp3" fadein 1.0
                show cath casual 1
                p "That was terrible. The piano is suppose to accompany the violin not the other way around... But I guess this is a huge improvement from yesterday. I guess I will let you continue coming to the music room because you are dedicated to improve and you kind of have potential.."
                $ girl2.add_closeness(-2)
       
        "Blues (Charm 2, Intelligence 2)":
            show cath casual 3 with dissolve
            p "Alright, if you want."
            hide cath with dissolve
            if cha_check >= 2 and int_check >= 2:
                play music "Blues.mp3" fadein 1.0
                "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
                stop music fadeout 1.0
                play music "Background Music.mp3" fadein 1.0
                show cath casual 5 with dissolve
                p "You have redeemed yourself a little bit. You can come back to the music room if you want. Just don't get in my way."
                $ girl2.add_closeness(2)
            else:
                play music "Piano Fail.mp3" fadein 1.0
                "> As you begin to play for the first few bars, you are able to stay on beat with Catherine, However, as the song intensifies, you stress out and begin to play fast and louder. The sounds created by piano overpowers the violin and there is dissonance in the music being played. Despite this, Catherine and  you imagine to finish the piece."
                stop music fadeout 1.0
                play music "Background Music.mp3" fadein 1.0
                show cath casual 1 with dissolve
                p "That was terrible. The piano is suppose to accompany the violin not the other way around... But I guess this is a huge improvement from yesterday. I guess I will let you continue coming to the music room because you are dedicated to improve and you kind of have potential.."
                $ girl2.add_closeness(-2)
   
    hide cath with dissolve
    "> After a while of practicing, the two of you decide to call it a day."
    scene bg home
    with fade            
    "> Your room."
    m "That was a long day, time to hit the sack."
    $ stats.increment_days()
    scene bg hallway with fade  
    "> Next morning."
    m "Another day at school..."
    scene bg classroom with fade
    "> Morning classes are the same as usual."
    scene bg hallway with fade
    "> Afternoon."
    m "Time for afternoon classes. What should I take today?"
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
    show cath casual 5:
        xalign 0.8
        linear 1.0 xalign 0.5
    p "Hey, you actually came. I hope you are prepared."
    show cath casual 4
    m "I think so! I practiced all of last night!"
    $ str_check = stats.get_stats("str")
    $ int_check = stats.get_stats("int")
    $ cha_check = stats.get_stats("cha")
    hide cath with dissolve
 
    stop music fadeout 1.0
    "> What will you play today?"
    $ str_check = stats.get_stats("str")
    $ int_check = stats.get_stats("int")
    $ cha_check = stats.get_stats("cha")
   
    menu:
        "Classical (no reqs)":
            play music "Classical.mp3" fadein 1.0
            "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
            stop music fadeout 1.0
            play music "Background Music.mp3" fadein 1.0
            show cath casual 4 with dissolve
            show cath casual 5
            p "You have redeemed yourself a little bit. You can come back to the music room if you want. Just don't get in my way."
            $ girl2.add_closeness(1)
 
           
        "Latin (Strength 2, Charm 3)":
            show cath casual 5 with dissolve
            p "Very, very interesting."
            show cath casual 3
            p "..I don't know how to start... ummm... here goes nothing."
            hide cath with dissolve
            if str_check >= 2 and cha_check >=3:
                play music "Latin.mp3" fadein 1.0
                "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
                stop music fadeout 1.0
                play music "Background Music.mp3" fadein 1.0
                show cath casual 5 with dissolve
                p "Wow. I am impressed. Even though there were some errors, that was a huge improvement from yesterday. You have redeemed yourself. You are free to come back anytime you want and I don't mind playing with you again... It was kind of fun."
                $ girl2.add_closeness(2)
            else:
                play music "Piano Fail.mp3" fadein 1.0
                "> As you begin to play for the first few bars, you are able to stay on beat with Catherine, However, as the song intensifies, you stress out and begin to play fast and louder. The sounds created by piano overpowers the violin and there is dissonance in the music being played. Despite this, Catherine and  you imagine to finish the piece."
                stop music fadeout 1.0
                play music "Background Music.mp3" fadein 1.0
                show cath casual 1 with dissolve
                p "That was terrible. The piano is suppose to accompany the violin not the other way around... But I guess this is a huge improvement from yesterday. I guess I will let you continue coming to the music room because you are dedicated to improve and you kind of have potential.."
                $ girl2.add_closeness(-2)
       
        "J-pop (Charm 2, Intelligence 3)":
            show cath casual 5 with dissolve
            p "Oh great!"
            show cath casual 8
            p "I have this song from a dating sim game I wanted to play!"
            hide cath with dissolve
            if cha_check >= 2 and int_check >= 3:
                play music "Jpop.mp3" fadein 1.0
                "> It is like Catherine and you have performed before. You accidently play the wrong keys here and there, but you are able to stay on beat and made sure that the piano does not overpower the violin."
                stop music fadeout 1.0
                play music "Background Music.mp3" fadein 1.0
                show cath casual 5 with dissolve
                p "Wow. I am impressed. Even though there were some errors, that was a huge improvement from yesterday. You have redeemed yourself. You are free to come back anytime you want and I don't mind playing with you again... It was kind of fun."
                $ girl2.add_closeness(2)
            else:
                play music "Piano Fail.mp3" fadein 1.0
                "> As you begin to play for the first few bars, you are able to stay on beat with Catherine, However, as the song intensifies, you stress out and begin to play fast and louder. The sounds created by piano overpowers the violin and there is dissonance in the music being played. Despite this, Catherine and  you imagine to finish the piece."
                stop music fadeout 1.0
                play music "Background Music.mp3" fadein 1.0
                show cath casual 12 with dissolve
                p "That was terrible. The piano is suppose to accompany the violin not the other way around... But I guess this is a huge improvement from yesterday. I guess I will let you continue coming to the music room because you are dedicated to improve and you kind of have potential.."
                $ girl2.add_closeness(-2)
   
    hide cath with dissolve
    "> After a while of practicing, the two of you decide to call it a day."
    scene bg home
    with fade
    "> Your room."
    m "That was a long day, time to hit the sack."
    $ stats.increment_days()
    scene bg hallway with fade  
    "> Next morning."
    m "Another day at school..."
    scene bg classroom with fade
    "> You feel that you've gotten used to the school system."
    "> ..."
    "> You start to wonder about how Catherine is doing."
    scene bg hallway with fade
    "> Afternoon."
    m "Time for afternoon classes. What should I take today?"
    $ stats.reset_classes()
    call make_schedule
    call music_event_check_1
    call music_event_check_2
    jump girl2_failure
   
label music_event_1:
    # triggered from closeness
    scene bg music_room
    with fade
    $ day = stats.get_days()
    "> After school."
    show cath casual 14 with dissolve
    "> You enter the music room quietly; you see Catherine on the floor curled up in a kneeling position. Sprawled around her are vibrantly coloured posters and unopened markers."
    menu:
        "Hey Catherine... should I come by another time? You look busy right now..":
            show cath casual 16
            p "I am busy at the moment. Leave me alone."
            show cath casual 14
            $ girl2.add_affection(-1)
            "> You decide to leave her alone."
            hide cath with dissolve
            $ girl2_event1_asked1 = True
            if day == 3:
                # show home image
                scene bg home
                with fade
                "> Your room."
                m "That was a long day, time to hit the sack."
                scene bg hallway with fade
                "> Next morning."
                m "Another day at school..."
                scene bg classroom with fade
                "> Morning classes are the same as usual."
                scene bg hallway with fade
                "> Afternoon."
                m "Time for afternoon classes. What should I take today?"
                $ stats.reset_classes()
                call make_schedule
                jump music_day_3
            elif day == 4:
                # show home image
                scene bg home
                with fade
                "> Your room."
                m "That was a long day, time to hit the sack."
                scene bg hallway with fade
                "> Next morning."
                m "Another day at school..."
                scene bg classroom with fade
                "> Morning classes are the same as usual."
                scene bg hallway with fade
                "> Afternoon."
                m "Time for afternoon classes. What should I take today?"
                $ stats.reset_classes()
                call make_schedule
                jump music_day_4
           
        "Don't say anything yet":
            "> You decide to watch her and see what she's doing. You notice her tugging on her hair occasionally and letting out fits of frustration."
            play sound "Cell Phone Ring.mp3"
            "> ring ring ring"
            show cath casual 16
            p "Sigh..."
            show cath talk1 with dissolve
            stop sound
            p "Hi Mom."
            p "... I'm at school still making posters for the concert."
            p "... No, I don't think I'll be home in time for dinner."
            p "... I know, I still need to practice, don't worry I'll be fine."
            "> Catherine's tone sounds a little frustrated at this point."
            p "... Don't worry about it-- I said I'll be fine!"
            p "... I'm sorry for lashing out, I am just frustrated right now."
            p "... You too, bye..."
            show cath casual 14
            show thought with dissolve
            m "{i}I wonder why she sounded so angry at the end of her conversation.{/i}"
            hide thought with dissolve
            "> You walk closer to her without her noticing and upon closer inspection; notice that she’s making posters for some sort of concert."
            m "Hey Catherine, what are all these for? Do you need help with something?"
            show cath casual 16
            p "Oh! Hi %(player_name)s."
            show cath casual 15
            "> She seems embarrassed that you're seeing her like this."
            show cath casual 17
            p "I'm trying to make posters for this concert; I need to promote it. No need for help, I'm perfectly capable of doing this myself."
            show cath casual 15
            m "Of course, of course! If I help you now though we'll have time to play some music. I've been looking forward to it all day."
            show cath casual 17
            p "Hmmm...Fine! Do whatever you want."
            hide cath with fade
            show cath drawing with fade
            "> She still seems embarrassed for accepting your help, but at the same time, satisfied."
            "> You end up kneeling beside her. As you sit she retracts a couple inches away from where you're sitting."
            show thought with dissolve
            m "{i}She doesn’t seem that comfortable with me. Maybe I should try to make some conversation.{/i}"
            hide thought with dissolve
            hide cath with dissolve          
            menu:
                "What is the concert for?":
                    $ girl2.add_affection(1)
                    show cath casual 8 with dissolve
                    p "This is my opportunity to be the greatest violinist of our time."
                    show cath casual 7
                    m "What...?"
                    show cath casual 8
                    p "A representative from the most prestigious music schools in the UK was invited to view my performance. Basically, I'm being evaluated before actually going there to do my audition for the school."
                    show cath casual 7
                    m "Uh huh... congrats, Cathy!"
                    show cath casual 13
                    p "Idiot. Don't call me that."
                    show cath casual 11
                    m "hahahahaha!"
                    "> She furiously starts sketching her posters."
                    menu:
                        "What do you need me to do?":
                            jump music_event_1_part_2
                   
                "What do you need me to do?":
                    jump music_event_1_part_2
       
label music_event_1_part_2:
   
    show cath casual 2
    p "Can you just sketch details, in pencil?"
    show cath casual 1
    m "Don't you want me to do more than that?"
    show cath casual 2
    p "No. I can't have any clumsy mistakes."
    show cath casual 1
    "> You look at the posters in front of her."
    m "But you didn't even colour in the lines."
    show cath casual 15
    "> Catherine is flustered."
    show cath casual 17
    p "N-no! That's for visual effect! I guess it's hard to appreciate for an uncultured eye."
    show cath casual 15
    m "That is debatable."
    show cath casual 13
    p "Just get to work!"
    show cath casual 11
    hide cath with fade
   
    "> You work for some time, not saying anything to each other."
    "> You look at your clock and notice that the sun is starting to set."
    "> You look towards the window and you see the sunlight give a warm colouring to the surroundings. The chalk dust in the air highlights the sun rays giving the room a calm atmosphere."
    "> Your eyes wander to Catherine in the middle room and under the sun rays. She is putting on the finishing touches on the posters."
    "> She looks like she's in a spotlight. She looks so natural in it, like she was born to be in the spotlight. Light passes through her hair giving it an ethereal look as it drapes down on her shoulders. By observing her alone, you begin to feel unsettled and hot."
    "> She tucks her hair behind her ear as she finishes up the final touches, but realizes that you are staring at her."
   
    show cath casual 2 with dissolve
    p "...Why are you staring at me?"
    show cath casual 1
    menu:
        "Is it hot in here?":
            $ girl2.add_affection(-1)
            show cath casual 2
            p "No not really, why are you sweating? That's kinda gross."
            show cath casual 1
            m "{b}{i}WHY AM I SWEATING???{/i}{/b}"
            m "uh gah... don't worry about it. It's just hot."
            show cath casual 2
            p "... o--okay..."
            show cath casual 1
            menu:
                "Sorry you just looked really good today":
                    $ girl2.add_affection(-1)
                    show cath casual 2
                    p "Creep."
                    show cath casual 1
                    show thought with dissolve
                    m "{i}Uhhh maybe I shouldn't have said that, she probably thinks I'm weird.{/i}"
                    hide thought with dissolve
                    "> You don't really know how to follow up on that response, so you decide to let the awkward space settle for a moment."
                    menu:
                        "Wow, the posters look amazing! We did a good job":
                            jump music_event_1_part_3
                "Wow, the posters look amazing! We did a good job":
                    jump music_event_1_part_3
                   
        "Sorry you just looked really good today":
            $ girl2.add_affection(-1)
            show cath casual 2
            p "Creep."
            show cath casual 1
            show thought with dissolve
            m "{i}Uhhh maybe I shouldn't have said that, she probably thinks I'm weird.{/i}"
            hide thought with dissolve
            "> You don't really know how to follow up on that response, so you decide to let the awkward space settle for a moment."
            menu:
                "Is it hot in here?":
                    $ girl2.add_affection(-1)
                    show cath casual 2
                    p "No not really, why are you sweating? That's kinda gross."
                    show cath casual 1
                    show thought with dissolve
                    m "{b}{i}WHY AM I SWEATING???{/i}{/b}"
                    hide thought with dissolve
                    m "Uh gah... don't worry about it. It's just hot."
                    show cath casual 2
                    p "... O--okay..."
                    show cath casual 1
                    menu:
                        "Wow, the posters look amazing! We did a good job":
                            jump music_event_1_part_3
                "Wow, the posters look amazing! We did a good job":
                    jump music_event_1_part_3
                           
        "Wow, the posters look amazing! We did a good job":
            jump music_event_1_part_3
 
label music_event_1_part_3:
    $ girl2.add_affection(1)
    show cath casual 4
    "> She looks happy at your comment."
    show cath casual 5
    p "I guess you aren't that useless."
    show cath casual 4
    m "Thanks?..."
    show thought with dissolve
    m "{i} At least I'm not ‘super useless'...{/i}"
    hide thought with dissolve
    m "I was thinking we should probably get to practicing soon."
    show cath casual 5
    p "Oh! Of course, I didn't forget about that---"
    show cath casual 4
    show thought with dissolve
    m "{i}Sureee...{/i}"
    hide thought with dissolve
    hide cath with dissolve
    scene bg hallway
    with fade
    "> Catherine and you are finished making the posters for the concert and put them around the school."
   
    scene bg music_room
    with fade
    show cath casual 4
    m "Do you want to play now?"
    show cath casual 5
    p "Uh... Sure. What do you want to play?"
    show cath casual 4
    stop music fadeout 1.0
    hide cath with dissolve
    menu:
        "Beethoven Violin Sonata No.9 Op.47 \"Kreutzer\"":
            m "Let's play Beethoven Violin Sonata No.9 Op.47 \"Kreutzer\"." #ADD MUSIC
            $ girl2_music_choice = 1
            play music "Beethoven.mp3" fadein 1.0
           
        "Chopin Tristesse Etudes in E major":
            m "Let's play Chopin Tristesse Etudes in E major." #ADD MUSIC
            $ girl2_music_choice = 2
            play music "Chopin.mp3" fadein 1.0
           
        "Rondo Capriccioso- Saint-Saens":
            m "Let's play Rondo Capriccioso- Saint-Saens." #ADD MUSIC
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
    show cath casual 4 with dissolve
    m "That was fun!"
    show cath casual 5
    p "Yeah..."
    show cath casual 4
    m "Here's an idea... Do you think that I could play with you in your concert?"
    show cath casual 12
    p "OF COURSE NOT!!! This is actually important."
    show cath casual 4
    menu:
        "Change your mind":
            $ girl2.add_affection(-1)
            m "Whatever, It's not like I cared enough to help anyways."
            show cath casual 1
            "> She looks pretty mad at that last comment."
            show cath casual 2
            p "You don't have to be so butthurt about it."
            show cath casual 1
            show thought with dissolve
            m "{i}Maybe I shouldn't have thought out loud.{/i}"
            hide thought with dissolve
        "Try to convince her":
            $ girl2.add_affection(1)
            m "What?! Why not? I think it would be fine, Cathy! If you ever want an accompanist, I'll be around."
            show cath casual 15
            "> She avoids eye contact and slightly blushes."
            show cath casual 17
            p "...Thanks, I'll think about it. BUT I TOLD YOU NOT TO CALL ME THAT."
            show cath casual 15
           
    show cath casual 2
    "> Catherine huffs."
    p "Anyways, I should get going."
    show cath casual 4
    "> She packs up quickly and begins to rush out."
    m "I'll see you tomorrow then."
    show cath casual 2
    p "...Yeah"
    hide cath with dissolve
    show thought with dissolve
    m "{i}Hmm she seems a little off. Was it something I said?{/i}"
    hide thought with dissolve
    scene bg home
    with fade
    "> Your room."
    m "That was a long day, time to hit the sack."
    $ stats.increment_days()
    scene bg hallway with fade  
    "> Next morning."
    m "Another day at school..."
    scene bg classroom with fade
    m "Time for classes. What should I take today?"
    $ stats.reset_classes()
    call make_schedule
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
    "> You walked into the music room. Strangely, there is no music being played."
    show cath casual 1 with dissolve
    "> You see Catherine leaning against the window sill. She's looking out the window contently."
    show thought with dissolve
    m "{i}I guess it's a good day out.{/i}"
    hide thought with dissolve
    "> The warm lighting gives her a glow, where she seems so peaceful. For some reason everything seems so vibrant. The lighting gives her a warm, peaceful glow."
    show cath casual 4
    "> Catherine sees your reflection in the window and turns around to address you with a smile on her face."
    show cath casual 5
    p "Can I ask you for a favour?"
    show cath casual 4
   
    menu:
        "Yeah, of course":
            $girl2.add_affection(1)
        "Sure, if you act a litter nicer to me":
            $girl2.add_affection(-1)
    show thought with dissolve
    m "{i}She looks pretty concerned. I wonder what it is about?{/i}"
    hide thought with dissolve
    show cath casual 17
    p "So... The concert..."
    show cath casual 15
    m "Yeah?"
    show cath casual 17
    p "Apparently, I’m required to have an accompanist."
    show cath casual 15
    m "Oh? And?"
    "> You try not to crack a smile knowing what's coming."
    show cath casual 17
    p "So... I... may need you to play as my accompanist."
    show cath casual 15
    m "I don't know... I thought I wasn't good enough?"
    show thought with dissolve
    m "{i}I'm not sure if I should be teasing her in a situation like this, but I need to make the most of this opportunity!{/i}"
    hide thought with dissolve
    "> She seems surprised at your response like she was expecting you to agree right away.  Her face instantly turns red from frustration."
    show cath casual 17
    p "I know I've been mean to you this whole time, but please! This is my only opportunity!"
    show cath casual 18
    "> Her eyes begin to water."
    show cath casual 17
    p "I just get so frustrated when I can't do anything myself. I don't want people to see me as weak, but it is a requirement and I need someone to lean on. Please..."
    show cath casual 19
    show thought with dissolve
    m "{i}Oh crap. She's super serious right now.{/i}"
    hide thought with dissolve
    menu:
        "Yeah, don't worry. I said I was going to be around if you needed me, right? Let's start practicing for it!":
            hide cath with dissolve
            jump music_event_2_part_2
 
label music_event_2_part_2:
    "> Several days later."
    scene bg music_room
    with fade
    "> You arrive outside of the music room. The suit you're wearing makes you feel stiff and limited in mobility."
    m "{i}I think I look okay, I can't tell with only the moonlight{/i}"
    "> You receive a text from Catherine."
   
    scene bg balcony
    with fade
    p "Hey, I'm on the balcony."
    show cath dress 1 with dissolve
    "> You get to the top of the building and through a set of glass doors you see her in a white dress. As you pass the doors, your eyes capture the city twinkling with streetlights and cars."
    "> You lean next to her on the railing. In the corner of your eye, you catch a glimpse of her dress and skin glowing in the moonlight."
    menu:
        "You look good in this lighting":
            $girl2.add_affection(-1)
            show cath dress 10
            p "What about other lightings?"
            show cath dress 8
            show thought with dissolve
            m "{i}Oops, I guess that came out wrong.{/i}"
            hide thought with dissolve
        "It's a beautiful night":
            $girl2.add_affection(1)
            show cath dress 3
            p "Yeah, it is."
            show cath dress 5
               
    m "It's the big day huh? How are you feeling?"
    show cath dress 2
    p "My palms are a little sweaty and my head is all jumbled with worries."
    show cath dress 1
    m "It will be fine, don't worry about it. Let's just try our best!"
    show cath dress 2
    p "I need this to be perfect..."
    show cath dress 1
    menu:
        "Downplay it to make her feel more at ease":
            $girl2.add_affection(-1)
            m "Calm down a little, it's not a big deal."
            show cath dress 2
            p "Haven't you been listening at all?"
            show cath dress 1
            show thought with dissolve
            m "{i}Oh crap, that wasn't smart of me.{/i}"
            hide thought with dissolve
            menu:
                "Reassure her":
                    show cath dress 1
                    m "Well it's an important day to you right? You want to get into the school? You want to make it into the school, right?"
                    p "..."
                    m "What's with the silence?"
                   
        "Reassure her":
            $girl2.add_affection(1)
            show cath dress 1
            m "Well it's an important day to you right? You want to get into the school?"
            p "..."
            m "What's with the silence?"
   
   
    show cath dress 2
    p "To be completely honest, I couldn't care less if I went to the music academy or not. Not anymore anyways..."
    show cath dress 1
    m "I thought that was your goal to become the greatest violinist of our time?"
    show cath dress 2
    p "I mean, excelling at playing the violin is my goal, but this concert is for approval from others."
    show cath dress 1
    m "Sounds like a lot of work for some recognition."
    show cath dress 2
    p "I know... But you don't know what it's like. I've always had people holding my hand while I do everything, not letting me take my own steps, and not letting me take any credit. Maybe you do... If not,  you could at least try understanding it from my perspective."
    show cath dress 6
    "> At this moment, she turns and looks up to you. The beauty of her red lips and rosy cheeks captivates you for a moment; you feel like a pin went through your chest."
    m "I think I can understand; What if I said that even though I'm here helping you on your journey, I can see everything you've worked towards on your own. You have definitely proved that you are more than cable of handling yourself!"
    "> She smiles."
    show cath dress 4
    p "Thanks for the words of encouragement. They mean a lot to me."
    show cath dress 6
    "> She sees your watch."
    show cath dress 4
    p "Oh! It's almost time to go! Quick smell my perfume, make sure it smells good!"
    show cath dress 6
    "> She pulls back her hair and leans forward, exposing her neck to you."
    "> You quickly lean in to smell."
    "> When you breathe in the scent, it’s like fireworks beginning to going off in your head. This feeling travels down through the rest of your body, but you feel something briefly pressed against you cheek."
    show cath dress 4
    p "That was for good luck...and for listening to me."
    show cath dress 6
    "> She covers her mouth and avoids eye contact, blushing."
    m "Thanks..."
    show cath dress 11
    p "D-don't look at me like that, you're wasting time."
    hide cath with dissolve
    "> She grabs your hand and leads you through the doors of the auditorium."
   
    scene bg auditorium
    with fade
    show cath dress 13 with dissolve
    "> You feel like a ragdoll as she makes sharp corners towards back-stage. She stops abruptly and turns around quickly to face you. Her eyes are shining with excitement and nervousness."
    show cath dress 12
    p "Ready?"
    show cath dress 13
    m "Your palms are sweaty."
    show thought with dissolve
    m "{i}Oh God, I literally could have said anything else.{/i}"
    hide thought with dissolve
    show cath dress 9
    "> She pulls her hand quickly away and picks up her violin."
    show cath dress 11
    p "Don't get full of yourself. Let's do this."
    show cath dress 9
    "> You walk out onto the stage; as you look out you don't see a face, but you feel like everyone is staring at you."
    "> You take a seat at the piano and wait for her signal."
    hide cath with fade
    show cath concert with fade
    # cue music here
    stop music fadeout 1.0
    if girl2_music_choice == 1:
        play music "Beethoven.mp3" fadein 1.0
    elif girl2_music_choice == 2:
        play music "Chopin.mp3" fadein 1.0
    else:
        play music "Rondo.mp3" fadein 1.0
    "> You hear her draw her bow across the strings. Her playing is colourful, vibrant, and full of expression.  You can feel her stage presence growing as the song reaches the climax."
       
    while(1):
        $ renpy.pause(10.0)
        menu:
            "Skip?":
                jump outta_girl2_while_loop2            
               
label outta_girl2_while_loop2:  
    hide cath with fade
    stop music fadeout 1.0
    play music "Background Music.mp3" fadein 1.0
   
    "> You reach the end of the song and you get up to stand next to her. When you approach her, she holds out her hand in front of you; you grab it and bow together. The audience gives you a large applause."
    "> Both of you walk off stage."
    show cath dress 4
    p "We did it!"
    show cath dress 6
    menu:
        "Hug her":
            $ girl2.add_affection(1)
            m "Yeah, good job!"
            "> You hug her. You intended to have a quick hug, but it lingers for a while longer."
            show cath dress 4
            p "I'm really thankful for you helping me out."
            show cath dress 6
        "Talk about the Academy":
            $ girl2.add_affection(-1)
            m "You did it, you're sure to get in now! I'm glad it went well."
            show cath dress 2
            p "Oh yeah... right. Thanks..."
            show cath dress 1
           
   
    m "We should celebrate!"
    show cath dress 2
    p "Celebrate? What do you have in mind?"
    show cath dress 1
    m "How about karaoke?"
    show cath dress 10
    p "Karaoke?"
    show cath dress 8
    m "Yeah, that thing where you sing in a room..."
    show cath dress 10
    p "I know what it is, but why karaoke?"
    show cath dress 8
    m "Why not? You've been so stressed out on music lately; this is a good way to destress."
    "> She sighs."
    show cath dress 10
    p "Okay..."
    show cath dress 8
    m "GREAT! LET'S GO."
    hide cath with dissolve
    jump music_event_3
           
label music_event_3:
    # karaoke event here, success or failure
    #TODO ADD IMAGE OUTSIDE KARAOKE
    scene bg karaoke_lobby with fade
    with fade
    show cath casual 14 with dissolve
    m "Here we are."
    show cath casual 16
    p "Y-yeah..."
    show cath casual 14
    m "What's wrong, Cathy?"
    show cath casual 16
    p "I've never sung in front of anyone..."
    show cath casual 14
    m "So wait, you're telling me that you can get on a stage in front of hundreds of people, but you can't sing in front of me?"
    show cath casual 17
    p "IT'S DIFFERENT! The violin produces such elegant music."
    show cath casual 14
    menu:
        "Reassure her":
            $ girl2.add_affection(1)
            m "It can't be that bad. Don't worry, I'm not here to judge you."
            show cath casual 16
            p "Liar..."
            show cath casual 14
            m "PROMISE."
            "> She rolls her eyes."
            show cath casual 16
            p "Don't say I didn't warn you."
            show cath casual 14
           
        "Joke":
            $ girl2.add_affection(-1)
            m "Well that's a shame, I guess that's the problem with hiding behind an instrument your whole life."
            show cath casual 16
            p "Aren't you a tad bit conceited?"
            show cath casual 14
            m "That came out wrong..."
            show cath casual 16
            p "Yeah it did."
            show cath casual 14
    show cath casual 16
    p "Well... let's get this over with."
    show cath casual 14
    "> You place your hands on her shoulders and guide her into the karaoke room."
    hide cath with fade
    scene bg karaoke
    with fade
    show cath casual 3
    m "Come on, it's going to be fun!"
    "> When you sit down, you place songs in the playlist. As one of them is about to begin, you notice out of the corner of your eye, Catherine clutching the mic with both hands. She holds it with her arms retracted close to her chest."
    m "C'mon, lighten up! This is supposed to be fun! Just imagine I'm not even here."
    "> You take 2 short consecutive breaths out, followed by one drawn out exhale."
    show cath casual 5
    "> She bursts out laughing."
    p "That's what you do when you're giving birth!"
    show cath casual 4
    m "THEN YOU HAVE NOTHING TO WORRY ABOUT!"
    show cath casual 5
    "> She laughs."
    p "Alright, alright I'm ready."
    show cath casual 3
    "> Her shoulders relax and she takes a deep breath."
    "> As the music starts playing, the song starts slow. While following the lyrics, her voice takes you by surprise. Her voice actually is powerful and smooth."
    hide cath with fade
    stop music fadeout 1.0
    play music ["Adele Karaoke.mp3", "John Legend Karaoke.mp3", "Jpop.mp3"] fadeout 1.0 fadein 1.0
    show thought with dissolve
    m "{i}SHE LIED TO ME{/i}"
    hide thought with dissolve
    show cath casual 5 with dissolve
    "> You decide to just go with it. You have an almost Déjà vu moment as if you were her accompanist again. Naturally, you begin to harmonize with her. It must be from practicing with her. At one point of the song, you both feel each other pushing your diaphragms to their limit. You look at each other trying not to laugh."
    "> You see her under the fluorescent rose lighting of the room, she looks like she's really having enjoying herself. She looks at you and smiles as the song ends."
    #stop music fadeout 1.0
    
    show cath casual 4
    p "That was great!"
    "> She begins laughing uncontrollably while leaning forward."
    "> She beings to lose balance as she falls forward and falls in your direction. You react by trying to catch her with both arms, but her momentum catches you off guard and pushes you back. You fall directly on your butt."
    show cath casual 13
    p "OH! I'M SO SORRY ARE YOU OKAY?"
    show cath casual 11
    "> She immediately panics and clumsily tries helping you up."
    m "Probably just fractured my tailbone, but I'm fine."
    show cath casual 9
    p "SERIOUSLY?"
    show cath casual 15
    m "Don't worry... I'm just kidding."
    show cath casual 17
    p "Don't scare me like that..."
    show cath casual 15
    m "Since when did you start worrying about me so much?"
    show cath casual 9
    "> Her cheeks instantly turn red."
    p "I-I don't know what you're talking about... Idiot."
    show cath casual 15
    menu:
        "Hey, if you want to talk about something, I'm listening":
            $ girl2.add_affection(1)
            p "..."
           
        "Oh alright":
            $ girl2.add_affection(-1)
            p "... Why do you have to be so dense all the time?"
           
    "> She sighs."
    show cath casual 16
    p "Look... It's been really hard for me to be comfortable around you."
    show cath casual 14
    m "What do you mean?"
    show cath casual 16
    p "In the short time I've known you, I don't think I've ever felt so close to anyone. At first I couldn't stand you being around, but you just kept persisting to help me out and to help you out. Then well I guess you just grew on me."
    show cath casual 14
    m "Is that a bad thing?"
    show cath casual 16
    p "No... I’m just a little confused, that’s all... I’ve grown up in a well off family and I always was given opportunities, as if they were served to me on a silver platter. I never felt like I earned anything. I eventually just hated it when people helped me accomplish tasks; people always checking up on me saying ‘Do you need help with that’ As if I couldn’t handle myself, as if I was completely incapable of doing anything. I started to be secluded from people and refused people that tried to get close to me."
    show cath casual 14
    m "What about now?"
    show cath casual 16
    p "I don't know anymore. I guess you could say that you're now an exception to the rule."
    show cath casual 4
    "> She smiles, leans back into the couch, and stares blankly towards the karaoke lyrics rolling."
    show cath casual 5
    p "You know, it's funny. I try to push people away, but then one person is just able to push through all the walls I set up. I didn't want to trust that person, but I end up leaning on them the most, when I'm in need."
    show cath casual 4
    "> She shifts her weight so that her rests upon your shoulder."
    "> You feel a tension while your beats per minute skyrocket. It's like your head is going to explode from built up pressure."
    m "H-hey Ca--"
    show cath casual 5
    p "Just be quiet for a moment..."
    show cath casual 4
    "> Neither of you move while the karaoke lyrics roll and the rose lights pulsate in the room. From this atmosphere, you just enjoy each other's presence."
    menu:
        "Hey Cathy, do you want to go out with me?":
            # check affection level
            $ affection = girl2.get_affection("Catherine")
            # if success:
            if affection >= 4: # NUMBER CAN VARY
                show cath casual 8
                p "Does it look like I don't want to?"
                show cath casual 7
                m "Well maybe you just wanted to be friends."
                show cath casual 8
                p "Sometimes I can't believe how clueless you can be... So I'll say it plainly: I want to go out with you."
                show cath casual 7
                "> She wraps her arms around your torso, smiling. You both continue to bask in the emotions until it's time to go."
                show cath casual 5
                p "Thank you for everything. I am really glad to have met you."
                stop music fadeout 1.0
                hide cath with dissolve
                jump music_event_3_part_2
            # if failure:
            else:
                show cath casual 8
                p "Does it look like I don't want to?"
                show cath casual 7
                m "Well maybe you just wanted to be friends."
                show cath casual 8
                p "Sometimes I can't believe how clueless you can be... But, I can't..."
                show cath casual 14
                m "..."
                show cath casual 16
                p "I got into the academy..."
                show cath casual 14
                m "Oh... Congrats..."
                "> She wraps her arms around your torso, and begins to have tears streaming down her face."
                show cath casual 16
                p "I'm so sorry... as much as I want to be with you... this is a really important opportunity."
                show cath casual 14
                m "No of course... I couldn't expect you to drop everything for me..."
                "> You both sit and try to savour the moment. She latches onto you tight, not wanting to let go. You sit trying to hold on to each other's presence inevitably comes to an end."
                show cath casual 16
                p "Thank you for everything. I am really glad to have met you..."
                stop music fadeout 1.0
                hide cath with dissolve
                jump girl2_fail_end
   
label music_event_3_part_2:
    scene bg home
    with fade
    play music "Background Music.mp3" fadein 1.0
    "> A few days have passed since that day."
    play sound "Cell Phone Ring.mp3"
    "> Your phone rings."
    stop sound
    m "Hello?"
    p "Hi %(player_name)s."
    m "Hey, Cathy!"
    p "I got the results from the evaluation."
    menu:
        "Great! this will be a great opportunity for you!":
            p "It is good..."
            m "I'll see you at the music room then."
           
        "Oh I see, how do you feel about it?":
            p "Hmm... I don't know if I really want to go anymore."
            m "What about being the greatest violinist ever?"
            p "Well I just wanted to talk to you about it too. Wanna meet in the music room?"
            m "Sure."
           
    scene bg music_room
    with fade
    show cath casual 7 with dissolve
    "> You arrive to the music room."
    "> You see her again against the window sill."
    m "Hey, Cathy."
    show cath casual 8
    p "Hey..."
    show cath casual 7
    m "Did you want to talk about it?"
    show cath casual 8
    p "I'll just get to the point: Do you want me to go or not?"
    show cath casual 7
    m "Wait what? For the Academy? Why does my opinion matter?"
    show cath casual 8
    p "Because it matters to me... because you're important to me."
    show cath casual 7
    m "Oh..."
    show cath casual 8
    p "So tell me, do you want me to stay or not?"
    show cath casual 7
    menu:
        "I want you to stay":
            jump girl2_good_end
           
        "I think you should take the opportunity":
            show cath casual 14
            m "I completely support your decision."
            show cath casual 16
            p "Ohh... haha... Yeah, thanks for supporting me"
            show cath casual 14
            m "Yeah, of course."
            "> She sighs."
            show cath casual 16
            p "Well I guess this is what I asked for."
            show cath casual 14
            m "Don't worry, I think you'll go really far with it. You'll be able to experience a lot of great things, especially living in the UK independently."
            show cath casual 16
            p "Yeah you're right..."
            show cath casual 14
            "> She seems frustrated about something."
            show cath casual 16
            p "I don't get it! I haven't even known you for that long, but all the sudden you'll be out of my life. I tried so hard to be independent and do things on my own, and when I finally get the chance, I don't want it. I end up depending on you anyways. I even said 'yes', when you asked me out!"
            show cath casual 14
            menu:
                "We can still keep in touch":
                    m "Hmm... You didn't necessarily depend on me, you could always do it by yourself, I was just an accompanist. Besides we can still keep in touch."
                    show cath casual 16
                    p "Yeah... that's a fair argument."
                    show cath casual 19
                    "> She shoves her face into your chest and latches around your torso."
                    show cath casual 17
                    p "...Will you remember me?"
                    show cath casual 15
                    m "What if told you I will?"
                    show cath casual 17
                    p "That would make me happy... Well... Goodbye then..."
                    show cath casual 7
                    m "This isn't 'goodbye', it's just a 'see you later'..."
                    stop music fadeout 1.0
                    jump girl2_bad_end
                   
                "Change your mind":
                    m "I'm just trying to not be selfish but believe me when I say I really do want you to stay. You're important to me and it would hurt to watch you leave."
                    stop music fadeout 1.0
                    jump girl2_good_end
                   
        "You should make the decision yourself":
            "> Catherine seems frustrated."
            show cath casual 12
            p "I don't get it! I haven't even known you for that long, but all the sudden you'll be out of my life. I tried so hard to be independent and do things on my own, and when I finally get the chance, I don't want it. I end up depending on you anyways. I even said 'yes', when you asked me out!"
            show cath casual 10
            m "This is finally your chance to be independent."
            m "This is what you wanted. What you worked for. You made it and you shouldn't let me hold you back."
            show cath casual 12
            p "...Is it so wrong to have someone to lean on at least sometimes...I thought I could depend on you. We've been through a lot together...I really had feelings for you."
            show cath casual 10
            m " I didn't mean it like that..."
            show cath casual 12
            p "Forget it. You're right. I don't know what I was thinking. I'll go ahead with the academy. Thank you for everything. Let's both work hard on our separate paths."
            hide cath with fade
            "> Catherine starts walking towards the door but stops at your side. She glances up towards you quickly but then looks away and continues out the door, leaving you behind. You're left alone standing in the silent music room and you have a feeling you won't be playing the piano for a long time."
            stop music fadeout 1.0
            jump girl2_bad_end
 
label girl2_failure:
    scene bg music_room with fade
    "> You head over to the music room and expect to see Catherine playing where she usually is. "
    "> As you’re walking towards the room, there is an absence of music in the air. It is silent." 
    "> You reach the room and Catherine is nowhere in sight. You wait for almost half an hour, but she still doesn’t show up. Suddenly, your phone starts to ring." 
    show thought with dissolve
    p " Hey %(player_name)s, I totally forgot to tell you, but I hope that you aren’t at the music room waiting for me.. I’m in London."
    m "London?"
    p "I got a last minute invite to a music competition. Sorry that I didn’t call you earlier; the performances just finished."
    m "Oh.. How did you do?"
    p "I thought that I played poorly, but I got approached afterwards by a scout." 
    p "He said that I had great performance and invited me to a prestigious music academy." 
    m "Thats great! Congratulations."
    p "Thanks! I’m glad. This means I won’t be coming back to Gouglas Private Academy though. I hope that you’ll continue to practice the piano even without me there to teach you." 
    m "Right…"
    p "Good luck." 
    hide thought with fade
    "> She hangs up on you. You leave the music room feeling a little disappointed. Regretfully, you go on with the rest of your high school days." 
    "> You end up quitting the piano for the second time in your life."
    jump credit
    #return
   
label girl2_bad_end:
    scene bg music_room with fade
    "> You head over to the music room and expect to see Catherine playing where she usually is. "
    "> As you’re walking towards the room, there is an absence of music in the air. It is silent." 
    "> You reach the room and Catherine is nowhere in sight. You wait for almost half an hour, but she still doesn’t show up. Suddenly, your phone starts to ring." 
    show thought with dissolve
    p " Hey %(player_name)s, I totally forgot to tell you, but I hope that you aren’t at the music room waiting for me.. I’m in London."
    m "London?"
    p "I got a last minute invite to a music competition. Sorry that I didn’t call you earlier; the performances just finished."
    m "Oh.. How did you do?"
    p "I thought that I played poorly, but I got approached afterwards by a scout." 
    p "He said that I had great performance and invited me to a prestigious music academy." 
    m "Thats great! Congratulations."
    p "Thanks! I’m glad. This means I won’t be coming back to Gouglas Private Academy though. I hope that you’ll continue to practice the piano even without me there to teach you." 
    m "Right…"
    p "Good luck." 
    hide thought with fade
    "> She hangs up on you. You leave the music room feeling a little disappointed. Regretfully, you go on with the rest of your high school days." 
    "> You end up quitting the piano for the second time in your life."
    jump credit
    #return
 
label girl2_good_end:
    show cath casual 4
    "> She smiles."
    show cath casual 5
    p "Hahaha! You’re funny."
    "> She continues to laugh at you, but you stand there confused at what just happened."
    show cath casual 4
    m "I think I'm lost."
    show cath casual 5
    p "I already declined the offer so whether you like it or not; it looks like you're going to be stuck with me."
    show cath casual 4
    m "Oh hahaha... I thought you were asking seriously."
    show cath casual 5
    p "Well I was just asking so that I could figure out how much you like me."
    show cath casual 4
    m "Charming..."
    show cath casual 5
    p "So? What say you? Do I need to make you smell my perfume again?"
    show cath casual 4
    m "Yeah... Yeah, I do."
    "> She leans over then you feel something press against your cheek."
    show cath casual 5
    p "Besides, I already said yes to you. You're my new dream. You're mine."
    hide cath with fade
    scene bg music_room with fade
    "> Days pass and your relationship with Catherine continues to prosper."
    scene cath grad with fade
    "> You enjoy the rest of your high school life together with your girlfriend."
    "> Congratulations %(player_name)s!"
    jump credit
    #return
   
label girl2_fail_end:
    scene bg music_room with fade
    "> You head over to the music room and expect to see Catherine playing where she usually is. "
    "> As you’re walking towards the room, there is an absence of music in the air. It is silent." 
    "> You reach the room and Catherine is nowhere in sight. You wait for almost half an hour, but she still doesn’t show up. Suddenly, your phone starts to ring." 
    show thought with dissolve
    p " Hey %(player_name)s, I totally forgot to tell you, but I hope that you aren’t at the music room waiting for me.. I’m in London."
    m "London?"
    p "I got a last minute invite to a music competition. Sorry that I didn’t call you earlier; the performances just finished."
    m "Oh.. How did you do?"
    p "I thought that I played poorly, but I got approached afterwards by a scout." 
    p "He said that I had great performance and invited me to a prestigious music academy." 
    m "Thats great! Congratulations."
    p "Thanks! I’m glad. This means I won’t be coming back to Gouglas Private Academy though. I hope that you’ll continue to practice the piano even without me there to teach you." 
    m "Right…"
    p "Good luck." 
    hide thought with fade
    "> She hangs up on you. You leave the music room feeling a little disappointed. Regretfully, you go on with the rest of your high school days." 
    "> You end up quitting the piano for the second time in your life."
    jump credit
    #return
#-----------------------------END OF MUSIC GIRL---------------------------------------------#
 
#----------------------------START OF MARY--------------------------------------------------#
#Mary first encounter ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
label home_ec_room:
    # show image of room
    # play sound of sizzling noise
   
    # you have chosen Mary as the girl
    $ stats.set_chosen_girl(1)
    scene bg hallway with fade
    "> In front of the Home-Ec Room."
    scene bg home_ec_room with fade
    "> As you enter the room, you hear a sizzling noise. The fragrances tickle your nose as you enter the room. Your sight is drawn to the centre of the room, to a girl. She looks up to acknowledge you and she gives a friendly, but shy smile."
    show mary cook smile with dissolve:
        xalign 0.7
        linear 1.0 xalign 0.5
    p "Hello, I haven't seen your face around, are you new?"
   
    m "Yeah, I just transferred here recently. Is this the cooking club?"
   
    show mary cook happy
    p "Yes! You've come to the right place."
   
    m "Where do I sign up?"
    show mary cook wonder
    p "Well... You kind of need to cook in this club. Show me what you can do first and then we can talk about your membership."
    show mary cook straight
    show thought with dissolve
    "> You realize that you've only been here for a day and the only culinary experience you have comes from instant ramen, but how hard could it be?"
    hide thought with dissolve
    p "...Hello? You blanked out for a second. What do you plan on making for me?"
    $ str_check = stats.get_stats("str")
    $ int_check = stats.get_stats("int")
    $ cha_check = stats.get_stats("cha")
   
    menu:
        "Chocolate chip cookies (Need: 1 Strength & 1 Charm)":
            hide mary cook wonder
            if str_check >= 1 and cha_check >= 1:
                "> Miraculously, you remember a recipe for chocolate cookies and manage to put them together."
                $ stats.set_food_choice(0)
                jump girl_1_convo_1
            else:
                "> You don't remember how to make this, time to guess!"
                $ stats.set_food_choice(1)
                jump girl_1_convo_1
       
 
        "Instant Ramen (No requirements)":
            hide mary cook wonder
            "> You decide that it’s would be more efficient to make what you know the best. Conveniently, you remember that you brought along a spare package of instant noodles to school with you. You pull it out of your backpack and proceed to open the plastic wrapping."
            $ stats.set_food_choice(2)
            jump girl_1_convo_1
       
        "Beef Carpaccio (Need: 2 Strength)":
            hide mary cook wonder
            "> You decide that it would be best to go big or go home. If you managed to pull this off, she would be incredibly impressed. Unfortunately, you do not have the knowledge of the ingredients or techniques need to put this dish together. You improvise as you go."
               
            if str_check >= 2:
                $ stats.set_food_choice(3)
                jump girl_1_convo_1
            else:
                $ stats.set_food_choice(4)
                jump girl_1_convo_1
           
label girl_1_convo_1:
 
    "> As you're working, you can't help notice the awkward silence settling in. You glance over to her and end up making eye contact. You could probably use this time to get to know her."
 
    menu:
        "Ask her for her name":
            show mary cook straight with fade
            m "Soooo... I actually never caught your name, my name's %(player_name)s."
            show mary cook shock
            p "Oh, sorry about that!"
            show mary cook smile
            p"I'm Mary, I am president of the cooking club. I'm also in my senior year."
            # change the name of p to Mary
            $ unknown_name = "Mary"
           
            menu:
                "Ask her why she joined the cooking club":
                    show mary cook shy
                    p "It's just a hobby, nothing that serious."
           
        "Ask her why she joined the cooking club":
            show mary cook wonder with fade
            p "Why did I join the cooking club?"
            p "It's just a hobby, nothing that serious."
           
            menu:
                "Ask her for her name":
                    m "Soooo... I actually never caught your name, my name's %(player_name)s."
                    show mary cook shock
                    p "Oh, sorry about that!"
                    show mary cook smile
                    p "I'm Mary, I am president of the cooking club. I'm also in my senior year."
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
        hide mary
        "> You peek at her eyes to get some idea of what she may be thinking, but it's not really discernible. You watch nervously as she takes a bite. This is your favorite flavor of instant noodles. After swallowing, she hesitates for a moment, and her eyes bulge. Violently she clasps her mouth and supports herself with the edge of the counter. She spits out your creation."
        jump made_bad_food_1
    else:
        hide mary
        "> You peek at her eyes to get some idea of what she may be thinking, but it's not really discernible. You watch nervously as she takes a bite, wondering if you put in enough sriracha sauce to mask the overbearing taste of durian. After swallowing, she hesitates for a moment, and her eyes bulge. Violently she clasps her mouth and supports herself with the edge of the counter. She spits out your creation."
        jump made_bad_food_1
       
label made_bad_food_1:
    show mary cook pout with fade
    p "It was... uh... not bad... "
    show mary cook shy
    "> She forces a smile and pushes your food a few inches away"
    m "Sorry about that. Maybe you can teach me some basics?"
    show mary cook straight
    p "Hmmm... That sounds okay I suppose..."
    show mary cook smile
    p "Come by tomorrow and I'll teach you a little of what I know."
    "> You decide to head home for the day."
    jump end_day_1
   
label made_good_food_1:
    show mary cook shock with fade
    p "It was good!"
    $ girl1.add_closeness(1)
    show mary cook smile
    "> Mary gives a warm smile"
    show mary cook happy
    # change it to something without sous chef. No relevancy. Just be like Okay you've proven yourself. You are free to come by tomorrow after classes or something
    p "With your cooking skills, I'd be happy to let you into the club! Come by again tomorrow after class if you're free."
    "> You decide to head home for the day."
    jump end_day_1
    #jump standard_end_day #LINE TO JUMP TO STANDARD CYCLE CODE in day_cycle.rpy
   
label end_day_1:
    scene bg player room with fade
    #show image of bedroom at night
    m "That was a long day; it's time to hit the sack."
    $ stats.increment_days()
    jump standard_day_cycle
#    jump start_day_2
# end of mary introduction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
label start_day_2:
    scene bg hallway with fade
    "> Next morning."
    m "Another day at school..."
    scene bg classroom with fade
    "> Morning classes don't seem to be getting any easier for you."
    scene bg hallway with fade
    "> Afternoon."
    m "Alright, time for afternoon classes."
    $ stats.reset_classes()
    call make_schedule
    scene bg hallway with fade
    show thought with dissolve
    m "{i}Maybe I should drop by the club room. Mary might be there too.{/i}"
    hide thought with dissolve
   
    jump home_ec_day_2
   
label girl1_check_1:
    $ closeness = girl1.get_closeness("Mary")
    $ day = stats.get_days()
    $ event_num = girl1.get_event("Mary")
    if not girl1check1: #Check if date has triggered already
        if day <= 5 and closeness > -3 and closeness < 5:
            # continue on with cooking
            return
        elif day > 5:
            # too long trigger failure event
            jump girl1_time_passed
        elif closeness <= -3:
            # lost too much closeness
            jump girl1_time_passed
        elif day < 5 and closeness >= 5 and event_num == 0: #EVENT TRIGGERED
            # trigger event 1 of cafe as day < 5 and closess > 5
            # set the event value to 1
            $ girl1.add_event()
            $ girl1check1 = True
            $ standard_dc = 0
            scene bg hallway with fade
            show mary casual straight with dissolve:
                xalign 1.0
                linear 1.0 xalign 0.5
            "> Outside Home-Ec room"
            "> You see Mary standing outside the door."
            p "Hey %(player_name)s! Do you have a minute?"
            m "Sure, what's up?"
            show mary casual happy
            p "I was wondering if you would want to grab some coffee after our club today."
            show mary casual smile
            m "Of course! Where did you have in mind?"
            show mary casual happy
            p "There's this small cafe a couple blocks away from school. It's a nice, quiet place to relax every now and then."
            show mary casual smile
            menu:
                "Sounds great!":
                    show mary casual laugh
                    p "Let's meet up afterwards then!"
                    "> Mary looks very excited."
                "A cafe... really?":
                    show mary casual pout
                    $ girl1.add_closeness(-1)
                    p "Is.. that a no?"
                    "> Mary starts pouting at you."
                    "> You no longer feel any urge to reject her offer."
                    m "Alrgiht. I'll join you."
                    show mary casual laugh
                    p "Great! Let's meet up afterwards then!"
            jump cafe_date1
    else:
        return
       
label girl1_check_2:
   
    $ closeness = girl1.get_closeness("Mary")
    $ event_num = girl1.get_event("Mary")
    if not girl1check2:
        if closeness >= 11  and event_num == 1: #EVENT TRIGGERED
            $ girl1.add_event()
            $ girl1check2 = True
            $ standard_dc = 1
            scene bg hallway with fade
            show mary casual straight with dissolve
            "> Mary is standing outside the club room. It looks like she was waiting for you."
            show mary casual shock
            p "Ah!"
            show mary casual happy
            p "There you are %(player_name)s! Are you free right now?"
            show mary casual wonder
            p "You see, my mother had made reservations tonight at this restaurant I've been dying to try."
            show mary casual sad
            p "But, I got a call from her earlier saying she couldn't make it tonight. She suggested I find a friend to go with instead so we don't waste the reservation."
            show mary casual happy
            p "Immediately I thought, 'who better than the newcomer.' I feel like you can appreciate good food as much as I do."
            show mary casual shy
            p "You will join me, right?"
            show thought with dissolve
            "> You have no power here. To the restaurant!"
            jump restaurant_date1
        else:
            return
    else:
        return
       
label girl1_check_3:
    $ closeness = girl1.get_closeness("Mary")
    $ event_num = girl1.get_event("Mary")
    if not girl1check3:
        if closeness >= 18 and event_num == 2: #EVENT TRIGGERED
            $ girl1check3 = True
            $ standard_dc = 2
            scene bg hallway with fade
            show mary casual sad with dissolve:
                xalign 0.7
                linear 1.0 xalign 0.5
            show thought with dissolve
            "> You notice Mary doesn't look as cheerful as she normally does when she cooks."
            m "Is she still concerned about what we talked about at the restaurant?"
            "> You decide to try and cheer her up."
            hide thought with dissolve
            jump girl1_home_date
        else:
            return
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
   
    scene bg home_ec_room with fade
    show mary cook wonder with dissolve:
        xalign 0.7
        linear 1.0 xalign 0.5
    p "Is everyone here now? Alright! Let's start cooking!"
    hide mary with dissolve
    "> There are 3 different recipes on a counter."
    m "Which one should I make today?"
    menu:
        "Blueberry Muffin (No requirements)":
            scene bg home_ec_room with fade
            "> The muffins turned out great!"
            p "Wow! They're so fluffy, but the top is so crisp. Good job!"
            $ girl1.add_closeness(1)
           
        "Crème brûlée (Need: 2 Intelligence  & 2 Charm)":
            scene bg home_ec_room with fade
            if int_check >= 2 and cha_check >= 2:
                # sucess
                "> The crème brûlée  looks great! nice golden caramelize on it! Looks delicious!"
                p "Looks great. I'm impressed."
                $ girl1.add_closeness(3)
            else:
                # failure
                "> The crème brûlée turned out completely black... You think that you burnt it..."
                p "Uhh... is this even edible?"
                $ girl1.add_closeness(-3)
               
        "Lasagna (Need: 2 Strength & 1 Charm)":
            scene bg home_ec_room with fade
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
    scene bg hallway with fade
    "> Next morning."
    m "Another day at school..."
    scene bg classroom with fade
    "> You feel you're slowing getting more used to school life."
    scene bg hallway with fade
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
           
 
        "Assorted Sashimi (Intelligence 3, Strength 3)":
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
    scene bg hallway with fade
    m "Another day at school..."
    scene bg classroom with fade
    "> Morning lectures weren't anything too difficult for you to understand."
    scene bg hallway with fade
    m "Time to pick my afternoon classes."
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
 
    p "I feel like I need some inspiration right now... I wish I could try some new food somewhere. Do you have any suggestions %(player_name)s?"
 
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
                p "I think that you overbaked the pie."
                $ girl1.add_closeness(-2)
               
    $stats.increment_days()
 
label return_to_which_day:
    $ day = stats.get_days()
    if day == 1:
        jump end_day_1
    elif day == 2:
        jump start_day_2
    elif day == 3:
        jump day_3
    elif day == 4:
        jump day_4
    else:
        jump day_5
 
label day_5:
    scene bg hallway with fade
    m "Another day at school..."
    scene bg classroom with fade
    "> Morning classes are the same as usual. You can't help but feel that you're forgetting somethhing."
    scene bg hallway with fade
    m "What should I take in the afternoon today?"
    $ stats.reset_classes()
    call make_schedule
    jump girl1_time_passed
   
label girl1_failure:
    if stats.get_days == 5:
        "> It seems that too many days have passed and you still haven't gotten any closer to Mary."
    jump mary_bad_end
    #else:
    #    jump mary_bad_end
    # failed, end game here
    return
               
 
#the main daytime routine. //UNUSED
#label daytime:
#    $ stats.days += 1
#    $ temp = stats.days
#    "this is the daytime routine (Day %(temp)d)"
#    call raisestat #go to raisestat routine
#
#    if stats.days < 5:
#        jump daytime #jump to daytime again
#
#    "ya out of time"
#
#    return #end game
#
#routine for raising stats //UNUSED
#label raisestat:
#    menu:
#        "What Stat to raise"
#
#        "Strength":
#            $ stats.add_stats("str",1)
#            $ temp = stats.get_stats("str")
#            "strength is now [temp]."
#        "Intelligence" if stats.get_stats("str") > 1:
#            $ stats.add_stats("int",1)
#            $ temp = stats.get_stats("int")
#            "intelligence is now [temp]."
#        "Charm" if stats.get_stats("str") + stats.get_stats("int") > 3:
#            $ stats.add_stats("cha",1)
#            $ temp = stats.get_stats("cha")
#            "charm is now [temp]."
#    return
 
 
 
#MARY DATE EVENTS ================================================================================================================================================
#Mary - Cafe Date ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
label cafe_date1 :
    if cafe_trigger == 0:
       
        if cafe_asked_count == 0 :
            scene bg cafe with fade
            "> At the cafe."
            show mary casual smile with dissolve
            "> You make your way to the cafe with Mary. "
            "> The two of you spend some time casually talking at your table. A warm glow shines through the windows."
            show mary casual straight
            "> Mary is looking off to the distance, showing little expression."
           
            "> Your orders arrive at the table."
            show mary casual wonder
            p "Thank you!"
            show mary casual straight
            show thought with dissolve
            m "{i}She seems distracted. Maybe I should be more engaging. What should I ask her?{/i}"
        else:
            show thought with dissolve
            m "{i}What else should I ask her?{/i}"
        menu:
            "Do you have a boyfriend?" if not cafe_boyfriend:
                $ cafe_asked_count += 1
                $ girl1.add_closeness(-1)
                hide thought with dissolve
                show mary casual grumpy
                p "Excuse me? Where is this coming from all of a sudden? What does it matter to you anyways?"
               
                "> Mary looks displeased."
                   
                " Maybe I should I should drop the topic..."
                $ cafe_boyfriend = True
                jump cafe_date1
           
            "C'mon, just tell me." if cafe_boyfriend:
                hide thought with dissolve
                $ cafe_asked_count += 1
                $ girl1.add_closeness(-1)
                p "Mmm... You really are persistent."
                show mary casual sad  
                "> Mary looks very uncomfortable."
                   
                p "Oh yeah... I remembered there was something I had to do back home."
                show mary casual pout
                p "Sorry to leave you so suddenly. Here's some money for the bill."
                jump cafe_date_badending
                   
           
            "What do you want to do after high school?" :
                hide thought with dissolve
                $ cafe_asked_count += 1
                show mary casual wonder
                p "Hmm.. not sure. Medicine? Engineering? Something in those professional fields. What do you think?"
               
                menu :
                    "Sounds great! I'll support you if you ever need help." :
                        show mary casual shy
                        p "Yeah... It does sound great, doesn't it?"
                       
                        "> Mary forces a smile. She lets out a small sigh."
                        show mary casual sigh
                        p "That's how life is supposed to go, right? As long as I can meet my mom's expectations. I guess that's what is most important. Cooking will always be just a hobby."
                       
                        "> You sense a hint of frustration in her voice."
                       
                        m "What do you mean?"
                       
                        jump mary_backstory1
                       
                    "What about a profession in cooking?" :
                        $ girl1.add_closeness(1)
                        jump mary_backstory1
                       
                       
            "Do you usually come here?" if not cafe_before:
                hide thought with dissolve
                $ cafe_asked_count += 1
                $ cafe_before = True
                $ girl1.add_closeness(1)
                $ girl1.add_affection(1)
                show mary casual happy
                p "Yeah! I love coming here for the pastries and desserts!"
               
                " > Mary looks more excited as she rapidly counts her fingers."
                show mary casual laugh
                p "Everything here is good, black forest cake, gingersnaps, cinnamon buns... "
                p "You should try the tiramisu here!"
                p "..."
                "> Mary pauses."
                show mary casual shy
                p "Oops.. Haha, sorry. I'm usually more calm."
                show mary casual sigh
                "> Mary takes a therapeutic breath."
               
                m "Hahaha, don't worry. It's really kind of cute."
                show mary casual flustered1
                "> Mary blushes. Her eyes drop to her latte."
                                         
                jump cafe_date1
               
            "How are classes?" if not cafe_asked1:
                $ cafe_asked_count += 1
                $ cafe_asked1 = True
                show mary casual wonder
                p "Ehhh... not bad. Classes are the same old. Nothing that interesting."
               
                jump cafe_date1
    else:
        return
           
 
label mary_backstory1 :
   
    $ cafe_trigger = 1
    show mary casual sad
    p "Hmm... I don't know. I feel that cooking is not the most stable career out there."
   
    m "So?"
    show mary casual pout
    p "Soooo... That's being pretty unrealistic. It's too selfish for me to just think about what I want to do."
    p "I mean, when I get older I have to think about supporting a family and taking care of kids so that they can go to university. At least that's what my mom thinks."
    show mary casual sigh
    "> Mary lets out a heavy sigh as her eyes roll back and she leans back into her chair. Her posture sinks and her eyes fall down to her cup."
    menu:
        "> Joke." :
           #$girl1.add_closeness(-1)
           m "Oh... Talk to me about it. Tell Dr. Fill about your problems."
           show mary casual sad
           p " Uhmm... I'd rather not talk about it right now."
           m "Feel free to talk to me anytime."
           show mary casual shy
           p "Yeah, thanks."
           
        "> Console." :
            $girl1.add_closeness(1)
            $girl1.add_affection(1)
            m" That's rough. If you ever want to talk about it sometime, I'll be here."
            show mary casual shy  
            p "Thanks. Maybe another time."
           
            m "Yeah, anytime!"
    show mary casual shock
    p "Ahh.. It's getting pretty late, I should head home."

    jump cafe_date_goodending
 
label cafe_date_goodending :
    scene bg cafe with fade
    show mary casual smile with dissolve
    "> After a while of more small talk, the two of you finish your food. You both stand up and she looks at you."
    show mary casual happy
    p "I enjoyed this. We should get together more often."
    "> You hold the door open for her and you guys part ways. As you're walking you look back to catch her peeking over her shoulders as well. You both wave at each other."
    "> It seems you've managed to get closer to Mary."
   
    #jump return_to_which_day
    jump standard_end_day
 
label cafe_date_badending :
    $ girl1.add_closeness(-1)
    scene bg cafe with fade
    show mary casual sigh with dissolve
    "> You guys finish your food. Mary stands up and looks away."
    show mary casual sad        
    p "Well... have a goodnight."
    hide mary casual sad with dissolve
    "> Mary leaves first and you are left alone. You sit for a moment to avoid getting in her way. As you leave the cafe, she is no where in sight."
    "> You were unsuccessful in this date."
    jump mary_bad_end
    #jump return_to_which_day
   
    #cue bad game ending?
 
   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Mary - Restaurant Date
 
label restaurant_date1: 
    if not rest1_asked2 and not rest1_asked3:
        scene bg restaurant with fade
        "> At the restaurant."
        "> The hostess leads you to your table, and both of you get in each other's way trying to decide where each of you will sit. As you two take your respective seats, you chuckle to each other."
        show mary casual shy with dissolve
        p "Wow, haha.. This place sure is fancy."
        show thought behind mary
        "> Awkward silence follows."
        "> Mary looks a little flustered."
        "> QUICK! SAY SOMETHING TO HER YOU FOOL!"
        hide thought behind mary
    else:
        show thought with dissolve
        m "{i}What else should I ask her?{/i}" 
    menu:
        "You look very pretty today." if not rest1_asked2 :
            $ rest1_asked2 = True
            $ girl1.add_closeness(1)
            $girl1.add_affection(1)
            show mary casual flustered2
            p "O-Oh."
            show mary casual flustered1
            "> Mary blushes and can't seem to look you in the eye. You hope this is a good sign?"
            "> Your compliment doesn't do anything to spark any conversation, rather, she seems even more flustered."
            jump restaurant_date1
        "So what else do you like about cooking?" :
            jump restaurant_date2
           
        "We look like a real couple!" if not rest1_asked2 : #no effect
            $ rest1_asked2 = True
            show mary casual confused
            p "Uhm.."
            "> Mary looks confused."
            show mary casual pout
            p "We're not... Sorry, I just don't think we're on the same page.."
            "> Mary looks a little shy about it but not annoyed or anything. She seems even more flustered than before."
           
            jump restaurant_date1
           
label restaurant_date2:
    if not rest2_asked1:
        show mary casual shy
        "> The corners of her mouth raise ever so slightly, but her eyes wince a little."
           
        p "I've been really curious about ever since I was little. Cooking made me feel some sort of wonder and eventually it just grew into a passion."
           
        "> She shifts her glass back and forth. Her eyes follow the glass. She lets out a shallow sigh."
        show mary casual wonder    
        p "Something about cooking makes me feel unique, you know?"
        show mary casual shy
        p "Haha, sometimes I like to pretend that I'm really good at it. "
        show mary casual pout
        "> Her glass slows down, and her smile fades to concern."
        show mary casual sigh    
        p "But... In the end it's just a hobby..."
    show mary casual sad
    "> Mary becomes silent as her eyes wander down to her glass."       
    menu :
        "> Reassure." if not rest2_asked1: #chance to gain closeness
            $ rest2_asked1 = True
            $ reassure = True
            m "Just a hobby? But you're the president of the cooking club!"
            show mary casual shy
            p "Titles don't really mean a whole lot to me. Besides, you've never even tried my cooking."
           
            menu :
                "> Be bold." : #stat requirement to say? (+2)
                    $ girl1.add_closeness(2)
                    $ girl1.add_affection(2)
                    m "I feel like there's a pretty easy solution to that."
                    show mary casual smile
                    "> Mary leans forward. Her eyes are on you as she smirks."
                    show mary casual happy
                    p "Well don't expect much if I cook all by myself."
                    show mary casual smile
                    m "Haha, I doubt I'll be much help to you. You're on your own!"
                    show mary casual laugh
                    "> The two of you joke together. Mary playfully punches your shoulder as the two of you roll back laughing in your seats."
               
                "> Joke." : #-1
                    $ girl1.add_closeness(-1)
                    m "Yeah I guess. I mean, how many people even ran for president anyway?"
                    show mary casual sad
                    p "Yeah, right..?"
                    show mary casual shy
                    "> Mary forces a smile."
                   
                "> Be polite":
                    m "You've tried mine. We should make something together, and you can teach me a few things."#(+1)
                    $ girl1.add_affection(1)
                    $ girl1.add_closeness(1)
                    show mary casual happy
                    p "Sounds like a fun time. Haha, alright then."
                    show mary casual smile
                    "> Mary smiles as you two think of things to make together."
            show mary casual wonder with fade
            show thought with dissolve
            "> Time passes as the two of you continue to talk."
            show mary casual straight
            "> You notice Mary's gaze getting lost in the distance more frequently."
            hide thought with dissolve
            m "Is something the matter Mary?"
            show mary casual sad
            p "Well.. back when I said that cooking was just a hobby. The reason I said that was.."
            jump mary_backstory2
               
        "> Question." : #backstory opener
            m "It seems like cooking means a lot more to you. You seem upset. What's wrong?"
            jump mary_backstory2
           
label mary_backstory2:
    "> Mary rolls her eyes as she sits back in her chair while letting her posture sink and her sight drops to her glass."
    show mary casual pout
    p "...It's my mom and her opinions towards me wanting to cook."
    show mary casual sigh
    p "I know she means well and it's not like she's being mean about it. I just feel this pressure not to disappoint her. I don't even know why I'm telling you all of this. I've only known you for a couple of days. Sorry."
    m "Honestly Mary, don't worry I'm completely fine with it. Have you ever told her how you feel about cooking?"
    show mary casual wonder
    p "I've sort of suggested being a chef, but she avoids really talking about it much. She redirects the conversation or tells me that {i}\"It would be better to keep it as a hobby.\"{/i}"
    show mary casual sigh
    "> Mary pauses briefly."
    show mary casual sad
    p "... My dad was a chef and bring me into the kitchen and teach me different things about cooking. I really love those moments. It's why I fell in love with cooking."
    m "What about your dad? What does he think?"
    show mary casual sigh
    "> Mary stops for a moment. She takes a prolonged deep breath."
    show mary casual sad
    p "He would have said, “Do it!” He was the nonchalant character that brought life to the family."
    p "My mom and dad were a strange couple and they both worked really hard. It's funny because my mom was the bread-winner, but my dad was the one who baked the bread. Hahaha... But he's not here to say that anymore..."
   
    m "I'm really sorry to hear that..."
    show mary casual shy
    p "Thanks. I was about 14 at the time so I've already come to accept it..."
    show mary casual sad
    p "Dad really loved his work. Sometimes he would spend 16 hours a day at his restaurant. "
    p "The doctors said that he needed to take more breaks or he may suffer from stress, but my dad was the kind of guy who wouldn't accept that."
    p "One day he had a heart attack. It turned out that the stress caused high blood pressure and lead to heart failure."
 
    p "Mom and I were devastated. Cooking for me lets me keep a memory of him living. I think for my mom, seeing me cook, just reminds her of a passion that took dad away."
    show thought with dissolve
    m "{i}What should I say to her?{/i}"
    hide thought with dissolve
    menu: # choices should not decrease stats at this point of date
        "Keep cooking a secret." :
           
            m "You should continue pursuing a professional career to keep your mom happy. But try to keep cooking as a secret hobby for as long as possible so you can keep doing what you love."
            show mary casual shy
            "> Mary smiles a little, but doesn't seem satisfied."
           
            p "Haha, maybe you're right, but having to keep this a secret forever doesn't seem possible."
            show mary casual sad
            "> Mary goes silent for a moment. She doesn't seem to be feeling well."
           
        "Don't listen to your mom." :
            m "It's really considerate of you to try and make your mom happy, but I think you deserve to be happy too, even if it means going against her wishes."
            show mary casual grumpy
            p "But how can I have happiness without my mom's approval? She's still important to me so her wishes are important as well...."
            show mary casual pout
            p "...Sorry. I know you're just trying to help. That means a lot to me. Thanks."
            show mary casual sad
            "> Mary goes silent for a moment."
           
        "Talk to your mom about it.":
            $ girl1.add_closeness(2)
            m "It sounds like you're pretty torn and I think expressing your feelings towards your mom would be a pretty good step forward. She probably wants you to be as happy just as much as you want her to be happy."
            show mary casual straight
            "> Mary looks contemplative. Her expression turns sour."
            show mary casual grumpy
            p "No...I can't. You don't know my mom. She would never understand. This is important to me."
            show mary casual sad
            p "What if I end up losing all of it? I wouldn't be able to..."
           
            "> Mary looks like she's on the verge of tears."
           
            p "..I'm sorry."
    hide mary with dissolve
    show thought with dissolve
    "> You comfort Mary. After a while she seems to recover and insists that she is okay. You both continue talking about different subjects, but she seems distracted."
    hide thought with dissolve
    show mary casual shy
    p "Hey.. thanks for today. I'm glad we got to spend more time with each other. It feels good talking to you about my problems."
    p "Well.. Have a goodnight."
    m "Goodnight."
    hide mary with dissolve
    "> Mary gives you a warm smile before turning around. The two of you part ways in front of the restaurant."
    show thought with dissolve
    m "{i}Was she really okay..?{/i}"
    jump standard_end_day
#    jump return_to_which_day
           
#label restaurant_ending:
#label restaurant_badending:
   
#Mary - Home Date~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
label girl1_home_date:
    scene bg hallway with fade
    show mary casual straight with dissolve:
            xalign 0.7
            linear 1.0 xalign 0.5
    if reassure:
        m "Hey Mary. I remember before you mentioned that I never tasted your cooking. If it's okay with you, I'd really like to try some today."
        show mary casual wonder
        p "Oh! so you did remember!"
    else:
        m "Hey Mary. After all our conversations about cooking, it's surprising that I haven't actually tried any of your cooking yet."
        m "I'd really like to try some as soon as I can."
       
        "> Mary seems surprised as your sudden request."
       
        p "Hmm.. that is true."
        p "How about today then? You're free right?"
       
        m "Of course."
    show mary casual shy    
    "> Mary smiles shyly."
 
    p "Then.. Instead of cooking it here, Why don't we go to my house? There's plenty of ingredients there."
 
    m "S-sure."
   
    "> A nervous tension suddenly fills the air."
    #fade out
    hide mary with dissolve
    scene bg sidewalk with fade
    "> You and Mary head back to her place after club activities. You feel tenser than usual, despite the fact you've recently spent a lot of time with her."
    "> In the corner of your eye you catch her peeking slightly in your direction, but she immediately redirects her vision forward after being noticed."
    show mary casual happy
    p "It's a really beautiful day today isn't it?"
   
    "> It seems that Mary's trying her hardest to cope with the awkwardness."
    hide mary with dissolve
    scene bg outside_house with fade
    "> As you approach her house, your eyes follow her as she leaps ahead."
    #Insert Leapsahead.png
    show leapsahead with fade
    "> She moves forward and her hair swings, pushing its scent towards you."
    "> For a second you get hung on the scent as you're both entering. She turns to notice you."
    scene bg house with fade
    show mary casual wonder with dissolve
    p "You look like you're lost."
 
    m "E-ehh. My bad."
    "> You look around her house, but you are a bit flustered because you don't know how to recover smoothly."
    show mary casual laugh
    p "Hehehe, the kitchen is this way."
    hide mary with dissolve
    "> She leads you into the kitchen and immediately moves along the room in a rehearsed efficiency, preparing her supplies."
    "> You pick up some newspapers in an attempt to help."
    show mary casual shock with dissolve
    p "No, not there!"
    "> She pulls the papers out of your hands and sets them aside. She turns to you."
    show mary casual happy
    p "Alright! Everything is set! What do you want to eat?"
    call girl1_home_date_choice
 
    show thought with dissolve
    "> You look around the room; it's pretty nice. What should you do?"
    hide thought with dissolve
    menu:
        "Sit in the living room and play video games.":
            $ girl1.add_affection(-1)
            show thought with dissolve
            "> You decide to head to the living room to play video games. Unfortunately there is not a game console in sight."
            "> Your impatience gets the better of you and you decide to head back into the kitchen."
            jump girl1_home_date_kitchen
        "Go into the kitchen and offer your assistance.":
            jump girl1_home_date_kitchen
        "Look around for any photo albums that she may have.":
            show thought with dissolve
            "> You stray into the hall and walk along a line of portraits along the wall, many of them focused around Mary as a child."
            "> Many of the photos appear almost bleak, with little expression on her face."
            "> Soccer photos, class photos, academic achievement photos, she hardly ever smiles."
            "> You pick one with her flour all over her face as a kid, her glasses caked in powder. Her smile was the only distinguishable feature."
            hide thought with dissolve
            show mary cook wonder with dissolve:
                xalign 0.2
                linear 1.0 xalign 0.5
            p "..What are you up to?"
            "> Mary peeks in from the kitchen."
            show mary cook shock
            p "Ah! Nooo! That's such an embarrassing picture of me! Don't look!"
            m "Hahaha! I think it's cute."
            show mary cook flustered1
            "> Her cheeks grow red."
            show mary cook flustered2
            p "D-don't say things like that!"
            "> Despite saying that, it was obvious she was forcing herself to hold back her smile."
            show mary cook grumpy
            p "I-I think you should stay put in the kitchen from now on!"
            menu:
                "If you say so.":
                    jump girl1_home_date_kitchen
                    hide thought with dissolve
                "Why is this the only happy photo?":
                    show mary cook wonder
                    p "I don't really know. That was the first time my mom let me bake all by myself. I ended up dropping the flour bag and making a huge mess all over the place."
                    p "As for the other photos, I was just never excited about those things."
                    show mary cook sad
                    p "My mom really wanted me to get good grades so I was told avoid any extra-curricular activity because she felt they would get in the way."
                    p "{i}'Mary, you have to do well so I can get into a good university and find a stable job.'{/i}"
                    p "{i}'Marry a good husband and raise a family.'{/i} I've heard it all.. "
                    show mary cook pout
                    "> Mary seems displeased."
                    menu:
                        "Console.":
                            #Affection up
                            $ girl1.add_affection(1)
                            m "I can tell that your parents really love and care about you. I almost feel like your mom would be more understanding of your current situation if you seriously expressed how passionate you are about cooking."
                            show mary cook shy
                            p "Haha, you really do know what to say.. most of the time."
                            p "C'mon. lets get back to the kitchen."
                        "Hug her.": #IDK WHAT TO DO HERE. EXTRA AFFECTION PTS??
                            #Affection up bonus
                            $ girl1.add_affection(2)
                            "> You wrap your arms around her shoulders."
                            show mary cook confused
                            p "Wha-?!"
                            show mary cook flustered1
                            "> Mary flinches slightly when she realizes what you're doing. However, she doesn't seem to dislike it."
                            "> She begins to settle down. Her arms slowly wrap around your back."
                            "> The two of you stand silently for a while before finally letting go of each other."
                            show mary cook flustered2
                            p "U-uumm... Thank you. Sorry if I made you feel uncomfortable."
                            m "We should probably head back to the kitchen."
                            p "Y-yeah! Of course!"
                    "> Mary grabs on to your arm and brings you back into the kitchen."
                    jump girl1_home_date_kitchen
           
label girl1_home_date_kitchen:
    scene bg house with fade
    show mary cook happy with dissolve:
        xalign 0.8
        linear 1.0 xalign 0.2
        pause 1.0
        linear 1.0 xalign 1.0
        pause 1.0
        repeat
    "> You watch Mary wander back and forth between different areas of the kitchen. Her smile is an obvious sign she's enjoying herself."
    hide mary with dissolve
    m "I can't stand just watching! Let me help you, Mary."
    show mary cook happy with dissolve
    p "Haha. Then.. can you preheat the oven for me?"
    #positive
    show thought with dissolve
    "> You accept and decide to help her where you can."
    "> Mary starts measuring dry ingredients from a flour bag."
    hide thought with dissolve
    show mary cook wonder
    p "Ah! Can you handle the wet ingredients while I do this?"
    "> The two of you watch as the parts slowly come together. You feel her elbow brushes against yours every now and then."
    show mary cook shock
    p "Sorry!"
    show mary cook pout
    "> She looks up at you for a brief moment and catches your gaze."
    m "Don't apologize. It's alright."
    show mary cook shy
    "> Her eyes widen slightly, but immediately her face turns back to focus on the preparations."
    "> You notice a bead of sweat trail down from her temple to the front of her neck. Her cheeks flooded with red."
    "> A sense of nervousness and excitement fills your mind. Your breathing becomes shallow."
    show mary cook flustered2
    p "Uhh.. It's getting a little warm in here. How hot did you preheat that oven exactly?"
    show mary cook flustered1
    "> Mary turns to the oven."
    show mary cook flustered2
    p "Oh! 350 degrees. Perfect! Uhhm.. I guess the weather is pretty warm today."
    "> Frantically, she tries to clear her sweat, however she knocks the bowl of flour off the counter top."
    show mary cook shock
    p "OH NO!"
    hide mary with dissolve
    "> You manage save the bowl, however all the flour that was in it is now spread across the floor."
    menu:
        "Somebody's got a lot of cleaning to do...":
            #negative
            $ girl1.add_affection(-1)
            show mary cook confused with dissolve
            p "Just get me more flour."
            "> After clearing the mess, you head into the pantry and find an extra-large bag of flour up on the top shelf."
        "Don't worry! I'll grab you some more flour.":
            #positive
            $girl1.add_affection(1)
            show mary cook laugh with dissolve
            p "Haha. So dependable."
            "> After clearing the mess, you head into the pantry and find an extra-large bag of flour up on the top shelf."
            hide mary with dissolve
    show thought with dissolve    
    "> The two of you struggle with the heavy bag as you try to get it. The shifting of the bag causes it to tip over."
    "> Unable to realize that the top of the bag was unsealed, a torrent of flour rains down and covers both your faces."
    m "You got some... Umm.. flour all over you."
 
    #says both of you have flour all over your faces , but u only wipe off hers . Maybe put a text saying u wipe your face first
    "> You brush the flour off her shoulders, trying to avoid making awkward physical contact."
    p "Well... I could only assume. My lenses are completely covered. I can't see a thing."
               
    m "Here I got it for you."
    hide thought with dissolve
    #Insert flour image
    show mary_flour with fade
    "> You lean in closer as you lift the frames off her eyes."
    "> Her brown eyes fixated on you. Unprepared, you find your faces lingering mere inches apart."
 
    menu:
        "{b}JUST DO IT!!{/b}":
            "> You decide to take the relationship further."
            "> You wipe the flour off her cheeks and find your hands resting on the back of her neck."
            "> Before you know it, your hand pulls her towards you. As anticipation is building, you close your eyes."
            "> ..."
            "> ... You feel something press against your lips..."
            "> ..."
            "> Something doesn't feel right..."
            "> As you open your eyes you find your mouth, cupped by her hand."
            #SPLIT HERE BASED ON AFFECTION
            #change back to kitchen scene
            hide mary_flour with fade
            if girl1.affection >= 5:
                show mary cook smile with dissolve
                "> Mary's eyes still wide open, smiling."
                show mary cook happy
                p "I may not be able to see that well without glasses, but I'm not blind."
                show mary cook shy
                p "Don't get me wrong, I can't deny that I have feelings for you, but let's take it slow."
                "> She lifts your hands off of her, she holds you palm open and examines it. You both turn slightly towards the counter to face shoulder to shoulder."
                "> Still examining your hand, she places her hand on top of your's as if comparing hand sizes."
                #Insert hand image
                show hands with fade
                p "You know, you have pretty soft hands. I think I'll hold on to them for a while."
                "> Both your hands begin to offset a little. You decide not to resist and allow your fingers to interlock."
                jump mom_drama
               
            else:
                show mary cook sad with dissolve
                "> Mary's eyes are half-opened. A look of regret covers her face."
                p "..."
                p "... I can't... I'm sorry..."
                show mary cook pout
                m "..Oh.."
                "> You find yourself lost for words."
                "> Your silence divides you."
                show mary cook flustered2
                p "Hmm... You see.. I'm really sorry. I can't really find enough reason to see you the same way. That's why I can't return your feelings. We're just not at that level."
                show mary cook flustered1
                "> You feel your chest compressing, as if the inside of your ribcage is caving in."
                m "Yeah.. I think I understand."
                show mary cook sad
                p "At least we had fun together..."
                m "..."
                p "A relationship right now would be too distracting for me.... "
                p "Also.. I need to focus on other things, like school..."
                p "...It's going to be hard to go back to the way things were before."
                m "... Yeah."
                "> You both get up."
                "> You feel as if your legs are about to give out. "
                m "I should probably go..."
                p " ...Yeah."
                hide mary with dissolve
                show thought with dissolve
                scene bg outside_house with fade
                "> Mary leads you to the exit. You can't think of much to say without making it more awkward, so you just keep walking."
                "> You look back. The door is closed."
                m "{i} I guess that's it, huh...? {/i}"
               
                jump mary_bad_end
                #return
               
label girl1_home_date_choice:
    menu:
        "Deep-fried sushi" :
            show mary casual wonder
            p "Wow! Your taste is pretty extravagant, huh?"
            menu:
                "You don't have to cook it if you don't want to.":
                    show mary casual grumpy
                    p "You don't think I can do it?"
                    p "I'll prove you wrong."
                    "> Mary seems motivateds all of a sudden."
                    #negative
                " I really want to eat this.":
                    show mary casual shy
                    "> Mary seems intimidated by the challenge but finds her resolve."
                    p "I'll do my best!"
                    "> Mary seems motivateds all of a sudden."
                    #positive/neutral
        "Instant noodles":
            show mary casual grumpy
            p "C'mon..are you taking my offer seriously here?"
            $ girl1.add_affection(-1)
            call girl1_home_date_choice
            return
        "Triple Layer Chocolate Cake":
            show mary casual wonder
            "> She seems surprised by your request"
 
            p "I thought you'd choose something more difficut. Why did you choose a cake?"
            menu:
                "I didn't want you to work too hard.":
                    show mary casual happy
                    p "What? Don't worry so much...I can handle it. But alright, I'll make the cake if that's what you want."
                "So we can share it when you're done.":
                    show mary casual laugh
                    p "Haha, Are you usually this corny? But alright, if that's what you want."
                    #neutral
                "It has a special meaning.":
                    $ girl1.add_affection(1)
                    p "Meaning?"
                    show mary casual straight
                    m "Yeah. Each layer of the cake represents each place we've spent time together and how far we've come building on our relationship. One layer at a time."
                    show mary casual laugh
                    "> Mary's face turns red as she tries hard to hold back her laughter."
                    p "Were you always this corny?"
                    "> Mary seems pleased by your thought."
                    show mary casual happy
                    p " Alright, I'll get started then."
 
                    #positive
    hide mary with dissolve
    "> Mary begins cooking the dish and you're left sitting in her living room alone."
    return
   
label mom_drama:
    #mom drama stuff
    scene bg house with fade
    show thought with dissolve
    "> You hear the door bell ring. An unfamiliar voice calls from the door."
 
    mom "Hey Mary, I'm home from my business trip!"
    hide thought with dissolve
    show mary cook shock with dissolve
    p "What?! She's home a day early! Why?!"
   
    "> Mary looks around at all the cooking equipment and ingredients splayed out on the counters and looks helpless."
    "> She's visibly panicking and attempts to make a move to put things away, but it's futile. "
    hide mary with dissolve
    show mom 3 with dissolve
    "> You don't have much time to react before her mom comes into the kitchen."
   
    "> Her mom spots you."
    show mom 2
    mom "Who is this, Mary? Why are you guys alone together?"
    show mary cook flustered2 at left
    show mom 3
    p  "Uh, this is my friend, %(player_name)s. We are just hanging out after school mom. That's all.."
    show mom 7
    show mary cook flustered1 at left
    mom "You shouldn't be inviting people over when I'm away on a business trip. Shouldn't you be studying too? It's a school night!"
    show mom 9
    show mary cook flustered2 at left
    p "I-I just wanted to relieve some stress. It's just a little bit of cooking."
    show mary cook flustered1 at left
    "> The tension is getting heavy as you stand there as if you are not even in the room."
    show mom 7
    mom "Mary, you should be using your time more wisely. What happen to the money I gave you to buy food with? You should be focusing on getting into university so you can get a career."
    "> Mary's mom's eyes turn to the kitchen counter."
    mom "What is all this doing out here?"
    show mary cook sad at left
    show mom 9
    "> Mary's mom gestures to all of the equipment and ingredients out in the open."
    "> Mary's face is flushed of all its color and her voice is small."
    p " I didn't use the money; it's still in your office. As for all of this...I-  What if I wanted to be a chef? ...Like dad?"
    show mom 5
    "> Her mom is taken aback for a moment but then her voice is heightened."
    show mom 12
    mom "Don't you remember what happened to your father? Why would you do this? I can't let that happen to you, Mary, I can't lose both of you like that."
    show mom 11
    p "But.."
    "> Mary looks down and appears defeated."
    show mom 7
    mom "No buts! Don't try to argue with me. Escort your friend out and then go to your room."
    show mary cook cry at left
    show mom 9
    "> Mary turns to you with some tears escaping her eyes and falling down her cheeks."
    p "I'm sorry %(player_name)s... I'm sorry about all of this.. Can you please leave?"
    menu:
        "Leave the house":
            show thought with dissolve
            "> You stand there for a moment and Mary's look of disappointment and sadness is enough to tell you to that you've failed."
            "> You move your legs mechanically out of the kitchen and out of the house."
            "> You tried your best but it wasn't enough. You probably won't be able to spend as much time with Mary anymore..."
            hide thought with dissolve
            jump mary_bad_end
            #replace return with jump to game over screen
        "Confront Mary's mom":
            show mom 9
            "> You gather all the courage you can muster and take a purposeful step forward as you look at Mary's mother in the eye."
            m "I'm sorry. I can't leave like this."
            show mom 7
            mom "What? How dare you! This is my house."
            show mary cook shock at left
            show mom 9
            "> Mary looks shocked."
            p "%(player_name)s?"
            show mary cook pout at left
            m"Hear me out, please. Mary told me about what happened with her father. It must've been terrible. Judging by the way Mary talked about him, it sounded like both of you must have loved him very much."
            "> Her mom seems agitated by a stranger bringing up family matters and she snaps at you."
            show mom 8
            mom "What of it?"
            show mom 9
            show mary cook cry
            show thought with dissolve
            "> Mary's mom's eyes are full of anger and at the same time hurt. You feel beads of sweat forming on your neck as you feel the pressure. "
            "> Your resolve is cracking under the weight of her glare and aura."
            "> You glance over to Mary, whose eyes are wide and full of tears. "
            "> Seeing Mary strengthens your resolve and you look back to her mom."
            menu:
                "Ease into it":
                    hide thought with dissolve
                    m "Well..I think there's a misunderstanding between you and Mary right now...You're not really on the same page. "
                    show mom 8
                    mom "What are you saying? You think you know my daughter more than I know her? I've raised her and I know what's best for her."
                    show mom 9
                    m "I'm not saying that I know her more..I just mean.."
                    show mom 7
                    mom "Who do you think you are?"
                    show thought with dissolve
                    m "{i}This isn't going so well...{/i}"
                    menu:
                        "Talk about Mary's Dad":
                            hide thought with dissolve
                            show mom 9
                            m "I'm sure you remember your husband's passion for cooking! It made him happy and it made Mary happy too!"
                            show mom 7
                            mom "Don't act like you know everything. He's gone now because of that passion. He's gone so I can only look after Mary and her well-being now."
                            show mom 9
                            m "..."
                            show mom 8
                            show mary cook sad
                            mom "You might mean well, but please. You're not helping anyone here. Bringing up past pain will not help Mary now. Just leave."
                            show thought with dissolve
                            "> You stand there for a moment and Mary's look of disappointment and sadness is enough to tell you that you've failed."
                            "> You move your legs mechanically out of the kitchen and out of the house."
                            hide thought with dissolve
                            hide mary with dissolve
                            scene bg outside_house with fade
                            "> You've tried your best but it wasn't enough."
                            "> You probably won't be able to spend as much time with Mary anymore.."
                           
                            jump mary_bad_end
                            #jump bad ending
                        "Talk about Mary":
                            hide thought with dissolve
                            jump be_blunt
                "Be blunt":
                    hide thought with dissolve
                    jump be_blunt
               
           
label be_blunt:
   
    m " To be straightforward, Mary's the president of the cooking club at school and she's been cooking for a long time behind your back."
    "> Mary's mom sharply turns to Mary in disbelief and Mary cowers even more."
    show mary cook shock at left
    p "%(player_name)s!! Mom it's not what you think, mom..."
    show mary cook pout at left
    m "It's exactly how it looks."
    show mom 12
    mom "Mary..Why haven't you been listening to me? You know exactly why I forbid you to cook."
    show mom 11
    m "She does it because it's her passion."
    m "A passion that was fostered by your husband. She does it to honor him and ultimately, because it makes her happy. Is that really so bad?"
    show mom 9
    "> Mary's mom stares at you for a moment."
    show mom 8
    mom "Do you think I don't know what's best for my own daughter?"
    show mom 9
    m "Please, I'm not trying to undermine you or your ideals."
    m "But I think it'd be great for both you and Mary if you would even just consider the idea of letting her cook as a hobby and potentially even going further as a career."
    show mom 11
    mom "She..she can't. Or else she'll end up just like her father."
    show mom 12
    "> Her eyes seem less hard now, and more sad."
    m "In some ways. She'll definitely be happier. More passionate. I can see why you worry about her...I do too."
    "> You look over at Mary again and your eyes lock. She smiles a little bit."
    m" But you should trust her to know her limits - I know I've come to."
    m "She's smart, she's reasonable. she knows her abilities and her talents. Honestly, she's great. Limiting her is putting on more stress than not. "
    "> Mary's mom is silent. She then looks over to Mary."
    show mom 11
    mom "Is..all of this true?"
    show mom 12
    show mary cook sad at left
    p "Yes, mom...I've always loved cooking and I haven't stopped even if dad has died."
    p "I'm sorry..I never wanted you to find out like this.."
    mom "..."
    p "Please mom..This is what I really want to do. I know you loved dad because he was very passionate as well.."
    "> Mary's mom looks away from the both you and Mary."
    show mary cook pout at left
    show mom 6
    mom "I didn't mean to drive a wall between us. You really kept all of this a secret from me?"
    show mom 5
    show mary cook cry at left
    p "I was too scared..I didn't want to hurt you too. But this is who I am.."
    "> Mary's mom turns around and embraces Mary."
    show thought with dissolve
    mom "I'm sorry."
    "> It seems like she's unable to say anything else as her voice starts wavering. Mary is crying too."
    "> You decide that you shouldn't intrude and you leave the room."
    "> ..."
    hide thought with dissolve
    hide mary with dissolve
    hide mom with dissolve
    scene bg outside_house with fade
    "> Time passes as you wait outside. You wonder if you could have said anything else, but it's up to Mary now."
    "> After a while, the door opens behind you and you turn to see Mary coming out."
    show mary cook sigh with dissolve:
        xalign 0.8
        linear 1.0 xalign 0.5
    m "Hey. You okay?"
    show mary cook shy
    "> Mary nods and a huge smile breaks out on her face."
    show mary cook happy
    p "She's letting me continue to cook! Can you believe it?"
    p "We talked it over and she's letting me have my shot at being a chef like my dad! She said I had to keep my grades up but that's all fine."
    show mary cook laugh
    p "I'm so glad! It's all thanks to you, %(player_name)s. You stood up for me."
    m "I wanted to protect you."
    show mary cook smile
    "> Mary smiles even more and hugs you."
    p "I'm so thankful for you..thank you so much.."
    "> You give her a hug back and you both relish in each other's happiness."
    jump mary_good_end
 
 
#Endings ================================================================================================================================================================================
label mary_good_end:
    scene bg home_ec_room with fade
    ">At school."
    "> The next day you run to the home-ec room, hoping to find your girlfriend."
    "> You open the door to find her making preparations for todays club meeting."
    show mary casual shock with dissolve
    p "Oh! You scared me. Why are you here so early?"
    m "Haha. I couldn't wait to see you."
    show mary casual shy
    "> The two of you decide to keep each other company until the morning bell rings."
    "> Before you both depart to your own separate classes, you give her a hug. "
    "> As you draw back, she lingers in your arms for a bit and looks up at you."
    "> You look into her eyes and you can't help but lean in. Surprisingly, her eyes close."
    hide mary with dissolve
    show mary_kiss with fade
    #INSERT KISS-KISS
    "> ..."
    hide mary_kiss with dissolve
    scene bg hallway with fade
    show thought with dissolve
 
    "> Days pass and your relationship with Mary continues to prosper."
    scene mary grad with fade
    "> You enjoy the rest of your high school life together with your girlfriend."
    "> Congratulations %(player_name)s!"
    jump credit
    #game end
    #return #to end game
   
label mary_bad_end:
    scene bg home_ec_room with fade
    "> At school the next day."
    "> You decide to check the home-ec room, but there's no sign of Mary."
    "> It seems you weren't too successful in building your relationship..."
    "> ..."
    scene bg hallway with fade
    show thought with dissolve
    "> Days pass and you're unable to bring yourself to even see her. Eventually you give up all together."
    "> You spend the rest of your normal high school life single, working hard to secure your future career."
    "> Who knows? Maybe it'll be better after highshool...?"
    "> Better luck next time, %(player_name)s."
    jump credit
    #return #to end game

label credit:
    #show ending credit/references
    #pause for 120 seconds
    scene bg hallway with fade
    show text "The End." with dissolve
    hide text with dissolve
    scene credits with fade
    $renpy.pause(120.0)
    $renpy.quit(True)
    


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
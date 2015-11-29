#Mary only
#This code will cycle through the 5 day limit between mary events.
#day count is reset to 1 once event is triggered.
define standard_dc = 0 #hidden day counter for day cycles. NOT the same as days passed

label standard_day_cycle: 
    #"TEST LINE"
    if standard_dc < 5: #run normal day events. Once special event triggers, reset count.
        scene bg hallway with fade
        "> Next morning."
        m "Another day at school..."
        scene bg classroom with fade
        if standard_dc == 0:
            "> Morning classes seem getting any easier for you."
        elif standard_dc == 1:
            "> You feel you're slowing getting more used to school life."
        elif standard_dc == 2:
            "> You decide to come to morning classes fully prepared today."
        elif standard_dc == 3:
            "> The morning lectures today seemed almost too easy for you."
        elif standard_dc == 4:
            "> You felt that it would be good to take a short nap during morning classes today."
            "> You feel you have yet to make any progress in your relationship."
        scene bg hallway with fade
        "> Afternoon."
        m "Alright, time for afternoon classes."
        $ stats.reset_classes()
        call make_schedule
        scene bg hallway with fade
        if standard_dc == 0:
            show thought with dissolve
            m "{i}Maybe I should drop by the club room. Mary might be there too.{/i}"
            hide thought with dissolve
        else:
            show thought with dissolve
            m "{i}Time to go to the club room.{/i}"
            hide thought with dissolve
        if girl1.closeness < 0:
            jump girl1_time_passed
        if girl1.closeness < 2:
            m "Mary seems more distant.. I should really get my act together."
        jump standard_home_ec        
        
    else: #too much time passed. Trigger bad end
        scene bg hallway with fade
        "> Next morning."
        m "Another day at school..." 
        scene bg classroom with fade
        "> Morning classes are the same as usual. You can't help but feel that you're forgetting somethhing."
        scene bg hallway with fade
        m "What should I take in the afternoon today?"
        $ stats.reset_classes()
        call make_schedule
        jump girl1_time_passed
    
label standard_home_ec:
    call girl1_check_1
    call girl1_check_2
    call girl1_check_3
    $ closeness = girl1.get_closeness("Mary")
    $ str_check = stats.get_stats("str")
    $ int_check = stats.get_stats("int")
    $ cha_check = stats.get_stats("cha")
    scene bg home_ec_room with fade
    if closeness < 1: #Closeness too low. Add dialogue and trigger bad ending
        jump girl1_failure
    show mary cook wonder with dissolve:
        xalign 0.7
        linear 1.0 xalign 0.5
    p "Is everyone here now? Alright! Pick a recipe and let's start cooking!"
    hide mary with dissolve

    "> There are 3 different recipes on the counter."
    m "Which one should I make today?"
    if standard_dc == 0: 
        menu:
            "Blueberry Muffins (No requirements)":
                scene bg home_ec_room with fade
                "> The muffins turned out great!"
                show mary cook happy with dissolve
                p "Wow! They're so fluffy!" 
                show mary cook laugh
                p "The top is so crisp too. Good job!"
                $ girl1.add_closeness(1)
                
            "Crème brûlée  (Need: 2 Intelligence  & 2 Charm)":
                scene bg home_ec_room with fade
                if int_check >= 2 and cha_check >= 2:
                    # sucess
                    "> The crème brûlée  looks great! nice golden caramelize on it! Looks delicious!"
                    show mary cook laugh with fade
                    p "Looks great. I'm impressed."
                    $ girl1.add_closeness(3)
                else:
                    # failure
                    "> The vrème brûlée  turned out completely black... You think that you burnt it..."
                    show mary cook pout with fade
                    p "Uhh... is this even edible?"
                    $ girl1.add_closeness(-3)
                    
            "Lasagna (Need: 2 Strength & 1 Charm)":
                scene bg home_ec_room with fade
                if str_check >= 2 and cha_check >= 1:
                    "> The lasagna turned out great! The cheese is perfectly melted."
                    show mary cook happy with fade
                    p "The Lasagna looks awesome! The layers look so even!"
                    $ girl1.add_closeness(2)
                else:
                    "> You reach into the oven and pull out what looks like a pile of plain pasta."
                    show mary cook wonder with fade
                    p "I think you didn't use enough tomato sauce... it looks pretty dry."
                    $ girl1.add_closeness(-2)
        
    elif standard_dc == 1:
        menu:
            "Cinnamon Buns (No requirements)":
                scene bg home_ec_room with fade
                "> The Cinnamon Buns turned out great! The icing looks shiny and delicious!"
                show mary cook laugh with fade
                p "Looks so good! Can't wait to try it."
                $ girl1.add_closeness(1)
            
            "Assorted Sashimi (Need: Intelligence 3 & Strength 3)":
                scene bg home_ec_room with fade
                if int_check >= 3 and str_check >= 3:
                    "> The sashimi is perfectly sliced."
                    show mary cook happy with fade
                    p "Wow! Looks so good I almost don't want to eat it!"
                    $ girl1.add_closeness(3)
                else:
                    "> The slices turned out oddly-shaped and uneven. You see pieces of bones and scales mixed in with the fish."
                    show mary cook pout with fade
                    p "Uhh... It's okay. We can always get some more expensive fish."
                    $ girl1.add_closeness(-3)
                    
            "Carbonara (Need: Strength 2 & Charm 2)":
                scene bg home_ec_room with fade
                if str_check >= 2 and cha_check >= 2:
                    "> The pasta turned out perfectly cooked! The aroma of the sauce fills the air."
                    show mary cook laugh with fade
                    p "That smells so good!"
                    $ girl1.add_closeness(2)
                else:
                    "> The pasta looks like a pile of mush..."
                    show mary cook sigh with fade
                    p "I think the pasta is way too overcooked..."
                    $ girl1.add_closeness(-2)
   
    elif standard_dc == 2:
        menu:
            "Mac and Cheese (No requirements)":
                scene bg home_ec_room with fade
                "> The cheese is perfectly melted and crisp on the surface of the casserole dish."
                show mary cook laugh with fade
                p "I can't wait to try this! Looks fantastic!"
                $ girl1.add_closeness(1)
                
            "Beef Stroganoff (Needs: Strength 4 & Charm 4)":
                scene bg home_ec_room with fade
                if str_check >= 4 and cha_check >= 4:
                    "> The pasta turned out perfectly cooked! The aroma of the sauce fills the air."
                    show mary cook happy with fade
                    p "That smells so good!"
                    $ girl1.add_closeness(2)

                else:
                    "> The pasta looks like a pile of mush..."
                    show mary cook wonder with fade
                    p "I think the pasta is way too overcooked..."
                    $ girl1.add_closeness(-2)
                    
            "Lemon Meringue Pie (Need: Intelligence 3 & Charm 3)":
                scene bg home_ec_room with fade
                if int_check >= 3 and cha_check >= 3:
                    "> The pie is firm and the meringue keeps it's form."
                    show mary cook laugh with fade
                    p "Wow! The browning of the meringue is beautiful!"
                    $ girl1.add_closeness(2)
                else:
                    "> The filling is too liquidy; it will not hold its shape."
                    p "I think that you overbaked the pie."
                    $ girl1.add_closeness(-2)
   
    elif standard_dc == 3:
        menu:
            "Blueberry Muffins (No requirements)":
                scene bg home_ec_room with fade
                "> The muffins turned out great!"
                show mary cook happy with dissolve
                p "Wow! They're so fluffy!" 
                show mary cook laugh
                p "The top is so crisp too. Good job!"
                $ girl1.add_closeness(1)
                
            "Crème brûlée  (Need: 2 Intelligence  & 2 Charm)":
                scene bg home_ec_room with fade
                if int_check >= 2 and cha_check >= 2:
                    # sucess
                    "> The crème brûlée  looks great! nice golden caramelize on it! Looks delicious!"
                    show mary cook laugh with fade
                    p "Looks great. I'm impressed."
                    $ girl1.add_closeness(3)
                else:
                    # failure
                    "> The crème brûlée  turned out completely black... You think that you burnt it..."
                    show mary cook pout with fade
                    p "Uhh... is this even edible?"
                    $ girl1.add_closeness(-3)
                    
            "Lasagna (Need: 2 Strength & 1 Charm)":
                scene bg home_ec_room with fade
                if str_check >= 2 and cha_check >= 1:
                    "> The lasagna turned out great! The cheese is perfectly melted."
                    show mary cook happy with fade
                    p "The Lasagna looks awesome! The layers look so even!"
                    $ girl1.add_closeness(2)
                else:
                    "> You reach into the oven and pull out what looks like a pile of plain pasta."
                    show mary cook wonder with fade
                    p "I think you didn't use enough tomato sauce... it looks pretty dry."
                    $ girl1.add_closeness(-2)
   
    elif standard_dc == 4:
        menu:
            "Cinnamon Buns (No requirements)":
                scene bg home_ec_room with fade
                "> The Cinnamon Buns turned out great! The icing looks shiny and delicious!"
                show mary cook laugh with fade
                p "Looks so good! Can't wait to try it."
                $ girl1.add_closeness(1)
            
            "Assorted Sashimi (Need: Intelligence 3 & Strength 3)":
                scene bg home_ec_room with fade
                if int_check >= 3 and str_check >= 3:
                    "> The sashimi is perfectly sliced."
                    show mary cook happy with fade
                    p "Wow! Looks so good I almost don't want to eat it!"
                    $ girl1.add_closeness(3)
                else:
                    "> The slices turned out oddly-shaped and uneven. You see pieces of bones and scales mixed in with the fish."
                    show mary cook pout with fade
                    p "Uhh... It's okay. We can always get some more expensive fish."
                    $ girl1.add_closeness(-3)
                    
            "Carbonara (Need: Strength 2 & Charm 2)":
                scene bg home_ec_room with fade
                if str_check >= 2 and cha_check >= 2:
                    "> The pasta turned out perfectly cooked! The aroma of the sauce fills the air."
                    show mary cook laugh with fade
                    p "That smells so good!"
                    $ girl1.add_closeness(2)
                else:
                    "> The pasta looks like a pile of mush..."
                    show mary cook sigh with fade
                    p "I think the pasta is way too overcooked..."
                    $ girl1.add_closeness(-2)
        
    else: #Extra just in case. Shouldn't get past standard_dc == 4
        menu:
            "Mac and Cheese (No requirements)":
                scene bg home_ec_room with fade
                "> The cheese is perfectly melted and crisp on the surface of the casserole dish."
                show mary cook laugh with fade
                p "I can't wait to try this! Looks fantastic!"
                $ girl1.add_closeness(1)
                
            "Beef Stroganoff (Needs: Strength 4 & Charm 4)":
                scene bg home_ec_room with fade
                if str_check >= 4 and cha_check >= 4:
                    "> The pasta turned out perfectly cooked! The aroma of the sauce fills the air."
                    show mary cook happy with fade
                    p "That smells so good!"
                    $ girl1.add_closeness(2)

                else:
                    "> The pasta looks like a pile of mush..."
                    show mary cook wonder with fade
                    p "I think the pasta is way too overcooked..."
                    $ girl1.add_closeness(-2)
                    
            "Lemon Meringue Pie (Need: Intelligence 3 & Charm 3)":
                scene bg home_ec_room with fade
                if int_check >= 3 and cha_check >= 3:
                    "> The pie is firm and the meringue keeps it's form."
                    show mary cook laugh with fade
                    p "Wow! The browning of the meringue is beautiful!"
                    $ girl1.add_closeness(2)
                else:
                    "> The filling is too liquidy; it will not hold its shape."
                    p "I think that you overbaked the pie."
                    $ girl1.add_closeness(-2)
                
    p "Good work everyone! That's enough for today."
    "> You clean up your supplies and decide to head home for the day."
    jump standard_end_day
    
label standard_end_day:
    scene bg player room with fade
    "> Inside your room."
    # show image of bedroom at night?
    #"THIS IS A TEST LINE. GAME ENTERED CYCLE" #Delete after testing
    if standard_dc == 0:
        m "That was a long day; it's time to hit the sack."
    elif standard_dc >3:
        m "{i} I hope I can get closer to Mary tomorrow...{/i}"
    else:
        m "Time to sleep. I've got another day of school tomorrow."
    $stats.increment_days()
    $standard_dc += 1
    jump standard_day_cycle
    
label girl1_time_passed: #Ending that triggers when the player waits too long
    "> You head over to the home ec room and expect to see Mary working where she usually is. You don’t see her." 
    "> You wait for almost half an hour, but she still doesn’t show up. You leave the room to go home, a little worried." 
    "> Next day."
    "You arrive at school, but just before your first class starts, you are called to the principal’s office." 
    principal "Hello again, %(player_name)s. How are you doing this morning?...Well I’ll just get straight to the point." 
    principal "I understand that you joined the cooking club? I’m afraid to tell you that the club will be cancelled until further notice."
    m "What happened?"
    principal "Unfortunately, Mary, the president of the club, won’t be able to run the club anymore due to illness." 
    principal "Apparently, she was under a lot of stress. I’m sorry about this, %(player_name)s. "
    principal "Hopefully you can still enjoy the rest of your year here." 
    "> You leave the office feeling a little numb. You wonder if you could’ve done anything to help Mary." 
    "> Regretfully, you go with the rest of your day with less energy than usual."
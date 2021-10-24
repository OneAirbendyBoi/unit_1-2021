import sys
global name
import time
import os
def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))

def death():
    delay_print("You Died! Game Over")
    quit()

def dummy():

   return("hey you, it says yes or no, get it right!\n")



def intro():

    score = 0
    start_time = time.time()
    delay_print("Darkness...\n")
    time.sleep(5)
    delay_print('''In the pure void that is space, you would think that in the year 4XXX,
       there wouldn't be too much left to be seen in the universe.\n''')
    delay_print(f'''Millions have been all around the galaxy, and in its review by \x1B[3mThis Eon in Entertainment\x1B[0m it was described as,
       "The most boring place to go on vacation since Palm Springs,California.\n"''')
    os.system("clear")
    delay_print("However, little did they know, space was about to become a lot more interesting...\n")
    os.system("clear")
    time.sleep(5)
    delay_print("A small light flashes in the distance, and within seconds, a small food skiff comes into view, on the way to serve \n")
    delay_print('''their specialty, blarg al la mode, to the busy sla-, err office workers 
             of the tiny moon Nurdhaus for their bicentennial lunch break\n''')

    delay_print('''Here we find our daring protagonist, battling fiercely, trusty peeler in hand, 
             struggling against your greatest adversary to date:\n''')
    time.sleep(3)
    delay_print("the potato.\n")
    time.sleep(3)
    delay_print("Your hand slips off the iron skin of the steadfast spud, causing you to slice off the skin of your finger.\n")
    delay_print('''As our hero whines like a baby over a little scratch, the rest of your arm whips around, 
             trying to wipe away the pain.''')
    delay_print("Its only then that the tattoo on your arm becomes visible. It contains your age, blood type and name... \n")
    os.system("clear")
    name = input("What's your name again? ")
    delay_print(f"Are you sure {name} is your name?\n")
    rusure = input("Is it?:")
    if rusure == "yes":
        with open("database.txt", "a") as file:
            file.write(f"{name},{time},{score}\n")
        score += 50
    else:
        if rusure == "no":
            delay_print("Final Chance!")
            name = input("insert name here:")
            delay_print(f"Are you sure {name} is your name?")
            rusure = input("Is it?:")
            if rusure == "yes":
                with open("database.txt", "a") as file:
                    file.write(f"{name},{time},{score}\n")
                score += 50
            else:
                death()

    delay_print(f"Ok, so you...{name}, yeah {name}... you know what? no more second person, only third person, alright {name}? \n")
    yn = input("yes or no")
    if yn == "yes":
        delay_print("Sweet, alright then!\n")
        score += 50
    else:
        delay_print("Too Bad!\n")
    os.system("clear")
    delay_print(f"Alright! Where were we? Right! yo-{name} is whining about slicing the skin off their finger, awww boohoo \n")
    delay_print('''The relinquished root rattled round the floor, hitting a button labeled 'Fire Alarm.'
     (which for some reason was on the floor as opposed to a wall or something)\n''')
    delay_print('''Suddenly, the entire interior of the ship lit up bright red, and a robotic voice over the PA system 
     yelled at everyone calmly,\n''')
    os.system("clear")
    delay_print(''' "MAYDAY MAYDAY, FIRE ONBOARD, EMERGENCY PROTOCOLS INITIATED, NEAREST LANDMASS FOR LANDING: D'ZHANGO'O"\n''')
    delay_print(f'''The skiff pitches forward and rockets into the atmosphere of the foreign planet, and before our intrepid hero blacks out 
    they think to themselves,"Man, I knew putting the button on the floor so I could hang up that poster was a bad idea... \n''')
    time.sleep(6)
    os.system("clear")

    delay_print(f'''
 )   ___    ____  ___) _____   _____     ______) _____) _____       _      
(__/_____) (, /   /   (, /  | (, /   )  (, /   /       (, /   )   / /      
  /          /---/      /---|  _/__ /     /    )__       /__ /     /    '  
 /        ) /   (__  ) /    |_ /       ) /   /        ) /   \_    /     '  
(______) (_/        (_/     ) /       (_/   (_____)  (_/         /        
Asterodeo\f''')
    delay_print(f'''{name} snaps awake. Around them lies the remains of the ship and crew. 
        "Man, why did we install emergency protocols if the ship couldn't handle them?, they think. They shrug it off.\n''')
    delay_print(f'''After clearing the debris from around them and making it out the carcass of the once mediocre truck,
        {name} looks around, barely noticing the arid desert surrounding them in all directions\n''')
    delay_print('''Finally, they notice\n''')
    delay_print('''"Man, this desert is hot," they finally remark\n''')
    delay_print('''after spinning in circles for a few minutes they finally stand still, noticing the big neon sign that says,
         ASTERODEO SALOON: 1 MI"\n''')
    delay_print('''Hey, by the by, the tutorial is over, so get ready for the actual game, prepare to look around, 
        there may be items to find that will be important for the future! (P.S. get a paper and pen out, I couldn't really 
         figure out the inventory system, so write what items you find down!)\n''')
    travel = input("What will you do? ")
    while travel not in ("walk to saloon", "walk to asterodeo","travel to saloon","travel to asterodeo"):
        if travel in "inspect land" "look around":
                delay_print('''In the arid wasteland that is D'zhango'o, all you see around you are a few tumbleweeds, 
                the debris of your old ship, and the flashing neon sign. In the distance you hear some twangy music and a big ball of dust.
                 A long strip of highway goes from the sign to the ball of dust.\n''')
                score += 50
                travel = input("What will you do? ")
        elif travel in "look at ship" "inspect ship" "look at skiff" "inspect skiff":
            delay_print(f'''{name} peers into the massive crater on the roof, and sees the mangled body of their once menacing shift leader below.\n''')
            delay_print(f'''climbing in to observe the damage, {name} notices a small golden 20 sided die that fell out of the
                  shift leader's pocket.\n''')
            score += 50
            pickup = input("pick it up?")
            if pickup == "yes":
                    delay_print(f"Sweet! {name} got the die! Don't forget to write that down!\n")
                    score += 100
            elif pickup == "no":
                    delay_print(f"{name} leaves the die behind\n")
            else: delay_print(dummy())
            score -= 10
            delay_print(f"{name} also finds a half empty bottle of water and a can of SPAN.\n")
            delay_print("finding the sustenance they need, they climb out the ship and step back onto the road\n")
            travel = input("What will you do? \n")
        elif travel in "look at sign" "inspect sign":
            delay_print("A standard neon sign, similar to ones found in the Earthling ruins of the ancient ritual site of Vegas\n")
            score += 50
            travel = input("What will you do? \n")
        else:
            delay_print("no can do, buckaroo \n")
            travel = input("What will you do? \n")
    else:
        os.system("clear")
        delay_print(f'''As {name} treks along the highway toward the sound of the twangy music, a Mythomast pulls up right next
             to them, riding a dwalf \n''')
        delay_print(f'''The strange creature says, "Howdy Yung'un, what brings you to these parts?\n''')
        delay_print(f'''{name} responds, "I'm lost, but I saw a sign that said 1 mile to some bar or grill or something so
            I'm headed there now."\n''')
        delay_print(f'''The creature exclaims, "WALK?! Pardner, Asterodeo is a Meller's Increment away! That's the opposite side of
            the gulch!\n''')
        delay_print(f'''"Then whats that big cloud of dust?" Our daring protagonist questions, pointing at the rapidly approaching cloud of dust.''')
        delay_print(f'''"What cloud of dusk?" th mythomast asked, looking over to where {name} is pointing\n''')
        delay_print("By the great horn spoon! Its the wretched Hewitt Gang! Hop on quick, we can only outrun them on dwalfback!\n ")
        delay_print(f'''The cowthomast pulls {name} over the back of the dwalf, yelps, "Giddy up!" and the sleek blue dwalf rockets away\n''')
        delay_print(f'''After a while of our protagonist bouncing up and down the dwalf's back as they get away in style
            they decide to ask,"So who were those guys?\n"''')
        delay_print(f'''The cowpoke looked over his shoulder with surprise. "You've never heard of the Hewitt gang?" He said,
            "They're a band of miscreants, part of this big interplanetary enterprise uhhh whatsit? Evil Megacorp or sum
             like that. They're supposed 'protect' us from  Megacorp's ether drilling on the planet, but they really are just a gang 
             of thieves and murderers who do what they want\n''')
        delay_print(f'''"Huh, interesting. So why don't you guys just leave the planet?" Our increasingly less intelligent hero questions.\n''')
        delay_print(f'''The mythomast retorts, "Hewitt's henchman confiscated all our spacecraft, and anything that makes it into the sky gets shot
            down by Megacorp's railguns. Anyways, here we are buckaroo, welcome to Asterodeo."\n''')
        os.system("clear")
        delay_print(f'''Surprisingly, Asterodeo doesn't look too much different from the place where the ship crashed.
            A mostly empty wasteland, with a few tumbleweeds, but this time there are a few once glorious shacks labeled
            SHERIFF'S STATION, GENERAL STORE, and SALOON in neon lights. However, since its day, the lights are off.\n''')
        asterodeo = input("What will you do now? \n")
        while asterodeo not in ("walk to bar", "walk to saloon", "walk to asterodeo","travel to bar","travel to saloon","travel to asterodeo"):
            if asterodeo in ("look around", "inspect town"):
                delay_print(f'''{name} scans the area, taking note of the dwalf you rode into town tied up in front of the
                 sheriff's station. You also notice a an unfired bullet by your feet\n''')
                score += 50
                bullet = input("Pick up bullet?\n")
                if bullet == "yes":
                    delay_print(f'''You  have obtained one bullet\n''')
                    score += 100
                elif bullet == "no":
                    delay_print(f'''You left the bullet behind\n''')
                else: delay_print(dummy())
            asterodeo = input("What will you do now? \n")
            if asterodeo in ("walk to sheriff's station", "walk to station"):
                delay_print('''Walking into the sheriffs station, you see the mythomast who helped you out of that sticky situation
                with the Hewitts. \n''')
                delay_print(f'''The blob of a sheriff looks over and sees you. "Oh, its you again, we haven't been properly introduced
                I'm Sheriff Livingston. I protect this town, at least what's left of it. Most folks left or upn died...
                 No more guns left either, ammo shipments haven't come in since Megacorp took over. Not that they'd be any match for
                 the soldier's armor anyways." frustrated, Livingston throws his gun out the door and proclaims, "Imma go get me some hooch at the 
                 saloon." He walks out through the back exit. {name} walks back out the door and decides what do do next.\n''')
                score += 50
                asterodeo = input("What will you do now? \n")
            if asterodeo in ("pick up gun", "grab gun"):
                delay_print(f"{name} grabs the gun, and stows it. With a bullet, maybe this would be useful")
                score += 100
                asterodeo = input("What will you do now? \n")
            if asterodeo in ("load gun", "put round in gun", "put bullet in gun"):
                delay_print(f'''"probably a bad idea, this should wait till I need it,"{name} states \n''')
                score += 50
                asterodeo = input("What will you do now? \n")
            if asterodeo in ("walk to store", "enter store"):
                delay_print(f'''"{name} walks up to the front door of the general store. There's a little note that says,
                "On lunch break, will be back soon\n''')
                score += 50
                asterodeo = input("What will you do now? \n")
        os.system("clear")
        delay_print(f'''{name} walks through the doors of the musty saloon, and everyone turns to look at them\n''')
        delay_print(f'''"You're the new one aintcha? The one Sheriff Livingston saved?" an old eln in the corner questions\n''')
        delay_print(f'''"Yessir! Y'know where I could find him?" {name} asks.\n''')
        delay_print(f'''"Over there," the eln says, pointing to the bar. "Don't anger him though boy, he gets madder than the devil
        when something gets him worked up"\n''')
        delay_print(f'''{name} walks over to the bar, sits next to the sheriff, and asks the bartender for a tonic water\n''')
        delay_print(f'''Livingston looks over at them, sighs, and then goes back to nursing his drink\n''')
        delay_print(f'''BANG!\n''')
        time.sleep(3)
        delay_print(f''' Everyone turns towards the door to see a thin, gangly man with his gun raised toward the ceiling,
         having just shot a hole in it\n''')
        delay_print(f'''"Hewitt. What does your ugly mug want with us?" Livingston spat. \n''')
        delay_print(f'''"Oh nothing, just looking for some entertainment," Hewitt drawled\n''')
        delay_print(f'''"Hey you!," Hewitt pointed, "I haven't seen your face here before, you oughta be fun to play with."
        "What game d'ya wanna play?"\n''')
        game = input("What game will you choose?")
        while game not in "dice":
            if game in "russian roulette":
                delay_print(f'''"I like your style, but I don't feel like risking my life, just yours," Hewitt says.\n''')
                score += 50
                game = input("What game will you choose?")
            else:
                delay_print(f'''You don't have the item for this game, maybe you missed something on your adventure?\n''')
                game = input("What game will you choose?")
        else:
            delay_print(f'''Ah dice I see. But you have a 20 sided die... Whatever, whoever rolls the highest number wins alright?\n''')
            score += 100
            yn = input("Are these terms acceptable? ")
            while yn not in "yes":
                delay_print('''"Listen here pal, I'm giving you the benefit of the doubt here. I'll blow your brains out right now
                if you wanna complain," The stringy outlaw retorted \n''')
            else:
                delay_print(f'''Hewitt says, "Glad to hear it, now here is the catch. If you win, I leave this town forever. But,
                If I win, you die. Got it? Good"\n''')
                delay_print(f'''Before {name} has time to respond, he snatches the die from their hand, shoves it in a cup
                and rolls.\n''')
                time.sleep(3)
                delay_print(f'''An 18\n''')
                delay_print(f'''"Not bad!," he says, "your turn!"\n''')
                delay_print(f'''{name} grabs the die and cup in anticipation.\n''')
                time.sleep(2)
                delay_print(f'''"What're you waiting for?! C'mon cowpoke!" Hewitt says\n''')
                delay_print(f'''"Here goes nothing," {name} mutters. They squeeze the die 3 times for luck, put it in the cup,
                shake, and roll...\n''')
                delay_print(f'''...\n''')
                delay_print(f'''...\n''')
                time.sleep(3)
                delay_print(f'''A 20!\n''')
                score += 100
                delay_print(f'''For some reason Hewitt didn't look too bothered.\n''')
                delay_print(f'''"Alright, I'll take my leave," he said, "and while you've won this battle, don't think you've
                won the war foreigner."\n''')
                delay_print(f'''And with that, Hewitt walked out the door, and the whole town cheered.\n''')
                os.system("clear")
                delay_print(f'''That night, {name} woke up to the smell of smoke. Being on the second floor, far away from
                the saloon's kitchen, they knew something was wrong. They pulled the die that they used to win out of their pocket,
                squeezing it three times for good luck. Running downstairs,they see the saloon on fire. {name} got low and 
                got outside, but it wasn't any better. The whole town was going up in flames. Men, women, and children were
                scrambling about trying to save what they had, and in the distance, a few men on dwalfback ran away, flares in hand.\n''')
                delay_print(f'''The morning took to long to come. By then, all that remained were the charred remains of the 
                dilapidated architecture.\n''')
                delay_print(f'''Livingston walked up behind {name} and put his hand on their shoulder.\n''')
                delay_print(f'''"I knew it was too good to be true," he said morosely\n''')
                delay_print(f'''{name} said, "No, I will free this place from Megacorp. I can't let them bully you forever." \n''')
                delay_print(f'''"How?" the Sheriff said, "We don't even have weapons, or homes anymore!"\n''')
                delay_print(f'''You don't need weapons to fight, {name} retorted. "Now tell me. Where are the Hewitts hiding?"\n''')
                delay_print(f'''"Across Cowpoke Canyon, a few miles out of town," Livingston says\n''')
                delay_print(f'''"Well then, I've got a visit to make."\n''')
                os.system("clear")
                time.sleep(8)
                delay_print(f'''YOU HAVE REACHED THE END OF WORDLINE: A SPACE ODYSSEY ALPHA THANK YOU FOR PLAYING\n''')
                end_time = time.time()
                time_lapsed = end_time - start_time
                time_convert(time_lapsed)
                with open("database.txt", "a") as file:
                    file.write(f"{name},{time_convert},{score}\n")
                delay_print(f'''{name} you had a score of {score}. Congratulations!\n''')
                time_convert(time_lapsed)



























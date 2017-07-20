
define t = Character("Teacher")
define z = Character("Voice 1")
define y = Character("Voice 2")
define u = Character ("Unknown")
define h = Character ("Headmaster")
define m = Character ("Mom")
define gu = Character ("Guy")
define gi = Character ("Girl")
define k = Character ("Kilia")
define j = Character ("Jordan")
define d = Character ("Dr. Matis")
define r = Character ("Ryner")
define e = Character ("Jessica")
define s = Character ("Seita")
define dj = Character ("Dr. Jenner")
define f = Character ("Figure 1")
define F = Character ("Figure 2")
define narration = nvl_narrator
define ri = Character("Rin", image="rinn", who_color="#c8ffc8")
define ru = Character ("Rui", image="ruii", who_color="#c8ffc8")
define ii = Character("Iida", image="iidaa", who_color="#c8ffc8")
define ir = Character("Iris", image="iriss", who_color="#87CEFA")
init:
    image bg start = "office.jpg"
    image bg door = "hall.jpg"
    image bg dormnightlight = "dorm2.png"
    image bg dormsleep = "dorm3.png"
    image bg dormday = "dorm1.png"
    image bg cla2 = "classroom.png"
    image bg room = "background3.jpg"
    image bg aud = "aud.jpg"
    image bg caf = "caf.jpg"
    image bg back = "back.png"
    image bg back2 = "background 2.jpg"
    image bg locker = "locker.jpg"
    image bg home = "home.jpg"
    image bg night = "night.jpg"
    image bg hallway = "hallway.jpg"
    image bg background2 = "back2.jpg"
    image bg open = "open.jpg"
    image bg aud2 = "aud.jpe"
    image bg school = "school.jpg"

    $ flash = Fade(.25, 0, .75, color="#fff")
    $ pixellade = Pixellate(1.0, 5)
    
label start:
    play music ("background.mp3")

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    
    
    
    
    
    image headmaster = "characters/headmaster/headmaster.png"
    image headmaster1 = "characters/headmaster/down.png"
    image headmaster2 = "characters/headmaster/up.png"
    
    scene bg back
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    image rinbright = "characters/rin/bright rin.png"
    image rindizzy = "characters/rin/dizzy rin.png"
    image rinmad ="characters/rin/mad rin.png"
    image rinnervous = "characters/rin/nervous rin.png"
    image rin ="characters/rin/rin happy.png"
    image rinangry = "character/rin/rin angry.png"
    image rinlol = "characterss/rin/rin chan burst.png"
    image rincry = "characters/rin/rin cry.png"
    image rinsad1 = "characters/rin/rin cry+sad.png"
    image rinlaugh = "characters/rin/rin laugh.png"
    image rinoops = "characters/rin/rin oopsi.png"
    image rinsad2 = "characters/rin/rin sad.png"
    image rinsuperhappy = "characters/rin/rin super happy.png"
    image rinsurprise = "characters/rin/rin surprise.png"
    image rinyeah = "characters/rin/rin yeah.png"
    image rinshock = "characters/rin/shock rin.png"
    image rinsign = "characters/rin/sign rin.png"
    image rinsmirk = "characters/rin/smirky rin.png"
    image rinwelcome = "characters/rin/welcome rin.png"
    image rineee = "characters/rin/eee rin.png"
    
    image ruibright = "characters/rui/bright rui.png"
    image ruidizzy = "characters/rui/dizzy rui.png"
    image ruimad ="characters/rui/mad rui.png"
    image ruinervous = "characters/rui/nervous rui.png"
    image rui ="characters/rui/rui smiles.png"
    image ruiangry = "characters/rui/rui angry.png"
    image ruilol = "characters/rui/rui burst.png"
    image ruicry = "characters/rui/rui crying.png"
    image ruisad1 = "characters/rui/poor rui.png"
    image ruilaugh = "characters/rui/rui laugh.png"
    image ruioops = "characters/rui/guilty rui.png"
    image ruisad2 = "characters/rui/rui sad.png"
    image ruisuperhappy = "characters/rui/rui happy.png"
    image ruisurprise = "characters/rui/rui surprise.png"
    image ruiyeah = "characters/rui/rui yeah.png"
    image ruishock = "characters/rui/shocked rui.png"
    image ruisign = "characters/rui/sign rui.png"
    image ruismirk = "characters/rui/smirky rui.png"
    image ruiwelcome = "characters/rui/welcome rui.png"
    image ruieee = "characters/rui/eee rui.png"
    
    image irisbright = "characters/iris/bright iris.png"
    image irisdizzy = "characters/iris/dizzy confused.png"
    image irismad ="characters/iris/mad iris.png"
    image irisnervous = "characters/iris/nervous iris.png"
    image iris ="characters/iris/iris smile.png"
    image irisangry = "characters/iris/iris angry.png"
    image irislol = "characters/iris/iris burst out.png"
    image iriscry = "characters/iris/iris cry.png"
    image irissad1 = "characters/iris/iris cry+sad.png"
    image irislaugh = "characters/iris/iris laugh.png"
    image irisoops = "characters/iris/fake smile iris(maybe).png"
    image irissad2 = "characters/iris/iris sad.png"
    image irissuperhappy = "characters/iris/iris happy.png"
    image irissurprise = "characters/iris/iris surprised.png"
    image irisyeah = "characters/iris/iris yeah.png"
    image irisshock = "characters/iris/iris shock.png"
    image irissign = "characters/iris/sign iris.png"
    image irissmirk = "characters/iris/haha.png"
    image iriswelcome = "characters/iris/welcome iris.png"
    image iriseee = "characters/iris/eee iriz.png"
    
    image iidabright = "characters/iida/bright iida.png"
    image iidadizzy = "characters/iida/iida confused.png"
    image iidamad ="characters/iida/mad iida.png"
    image iidanervous = "characters/iida/nervous iida.png"
    image iida ="characters/iida/iida smiles.png"
    image iidaangry = "characters/iida/iida angry.png"
    image iidalol = "characters/iida/iida too happy.png"
    image iidacry = "characters/iida/iida cry.png"
    image iidasad1 = "characters/iida/iida cry+sad.png"
    image iidalaugh = "characters/iida/iida laugh.png"
    image iidaoops = "characters/iida/iida ehhhh.png"
    image iidasad2 = "characters/iida/iida sad.png"
    image iidasuperhappy = "characters/iida/iida happy.png"
    image iidasurprise = "characters/iida/iida surprised.png"
    image iidayeah = "characters/iida/iida yeah.png"
    image iidashock = "characters/iida/iida shock.png"
    image iidasign = "characters/iida/sign iida.png"
    image iidasmirk = "characters/iida/smirk iida.png"
    image iidawelcome = "characters/iida/welcome iida.png"
    image iidaeee = "characters/iida/eee iida.png"
    
    image friend1bright = "characters/friend1/with iida +iris/bright friend 2.png"
    image friend1dizzy = "characters/friend1/with iida +iris/friend confused 2.png"
    image friend1mad ="characters/friend1/with iida +iris/mad friend 2.png"
    image friend1nervous = "characters/friend1/with iida +iris/friend nervous 2.png"
    image friend1 ="characters/friend1/with iida +iris/friend smiles 2.png"
    image friend1angry = "characters/friend1/with iida +iris/friend angry.png"
    image friend1lol = "characters/friend1/with iida +iris/friend chan burst.png"
    image friend1cry = "characters/friend1/with iida +iris/friend cry 2.png"
    image friend1sad1 = "characters/friend1/with iida +iris/friend cry+sad 2.png"
    image friend1laugh = "characters/friend1/with iida +iris/friend laugh 2.png"
    image friend1oops = "characters/friend1/with iida +iris/ehhh 2.png"
    image friend1sad2 = "characters/friend1/with iida +iris/friend sad 2.png"
    image friend1superhappy ="characters/friend1/with iida +iris/friend happy 2.png"
    image friend1surprise = "characters/friend1/with iida +iris/friend chan surprise 2.png"
    image friend1yeah = "characters/friend1/with iida +iris/friend yeah.png"
    image friend1shock = "characters/friend1/with iida +iris/friend shock 2.png"
    image friend1sign = "characters/friend1/with iida +iris/friend sign 2.png"
    image friend1smirk = "characters/friend1/with iida +iris/friend smirk 2.png"
    image friend1welcome = "characters/friend1/with iida +iris/friend welcome 2.png"
    image friend1eee = "characters/friend1/with iida +iris/eee friend.png"
    
    image friend1_bright = "characters/friend1/with rui +rin/bright friend.png"
    image friend1_dizzy = "characters/friend1/with rui +rin/friend confused.png"
    image friend1_mad ="characters/friend1/with rui +rin/mad friend 2.png"
    image friend1_nervous = "characters/friend1/with rui +rin/nervous friend.png"
    image friend1_ ="characters/friend1/with rui +rin/friend happy.png"
    image friend1_angry = "characters/friend1/with rui +rin/friend chan angry.png"
    image friend1_lol = "characters/friend1/with rui +rin/friend chan burst out.png"
    image friend1_cry = "characters/friend1/with rui +rin/friend cry.png"
    image friend1_sad1 = "characters/friend1/with rui +rin/friend cry+sad.png"
    image friend1_laugh = "characters/friend1/with rui +rin/friend laugh.png"
    image friend1_oops = "characters/friend1/with rui +rin/eee friend.png"
    image friend1_sad2 = "characters/friend1/with rui +rin/friend sad.png"
    image friend1_superhappy = "characters/friend1/with rui +rin/friend happy.png"
    image friend1_surprise = "characters/friend1/with rui +rin/friend chan surprise.png"
    image friend1_yeah = "characters/friend1/with rui +rin/friend yeah 2.png"
    image friend1_shock = "characters/friend1/with rui +rin/friend shock.png"
    image friend1_sign = "characters/friend1/with rui +rin/friend sign.png"
    image friend1_smirk = "characters/friend1/with rui +rin/friend chan smirk.png"
    image friend1_welcome = "characters/friend1/with rui +rin/friend welcome.png"
    image friend1_eee = "characters/friend1/with rui +rin/eee friend.png"
    
    image friend2bright = "characters/friend 2/with iida +iris/bright.png"
    image friend2dizzy = "characters/friend 2/with iida +iris/dizzy.png"
    image friend2nervous = "characters/friend 2/with iida +iris/.png"
    image friend2 ="characters/friend 2/with iida +iris/smile.png"
    image friendangry = "characters/friend 2/with iida +iris/angry.png"
    image friendlol = "characters/friend 2/with iida +iris/burst.png"
    image friend2cry = "characters/friend 2/with iida +iris/cry.png"
    image friend2sad1 = "characters/friend 2/with iida +iris/sad1.png"
    image friend2laugh = "characters/friend 2/with iida +iris/laugh.png"
    image friend2oops = "characters/friend 2/with iida +iris/oops.png"
    image friend2sad2 = "characters/friend 2/with iida +iris/sad2.png"
    image friend2superhappy ="characters/friend 2/with iida +iris/happy.png"
    image friend2surprise = "characters/friend 2/with iida +iris/surprise.png"
    image friend2yeah = "characters/friend 2/with iida +iris/yeah.png"
    image friend2shock = "characters/friend 2/with iida +iris/shock.png"
    image friend2sign = "characters/friend 2/with iida +iris/sign.png"
    image friend2smirk = "characters/friend 2/with iida +iris/smirk.png"
    image friend2eee= "characters/friend 2/with iida +iris/eee.png"
    
    
    image friend2_bright = "characters/friend 2/with rui +rin/bright.png"
    image friend2_dizzy = "characters/friend 2/with rui +rin/dizzy.png"
    image friend2_mad ="characters/friend 2/with rui +rin/mad.png"
    image friend2_nervous = "characters/friend 2/with rui +rin/nervous.png"
    image friend2_angry = "characters/friend 2/with rui +rin/angry.png"
    image friend2_lol = "characters/friend  2/with rui +rin/burst.png"
    image friend2_sad1 = "characters/friend 2/with rui +rin/sad1.png"
    image friend2_oops = "characters/friend 2/with rui +rin/oops.png"
    image friend2_superhappy = "characters/friend 2/with rui +rin/happy.png"
    image friend2_surprise = "characters/friend 2/with rui +rin/surprise.png"
    image friend2_yeah = "characters/friend 2/with rui +rin/yeah.png"
    image friend2_smirk = "characters/friend 2/with rui +rin/smirk.png"
    image friend2_welcome = "characters/friend 2/with rui +rin/welcome.png"
    image friend2_eee= "characters/friend 2/with rui +rin/eee.png"
    image friend2_= "characters/friend 2/with rui +rin/smile.png"
    image friend2_sign="characters/friend 2/with rui +rin/sign.png"
    
    image friend3bright = "characters/friend3/with iida +iris/bright.png"
    image friend3dizzy = "characters/friend3/with iida +iris/confused.png"
    image friend3mad ="characters/friend3/with iida +iris/mad.png"
    image friend3nervous = "characters/friend3/with iida +iris/nervous.png"
    image friend3 ="characters/friend3/with iida +iris/smiles.png"
    image friend3angry = "characters/friend3/with iida +iris/angry.png"
    image friend3lol = "characters/friend3/with iida +iris/too happy.png"
    image friend3cry = "characters/friend3/with iida +iris/cry.png"
    image friend3sad1 = "characters/friend3/with iida +iris/cry+sad.png"
    image friend3laugh = "characters/friend3/with iida +iris/laugh.png"
    image friend3oops = "characters/friend3/with iida +iris/ehh.png"
    image friend3sad2 = "characters/friend3/with iida +iris/sad.png"
    image friend3superhappy ="characters/friend3/with iida +iris/happy.png"
    image friend3surprise = "characters/friend3/with iida +iris/surprise.png"
    image friend3yeah = "characters/friend3/with iida +iris/yeah.png"
    image friend3shock = "characters/friend3/with iida +iris/shock.png"
    image friend3sign = "characters/friend3/with iida +iris/sign.png"
    image friend3smirk = "characters/friend3/with iida +iris/smirk.png"
    image friend3welcome = "characters/friend3/with iida +iris/welcome.png"
    image friend3eee = "characters/friend3/with iida +iris/eee.png"
    #-------------------------------------------------------------------------
    image matisserious = "characters/male teacher/serious.png"
    image matissmile = "characters/male teacher/smile.png"
    image matis = "characters/male teacher/normal.png"
    image matissad = "characters/male teacher/sad.png"
    
    image jennersad = "characters/female teacher/sad.png"
    image jennersmile = "characters/female teacher/smile.png"
    image jenner = "characters/female teacher/hola.png"
    image jennerangry = "characters/female teacher/angry.png"
    
    image momsad = "characters/mom/sad.png"
    image mom = "characters/mom/normal.png"
    image momhappy = "characters/mom/happy.png"
    image momangry = "characters/mom/angry.png"
    #-------------------------------------------------side character
    
    
    image side rinn bright = "characters/rin/side/side_bright rin.png"
    image side rinn dizzy = "characters/rin/side/side_dizzy rin.png"
    image side rinn mad ="characters/rin/side/side_mad rin.png"
    image side rinn nervous = "characters/rin/side/side_nervous rin.png"
    image side rinn smiles ="characters/rin/side/side_rin happy.png"
    image side rinn angry = "character/rin/side/side_rin angry.png"
    image side rinn lol = "characterss/rin/side/side_rin chan burst.png"
    image side rinn cry = "characters/rin/side/side_rin cry.png"
    image side rinn sad1 = "characters/rin/side/side_rin cry+sad.png"
    image side rinn laugh = "characters/rin/side/side_rin laugh.png"
    image side rinn oops = "characters/rin/side/side_rin oopsi.png"
    image side rinn sad2 = "characters/rin/side/side_rin sad.png"
    image side rinn superhappy = "characters/rin/side/side_rin super happy.png"
    image side rinn surprise = "characters/rin/side/side_rin surprise.png"
    image side rinn yeah = "characters/rin/side/side_rin yeah.png"
    image side rinn shock = "characters/rin/side/side_shock rin.png"
    image side rinn sign = "characters/rin/side/side_sign rin.png"
    image side rinn smirk = "characters/rin/side/side_smirky rin.png"
    image side rinn welcome = "characters/rin/side/side_welcome rin.png"
    image side rinn eee = "characters/rin/side/side_eee rin.png"
    
    image side ruii bright = "characters/rui/side/side_bright rui.png"
    image side ruii dizzy = "characters/rui/side/side_dizzy rui.png"
    image side ruii mad ="characters/rui/side/side_mad rui.png"
    image side ruii nervous = "characters/rui/side/side_nervous rui.png"
    image side ruii smiles ="characters/rui/side/side_rui smiles.png"
    image side ruii angry = "characters/rui/side/side_rui angry.png"
    image side ruii lol = "characters/rui/side/side_rui burst.png"
    image side ruii cry = "characters/rui/side/side_rui crying.png"
    image side ruii sad1 = "characters/rui/side/side_poor rui.png"
    image side ruii laugh = "characters/rui/side/side_rui laugh.png"
    image side ruii oops = "characters/rui/side/side_guilty rui.png"
    image side ruii sad2 = "characters/rui/side/side_rui sad.png"
    image side ruii superhappy = "characters/rui/side/side_rui happy.png"
    image side ruii surprise = "characters/rui/side/side_rui surprise.png"
    image side ruii yeah = "characters/rui/side/side_rui yeah.png"
    image side ruii shock = "characters/rui/side/side_shocked rui.png"
    image side ruii sign = "characters/rui/side/side_sign rui.png"
    image side ruii smirk = "characters/rui/side/side_smirky rui.png"
    image side ruii welcome = "characters/rui/side/side_welcome rui.png"
    image side ruii eee = "characters/rui/side/side_eee rui.png"
    
    image side iriss bright = "characters/iris/side/side_bright iris.png"
    image side iriss dizzy = "characters/iris/side/side_dizzy confused.png"
    image side iriss mad ="characters/iris/side/side_mad iris.png"
    image side iriss nervous = "characters/iris/side/side_nervous iris.png"
    image side iriss smiles ="characters/iris/side/side_iris smile.png"
    image side iriss angry = "characters/iris/side/side_iris angry.png"
    image side iriss lol = "characters/iris/side/side_iris burst out.png"
    image side iriss cry = "characters/iris/side/side_iris cry.png"
    image side iriss sad1 = "characters/iris/side/side_iris cry+sad.png"
    image side iriss laugh = "characters/iris/side/side_iris laugh.png"
    image side iriss oops = "characters/iris/side/side_fake smile iris(maybe).png"
    image side iriss sad2 = "characters/iris/side/side_iris sad.png"
    image side iriss superhappy = "characters/iris/side/side_iris happy.png"
    image side iriss surprise = "characters/iris/side/side_iris surprised.png"
    image side iriss yeah = "characters/iris/side/side_iris yeah.png"
    image side iriss shock = "characters/iris/side/side_iris shock.png"
    image side iriss sign = "characters/iris/side/side_sign iris.png"
    image side iriss smirk = "characters/iris/side/side_haha.png"
    image side iriss welcome = "characters/iris/side/side_welcome iris.png"
    image side iriss eee = "characters/iris/side/side_eee iris.png"
    
    image side iidaa bright = "characters/iida/side/side_bright iida.png"
    image side iidaa dizzy = "characters/iida/side/side_iida confused.png"
    image side iidaa mad ="characters/iida/side/side_mad iida.png"
    image side iidaa nervous = "characters/iida/side/side_nervous iida.png"
    image side iidaa smiles ="characters/iida/side/side_iida smiles.png"
    image side iidaa angry = "characters/iida/side/side_iida angry.png"
    image side iidaa lol = "characters/iida/side/side_iida too happy.png"
    image side iidaa cry = "characters/iida/side/side_iida cry.png"
    image side iidaa sad1 = "characters/iida/side/side_iida cry+sad.png"
    image side iidaa laugh = "characters/iida/side/side_iida laugh.png"
    image side iidaa oops = "characters/iida/side/side_iida ehhhh.png"
    image side iidaa sad2 = "characters/iida/side/side_iida sad.png"
    image side iidaa superhappy = "characters/iida/side/side_iida happy.png"
    image side iidaa surprise = "characters/iida/side/side_iida surprised.png"
    image side iidaa yeah = "characters/iida/side/side_iida yeah.png"
    image side iidaa shock = "characters/iida/side/side_iida shock.png"
    image side iidaa sign = "characters/iida/side/side_sign iida.png"
    image side iidaa smirk = "characters/iida/side/side_smirk iida.png"
    image side iidaa welcome = "characters/iida/side/side_welcome iida.png"
    image side iidaa eee = "characters/iida/side/side_eee iida.png"
    
    
    #ppicture of the game +logo 
    "Hello and welcome to our game! You might question why the game named 'Two sides of the coin'! Let's me give you a hint, life never goes in one way! Play the game to find out the meaning of it! LET'S GO!!!"
    scene bg back2
    with Dissolve (.5)
    
    menu:
        "Morality":
            show rui at right
            with Dissolve(.4)
            show rin at left
            with Dissolve(.4)
            "You are about to start the morality route! But before you do, select a character."
            "Are you a girl or a boy?"
            menu:
                "Girl":
                    hide rui
                    hide rin
                    show rinsuperhappy at left
                    show ruisad2 at right
                    
                    "Ok! Your character is ready! You may now begin the Morality storyline."
                    hide rinsuperhappy
                    hide ruisad2
                    scene bg start
                    with flash
                
                    ri smiles "I open my eyes to see I'm sitting in an office with a large bookcase resting against one wall. Expansive windows let in the morning light from the left side of the room."
                    
                    show headmaster1 
                    with pixellade
                    ri smiles "Across from me an imposing man stared at me across the large oak table that we've been sitting at for the past hour."
                
                    #show teacher with folder
                    ri smiles "The man is holding a large and imposing folder in his left hand."
                    t "You've been assigned under Dr. Matis with the rest of class 1A."
                    hide headmaster1
                    show headmaster2
                    #hide teacher with folder
                    #show teacher look up right
                    t "You are to meet them Orientation at 7:00 which means you have twenty minutes until you have to be in the Auditorium."
                    #hide teacher
                    #show teacher smiles
                    t "It's just past the Cafeteria."
                    "The imposing man stares at you for a few more moments, but then he leaves."
                    hide headmaster2
                    with Dissolve (.4)
                    $renpy.pause(.5)
                    
                    show rinsign
                    with Dissolve(.4)
                    "Whew! That was stressful, but at long last, I've passed the final interview!"
                    hide rinsign
                    show rinsuperhappy
                    "I DID IT!"
                    "I finally made it into the Epannian School of Strategy!"
                    "I can now proudly say that I am a student of the most prestigious school in my country, Padelia."
                    hide rinsuperhappy
                    
                    scene bg door
                    with flash
                    play sound ("door open.mp3")
                    ri smiles "I rose to stand in front of the door and touched the cool door handle. The door released a low groan as I pushed it open and left the room."
                    
                    ri sad2 "The hallway is completely deserted."
                    ri sad2 "I hesitate for a moment."
                    "Do you want to go straight to the auditorium or would you rather explore your new home for the next four years?"
                    menu:
                        "Auditorium":
                            scene bg locker
                            with flash
                            $ renpy.pause (.8)
                            scene bg door
                            with flash
    
                            ri superhappy "Alright! I set off in the direction I believe the cafeteria is in..."
                            
                            ri oops "But I quickly remember I don't know where anything is, or even where I am!"
                            show rindizzy with hpunch
                            "I quickly look around and realize I am in an unmarked hallway. Oh Goodness!"
                            hide rindizzy
                        "Explore":
                            
                            ri laugh "Excellent! I turn on my heel and pick a random direction to investigate. This should be fun!"
                            ri smiles "For the most part, the building is uninhabited."
                            ri welcome "All the current students are elsewhere, probably either in class or in a tactical battlefield simulation."
                    ri oops "As I stride past another dark, unmarked door, I hear something break the monotonous sound of my footsteps."
                    ri oops "Hushed voices are leaking past the door up ahead on my right."
                    
                    #creepy voice if possible
                    play sound ("whispering.mp3")
                    z "...tensions out of hand"
                    z "... somehow ..." 
                    z "must find out their plans..."
                    y "... but what about the recent..."
                    y "... security increase..."
                    y "... threats..."
                    play sound ("whispering.mp3")
                    y "... not enough information..."
                    z "... sigh..."
                    z "... it is what it is..."
                    z "... contact..."
                    z "... know what to do..."
                    " Do you want to keep listening?"
                    stop sound
                    menu:
                        "Yes":
                            play sound("whispering.mp3")
                            ri smirk "I inch closer to the door as my heartbeat pounds in my ears."
                            ri smirk "The voices inside seem to hush even further."
                            ri mad "What's going on?"
                            
                            show rinsurprise
                            with Dissolve (.3)
                            "Threats?"
                            "Contact who?"
                            "Find what out?"
                            "I lose myself in my thoughts about what's going on."
                            hide rinsurprise
                        "No":
                            ri mad "I stumble back from the previously unnoticeable door that now seems to hold so many secrets."
                            ri mad "What's going on?"
                            show rinshock
                            with Dissolve(.3)
                            "Threats?"
                            "Contact who?"
                            "Find what out?"
                            "I lose myself in my thoughts about what's going on."
                            hide rinshock
                    ri dizzy "I lose my train of thought with a jolt. I look around and remember that I am still completely and utterly lost!"
                    show rinshock at center with hpunch
                    "Oh no! There's only two minutes until 7:00!"
                    "I start running, but by the time I break around the corner of yet another unmarked hallway, I realize it's hopeless."
                    hide rinshock with Dissolve(.4)
                    ri sign "I bent over gasping with my hands on my knees when I hear a new set of footsteps rounding the corner in front of me."
                    ri oops"Looking up, I see a stern man in an unknown uniform walking toward me. Before i can register anything else, he's already standing in front of me."

                    show matis at center
                    "How will you address the man?"
                    menu:
                        "Address him as sir and offer a salute":
                            "Sir."
                            u "Student. You've got a minute to report to the Auditorium. What are you doing here?"
                            hide matis
                            show matisserious
                            ri oops "Sir, I am aware of the urgency, but I am new and seem to have lost my way, Sir."
            
                            ri nervous "If you could point me in the right direction...?"
                            hide matis serious
                            show matis 
                            
                            "The man sighs and cocks his head towards the corner at the other end of the hall."
                            hide matis
                            show matissmile
                            u "You can follow me. I'm also headed in that direction."
                            hide matissmile with Dissolve(.4)
                        "Ask the man who he it":
                            ri oops"The weight of his stare bares down on my neck. The stern man suddenly grips me by the ear and begins walking again, dragging me alongside him."
                            ri cry "My eyes are watering and I realize he must be a teacher here."
                            show matisserious at center with Dissolve(.4)
                            u "Ugh... Rookies. You know you're supposed to be in the auditorium in..."
                            "The man checks his watch and lets out a sigh."
                            hide matisserious
                            show matis
                            u "30 seconds. What's your name kid?"
                            ri oops "I squirm uncomfortably."
                            ri nervous"I am [ri]. Are you taking me to the Auditorium now?"
                            u "No more questions squirt, and try to keep your trap shut on the way."
                            hide matis
                        "Ignore him and try to catch your breath. You don't know him.":
                            ri smiles"I avoided eye contact, but the man just wasn't having it."
                            u "You there! Newbie! You've got a minute to report in the Auditorium."
                            show matisserious
                            u "Quit dawdling and get moving!"
                            ri sad2 "..."
                            u "SCRAM!" with hpunch
                            "The man makes a shooing motion with his hands and shakes his head in annoyance."
                            #hide stranger and show other expression
                            hide matisserious
                            show matis
                            u "Ugh, nevermind. I bet you don't even know where it is. Come on, kid. It's this way"
                            hide matis with Dissolve (.5)
                            
                        "Avoid eye contact, he's scary":
                            ri oops "The man's stare softened as he appraised me."
                            show matis
                            u "Excuse me, you're a new student correct?"
                            hide matis
                            show matissmile
                            u "There's only a minute until report time for the Orientation. What's your name?"
                            ri nervous "My...My name is [ri]. Um... Could you please show me where the Auditorium is? I'm lost..."
                            hide matissmile
                            show matis
                            "The man sighed and cocked his head towards the corner at the other end of the hall."
                            #show rin at the corner
                            u "You can follow me. I'm headed there as well."
                            hide matis
                    scene bg aud
                    with flash
                
                    ri sign "Whew. I just managed to slip in with the crowd of last-second students and snatch a seat. The mystery man walked off somewhere as soon as the Auditorium was in view."
                    ri bright "He seemed a little rough around the edges, but he did bring me along when he could've just left me to wander the halls."
                    ri bright "Huh, it wouldn't be a stretch to imagine him doing it though."
                    "I snap back to reality and focus on the stage as the headmaster appears to introduce all the teachers."
                    show headmaster
                    ri surprise "Whoa! The man I met is up there too! He stands up as the head moves on to begin introducing him."
                    #show rin at the corner
                    h "And here is our most recent addition to the staff here at Epannian, Dr. Matis!"
                    show matis at right
                    with Dissolve (.6)
                    h "He'll be teaching Espionage Tactics and is the homeroom teacher to class 1A."
                    hide matis with Dissolve(.5)
                    h "Next up is Mrs. Spannend...."
                    "The rest of Orientation droned on as all the teachers returned to their seats and the head began talking about the pride of the school and upcoming exams."
                    "It all came to a close with a speech from the student body president of the freshmen and a final remark from the deputy headmaster."
                    "Later........."
                    scene bg dormnightlight
                    with pixellade
                    show rinlaugh 
                    "Wow. A day full of tours and clubs dragging me over to join. I fall back on my small bed and close my eyes to the unfamiliar dorm around me."
                    "Wow...what a long day! I'm ready to pass out. Hopefully the night lasts long enough to get a good rest."
                    hide rinlaugh
                    show rinbright
                    "I smile to myself and think of my day and my family that were back home."
                    "Oh! They must be wondering how the final interview went."
                    hide rinbright
                    show rinsuperhappy
                    "Maybe Mom will pick up if I call."
                    "Do you want to call Mom now or in the morning?"
                    hide rinsuperhappy
                    menu:
                        "Now":
                            "I dig around my bag for the cheap phone mom bought me, so I could keep in touch while at school, and press speed dial one."
                            ri smiles"Riing..."
                            ri smiles"Riing..."
                            ri smiles"Riing..."
                            ri supperhappy"Rii-- Click"
                            ri superhappy "Mom?"
                            #show rin at the corner
                            scene bg home
                            with Dissolve(.5)
                            show mom
                            #------------------------------------------------------------------------------------
                            m "Hello? Oh, [ri] sweetie! I've been waiting all day! So...? How'd it go?"
                            ri laugh"Eeeee! I made it!! Haha! I made it into Epannian!"
                            m "Oh my goodness! Oh... I'm so proud of you, [ri]. My baby, you've made your sisters and I so proud. Oh Honey..."
                            hide mom
                            show momhappy
                            "I can hear her happily tearing up on the other end."
                            hide momhappy
                            show mom
                            m "*sniffle*...Oh! Before I go, sweetie, I want to let you know-- be careful anytime you go out, ok [ri]?"
                            hide mom
                            show momsad
                            m "There's been a lot in the news about threats on Epannian students from rival schools."
                            m " I know you'll have buddies who want to hang out but be sure you're careful."
                            m "I worry so much for you now that you're so far away.... Be safe, ok hun?"
                            ri oops" My mind whirrs as I connect the conversation I overheard earlier today to the news of threats on the other students here."
                            m "...Sweetie?"
                            hide momsad
                            show mom
                            ri bright "Oh, of course Mom, I'll keep my guard up. You don't have to worry."
                            ri smiles"I promise."
                            m "*Sniffle* ...Alright, [ri]. I love you. Hmm, but don't forget to have fun, too. Do your best while you're there! Bye..."
                            "Click"
                            hide mom
                           #-------------------------------------------------------------------------------------- 
                            scene bg dormsleep
                            show rin
                            "Hmmmm. I collapse back down onto the duvet and start nodding off."
                            "Time to sleep I guess."
                            hide rin
                            with Dissolve (.5)
                            "I fall asleep in my clothes and dream deeply of home and happy childhood moments."
                            scene bg dormday with vpunch
                            "BEEP...BEEP...BEEP...BE-"
                            show rindizzy with hpunch
                            "Urgh.... what.... where...?"
                            hide rindizzy
                            show rinbright
                            "Oh, right. Epannian!"
                            hide rinbright
                            
                        "In the Morning":
                            scene bg dormsleep
                            show rinbright
                            "Yeah... It's already so late. It's probably best to let her rest and just check in when morning comes."
                            "I'll just have to set my alarm early."
                            hide rinbright
                            with Dissolve(1.)
                            "Aaah, finally time for sleep."
                            " I fall asleep in my clothes and dream deeply of home and happy childhood moments."
                            scene bg dormday with vpunch
                            "BEEP...BEEP...BEEP...BE--"
                            show rindizzy with hpunch
                            "Urgh.... what..... where...?"
                            hide rindizzy
                            show rinsurprise
                            "Oh, right. Mom. Where....my phone...?"
                            "I dig around the blankets wrapping me until I find the cheap phone mom bought me, so I could keep in touch while I'm at school, and press speed dial one."
                            hide rinsurprise
                            show rin 
                            "Riing..."
                            "Riing..."
                            "Riing..."
                            "Rii- Click"
                            scene bg home
                            with flash
                            show momangry
                            m "Hello? Oh, [ri]! You meanie! You made me wait so long to hear the news!"
                            #---------------------------------------------------------------------------------
                            m "So...? How'd it go?"
                            hide momangry
                            show mom
                            ri superhappy"...Oh Yeah! I made it!! Haha! I made it into Epannian!"
                            ri superhappy"I glance around and survey the dorm I didn't bother to check out last night."
                            ri bright"There's a small bed, a desk, a tiny dresser, with a mini fridge beside it and a window that divide the wall across from the bed in half."
                            ri bright"Aside from that, the room is barren. A typical freshman's room."
                            m "Oh my goodness! Oh... I'm so proud of you, [ri]. My baby, you've made your sisters and I so proud. Oh honey..."
                            hide mom
                            show momhappy
                            "I can hear her tearing up on the other end."
                            m "*sniffle*...Oh! Before I go, sweetie, I want to let you know-- be careful anytime you go out, ok [ri]?"
                            hide momsuperhappy
                            show momsad
                            
                            m "There's been a lot in the news about threats on Epannian students from rival schools."
                            m " I know you'll have buddies who want to hang out but be sure you're careful."
                            m "I worry so much for you now that you're so far away.... Be safe, ok hun?"
                            " My mind whirrs as I connect the conversation I overheard yesterday to the news of threats on the other students here."
                            m "...Sweetie?"
                            hide momsad
                            show mom
                            ri smiles "Oh, of course Mom, I'll keep my guard up. You don't have to worry."
                            ri bright"I promise."
                            m "*Sniffle* ...Alright, [ri]. I love you. Hmm, but don't forget to have fun, too. Do your best while you're there! Bye..."
                            "Click"
                            hide mom
                        #-------------------------------------------------------------------------------------
                    scene bg dormday
                    with Dissolve(.5)
                    "Later..."
                    show rinwelcome
                    "Hmmmm... I guess I'll just follow the crowd to find the cafeteria again."
                    "A steady trickle of people leads to the doors of the massive building."
                    hide rinbright
                    scene bg caf
                    with flash
                    ri surprise "Oh wow! So many students here! I wander over to the line and peek over shoulders to get a glimpse of the menu."
                    ri smiles"As I strain to stay on my tiptoes, I feel a finger tapping my shoulder."
                    show friend2_ at center with move
                    with Dissolve(.4)
                    gu "Hey, do you want a menu?"
                    "In the boy's other hand is a paper printout of the menu on the wall."
                    
                    ri oops "Huh?"
                    show friend1_ at right with move
                    gi "He said a menu, silly!"
                    #show rineee
                    ri eee"Oh. Um, sure. Thank you!"
                    #hide rineee
                    hide friend2_
                    hide friend1_
                    show friend1_welcome at right 
                    show friend2_bright at center
                    gi "Haha! No problem! I'm Kilia, this guy here is Jordan."
                    k "We're in the Tactical Communications department, what about you?"
                    ri superhappy "Oh, neat! I'm [ri] also in the Tactical Comms department."
                    #show rin at the corner
                    ri bright "What about your homeroom?"
                    hide friend1_welcome
                    hide friend2_bright
                    show friend2_sign at center
                    show friend1_ at right
                    j "Matis. I got a look at him at the Orientation. Seems like he's not gonna let us lack on homework, that's for sure."
                    k "Um, ew! C'mon..."
                    #show rin at the corner sad
                    ri smiles"Actually, I ran into him before the Orientation. He found me when I was lost and helped me back and all. I don't think he likes me though..."
                    hide friend1_
                    show friend1_oops at right
                    k "I get the feeling he just doesn't like any of us. Ha, see? He's over there in the corner, staring us all down."
                    hide friend2_sign
                    show friend2_surprise at center
                    j "Whoa! That's creepy."
                    #hide guy
                    #show guy 2 surprise
                    ri surprise "Huh, I never would have noticed he was there."
                    hide friend1_oops
                    hide friend2_surprise
                    show friend1_bright at right
                    show friend2_bright at center
                    k "Let's just finish up and go to class. I don't wanna risk being stared at like that if we're late."
                    ri bright"I finish up breakfast and leave the cafeteria to search for class 1A with my new friends."
                    hide friend1_bright 
                    hide friend2_bright
                    scene bg cla2
                    with Dissolve(.5)
                    play sound ("bell.mp3")
                    " As soon as we cross the threshold into the room, the late bell sounds and we breathe a collective sigh of relief as you meander over to the last three available seats..."
                    "... at the very front."
                    "I hear the same clunking footsteps from yesterday enter the room just as we've all sat down."
                    show matis at center with move
                    "All the students settle down and wait silently for him to speak."
                    hide matis
                    show matisserious
                    d "Any questions? No?"
                    d "Good, then let's get started on what we came here to do."
                    d "First things first, we've got written and physical exams."
                    hide matisserious
                    show matis
                    d "We'll use this to measure your potential and progress throughout the year."
                    d "Last place student is expelled."
                    d "Prepare yourselves."
                    hide matis
                    narration"The test is insert outside of the game! Finish the test then come back here"
                    play sound("school bell.mp3")
                    "Ding, Dong, Ding, Dong, ....Ding, Dong, Ding, Dong"
                    show matis
                    d "That's it everyone! Class dismissed!"
                    hide matis
                    show friend1_sign at center
                    show friend2_sign at right
                    #at the corner
                    ri sign "Aaaaaaahhhhh"
                    "The entire room sighed in relief."
                    scene bg locker
                    with Dissolve(.7)
                    show rinbright at center
                    show friend1_sign at right
                    show friend2_ at left
                    k "Oh. My. God. What a day!"
                    k "I swear he was looking to kill one of us!"
                    k "Poor Debbie got it the worst, it was like he was intent on really ruining her day. All she did was sneak a bite of leftover breakfast!"
                    hide friend1_sign
                    show friend1_ at right
                    hide friend2_
                    show friend2_sign at left
                    j "No kidding. Ughhh. Not like he eased up on us either. Nooo, he had to make us run a freaking marathon on day one!"
                    hide rinbright
                    show rinlaugh at center
                    ri "Haha, yeah, are we gonna sleep well tonight or what. Wow."
                
                    k "Oh, [ri], speaking of tonight..."
                    hide friend1_
                    show friend1_smirk at right
                    hide friend2_sign
                    show friend2_eee at left
                    hide rinlaugh
                    show rin
                    "Jordan motions me to come in close and Kilia looks over her shoulder before turning back to face me."
                    j "We were thinking we all meet up in my room after dinner and spend our first night cooling off and relaxing."
                    j "Nothing crazy, just some fun."
                    hide rin
                    show rinbright
                    ri "Um, sure, I guess. What room? I wanna grab my clothes before coming over."
                    k "105. We're meeting there at 8:30, so don't be late, kay?"
                    hide friend1_smirk
                    show friend1_ at right
                    ri "Sounds good, then. Hey, guys, I'm gonna go take a shower, so see you at dinner, alright?"
                    j "Yeah, me too. I'm outta here. I'll be back when I smell a little less like a gorilla."
                    k "That makes all three of us. See you after dinner!"
                    scene bg night
                    ri bright"Alright, it's 8:20. Now I'm ready to sneak over. I've already made sure I have everything I'll need tomorrow in my overnight bag."
                    play sound ("knock.mp3")
                    "Knock, knock"
                    ri smirk " *Whispers* Hey there, guys, it's me, [ri]."
                    "The door is silently pulled inwards and light spills into the dark hallway."
                    "An unidentifiable silhouette tugs me by the arm into the room and quickly shuts the door behind me, stuffing a cloth into the cracks of the door so the light does't escape."
                    scene bg dormnightlight
                    with flash
                    show friend1_angry at right
                    
                    k "Hey there. Why'd you make us wait so long? You big meanie."
                    ri oops "I look down and check my watch, 8:29."
                    j "Heyo, you're here! Ok it's finally time to pull out the goodies."
                    hide friend1_angry
                    show friend1_bright at right
                    show friend2_bright at center with Dissolve(.7)
                    j "We didn't want to start without you [ri]."
                    "Kilia grabs a bottle from the mini fridge on the dresser and tosses it over to Jordan and is about to toss one over to me as well."
                    ri shock "What will you do?"
                    hide friend1_bright
                    hide friend2_bright
                    
                    menu:
                        "Say no":
                            ri nervous "Nah, I'm fine. I'm such a lightweight anyway so it's best if I don't."
                            show friend1_yeah
                            k "Hey whatever, that's cool [ri]."
                            hide friend1_yeah
                        "Say yes":
                            "I hold up my hands to catch the bottle."
                            show friend1_laugh
                            k "Haha, alright , here you go!"
                            "She tosses the bottle and I easily catch it."
                            hide friend1_laugh
                        "Don't respond":
                            show friend1_sign
                            k "Huh? oh, hey if you don't wanna that's totally fine [ri]."
                            k "We're just tryin to relax, not pressure you or anything."
                            hide friend1_sign
                    show friend1_bright at right with Dissolve(.5)
                    show friend2_bright at center with Dissolve(.5)
                    ri nervous "So... are we gonna play a game or something"
                    j "Oh, right! So we got a choice of games and puzzles"
                    "What would you like to do?"
                    hide friend1_bright
                    hide friend2_bright
                    
                    menu:
                        "word salad!":
                            ri"let's do some cool game!"
                            j "Yeah, sure! let's write some random story by ourselves."
                            j "Ok!"
                            python: 
                                Adjective1 = renpy.input("enter an adjective")
                                Adjective1 = Adjective1.strip()
                                Time = renpy.input("enter hour and minute")
                                Time = Time.strip()
                                Verb1 = renpy.input("enter a verd ending in ing")
                                Verb1 = Verb1.strip()
                                Noun = renpy.input("enter one thing, a noun")
                                Noun = Noun.strip()
                                Bodypart = renpy.input("enter a body part")
                                Bodypart = Bodypart.strip()
                                Adjective2 = renpy.input("enter an adjective")
                                Adjective2 = Adjective2.strip()
                                Verb2 = renpy.input("enter a verd")
                                Verb2 = Verb2.strip()
                                Verb3 = renpy.input("enter a verb in the past")
                                Verb3 = Verb3.strip()
                                Name = renpy.input("enter a name")
                                Name = Name.strip()
                            j "let's see what the stoy we did!"
                            narration "Oh my gosh, a [Adjective1] thing just happened to me yesterday. At [Time], when I was [Verb1],a [Noun] looked at me. It had no [Bodypart]. I tried to [Verb2] but it did nothing. After a few second, it [Verb3] me. I was too[Adjective2] and coudn's say anything. Luckily, [Name] came and everthing was over."
                        "seems like this is the only game we have now!":
                            ri welcome "maybe next time!"
                           
                    play sound ("door open.mp3")
                    show friend2_surprise with vpunch
                    "Creeeaak"
                     
                    j "Huh... oh?"
                    hide friend2_surprise
                    show matis
                    d "Hmm! What have we here?"
                    d "First-day students breaking curfew..."
                    d "Sneaking out and about at night..."
                    hide matis
                    show matisserious
                    d "In possession of alcohol on school grounds..."
                    d "Tut, tut."
                    d "You should know this is easily grounds for expulsion, especially given the recent tensions and threats from rival schools."
                    d "I don't believe the headmaster is in a forgiving mood at the moment."
                    t "..."
                    j "..."
                    ri sad2 "..."
                    hide matisserious
                    show matissad
                    d "Hmph! Lucky for you, I am feeling forgiving today, unlike your headmaster."
                    d "Be grateful and get to your own bed. It's late out, none of us should even be awake."
                    hide matissad 
                    show matis
                    "None of us are able to look Dr. Matis in the eye as we all gather our things together and walk out the door. As I pass him on the way out, Dr. Matis grabs my arm and leans in to say something."
                    d "...Meet me in my room at 1:00. I need to confirm something."
                    ri oops "I stare bewildered as I walk away, wondering what it is he'd want to talk to me about. Hopefully nothing bad!"
                    ri oops "Oh goodness, hopefully he doesn't want to rescind his 'forgiveness or anything..."
                    ri cry "It's 12:50. I'm about to sneak of of my room for the second time tonight, although this time there's an entirely different roiling in the pit of my stomach."
                    scene bg hallway
                    ri sad2"I feel my way through the hallways that eerily remind me of a nightmarish reccurence of the first time I was lost in them."
                    ri sad2"Once I reach the door th enter class 1A, and I hesitate."
                    ri oops"I want to turn back, now."
                    ri oops"Something about this atmosphere spells trouble."
                    ri shock" The door cracks open. A shadowed face appears from the dark within, peering through to examine the contents of the hall outside."
                    ri shock"I can feel it when his gaze reaches me, and I freeze like a deer in headlights."
                    ri shock "The door opens further, and he gestures me inside."
                    scene bg cla2
                    with flash
                    narration"Inside, the once benign classroom appears mysterious and foreign. Shadows weave across the floor and the windows to the side let in just enough moonlight to emphasize the darkness."
                    narration "Dr. Matis turns to look out the window and begins to speak softly."
                    show matis
                    d "...Yesterday, I know you heard the conversation between myself and another. For the sake of safety, i must assume you heard everything."
                    ri sad1 "Huh? Oh, no- really I only accidentally caught a bit of conversation but I've no idea what it--"
                    hide matis
                    show matissad
                    d "Enough! I haven't called you here to interrogate you or anything- as if I would believe that anyway. Instead, /i have a proposal for you."
                    ri oops "Huh?"
                    d "I was sent her to keep an eye on the local coming and goings by the Laguardian Rival School."
                    hide matissad
                    show matis
                    d "From the very first moment I got here though, someone had already discovered my true identity and tried to run off with it."
                    d "Of course, you still haven't said anything, so I've got to wonder... maybe you're interested in what I'm doing?"
                    ri nervous "Ummmm, honestly, Sir--"
                    hide matis
                    show matisserious
                    d "No more lies! What did I say before?"
                    d "... Anyway, with that thought in mind, I invited you here so I could gauge your interest."
                    d "So? Are you interested?"
                    ri oops "I'm sorry to disapoint, Sir--"
                    d "Keep in mind, I have the materials necessary to expel you in an instant if I hear something I don't like."
                    d "Now go on, what were you going to say?"
                    hide matisserious
                    menu:
                        "...Very well, Sir. I'll do whatever you ask, just don't expel me, please.":
                            ri nervous "...Very well, Sir. I'll do whatever you ask, just don't expel me, please."
                            show matissmile
                            d "Now that's what I was hoping you'd say [ri]! Funny how it all works--"
                            play sound ("door open.mp3")
                            
                            "Creeeaaak"
                            hide matissmile
                            show matis
                            d "Huh? Headmaster?"
                            d "Oh crap! Run!"
                            hide matis with Dissolve(.7)
                            narration "You can play minigame 2 down below, then continue the story."
                            show headmaster with Dissolve(0.6)
                            h "Well, well, look what we've got here. A few rats to be flushed out!"
                            menu:
                                "GAME OVER: EXPULSION!":
                                    "Stick to your morals, even in strange or bad situations."
                                    return
                        "Oooh, spying? Fun! Sign me up, I don't care what it's for!":
                            ri smirk "Oooh, spying? Fun! Sign me up, I don't care what it's for!"
                            show matissmile
                            d "Now that's what I was hoping you'd say [ri]! Funny how it all works--"
                            play sound ("door open.mp3") 
                            
                            "Creeeaaak"
                            hide matissmile
                            show matis
                            d "Huh? Headmaster?"
                            d "Oh crap! Run!"
                            hide matis with Dissolve(.7)
                            "You can play minigame 2 down below, then continue the story."
                            show headmaster with Dissolve (.6)
                            h "Well, well, look what we've got here. A few rats to be flushed out!"
                            menu:
                                "GAME OVER: EXPULSION!":
                                    "Stick to your morals, even in strange or bad situations."
                                    return
                        "No.":
                            ri mad "...It still doesn't quite sit right with me. And...sir? Don't forget, now I've got material on you too, so please don't bother me with this again."
                            show matisserious
                            d "Hmm, that's not what I was hoping you'd say [ri]. Too bad it couldn't work out--"
                            play sound ("door open.mp3") 
                            
                            "Creeeaaak"
                            d "Eh? [ri]? Ugh, stop running!"
                            hide matisserious with Dissolve (.5)
                            narration "You can play minigame 2 down below, then continue the story."
                            show headmaster with pixellade
                            h "Well, well, look what we've got here. Dr. Matis, you're fired. I expect you out by morning."
                            h " [ri], you've done well not to be misguided by this man's disloyalty."
                            menu:
                                "CONGRATULATIONS! YOU MADE IT TO THE END!":
                                    "Final message, stick to your morals, even in strange or poor situations."
                                    return
                #--------------------------------------------------------------------------------------------------------------------------------------                    
                "Boy":
                    hide rui
                    hide rin
                    show rinsad1 at left
                    show ruibright at right
                    "Ok! Your character is ready! You may now begin the morality storyline."
                    hide rinsad
                    hide ruibright
                    scene bg start with pixellade
                    
                    ru smiles "I open my eyes to see I'm sitting in an office with a large bookcase resting against one wall. Expansive windows let in the morning light from the left side of the room."
                    
                    show headmaster1 
                    with Dissolve(.5)
                    ru smiles "Across from me an imposing man stared at me across the large oak table that we've been sitting at for the past hour."
                
                    #show teacher with folder
                    ru smiles "The man is holding a large and imposing folder in his left hand."
                    t "You've been assigned under Dr. Matis with the rest of class 1A."
                    hide headmaster1
                    show headmaster2
                    #hide teacher with folder
                    #show teacher look up right
                    t "You are to meet them Orientation at 7:00 which means you have twenty minutes until you have to be in the Auditorium."
                    #hide teacher
                    #show teacher smiles
                    t "It's just past the Cafeteria."
                    "The imposing man stares at you for a few more moments, but then he leaves."
                    hide headmaster2
                    with Dissolve (.4)
                    $renpy.pause(.5)
                    
                    show ruisign
                    with Dissolve(.4)
                    "Whew! That was stressful, but at long last, I've passed the final interview!"
                    hide ruisign
                    show ruisuperhappy
                    "I DID IT!"
                    "I finally made it into the Epannian School of Strategy!"
                    "I can now proudly say that I am a student of the most prestigious school in my country, Padelia."
                    hide ruisuperhappy
                    
                    scene bg door
                    with flash
                    play sound ("door open.mp3")
                    ru smiles "I rose to stand in front of the door and touched the cool door handle. The door released a low groan as I pushed it open and left the room."
                    
                    ru sad2 "The hallway is completely deserted."
                    ru sad2 "I hesitate for a moment."
                    "Do you want to go straight to the auditorium or would you rather explore your new home for the next four years?"
                    menu:
                        "Auditorium":
                            scene bg locker
                            with flash
                            $ renpy.pause (.8)
                            scene bg door
                            with flash
    
                            ru superhappy "Alright! I set off in the direction I believe the cafeteria is in..."
                            
                            "But I quickly remember I don't know where anything is, or even where I am!"
                            show ruidizzy
                            "I quickly look around and realize I am in an unmarked hallway. Oh Goodness!"
                            hide ruidizzy
                        "Explore":
                            
                            ru laugh "Excellent! I turn on my heel and pick a random direction to investigate. This should be fun!"
                            ru smiles "For the most part, the building is uninhabited."
                            ru welcome "All the current students are elsewhere, probably either in class or in a tactical battlefield simulation."
                    ru oops "As I stride past another dark, unmarked door, I hear something break the monotonous sound of my footsteps."
                    ru oops "Hushed voices are leaking past the door up ahead on my right."
                    
                    #creepy voice if possible
                    play sound ("whispering.mp3")
                    z "...tensions out of hand"
                    z "... somehow ..." 
                    z "must find out their plans..."
                    y "... but what about the recent..."
                    y "... security increase..."
                    y "... threats..."
                    play sound ("whispering.mp3")
                    y "... not enough information..."
                    z "... sigh..."
                    z "... it is what it is..."
                    z "... contact..."
                    z "... know what to do..."
                    " Do you want to keep listening?"
                    stop sound
                    menu:
                        "Yes":
                            play sound("whispering.mp3")
                            ru smirk "I inch closer to the door as my heartbeat pounds in my ears."
                            ru smirk "The voices inside seem to hush even further."
                            ru mad "What's going on?"
                            
                            show ruisurprise
                            with Dissolve (.3)
                            "Threats?"
                            "Contact who?"
                            "Find what out?"
                            "I lose myself in my thoughts about what's going on."
                            hide ruisurprise
                        "No":
                            ru mad "I stumble back from the previously unnoticeable door that now seems to hold so many secrets."
                            ru mad "What's going on?"
                            show ruishock
                            with Dissolve(.3)
                            "Threats?"
                            "Contact who?"
                            "Find what out?"
                            "I lose myself in my thoughts about what's going on."
                            hide ruishock
                    ru dizzy "I lose my train of thought with a jolt. I look around and remember that I am still completely and utterly lost!"
                    show ruishock at center with hpunch
                    "Oh no! There's only two minutes until 7:00!"
                    "I start running, but by the time I break around the corner of yet another unmarked hallway, I realize it's hopeless."
                    hide ruishock with Dissolve(.4)
                    ru sign "I bent over gasping with my hands on my knees when I hear a new set of footsteps rounding the corner in front of me."
                    ru oops"Looking up, I see a stern man in an unknown uniform walking toward me. Before i can register anything else, he's already standing in front of me."

                    show matis at center
                    "How will you address the man?"
                    menu:
                        "Address him as sir and offer a salute":
                            "Sir."
                            u "Student. You've got a minute to report to the Auditorium. What are you doing here?"
                            hide matis
                            show matisserious
                            ru oops "Sir, I am aware of the urgency, but I am new and seem to have lost my way, Sir."
            
                            ru nervous "If you could point me in the right direction...?"
                            hide matis serious
                            show matis 
                            
                            "The man sighs and cocks his head towards the corner at the other end of the hall."
                            hide matis
                            show matissmile
                            u "You can follow me. I'm also headed in that direction."
                            hide matissmile with Dissolve(.4)
                        "Ask the man who he it":
                            ru oops"The weight of his stare bares down on my neck. The stern man suddenly grips me by the ear and begins walking again, dragging me alongside him."
                            ru cry "My eyes are watering and I realize he must be a teacher here."
                            show matisserious at center with Dissolve(.4)
                            u "Ugh... Rookies. You know you're supposed to be in the auditorium in..."
                            "The man checks his watch and lets out a sigh."
                            hide matisserious
                            show matis
                            u "30 seconds. What's your name kid?"
                            ru oops "I squirm uncomfortably."
                            ru nervous"I am [ru]. Are you taking me to the Auditorium now?"
                            u "No more questions squirt, and try to keep your trap shut on the way."
                            hide matis
                        "Ignore him and try to catch your breath. You don't know him.":
                            ru smiles"I avoided eye contact, but the man just wasn't having it."
                            u "You there! Newbie! You've got a minute to report in the Auditorium."
                            show matisserious
                            u "Quit dawdling and get moving!"
                            ru sad2 "..."
                            u "SCRAM!" with hpunch
                            "The man makes a shooing motion with his hands and shakes his head in annoyance."
                            #hide stranger and show other expression
                            hide matisserious
                            show matis
                            u "Ugh, nevermind. I bet you don't even know where it is. Come on, kid. It's this way"
                            hide matis with Dissolve (.5)
                            
                        "Avoid eye contact, he's scary":
                            ru oops "The man's stare softened as he appraised me."
                            show matis
                            u "Excuse me, you're a new student correct?"
                            hide matis
                            show matissmile
                            u "There's only a minute until report time for the Orientation. What's your name?"
                            ru nervous "My...My name is [ru]. Um... Could you please show me where the Auditorium is? I'm lost..."
                            hide matissmile
                            show matis
                            "The man sighed and cocked his head towards the corner at the other end of the hall."
                            #show rin at the corner
                            u "You can follow me. I'm headed there as well."
                            hide matis
                    scene bg aud
                    with flash
                
                    ru sign "Whew. I just managed to slip in with the crowd of last-second students and snatch a seat. The mystery man walked off somewhere as soon as the Auditorium was in view."
                    ru bright "He seemed a little rough around the edges, but he did bring me along when he could've just left me to wander the halls."
                    ru bright "Huh, it wouldn't be a stretch to imagine him doing it though."
                    "I snap back to reality and focus on the stage as the headmaster appears to introduce all the teachers."
                    show headmaster
                    ru surprise "Whoa! The man I met is up there too! He stands up as the head moves on to begin introducing him."
                    #show rin at the corner
                    h "And here is our most recent addition to the staff here at Epannian, Dr. Matis!"
                    show matis at right
                    with Dissolve (.6)
                    h "He'll be teaching Espionage Tactics and is the homeroom teacher to class 1A."
                    hide matis with Dissolve(.5)
                    h "Next up is Mrs. Spannend...."
                    "The rest of Orientation droned on as all the teachers returned to their seats and the head began talking about the pride of the school and upcoming exams."
                    "It all came to a close with a speech from the student body president of the freshmen and a final remark from the deputy headmaster."
                    "Later........."
                    scene bg dormnightlight
                    with pixellade
                    show ruilaugh 
                    "Wow. A day full of tours and clubs dragging me over to join. I fall back on my small bed and close my eyes to the unfamiliar dorm around me."
                    "Wow...what a long day! I'm ready to pass out. Hopefully the night lasts long enough to get a good rest."
                    hide ruilaugh
                    show ruibright
                    "I smile to myself and think of my day and my family that were back home."
                    "Oh! They must be wondering how the final interview went."
                    hide ruibright
                    show ruisuperhappy
                    "Maybe Mom will pick up if I call."
                    "Do you want to call Mom now or in the morning?"
                    hide ruisuperhappy
                    menu:
                        "Now":
                            "I dig around my bag for the cheap phone mom bought me, so I could keep in touch while at school, and press speed dial one."
                            ru smiles"Riing..."
                            ru smiles"Riing..."
                            ru smiles"Riing..."
                            ru supperhappy"Rii-- Click"
                            ru superhappy "Mom?"
                            #show rin at the corner
                            scene bg home
                            with Dissolve(.5)
                            show mom
                            #------------------------------------------------------------------------------------
                            m "Hello? Oh, [ru] sweetie! I've been waiting all day! So...? How'd it go?"
                            ru laugh"Eeeee! I made it!! Haha! I made it into Epannian!"
                            m "Oh my goodness! Oh... I'm so proud of you, [ru]. My baby, you've made your sisters and I so proud. Oh Honey..."
                            hide mom
                            show momhappy
                            "I can hear her happily tearing up on the other end."
                            hide momhappy
                            show mom
                            m "*sniffle*...Oh! Before I go, sweetie, I want to let you know-- be careful anytime you go out, ok [ri]?"
                            hide mom
                            show momsad
                            m "There's been a lot in the news about threats on Epannian students from rival schools."
                            m " I know you'll have buddies who want to hang out but be sure you're careful."
                            m "I worry so much for you now that you're so far away.... Be safe, ok hun?"
                            ru oops" My mind whirrs as I connect the conversation I overheard earlier today to the news of threats on the other students here."
                            m "...Sweetie?"
                            hide momsad
                            show mom
                            ru bright "Oh, of course Mom, I'll keep my guard up. You don't have to worry."
                            ru smiles"I promise."
                            m "*Sniffle* ...Alright, [ri]. I love you. Hmm, but don't forget to have fun, too. Do your best while you're there! Bye..."
                            "Click"
                            hide mom
                           #-------------------------------------------------------------------------------------- 
                            scene bg dormsleep
                            show rui
                            "Hmmmm. I collapse back down onto the duvet and start nodding off."
                            "Time to sleep I guess."
                            hide rui
                            with Dissolve (.5)
                            "I fall asleep in my clothes and dream deeply of home and happy childhood moments."
                            scene bg dormday with vpunch
                            "BEEP...BEEP...BEEP...BE-"
                            show ruidizzy with hpunch
                            "Urgh.... what.... where...?"
                            show ruibright
                            "Oh, right. Epannian!"
                            
                        "In the Morning":
                            scene bg dormsleep
                            show ruibright
                            "Yeah... It's already so late. It's probably best to let her rest and just check in when morning comes."
                            "I'll just have to set my alarm early."
                            hide ruibright
                            with Dissolve(1.)
                            "Aaah, finally time for sleep."
                            " I fall asleep in my clothes and dream deeply of home and happy childhood moments."
                            scene bg dormday with vpunch
                            "BEEP...BEEP...BEEP...BE--"
                            show ruidizzy with hpunch
                            "Urgh.... what..... where...?"
                            hide ruidizzy
                            show ruisurprise
                            "Oh, right. Mom. Where....my phone...?"
                            "I dig around the blankets wrapping me until I find the cheap phone mom bought me, so I could keep in touch while I'm at school, and press speed dial one."
                            hide ruisurprise
                            show run 
                            "Riing..."
                            "Riing..."
                            "Riing..."
                            "Rii- Click"
                            scene bg home
                            with flash
                            show momangry
                            m "Hello? Oh, [ru]! You meanie! You made me wait so long to hear the news!"
                            #---------------------------------------------------------------------------------
                            m "So...? How'd it go?"
                            hide momangry
                            show mom
                            ru superhappy"...Oh Yeah! I made it!! Haha! I made it into Epannian!"
                            ru superhappy"I glance around and survey the dorm I didn't bother to check out last night."
                            ru bright"There's a small bed, a desk, a tiny dresser, with a mini fridge beside it and a window that divide the wall across from the bed in half."
                            ru bright"Aside from that, the room is barren. A typical freshman's room."
                            m"Oh my goodness! Oh... I'm so proud of you, [ru]. My baby, you've made your sisters and I so proud. Oh honey..."
                            hide mom
                            show momhappy
                            
                            "I can hear her tearing up on the other end."
                            m "*sniffle*...Oh! Before I go, sweetie, I want to let you know-- be careful anytime you go out, ok [ru]?"
                            hide momsuperhappy
                            show momsad
                            
                            m "There's been a lot in the news about threats on Epannian students from rival schools."
                            m " I know you'll have buddies who want to hang out but be sure you're careful."
                            m "I worry so much for you now that you're so far away.... Be safe, ok hun?"
                            " My mind whirrs as I connect the conversation I overheard yesterday to the news of threats on the other students here."
                            m "...Sweetie?"
                            hide momsad
                            show mom
                            ru smiles "Oh, of course Mom, I'll keep my guard up. You don't have to worry."
                            ru bright"I promise."
                            m "*Sniffle* ...Alright, [ru]. I love you. Hmm, but don't forget to have fun, too. Do your best while you're there! Bye..."
                            "Click"
                            hide mom
                        #-------------------------------------------------------------------------------------
                    scene bg dormday
                    with Dissolve(.5)
                    "Later..."
                    show ruiwelcome
                    "Hmmmm... I guess I'll just follow the crowd to find the cafeteria again."
                    "A steady trickle of people leads to the doors of the massive building."
                    hide ruibright
                    scene bg caf
                    with flash
                    ru surprise "Oh wow! So many students here! I wander over to the line and peek over shoulders to get a glimpse of the menu."
                    ru smiles"As I strain to stay on my tiptoes, I feel a finger tapping my shoulder."
                    show friend2_ at center with move
                    with Dissolve(.4)
                    gu "Hey, do you want a menu?"
                    "In the boy's other hand is a paper printout of the menu on the wall."
                    
                    ru oops "Huh?"
                    show friend1_ at right with move
                    gi "He said a menu, silly!"
                    #show rineee
                    ru eee"Oh. Um, sure. Thank you!"
                    #hide rineee
                    hide friend2_
                    hide friend1_
                    show friend1_welcome at right 
                    show friend2_bright at center
                    gi "Haha! No problem! I'm Kilia, this guy here is Jordan."
                    k "We're in the Tactical Communications department, what about you?"
                    ru superhappy "Oh, neat! I'm [ru] also in the Tactical Comms department."
                    #show rin at the corner
                    ru bright "What about your homeroom?"
                    hide friend1_welcome
                    hide friend2_bright
                    show friend2_sign at center
                    show friend1_ at right
                    j "Matis. I got a look at him at the Orientation. Seems like he's not gonna let us lack on homework, that's for sure."
                    k "Um, ew! C'mon..."
                    #show rin at the corner sad
                    ru smiles"Actually, I ran into him before the Orientation. He found me when I was lost and helped me back and all. I don't think he likes me though..."
                    hide friend1_
                    show friend1_oops at right
                    k "I get the feeling he just doesn't like any of us. Ha, see? He's over there in the corner, staring us all down."
                    hide friend2_sign
                    show friend2_surprise at center
                    j "Whoa! That's creepy."
                    #hide guy
                    #show guy 2 surprise
                    ru surprise "Huh, I never would have noticed he was there."
                    hide friend1_oops
                    hide friend2_surprise
                    show friend1_bright at right
                    show friend2_bright at center
                    k "Let's just finish up and go to class. I don't wanna risk being stared at like that if we're late."
                    ru bright"I finish up breakfast and leave the cafeteria to search for class 1A with my new friends."
                    hide friend1_bright 
                    hide friend2_bright
                    scene bg cla2
                    with Dissolve(.5)
                    play sound ("bell.mp3")
                    " As soon as we cross the threshold into the room, the late bell sounds and we breathe a collective sigh of relief as you meander over to the last three available seats..."
                    "... at the very front."
                    "I hear the same clunking footsteps from yesterday enter the room just as we've all sat down."
                    show matis at center with move
                    "All the students settle down and wait silently for him to speak."
                    hide matis
                    show matisserious
                    d "Any questions? No?"
                    d "Good, then let's get started on what we came here to do."
                    d "First things first, we've got written and physical exams."
                    hide matisserious
                    show matis
                    d "We'll use this to measure your potential and progress throughout the year."
                    d "Last place student is expelled."
                    d "Prepare yourselves."
                    hide matis
                    narration"The test is insert outside of the game! Finish the test then come back here"
                    play sound("school bell.mp3")
                    "Ding, Dong, Ding, Dong, ....Ding, Dong, Ding, Dong"
                    show matis
                    d "That's it everyone! Class dismissed!"
                    hide matis
                    show friend1_sign at center
                    show friend2_sign at right
                    #at the corner
                    ru sign "Aaaaaaahhhhh"
                    "The entire room sighed in relief."
                    scene bg locker
                    with Dissolve(.7)
                    show ruibright at center
                    show friend1_sign at right
                    show friend2_ at left
                    k "Oh. My. God. What a day!"
                    k "I swear he was looking to kill one of us!"
                    k "Poor Debbie got it the worst, it was like he was intent on really ruining her day. All she did was sneak a bite of leftover breakfast!"
                    hide friend1_sign
                    show friend1_ at right
                    hide friend2_
                    show friend2_sign at left
                    j "No kidding. Ughhh. Not like he eased up on us either. Nooo, he had to make us run a freaking marathon on day one!"
                    hide ruibright
                    show ruilaugh at center
                    ru "Haha, yeah, are we gonna sleep well tonight or what. Wow."
                
                    k "Oh, [ru], speaking of tonight..."
                    hide friend1_
                    show friend1_smirk at right
                    hide friend2_sign
                    show friend2_eee at left
                    hide ruilaugh
                    show rui
                    "Jordan motions me to come in close and Kilia looks over her shoulder before turning back to face me."
                    j "We were thinking we all meet up in my room after dinner and spend our first night cooling off and relaxing."
                    j "Nothing crazy, just some fun."
                    hide rui
                    show ruibright
                    ru "Um, sure, I guess. What room? I wanna grab my clothes before coming over."
                    k "105. We're meeting there at 8:30, so don't be late, kay?"
                    hide friend1_smirk
                    show friend1_ at right
                    ru "Sounds good, then. Hey, guys, I'm gonna go take a shower, so see you at dinner, alright?"
                    j "Yeah, me too. I'm outta here. I'll be back when I smell a little less like a gorilla."
                    k "That makes all three of us. See you after dinner!"
                    scene bg night
                    ru bright"Alright, it's 8:20. Now I'm ready to sneak over. I've already made sure I have everything I'll need tomorrow in my overnight bag."
                    play sound ("knock.mp3")
                    "Knock, knock"
                    ru smirk " *Whispers* Hey there, guys, it's me, [ru]."
                    narration "The door is silently pulled inwards and light spills into the dark hallway."
                    "An unidentifiable silhouette tugs me by the arm into the room and quickly shuts the door behind me, stuffing a cloth into the cracks of the door so the light does't escape."
                    scene bg dormnightlight
                    with flash
                    show friend1_angry at right
                    
                    k "Hey there. Why'd you make us wait so long? You big meanie."
                    ru oops "I look down and check my watch, 8:29."
                    j "Heyo, you're here! Ok it's finally time to pull out the goodies."
                    hide friend1_angry
                    show friend1_bright at right
                    show friend2_bright at center with Dissolve(.7)
                    j "We didn't want to start without you [ru]."
                    "Kilia grabs a bottle from the mini fridge on the dresser and tosses it over to Jordan and is about to toss one over to me as well."
                    ru shock "What will you do?"
                    hide friend1_bright
                    hide friend2_bright
                    
                    menu:
                        "Say no":
                            ru nervous "Nah, I'm fine. I'm such a lightweight anyway so it's best if I don't."
                            show friend1_yeah
                            k "Hey whatever, that's cool [ru]."
                            hide friend1_yeah
                        "Say yes":
                            "I hold up my hands to catch the bottle."
                            show friend1_laugh
                            k "Haha, alright , here you go!"
                            "She tosses the bottle and I easily catch it."
                            hide friend1_laugh
                        "Don't respond":
                            show friend1_sign
                            k "Huh? oh, hey if you don't wanna that's totally fine [ru]."
                            k "We're just tryin to relax, not pressure you or anything."
                            hide friend1_sign
                    show friend1_bright at right with Dissolve(.5)
                    show friend2_bright at center with Dissolve(.5)
                    ru nervous "So... are we gonna play a game or something"
                    j "Oh, right! So we got a choice of games and puzzles"
                    "What would you like to do?"
                    hide friend1_bright
                    hide friend2_bright
                    
                    menu:
                        "word salad!":
                            ru"let's do some cool game!"
                            j "Yeah, sure! let's write some random story by ourselves."
                            j "Ok!"
                            python: 
                                Adjective1 = renpy.input("enter an adjective")
                                Adjective1 = Adjective1.strip()
                                Time = renpy.input("enter hour and minute")
                                Time = Time.strip()
                                Verb1 = renpy.input("enter a verb ending in ing")
                                Verb1 = Verb1.strip()
                                Noun = renpy.input("enter one thing, a noun")
                                Noun = Noun.strip()
                                Bodypart = renpy.input("enter a body part")
                                Bodypart = Bodypart.strip()
                                Adjective2 = renpy.input("enter an adjective")
                                Adjective2 = Adjective2.strip()
                                Verb2 = renpy.input("enter a verb")
                                Verb2 = Verb2.strip()
                                Verb3 = renpy.input("enter a verb in the past")
                                Verb3 = Verb3.strip()
                                Name = renpy.input("enter a name")
                                Name = Name.strip()
                            j "let's see what the stoy we did!"
                            narration "Oh my gosh, a [Adjective1] thing just happened to me yesterday. At [Time], when I was [Verb1],a [Noun] looked at me. It had no [Bodypart]. I tried to [Verb2] but it did nothing. After a few second, it [Verb3] me. I was too[Adjective2] and coudn's say anything. Luckily, [Name] came and everthing was over."
                        "Seem like that is the only game we have! ":
                            ru welcome "maybe next time!"
                            
                                
                                    
                    play sound ("door open.mp3")
                    show friend2_surprise with vpunch
                    "Creeeaak"
                     
                    j "Huh... oh?"
                    hide friend2_surprise
                    show matis
                    d "Hmm! What have we here?"
                    d "First-day students breaking curfew..."
                    d "Sneaking out and about at night..."
                    hide matis
                    show matisserious
                    d "In possession of alcohol on school grounds..."
                    d "Tut, tut."
                    d "You should know this is easily grounds for expulsion, especially given the recent tensions and threats from rival schools."
                    d "I don't believe the headmaster is in a forgiving mood at the moment."
                    t "..."
                    j "..."
                    ru sad2 "..."
                    hide matisserious
                    show matissad
                    d "Hmph! Lucky for you, I am feeling forgiving today, unlike your headmaster."
                    d "Be grateful and get to your own bed. It's late out, none of us should even be awake."
                    hide matissad 
                    show matis
                    "None of us are able to look Dr. Matis in the eye as we all gather our things together and walk out the door. As I pass him on the way out, Dr. Matis grabs my arm and leans in to say something."
                    d "...Meet me in my room at 1:00. I need to confirm something."
                    ru oops "I stare bewildered as I walk away, wondering what it is he'd want to talk to me about. Hopefully nothing bad!"
                    ru oops "Oh goodness, hopefully he doesn't want to rescind his 'forgiveness or anything..."
                    ru cry "It's 12:50. I'm about to sneak of of my room for the second time tonight, although this time there's an entirely different roiling in the pit of my stomach."
                    scene bg hallway
                    ru sad2"I feel my way through the hallways that eerily remind me of a nightmarish reccurence of the first time I was lost in them."
                    ru sad2"Once I reach the door th enter class 1A, and I hesitate."
                    ru oops"I want to turn back, now."
                    ru oops"Something about this atmosphere spells trouble."
                    ru shock" The door cracks open. A shadowed face appears from the dark within, peering through to examine the contents of the hall outside."
                    ru shock"I can feel it when his gaze reaches me, and I freeze like a deer in headlights."
                    ru shock "The door opens further, and he gestures me inside."
                    scene bg cla2
                    with flash
                    narration "Inside, the once benign classroom appears mysterious and foreign. Shadows weave across the floor and the windows to the side let in just enough moonlight to emphasize the darkness."
                    narration "Dr. Matis turns to look out the window and begins to speak softly."
                    show matis
                    d "...Yesterday, I know you heard the conversation between myself and another. For the sake of safety, i must assume you heard everything."
                    ru sad1 "Huh? Oh, no- really I only accidentally caught a bit of conversation but I've no idea what it--"
                    hide matis
                    show matissad
                    d "Enough! I haven't called you here to interrogate you or anything- as if I would believe that anyway. Instead, /i have a proposal for you."
                    ru oops "Huh?"
                    d "I was sent her to keep an eye on the local coming and goings by the Laguardian Rival School."
                    hide matissad
                    show matis
                    d "From the very first moment I got here though, someone had already discovered my true identity and tried to run off with it."
                    d "Of course, you still haven't said anything, so I've got to wonder... maybe you're interested in what I'm doing?"
                    ru nervous "Ummmm, honestly, Sir--"
                    hide matis
                    show matisserious
                    d "No more lies! What did I say before?"
                    d "... Anyway, with that thought in mind, I invited you here so I could gauge your interest."
                    d "So? Are you interested?"
                    ru oops "I'm sorry to disapoint, Sir--"
                    d "Keep in mind, I have the materials necessary to expel you in an instant if I hear something I don't like."
                    d "Now go on, what were you going to say?"
                    hide matisserious
                    menu:
                        "...Very well, Sir. I'll do whatever you ask, just don't expel me, please.":
                            ru nervous "...Very well, Sir. I'll do whatever you ask, just don't expel me, please."
                            show matissmile
                            d "Now that's what I was hoping you'd say [ru]! Funny how it all works--"
                            play sound ("door open.mp3")
                            
                            "Creeeaaak"
                            hide matissmile
                            show matis
                            d "Huh? Headmaster?"
                            d "Oh crap! Run!"
                            hide matis with Dissolve(.7)
                            narration"You can play minigame 2 down below, then continue the story."
                            show headmaster with Dissolve(0.6)
                            h "Well, well, look what we've got here. A few rats to be flushed out!"
                            menu:
                                "GAME OVER: EXPULSION!":
                                    "Stick to your morals, even in strange or bad situations."
                                    return
                        "Oooh, spying? Fun! Sign me up, I don't care what it's for!":
                            ru smirk "Oooh, spying? Fun! Sign me up, I don't care what it's for!"
                            show matissmile
                            d "Now that's what I was hoping you'd say [ru]! Funny how it all works--"
                            play sound ("door open.mp3") 
                            
                            "Creeeaaak"
                            hide matissmile
                            show matis
                            d "Huh? Headmaster?"
                            d "Oh crap! Run!"
                            hide matis with Dissolve(.7)
                            narration "You can play minigame 2, then continue the story."
                            show headmaster with Dissolve (.6)
                            h "Well, well, look what we've got here. A few rats to be flushed out!"
                            menu:
                                "GAME OVER: EXPULSION!":
                                    "Stick to your morals, even in strange or bad situations."
                                    return 
                        "No.":
                            ru mad "...It still doesn't quite sit right with me. And...sir? Don't forget, now I've got material on you too, so please don't bother me with this again."
                            show matisserious
                            d "Hmm, that's not what I was hoping you'd say [ru]. Too bad it couldn't work out--"
                            play sound ("door open.mp3") 
                            
                            "Creeeaaak"
                            d "Eh? [ru]? Ugh, stop running!"
                            hide matisserious with Dissolve (.5)
                            narration "You can play minigame 2 down below, then continue the story."
                            show headmaster with pixellade
                            h "Well, well, look what we've got here. Dr. Matis, you're fired. I expect you out by morning."
                            h " [ru], you've done well not to be misguided by this man's disloyalty."
                            menu:
                                "CONGRATULATIONS! YOU MADE IT TO THE END!":
                                    "Final message, stick to your morals, even in strange or poor situations."
                                    return
                        
                    
        "Awareness":
            scene bg background2
            with Dissolve (.5)
            "You are about to start the Awareness route! But, before you do, please select a character."
            show irisbright at left
            with Dissolve (.4)
            show iida at right
            with Dissolve (.4)
            "Are you a girl or a boy?"
            menu:
                "Girl":
                    
                    show irisbright at left
                    show iida sad at right
                    "Congratulations! Your character [ir] is ready to begin the game!"
                    scene bg start with pixellade
                    narration "I open my eyes to see I'm sitting in an office with a large bookcase resting against one wall. Expansive windows let in the morning light from the left side of the room."
                    ir smiles "There is a tall woman standing across from me at the other end of the dark mahogany table I've been seated at for the last hour."
                    show jenner
                    "The woman holds an imposing file in her left hand."
                    hide jenner
                    show jennersmile
                    t "[ir], you've been assigned under Dr. Jenner with the rest of class 1A."
        
                    t "You are to meet them for Orientation at 7:00. That means you have twenty minutes until report time in the Auditorium. It's just past the cafeteria."
                    hide jennersmile
                    show jenner
                    " The tall lady levels a stare at me, then turns to exit."
                    ir sign "Whew! That was stressful, but at long last, I've passed my final interview."
                    ir bright"Yes! I've finally made it into the Laguardian School of Strategy and on full scholarship too!"
                    ir bright "Now my family won't have to worry anymore about me, and I won't be putting more financial burden on them."
                    ir smiles "I stand up and go to the exit."
                    scene bg hallway with flash
                    play sound("door open.mp3")
                    ir smiles "My hand makes contact with the cool door handle and the door releases a low groan as I push it open."
                    ir sad2 "The hallway outside is completely deserted."
                    ir sad2 "I hesitate for a moment."
                    "Do you want to go straight to the Auditorium or would you rather explore your new home for the next four years?"
                    menu:
                        "Auditorium":
                            ir bright"Alright! I set off in the direction I think the cafeteria is in... "
                            ir oops "but I quickly encounter a critical problem. I don't have a clue where anything is, or even where I am now."
                            ir dizzy"I look around me and find I'm already hopelessly lost in an unmarked hallway."
                            ir dizzy"Crap."
                        "Explore":
                            ir laugh "Excellent! I turn on my heel and pick a random direction to explore."
                            ir laugh"This should be fun!"
                            ir smiles "For the most part, the building is uninhabited as all the current students are elsewhere, either in classes or in a tactical battlefield simulation."
                    ir oops "As I stride past yet another dark, unmarked door, I hear something break the monotonous sound of my footsteps."
                    play sound ("whispering.mp3")
                    "Someone down the hall is humming the national anthem."
                    ir nervous "...Hello? Who's there?"
                    ir oops "I get no response and the empty hall provides no clue as to who was there."
                    ir nervous"Ummm... I heard you earlier. That was the national anthem, right?"
                    
                    "A moment passes, but soon a voice rings out, and it's owner rounds the corner not long after the voice sounds."
                    show friend3laugh
                    with pixellade
                    gu "Haha, you got me!"
                    gu "Hey, are you new here? What are you doing so far from the Auditorium?"
                    ir oops "Well I--"
                    hide friend3laugh
                    show friend3bright
                    gu "Whatever, just follow me. Since there's still time before Orientation, I'll give you a tour."
                    ir dizzy "Huh?"
                    "Do you want to go on a tour?"
                    hide friend3bright
                    menu:
                        "Yes":
                            show friend3laugh
                            ir superhappy "Um, sure, I wanted to explore a little anyway."
                            gu "Cool! I'm Ryner by the way. What's your name?"
                            ir superhappy "[ir]"
                            hide friend3laugh
                            show friend3
                            r "Cool."
                            r "Hey, so what course are you in? All freshman have a choice between the Tactical Comms and Business Study departments, right?"
                            hide friend3
                        "No":
                            show friend3bright
                            ir oops "Hmm, no thanks. I'd really rather not risk being late to my first school event."
                            hide friend3bright
                            show friend3sad2
                            gu "Aw, that's lame."
                            hide friend3sad2
                            show friend3bright
                            gu "Well, I'll show you the way at least. It's easy to get lost around here."
                            gu "Hey, it's nice to meet you ...?"
                            ir welcome "[ir]"
                            hide friend3bright
                            show friend3welcome
                            gu "Alright [ir]. I'm Ryner. What department are you studying in? If I remember correctly, you had a choice between Tactical Comms and Business Studies, right?"
                            hide friend3welcome
                    ir smiles "Yeah, that's right. I'm enrolled in Business Study."
                    show friend3superhappy
                    r "Cool! I was too, so if you ever want a different opinion on a project, just ask me, ok?"
                    r "Let me know anytime you need help."
                    ir laugh "Um... sure. Thanks."
                    hide friend3superhappy
                    show friend3mad
                    r "Hey, uh... no offense, but you don't seem too thrilled to be here."
                    ir welcome "None taken, and yeah. I mean, the school's great and all, but I'm mostly here to take the strain off my family. They don't need another mouth to feed hanging around."
                    hide friend3mad
                    show friend3yeah
                    r "Why'd you go through all the trouble to get into this school then if you don't even want to be here? There are so many other places you could get into, why put in the effort for this one?"
                    ir bright "Well... when I graduate, I don't want to go back to being a burden for my family."
                    ir bright"If I get recognized by this school, I'm bound to get a decent job in the government or something."
                    hide friend3yeah
                    show friend3sign
                    r "Jeez. You know, I bet your family wouldn't want you to just slave away your days here. They'd probably want you to enjoy your life too."
                    r "It doesn't all have to be about money and burdens!"
                    ir smiles"I guess."
                    hide friend3sign
                    show friend3angry
                    r "I'm serious!"
                    r "I just mean, your family wouldn't want you to be so hard on yourself, that's all."
                    ir nervous"...."
                    ir oops "Thank you."
                    hide friend3angry
                    show friend3sad2
                    narration "Ryner appears lost in thought. It looks like he is remembering something sad."
                    hide friend2sad2
                    show friend3laugh
                    r "...... OH! Haha, it's nothing, just some passing advice that you probably won't even remember."
                    ir laugh"Nevertheless, thank you."
                    r "Hmmm... Alright! Looks like we've made a full loop around, now we're at the Auditorium."
                    scene bg open
                    narration "A large, squat building stands in front of the two of you."
                    show friend3laugh
                    ir bright "Thanks again."
                    r "Seriously [ir] anytime you want help, just go to dorm 3 and ask around for me."
                    hide friend3laugh
                    show friend3
                    ir laugh"Haha, alright, I will! See you around Ryner."
                    r "Yeah, talk to you later sometime. Good luck at Orientation!"
                    hide friend3
                    with Dissolve (.6)
                    
                    scene bg aud2
                    with flash
                    narration "As the rest of the freshman student body fills into the Auditorium, the Headmaster scales the steps of the stage and begins to address the crowd."
                    show headmaster
                    h"Welcome, everyone, to the Laguardian School of Strategy. Everyone, please look forward to a productive year!"
                    ir smiles "He gives his outlook on life and education, then begins introducing the teaching staff."
                    h "And here is our most recent addition to the staff here at Laguardian, Dr. Jenner! She'll be teaching Macroeconomics and is the homeroom teacher to all you students assigned to class 1A. Next up, is Mr. Spannend..."
                    show jenner at right
                    ir superhappy "Oh, looks like that'll be my teacher for the next year."
                    ir superhappy "I hope she's lenient..."
                    "Suddenly, the kid sitting next to me started whispering to me."
                    hide headmaster with Dissolve(.5)
                    hide jenner with Dissolve(.5)
                    
                    show friend2sign at center with Dissolve(.4)
                    gu "Nah, when I met her in the halls earlier, she snapped at me and Jessica, and I quote, 'to scram' and 'do something worthwhile with our meatsuits.'"
                    ir dizzy "huh?"
                    show friend1sign at right with Dissolve(.4)
                    gi "Yeah, and she even threatened to give us detention for loitering! I'm Jessica, by the way."
                    
                    ir sad2 "Whoa... Looks like we're in for a rough year. Dang it!"
                    hide friend1sign
                    hide friend2sign
                    show friend1sad2 at right
                    show friend2sad2 at center
                    ir sign"... I just wanted to peacefully graduate from this place and support myself."
                    
                    e "Well, as long as she's our teacher, the 'peaceful' part of that might have to be put on hold."
                    hide friend2sad2
                    show friend2 at center
                    e "Hey Seita, you're in class 1A too, right?"
                    hide friend1sad2
                    show friend1bright at right
                    s "Yurp."
                    s "Man, I was really hoping to get a teach who'd ignore it if I forgot my homework."
                    hide friend1bright
                    show friend1sign at right
                    s "This lady looks like she'll whip me if I have a crinkle on the paper!"
                    "The Headmaster on stage calls up the freshman student body representative to give a speech."
                    ir sign "Sigh..."
                    hide friend2sad2
                    show friend2 at center 
                    e "Well- this is Laguardia! We'll take the good and the bad- after all, we put in so much work and time to get in!"
                    s "I second that."
                    narration "The student on stage finishes his spiel and the Head closes Orientation by telling students to meet back here at 1:00 for tours of the grounds."
                    hide friend2welcome
                    hide friend1sign
                    show friend1bright at right
                    show friend2bright at center
                    
                    e "Oh, right! What's your name?"
                    ir "Haha, I forgot to mention! It's [ir]."
                    s "Cool [ir]. See you around!"
                    hide friend1bright with Dissolve(.4)
                    hide friend2bright with Dissolve(.4)
                    
                    scene bg dormnightlight
                    with pixellade
                    ".....Later that day....."
                    show irislaugh with Dissolve (.4)
                    "Wow...what a long day! I'm ready to pass out; hopefully the night lasts long enough to get a good rest."
                    hide irislaugh
                    show irisbright
                    " I crumple onto my dorm room bed and smile to myself."
                    "I think of my day and my thoughts go to my family way back home."
                    hide irisbright
                    show irislaugh
                    "Oh! They must be wondering how the final interview went. Maybe Mom will pick up if I call."
                    "Do you want to call Mom now or in the morning?"
                    hide irislaugh with Dissolve (.5)
                    menu:
                        "Now":
                            show iris
                            "I dig around for the cheap phone mom bought me so I could keep in touch while at school and press speed dial one."
                            "Riing..."
                            "Riing..."
                            "Riing..."
                            hide iris
                            show irissurprise
                            "Rii-- Click"
                            
                            scene bg home
                            with flash
                            show momsad 
                            m "... Hello? Oh, [ir]! You meanie! You made me wait so long to hear the news!"
                            m "So...? How'd it go?"
                            hide momsad
                            show mom
                            ir laugh "...Oh yeah! I made it into Laguardia."
                            ir laugh "Haha, finally you guys can take proper care of yourselves."
                            ir superhappy "Hey, don't go getting any ideas either, ok? I don't want any gifts or anything."        
                            ir smiles"I glance around and survey the dorm I'll be in for the next year."
                            ir bright"There's the small bed, a desk, a tiny dresser with a mini fridge beside it and a window that divides the wall across from the bed in half."
                            ir bright "Aside from that, the room is barren. A typical freshman's room." 
                            hide mom
                            show momhappy
                            m "Oh my goodness! Oh... I'm so proud of you, [ir]."
                            m "My baby, you've made your sisters and I so proud. Oh honey..."
                            "I can hear my mom tearing up on the other end."
                            ir oops "..."
                            hide momhappy
                            show momsad
                            m "*Sniffle*... Oh! Before I go, sweetie, I want to let you know-- be careful, ok [ir]?"
                            m "There's been a lot in the news about Laguardian students turning out to be spies from rival schools."
                            m "I know you'll have buddies who want to hang out but be sure you're cautious."
                            m "I worry so much for you now that you're so far away... Be safe, ok hon?"
                            ir oops "I wonder about all my fellow students"
                            ir sad2 "Ryner, Jessica, Seita... "
                            ir oops  "I can't help but get suspicious."
                            hide momsad
                            show mom
                            m "...Sweetie?"
                            ir laugh "Oh- of course mom, I'll keep my guard up. You don't have to worry." 
                            ir bright "I promise."
                            m "*Sniffle*..."
                            m "Alright, [ir]. I love you."
                            m "Hmm, but don't forget to have fun, too. Do your best while you're there!"
                            m "Bye..."
                            
                            scene bg dormsleep
                            "I collapse back down onto the duvet and feel myself nodding off."
                            ir sad "Aaah. Time for some shuteye."
                            ir "Hmmm...."
                            "...I fall asleep in my clothes and dream deeply of home and distant childhood moments."
                            
                            scene bg dormday
                            with vpunch
                            "BEEP...BEEP... BEEP...BE--"
                            show irisdizzy with hpunch
                            "Urgh... what... where...?"
                            hide irisdizzy
                            show irisbright
                            "Oh, right. Laguardia..."
                        "Later":
                            show irisbright
                            ir"Yeah... it's already so late- probably best to let her rest and just check in when morning comes."
                            ir "I'll have to set my alarm early, though."
                            hide irisbright
                            show irislaugh
                            ir"Aaaah. Time for some shuteye."
                            ir "Hmmmmm....."
                            hide irislaugh with Dissolve(.5)
                            "I fall asleep in my clothes and dream deeply of home and distant childhood moments."
                            
                            scene bg dormday
                            with vpunch
                            
                            "BEEP...BEEP... BEEP...BE--"
                            show irisdizzy with hpunch
                            ir "Urgh... what... where...?"
                            ir "Oh, right. Laguardia..."
                            hide irisdizzy
                            show irissurprise
                            ir "Oh. Mom. Where... my phone...?"
                            "I dig around the blankets wrapping me until I find the heap phone mom purchased for me so I could keep in touch while at school."
                            hide irissurprise
                            show iris 
                            "I open the phone and press speed dial one."
                            "Riing..."
                            "Riing..."
                            "Riing..."
                            "Rii-- Click"
                            
                            scene bg home
                            with flash
                            show momsad 
                            m "... Hello? Oh, [ir]! You meanie! You made me wait so long to hear the news!"
                            m "So...? How'd it go?"
                            hide momsad
                            show mom
                            ir laugh "...Oh yeah! I made it into Laguardia."
                            ir laugh "Haha, finally you guys can take proper care of yourselves."
                            ir superhappy "Hey, don't go getting any ideas either, ok? I don't want any gifts or anything."        
                            ir smiles"I glance around and survey the dorm I'll be in for the next year."
                            ir bright"There's the small bed, a desk, a tiny dresser with a mini fridge beside it and a window that divides the wall across from the bed in half."
                            ir bright "Aside from that, the room is barren. A typical freshman's room." 
                            hide mom
                            show momhappy
                            m "Oh my goodness! Oh... I'm so proud of you, [ir]."
                            m "My baby, you've made your sisters and I so proud. Oh honey..."
                            "I can hear my mom tearing up on the other end."
                            ir oops "..."
                            hide momhappy
                            show momsad
                            m "*Sniffle*... Oh! Before I go, sweetie, I want to let you know-- be careful, ok [ir]?"
                            m "There's been a lot in the news about Laguardian students turning out to be spies from rival schools."
                            m "I know you'll have buddies who want to hang out but be sure you're cautious."
                            m "I worry so much for you now that you're so far away... Be safe, ok hon?"
                            ir oops "I wonder about all my fellow students"
                            ir sad2 "Ryner, Jessica, Seita... "
                            ir oops  "I can't help but get suspicious."
                            hide momsad
                            show mom
                            m "...Sweetie?"
                            ir laugh "Oh- of course mom, I'll keep my guard up. You don't have to worry." 
                            ir bright "I promise."
                            m "*Sniffle*..."
                            m "Alright, [ir]. I love you."
                            m "Hmm, but don't forget to have fun, too. Do your best while you're there!"
                            m "Bye..."
                    scene bg dormday
                    with Dissolve(.5)
                    "Later..."
                    show iriswelcome
                    "Hmmmm... I guess I'll just follow the crowd to find the cafeteria again."
                    "A steady trickle of people leads to the doors of the massive building."
                    hide irisbright
                    scene bg caf
                    with flash
            
                    ir "Hmmm... I guess I'll just follow the crowd to find the cafeteria again."
                    "A steady trickle of people leads to the doors of the massive building."
                    ir surprise"Oh wow! So many students here!"
                    ir smiles"I wander over to the line and peek over shoulders to get a glimpse of the menu."
                    ir smiles "As I'm straining to stay on my tiptoes, I feel someone tapping on my shoulder."
                    show friend2 at center  with move
                    s "Heyo, you want a menu?"
                    "In his hand is a paper printout of the menu on the wall."
                    ir oops "Huh?"
                    show friend1 at right with move
                    j "He said a menu silly."
                    ir eee "Oh. Haha, thanks."
                    s "Ugh... I'm so not psyched to meet Dr. Jenner in person."
                    hide friend1
                    show friend1oops at right
                    j "I get the feeling she just doesn't like any of us. Ha, see? She's over there in the corner staring us all down."
                    s "Huh, I never would have noticed she was there."
                    hide friend2
                    show friend2surprise at center
                    s "Hey, that's creepy..."
                    
                    
                    s "Some kid is standing right next to her. I understand the weirdo tach, but why's he staring us all down like that?"
                    ir oops"I look over to see what which random person is staring."
                    ir surprise"Whoa! It's Ryner...?"
                    ir oops"...That's weird. I met him before Orientation yesterday. He found me in some office hallway and helped me..."
                    ir dizzy"My mind whirs as I remember mom's words of caution."
                    hide friend1oops
                    hide friend2surprise
                    show friend1bright at right
                    show friend2bright at center
                    j "Let's just finish up and go to class. I don't wanna risk being stared at like that if we're late."
                    ri briht"We finish up breakfast and leave the cafeteria to search for class 1A."
                    
                    
                    scene bg cla2
                    
                    #-----------
                    with Dissolve(.5)
                    play sound ("bell.mp3")
                    " As soon as we cross the threshold into the room, the late bell sounds and we breathe a collective sigh of relief as you meander over to the last three available seats..."
                    "... at the very front."
                    "I hear the same clunking footsteps from yesterday enter the room just as we've all sat down."
                    show jenner at center with move
                    "All the students settle down and wait silently for her to speak."
                    dj "Alright, now that I've got your attention, I'll make the introductions brief."
                    dj "I am your homeroom teacher, Dr. Jenner."
                    dj "I'm sure the lot of you are proud to have made it into this prestigious school, and you all share dreams of graduating and leading a long, fulfilling career in our fine military,"
                    dj "I'm also sure that at least half of you will not graduate at all."
                    dj "My job from this day forward is to push you until you break, then break you again and again until we can remake you into something worth keeping around."
                    dj "Savor this moment, while you still enjoy living."
                    dj "Buckle up boys and girls, you've got nothing but a grueling four years ahead of you."
                    dj "That will be all for introductions."
                    hide jenner
                    show jennerangry
                    dj "Any questions? No?"
                    dj "Good, then let's get started on what we came here to do."
                    dj "First things first, we've got written and physical exams."
                    hide jennerangry
                    show jenner
                    dj "We'll use this to measure your potential and progress throughout the year."
                    dj "Last place student is expelled."
                    dj "Prepare yourselves."
                    hide jenner

                    narration "The test is insert outside of the game! Finish the test then come back here"
                    play sound("school bell.mp3")
                    "Ding, Dong, Ding, Dong, ....Ding, Dong, Ding, Dong"
                    show jenner
                    dj "That's it everyone! Class dismissed!"
                    hide jenner
                    show friend1sign at right
                    show friend2sign at center
                    #at the corner
                    ir sign "Aaaaaaahhhhh"
                    "The entire room sighed in relief."
                    scene bg locker
                    with Dissolve(.7)
                    show irisbright at center
                    show friend1sign at right
                    show friend2 at left
                    j "Oh. My. God. What a day!"
                    j "I swear he was looking to kill one of us!"
                    j "Poor Debbie got it the worst, it was like he was intent on really ruining her day. All she did was sneak a bite of leftover breakfast!"
                    hide friend1sign
                    show friend1 at right
                    hide friend2
                    show friend2sign at left
                    j "No kidding. Ughhh. Not like he eased up on us either. Nooo, he had to make us run a freaking marathon on day one!"
                    #------------
                    s "Nooo, she had to make us run a freaking marathon on day one!"
                    ir "Yeah, are we  gonna sleep well tonight or what. Wow."
                    hide friend1
                    hide irisbright
                    show friend1bright at right
                    j "Oh, [ir], speaking of tonight..."
                    " [j] motions me to come in closer and [s] looks over his shoulder before turning back to face me."
                    hide friend2sign
                    hide friend1bright
                    show friend1smirk at right
                    show friend2 at center
                    s "We're going to the local hang-out later today. Wanna come?"
                    ir oops "..."
                    "Would you like to go with Seita and Jessica to the local hang-out?"
                    hide friens1smirk
                    hide friend2
                    menu:
                        "Yeah!":
                            show friend1laugh at right
                            show friend2laugh at center
                            ir smiles "Yeah, I was gonna go there for dinner anyway!"
                            
                            s "Alright! We'll meet you back at the auditorium, then! How's 8:00 sound?"
                            hide friend1laugh
                            hide friend2laugh
                        "Sure.":
                            show friend1bright at right
                            show friend2bright at center
                            ir bright "Hmmm... Sure! I wanted to check it out sometime anyway."
                            s "Alright! We'll meet you back at the auditorium then! How's 8:00 sound?"
                            hide friend1bright
                            hide friend2bright
                        "No.":
                            show friend1 at right
                            show friend2 at center
                            ir nervous "Oh, thank you for the offer, but I'm beat. I'm gonna go to my dorm."
                            hide friend1
                            show friend1welcome at right
                            s "Hey, c'mon, loosen up a little!"
                            hide friend2
                            show friend2eee at center
                            j "Yeah, it's not like we're staying out late or anything."
                            j "Just come check it out, you can leave if you don't like it."
                            s "...Or is it the company? If you don't wanna hang out with us, that's... whatever..."
                            ir oops "No! That's not it at all, really."
                            ir sign"*Sigh*... Alright. When and where are we meeting?"
                            hide friend1welcome
                            hide friend2eee
                            show friend1superhappy at right
                            show friend2laugh at center
                            
                            j "Yay! Haha, we'll meet back at the auditorium at 8:00- don't be late kay?"
                            hide friend1superhappy with Dissolve (.4)
                            hide friend2laugh with Dissolve (.4)
                    show friend1laugh at right
                    show friend2 at center
                    ir laugh "Sounds fine to me."
                    s "Yes! Alright, see you round [ir]."
                    ir "See you later guys."
                    hide friend1laugh 
                    hide friend2
                    
                    scene bg aud
                    ir oops "The auditorium at night looks eerie, lit only by the dim glow of light from the cafeteria beside it. It's 7:45; you're a little early, but better than being late."
                    "Two lone figures are standing in front of it."
                    ir cry "Hey! Come on, guys! Why're you hanging out in the shadows like that? Let's go!"
                    f "..."
                    F "..."
                    ir nervous "...Guys?"
                    ir oops "As I close in on the two figures cloaked in shadow, I notice one is much taller than the other, and they seem to be passing papers."
                    ir nervous "Oh, sorry- I thought you were my friends..."
                    show jennerangry at center with Dissolve(.5)
                    dj "Well, Ryner? How will you handle this?"
                    show friend3yeah at right with Dissolve(.5)
                    r "...Oh, [ir]... Why'd you have to walk in on this? Now you've seen too much."
                    dj "Ugh... Stop chitchatting and grab them already!"
                    hide friend3yeah
                    show friend3shock with hpunch
                    r "Too bad it couldn't work out--Eh? [ir]? Huh, STOP RUNNING!"
                    hide friend3shock
                    hide jennerangry
                    narration "You can play minigame 2 down below, then continue the story."
                    show headmaster
                    with flash
                    h "Well, well, look what we've got here."
                    h "Dr. Jenner, you're fired. I expect you out by morning."
                    h "And some goes to you, Ryner. You're expelled."
                    ir oops "..."
                    h " [ir], we've known for some time that we had an infiltration problem among the students, but Dr. Jenner, you were a surprise."
                    h "[ir], I want to thank you for helping discover them- it may have taken months without your help."
                    menu:
                        "CONGRATULATIONS! YOU MADE IT TO THE END!":
                           narration "Be careful and aware. If you see something suspicious- even if you know the person or people involved."
                           return
                           #-----------------------------------------------------------------------------------------------
                "Boy":
                    
                    show irisbright at left
                    show iidasad2 at right
                
                    "Congratulations! Your character [ir] is ready to begin the game!"
                    scene bg start with pixellade
                    narration "I open my eyes to see I'm sitting in an office with a large bookcase resting against one wall. Expansive windows let in the morning light from the left side of the room."
                    "There is a tall woman standing across from me at the other end of the dark mahogany table I've been seated at for the last hour."
                    show jenner
                    "The woman holds an imposing file in her left hand."
                    hide jenner
                    show jennersmile
                    t "[ii], you've been assigned under Dr. Jenner with the rest of class 1A."
        
                    t "You are to meet them for Orientation at 7:00. That means you have twenty minutes until report time in the Auditorium. It's just past the cafeteria."
                    hide jennersmile
                    show jenner
                    "The tall lady levels a stare at me, then turns to exit."
                    hide jenner
                    ii sign "Whew! That was stressful, but at long last, I've passed my final interview."
                    ii bright"Yes! I've finally made it into the Laguardian School of Strategy and on full scholarship too!"
                    ii bright "Now my family won't have to worry anymore about me, and I won't be putting more financial burden on them."
                    ii smiles "I stand up and go to the exit."
                    scene bg hallway with flash
                    play sound("door open.mp3")
                    ii smiles "My hand makes contact with the cool door handle and the door releases a low groan as I push it open."
                    ii sad2 "The hallway outside is completely deserted."
                    ii sad2 "I hesitate for a moment."
                    "Do you want to go straight to the Auditorium or would you rather explore your new home for the next four years?"
                    menu:
                        "Auditorium":
                            ii bright"Alright! I set off in the direction I think the cafeteria is in... "
                            ii oops "but I quickly encounter a critical problem. I don't have a clue where anything is, or even where I am now."
                            ii dizzy"I look around me and find I'm already hopelessly lost in an unmarked hallway."
                            ii dizzy"Crap."
                        "Explore":
                            ii laugh "Excellent! I turn on my heel and pick a random direction to explore."
                            ii laugh"This should be fun!"
                            ii smiles "For the most part, the building is uninhabited as all the current students are elsewhere, either in classes or in a tactical battlefield simulation."
                    ii oops "As I stride past yet another dark, unmarked door, I hear something break the monotonous sound of my footsteps."
                    play sound ("whispering.mp3")
                    "Someone down the hall is humming the national anthem."
                    ii nervous "...Hello? Who's there?"
                    ii oops "I get no response and the empty hall provides no clue as to who was there."
                    ii nervous"Ummm... I heard you earlier. That was the national anthem, right?"
                    
                    "A moment passes, but soon a voice rings out, and it's owner rounds the corner not long after the voice sounds."
                    show friend3laugh
                    with pixellade
                    gu "Haha, you got me!"
                    gu "Hey, are you new here? What are you doing so far from the Auditorium?"
                    ii oops "Well I--"
                    hide friend3laugh
                    show friend3bright
                    gu "Whatever, just follow me. Since there's still time before Orientation, I'll give you a tour."
                    ii dizzy "Huh?"
                    "Do you want to go on a tour?"
                    hide friend3bright
                    menu:
                        "Yes":
                            show friend3laugh
                            ii superhappy "Um, sure, I wanted to explore a little anyway."
                            gu "Cool! I'm Ryner by the way. What's your name?"
                            ii superhappy "[ii]"
                            hide friend3laugh
                            show friend3
                            r "Cool."
                            r "Hey, so what course are you in? All freshman have a choice between the Tactical Comms and Business Study departments, right?"
                            hide friend3
                        "No":
                            show friend3bright
                            ii oops "Hmm, no thanks. I'd really rather not risk being late to my first school event."
                            hide friend3bright
                            show friend3sad2
                            gu "Aw, that's lame."
                            hide friend3sad2
                            show friend3bright
                            gu "Well, I'll show you the way at least. It's easy to get lost around here."
                            gu "Hey, it's nice to meet you ...?"
                            ii welcome "[ii]"
                            hide friend3bright
                            show friend3welcome
                            gu "Alright [ii]. I'm Ryner. What department are you studying in? If I remember correctly, you had a choice between Tactical Comms and Business Studies, right?"
                            hide friend3welcome
                    ii smiles "Yeah, that's right. I'm enrolled in Business Study."
                    show friend3superhappy
                    r "Cool! I was too, so if you ever want a different opinion on a project, just ask me, ok?"
                    r "Let me know anytime you need help."
                    ii laugh "Um... sure. Thanks."
                    hide friend3superhappy
                    show friend3mad
                    r "Hey, uh... no offense, but you don't seem too thrilled to be here."
                    ii welcome "None taken, and yeah. I mean, the school's great and all, but I'm mostly here to take the strain off my family. They don't need another mouth to feed hanging around."
                    hide friend3mad
                    show friend3yeah
                    r "Why'd you go through all the trouble to get into this school then if you don't even want to be here? There are so many other places you could get into, why put in the effort for this one?"
                    ii bright "Well... when I graduate, I don't want to go back to being a burden for my family."
                    ii bright"If I get recognized by this school, I'm bound to get a decent job in the government or something."
                    hide friend3yeah
                    show friend3sign
                    r "Jeez. You know, I bet your family wouldn't want you to just slave away your days here. They'd probably want you to enjoy your life too."
                    r "It doesn't all have to be about money and burdens!"
                    ii smiles"I guess."
                    hide friend3sign
                    show friend3angry
                    r "I'm serious!"
                    r "I just mean, your family wouldn't want you to be so hard on yourself, that's all."
                    ii nervous"...."
                    ii oops "Thank you."
                    hide friend3angry
                    show friend3sad2
                    narration "Ryner appears lost in thought. It looks like he is remembering something sad."
                    hide friend3sad
                    show friend3laugh
                    r "...... OH! Haha, it's nothing, just some passing advice that you probably won't even remember."
                    ii laugh"Nevertheless, thank you."
                    r "Hmmm... Alright! Looks like we've made a full loop around, now we're at the Auditorium."
                    scene bg open
                    narration "A large, squat building stands in front of the two of you."
                    show friend3laugh
                    ii bright "Thanks again."
                    r "Seriously [ii] anytime you want help, just go to dorm 3 and ask around for me."
                    hide friend3laugh
                    show friend3
                    ii laugh"Haha, alright, I will! See you around Ryner."
                    r "Yeah, talk to you later sometime. Good luck at Orientation!"
                    hide friend3
                    with Dissolve (.6)
                    
                    scene bg aud2
                    with flash
                    narration "As the rest of the freshman student body fills into the Auditorium, the Headmaster scales the steps of the stage and begins to address the crowd."
                    show headmaster
                    h"Welcome, everyone, to the Laguardian School of Strategy. Everyone, please look forward to a productive year!"
                    ii smiles "He gives his outlook on life and education, then begins introducing the teaching staff."
                    h "And here is our most recent addition to the staff here at Laguardian, Dr. Jenner! She'll be teaching Macroeconomics and is the homeroom teacher to all you students assigned to class 1A. Next up, is Mr. Spannend..."
                    show jenner at right
                    ii superhappy "Oh, looks like that'll be my teacher for the next year."
                    ii superhappy "I hope she's lenient..."
                    "Suddenly, the kid sitting next to me started whispering to me."
                    hide headmaster with Dissolve(.5)
                    hide jenner with Dissolve(.5)
                    
                    show friend2sign at center with Dissolve(.4)
                    gu "Nah, when I met her in the halls earlier, she snapped at me and Jessica, and I quote, 'to scram' and 'do something worthwhile with our meatsuits.'"
                    ii dizzy "huh?"
                    show friend1sign at right with Dissolve(.4)
                    gi "Yeah, and she even threatened to give us detention for loitering! I'm Jessica, by the way."
                    
                    ii sad2 "Whoa... Looks like we're in for a rough year. Dang it!"
                    hide friend1sign
                    hide friend2sign
                    show friend1sad2 at right
                    show friend2sad2 at center
                    ii sign"... I just wanted to peacefully graduate from this place and support myself."
                    
                    e "Well, as long as she's our teacher, the 'peaceful' part of that might have to be put on hold."
                    hide friend2sad2
                    show friend2 at center
                    e "Hey Seita, you're in class 1A too, right?"
                    hide friend1sad2
                    show friend1bright at right
                    s "Yurp."
                    s "Man, I was really hoping to get a teach who'd ignore it if I forgot my homework."
                    hide friend1bright
                    show friend1sign at right
                    s "This lady looks like she'll whip me if I have a crinkle on the paper!"
                    "The Headmaster on stage calls up the freshman student body representative to give a speech."
                    ii sign "Sigh..."
                    hide friend2sad2
                    show friend2welcome at center 
                    e "Well- this is Laguardia! We'll take the good and the bad- after all, we put in so much work and time to get in!"
                    s "I second that."
                    narration "The student on stage finishes his spiel and the Head closes Orientation by telling students to meet back here at 1:00 for tours of the grounds."
                    hide friend2smile
                    hide friend1sign
                    show friend1bright at right
                    show friend2bright at center
                    
                    e "Oh, right! What's your name?"
                    ii "Haha, I forgot to mention! It's [ii]."
                    s "Cool [ii]. See you around!"
                    hide friend1bright with Dissolve(.4)
                    hide friend2bright with Dissolve(.4)
                    
                    scene bg dormnightlight
                    with pixellade
                    ".....Later that day....."
                    show iidalaugh with Dissolve (.4)
                    "Wow...what a long day! I'm ready to pass out; hopefully the night lasts long enough to get a good rest."
                    hide iidalaugh
                    show iidabright
                    " I crumple onto my dorm room bed and smile to myself."
                    "I think of my day and my thoughts go to my family way back home."
                    hide iidabright
                    show iidalaugh
                    "Oh! They must be wondering how the final interview went. Maybe Mom will pick up if I call."
                    "Do you want to call Mom now or in the morning?"
                    hide iidalaugh with Dissolve (.5)
                    menu:
                        "Now":
                            show iida
                            "I dig around for the cheap phone mom bought me so I could keep in touch while at school and press speed dial one."
                            "Riing..."
                            "Riing..."
                            "Riing..."
                            hide iida
                            show iidasurprise
                            "Rii-- Click"
                            
                            scene bg home
                            with flash
                            show momsad 
                            m "... Hello? Oh, [ii]! You meanie! You made me wait so long to hear the news!"
                            m "So...? How'd it go?"
                            hide momsad
                            show mom
                            ii laugh "...Oh yeah! I made it into Laguardia."
                            ii laugh "Haha, finally you guys can take proper care of yourselves."
                            ii superhappy "Hey, don't go getting any ideas either, ok? I don't want any gifts or anything."        
                            ii smiles"I glance around and survey the dorm I'll be in for the next year."
                            ii bright"There's the small bed, a desk, a tiny dresser with a mini fridge beside it and a window that divides the wall across from the bed in half."
                            ii bright "Aside from that, the room is barren. A typical freshman's room." 
                            hide mom
                            show momhappy
                            m "Oh my goodness! Oh... I'm so proud of you, [ii]."
                            m "My baby, you've made your sisters and I so proud. Oh honey..."
                            "I can hear my mom tearing up on the other end."
                            ii oops "..."
                            hide momhappy
                            show momsad
                            m "*Sniffle*... Oh! Before I go, sweetie, I want to let you know-- be careful, ok [ir]?"
                            m "There's been a lot in the news about Laguardian students turning out to be spies from rival schools."
                            m "I know you'll have buddies who want to hang out but be sure you're cautious."
                            m "I worry so much for you now that you're so far away... Be safe, ok hon?"
                            ii oops "I wonder about all my fellow students"
                            ii sad2 "Ryner, Jessica, Seita... "
                            ii oops  "I can't help but get suspicious."
                            hide momsad
                            show mom
                            m "...Sweetie?"
                            ii laugh "Oh- of course mom, I'll keep my guard up. You don't have to worry." 
                            ii bright "I promise."
                            m "*Sniffle*..."
                            m "Alright, [ii]. I love you."
                            m "Hmm, but don't forget to have fun, too. Do your best while you're there!"
                            m "Bye..."
                            
                            scene bg dormsleep
                            "I collapse back down onto the duvet and feel myself nodding off."
                            ir sad "Aaah. Time for some shuteye."
                            ir "Hmmm...."
                            "...I fall asleep in my clothes and dream deeply of home and distant childhood moments."
                            
                            scene bg dormday
                            with vpunch(1.)
                            "BEEP...BEEP... BEEP...BE--"
                            show iidadizzy with hpunch
                            "Urgh... what... where...?"
                            hide iidadizzy
                            show iidabright
                            "Oh, right. Laguardia..."
                        "Later":
                            show iidabright
                            ii"Yeah... it's already so late- probably best to let her rest and just check in when morning comes."
                            ii "I'll have to set my alarm early, though."
                            hide iidabright
                            show iidalaugh
                            ii"Aaaah. Time for some shuteye."
                            ii "Hmmmmm....."
                            hide iidalaugh with Dissolve(.5)
                            "I fall asleep in my clothes and dream deeply of home and distant childhood moments."
                            
                            scene bg dormday
                            with vpunch
                            
                            "BEEP...BEEP... BEEP...BE--"
                            show iidadizzy with hpunch
                            ii "Urgh... what... where...?"
                            ii "Oh, right. Laguardia..."
                            hide iidadizzy
                            show iidasurprise
                            ii "Oh. Mom. Where... my phone...?"
                            "I dig around the blankets wrapping me until I find the heap phone mom purchased for me so I could keep in touch while at school."
                            hide iidasurprise
                            show iida 
                            "I open the phone and press speed dial one."
                            "Riing..."
                            "Riing..."
                            "Riing..."
                            "Rii-- Click"
                            
                            scene bg home
                            with flash
                            show momsad 
                            m "... Hello? Oh, [ii]! You meanie! You made me wait so long to hear the news!"
                            m "So...? How'd it go?"
                            hide momsad
                            show mom
                            ii laugh "...Oh yeah! I made it into Laguardia."
                            ii laugh "Haha, finally you guys can take proper care of yourselves."
                            ii superhappy "Hey, don't go getting any ideas either, ok? I don't want any gifts or anything."        
                            ii smiles"I glance around and survey the dorm I'll be in for the next year."
                            ii bright"There's the small bed, a desk, a tiny dresser with a mini fridge beside it and a window that divides the wall across from the bed in half."
                            ii bright "Aside from that, the room is barren. A typical freshman's room." 
                            hide mom
                            show momhappy
                            m "Oh my goodness! Oh... I'm so proud of you, [ii]."
                            m "My baby, you've made your sisters and I so proud. Oh honey..."
                            "I can hear my mom tearing up on the other end."
                            ii oops "..."
                            hide momhappy
                            show momsad
                            m "*Sniffle*... Oh! Before I go, sweetie, I want to let you know-- be careful, ok [ii]?"
                            m "There's been a lot in the news about Laguardian students turning out to be spies from rival schools."
                            m "I know you'll have buddies who want to hang out but be sure you're cautious."
                            m "I worry so much for you now that you're so far away... Be safe, ok hon?"
                            ii oops "I wonder about all my fellow students"
                            ii sad2 "Ryner, Jessica, Seita... "
                            ii oops  "I can't help but get suspicious."
                            hide momsad
                            show mom
                            m "...Sweetie?"
                            ii laugh "Oh- of course mom, I'll keep my guard up. You don't have to worry." 
                            ii bright "I promise."
                            m "*Sniffle*..."
                            m "Alright, [ii]. I love you."
                            m "Hmm, but don't forget to have fun, too. Do your best while you're there!"
                            m "Bye..."
                    scene bg dormday
                    with Dissolve(.5)
                    "Later..."
                    show iidawelcome
                    "Hmmmm... I guess I'll just follow the crowd to find the cafeteria again."
                    "A steady trickle of people leads to the doors of the massive building."
                    hide iidabright
                    scene bg caf
                    with flash
            
                    ii "Hmmm... I guess I'll just follow the crowd to find the cafeteria again."
                    "A steady trickle of people leads to the doors of the massive building."
                    ii surprise"Oh wow! So many students here!"
                    ii smiles"I wander over to the line and peek over shoulders to get a glimpse of the menu."
                    ii smiles "As I'm straining to stay on my tiptoes, I feel someone tapping on my shoulder."
                    show friend2 at center  with move
                    s "Heyo, you want a menu?"
                    "In his hand is a paper printout of the menu on the wall."
                    ii oops "Huh?"
                    show friend1 at right with move
                    j "He said a menu silly."
                    ii eee "Oh. Haha, thanks."
                    s "Ugh... I'm so not psyched to meet Dr. Jenner in person."
                    hide friend1
                    show friend1oops at right
                    j "I get the feeling she just doesn't like any of us. Ha, see? She's over there in the corner staring us all down."
                    s "Huh, I never would have noticed she was there."
                    hide friend2
                    show friend2surprise at center
                    s "Hey, that's creepy..."
                    
                    
                    s "Some kid is standing right next to her. I understand the weirdo tach, but why's he staring us all down like that?"
                    ii oops"I look over to see what which random person is staring."
                    ii surprise"Whoa! It's Ryner...?"
                    ii oops"...That's weird. I met him before Orientation yesterday. He found me in some office hallway and helped me..."
                    ii dizzy"My mind whirs as I remember mom's words of caution."
                    hide friend1oops
                    hide friend2surprise
                    show friend1bright at right
                    show friend2bright at center
                    j "Let's just finish up and go to class. I don't wanna risk being stared at like that if we're late."
                    ii bright"We finish up breakfast and leave the cafeteria to search for class 1A."
                    
                    
                    scene bg cla2
                    
                    #-----------
                    with Dissolve(.5)
                    play sound ("bell.mp3")
                    " As soon as we cross the threshold into the room, the late bell sounds and we breathe a collective sigh of relief as you meander over to the last three available seats..."
                    "... at the very front."
                    "I hear the same clunking footsteps from yesterday enter the room just as we've all sat down."
                    show jenner at center with move
                    "All the students settle down and wait silently for her to speak."
                    dj "Alright, now that I've got your attention, I'll make the introductions brief."
                    dj "I am your homeroom teacher, Dr. Jenner."
                    dj "I'm sure the lot of you are proud to have made it into this prestigious school, and you all share dreams of graduating and leading a long, fulfilling career in our fine military,"
                    dj "I'm also sure that at least half of you will not graduate at all."
                    dj "My job from this day forward is to push you until you break, then break you again and again until we can remake you into something worth keeping around."
                    dj "Savor this moment, while you still enjoy living."
                    dj "Buckle up boys and girls, you've got nothing but a grueling four years ahead of you."
                    dj "That will be all for introductions."
                    hide jenner
                    show jennerangry
                    dj "Any questions? No?"
                    dj "Good, then let's get started on what we came here to do."
                    dj "First things first, we've got written and physical exams."
                    hide jennerangry
                    show jenner
                    dj "We'll use this to measure your potential and progress throughout the year."
                    dj "Last place student is expelled."
                    dj "Prepare yourselves."
                    hide jenner

                    narration "The test is insert outside of the game! Finish the test then come back here"
                    play sound("school bell.mp3")
                    "Ding, Dong, Ding, Dong, ....Ding, Dong, Ding, Dong"
                    show jenner
                    dj "That's it everyone! Class dismissed!"
                    hide jenner
                    show friend1sign at right
                    show friend2sign at center
                    #at the corner
                    ii sign "Aaaaaaahhhhh"
                    "The entire room sighed in relief."
                    scene bg locker
                    with Dissolve(.7)
                    show iidabright at center
                    show friend1sign at right
                    show friend2 at left
                    j "Oh. My. God. What a day!"
                    j "I swear he was looking to kill one of us!"
                    j "Poor Debbie got it the worst, it was like he was intent on really ruining her day. All she did was sneak a bite of leftover breakfast!"
                    hide friend1sign
                    show friend1 at right
                    hide friend2
                    show friend2sign at left
                    j "No kidding. Ughhh. Not like he eased up on us either. Nooo, he had to make us run a freaking marathon on day one!"
                    #------------
                    s "Nooo, she had to make us run a freaking marathon on day one!"
                    ii smiles "Yeah, are we  gonna sleep well tonight or what. Wow."
                    hide friend1
                    show friend1bright at right
                    j "Oh, [ir], speaking of tonight..."
                    " [j] motions me to come in closer and [s] looks over his shoulder before turning back to face me."
                    hide friend2sign
                    hide friend1bright
                    show friend1smirk at right
                    show friend2 at left
                    s "We're going to the local hang-out later today. Wanna come?"
                    "..."
                    "Would you like to go with Seita and Jessica to the local hang-out?"
                    hide friens1smirk
                    hide friend2
                    hide iidabright
                    menu:
                        "Yeah!":
                            show friend1laugh at right
                            show friend2laugh at center
                            ir smiles "Yeah, I was gonna go there for dinner anyway!"
                            
                            s "Alright! We'll meet you back at the auditorium, then! How's 8:00 sound?"
                            hide friend1laugh
                            hide friend2laugh
                        "Sure.":
                            show friend1bright at right
                            show friend2bright at center
                            ir bright "Hmmm... Sure! I wanted to check it out sometime anyway."
                            s "Alright! We'll meet you back at the auditorium then! How's 8:00 sound?"
                            hide friend1bright
                            hide friend2bright
                        "No.":
                            show friend1 at right
                            show friend2 at center
                            ir nervous "Oh, thank you for the offer, but I'm beat. I'm gonna go to my dorm."
                            hide friend1
                            show friend1welcome at right
                            s "Hey, c'mon, loosen up a little!"
                            hide friend2
                            show friend2eee at center
                            j "Yeah, it's not like we're staying out late or anything."
                            j "Just come check it out, you can leave if you don't like it."
                            s "...Or is it the company? If you don't wanna hang out with us, that's... whatever..."
                            ir oops "No! That's not it at all, really."
                            ir sign"*Sigh*... Alright. When and where are we meeting?"
                            hide friend1welcome
                            hide friend2eee
                            show friend1superhappy at right
                            show friend2laugh at center
                            
                            j "Yay! Haha, we'll meet back at the auditorium at 8:00- don't be late kay?"
                            hide friend1superhappy with Dissolve (.4)
                            hide friend2laugh with Dissolve (.4)
                    show friend1laugh at right
                    show friend2 at center
                    ii laugh "Sounds fine to me."
                    s "Yes! Alright, see you round [ii]."
                    ii "See you later guys."
                    hide friend1laugh
                    hide friend2
                    
                    scene bg aud
                    ii oops "The auditorium at night looks eerie, lit only by the dim glow of light from the cafeteria beside it. It's 7:45; you're a little early, but better than being late."
                    "Two lone figures are standing in front of it."
                    ii cry "Hey! Come on, guys! Why're you hanging out in the shadows like that? Let's go!"
                    f "..."
                    F "..."
                    ii nervous "...Guys?"
                    ii oops "As I close in on the two figures cloaked in shadow, I notice one is much taller than the other, and they seem to be passing papers."
                    ii nervous "Oh, sorry- I thought you were my friends..."
                    show jennerangry at center with Dissolve(.5)
                    dj "Well, Ryner? How will you handle this?"
                    show friend3yeah at right with Dissolve(.5)
                    r "...Oh, [ii]... Why'd you have to walk in on this? Now you've seen too much."
                    dj "Ugh... Stop chitchatting and grab them already!"
                    hide friend3yeah
                    show friend3shock with hpunch
                    r "Too bad it couldn't work out--Eh? [ii]? Huh, STOP RUNNING!"
                    hide friend3shock
                    hide jennerangry
                
                    narration "You can play minigame 2 down below, then continue the story."
                    show headmaster
                    with flash
                    h "Well, well, look what we've got here."
                    h "Dr. Jenner, you're fired. I expect you out by morning."
                    h "And some goes to you, Ryner. You're expelled."
                    ii oops "..."
                    h " [ii], we've known for some time that we had an infiltration problem among the students, but Dr. Jenner, you were a surprise."
                    h "[ii], I want to thank you for helping discover them- it may have taken months without your help."
                    menu:
                        "CONGRATULATIONS! YOU MADE IT TO THE END!":
                           narration "Be careful and aware. If you see something suspicious- even if you know the person or people involved."
                           return

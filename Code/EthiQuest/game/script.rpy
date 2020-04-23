# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.

# Narrateur
define narrateur = Character('Narratuer', color="#ebc634")

#Joueur
define player = Character("[nom]", color="#ebc634", image="boy")
image boy_angry = Image("Jour_1/pere_et_hero/boy_angry.png", xalign=0.0, yalign=1.0)
image boy_confused = Image("Jour_1/pere_et_hero/boy_confused.png", xalign=0.0, yalign=1.0)
image boy_cry = Image("Jour_1/pere_et_hero/boy_cry.png", xalign=0.0, yalign=1.0)
image boy_flustered = Image("Jour_1/pere_et_hero/boy_flustered.png", xalign=0.0, yalign=1.0)
image boy_happy = Image("Jour_1/pere_et_hero/boy_happy.png", xalign=0.0, yalign=1.0)
image boy_nervous = Image("Jour_1/pere_et_hero/boy_nervous.png", xalign=0.0, yalign=1.0)
image boy = Image("Jour_1/pere_et_hero/boy_normal.png", xalign=0.0, yalign=1.0)
image boy_sad = Image("Jour_1/pere_et_hero/boy_sad.png", xalign=0.0, yalign=1.0)
image boy_shocked = Image("Jour_1/pere_et_hero/boy_shocked.png", xalign=0.0, yalign=1.0)

#Pere
define dad = Character("Papa", color="#3443eb", image="dad")
image dad = Image("Jour_1/pere_et_hero/dad.png", xalign=0.0, yalign=1.0)
image dad_smoking = Image("Jour_1/pere_et_hero/dad_smoking.png", xalign=0.0, yalign=1.0)

#Meilleur amie
define best_friend = Character("Emma", color="#3443eb", image="best_friend")
image best_friend = Image("Jour_1/meilleur_amie/best_friend_neutral01.png", xalign=0.0, yalign=1.0)
image best_friend_angry = Image("Jour_1/meilleur_amie/best_friend_angry01.png", xalign=0.0, yalign=1.0)
image best_friend_annoyed = Image("Jour_1/meilleur_amie/best_friend_annoyed01.png", xalign=0.0, yalign=1.0)
image best_friend_sad = Image("Jour_1/meilleur_amie/best_friend_sad01.png", xalign=0.0, yalign=1.0)
image best_friend_smile = Image("Jour_1/meilleure_amie/best_friend_smile01.png", xalign=0.0, yalign=1.0)

#Mere
define mere = Character("Maman", color="#ebe834", image="mere")
image mere = Image("Jour_1/mere/mere_neutral.png", xalign=0.0, yalign=1.0)
image mere_angry = Image("Jour_1/mere/mere_angry.png", xalign=0.0, yalign=1.0)
image mere_happy = Image("Jour_1/mere/mere_happy.png", xalign=0.0, yalign=1.0)
image mere_sad = Image("Jour_1/mere/mere_sad.png", xalign=0.0, yalign=1.0)
image mere_surprised = Image("Jour_1/mere/mere_surprised.png", xalign=0.0, yalign=1.0)

#Professeur
define teacher = Character("Professeur", color="#ebe834", image="teacher")
image teacher = Image("Jour_1/Professeur/teacher_neutral.png", xalign=0.0, yalign=1.0)
image teacher_annoyed = Image("Jour_1/Professeur/teacher.png", xalign=0.0, yalign=1.0)

#GM
define gm1 = Character('Game Master 1', color="#c8ffc8", image = "game_master_1")
image game_master_1 = Image("game_master.png", xalign=0.0)

define gm2 = Character("Game Master 2", color="#c8ffc8")
image game_master_2 = Image("game_master.png", xalign=0.0)

#Backgrounds

#Space
image earth_close = im.Scale("Intro/earth_close.jpg", 1920, 1080)
image earth_far = im.Scale("Intro/earth_far.jpg", 1920, 1080)
image universe = im.Scale("Intro/universe.png", 1920, 1080)

#Chambre hreo
image room_hero = im.Scale("Jour_1/chambre_hero/room_day.png", 1920, 1080)
image room_hero_night = im.Scale("Jour_1/chambre_hero/room_night.png", 1920, 1080)
image room_night_light = im.Scale("Jour_1/chambre_hero/room_night_light.png", 1920, 1080)

#Salon
image salon = im.Scale("Jour_1/cuisine_salon/salon_jour.png", 1920, 1080)
image salon_crepuscule = im.Scale("Jour_1/cuisine_salon/salon_dawn.png", 1920, 1080)
image salon_nuit = im.Scale("Jour_1/cusiine_salon/salon_nuit.png", 1920, 1080)

#Ecole
image classroom = im.Scale("Jour_1/ecole/classroom.png", 1920, 1080)
image classroom_empty_full_light = im.Scale("Jour_1/ecole/classroom_empty_full_light.png", 1920, 1080)
image classroom_empty_mid_light = im.Scale("Jour_1/ecole/classroom_empty_mid_light.png", 1920, 1080)
image classroom_empty_no_day_light = im.Scale("Jour_1/ecole/classroom_empty_no_day_light.png", 1920, 1080)
image classroom_teacher = im.Scale("Jour_1/ecole/classroom_teacher.png", 1920, 1080)
image ecole_couloir = im.Scale("Jour_1/ecole/couloir.png", 1920, 1080)
image ecole_entree_jour = im.Scale("Jour_1/ecole/entree_jour.png", 1920, 1080)
image lunchroom_empty_dawn = im.Scale("Jour_1/ecole/lunchroom_empty_dawn.png", 1920, 1080)
image lunchroom_empty = im.Scale("Jour_1/ecole/lunchroom_empty.png", 1920, 1080)
image lunchroom_full = im.Scale("Jour_1/ecole/lunchroom_full.png", 1920, 1080)
image lunchroom_full_no_sunlight = im.Scale("Jour_1/ecole/luchroom_full_no_sunlight", 1920, 1080)
image lunchroom_half_full = im.Scale("Jour_1/ecole/lunchroom_half_full.png", 1920, 1080)


define camarade_1 = Character("Camarade", color="#32a852")
define camarade_2 = Character("Autre camarade", color="#32a852")

# Le jeu commence ici
label start:

    #Bienvenue
    narrateur "Bienvenue dans EthiQuest"


    #Name input
    narrateur "Commencez par écrire votre nom."
    $ nom = renpy.input("Entrez un nom.")
    $ nom = nom.strip()

    if not nom:
      $nom = "Lucas"

    "Tu es [nom] !"

    jump intro_gm

    return

label intro_gm:
    
    scene universe
    with dissolve

    show game_master_1
    with dissolve

    show game_master_2:
      xalign 1.0
      yalign 1.0
    with dissolve

    gm1 "NON PAS DU TOUT, TU TE TROMPES !"
    gm2 "C'EST TOI QUI TE TROMPES TU RACONTES N'IMPORTE QUOI !"

    gm1 "De toute façon c’est moi le plus grand alors c’est moi qui décide."
    gm2 " Mais non, on a le même âge ! Et c’est moi le plus beau."

    gm1 "Arrête un peu tes conneries ! On ne peut pas laisser tout le monde faire ce qu’il veut. Il faut des règles."
    gm2 " Mais il y a des règles ! Chacun dispose de lui-même comme il le souhaite, sans que personne ne puisse l’en empêcher."
    gm1 "Ça ne marchera jamais !"
    gm2 "Bien sûr que si ! "
    gm2 "Et tu penses que laisser la décision au plus grand nombre est plus efficace ?"
    gm1 "Tout à fait ! En satisfaisant le plus gens, tout le monde est content."
    gm2 "Non, pas tout le monde ! Tu ne pense pas à toutes les minorités que tu exclues. "
    gm2 "Si tout le monde dispose de lui comme il l’entend, chacun est satisfait."
    gm1 "Mais c’est l’anarchie ! Personne n’a le contrôle."
    gm2 "C’est ça ton problème, tu veux toujours avoir le contrôle sur tout. Laisse les autres décider de ce qu’ils veulent."
    gm1 "Mais les gens ont besoin d’être guidés."
    gm2 "…"
    gm1 "…"
    gm2 "Je sais comment te prouver que tu as tort. "
    gm2 "On va faire une expérience sur des cas réels. On a tout l’univers à notre disposition. On peut choisir n’importe qui, n’importe où parmi les 299 792 458 planètes."
    gm1 "Alors c’est moi qui choisis la…"
    gm2 "Trop tard, hi hi hi ! J’ai déjà choisi celle-là."

    jump intro_gm_earth

label intro_gm_earth:
    
    scene earth_far
    with dissolve

    show game_master_1
    with dissolve

    show game_master_2:
      xalign 1.0
      yalign 1.0
    with dissolve

    gm2 "Reste plus qu'à trouver notre ..."
    gm1 "J'ai déjà choi ! On se retrouve en bas frangin !"

    hide game_master_1
    with dissolve

    gm2 "Hé attends-moi ! Aaaaarrrrh, il m'énerve ..."

    jump intro_context

label intro_context:
    
    scene earth_close
    with dissolve

    narrateur "Les deux GM décident d'aller choisir un humain sur la planète Terre pour être le sujet de leurs expériences."

    jump jour1_appartement

label jour1_appartement:

    scene black_background
    with dissolve

    "TOC TOC TOC"

    mere "Réveille-toi, [nom]! Tu va être en retard à l'école!!"

    scene room_hero
    with dissolve

    show mere
    with dissolve

    show boy:
      xalign 1.0
      yalign 1.0
      zoom 0.3
    with dissolve

    player "*Bâille* Il faut que j'aille à la cuisine prendre mon petit déjeuner avant d'aller en cours..."

    menu:
      "Cuisine":
        jump jour1_cuisine

label jour1_cuisine:

    scene salon
    with dissolve

    show mere:
      xalign 0.0
      yalign 0.0
    with dissolve

    show boy:
      xalign 1.0
      yalign 1.0
      zoom 0.3
    with dissolve


    mere "Ah tu es debout, très bien! Voilà tes céréales, [nom]. Manges les vite, tu dois te dépêcher." 

    menu:
      "Bol":
        jump jour1_bol

label jour1_bol:

    player "*Crunch, crunch*"
    player "Bon j'y vais ! A ce soir maman."
    mere "Bonne journée, mon chou !"
    menu:
      "Extérieur":
        jump jour1_exterieur

label jour1_exterieur:
    # Carte de la ville à ajouter

    scene classroom_teacher
    with dissolve

    show teacher:
      xalign 0.0
      yalign 1.0
      zoom 0.7
    with dissolve


    teacher  "Bonjour tout le monde, aujourd'hui nous allons voir ensemble l'anatomie du système digestif."
    teacher  "Est-ce que quelqu'un arrive à me dire quels organes en font partie ?"

    "*Silence*"

    hide teacher
    with dissolve

    show teacher_annoyed:
      xalign 0.0
      yalign 1.0
      zoom 0.7
    with dissolve

    teacher "Personne ? N'oubliez pas que vous examens finaux sont le mois prochain, il va falloir se mettre au travail !"

    hide teacher_annoyed
    with dissolve

    show boy_nervous:
      xalign 1.0
      yalign 1.0
      zoom 0.25
    with dissolve

    player "Je sens que cette matinée va être longue...Vivement la pause de midi !"

    jump jour1_lunch

label jour1_lunch:

    scene lunchroom_full
    with dissolve

    show best_friend_smile:
      xalign 0.0
      yalign 1.0
      zoom 0.6
    with dissolve

    show boy_confused:
      xalign 1.0
      yalign 1.0
      zoom 0.25
    with dissolve


    best_friend "[nom]! Tu es là !"
    best_friend "Comment s'est passé ta matinée ?"

    menu:
      "Ennuyant":
        player "Ennuyant à mourir... On a fait de la biologie."
      "Passionant":
        player "Passionant! Le corps humain est fascinant."
      "Long":
        player "Long, je meurs de faim."

    best_friend "Je vois ! Dépêchons nous d'aller manger, il y a déjà une queue."
    player "J'arrive!"

    jump jour1_manger

label jour1_manger:
    scene balck_screen
    with dissolve

    scene lunchroom_full
    with dissolve

    show best_friend_smile:
      xalign 0.0
      yalign 1.0
      zoom 0.6
    with dissolve

    show boy_confused:
      xalign 1.0
      yalign 1.0
      zoom 0.25
    with dissolve


    best_friend "Heureusement qu'on s'est dépéchés, on a eu les dernières places!" 
    best_friend "Avec les examens qui arrivent tout le monde est stressé et veux manger au plus vite pour avoir le temps de réviser..."
    menu:
      "Sûr de soi":
        player "Pas moi en tout cas! Je sais que je vais réussir sans problèmes!"
      "Prévoyant.":
        player "Oui, le temps passe trop vite... Il faut aussi que je m'y mette."
      "Evasif":
        player "Je préfère passer du temps avec toi!"

    best_friend "Haha, tu as bien raison !"
    best_friend "En parlant de ça, cette nuit, j'ai fait un rêve où on était les deux enfermés à l'école jusqu'à qu'on arrive à résoudre un exercice de math impossible!"
    best_friend "Je regardais la feuille mais je comprenais rien et toi tu pleurais en disant qu'on allait mourir de faim avant d'y arriver."
    best_friend "Puis un Pikachu géant est arrivé et a mangé la feuille."
    best_friend "Là, je me suis réveillé en sursaut..."
    best_friend "Bizarre non?"

    player "Haha, oui mais ne t'inquiète pas, c'est qu'un rêve, c'était pas réel..."
    best_friend "Je sais ! Mais imagine si les rêves avaient des conséquences sur la réalité ! Ca serait terrifiant..."
    best_friend "En effet... Heureusement, que ça reste dans nos têtes!"

    "*Ding* *Ding*"

    best_friend "Ah, c'est l'heure de retourner en classe. Bon j'y vais. Bon aprem [nom] !"

    jump jour1_cours

label jour1_cours:

    scene classroom_teacher
    with dissolve

    show teacher:
      xalign 0.0
      yalign 1.0
      zoom 0.7
    with dissolve

    teacher "N'oubliez pas vos devoirs pour demain! Lire un chapitre du livre et répondre aux questions liées. On en parle tous ensemble demain."
    teacher "Bonne soirée."

    hide teacher
    with dissolve

    camarade_1 "Aaaah, j'avais oublié, je vais devoir repousser mon entrainement..."
    camarade_2 "Je pense que tu vas pouvoir les oublier tes entrainements ces prochains temps! On va devoir mettre toute notre énérgie dans les révisions..."
    
    show boy:
      xalign 1.0
      yalign 1.0
      zoom 0.25
    with dissolve

    player "Ils plaisantent pas avec ces examens..."
    camarade_2 "Vraiment... Et en plus, on a une grosse journée demain..."
    player "Il va falloir que j'aie me coucher tôt si je veux être en forme."

    jump jour1_maison_soir

label jour1_maison_soir:
    
    scene salon
    with dissolve

    show dad:
      xpos -250
      yalign 1.0
      zoom 0.7
    with dissolve

    dad "Alors, tu as bien travaillé aujourd'hui, [nom] ?"

    show boy:
      xpos 1500
      ypos   1800
      zoom 0.4
    with dissolve
    menu:
      "Oui":
        player "Oui, on a vu le système digestif. Mais c'est compliqué."
      "Pas tellement":
        player "J'ai pas tellement suivi..."
      "J'ai beaucoup de travail.":
        player "Oui, mais j'ai encore des devoirs pour demain à finir."

    show mere:
      xalign 0.5
      ypos 1600
      zoom 1.2
    with dissolve

    mere "Alors, il faut que tu travailles consciencieusement ce soir. Tu aurais besoin d'aide?"
    player  "Non, ça va aller."
    mere "N'hésite pas, si besoin. Il faut que tu les réussisses ces examens!"
    dad "Ne lui mets pas tant de pression, c'est encore un enfant."
    player "Papa !"
    mere "Oui, je sais... Un adolescent."
    player "*Soupir* Je vais travailler dans ma chambre."

    jump jour1_chambre_soir

label jour1_chambre_soir:
    
    scene room_night_light
    with dissolve

    show boy:
      xalign 0.0
      yalign 1.0
      zoom 0.25
    with dissolve

    player "J'ai fini mes devoirs mais je n'arrive pas à dormir..."
    player "Ces histoires d'examens me stressent."
    player "J'espère que je ne vais pas faire un rêve comme Emma cette nuit, je suis crevée."





    





# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.

# Narrateur
define narrateur = Character('Narrateur', color="#ebc634")

screen show_char(path, alignX, alignY, zoomV):
  tag show_char
  add path xalign alignX yalign alignY zoom zoomV

screen show_char1(path, alignX, alignY, zoomV):
  tag show_char1
  add path xalign alignX yalign alignY zoom zoomV

screen show_char2(path, alignX, alignY, zoomV):
  add path xalign alignX yalign alignY zoom zoomV

screen show_char_pos(path, posX, posY, zoomV):
  add path zoom zoomV xpos posX ypos posY

screen show_char_pos1(path, posX, posY, zoomV):
  add path zoom zoomV xpos posX ypos posY

screen show_char_pos2(path, posX, posY, zoomV):
  add path zoom zoomV xpos posX ypos posY

#Hero ========================================================================================
define player = Character("[nom]", color="#ebc634", image="boy")

define boy_angry = "Perso/hero/boy_angry.png"
define boy_confused = "Perso/hero/boy_confused.png"
define boy_cry = "Perso/hero/boy_cry.png"
define boy_flustered = "Perso/hero/boy_flustered.png"
define boy_happy = "Perso/hero/boy_happy.png"
define boy_nervous = "Perso/hero/boy_nervous.png"
define boy = "Perso/hero/boy_normal.png"
define boy_sad = "Perso/hero/boy_sad.png"
define boy_shocked = "Perso/hero/boy_shocked.png"

define zoom_boy = 0.25
#Hero ========================================================================================

#Pere ========================================================================================
define dad = Character("Papa", color="#3443eb", image="dad")
define dad_path = "Perso/pere/dad.png"
define dad_smoking = "Perso/pere/dad_smoking.png"

define zoom_dad=0.7
#========================================================================================

#Meilleur amie ========================================================================================
define best_friend = Character("Emma", color="#3443eb", image="best_friend")
define best_friend_neutral = "Perso/amie/amie_neutral.png"
#define best_friend_angry = "Perso/amie/amie_neutral.png"
define best_friend_annoyed = "Perso/amie/amie_gene.png"
#define best_friend_sad = "Perso/amie/amie_neutral.png"
define best_friend_smile = "Perso/amie/amie_happy.png"
define best_friend_reading = "Perso/amie/amie_lecture.png"

define zoom_best_friend = 1.4
#========================================================================================

#Mere ========================================================================================
define mere = Character("Maman", color="#ebe834", image="mere")
define mere_neutral = "Perso/mere/mere_bienveillante.png"
define mere_angry = "Perso/mere/mere_colere.png"
define mere_happy = "Perso/mere/mere_rire.png"
define mere_sad = "Perso/mere/mere_sad.png"
define mere_surprised = "Perso/mere/mere_surprised.png"
define zoom_mom = 0.7
# ========================================================================================

#Professeur =========================================================================
define teacher = Character("Professeur", color="#ebe834", image="teacher")
define teacherP = "Perso/professeur/professeur_talking.png"
define teacher_annoyed = "Perso/professeur/professeur_talking_2.png"

define zoom_teacher = 0.9
#=====================================================================================

#GM =========================================================================
define gmu = Character('Shiawase', color="#c8ffc8", image = "game_master_1")
define game_master_1 = "Perso/gm1/GM1_1.png"

define gml = Character("Jiyu", color="#c8ffc8")
define game_master_2 = "Perso/gm2/GM2_1.png"

# =========================================================================

#Docteur perso =========================================================================
define doc = Character("[nom]", color="#c8ffc8")
define docteur = "Perso/docteur/Dr_noname.png"

define zoom_doc = 0.4
# ======================================================================================

#Camarade =========================================================================
define camarade_1 = Character("Camarade", color="#32a852")
define camarade_2 = Character("Autre camarade", color="#32a852")
#======================================================================================

#Infirmiere ======================================================================================
define infirmiere = Character("Infirmiere", color="#85ce25")
define infirmierePath = "Perso/infirmiere/infirmiere.png"
define zoom_infirmiere = 0.9
#======================================================================================

#Chirurgien ======================================================================================
define chir = Character("Michelle", color="#85ce25")
define chirurgien = "Perso/docteur/dr_Michelle.png"
define zoom_chir = 0.4
#======================================================================================

#Prisonnier ======================================================================================
define priso = Character("[nom_priso]", color="#85ce25")
define prisonnier = "Perso/prisonnier/prisonnier.png"

define nom_priso = "Prisonnier"
define zoom_priso = 0.4
#======================================================================================

#Policiers ======================================================================================
define poli1 = Character("Policier 1", color="#85ce25")
define poli2 = Character("Policier 2", color="#85ce25")

define policier_1 = "Perso/policiers/police_1.png"
define policier_2 = "Perso/policiers/police_2.png"

define zoom_poli1 = 1.9
define zoom_poli2 = 0.8

#======================================================================================

#SDF
define sdf = Character("SDF", color="#85ce25")

define sdf_normal = "Jour2/SDF/SDF complet - Normal.png"
define sdf_decu = "Jour2/SDF/SDF complet - decu.png"
define sdf_gene = "Jour2/SDF/SDF complet - gene.png"

define zoom_sdf = 1.0


define mere_enfant = Character("Mere", color="#85ce25")

define mere_enfant_im = "Soir1/mere/coral_sad.png"

define zoom_mere_enfant = 0.7


#Backgrounds

#Space
image earth_close = im.Scale("Intro/earth_close.jpg", 1920, 1080)
image earth_far = im.Scale("Intro/earth_far.jpg", 1920, 1080)
image universe = im.Scale("Intro/universe.png", 1920, 1080)

#Chambre hreo
image room_hero = im.Scale("Backgrounds/chambre_hero/room_day.png", 1920, 1080)
image room_hero_night = im.Scale("Backgrounds/chambre_hero/room_night.png", 1920, 1080)
image room_night_light = im.Scale("Backgrounds/chambre_hero/room_night_light.png", 1920, 1080)

#Salon
image salon = im.Scale("Backgrounds/cuisine_salon/salon_jour.png", 1920, 1080)
image salon_crepuscule = im.Scale("Backgrounds/cuisine_salon/salon_dawn.png", 1920, 1080)
image salon_nuit = im.Scale("Backgrounds/cusiine_salon/salon_nuit.png", 1920, 1080)

#Ecole
image classroom = im.Scale("Backgrounds/ecole/classroom.png", 1920, 1080)
image classroom_empty_full_light = im.Scale("Backgrounds/ecole/classroom_empty_full_light.png", 1920, 1080)
image classroom_empty_mid_light = im.Scale("Backgrounds/ecole/classroom_empty_mid_light.png", 1920, 1080)
image classroom_empty_no_day_light = im.Scale("Backgrounds/ecole/classroom_empty_no_day_light.png", 1920, 1080)
image classroom_teacher = im.Scale("Backgrounds/ecole/classroom_teacher.png", 1920, 1080)
image ecole_couloir = im.Scale("Backgrounds/ecole/couloir.png", 1920, 1080)
image ecole_entree_jour = im.Scale("Backgrounds/ecole/entree_jour.png", 1920, 1080)
image lunchroom_empty_dawn = im.Scale("Backgrounds/ecole/lunchroom_empty_dawn.png", 1920, 1080)
image lunchroom_empty = im.Scale("Backgrounds/ecole/lunchroom_empty.png", 1920, 1080)
image lunchroom_full = im.Scale("Backgrounds/ecole/lunchroom_full.png", 1920, 1080)
image lunchroom_full_no_sunlight = im.Scale("Backgrounds/ecole/luchroom_full_no_sunlight", 1920, 1080)
image lunchroom_half_full = im.Scale("Backgrounds/ecole/lunchroom_half_full.png", 1920, 1080)




#transition : jour nuit plus de temps genre ellipse


#Ville
image city_day  = im.Scale("Backgrounds/ville/ville_jour.png", 1920, 1080)
image city_night = im.Scale("Backgrounds/ville/ville_nuit.png", 1920, 1080)

#hopital
image hopital_couloir = im.Scale("Backgrounds/hopital/hopital_couloir.jpg", 1920, 1080)
image hopital_consultation = im.Scale("Backgrounds/hopital/hopital_consultation.jpg", 1920, 1080)
image hopital_exterieur = im.Scale("Backgrounds/hopital/hopital_exterieur.png", 1920, 1080)
image hopital_operation = im.Scale("Backgrounds/hopital/operation_1.jpg", 1920, 1080)

#salle_info
image salle_info_ouverte = im.Scale("Jour2/Ordinateur/salle_ordi_porte_ouverte.png", 1920, 1080)
image salle_info_ferme = im.Scale("Jour2/Ordinateur/salle_ordi_porte_ferme.png", 1920, 1080)
image ecran_ordi = im.Scale("Jour2/Ordinateur/Ecran ordi - Recherche 1.png", 1920, 1080)

#rue jour 2 
image rue = im.Scale("Jour2/Rue/Rue1 - Jour.png", 1920, 1080)
image boulangerie = im.Scale("Jour2/Rue/Boulangerie - Jour.png", 1920, 1080)

#bibliotheque
image bibliotheque = im.Scale("Jour2/Bibliotheque/Bibliotheque - Jour.png", 1920, 1080)

image black_background = im.Scale("black_background.png", 1920, 1080)

define utilitarisme = 0
define libertarianisme = 0

define config.menu_include_disabled = True

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

    #show screen test_screen()

    #show game_master_1
    #with dissolve
    show screen show_char(game_master_1, -0.1, 1.0, 1.0)
    with dissolve


    show screen show_char1(game_master_2, 1.0, 1.0, 1.0)
    with dissolve

    gmu "NON PAS DU TOUT, TU TE TROMPES !"
    gml "C'EST TOI QUI TE TROMPES TU RACONTES N'IMPORTE QUOI !"

    gmu "De toute façon c’est moi le plus grand alors c’est moi qui décide."
    gml " Mais non, on a le même âge ! Et c’est moi le plus beau."

    gmu "Arrête un peu tes conneries ! On ne peut pas laisser tout le monde faire ce qu’il veut. Il faut des règles."
    gml " Mais il y a des règles ! Chacun dispose de lui-même comme il le souhaite, sans que personne ne puisse l’en empêcher."
    gmu "Ça ne marchera jamais !"
    gml "Bien sûr que si ! "
    gml "Et tu penses que laisser la décision au plus grand nombre est plus efficace ?"
    gmu "Tout à fait ! En satisfaisant le plus gens, tout le monde est content."
    gml "Non, pas tout le monde ! Tu ne penses pas à toutes les minorités que tu exclus. "
    gml "Si tout le monde dispose de lui comme il l’entend, chacun est satisfait."
    gmu "Mais c’est l’anarchie ! Personne n’a le contrôle."
    gml "C’est ça ton problème, tu veux toujours avoir le contrôle sur tout. Laisse les autres décider de ce qu’ils veulent."
    gmu "Mais les gens ont besoin d’être guidés."
    gml "…"
    gmu "…"
    gml "Je sais comment te prouver que tu as tort. "
    gml "On va faire une expérience sur des cas réels. On a tout l’univers à notre disposition. On peut choisir n’importe qui, n’importe où parmi les 299 792 458 planètes."
    gmu "Alors c’est moi qui choisis la…"
    gml "Trop tard, hi hi hi ! J’ai déjà choisi celle-là."

    call hide_chars

    jump intro_gm_earth

label intro_gm_earth:
    
    scene earth_far
    with dissolve

    show screen show_char(game_master_1, -0.1, 1.0, 1.0)
    with dissolve

    show screen show_char1(game_master_2, 1.0, 1.0, 1.0)
    with dissolve

    gml "Reste plus qu'à trouver notre ..."
    gmu "J'ai déjà choi ! On se retrouve en bas frangin !"

    hide screen show_char
    with dissolve

    gml "Hé attends-moi ! Aaaaarrrrh, il m'énerve ..."

    hide screen show_char1
    with dissolve

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

    mere "Réveille-toi, [nom]! Tu vas être en retard à l'école!!"

    scene room_hero
    with dissolve

    show screen show_char(mere_neutral, 0.0, 1.0, zoom_mom)
    with dissolve

    show screen show_char1(boy, 1.0, 1.0, zoom_boy)
    with dissolve

    player "*Bâille* Il faut que j'aille à la cuisine prendre mon petit déjeuner avant d'aller en cours..."
    

    call hide_chars
    menu:
      "Cuisine":
        jump jour1_cuisine

label jour1_cuisine:

    scene salon
    with dissolve

    show screen show_char(mere_neutral, 0.0, 1.0, zoom_mom)
    with dissolve

    show screen show_char1(boy, 1.0, 1.0, zoom_boy)
    with dissolve

    mere "Ah tu es debout, très bien! Voilà tes céréales, [nom]. Mange-les vite, tu dois te dépêcher." 

    menu:
      "Bol":
        jump jour1_bol

label jour1_bol:

    player "*Crunch, crunch*"
    player "Bon j'y vais ! A ce soir maman."
    mere "Bonne journée, mon chou !"
    menu:
      "Extérieur":
        call hide_chars
        jump jour1_exterieur

label jour1_exterieur:
    # Carte de la ville à ajouter

    scene classroom_teacher
    with dissolve

    show screen show_char(teacherP, 0.0, 1.0, zoom_teacher)
    with dissolve


    teacher  "Bonjour tout le monde, aujourd'hui nous allons voir ensemble l'anatomie du système digestif."
    teacher  "Est-ce que quelqu'un arrive à me dire quels organes en font partie ?"

    "*Silence*"

    call hide_chars

    show screen show_char(teacher_annoyed, 0.0, 1.0, zoom_teacher)
    with dissolve

    teacher "Personne ? N'oubliez pas que vous examens finaux sont le mois prochain, il va falloir se mettre au travail !"

    call hide_chars
   
    show screen show_char(boy_nervous, 1.0, 1.0, zoom_boy)
    with dissolve

    player "Je sens que cette matinée va être longue...Vivement la pause de midi !"

    call hide_chars

    jump jour1_lunch

label jour1_lunch:

    scene lunchroom_full
    with dissolve


    show screen show_char(best_friend_smile, 0.0, 1.0, zoom_best_friend)
    with dissolve

    show screen show_char1(boy_confused, 1.0, 1.0, zoom_boy)
    with dissolve


    best_friend "[nom]! Tu es là !"
    best_friend "Comment s'est passée ta matinée ?"

    menu:
      "Ennuyant":
        player "Ennuyant à mourir... On a fait de la biologie."
      "Passionnant":
        player "Passionnant! Le corps humain est fascinant."
      "Long":
        player "Long, je meurs de faim."

    best_friend "Je vois ! Dépêchons nous d'aller manger, il y a déjà une queue."
    player "J'arrive!"

    call hide_chars

    jump jour1_manger

label jour1_manger:
    scene balck_screen
    with dissolve

    scene lunchroom_full
    with dissolve

    show screen show_char(best_friend_smile, 0.0, 1.0, zoom_best_friend)
    with dissolve
    
    show screen show_char1(boy_confused, 1.0, 1.0, zoom_boy)
    with dissolve


    best_friend "Heureusement qu'on s'est dépêché, on a eu les dernières places!" 
    best_friend "Avec les examens qui arrivent tout le monde est stressé et veut manger au plus vite pour avoir le temps de réviser..."
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
    

    call hide_chars

    jump jour1_cours

label jour1_cours:

    scene classroom_teacher
    with dissolve


    show screen show_char(teacherP, 0.0, 1.0, zoom_teacher)
    with dissolve

    teacher "N'oubliez pas vos devoirs pour demain! Lire un chapitre du livre et répondre aux questions liées. On en parlera tous ensemble demain."
    teacher "Bonne soirée."

    call hide_chars

    camarade_1 "Aaaah, j'avais oublié, je vais devoir repousser mon entrainement..."
    camarade_2 "Je pense que tu vas pouvoir les oublier tes entrainements ces prochains temps! On va devoir mettre toute notre énergie dans les révisions..."
    
    show screen show_char(boy_nervous, 1.0, 1.0, zoom_boy)
    with dissolve

    player "Ils plaisantent pas avec ces examens..."
    camarade_2 "Vraiment... Et en plus, on a une grosse journée demain..."
    player "Il va falloir que j'aille me coucher tôt si je veux être en forme."

    call hide_chars


    jump jour1_maison_soir

label jour1_maison_soir:
    
    scene salon
    with dissolve

    show screen show_char_pos(dad_path, -250, 500, zoom_dad)
    with dissolve

    dad "Alors, tu as bien travaillé aujourd'hui, [nom] ?"

    show screen show_char_pos1(boy, 1300, 500, 0.4)
    with dissolve


    menu:
      "Oui":
        player "Oui, on a vu le système digestif. Mais c'est compliqué."
      "Pas tellement":
        player "J'ai pas tellement suivi..."
      "J'ai beaucoup de travail.":
        player "Oui, mais j'ai encore des devoirs pour demain à finir."

    show screen show_char_pos2(mere_neutral, 700, 500, 0.9)
    with dissolve


    mere "Alors, il faut que tu travailles consciencieusement ce soir. Tu aurais besoin d'aide?"
    player  "Non, ça va aller."
    mere "N'hésite pas, si besoin. Il faut que tu les réussisses ces examens!"
    dad "Ne lui mets pas tant de pression, c'est encore un enfant."
    player "Papa !"
    mere "Oui, je sais... Un adolescent."
    player "*Soupir* Je vais travailler dans ma chambre."

    call hide_chars

    jump jour1_chambre_soir

label jour1_chambre_soir:
    
    scene room_night_light
    with dissolve

    show screen show_char(boy_sad, 0.0, 1.0, zoom_boy)
    with dissolve

    player "J'ai fini mes devoirs mais je n'arrive pas à dormir..."
    player "Ces histoires d'examens me stressent."
    player "J'espère que je ne vais pas faire un rêve comme Emma cette nuit, je suis crevée."
    call hide_chars
    jump reve_1
























label reve_1:

  scene universe
  with dissolve

  show screen show_char(game_master_1, 0.0, 1.0, 1.0)
  with dissolve

  gmu "Hey ! T’es enfin réveillé ?"

  narrateur "Le joueur se réveille petit à petit et se trouve en face d’un mystérieux personnage dans une salle étrange."

  show screen show_char1(boy_confused, 1.0, 1.0, zoom_boy)
  with dissolve

  gmu "Dis-moi tu n’as pas l’air de comprendre ce qu'il t’arrive."

  menu:
    "Qui est-tu ?":
      jump reve1_next
    "Où suis-je":
      jump reve1_next

label reve1_next:

  
  gmu "C’est bien ce qui me semblait. 
      Tu as été choisi parmi tous les êtres intelligents de l’univers pour avoir la noble tâche de prouver que je suis le plus sage et que ma vision du monde est la meilleure."

  player "Tous les êtres humains de l’univers ??? Il y a d’autres formes de vie intelligente ?"

  gmu " *Ne fais pas attention à ce que le joueur dit* C’est simple : il faut toujours chercher à maximiser le bonheur du plus grand nombre."

  gmu "Le noyau central de ma pensée est qu’il faut toujours chercher à maximiser le bonheur de la majorité."
  gmu "Alors qu’est-ce tu en penses ?"

  menu:
    "Oui c'est idéal":
      player "Oui c’est idéal. Je rêverai de vivre dans une telle société."
      gmu "Finalement j’ai peut-être choisi la bonne personne"
    "Indécis":
      player "Je ne sais pas, cela me paraît utopique mais assez difficilement réalisable."
      gmu "Toujours septique hein ? Tu verras bien assez vite comment ça s’applique."
      player "J’ai un peu peur de la place des minorités dans tout ça. Et puis… Comment définir le bonheur ?"
      gmu "Définir le bonheur…"
      gmu "C’est simple, c’est quand t’es heureux."
    "Suspicieux":
      player "Je n’ai pas encore assez étudié la question, il y a peut-être des cas où ce n’est pas la meilleure solution."
      gmu "Un cas où ce n’est pas la meilleure solution ? Les humains sont-ils tous aussi stupides que toi ?"
      player "J’ai un peu peur de la place des minorités dans tout ça. Et puis… Comment définir le bonheur ?"
      gmu "Définir le bonheur…"
      gmu "C’est simple, c’est quand t’es heureux."

  gmu "Bon allez, passons à la suite. Je n’ai pas que ça à faire que de t’apprendre des choses que tout le monde sait déjà."
  gmu "Pour pouvoir interpréter correctement les résultats de ma petite expérience, j’ai besoin de savoir qui est mon sujet."

  show screen show_char1(boy_angry, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Ça te tuerait de me respecter un peu… Je m’appelle [nom]."

  gmu "Je n’en ai strictement rien à faire. Je sais que tu es allé voir ta meilleure amie durant son audition de pi… * Interjection *."
  player "Attends ! Comment-tu sais qu’elle joue de la musique ?"
  gmu "Je sais tout ! Enfin presque…  Lui as-tu dit ce que tu en avais vraiment pensé ? Je crois sentir que ça ne t’a pas spécialement plus."
  player "Ça ne te regarde pas !"
  gmu "Dis-moi juste si tu lui as dit ce que tu en as réellement pensé ?"

  menu:
    "Oui":
      $ utilitarisme+=0
    "Non":
      $ utilitarisme+=1
  
  show screen show_char1(boy_confused, 1.0, 1.0, zoom_boy)
  with dissolve
  
  gmu "Très bien."


  player "Ces choix vont-ils avoir des conséquences sur ma vie ??? J’ai un peu peur…"
  gmu "Ah ça, tu le découvriras plus tard."
  gmu "Bon à présent on va passer à la partie un peu plus pratique. Pour le reste de la journée tu vivras dans la peau d’un chirurgien."
  gmu "Tu seras amené à faire des choix importants et tu comprendras, je l’espère, pourquoi ma façon de penser est la meilleure."

  call hide_chars

label reve1_hopital:

  scene hopital_exterieur
  with dissolve

  show screen show_char(docteur, 0.0, 1.0, zoom_doc)
  with dissolve

  show screen show_char1(game_master_1, 1.0, 1.0, 1.0)
  with dissolve

  narrateur "* Shiawase clac des doigts et les deux se retrouvent devant l'hôpital. *"

  doc "Nous sommes devant un hôpital à ce que je vois."
  gmu "Oui c'est bien ça. Bon à partir de maintenant je te laisse."
  doc "Comment ça ?"
  gmu "Tant que tu feras les bons choix tout ira bien pour toi. Allez à plus."

  call hide_chars

  jump reve1_hopital_interieur

label reve1_hopital_interieur:
  
  scene hopital_couloir
  with dissolve

  show screen show_char(docteur, 0.0, 1.0, zoom_doc)
  with dissolve

  show screen show_char1(infirmierePath, 1.0, 1.0, zoom_infirmiere)
  with dissolve

  infirmiere "Vous voilà enfin. Le patient est déjà prêt pour son opération. Il s’agit d’une fracture de l’avant-bras. 
Nous allons vous préparer."

  call hide_chars

label reve1_hopital_after_op:

  scene black_background
  with dissolve

  narrateur "Après quelques minutes le joueur se trouve dans une salle d’opération avec d’autres chirurgien. Au début le joueur 
  n’est pas sûr que ce qu’il faut faire mais comme annoncer par le GMU il commence à procéder à l’opération comme si 
  c’était quelque chose qu’il avait fait tout sa vie"

  menu:
    "Aller dehors":
      call hide_chars
      jump reve1_hopital_after_op_next
    "Aller à la cafétéria":
      call hide_chars
      jump reve1_hopital_after_op_next
    "Aller à la salle de repos":
      call hide_chars
      jump reve1_hopital_after_op_next

label reve1_hopital_after_op_next:

  scene hopital_couloir
  with dissolve

  narrateur "En se rendant à sa destination, le joueur se rend compte que tout le monde semble paniqué"

  show screen show_char(infirmierePath, 0.0, 1.0, zoom_infirmiere)
  with dissolve

  show screen show_char1(docteur, 1.0, 1.1, zoom_doc)
  with dissolve

  player "Qu’est-ce qu’il passe ici ? "

  infirmiere "*Affolé* Un camion est rentré dans un bus scolaire, c’est un carnage…"

  infirmiere "On a besoin de tout le personnel. On va devoir faire des opérations avec une seule équipe pour plusieurs patients."
  infirmiere "Il y a trois adultes qui ont des bouts de verre un peu partout sur le corps."
  infirmiere "Ils sont stables pour l’instant mais ça pourrait s’aggraver si le travail est mal fait ou si ça tourne en septicémie."
  infirmiere "Les infirmières essayent de faire de leur mieux mais elles ont besoin d’un chirurgien expérimenté pour les guider et tout contrôler."
  infirmiere "Tu peux aller au bloc B3 et t’en occuper ?"
  player "Oui, j’y vais tout de suite. "

  call hide_chars

  scene black_background
  with dissolve

  narrateur "*En se rendant au bloc B3 le joueur est interpellé par une maman*"

  scene hopital_couloir
  with dissolve


  show screen show_char(mere_enfant_im, 0.0, 1.0, zoom_mere_enfant)
  with dissolve

  show screen show_char1(docteur, 1.0, 1.1, zoom_doc)
  with dissolve

  mere_enfant "S’il vous plaît, sauvez mon fils ! Je vous en supplie !"

  infirmiere "Madame, laissez le personnel travailler."

  mere_enfant "Je vous en supplie !"

  player "Dans quel état est son fils ?"

  show screen show_char(infirmierePath, 0.0, 1.0, zoom_infirmiere)
  with dissolve


  infirmiere "Dans un état grave. Saignement interne, perte de conscience. "
  infirmiere "De nombreux organes sont touchés, si on ne l’opère pas tout de suite c’est fini pour lui."
  infirmiere "Mais il n’y a plus personne de disponible. Même si on intervient, vu son état on n’est même pas sûr de pouvoir le sauver."


  menu:
    "S'occuper des adultes":
      $ utilitarisme+=2
      call hide_chars
      jump reve1_soins_adultes
    "S'occuper de l'enfant":
      call hide_chars
      jump reve1_soin_enfant

label reve1_soins_adultes:
  scene hopital_consultation
  with dissolve

  show screen show_char(infirmierePath, 0.0, 1.0, zoom_infirmiere)
  show screen show_char1(docteur, 1.0, 1.0, zoom_doc)
  with dissolve

  infirmiere "J'ai un doute sur la façon de procéder ici. Cette zone est assez sensible et j'ai peur de lui sectionner une artère."
  doc "Oui, il suffit juste de faire comme ça."

  narrateur "Vous sentez une infirmière dans le doute à un moment. Vous décidez d’intervenir, vous venez de sauver la vie de cet adulte."

  call hide_chars

  scene black_background
  with dissolve

  narrateur "Après plusieurs heures d’opérations, les adultes sont sains et saufs. Ils ne courent plus aucun risque et pourront rejoindre leurs familles dans 4 jours."

  call hide_chars

label reve1_soins_enfant:
  scene hopital_operation
  with dissolve

  show screen show_char(docteur, 0.0, 1.0, zoom_doc)
  with dissolve

  doc " *Pense* Il faut que je te donne tout pour que cette mère revoit son enfant sain et sauf."

  "..."

  doc "J'ai donné tout ce que j'avais, je ne peux rien faire de plus."

  call hide_chars

  scene black_background
  with dissolve

  narrateur "L’enfant était dans un état trop grave. 
  Vous n’avez rien pu faire. Une des infirmières qui venait de commencer à l’hôpital a malheureusement commis une erreur et a sectionné une artère d'un adulte, le patient est mort."

  narrateur "Vous êtes fatigués mais vous prenez un café. Après quelques minutes vous sentez l’effet."
  narrateur "Le prochain bus est dans 30 min, si vous le prenez, vous allez peut-être rater le concert que vous avez offert à votre femme pour son 30eme anniversaire"

  menu:
    "Rentrer en voiture":
      jump voiture_reve1
    "Rentrer en bus":
      $ utilitarisme+=1
      jump bus_reve1

  

label voiture_reve1:


  scene city_day
  with dissolve

  show voiture_1:
    xpos 1350
    ypos 500
    zoom 0.15

  with dissolve

  show famille_5:
    xpos 1550
    ypos 500
    zoom 0.5
  with dissolve

  narrateur "Sur le chemin vous n’arrêtez pas de penser à ce jeune garçon, mort dans d’atroces souffrances* * Perdu dans vos pensées, vous ne faites pas attention. *"
  narrateur "*Cul de poule, perte de contrôle, accident* *Une famille décède*"

  call hide_chars

label bus_reve1:


  scene city_day
  with dissolve

  narrateur "*Le bus arrive en avance* *La route est dégagée sur le chemin* Vous arrivez à l’heure pour l’évènement*. *Réveil en sursaut*"

  call hide_chars































label jour2:
  
  scene room_hero
  with dissolve 

  "Réveil en sursaut, des sueurs froides coulant dans ton dos."

  show screen show_char(boy_shocked, 0.0, 1.0, zoom_boy)
  with dissolve

  player "Qu'est-ce que c'était que ce rêve??"
  player "Je n'en avais jamais fait d'aussi réaliste... J'en ai encore des frissons."
  player "En tout cas, ça me donne pas envie de devenir médecin!"

  "..."
  "..."

  player "Je ne me sens pas du tout reposé, c'est comme si j'avais vraiment dû faire ces opérations!"
  player "Et ces choix ...:"
  menu:
    "C'était facile":
      player "Au moins, c'était facile de choisir !"
    "Intéressant":
      player "Je me suis vraiment creusé la tête dans mon rêve, c'était intéressant !"
    "Plus jamais !":
      player "J'espère que je n'aurais jamais à faire des choix pareils dans la vraie vie..."
  
  mere "[nom], qu'est-ce que tu fais encore ? Tu vas de nouveau devoir courir!"
  player "J'arrive, j'arrive ..."

  call hide_chars

  jump jour2_cuisine

label jour2_cuisine:
  scene salon
  with dissolve

  show screen show_char_pos(dad_path, -250, 500, zoom_dad)
  show screen show_char_pos1(boy_nervous, 1300, 500, 0.4)
  show screen show_char_pos2(mere_neutral, 700, 500, 0.9)
  with dissolve

  dad "Tu as bien dormi, [nom] ?"
  player "Pas vraiment non..."
  mere "Il va falloir te reprendre, chou, n'oublie pas que tu as un groupe de travail ce soir."
  player  "Ah oui... Et en plus c'est mon tour d'amener un truc à manger aujourd'hui."
  player "D'ailleurs, je peux avoir des sous?"
  mere "Tiens, 10.-, mais ne fais pas comme la dernière fois, achète vraiment quelque chose pour tes amis!"
  
  show screen show_char_pos1(boy_flustered, 1300, 500, 0.4)
  with dissolve

  player "Oui, oui, ne t'inquiète pas."

  show screen show_char_pos1(boy, 1300, 500, 0.4)
  with dissolve
  
  hide screen show_char_pos
  hide screen show_char_pos2
  with dissolve
  
  player "Bon, j'ai vraiment la dalle. Je mange un bout et j'y vais."
  player "Zut ! Il ne reste qu'une seule brioche. J'ai vraiment faim mais mon père va encore me faire une crise."
  player "Je n'ai pas de temps à perdre avec ça."

  define brioche_state = 0

  menu:
    "Manger toute la brioche":
      $ brioche_state=1
    "Laisser la brioche à ton père":
      $ brioche_state=2
    "Partager la brioche en deux" if utilitarisme>=2:
      $ brioche_state=3
  

  call hide_chars

  jump jour2_classe


label jour2_classe:

  scene classroom_teacher
  with dissolve

  show screen show_char(boy_shocked, 0.0, 1.0, zoom_boy)
  with dissolve

  player "*Pense* Je n'arrive pas à me concentrer..."
  player "Je n'arrête pas de repenser à mon rêve de cette nuit."
  if brioche_state==2:
    player "En plus j'ai du mal à réfléchir le ventre vide."
  player "Et si ce n'était pas vraiment un rêve?"
  player "On entend souvent parler de gens qui ont des visions envoyées par des démons ou des dieux..."
  
  menu:
    "Mais ce sont des fous":
      player "Mais je me suis toujours dit qu'ils devaient être fous ou rechercher l'attention!"
    "C'est plutôt cool en fait":
      show screen show_char(boy_happy, 0.0, 1.0, zoom_boy)
      with dissolve
      player "Je me suis toujours dit que c'était trop classe!"
    "Je n'y crois pas.":
      player "Je ne sais pas si je peux vraiment y croire..."
  

  teacher "[nom]! Qu'est-ce que tu as ce matin?? Ca fait 3 fois que je te pose une question et tu ne fais que regarder dans le vague!"

  show screen show_char(boy_flustered, 0.0, 1.0, zoom_boy)
  with dissolve

  player "Ah, désole Professeur... J'ai mal dormi cette nuit."

  teacher "Hum, je vais laisser passer pour cette fois, mais tâchez à que cela ne se reproduise plus!"

  call hide_chars

  scene black_background
  with dissolve

  "Pause de midi"

  jump jour2_midi

label jour2_midi:
  scene lunchroom_full
  with dissolve

  show screen show_char(boy_confused, 0.0, 1.0, zoom_boy)
  show screen show_char1(best_friend_smile, 1.0, 1.0, zoom_best_friend)
  with dissolve

  best_friend "... Et quand il s'est enfin retourné, toute la classe a vu l'énorme trou dans son pantalon! HAHAHAH"

  "..."

  show screen show_char1(best_friend_neutral, 1.0, 1.0, zoom_best_friend)
  with dissolve

  best_friend "[nom] ? Tu t'es endormi pendant mon histoire ou bien? Tu as même pas rigolé!"

  player "Ah désolé, Emma!"
  player "J'ai la tête ailleurs..."

  best_friend "Je vois ça, quelque chose te tracasse? Un problème à la maison ? Ou juste les examens?"

  player "*Pense* Je ne peux pas lui parler de mon rêve, elle ne va jamais comprendre..."
  player "*Pense* Déjà qu'hier je lui ai dit que les rêves ne sont pas réels, elle va me prendre pour un fou."

  show screen show_char(boy_flustered, 0.0, 1.0, zoom_boy)
  with dissolve

  player "Les examens..."
  player "D'ailleurs, il faut que j'aille faire des recherches pour"
  menu:
    "Danse contemporaine":
      player "Mon cours de danse contemporaine."
    "La chute de l'Atlantide":
      player "Mon exposé sur la chute d'Atlantide."
    "Le coeur des fourmis":
      "En apprendre plus sur les problèmes de coeur des fourmis."
  
  best_friend "Je vois.. A bientôt alors."
  player "A plus!"

  call hide_chars

  jump jour2_salle_info

label jour2_salle_info:



  scene salle_info_ouverte
  with dissolve

  show screen show_char(boy_shocked, 0.0, 1.0, zoom_boy)
  with dissolve

  player "Je n'aime pas mentir à MA mais là je n'avais pas le choix..."
  player "Bon, j'aurais quand même pu trouver une meilleure excuse par contre!"
  player "J'aurais pu lui dire que j'avais mal à la tête..."
  player "Au moins, maintenant je suis tranquille pour faire des recherches sur les rêves et visions."

  

  call hide_chars

  scene ecran_ordi
  with dissolve

  player "Qu'est-ce que je pourrais bien rechercher ?"

  menu:
    "Visions + Dieu":
      jump jour2_info_next
    "Rêves + réalistes":
      jump jour2_info_next
    "Ethique + Démon":
      jump jour2_info_next
  
label jour2_info_next:
  
  scene black_background
  with dissolve

  "*Après quelques recherches...*"

  scene salle_info_ferme
  with dissolve

  show screen show_char(boy_nervous, 0.0, 1.0, zoom_boy)
  with dissolve


  player "On trouve vraiment de tout et de rien sur internet!"
  player "Je tombe autant sur des articles scientifiques qui expliquent les rêves lucides, que sur des témoignages de gens qui affirment avoir rencontré Dieu..."
  player "J'ai le cerveau qui surchauffe, je crois que je vais m'arrêter là pour aujourd'hui..."
  player "D'autant plus que si je ne pars pas maintenant je vais arriver en retard à mon groupe de travail, et je dois encore aller acheter à grignoter"

  call hide_chars

  jump jour2_rue

label jour2_rue:
  scene rue
  with dissolve

  show screen show_char(boy, 0.0, 1.0, zoom_boy)
  with dissolve

  if brioche_state==1:
    player "Je n'aurais peut-être pas dû prendre la brioche de papa ce matin. J'espère qu'il ne m'en voudra pas trop."
    player "Mais bon, j'ai d'autres choses à penser."

  player "Il me semble qui il y a une boulangerie au coin de cette rue."
  player "Avec 10.-, je vais pouvoir me rattraper de la dernière fois, où j'ai oublié d'amener quelque chose!"
  player "Peut-être des croissants pour tout le monde... Ou du pain et plein de chocolat ?"
  player "Hummmm...."

  call hide_chars

  jump jour2_boulangerie

label jour2_boulangerie:
  scene boulangerie
  with dissolve

  show screen show_char(boy, 0.0, 1.0, zoom_boy)
  show screen show_char1(sdf_normal, 1.0, 1.0, zoom_sdf)
  with dissolve

  sdf "Eh !"
  sdf "Eh, toi là!"

  show screen show_char(boy_flustered, 0.0, 1.0, zoom_boy)
  with dissolve

  player "On m'a parlé ?"

  show screen show_char(boy, 0.0, 1.0, zoom_boy)
  with dissolve

  sdf "Ah, oui c'était moi ! Excuse moi mais tu a l'air de quelqu'un de généreux. J'ai perdu mon travail l'année passée et depuis, ma femme m'a quitté et on m'a éjecté de mon appart..."
  sdf "Tu n'aurais pas un peu d'argent pour que je m'achète à manger?"

  player "L'argent que j'ai sur moi est pour acheter un gouter à mes amis... "

  define sdf_state = 0

  menu:
    "Mais je te le donne.":
      $ sdf_state=1
      player "Mais je te le donne volontiers, ils comprendront bien!"
      sdf "Merci! Je suis sûr que tes amis ne t'en voudront pas d'aider quelqu'un dans le besoin."
      sdf "Bonne soirée!"
      hide screen show_char1
      with dissolve
      player "Même si mes amis risquent d'être déçus et que ma mère va encore me faire une remarque, j'ai fait une bonne action aujourd'hui!"
    "Mais je te donne la moité." if utilitarisme>=1:
      $ sdf_state=2
      player "Mais je t'en donne la moitié, ils se contenteront de pain sans chocolat!"
      sdf "Merci! Je suis sûr que tes amis ne t'en voudront pas d'aider quelqu'un dans le besoin."
      sdf "Bonne soirée!"
      hide screen show_char1
      with dissolve
      player "Même si mes amis risquent d'être déçus et que ma mère va encore me faire une remarque, j'ai fait une bonne action aujourd'hui!"
    "Je suis désolé." if utilitarisme>=2:
      $ sdf_state=2
      show screen show_char(boy_flustered, 0.0, 1.0, zoom_boy)
      with dissolve
      player "Je suis désolé demande à quelqu'un d'autre. Bonne chance!"
      show screen show_char1(sdf_decu, 1.0, 1.0, zoom_sdf)
      with dissolve
      sdf "..."
      hide screen show_char1
      with dissolve
      show screen show_char(boy_confused, 0.0, 1.0, zoom_boy)
      with dissolve
      player "*Pense* J'ai peut-être loupé une chance de faire une bonne action mais au moins mes amis et ma mère ne seront pas déçus cette fois!"
    "Trouves-toi du travail !" if utilitarisme>=3:
      $ sdf_state=2
      show screen show_char(boy_angry, 0.0, 1.0, zoom_boy)
      with dissolve
      player "Trouve toi un travail au lieu de vivre comme un parasite!"
      show screen show_char1(sdf_decu, 1.0, 1.0, zoom_sdf)
      with dissolve
      sdf "..."
      hide screen show_char1
      with dissolve
      show screen show_char(boy_confused, 0.0, 1.0, zoom_boy)
      with dissolve
      player "*Pense* J'ai peut-être loupé une chance de faire une bonne action mais au moins mes amis et ma mère ne seront pas déçus cette fois!"
  
  call hide_chars


  jump jour2_revisions

label jour2_revisions:
  
  scene bibliotheque
  with dissolve

  "La séance de révision paraît durer des heures, tes yeux se ferment tout seuls, tu n'arrives pas à te concentrer."
  "Quand c'est enfin le moment de rentrer chez toi, tu dis à peine au revoir et te dépêches d'aller prendre le bus."

  jump jour2_fin

label jour2_fin:
  scene salon_crepuscule
  with dissolve

  show screen show_char(mere_neutral, 0.0, 1.0, zoom_mom)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  mere "Alors, cette séance de révision ? Tu as pensé à acheter du goûter cette fois ?"

  if sdf_state==1:
    show screen show_char1(boy_flustered, 1.0, 1.0, zoom_boy)
    with dissolve
    player "..."
    player "Non... J'ai donné l'argent à quelqu'un dans la rue qui en avait plus besoin que moi..."
    mere "..."
    mere "Bon, au moins cette fois c'était pour une bonne cause. Mais j'espère que tes amis ne vont pas t'en vouloir, tu leur avais quand même promis d'amener quelque chose!"
  elif sdf_state==2:
    show screen show_char1(boy_angry, 1.0, 1.0, zoom_boy)
    with dissolve

    player "Oui, oui, je l'ai fait cette fois!"
    player "Quand est-ce que tu vas arrêter de m'embêter avec ça, j'ai juste oublié une fois!!"

    mere "Pas besoin de t'énerver! Tes amis devaient être contents que tu aies pensé à eux cette fois."
    mere "Tu sais, c'est important de tenir tes promesses si tu veux garder tes amis."
  
  show screen show_char1(boy_flustered, 1.0, 1.0, zoom_boy)
  with dissolve
  player "Oui, maman ..."

  if brioche_state==1:
    mere "Au fait, ton père était vraiment mécontent quand il a vu que tu avais mangé sa brioche"
    show screen show_char1(boy_flustered, 1.0, 1.0, zoom_boy)
    with dissolve
    player  "Je sais maman, je ne peux pas aller à l'école le ventre vide"
    mere "Pense à aller t'excuser et évite que ça se reproduise."
  elif brioche_state==2:
    show screen show_char1(boy, 1.0, 1.0, zoom_boy)
    with dissolve
    mere "Au fait, tu es parti le ventre vide ce matin ?"
    player "Oui, j'ai vu qu'il ne restait qu'une brioche. Je l'ai laissé à papa."
    mere "C'est très gentil à toi mon chéri."
  elif brioche_state==3:
    show screen show_char1(boy, 1.0, 1.0, zoom_boy)
    with dissolve
    mere "Ton père était content que tu lui aies laissé la moitié de sa brioche. Il était étonné  de cette réflexion venant de ta part."
    player "haha ! On en apprend tous les jours !"
    player "*Pense* Ou dans mon cas la nuit."
    mere "C'est bien mon chéri, tu deviens vraiment mature."
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve
  "..."
  "..."
  player "J'ai mal dormi hier soir, je vais aller me coucher tôt pour rattraper ça."
  mere "D'accord, chou."
  mere "Bonne nuit et fait de beaux rêves!"
  player "*Pense* J'espère."











  

label hide_chars:
  
  hide screen show_char
  hide screen show_char1
  hide screen show_char_pos
  hide screen show_char_pos1
  hide screen show_char_pos2
  with dissolve

  return



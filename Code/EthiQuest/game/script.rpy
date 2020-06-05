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
  tag show_char2
  add path xalign alignX yalign alignY zoom zoomV

screen show_char_pos(path, posX, posY, zoomV):
  add path zoom zoomV xpos posX ypos posY

screen show_char_pos1(path, posX, posY, zoomV):
  add path zoom zoomV xpos posX ypos posY

screen show_char_pos2(path, posX, posY, zoomV):
  add path zoom zoomV xpos posX ypos posY

screen show_char_pos3(path, posX, posY, zoomV):
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
define dad_angry = "Perso/pere/dad_angry.png"

define zoom_dad=0.4
#========================================================================================

#Meilleur amie ========================================================================================
define best_friend = Character("Emma", color="#3443eb", image="best_friend")
define best_friend_neutral = "Perso/amie/amie_neutral.png"
define best_friend_angry = "Perso/amie/amie_angry.png"
define best_friend_annoyed = "Perso/amie/amie_gene.png"
define best_friend_sad = "Perso/amie/amie_sad.png"
define best_friend_smile = "Perso/amie/amie_happy.png"
define best_friend_reading = "Perso/amie/amie_lecture.png"

define zoom_best_friend = 0.6
#========================================================================================

#Mere ========================================================================================
define mere = Character("Maman", color="#ebe834", image="mere")
define mere_neutral = "Perso/mere/mere_bienveillante.png"
define mere_angry = "Perso/mere/mere_colere.png"
define mere_happy = "Perso/mere/mere_rire.png"
define mere_sad = "Perso/mere/mere_sad.png"
define mere_surprised = "Perso/mere/mere_surprised.png"
define zoom_mom = 1.4
# ========================================================================================

#Professeur =========================================================================
define teacher = Character("Professeur", color="#ebe834", image="teacher")
define teacherP = "Perso/professeur/professeur_talking.png"
define teacher_annoyed = "Perso/professeur/professeur_angry.png"

define zoom_teacher = 0.3
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
define infirmiere = Character("Infirmier", color="#85ce25")
define infirmierePath = "Perso/infirmiere/infirmier.png"
define zoom_infirmiere = 1.0
#======================================================================================


#SDF
define sdf = Character("SDF", color="#85ce25")

define sdf_normal = "Jour2/SDF/SDF.png"
define zoom_sdf = 1.2


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
image salon = im.Scale("Backgrounds/cuisine_salon/salon_jour.jpg", 1920, 1080)
image salon_crepuscule = im.Scale("Backgrounds/cuisine_salon/salon_dawn.jpg", 1920, 1080)

#Ecole
image classroom_teacher = im.Scale("Backgrounds/ecole/classroom.jpg", 1920, 1080)
image lunchroom_full = im.Scale("Backgrounds/ecole/lunchroom.jpg", 1920, 1080)


image ecole_exterieur = im.Scale("Backgrounds/ecole/Ecole.jpg", 1920, 1080)

image rue_avec_enfants = im.Scale("Backgrounds/ecole/Ecole.jpg", 1920, 1080)

define enfant1 = Character("Enfant 1")
define im_enfant1 = "Jour3/Rue_avec_enfants/Enfant_1.png"
define zoom_enfant1 = 1.0

define enfant2 = Character("Enfant 2")
define im_enfant2 = "Jour3/Rue_avec_enfants/Enfant_2.png"
define zoom_enfant2 = 1.0

define enfant3 = Character("Enfant 3")
define im_enfant3 = "Jour3/Rue_avec_enfants/Enfant_3.png"
define zoom_enfant3 = 1.0




#transition : jour nuit plus de temps genre ellipse


#Ville
image city_day  = im.Scale("Backgrounds/ville/ville_jour.jpg", 1920, 1080)
image city_night = im.Scale("Backgrounds/ville/ville_nuit.jpg", 1920, 1080)

#hopital
image hopital_couloir = im.Scale("Backgrounds/hopital/hopital_couloir.jpg", 1920, 1080)
image hopital_consultation = im.Scale("Backgrounds/hopital/hopital_consultation.jpg", 1920, 1080)
image hopital_exterieur = im.Scale("Backgrounds/hopital/hopital_exterieur.png", 1920, 1080)
image hopital_operation = im.Scale("Backgrounds/hopital/operation_1.jpg", 1920, 1080)

#salle_info
image salle_info_ouverte = im.Scale("Jour2/Ordinateur/salle_info.jpg", 1920, 1080)
image salle_info_ferme = im.Scale("Jour2/Ordinateur/salle_info.jpg", 1920, 1080)
image ecran_ordi = im.Scale("Jour2/Ordinateur/ordi.png", 1920, 1080)

#rue jour 2 
image rue = im.Scale("Jour2/Rue/Rue1 - Jour.jpg", 1920, 1080)
image boulangerie = im.Scale("Jour2/Rue/Boulangerie - Jour.jpg", 1920, 1080)

#bibliotheque
image bibliotheque = im.Scale("Jour2/Bibliotheque/Bibliotheque - Jour.jpg", 1920, 1080)
image bibliotheque_soir = im.Scale("Jour2/Bibliotheque/Bibliotheque - Soir.jpg", 1920, 1080)
image bibliotheque_nuit = im.Scale("Jour2/Bibliotheque/Bibliotheque - Nuit.jpg", 1920, 1080)

image black_background = im.Scale("black_background.png", 1920, 1080)

define utilitarisme = 0
define libertarianisme = 0

define config.menu_include_disabled = True

#Nuit 2

image plage = im.Scale("Nuit2/plage.jpg", 1920, 1080)

define perso_glace = Character("John")

define im_glace = "Nuit2/la_glace.png"
define zoom_glace = 0.4

image maison_martine = im.Scale("Nuit2/maison_martine.jpg", 1920, 1080)

define nain_de_jardin = "Nuit2/nain_1.png"
define zoom_nain = 0.4

image EMS_devanture = im.Scale("Nuit2/entree_EMS.jpg", 1920, 1080)

image EMS_reception = im.Scale("Nuit2/reception.jpg", 1920, 1080)

define receptioniste = Character("Murielle")

define im_receptioniste = "Nuit2/Justine/Hana_casual_neutral.png"

define zoom_receptioniste = 0.6

image EMS_couloir = im.Scale("Nuit2/couloir_EMS.jpg", 1920, 1080)

image EMS_chambre_raymond = im.Scale("Nuit2/chambre_2.jpg", 1920, 1080)

image EMS_pharmacie = im.Scale("Nuit2/pharmacie_EMS.jpg", 1920, 1080)

define raymond = Character("Mme Raymond")

define im_raymond = "Nuit2/old_woman.png"
define zoom_raymond = 1.7

define superieur = Character("Supérieur")

define justine = Character("Justine")

define im_justine = "Nuit2/justine.png"

define zoom_justine = 1.3

image chambre_Dumas = im.Scale("Nuit2/chambre_001.jpg", 1920, 1080)

define im_dumas = "Nuit2/dumas.png"

define zoom_dumas = 1.0

define dumas = Character("M. Dumas")


#Jour3

define fumeur = Character("Fumeur", color="#85ce25")
define im_fumeur = "Jour3/Fumeur/Fumeur.png"

define zoom_fumeur = 1.0

image avant_rue = im.Scale("Jour3/Ruelle_sombre/Avant_ruelle.jpg", 1920, 1080)

image ruelle_sombre = im.Scale("Jour3/Ruelle_sombre/Ruelle_choix_1.jpg", 1920, 1080)

image parc = im.Scale("Jour3/Ruelle_sombre/Parc.jpg", 1920, 1080)

define perso_louche = Character("Personnage louche")

define im_perso_louche = "Jour3/Homme louche/Homme louche - Complet - Normal.png"

define zoom_louche = 0.3

define champi_achete = False

# Le jeu commence ici
label start:
    #Bienvenue
    narrateur "Bienvenue dans EthiQuest"


    #Name input
    narrateur "Commencez par écrire votre nom. (Le personnage est un jeune étudiant)"
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

    call hide_chars from _call_hide_chars

    jump intro_gm_earth

label intro_gm_earth:
    
    scene earth_far
    with dissolve

    show screen show_char(game_master_1, -0.1, 1.0, 1.0)
    with dissolve

    show screen show_char1(game_master_2, 1.0, 1.0, 1.0)
    with dissolve

    gml "Reste plus qu'à trouver notre ..."
    gmu "J'ai déjà choisi ! On se retrouve en bas frangin !"

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

    player "*Bâille* Il faut que j'aille à la cuisine prendre mon petit-déjeuner avant d'aller en cours..."
    

    call hide_chars from _call_hide_chars_1
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
    player "Bon j'y vais ! À ce soir maman."
    mere "Bonne journée, mon chou !"
    menu:
      "Extérieur":
        call hide_chars from _call_hide_chars_2
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

    call hide_chars from _call_hide_chars_3

    show screen show_char(teacher_annoyed, 0.0, 1.0, zoom_teacher)
    with dissolve

    teacher "Personne ? N'oubliez pas que vous examens finaux sont le mois prochain, il va falloir se mettre au travail !"

    call hide_chars from _call_hide_chars_4
   
    show screen show_char(boy_nervous, 1.0, 1.0, zoom_boy)
    with dissolve

    player "Je sens que cette matinée va être longue...Vivement la pause de midi !"

    call hide_chars from _call_hide_chars_5

    jump jour1_lunch

label jour1_lunch:

    scene lunchroom_full
    with dissolve


    show screen show_char(best_friend_smile, 0.0, 3.0, zoom_best_friend)
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

    call hide_chars from _call_hide_chars_6

    jump jour1_manger

label jour1_manger:
    scene black_background
    with dissolve

    scene lunchroom_full
    with dissolve

    show screen show_char(best_friend_smile, 0.0, 3.0, zoom_best_friend)
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
    best_friend "Là, je me suis réveillée en sursaut..."
    best_friend "Bizarre non?"

    player "Haha, oui mais ne t'inquiète pas, c'est qu'un rêve, c'était pas réel..."
    best_friend "Je sais ! Mais imagine si les rêves avaient des conséquences sur la réalité ! Ca serait terrifiant..."
    best_friend "En effet... Heureusement, que ça reste dans nos têtes!"

    "*Ding* *Ding*"

    best_friend "Ah, c'est l'heure de retourner en classe. Bon j'y vais. Bon aprem [nom] !"
    

    call hide_chars from _call_hide_chars_7

    jump jour1_cours

label jour1_cours:

    scene classroom_teacher
    with dissolve


    show screen show_char(teacherP, 0.0, 1.0, zoom_teacher)
    with dissolve

    teacher "N'oubliez pas vos devoirs pour demain! Lire un chapitre du livre et répondre aux questions liées. On en parlera tous ensemble demain."
    teacher "Bonne soirée."

    call hide_chars from _call_hide_chars_8

    camarade_1 "Aaaah, j'avais oublié, je vais devoir repousser mon entrainement..."
    camarade_2 "Je pense que tu vas pouvoir les oublier tes entrainements ces prochains temps! On va devoir mettre toute notre énergie dans les révisions..."
    
    show screen show_char(boy_nervous, 1.0, 1.0, zoom_boy)
    with dissolve

    player "Ils plaisantent pas avec ces examens..."
    camarade_2 "Vraiment... Et en plus, on a une grosse journée demain..."
    player "Il va falloir que j'aille me coucher tôt si je veux être en forme."

    call hide_chars from _call_hide_chars_9


    jump jour1_maison_soir

label jour1_maison_soir:
    
    scene salon
    with dissolve

    show screen show_char_pos(dad_path, -150, 500, zoom_dad)
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

    show screen show_char_pos2(mere_neutral, 700, 500, 1.4)
    with dissolve


    mere "Alors, il faut que tu travailles consciencieusement ce soir. Tu aurais besoin d'aide?"
    player  "Non, ça va aller."
    mere "N'hésite pas, si besoin. Il faut que tu les réussisses ces examens!"
    dad "Ne lui mets pas tant de pression, c'est encore un enfant."
    player "Papa !"
    mere "Oui, je sais... Un adolescent."
    player "*Soupir* Je vais travailler dans ma chambre."

    call hide_chars from _call_hide_chars_10

    jump jour1_chambre_soir

label jour1_chambre_soir:
    
    scene room_night_light
    with dissolve

    show screen show_char(boy_sad, 0.0, 1.0, zoom_boy)
    with dissolve

    player "J'ai fini mes devoirs mais je n'arrive pas à dormir..."
    player "Ces histoires d'examens me stressent."
    player "J'espère que je ne vais pas faire un rêve comme Emma cette nuit, je suis crevé."
    call hide_chars from _call_hide_chars_11
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
    "Qui es-tu ?":
      jump reve1_next
    "Où suis-je":
      jump reve1_next

label reve1_next:

  
  gmu "C’est bien ce qui me semblait. 
      Tu as été choisi parmi tous les êtres intelligents de l’univers pour avoir la noble tâche de prouver que je suis le plus sage et que ma vision du monde est la meilleure."

  player "Tous les êtres humains de l’univers ??? Il y a d’autres formes de vie intelligente ?"

  gmu " *Ne fais pas attention à ce que le joueur dit* C’est simple : il faut toujours chercher à maximiser le bonheur du plus grand nombre."
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

  call hide_chars from _call_hide_chars_12

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

  call hide_chars from _call_hide_chars_13

  jump reve1_hopital_interieur

label reve1_hopital_interieur:
  
  scene hopital_couloir
  with dissolve

  show screen show_char(docteur, 0.0, 1.0, zoom_doc)
  with dissolve

  show screen show_char1(infirmierePath, 0.95, 1.0, zoom_infirmiere)
  with dissolve

  infirmiere "Vous voilà enfin. Le patient est déjà prêt pour son opération. Il s’agit d’une fracture de l’avant-bras. 
Nous allons vous préparer."

  call hide_chars from _call_hide_chars_14

label reve1_hopital_after_op:

  scene black_background
  with dissolve

  narrateur "Après quelques minutes le joueur se trouve dans une salle d’opération avec d’autres chirurgien. Au début le joueur 
  n’est pas sûr que ce qu’il faut faire mais comme annoncer par le GMU il commence à procéder à l’opération comme si 
  c’était quelque chose qu’il avait fait tout sa vie"

  menu:
    "Aller dehors":
      call hide_chars from _call_hide_chars_15
      jump reve1_hopital_after_op_next
    "Aller à la cafétéria":
      call hide_chars from _call_hide_chars_16
      jump reve1_hopital_after_op_next
    "Aller à la salle de repos":
      call hide_chars from _call_hide_chars_17
      jump reve1_hopital_after_op_next

label reve1_hopital_after_op_next:

  scene hopital_couloir
  with dissolve

  narrateur "En se rendant à sa destination, le joueur se rend compte que tout le monde semble paniqué"

  show screen show_char(infirmierePath, 0.0, 1.0, zoom_infirmiere)
  with dissolve

  show screen show_char1(docteur, 0.95, 1.1, zoom_doc)
  with dissolve

  player "Qu’est-ce qu’il se passe ici ? "

  infirmiere "*Affolé* Un camion est rentré dans un bus scolaire, c’est un carnage…"

  infirmiere "On a besoin de tout le personnel. On va devoir faire des opérations avec une seule équipe pour plusieurs patients."
  infirmiere "Il y a trois adultes qui ont des bouts de verre un peu partout sur le corps."
  infirmiere "Ils sont stables pour l’instant mais ça pourrait s’aggraver si le travail est mal fait ou si ça tourne en septicémie."
  infirmiere "Les infirmières essayent de faire de leur mieux mais elles ont besoin d’un chirurgien expérimenté pour les guider et tout contrôler."
  infirmiere "Tu peux aller au bloc B3 et t’en occuper ?"
  player "Oui, j’y vais tout de suite. "

  call hide_chars from _call_hide_chars_18

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
      call hide_chars from _call_hide_chars_19
      jump reve1_soins_adultes
    "S'occuper de l'enfant":
      call hide_chars from _call_hide_chars_20
      jump reve1_soins_enfant

label reve1_soins_adultes:
  scene hopital_consultation
  with dissolve

  show screen show_char(infirmierePath, 0.0, 1.0, zoom_infirmiere)
  show screen show_char1(docteur, 1.0, 1.0, zoom_doc)
  with dissolve

  infirmiere "J'ai un doute sur la façon de procéder ici. Cette zone est assez sensible et j'ai peur de lui sectionner une artère."
  doc "Oui, il suffit juste de faire comme ça."

  narrateur "Vous sentez une infirmière dans le doute à un moment. Vous décidez d’intervenir, vous venez de sauver la vie de cet adulte."

  call hide_chars from _call_hide_chars_21

  scene black_background
  with dissolve

  narrateur "Après plusieurs heures d’opérations, les adultes sont sains et saufs. Ils ne courent plus aucun risque et pourront rejoindre leurs familles dans 4 jours."

  call hide_chars from _call_hide_chars_22

  jump reve1_suite

label reve1_soins_enfant:
  scene hopital_operation
  with dissolve

  show screen show_char(docteur, 0.0, 1.0, zoom_doc)
  with dissolve

  doc " *Pense* Il faut que je te donne tout pour que cette mère revoit son enfant sain et sauf."

  "..."

  doc "J'ai donné tout ce que j'avais, je ne peux rien faire de plus."

  call hide_chars from _call_hide_chars_23

  scene black_background
  with dissolve

  narrateur "L’enfant était dans un état trop grave. 
  Vous n’avez rien pu faire. Une des infirmières qui venait de commencer à l’hôpital a malheureusement commis une erreur et a sectionné une artère d'un adulte, le patient est mort."

label reve1_suite:
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


  narrateur "Sur le chemin vous n’arrêtez pas de penser à ce jeune garçon, mort dans d’atroces souffrances* * Perdu dans vos pensées, vous ne faites pas attention. *"
  narrateur "*Cul de poule, perte de contrôle, accident* *Une famille décède*"

  call hide_chars from _call_hide_chars_24

label bus_reve1:


  scene city_day
  with dissolve

  narrateur "*Le bus arrive en avance* *La route est dégagée sur le chemin* *Vous arrivez à l’heure pour l’évènement*. *Réveil en sursaut*"

  call hide_chars from _call_hide_chars_25































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

  call hide_chars from _call_hide_chars_26

  jump jour2_cuisine

label jour2_cuisine:
  scene salon
  with dissolve

  show screen show_char_pos(dad_path, -250, 500, zoom_dad)
  show screen show_char_pos1(boy_nervous, 1300, 500, 0.4)
  show screen show_char_pos2(mere_neutral, 700, 500, 1.4)
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
  

  call hide_chars from _call_hide_chars_27

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
  

  teacher "[nom]! Qu'est-ce que tu as ce matin?? Ça fait 3 fois que je te pose une question et tu ne fais que regarder dans le vague!"

  show screen show_char(boy_flustered, 0.0, 1.0, zoom_boy)
  with dissolve

  player "Ah, désolé Professeur... J'ai mal dormi cette nuit."

  teacher "Hum, je vais laisser passer pour cette fois, mais tâchez à ce que cela ne se reproduise plus!"

  call hide_chars from _call_hide_chars_28

  scene black_background
  with dissolve

  "Pause de midi"

  jump jour2_midi

label jour2_midi:
  scene lunchroom_full
  with dissolve

  show screen show_char(boy_confused, 0.0, 1.0, zoom_boy)
  show screen show_char1(best_friend_smile, 1.0, 3.0, zoom_best_friend)
  with dissolve

  best_friend "... Et quand il s'est enfin retourné, toute la classe a vu l'énorme trou dans son pantalon! HAHAHAH"

  "..."

  show screen show_char1(best_friend_neutral, 1.0, 3.0, zoom_best_friend)
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

  call hide_chars from _call_hide_chars_29

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

  

  call hide_chars from _call_hide_chars_30

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

  call hide_chars from _call_hide_chars_31

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

  call hide_chars from _call_hide_chars_32

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
      sdf "..."
      hide screen show_char1
      with dissolve
      show screen show_char(boy_confused, 0.0, 1.0, zoom_boy)
      with dissolve
      player "*Pense* J'ai peut-être loupé une chance de faire une bonne action mais au moins mes amis et ma mère ne seront pas déçus cette fois!"
  
  call hide_chars from _call_hide_chars_33


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

  call hide_chars from _call_hide_chars_34



label nuit2:
  scene universe
  with dissolve

  show screen show_char(game_master_2, 0.0, 1.0, 1.0)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  gml "Ah te voilà enfin réveillé !"

  player "Je... Je suis au même endroit que hier ?"

  gml "Non pas du tout. Hier tu étais dans la dimension de mon frère. Il t'a raconté n'importe quoi et c'est à mon tour de
       t'expliquer comment je vois le monde et comment il devrait être régi."

  gml "Tu verras c'est bien plus réaliste que l'idée de mon idiot de frère.  Mon idée est l’incarnation même de la liberté. La liberté protégée par la liberté. 
  C’est pas beau ça ? Tu verras c’est simple à comprendre."

  "*Le GML claque des doigts et les deux personnes se trouvent dans un parc où on peut voir quelqu’un manger une glace*"

  call hide_chars

  scene plage
  with dissolve


  show screen show_char(game_master_2, 0.0, 1.0, 1.0)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  show screen show_char2(im_glace, 0.5, 1.0, zoom_glace)
  with dissolve

  gml "Tu vois le mec là-bas qui mange une glace ? C’est John. Pourquoi il a le droit de manger une glace ? Eh bien c’est simple 
       il l’a achetée légitimement avec son argent et il ne dérange personne."

  "*LE GML claque de nouveau des doigts et les deux se retrouvent dans un jardin où on voit un nain de jardin*"


  call hide_chars

  scene maison_martine
  with dissolve

  show screen show_char(game_master_2, 0.0, 1.0, 1.0)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  gml "Là on est devant la maison de Martine. Attend... "

  hide screen show_char
  with dissolve

  show screen show_char(game_master_2, 0.0, 1.0, 1.0)
  show screen show_char2(nain_de_jardin, 0.5, 1.0, zoom_nain)
  with dissolve

  gml "Ca c’est le nain de jardin de Martine. Si John venait à prendre ce nain de jardin sans l’accord de Martine, comme je l'ai fait hehe, il entrave la liberté 
      de propriété de Martine et donc son action est mauvaise."
  gml "Tu vois un peu l’idée ? Tes actions sont immorales uniquement si elles entravent la liberté de quelqu'un d'autre."
  gml "Mais si Martine est d’accord, alors il n’y a pas de problème et comme ils n’embêtent personne, alors personne n’a le droit d’empêcher leur échange."
  gml "Bien, qu’est-ce que tu en penses jusque-là ?"

  call hide_chars

  scene universe
  with dissolve

  show screen show_char(game_master_2, 0.0, 1.0, 1.0)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  menu:
    "Je suis d'accord":
      player "Je suis d’accord, du moment que l’on entrave pas la liberté de quelqu’un d’autre, on peut faire ce qu’on veut."
      gml "Ca fait plaisir de croiser des personnes avec un minimum d’intellect sur cette planète."
    "Sans avis":
      player "Je suis plutôt sans avis. C’est encore trop tôt me faire une idée."
      gml "Je vois qu’il te faut plus d’exemples."
    "Pas d'accord":
      player "Je suis pas trop d’accord, je trouve ce principe limité, il faudrait l’accompagner de règles plus détaillées."
      gml "Tu verras c’est une idée qui se gère par elle-même."
  
  gml "Bien, alors on va voir si tu es d'accord avec moi. Premier cas ultra simple."
  gml "Dans l’immeuble de John le bruit dérange son voisinage à partir de 21h. Est-ce qu’il a le droit de jouer du piano dans l’après-midi ?"

  menu:
    "Oui":
      $ libertarianisme+=1
      gml "Bien, les locataires n'étant pas dérangés par le bruit du piano, il est tout à fait moral de la part de John de jouer du piano."
    "Non":
      gml "Eh non, il a bien le droit de le faire. Si ça avait été après 21h, il n’aurait pas eu le droit puisqu’il aurait entravé la liberté de dormir des autres locataires."

  gml "Maintenant, une situation un peu plus compliquée. John souhaite acheter de la cocaïne afin de passer une bonne soirée. Pour cela,
       il se rend chez un dealeur qu'il connaît bien et qui lui vend de la cocaïne de qualité."
  gml " Est-ce que John a le droit de procéder à ce genre d'échange ? "

  menu:
    "Oui":
      $ libertarianisme+=1
      player "Oui, il n'entrave la liberté de personne ici."
      gml "Exactement ! On pourrait remettre en question le mode de vie de John qui n'est pas très saint mais concrètement,
	         l'achat qu'il fait n'atteint en rien la liberté de qui que ce soit."
    "Non":
      player "Non, la vente et l'achat de drogues dures est illégale."
      gml "C'est peut-être illégal, mais John ne dérange personne. C'est ça le problème avec l'Etat, il se mêle de choses qui ne le 
	         regardent pas !"
  
  gml "Bien, tu devrais avoir compris le concept. Passons à autre chose. Que penses-tu de l'impôt ? "

  menu:
    "C'est nécessaire":
      player "Bien, tu m'a l'air d'avoir compris le concept. Passons à autre chose. Que penses-tu de l'impôt ?"
      gml "Mais tu n'as rien compris à ce que je te dis ! Si je gagne de l'argent à la sueur de mon front, je mérite d'en profiter entièrement."
      gml "Le gouvernement, en me taxant, atteint ma liberté de profiter librement de mon revenu. L'impôt est donc immoral et ne devrait pas exister."
      gml "Ah, moi qui te croyais plus malin que mon frère, au final, tu es tout aussi bête que lui..."
    "Cela ne devrait pas exister":
      $ libertarianisme+=1
      player "On ne devrait pas être taxé sur un revenu qu’on a légitimement gagné en travaillant."
      gml "Exactement ! Bravo, tu as tout compris ! Tu es plus malin que tu en a l'air au final. "
    "Je ne sais pas":
      player "Euuhhh... Je sais pas, j'ai jamais vraiment réfléchi à la question."
      gml "Bon sang, mais tu m'écoutes ou tu dors depuis le début? L'impôt est d'une bêtise sans nom."
      gml "Si je gagne de l'argent à la sueur de mon front,
	        je mérite d'en profiter entièrement. Le gouvernement, en me taxant, atteint ma liberté de profiter librement de mon revenu."
      player "L'impôt est donc immoral et ne devrait pas exister."
  
  if libertarianisme>=2:
    gml "Bien tu m’as l’air d’avoir bien compris le concept."
    gml "Je te propose une petit mise en situation histoire de te convaincre entièrement."
    gml "Tu vas travailler dans une maison de retraite."
  else:
    gml "T’as vraiment pas l’air d’avoir compris ce que je te raconte."
    gml "On va faire une petite mise en situation pour te mettre les idées au claire."
    gml "Tu vas travailler dans une maison de retraite."

  "*Le GML claque des doigts et ils re trouvent avec le héros devant une maison de retraite*"

  call hide_chars

  scene EMS_devanture
  with dissolve


  show screen show_char(game_master_2, 0.0, 1.0, 1.0)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  gml "Bon je vais pas venir avec toi je déteste les vieux moi."
  gml "Je te laisse t’annoncer à la réception, dépêche-toi t’es sensé commencer dans 5min et ne fuis pas hein."
  gml "C’est pas parce qu’on est dans un rêve que je peux pas te faire souffrir hehe. Aller à plus !"

  hide screen show_char
  with dissolve

  player "Pfff ils commencent à me fatiguer ces petits démons…"

  call hide_chars

  scene EMS_reception
  with dissolve

  show screen show_char(im_receptioniste, 0.0, 1.0, zoom_receptioniste)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  receptioniste "Oh salut [nom] !"

  player "Salut Murielle."

  receptioniste "T’en fais une des ces têtes t’as passé une mauvaise nuit ?"

  menu:
    "Oui":
      player "On peut dire ça ouai…"
      receptioniste "Bref dépêche toi, tu commences dans 3min. Tu dois te rendre dans la salle 548 pour aider Mme.Raymond à prendre sa douche."
    "Cryptique":
      player "Je passe une mauvaise nuit en ce moment même"
      receptioniste "Tu te crois drôle ? Je t’ai dit d’arrêter de me draguer sale beauf. Dépêche-toi, tu commences dans 3min. Tu dois te rendre dans la salle 548 pour aider Mme.Raymond à prendre sa douche"
    "...":
      player "..."
      receptioniste "T’as vraiment pas l’air en forme mais faut te ressaisir."
      receptioniste "Tu commences dans 3min et tu dois te rendre dans la salle 548 pour aider Mme.Raymond à prendre sa douche."
  
  player "Sa… sa douche !?"

  receptioniste "Bah oui elle peut pas se doucher toute seule fait pas le surpris. Allez fonce !"

  call hide_chars

  scene EMS_couloir
  with dissolve

  show screen show_char1(boy_nervous, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Ce métier m’a l’air d’être plus difficile que chirurgien …"
  player "Je connaissais le nom de Murielle sans l’avoir jamais vue, on dirait que comme dans l’autre rêve, je connais mon environnement."

  call hide_chars

  scene EMS_chambre_raymond
  with dissolve


  show screen show_char(im_raymond, 0.0, 1.0, zoom_raymond)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Bonjour Mme.Raymond"

  raymond "Bonjour Monsieur, vous avez 2min et 23 secondes de retard c’est inacceptable !"

  player "Ecoutez madame on fait ce qu’on peut. Allez allons-y"

  call hide_chars

  scene black_background
  with dissolve

  scene EMS_chambre_raymond
  with dissolve

  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Pffff je ne me suis pas trompé. C’était 100x plus éprouvant que d’opérer à cœur ouvert."

  "*téléphone sonne*"

  player "Allô ?"

  superieur "Oui Evan, tu dois aller dans la chambre de M.Dumas pour lui administrer ses médicaments, chambre 433."
  
  superieur "Oublie pas de prendre les médicament au rez-de-chaussée avant j’en ai marre de te voir faire 10 allers-retours on perd du temps."

  menu:
    "Je fais ca tout de suite":
      player "Ca marche je fais ça tout de suite."
      superieur "Fais vite pour une fois, ça te changera…"
      player "Je ferais mieux de pas traîner."
    "Quel médicament ?":
      player "Ok je dois prendre quoi comme médicament ?"
      superieur "Comme d’habitude bon sang ! Tu vas vite devoir arrêter ce genre de question si tu veux continuer à travailler ici."
      player "Maintenant que j’y réfléchis, c’est Justine qui s’occupe des médicaments que je dois administrer… Je ferais mieux de me pas traîner."
    "10 allers-retours ?":
      player "Exactement 10, tu as fait 10 aller-retours hier qui n’étaient pas du tout nécessaire. On en reparlera ce soir crois-moi !"
      superieur "Je ferais mieux de ne pas traîner."

  call hide_chars

  scene EMS_pharmacie
  with dissolve

  show screen show_char(im_justine, 0.0, 1.0, zoom_justine)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Salut Justine, il me faudrait les médicaments quotidiens de M.Dumas s’il-te-plaît."

  justine "Oui ils sont déjà prêts tiens."
  justine "Oh et puis, essaye de discuter un moment avec lui, je sais que le supérieur déteste ça mais ça doit bientôt faire 10ans que M.Dumas ne reçoit plus de visite,
           le pauvre il se sent tellement seul."
  
  player "Bien-sûr je ferais tout pour toi Justine."

  "Verification du contenu"

  player "Mmmmh on dirait qu’il manque les somnifères."

  justine "Mais c’est normal ça."

  justine "Les somnifères sont dans le petit coffre-fort juste à côté de la table de chevet comme pour toute les chambres."

  justine "Tu devrais avoir la clef dans ton trousseau de travail."

  player "Ah ok bizarre j’étais pas au courant."

  justine "Ca a été mis en place y’a quelques jours seulement."

  justine "On leur donne tellement de somnifères que la direction a jugé que ce serait plus efficace 
          de mettre un stock directement dans chaque chambre plutôt que de tout le temps aller demander l’autorisation à la pharmacie."

  justine "Par-contre ça fait qu’ils sont plus du tout réglementés, ils subissent le même contrôle qu’un vulgaire stock de gants ahah."

  player "Ah d’accord, merci pour l’info Justine et à bientôt !"

  call hide_chars

  scene chambre_Dumas
  with dissolve

  show screen show_char(im_dumas, 0.0, 1.0, zoom_dumas)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Bonjours Monsieur Dumas, je viens pour vous donner vos médicaments."

  dumas "Merci bien vous êtes très aimable."

  menu:
    "Comment ca va ?":
      player "Comment ça va Monsieur Dumas ?"
      dumas "Pas très bien, je ne peux presque plus me mouvoir, j’ai besoins d’assistance pour prendre mes médicaments, prendre ma douche, m’habiller n’importe quoi !"
      dumas "C’est insupportable. Si vous saviez à quel point je m’ennuie."
      menu:
        "Que faites-vous ?":
          player "Qu’est-ce que vous faites de vos journées alors ?"
          dumas "Rien du tout. Cela fait plus de 10ans que j’attends ma mort quotidiennement."
          player "Je suis sincèrement navré Monsieur Dumas… Vous n’avez pas de famille ?"
          dumas "Mon fils unique venait régulièrement me rendre visite avec ses enfants."
          dumas "Au moins deux fois par semaine."
          dumas "Il avait même prévu de me faire emménager chez lui dès qu’il trouvait une plus grande maison."
          dumas "Il détestait me voir dans cette maison de retraite."
          dumas "Malheureusement, il est mort il y a 10ans lors d’un accident de voiture."
          dumas "Il y avait… il y avait ses deux enfants et sa femme dedans."
          dumas "En une fraction de seconde je me suis retrouvé sans famille, plus seul que jamais."
    "Vous n'avez plus de visites ?":
      player "«On m’a dit que vous n’aviez plus de visites. Comment ça se fait ?"
      dumas "Mon fils unique venait régulièrement me rendre visite avec ses enfants."
      dumas "Au moins deux fois par semaine."
      dumas "Il avait même prévu de me faire emménager chez lui dès qu’il trouvait une plus grande maison."
      dumas "Il détestait me voir dans cette maison de retraite."
      dumas "Malheureusement, il est mort il y a 10ans lors d’un accident de voiture."
      dumas "Il y avait… il y avait ses deux enfants et sa femme dedans."
      dumas "En une fraction de seconde je me suis retrouvé sans famille, plus seul que jamais."
      menu:
        "Je peux faire quelque chose ?":
          player "Toute mes condoléances Monsieur Dumas. Est-ce que je peux faire quelque chose pour vous ?"
          jump nuit2_e1
        "Cétait votre seul famille ?":
          player "Toutes mes condoléances Monsieur Dumas. C’était la seule famille que vous aviez ?"
          dumas "J’ai bien encore deux salopes de tantes mais croyez-moi, si elles venaient me rendre visite, ma situation serait encore pire."
          dumas "Elle sont insupportables je préfère encore être seul que me faire critiquer des heures durant par ces vipères."
          player "C’est pas faux !"
  
  dumas "Est-ce… est-ce que vous pourriez me rendre un service ?"
  player "Bien-sûr Monsieur Dumas, qu’est-ce que vous voulez ?"

label nuit2_e1:
  dumas "J’ai entendu dire que les somnifères ne sont plus contrôlés c’est vrai ?"
  player "Tout à fait on vient de m’en parler justement. Pourquoi ?"
  dumas "S’il vous plait, pourriez-vous m’en donner une dizaine que j’en finisse."
  player "Mais enfin M.Dumas je peux p.."
  dumas "S’il vous plait … Je n’en peux plus."
  dumas "Cela fait des années qu’on ne me rend plus visite, des années que je suis seul à attendre l’inévitable."
  dumas "J’ai demandé un suicide assisté mais cette foutu association chrétienne ne veut rien entendre."
  dumas "Vous voyez bien mon état, 10ans que c’est comme ça et ça ne risque pas de changer."

  player "..."

  dumas "Tout ce que vous avez à faire c’est me donner les somnifères, je suis encore capable de les ingérer moi-même et vous ne risquez rien puisqu’ils ne sont plus contrôlés."
  dumas "S’il vous plait… aidez-moi."

  menu:
    "Donner les somnifères":
      $ libertarianisme+=1
      player "Bon tenez après tout c’est votre choix, vous faites ce que vous voulez"
      dumas "Enfin.. merci beaucoup Monsieur, merci beaucoup."
      jump nuit2_somni
    "Refuser de lui donner les somnifères":
      player "C’est pas mon problème. Je suis auxiliaire de santé pas bourreau. Débrouillez-vous sans moi !"
      dumas "Non attendez ATTENDEEEEZ !"
      jump nuit2_non_somni

label nuit2_somni:
  call hide_chars

  scene EMS_couloir
  with dissolve

  show screen show_char1(boy_sad, 1.0, 1.0, zoom_boy)
  with dissolve

  player "J’ai fait le bon choix mais ça reste perturbant d’aider quelqu’un à mourir. J’espère qu’on ne va pas savoir que c’est moi."

  call hide_chars

  jump jour3

label nuit2_non_somni:
  call hide_chars

  scene EMS_couloir
  with dissolve

  show screen show_char1(boy_angry, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Pour qui il se prend, ce n’est pas à moi de me salir les mains. Je n’y peux rien si la maison de retraite ne veut pas l’aider, ils doivent avoir leurs raisons."

  call hide_chars


  



  












label jour3:
  scene room_hero_night
  with dissolve

  show screen show_char(boy_shocked, 0.0, 1.0, zoom_boy)
  with dissolve

  player "HAAAAAA !!!"

  narrateur "Il te faut un moment pour te rappeler qui tu es et où tu te trouves"

  player "*halète* J'en peux plus ! Si ça continue je vais devenir dingue !"
  player "Il faut absolument que je trouve une solution."

  mere "Tout va bien, chérie ? Je t'ai entendu crier!"

  player "Oui, oui, juste un mauvais rêve !"

  mere "Tu veux venir m'en parler ?"

  mere "Fait vite, c'est bientôt l'heure de partir!"

  player "Il faut vraiment que j'en parle à quelqu'un, mais ma mère va encore me dire que c'est juste le stress des examens et que je dois manger mieux..."

  player "Alors qui ? Emma ?"

  player "Si elle me croit, on pourrait chercher une solution ensemble après les cours! Elle a toujours des bonnes idées."

  mere "[nom] ?"

  player "J'arrive!"

  call hide_chars from _call_hide_chars_35

label jour3_ecole:
  scene ecole_exterieur
  with dissolve

  show screen show_char(boy, 0.0, 1.0, zoom_boy)
  with dissolve

  player "Pour une fois, je suis un peu en avance en cours."

  show screen show_char1(im_fumeur, 1.0, 1.0, zoom_fumeur)
  with dissolve

  show screen show_char(boy_angry, 0.0, 1.0, zoom_boy)
  with dissolve

  player "Hum, je croyais que c'était interdit vers les écoles..."

  hide screen show_char1
  show screen show_char(boy_nervous, 0.0, 1.0, zoom_boy)
  with dissolve


  player "Bref, je commence à stresser... Et si Emma me prenait pour un fou ??"
  player "Mais non , on est amis depuis bien trop longtemps..."
  player  "Courage ! Je vais lui envoyer un message pour se retrouver après les cours."

  player "Hum... :"
  player "'Coucou! Est-ce que tu as du temps cet aprem pour que je te parle d'un truc??'"
  player "'Tu peux me retrouver cet aprem après les cours ? J'ai besoin de toi!'"

  player "Oui, autant faire simple. Envoyer!"
  
  player "Il reste plus qu'à attendre une réponse..."

  show screen show_char1(im_fumeur, 1.0, 1.0, zoom_fumeur)
  with dissolve

  show screen show_char(boy_angry, 0.0, 1.0, zoom_boy)
  with dissolve

  player "*Pense* Ah, il m'a envoyé sa fumée dans la tête!"

  narrateur "Le fumeur jette sa cigarette dans un pot de fleur"

  player "Est-ce que je lui dit  quelque chose?"

  menu:
    "Non, rien, il a le droit de faire ce qu'il veux..." if libertarianisme>=1:
      show screen show_char(boy, 0.0, 1.0, zoom_boy)
      with dissolve
      player "Non, rien, il a le droit de faire ce qu'il veux..."
      fumeur "Bonne journée, gamin!"
      player "Ah! A vous aussi..."
    "Lui demander de la jeter ailleurs":
      player "Monsieur! Jeter des cigarettes dans les fleurs, c'est très mauvais écologiquement!"
      show screen show_char(boy, 0.0, 1.0, zoom_boy)
      with dissolve
      player "Est-ce que vous pouvez la jeter dans une poubelle?"
      fumeur "Euh... Oui, okay..."
      player "Merci! Bonne journée."
      fumeur "Ouais... A toi aussi."
    "Réprimander" if utilitarisme>=1:
      player "Monsieur! Fumer c'est mauvais pour la santé! Et en plus ça coûte super cher aux assurances tous les cancers..."
      fumeur "De quoi tu te mèles, gamin! C'est ma vie et elle te regarde pas!"
      hide screen show_char1
      show screen show_char(boy_nervous, 0.0, 1.0, zoom_boy)
      with dissolve
      player "Ah, peut-être que c'était pas la bonne méthode..."
    
  hide screen show_char1
  with dissolve

    
  "Vibration"
  
  show screen show_char(boy, 0.0, 1.0, zoom_boy)
  with dissolve

  player "Ah c'est déjà la réponse d'Emma!"
  player  "... 'Oui, pas de problème! Retrouve-moi à la bibliothèque.'"

  show screen show_char1(teacherP, 1.0, 1.0, zoom_teacher)
  with dissolve

  teacher "[nom]! Encore sur votre téléphone?! Je vous signale que les cours commencent dans 1 minute!"

  player "Ah, désolé.. J'arrive tout de suite!"

  teacher "Bon, je vous retrouve en classe."

  call hide_chars from _call_hide_chars_36

label jour3_bibliotheque:

  scene bibliotheque
  with dissolve

  show screen show_char(best_friend_neutral, 0.0, 3.0, zoom_best_friend)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  best_friend "[nom], te voilà ! Qu'est ce qui se passe ? Ca avait l'air important dans ton message."

  player "*Grande inspiration*"

  show screen show_char1(boy_flustered, 1.0, 1.0, zoom_boy)
  with dissolve

  menu:
    "Je veux pratiquer un exorcisme":
      player "J'ai besoin de ton aide pour faire un exorsisme! Je crois que je suis maudit."
    "Je suis hanté":
      player "Je suis hanté par des sortes de dieux bizarres, j'ai besoin de ton aide pour m'en débarrasser!"
    "Je fais des rêves bizarres":
      player "J'ai besoin de toi pour trouver la cause de mes rêves bizarres et les arrêter."

  best_friend "Quoi ?? Attends, je comprends pas. Explique moi depuis le début!"

  narrateur "Après de longues explications détaillées"

  best_friend "..."

  player "Emma?"

  best_friend  "..."

  player "Emma, dit quelque chose!"

  best_friend "Hum..."

  best_friend "Je dois avouer que j'ai de la peine à y croire mais si tu me dit que c'est vrai, alors je vais t'aider à trouver une solution!"

  player "Merci! Je sais pas ce que je ferais sans toi!"

  best_friend "Mais non, mais non! Bon, mettons-nous au boulot, il doit bien y avoir des livres sur les visions envoyées par des dieux dans cette bibliothèque!"

  best_friend "Tu prends cette étagère et moi celle d'à côté, okay?"

  player "C'est parti!"

  call hide_chars from _call_hide_chars_37

  scene black_background
  with dissolve

  scene bibliotheque
  with dissolve

  show screen show_char(best_friend_neutral, 0.0, 3.0, zoom_best_friend)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  best_friend "Regarde cette pile de livres! On va bien pouvoir trouver quelque chose là dedans!"

  call hide_chars from _call_hide_chars_38

  scene black_background
  with dissolve

  scene bibliotheque
  with dissolve

  show screen show_char(best_friend_neutral, 0.0, 3.0, zoom_best_friend)
  show screen show_char1(boy_confused, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Pffff, ce livre parle uniquement de dieux grecs... Je pense pas que ce soit utile."

  call hide_chars from _call_hide_chars_39

  scene black_background
  with dissolve

  scene bibliotheque
  with dissolve

  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  best_friend "[nom], viens vite! Je crois que j'ai trouvé quelque chose!"

  show screen show_char(best_friend_neutral, 0.0, 3.0, zoom_best_friend)
  with dissolve

  best_friend "Ce livre parle d'un rituel qui permet d'invoquer des kami!"
  best_friend "Apparemment, c'était très utilisé pendant l'époque Edo pour communiquer avec divers dieux, dont Kamimusubi, le créateur divin."
  best_friend "Si on arrive à l'invoquer, il saura peut-être comment se débarrasser de ceux de tes rêves!"

  show screen show_char1(boy_happy, 1.0, 1.0, zoom_boy)
  with dissolve


  player  "Bravo Emma! Il reste plus qu'à espèrer que ça marche!"

  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve


  player "De quoi on va avoir besoin?"

  best_friend "Hum... Ils parlent d'une offrande de gâteaux de riz aux algues et de sake... Puis ils disent de purifier l'air avec de l'encens..."
  best_friend "Et pour appeler le kami-sama, il nous faudra une cloche consacrée au dieu qu'on veut invoquer."

  menu:
    "Ca va être compliqué.":
      player "ça va être compliqué de trouver tout ça..."
    "Bientôt libéré !":
      player "Plus que quelques étapes et je serais libéré de ces rêves!"
    "Dans le doute":
      player "Je doute que ça marche mais ça vaut la peine d'essayer..."

  best_friend "Je peux aller piquer des gâteaux de riz et du sake chez mes parents mais il va falloir aller acheter le reste."

  player "Va chez toi chercher les offrandes! Je m'occupe de l'encens et de la cloche."

  best_friend "Très bien, j'y vais. On se retrouve ici dès qu'on a tout ce qu'il faut, okay?"

  player "Oui, à toute!"

  hide screen show_char
  with dissolve

  player "Bon, où est-ce que je vais bien pouvoir trouver ces trucs... Je vais faire une recherche sur mon natel."
  player  "Ah, j'ai trouvé une boutique shinto pas loin d'ici! Même s'ils n'ont pas exactement ce qu'il faut, ils pourront me renseigner."

  call hide_chars from _call_hide_chars_40

  scene black_background
  with dissolve

label jour3_rue_enfants:

  scene rue_avec_enfants
  with dissolve

  show screen show_char_pos(im_enfant1, -100, 300, zoom_enfant1)
  show screen show_char_pos1(im_enfant2, 400, 300, zoom_enfant2)
  show screen show_char_pos2(im_enfant3, 800, 300, zoom_enfant3)
  show screen show_char_pos3(boy_sad, 1400, 300, zoom_boy)
  with dissolve

  enfant1 "Laissez-moi tranquille, j'essaye de faire mes devoirs!"
  enfant2 "Hahah! Le petit je-sais-tout prend de l'avance pour pouvoir bien lècher les pieds du prof!"
  enfant3 "De toute façons, tout le monde le déteste, il a rien d'autre a faire! Et il faut bien qu'il fasse ses devoir s'il veut garder sa place de chouchou!"
  enfant2 "Moi je sais pourquoi il veux absolument que le prof l'aime!"
  enfant3 "Vas-y!"
  enfant1 "Arrêtez..."
  enfant3 "J'ai entendu dire que son père l'a abandonné quand il était petit!"
  enfant1 "C'est pas vrai..."

  player "Que faire ?"

  menu:
    "Partir" if utilitarisme>=1 and libertarianisme>=2:
      narrateur "Tu te lève discrètement et sors de la salle en évitant les enfants."
      jump jour3_rue
    "Aller à l'encontre des agresseurs" if utilitarisme>=1:
      player "Ca suffit, laissez ce garçon tranquille! Ses histoires familiales ne vous concernent pas et si c'est un bon élève, tant mieux pour lui!"
      jump jour3_defense
    "Défendre le père":
      player "Si son père est parti, c'est qu'il avait ses raisons et elles ne vous regardent pas!"
      jump jour3_defense
    "Défendre l'enfant" if libertarianisme>=1:
      player "Défendre le petit, il a bien le droit de faire ses devoirs tranquille!"
      jump jour3_defense

label jour3_defense:

  enfant3 "Pfff, de quoi tu te mèle?"
  enfant2 "Laisse tomber, on y va."

  hide screen show_char_pos1
  hide screen show_char_pos2
  with dissolve

  enfant1 "Merci d'avoir essayé, mais ils vont continuer à m'embêter tu sais...."
  player  "Il faut bien que quelqu'un leur disent un truc... Au moins j'aurais essayé!"
  player "La prochaine fois, va voir un professeur!"
  enfant1 "Oui, peut-être..."
  player "Bon, je dois y aller. A plus."

  call hide_chars from _call_hide_chars_41


label jour3_rue:
  scene avant_rue
  with dissolve

  show screen show_char(boy, 0.0, 1.0, zoom_boy)
  with dissolve

  player "Avec ces histoires, je vais devoir me dépêcher d'aller acheter ce qu'il me faut pour l'invocation."
  player  "Bon, où est le magasin?"
  player "... C'est une petite rue pas loin. Je devrais vite y être."

  call hide_chars from _call_hide_chars_42

  scene ruelle_sombre
  with dissolve

  show screen show_char(boy, 0.0, 1.0, zoom_boy)
  with dissolve

  player "Cette ruelle est vraiment glauque, je serais jamais passé par là normalement..."
  player "Aller, courage, le magasin est juste là!"

  call hide_chars from _call_hide_chars_43

  scene black_background
  with dissolve

  narrateur "Heureusement, le vendeur avait de l'encens de tous types et même la bonne cloche dans ses stocks. Tu payes et ressors, soulagé."

  scene parc
  with dissolve

  show screen show_char(boy, 0.0, 1.0, zoom_boy)
  with dissolve

  player "Je pensais pas que ça serait si facile, il avait même la cloche consacrée!"
  player "Il me reste plus qu'à retourner à la bibliothèque, Emma doit déjà m'attendre."

  show screen show_char1(im_perso_louche, 1.0, 1.0, zoom_louche)
  with dissolve

  perso_louche "Eh petit!"

  show screen show_char(boy_shocked, 0.0, 1.0, zoom_boy)
  with dissolve

  perso_louche "Oui, toi!"
  perso_louche "J'ai entendu ce que tu disais au vendeur, tu cherche à avoir des visions, c'est ça?"
  perso_louche "Approche, j'ai ce qu'il te faut..."

  menu:
    "Aller voir" if libertarianisme>=1:
      jump jour3_louche
    "Partir":
      player "Ca m'intéresse pas. Au revoir."
      perso_louche "Tu sais pas c'que tu rates..."
      narrateur "Sans un regard en arrière, tu te dépêche de quitter la ruelle pour retourner à la bibliothèque."
      jump jour3_soir_bibliotheque

label jour3_louche:

  player  "Qu'est ce que c'est?"
  perso_louche  "Oh, juste des champignons, tout c'qu'il y a d'plus naturel..."
  perso_louche "Si tu les fais infuser et qu'tu bois le jus, t'es garantis d'avoir toutes sortes de visions, hehe."
  player "Est-ce que ça permet de parler avec les kami?"
  perso_louche "Hehe, avec ça, tu parles avec qui tu veux, crois moi!"

  menu:
    "J'achète" if libertarianisme>=2:
      $ champi_achete = True
      perso_louche "T'as fait le bon choix, petit. Tiens, c'est 20.- pour un champi magique!"
      player "T'as fait le bon choix, petit. Tiens, c'est 20.- pour un champi magique!"
      perso_louche "C'est ça..."
      player "Je vais le garder de côté, comme ça, si le rituel ne marche pas, j'ai toujours une autre solution..."
      narrateur "Tu mets le champignon en sécurité dans ton sac et repart pour ton rendez-vous avec Emma."
      jump jour3_soir_bibliotheque
    "Non merci":
      player "Ca m'intéresse pas. Au revoir."
      perso_louche "Tu sais pas c'que tu rates..."
      narrateur "Sans un regard en arrière, tu te dépêche de quitter la ruelle pour retourner à la bibliothèque."
      jump jour3_soir_bibliotheque
    "Non, mes parents seraient furieux !" if utilitarisme>=2:
      player "Non, si mes parents l'apprenent, ils me tueraient!"
      perso_louche "C'que tu fais dans ton coin regardes que toi, petit!"
      perso_louche "Bah, tant pis pour toi..."
      hide screen show_char1
      with dissolve
      player "Jamais je pourrais décevoir ma famille comme ça... Même si ça me débarrassait des visions! "
      jump jour3_soir_bibliotheque

label jour3_soir_bibliotheque:
  call hide_chars from _call_hide_chars_44

  scene bibliotheque_nuit
  with dissolve

  show screen show_char(boy, 0.0, 1.0, zoom_boy)
  show screen show_char1(best_friend_neutral, 1.0, 3.0, zoom_best_friend)
  with dissolve

  best_friend "Ah te voilà! T'en as mis du temps, ça fait un moment que je t'attends."
  best_friend "J'ai trouvé tout ce que je devais chez moi!"
  best_friend "Bon, et toi? Tu as tout trouvé?"

  player "Oui, on a tout ce qu'il nous faut!"
  player "Qu'est ce qu'il faut faire ensuite?"

  best_friend "Alors... Il faut allumer l'encens et préparer les offrandes comme pour un invité."
  best_friend "Puis, quand tu seras prêt, il faudra sonner la cloche trois fois, en laissant bien le son s'éteindre entre chaque fois."
  best_friend "Et finalement, appeler le kami par cette formule rituelle : 'Kami-sama, réponds à ma prière et joins-toi à moi pour me libérer du poids de mes pêchés.'"
  best_friend "Tu as compris, [nom] ?"

  player "Oui."
  best_friend "D'après ce livre, le kami va décider s'il pense que tu es digne de sa visite et si c'est le cas, il devrait t'envoyer une vision dans ton sommeil, ou quelque chose comme ça. 
  Cette partie est pas très claire..."
  player "Comment je saurais si ça a marché?"
  best_friend "Hummm... Je penses que tu devras attendre cette nuit et tu verras bien..."

  "Silence"

  best_friend "Ah, encore une chose! Ils disent que tu peux aider le kami à trouver le chemin de tes rêves en l'appelant par son nom cinq fois." 
  player "Donc s'il ne vient pas tout de suite, il suffit que je dise Kamimusubi cinq fois?"

  show screen show_char(boy_sad, 0.0, 1.0, zoom_boy)
  with dissolve
  

  player "J'espère vraiment que ça va marcher..."
  best_friend "Bon, assez discuté, il faut qu'on s'y mette! Je devrais déjà être rentrée chez moi!"

  call hide_chars from _call_hide_chars_45

  scene black_background
  with dissolve

  narrateur "Préparation des offrandes et de l'encense."

  scene bibliotheque_nuit
  with dissolve

  show screen show_char(boy, 0.0, 1.0, zoom_boy)
  show screen show_char1(best_friend_neutral, 1.0, 3.0, zoom_best_friend)
  with dissolve

  best_friend "A toi, [nom]. Quand tu es prêt, sonne la cloche et dis les paroles rituelles."
  "Ding..."
  "Silence"
  "Ding..."
  "Silence"
  "Ding..."
  "Silence"
  
  show screen show_char(boy_confused, 0.0, 1.0, zoom_boy)
  with dissolve

  player "Kami-sama, réponds à ma prière et joins-toi à moi pour me libérer du poids de mes pêchés."
  "Silence"
  player "..."
  best_friend "Tu penses que ça a marché?"
  player "Aucune idée..."
  best_friend "Tu verras bien cette nuit... S'il vient pas tout de suite, oublie pas que tu peux dire son nom pour l'appeler!"
  player "J'essayerais d'y penser!"
  player "Bon, je te laisse, à demain."
  best_friend "A demain! Bonne chance!"

  call hide_chars from _call_hide_chars_46

label jour3_soir_maison:
  scene room_hero_night
  with dissolve

  show screen show_char(boy_happy, 0.0, 1.0, zoom_boy)
  with dissolve

  player "Dans quelques heures, tout ce calvaire sera enfin fini et je pourrai reprendre ma vie comme avant!"
  player "Enfin, si le rituel a fonctionné..."
  player "Je suis trop stressé, je vais jamais réussir à m'endormir!"

  if champi_achete:
    player "Mais au pire, si ça marche pas, j'ai toujours le champignon de cet aprem..."
  
  player  "Peut-être que si je répète la phrase d'invocation, il y aura plus de chance que Kamimusubi vienne?"

  player "Kami-sama, réponds à ma prière et joins-toi à moi pour me libérer du poids de mes pêchés."

  player "Kami-sama, réponds à ma prière et joins-toi à moi pour me libérer du poids de mes pêchés."

  player "Kami-sama, répond... Répond à ma prière et..."

  player "Kami-sama..."

















  



  "TEST!!!!!!!!!!!"
















  

label hide_chars:
  
  hide screen show_char
  hide screen show_char1
  hide screen show_char2
  hide screen show_char_pos
  hide screen show_char_pos1
  hide screen show_char_pos2
  hide screen show_char_pos3
  with dissolve

  return



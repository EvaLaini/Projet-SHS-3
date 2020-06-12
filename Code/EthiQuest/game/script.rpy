# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.

# Narrateur
define narrateur = Character('Narrateur', color="#ebac34")

screen show_char(path, alignX, alignY, zoomV):
  tag show_char
  add path xalign alignX yalign alignY zoom zoomV

screen show_char1(path, alignX, alignY, zoomV):
  tag show_char1
  add path xalign alignX yalign alignY zoom zoomV

screen show_char2(path, alignX, alignY, zoomV):
  tag show_char2
  add path xalign alignX yalign alignY zoom zoomV

screen show_char3(path, alignX, alignY, zoomV):
  tag show_char3
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
define player = Character("[nom]", color="#f9e571", image="boy")

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
define best_friend = Character("Emma", color="#e382fd", image="best_friend")
define best_friend_neutral = "Perso/amie/amie_neutral.png"
define best_friend_angry = "Perso/amie/amie_angry.png"
define best_friend_annoyed = "Perso/amie/amie_gene.png"
define best_friend_sad = "Perso/amie/amie_sad.png"
define best_friend_smile = "Perso/amie/amie_happy.png"
define best_friend_reading = "Perso/amie/amie_lecture.png"

define zoom_best_friend = 0.6
#========================================================================================

#Mere ========================================================================================
define mere = Character("Maman", color="#6255b4", image="mere")
define mere_neutral = "Perso/mere/mere_bienveillante.png"
define mere_angry = "Perso/mere/mere_colere.png"
define mere_happy = "Perso/mere/mere_rire.png"
define mere_sad = "Perso/mere/mere_sad.png"
define mere_surprised = "Perso/mere/mere_surprised.png"
define zoom_mom = 1.4
# ========================================================================================

#Professeur =========================================================================
define teacher = Character("Professeur", color="#963e20", image="teacher")
define teacherP = "Perso/professeur/professeur_talking.png"
define teacher_annoyed = "Perso/professeur/professeur_angry.png"

define zoom_teacher = 0.3
#=====================================================================================

#GM =========================================================================
define gmu = Character('Shiawase', color="#88aedb", image = "game_master_1")
define game_master_1 = "Perso/gm1/GM1_1.png"

define gml = Character("Jiyu", color="#c7f9f2")
define game_master_2 = "Perso/gm2/GM2_1.png"

# =========================================================================

#Docteur perso =========================================================================
define doc = Character("[nom]", color="#f9e571")
define docteur = "Perso/docteur/Dr_noname.png"

define zoom_doc = 0.4
# ======================================================================================

#Camarade =========================================================================
define camarade_1 = Character("Camarade sportif", color="#32a852")
define camarade_2 = Character("Camarade studieux", color="#81ec9e")
#======================================================================================

#Infirmiere ======================================================================================
define infirmiere = Character("Infirmier", color="#85ce25")
define infirmierePath = "Perso/infirmiere/infirmier.png"
define zoom_infirmiere = 1.0
#======================================================================================


#SDF
define sdf = Character("SDF", color="#54d0ff")

define sdf_normal = "Jour2/SDF/SDF.png"
define zoom_sdf = 1.2


define mere_enfant = Character("Mère affolée", color="#eca781")

define mere_enfant_im = "Soir1/mere/coral_sad.png"

define zoom_mere_enfant = 0.7


#Backgrounds

#Space
image earth_close = im.Scale("Intro/earth_close.jpg", 1920, 1080)
image earth_far = im.Scale("Intro/earth_far.jpg", 1920, 1080)
image universe = im.Scale("Intro/universe.png", 1920, 1080)

#Chambre hero
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

define enfant1 = Character("Enfant effrayé", color="#71e0f0")
define im_enfant1 = "Jour3/Rue_avec_enfants/Enfant_1.png"
define zoom_enfant1 = 1.0

define enfant2 = Character("Enfant méchant", color="#d61212")
define im_enfant2 = "Jour3/Rue_avec_enfants/Enfant_2.png"
define zoom_enfant2 = 1.0

define enfant3 = Character("Enfant moqueur", color="#296dff")
define im_enfant3 = "Jour3/Rue_avec_enfants/Enfant_3.png"
define zoom_enfant3 = 1.0

#Crédits
image credits = im.Scale("Credits/credits.png", 1920, 1080)

#Gameover
image gameover = im.Scale("Gameover/gameover.png", 1920, 1080)

#Post-crédits
image phone1 = im.Scale("Post credits/phone1.png", 607, 1080)
image phone2 = im.Scale("Post credits/phone2.png", 607, 1080)
image phone3 = im.Scale("Post credits/phone3.png", 607, 1080)

image phone4_0_1 = im.Scale("Post credits/phone4_0_1.png", 607, 1080)
image phone4_0_2 = im.Scale("Post credits/phone4_0_2.png", 607, 1080)
image phone4_0_3 = im.Scale("Post credits/phone4_0_3.png", 607, 1080)
image phone4_0_4 = im.Scale("Post credits/phone4_0_4.png", 607, 1080)
image phone4_1_0 = im.Scale("Post credits/phone4_1_0.png", 607, 1080)
image phone4_1_1 = im.Scale("Post credits/phone4_1_1.png", 607, 1080)
image phone4_1_2 = im.Scale("Post credits/phone4_1_2.png", 607, 1080)
image phone4_1_3 = im.Scale("Post credits/phone4_1_3.png", 607, 1080)
image phone4_1_4 = im.Scale("Post credits/phone4_1_4.png", 607, 1080)
image phone4_2_0 = im.Scale("Post credits/phone4_2_0.png", 607, 1080)
image phone4_2_1 = im.Scale("Post credits/phone4_2_1.png", 607, 1080)
image phone4_2_2 = im.Scale("Post credits/phone4_2_2.png", 607, 1080)
image phone4_2_3 = im.Scale("Post credits/phone4_2_3.png", 607, 1080)
image phone4_2_4 = im.Scale("Post credits/phone4_2_4.png", 607, 1080)
image phone4_3_0 = im.Scale("Post credits/phone4_3_0.png", 607, 1080)
image phone4_3_1 = im.Scale("Post credits/phone4_3_1.png", 607, 1080)
image phone4_3_2 = im.Scale("Post credits/phone4_3_2.png", 607, 1080)
image phone4_3_3 = im.Scale("Post credits/phone4_3_3.png", 607, 1080)
image phone4_3_4 = im.Scale("Post credits/phone4_3_4.png", 607, 1080)
image phone4_4_0 = im.Scale("Post credits/phone4_4_0.png", 607, 1080)
image phone4_4_1 = im.Scale("Post credits/phone4_4_1.png", 607, 1080)
image phone4_4_2 = im.Scale("Post credits/phone4_4_2.png", 607, 1080)
image phone4_4_3 = im.Scale("Post credits/phone4_4_3.png", 607, 1080)
image phone4_4_4 = im.Scale("Post credits/phone4_4_4.png", 607, 1080)

image phone5_0_1 = im.Scale("Post credits/phone5_0_1.png", 607, 1080)
image phone5_0_2 = im.Scale("Post credits/phone5_0_2.png", 607, 1080)
image phone5_0_3 = im.Scale("Post credits/phone5_0_3.png", 607, 1080)
image phone5_0_4 = im.Scale("Post credits/phone5_0_4.png", 607, 1080)
image phone5_1_0 = im.Scale("Post credits/phone5_1_0.png", 607, 1080)
image phone5_1_1 = im.Scale("Post credits/phone5_1_1.png", 607, 1080)
image phone5_1_2 = im.Scale("Post credits/phone5_1_2.png", 607, 1080)
image phone5_1_3 = im.Scale("Post credits/phone5_1_3.png", 607, 1080)
image phone5_1_4 = im.Scale("Post credits/phone5_1_4.png", 607, 1080)
image phone5_2_0 = im.Scale("Post credits/phone5_2_0.png", 607, 1080)
image phone5_2_1 = im.Scale("Post credits/phone5_2_1.png", 607, 1080)
image phone5_2_2 = im.Scale("Post credits/phone5_2_2.png", 607, 1080)
image phone5_2_3 = im.Scale("Post credits/phone5_2_3.png", 607, 1080)
image phone5_2_4 = im.Scale("Post credits/phone5_2_4.png", 607, 1080)
image phone5_3_0 = im.Scale("Post credits/phone5_3_0.png", 607, 1080)
image phone5_3_1 = im.Scale("Post credits/phone5_3_1.png", 607, 1080)
image phone5_3_2 = im.Scale("Post credits/phone5_3_2.png", 607, 1080)
image phone5_3_3 = im.Scale("Post credits/phone5_3_3.png", 607, 1080)
image phone5_3_4 = im.Scale("Post credits/phone5_3_4.png", 607, 1080)
image phone5_4_0 = im.Scale("Post credits/phone5_4_0.png", 607, 1080)
image phone5_4_1 = im.Scale("Post credits/phone5_4_1.png", 607, 1080)
image phone5_4_2 = im.Scale("Post credits/phone5_4_2.png", 607, 1080)
image phone5_4_3 = im.Scale("Post credits/phone5_4_3.png", 607, 1080)
image phone5_4_4 = im.Scale("Post credits/phone5_4_4.png", 607, 1080)

image phone6_0_1 = im.Scale("Post credits/phone6_0_1.png", 607, 1080)
image phone6_0_2 = im.Scale("Post credits/phone6_0_2.png", 607, 1080)
image phone6_0_3 = im.Scale("Post credits/phone6_0_3.png", 607, 1080)
image phone6_0_4 = im.Scale("Post credits/phone6_0_4.png", 607, 1080)
image phone6_1_0 = im.Scale("Post credits/phone6_1_0.png", 607, 1080)
image phone6_1_1 = im.Scale("Post credits/phone6_1_1.png", 607, 1080)
image phone6_1_2 = im.Scale("Post credits/phone6_1_2.png", 607, 1080)
image phone6_1_3 = im.Scale("Post credits/phone6_1_3.png", 607, 1080)
image phone6_1_4 = im.Scale("Post credits/phone6_1_4.png", 607, 1080)
image phone6_2_0 = im.Scale("Post credits/phone6_2_0.png", 607, 1080)
image phone6_2_1 = im.Scale("Post credits/phone6_2_1.png", 607, 1080)
image phone6_2_2 = im.Scale("Post credits/phone6_2_2.png", 607, 1080)
image phone6_2_3 = im.Scale("Post credits/phone6_2_3.png", 607, 1080)
image phone6_2_4 = im.Scale("Post credits/phone6_2_4.png", 607, 1080)
image phone6_3_0 = im.Scale("Post credits/phone6_3_0.png", 607, 1080)
image phone6_3_1 = im.Scale("Post credits/phone6_3_1.png", 607, 1080)
image phone6_3_2 = im.Scale("Post credits/phone6_3_2.png", 607, 1080)
image phone6_3_3 = im.Scale("Post credits/phone6_3_3.png", 607, 1080)
image phone6_3_4 = im.Scale("Post credits/phone6_3_4.png", 607, 1080)
image phone6_4_0 = im.Scale("Post credits/phone6_4_0.png", 607, 1080)
image phone6_4_1 = im.Scale("Post credits/phone6_4_1.png", 607, 1080)
image phone6_4_2 = im.Scale("Post credits/phone6_4_2.png", 607, 1080)
image phone6_4_3 = im.Scale("Post credits/phone6_4_3.png", 607, 1080)
image phone6_4_4 = im.Scale("Post credits/phone6_4_4.png", 607, 1080)

image phone7_0_1 = im.Scale("Post credits/phone7_0_1.png", 607, 1080)
image phone7_0_2 = im.Scale("Post credits/phone7_0_2.png", 607, 1080)
image phone7_0_3 = im.Scale("Post credits/phone7_0_3.png", 607, 1080)
image phone7_0_4 = im.Scale("Post credits/phone7_0_4.png", 607, 1080)
image phone7_1_0 = im.Scale("Post credits/phone7_1_0.png", 607, 1080)
image phone7_1_1 = im.Scale("Post credits/phone7_1_1.png", 607, 1080)
image phone7_1_2 = im.Scale("Post credits/phone7_1_2.png", 607, 1080)
image phone7_1_3 = im.Scale("Post credits/phone7_1_3.png", 607, 1080)
image phone7_1_4 = im.Scale("Post credits/phone7_1_4.png", 607, 1080)
image phone7_2_0 = im.Scale("Post credits/phone7_2_0.png", 607, 1080)
image phone7_2_1 = im.Scale("Post credits/phone7_2_1.png", 607, 1080)
image phone7_2_2 = im.Scale("Post credits/phone7_2_2.png", 607, 1080)
image phone7_2_3 = im.Scale("Post credits/phone7_2_3.png", 607, 1080)
image phone7_2_4 = im.Scale("Post credits/phone7_2_4.png", 607, 1080)
image phone7_3_0 = im.Scale("Post credits/phone7_3_0.png", 607, 1080)
image phone7_3_1 = im.Scale("Post credits/phone7_3_1.png", 607, 1080)
image phone7_3_2 = im.Scale("Post credits/phone7_3_2.png", 607, 1080)
image phone7_3_3 = im.Scale("Post credits/phone7_3_3.png", 607, 1080)
image phone7_3_4 = im.Scale("Post credits/phone7_3_4.png", 607, 1080)
image phone7_4_0 = im.Scale("Post credits/phone7_4_0.png", 607, 1080)
image phone7_4_1 = im.Scale("Post credits/phone7_4_1.png", 607, 1080)
image phone7_4_2 = im.Scale("Post credits/phone7_4_2.png", 607, 1080)
image phone7_4_3 = im.Scale("Post credits/phone7_4_3.png", 607, 1080)
image phone7_4_4 = im.Scale("Post credits/phone7_4_4.png", 607, 1080)

#Fin
image fin = im.Scale("Fin/fin.png", 1920, 1080)

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

define receptioniste = Character("Murielle", color="#969696")

define im_receptioniste = "Nuit2/Justine/Hana_casual_neutral.png"

define zoom_receptioniste = 0.6

image EMS_couloir = im.Scale("Nuit2/couloir_EMS.jpg", 1920, 1080)

image EMS_chambre_raymond = im.Scale("Nuit2/chambre_2.jpg", 1920, 1080)

image EMS_pharmacie = im.Scale("Nuit2/pharmacie_EMS.jpg", 1920, 1080)

define raymond = Character("Mme Raymond")

define im_raymond = "Nuit2/old_woman.png"
define zoom_raymond = 1.7

define superieur = Character("Supérieur")

define justine = Character("Justine", color="#85b8ff")

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

#Nuit3

image bureau_maire = im.Scale("Nuit3/Bureau/bureau1.jpg", 1920, 1080)

define assistante = Character("Assistante", color="#e50404")

define im_assistante = "Nuit3/Supp/f338.png"

define maire = Character("Maire [nom]", color="#f9e571")

define im_maire = "Nuit3/Maire/maire1.png"

define zoom_maire = 1.0

define zoom_assistante = 1.0

image exterieur_tribunal = im.Scale("Nuit3/Tribunal/exterieur.jpg", 1920, 1080)

define juge = Character("Juge [nom]", color="#f9e571")

define im_juge = "Nuit3/Juge/juge1.png"

define zoom_juge = 1.0

image tribunal = im.Scale("Nuit3/Tribunal/interieur.jpg", 1920, 1080)

define journaliste1 = Character("Journaliste enjoué")

define im_journaliste1 = "Nuit3/Journaliste/journaliste1.png"

define zoom_journaliste1 = 1.0

define journaliste2 = Character("Journaliste prenant des notes", color="#77ff4e")

define im_journaliste2 = "Nuit3/Journaliste/journaliste2.png"

define zoom_journaliste2 = 1.0

image siege_juge = im.Scale("Nuit3/Tribunal/siege du juge.jpg", 1920, 1080)

define nuit3_utilitarisme_first = False
define nuit3_libertarianisme_first = False
define nuit3_utilitarisme_done = False
define nuit3_libertarianisme_done = False

define kami = Character("Kamimusubi", color="#fffdc6")

define im_kami = "Nuit3/Kamimusubi/kami.png"

define zoom_kami = 1.4

define choix_enfant = False
define choix_adultes = False

define sacrifice_quartier = False
define sacrifice_aleatoire = False
define sacrifice_economie = False

define suicide_assiste = False

define juge_relaxation = False
define juge_reduction_peine = False
define juge_perpetuite = False

# Le jeu commence ici
label start:
    #Bienvenue
    narrateur "Bienvenue dans EthiQuest"


    #Name input
    narrateur "Dans cette histoire, vous allez incarner un jeune étudiant. Commencez par écrire votre nom."
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
    gmu "NON PAS DU TOUT, TU TE TROMPES !"

    show screen show_char1(game_master_2, 1.0, 1.0, 1.0)
    with dissolve


    gml "C'EST TOI QUI TE TROMPES TU RACONTES N'IMPORTE QUOI !"

    gmu "De toute façon c’est moi le plus grand alors c’est moi qui décide."
    gml "Mais non, on a le même âge ! Et c’est moi la plus forte."

    gmu "Arrête un peu tes conneries ! On ne peut pas laisser tout le monde faire ce qu’il veut. Il faut des règles."
    gml "Mais il y a des règles ! Chacun dispose de lui-même comme il le souhaite, sans que personne ne puisse l’en empêcher."
    gmu "Ça ne marchera jamais !"
    gml "Bien sûr que si ! "
    gml "Et tu penses que laisser la décision au plus grand nombre, c'est plus efficace ?"
    gmu "Tout à fait ! En satisfaisant le plus de gens, tout le monde est content."
    gml "Non, pas tout le monde ! Tu ne penses pas à toutes les minorités que tu exclus. "
    gml "Si tout le monde dispose de lui-même comme il l’entend, chacun est satisfait."
    gmu "Mais c’est l’anarchie ! Personne n’a le contrôle."
    gml "C’est ça ton problème, tu veux toujours avoir le contrôle sur tout. Laisse les autres décider de ce qu’ils veulent."
    gmu "Mais les gens ont besoin d’être guidés !"
    gml "…"
    gmu "…"
    gml "Je sais comment te prouver que tu as tort. "
    gml "On va faire une expérience sur des cas réels. On a tout l’univers à notre disposition. On peut choisir n’importe qui, n’importe quel endroit, parmi les 299 792 458 planètes."
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
    gmu "J'ai déjà choisi ! On se retrouve en bas frangine !"

    hide screen show_char
    with dissolve

    gml "Hé attends-moi ! Aaaaarrrrh, il m'énerve ..."

    hide screen show_char1
    with dissolve

    jump intro_context

label intro_context:

    scene earth_close
    with dissolve

    narrateur "Les deux enfants-dieux décident d'aller choisir un humain sur la planète Terre pour être le sujet de leurs expériences."

    jump jour1_appartement

label jour1_appartement:

    scene black_background
    with dissolve

    "TOC TOC TOC"

    mere "Réveille-toi, [nom] ! Tu vas être en retard à l'école !!"

    scene room_hero
    with dissolve

    show screen show_char1(boy, 1.0, 1.0, zoom_boy)
    with dissolve

    player "*Bâille* Il faut que j'aille à la cuisine prendre mon petit-déjeuner avant d'aller en cours..."


    call hide_chars from _call_hide_chars_1

    scene salon
    with dissolve

    show screen show_char(im.Flip(mere_neutral, True), 0.0, 1.0, zoom_mom)
    with dissolve

    show screen show_char1(boy, 1.0, 1.0, zoom_boy)
    with dissolve

    mere "Ah tu es debout, très bien ! Voilà tes céréales, [nom]. Mange-les vite, tu dois te dépêcher."


    player "*Crunch, crunch*"
    player "Bon j'y vais ! À ce soir maman."
    mere "Bonne journée, mon chou !"
    menu:
      "Aller à l'école":
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

    teacher "Personne ? N'oubliez pas que vos examens finaux sont le mois prochain, il va falloir se mettre au travail !"

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

    show screen show_char1(boy_confused, 0.3, 1.0, zoom_boy)
    with dissolve


    best_friend "[nom] ! Tu es là !"
    best_friend "Comment s'est passée ta matinée ?"

    menu:
      "Ennuyante":
        player "Ennuyante à mourir... On a fait de la biologie."
      "Passionnante":
        player "Passionnante ! Le corps humain est fascinant."
      "Longue":
        player "Longue, je meurs de faim."

    best_friend "Je vois ! Dépêchons-nous d'aller manger, il y a déjà une queue."
    player "J'arrive !"

    call hide_chars from _call_hide_chars_6

    jump jour1_manger

label jour1_manger:
    scene black_background
    with dissolve

    scene lunchroom_full
    with dissolve

    show screen show_char(best_friend_smile, 0.7, 3.0, zoom_best_friend)
    with dissolve

    show screen show_char1(boy_confused, 1.0, 1.0, zoom_boy)
    with dissolve


    best_friend "Heureusement qu'on s'est dépêchés, on a eu les dernières places !"
    best_friend "Avec les examens qui arrivent tout le monde est stressé et veut manger au plus vite pour avoir le temps de réviser..."
    menu:
      "Sûr de soi":
        player "Pas moi en tout cas ! Je sais que je vais réussir sans problèmes !"
      "Prévoyant":
        player "Oui, le temps passe trop vite... Il faut aussi que je m'y mette."
      "Evasif":
        player "Je préfère passer du temps avec toi !"

    best_friend "Haha, tu as bien raison !"
    best_friend "En parlant de ça, cette nuit, j'ai fait un rêve où on était tous les deux enfermés à l'école jusqu'à ce qu'on arrive à résoudre un exercice de maths impossible !"
    best_friend "Je regardais la feuille mais je comprenais rien et toi tu pleurais en disant qu'on allait mourir de faim avant d'y arriver."
    best_friend "Puis un Pikachu géant est arrivé et a mangé la feuille."
    best_friend "Là, je me suis réveillée en sursaut..."
    best_friend "Bizarre non ?"

    player "Haha, oui mais ne t'inquiète pas, c'est qu'un rêve, c'était pas réel..."
    best_friend "Je sais ! Mais imagine si les rêves avaient des conséquences sur la réalité ! Ca serait terrifiant..."
    player "En effet... Heureusement, que ça reste dans nos têtes !"

    "*Ding* *Ding*"

    best_friend "Ah, c'est l'heure de retourner en classe. Bon, j'y vais. Bon aprem [nom] !"


    call hide_chars from _call_hide_chars_7

    jump jour1_cours

label jour1_cours:

    scene classroom_teacher
    with dissolve


    show screen show_char(teacherP, 0.0, 1.0, zoom_teacher)
    with dissolve

    teacher "N'oubliez pas vos devoirs pour demain ! Lire un chapitre du livre et répondre aux questions liées. On en parlera tous ensemble demain."
    teacher "Bonne soirée."

    call hide_chars from _call_hide_chars_8

    camarade_1 "Aaaah, j'avais oublié, je vais devoir repousser mon entrainement..."
    camarade_2 "Je pense que tu vas pouvoir les oublier tes entrainements ces prochains temps ! On va devoir mettre toute notre énergie dans les révisions..."

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

    narrateur "De retour à la maison."

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
      "J'ai encore beaucoup de travail":
        player "Oui, mais j'ai encore des devoirs pour demain à finir."

    show screen show_char_pos2(mere_neutral, 700, 500, 1.4)
    with dissolve


    mere "Alors, il faut que tu travailles consciencieusement ce soir. Tu aurais besoin d'aide ?"
    player  "Non, ça va aller."
    mere "N'hésite pas, si besoin. Il faut que tu les réussisses ces examens !"
    dad "Ne lui mets pas tant de pression, c'est encore un enfant."
    player "Papa !"
    mere "Oui, je sais... Un adolescent."
    player "*Soupir* Je vais travailler dans ma chambre."

    call hide_chars from _call_hide_chars_10

    jump jour1_chambre_soir

label jour1_chambre_soir:

    scene room_night_light
    with dissolve

    show screen show_char(im.Flip(boy_sad, True), 0.0, 1.0, zoom_boy)
    with dissolve

    player "J'ai fini mes devoirs mais j'arrive pas à dormir..."
    player "Ces histoires d'examens me stressent."
    player "J'espère que je ne vais pas faire un rêve comme Emma cette nuit, je suis crevé."
    call hide_chars from _call_hide_chars_11
    jump reve_1








label reve_1:

  scene universe
  with dissolve

  show screen show_char(game_master_1, 0.0, 1.0, 1.0)
  with dissolve

  gmu "Hey ! Te voilà enfin !"

  narrateur "Tu te retrouve en face d’un mystérieux personnage dans une salle étrange."

  show screen show_char1(boy_confused, 1.0, 1.0, zoom_boy)
  with dissolve

  player "C'est un rêve ?"

  gmu "Dis-moi, tu n’as pas l’air de comprendre ce qu'il t’arrive."

  menu:
    "Qui es-tu ?":
      player "Qui est-tu ?"
      jump reve1_next
    "Où suis-je ?":
      player "Où suis-je ?"
      jump reve1_next

label reve1_next:

  gmu "C’est bien ce qui me semblait.
      Tu as été choisi parmi tous les êtres intelligents de l’univers pour avoir la noble tâche de prouver que je suis le plus sage et que ma vision du monde est la meilleure."

  player "Tous les êtres humains de l’univers ??? Il y a d’autres formes de vie intelligente ?"
  gmu "..."
  gmu "C’est simple, mon idée c'est qu'il faut toujours chercher à maximiser le bonheur du plus grand nombre."
  gmu "T'es d'accord avec moi ?"

  menu:
    "C'est idéal":
      player "Oui c’est idéal. Je rêverai de vivre dans une telle société."
      gmu "Finalement j’ai peut-être choisi la bonne personne"
    "Indécis":
      player "Je ne sais pas, cela me paraît utopique mais assez difficilement réalisable."
      gmu "Toujours septique hein ? Tu verras bien assez vite comment ça s’applique."
      player "J’ai un peu peur de la place des minorités dans tout ça. Et puis… Comment définir le bonheur ?"
      gmu "Définir le bonheur…"
      gmu "C’est simple, c’est quand t’es heureux."
      gmu "Et j’ai pas que ça à faire que de t’apprendre des choses que tout le monde sait déjà."
    "Suspicieux":
      player "Je n’ai pas encore assez étudié la question, il y a peut-être des cas où ce n’est pas la meilleure solution."
      gmu "Un cas où ce n’est pas la meilleure solution ? Les humains sont-ils tous aussi stupides que toi ?"
      player "J’ai un peu peur de la place des minorités dans tout ça. Et puis… Comment définir le bonheur ?"
      gmu "Définir le bonheur…"
      gmu "C’est simple, c’est quand t’es heureux."
      gmu "Et j’ai pas que ça à faire que de t’apprendre des choses que tout le monde sait déjà."

  gmu "Bon allez, passons à la suite."
  gmu "Pour pouvoir interpréter correctement les résultats de ma petite expérience, j’ai besoin de savoir qui est mon sujet."

  show screen show_char1(boy_angry, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Ça te tuerait de me respecter un peu… Je m’appelle [nom]."

  gmu "Je n’en ai strictement rien à faire. Je sais que tu es allé voir ta meilleure amie durant son audition de pi…"
  player "Attends ! Comment-tu sais ça ?"
  gmu "Je sais tout ! Enfin presque…  Lui as-tu dit ce que tu en avais vraiment pensé ? Je crois sentir que ça ne t’a pas spécialement plus."
  player "Ça te regarde pas !"
  gmu "Dis-moi juste si tu lui as dit ce que tu en as réellement pensé ?"
  player "..."
  menu:
    "Oui":
      $ utilitarisme+=0
      player "Oui, j'ai été franc avec elle."
    "Non":
      $ utilitarisme+=1
      player "Non, j'ai eu honte de lui dire."

  show screen show_char1(boy_confused, 1.0, 1.0, zoom_boy)
  with dissolve

  gmu "Je vois."


  player "Je comprend pas pourquoi tu me poses ces questions ! Est-ce que ça a un effet sur la vie réelle ?"
  gmu "Ah ça, tu le découvriras plus tard."
  gmu "Bon, à présent on va passer à la partie un peu plus pratique. Pour le reste de la journée, tu vivras dans la peau d’un chirurgien."
  gmu "Tu seras amené à faire des choix importants et tu comprendras, je l’espère, pourquoi ma façon de penser est la meilleure."

  call hide_chars from _call_hide_chars_12

label reve1_hopital:

  scene hopital_exterieur
  with dissolve

  show screen show_char(docteur, 0.0, 1.0, zoom_doc)
  with dissolve

  show screen show_char1(im.Flip(game_master_1, True), 1.0, 1.0, 1.0)
  with dissolve

  narrateur "Shiawase claque des doigts et les deux se retrouvent devant un hôpital."

  doc "Qu'est ce qui s'est passé ? Comment on est arrivés devant un hôpital ?"
  doc "Et pourquoi je suis plus moi-même ??"
  gmu "T'occupes pas de ces détails. Bon, à partir de maintenant, je te laisse."
  doc "Comment ça ?"
  gmu "Si tu avais écouté ce que je t'ai dit, tu poserais pas ces questions stupides. Allez à plus."

  call hide_chars from _call_hide_chars_13

  jump reve1_hopital_interieur

label reve1_hopital_interieur:

  scene hopital_couloir
  with dissolve

  show screen show_char(docteur, 0.0, 1.0, zoom_doc)
  with dissolve

  show screen show_char1(im.Flip(infirmierePath, True), 0.95, 1.0, zoom_infirmiere)
  with dissolve

  infirmiere "Vous voilà enfin. Le patient est déjà prêt pour son opération. Il s’agit d’une fracture de l’avant-bras.
Nous allons vous préparer."


  call hide_chars from _call_hide_chars_14

label reve1_hopital_after_op:

  scene black_background
  with dissolve

  narrateur "Tu ne comprends toujours pas très bien ce qu'il se passe, mais tu décides de suivre l'infirmier dans les couloirs de l'hôpital."
  narrateur "Après quelques minutes tu te trouve dans une salle d’opération avec d’autres chirurgiens."
  narrateur "Au début, tu n’es pas sûr de ce qu’il faut faire, mais par tu ne sais quelle magie, tu commences à procéder à l’opération comme si
  tu avais fait ça toute ta vie."
  narrateur "Après l'opération, tu ne sais plus vraiment quoi faire. Tu comprends encore moins ce que tu fais ici."
  narrateur "Que faire ?"

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

  narrateur "En te rendant à ta destination, tu te rends compte que tout le monde semble paniquer."

  show screen show_char(infirmierePath, 0.0, 1.0, zoom_infirmiere)
  with dissolve

  show screen show_char1(docteur, 0.95, 1.1, zoom_doc)
  with dissolve

  doc "Qu’est-ce qu’il se passe ici ? "

  infirmiere "*Affolé* Un camion est rentré dans un bus scolaire, c’est un carnage…"

  infirmiere "On a besoin de tout le personnel. On va devoir faire des opérations avec une seule équipe pour plusieurs patients."
  infirmiere "Il y a trois adultes qui ont des bouts de verre un peu partout dans le corps."
  infirmiere "Ils sont stables pour l’instant mais ça pourrait s’aggraver si le travail est mal fait ou si ça tourne en septicémie."
  infirmiere "Les infirmières essayent de faire de leur mieux mais elles ont besoin d’un chirurgien expérimenté pour les guider et contrôler que tout se passe bien."
  infirmiere "Tu peux aller au bloc B3 et t’en occuper ?"
  doc "Oui, j’y vais tout de suite. "

  call hide_chars from _call_hide_chars_18

  scene black_background
  with dissolve

  narrateur "En te rendant au bloc B3, tu es interpellé par une dame qui semble affolée."

  scene hopital_couloir
  with dissolve


  show screen show_char(mere_enfant_im, 0.0, 1.0, zoom_mere_enfant)
  with dissolve

  show screen show_char1(docteur, 1.0, 1.1, zoom_doc)
  with dissolve

  mere_enfant "S’il vous plaît, sauvez mon fils ! Je vous en supplie !"

  infirmiere "Madame, laissez le personnel travailler."

  mere_enfant "Je vous en supplie !"

  doc "Dans quel état est son fils ?"

  show screen show_char(infirmierePath, 0.0, 1.0, zoom_infirmiere)
  with dissolve


  infirmiere "Dans un état grave. Hémoragie interne, perte de conscience."
  infirmiere "De nombreux organes sont touchés, si on ne l’opère pas tout de suite, c’est fini pour lui."
  infirmiere "Mais il n’y a plus personne de disponible. Et puis, même si on intervient, vu son état, on n’est même pas sûr de pouvoir le sauver."
  mere_enfant "Vous devez sauver mon fils !"
  infirmiere "Madame, s'il vous plaît !"
  infirmiere "Que voulez-vous faire docteur ?"


  menu:
    "S'occuper des adultes":
      $ utilitarisme+=2
      $ choix_adultes = True
      doc "Désolé madame, je dois m'occuper des adultes en priorité."
      call hide_chars from _call_hide_chars_19
      jump reve1_soins_adultes
    "S'occuper de l'enfant":
      $ choix_enfant = True
      doc "Ne vous inquiétez madame, je vais tout faire pour sauver votre enfant. "
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

  narrateur "Grâce à ton expertise magique, tu viens de sauver la vie de cet adulte. Qui sait ce qui se serait passé si tu n'étais pas intérvenu ?"

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

  doc "(Il faut que je donne tout pour que cette mère revoie son enfant sain et sauf.)"

  narrateur "Après plusieures heures d'efforts intenses, tu as fais tout ce que tu pouvais pour cet enfant."

  doc "J'ai donné tout ce que j'avais, je ne peux rien faire de plus."

  call hide_chars from _call_hide_chars_23

  scene black_background
  with dissolve

  narrateur "Malheureusement, l’enfant était dans un état trop grave. Tu n'as rien pu faire."
  narrateur "Pendant ce temps, au bloc B3, une des infirmières qui venait de commencer à l’hôpital a commis une erreur et a sectionné une artère d'un adulte, le patient est mort."

label reve1_suite:
  narrateur "Après tous ces efforts, tu es très fatigué. Tu décide de prendre un café avant de rentrer."
  narrateur "Soudain, tu te rappelles que ce soir, tu as promis à ta femme de l'emmener au concert pour son 30ème anniversaire."
  narrateur "Tu te sens trop fatigué pour rentrer en voiture mais le prochain bus est dans 30 minutes, et si tu le prends, tu vas peut-être rater le concert."
  narrateur "Il faut faire un choix."

  menu:
    "Rentrer en voiture":
      jump voiture_reve1
    "Rentrer en bus":
      $ utilitarisme+=1
      jump bus_reve1



label voiture_reve1:


  scene city_day
  with dissolve


  narrateur "Sur le chemin, tu n’arrêtes pas de penser à ce jeune garçon, mort dans d’atroces souffrances..."
  narrateur "Perdu dans tes pensées, tu ne fais plus attention à la route."
  narrateur "Un cul de poule te réveille en sursaut, tu perds le contrôle de la voiture. Tu vois avec horreur une famille en train de traverser la route pile sur ton chemin."
  narrateur "Tu ne peux rien faire pour éviter l'accident, la famille entière décède sur le coup."
  jump jour2

  call hide_chars from _call_hide_chars_24

label bus_reve1:


  scene city_day
  with dissolve

  narrateur "Le bus arrive en avance. La route est dégagée sur le chemin et finalement, tu arrives à l’heure pour l’évènement."

  call hide_chars from _call_hide_chars_25







label jour2:

  scene room_hero
  with dissolve

  "Tu te réveilles en sursaut, des sueurs froides coulant dans ton dos."

  show screen show_char(im.Flip(boy_shocked, True), 0.0, 1.0, zoom_boy)
  with dissolve

  player "Qu'est-ce que c'était que ce rêve ??"
  player "Je n'en avais jamais fait d'aussi réaliste... J'en ai encore des frissons."
  player "En tout cas, ça me donne pas envie de devenir médecin !"

  "..."
  "..."

  player "Je ne me sens pas du tout reposé, c'est comme si j'avais vraiment dû faire ces opérations !"
  player "Et ces choix ..."
  player "'Toujours maximiser le bonheur' ou je sais plus quoi ?"
  menu:
    "C'était facile":
      player "Mais au moins, c'était facile de choisir !"
    "Intéressant":
      player "Je me suis vraiment creusé la tête dans mon rêve, c'était intéressant malgré tout !"
    "Plus jamais":
      player "J'espère que je n'aurais jamais à faire des choix pareils dans la vraie vie..."

  mere "[nom], qu'est-ce que tu fais encore ? Tu vas de nouveau devoir courir !"
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
  player  "Ah oui... Et en plus, c'est mon tour d'amener un truc à manger aujourd'hui."
  player "D'ailleurs, je peux avoir des sous ?"
  mere "Tiens, 10 francs, mais ne fais pas comme la dernière fois, achète vraiment quelque chose pour tes amis !"

  show screen show_char_pos1(boy_flustered, 1300, 500, 0.4)
  with dissolve

  player "Oui, oui, ne t'inquiète pas."

  show screen show_char_pos1(boy, 1300, 500, 0.4)
  with dissolve

  hide screen show_char_pos
  hide screen show_char_pos2
  with dissolve

  player "(Bon, j'ai vraiment la dalle. Je mange un bout et j'y vais.)"
  player "(Zut ! Il ne reste qu'une seule brioche. J'ai vraiment faim mais mon père va encore me faire une crise si je lui laisse rien.)"
  player "(J'ai pas de temps à perdre avec ça !)"

  define brioche_state = 0

  menu:
    "Manger toute la brioche":
      $ brioche_state=1
    "Laisser la brioche à ton père":
      $ brioche_state=2
    "Partager la brioche en deux" if utilitarisme>=3:
      $ brioche_state=3


  call hide_chars from _call_hide_chars_27

  jump jour2_classe


label jour2_classe:

  scene classroom_teacher
  with dissolve

  show screen show_char(im.Flip(boy_shocked, True), 0.0, 1.0, zoom_boy)
  with dissolve

  player "(Je n'arrive pas à me concentrer...)"
  player "(Je n'arrête pas de repenser à mon rêve de cette nuit.)"
  if brioche_state==2:
    player "(En plus j'ai du mal à réfléchir le ventre vide.)"
  player "(Et si ce n'était pas vraiment un rêve ?)"
  player "(On entend souvent parler de gens qui ont des visions envoyées par des démons ou des dieux...)"

  menu:
    "Mais ce sont des fous":
      player "(Mais je me suis toujours dit qu'ils devaient être fous ou rechercher l'attention !)"
    "C'est plutôt cool en fait":
      show screen show_char(im.Flip(boy_happy, True), 0.0, 1.0, zoom_boy)
      with dissolve
      player "(Je me suis toujours dit que c'était trop classe !)"
    "Je n'y crois pas":
      player "(Je ne sais pas si je peux vraiment y croire...)"

  teacher "[nom] ! Qu'est-ce que tu as ce matin ?? Ça fait 3 fois que je te pose une question et tu ne fais que regarder dans le vide !"

  show screen show_char(im.Flip(boy_flustered, True), 0.0, 1.0, zoom_boy)
  with dissolve

  player "Ah, désolé Professeur... J'ai mal dormi cette nuit."

  teacher "Hum, je vais laisser passer pour cette fois, mais veille à ce que cela ne se reproduise plus !"

  call hide_chars from _call_hide_chars_28

  scene black_background
  with dissolve

  narrateur "La pause de midi arrive enfin."

  jump jour2_midi

label jour2_midi:
  scene lunchroom_full
  with dissolve

  show screen show_char(boy_confused, 1.0, 1.0, zoom_boy)
  show screen show_char1(best_friend_smile, 0.7, 3.0, zoom_best_friend)
  with dissolve

  best_friend "... Et quand il s'est enfin retourné, toute la classe a vu l'énorme trou dans son pantalon ! HAHAHAH"

  best_friend "..."

  show screen show_char1(best_friend_neutral, 0.7, 3.0, zoom_best_friend)
  with dissolve

  best_friend "[nom] ? Tu t'es endormi pendant mon histoire ou bien ? Tu as même pas rigolé !"

  player "Ah désolé, Emma !"
  player "J'ai la tête ailleurs..."

  best_friend "Je vois ça, quelque chose te tracasse ? Un problème à la maison ? Ou juste les examens ?"

  player "(Je ne peux pas lui parler de mon rêve, elle ne va jamais comprendre...)"
  player "(Déjà qu'hier, je lui ai dit que les rêves ne sont pas réels, elle va me prendre pour un fou.)"

  show screen show_char(boy_flustered, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Les examens..."
  player "D'ailleurs, il faut que j'aille faire des recherches pour..."
  menu:
    "Danse contemporaine":
      player "Mon cours de danse contemporaine."
    "La chute de l'Atlantide":
      player "Mon exposé sur la chute d'Atlantide."
    "Le coeur des fourmis":
      player "En apprendre plus sur les problèmes de coeur des fourmis."

  best_friend "... Je vois. A bientôt, alors."
  player "A plus !"

  call hide_chars from _call_hide_chars_29

  jump jour2_salle_info

label jour2_salle_info:



  scene salle_info_ouverte
  with dissolve

  show screen show_char(im.Flip(boy_shocked, True), 0.0, 1.0, zoom_boy)
  with dissolve

  player "(Je n'aime pas mentir à Emma mais là je n'avais pas le choix...)"
  player "(Bon, j'aurais quand même pu trouver une meilleure excuse par contre !)"
  player "(J'aurais pu lui dire que j'avais mal à la tête...)"
  player "(Au moins, maintenant, je suis tranquille pour faire des recherches sur les rêves et visions.)"



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

  narrateur "Après quelques recherches..."

  scene salle_info_ferme
  with dissolve

  show screen show_char(im.Flip(boy_nervous, True), 0.0, 1.0, zoom_boy)
  with dissolve


  player "On trouve vraiment de tout et de rien sur internet !"
  player "(Je tombe autant sur des articles scientifiques qui expliquent les rêves lucides, que sur des témoignages de gens qui affirment avoir rencontré Dieu...)"
  player "(J'ai le cerveau qui surchauffe, je crois que je vais m'arrêter là pour aujourd'hui...)"
  player "(D'autant plus que si je ne pars pas maintenant je vais arriver en retard à mon groupe de travail, et je dois encore aller acheter à grignoter !)"

  call hide_chars from _call_hide_chars_31

  jump jour2_rue

label jour2_rue:
  scene rue
  with dissolve

  show screen show_char(im.Flip(boy, True), 0.0, 1.0, zoom_boy)
  with dissolve

  if brioche_state==1:
    player "(Je n'aurais peut-être pas dû prendre la brioche de papa ce matin. J'espère qu'il ne m'en voudra pas trop.)"
    player "(Mais bon, j'ai d'autres choses à penser.)"

  player "(Il me semble qu'il y a une boulangerie au coin de cette rue.)"
  player "(Avec 10 francs, je vais pouvoir me rattraper de la dernière fois, où j'ai oublié d'amener quelque chose !)"
  player "(Peut-être des croissants pour tout le monde... Ou du pain et plein de chocolat ?)"
  player "Hummmm...."

  call hide_chars from _call_hide_chars_32

  jump jour2_boulangerie

label jour2_boulangerie:
  scene boulangerie
  with dissolve

  show screen show_char(im.Flip(boy, True), 0.0, 1.0, zoom_boy)
  show screen show_char1(sdf_normal, 1.0, 1.0, zoom_sdf)
  with dissolve

  sdf "Eh !"
  sdf "Eh, toi là !"

  show screen show_char(im.Flip(boy_flustered, True), 0.0, 1.0, zoom_boy)
  with dissolve

  player "On m'a parlé ?"

  show screen show_char(im.Flip(boy, True), 0.0, 1.0, zoom_boy)
  with dissolve

  sdf "Ah, oui c'était moi ! Excuse moi mais tu a l'air de quelqu'un de généreux. J'ai perdu mon travail l'année passée, ma femme m'a quitté depuis et on m'a éjecté de mon appart..."
  sdf "Tu n'aurais pas un peu d'argent pour que je m'achète à manger ?"

  player "L'argent que j'ai sur moi est pour acheter un gouter à mes amis... "

  define sdf_state = 0

  menu:
    "Mais je te le donne.":
      $ sdf_state=1
      player "Mais je te le donne volontiers, ils comprendront bien !"
      sdf "Merci ! Je suis sûr que tes amis t'en voudront pas d'aider quelqu'un dans le besoin."
      sdf "Bonne soirée !"
      hide screen show_char1
      with dissolve
      player "(Même si mes amis risquent d'être déçus et que ma mère va encore me faire une remarque, j'ai fait une bonne action aujourd'hui !)"
    "Mais je te donne la moité." if utilitarisme>=2:
      $ sdf_state=2
      player "Mais je t'en donne la moitié, ils se contenteront de pain sans chocolat !"
      sdf "Merci ! Je suis sûr que tes amis t'en voudront pas d'aider quelqu'un dans le besoin."
      sdf "Bonne soirée !"
      hide screen show_char1
      with dissolve
      player "(Même si mes amis risquent d'être déçus et que ma mère va encore me faire une remarque, j'ai fait une bonne action aujourd'hui !)"
    "Je suis désolé." if utilitarisme>=3:
      $ sdf_state=2
      show screen show_char(im.Flip(boy_flustered, True), 0.0, 1.0, zoom_boy)
      with dissolve
      player "Je suis désolé demande à quelqu'un d'autre. Bonne chance !"
      sdf "..."
      hide screen show_char1
      with dissolve
      show screen show_char(im.Flip(boy_confused, True), 0.0, 1.0, zoom_boy)
      with dissolve
      player "(J'ai peut-être loupé une chance de faire une bonne action mais au moins mes amis et ma mère ne seront pas déçus cette fois !)"
    "Trouves-toi du travail !" if utilitarisme>=4:
      $ sdf_state=2
      show screen show_char(im.Flip(boy_angry, True), 0.0, 1.0, zoom_boy)
      with dissolve
      player "Trouve toi un travail au lieu de vivre comme un parasite !"
      sdf "..."
      hide screen show_char1
      with dissolve
      show screen show_char(im.Flip(boy_confused, True), 0.0, 1.0, zoom_boy)
      with dissolve
      player "(J'ai peut-être loupé une chance de faire une bonne action mais au moins mes amis et ma mère ne seront pas déçus cette fois !)"

  call hide_chars from _call_hide_chars_33


  jump jour2_revisions

label jour2_revisions:

  scene bibliotheque
  with dissolve

  narrateur "La séance de révision paraît durer des heures, tes yeux se ferment tout seuls, tu n'arrives pas à te concentrer."
  narrateur "Quand c'est enfin le moment de rentrer chez toi, tu dis à peine au revoir et te dépêches d'aller prendre le bus."

  jump jour2_fin

label jour2_fin:
  scene salon_crepuscule
  with dissolve

  show screen show_char(im.Flip(mere_neutral, True), 0.0, 1.0, zoom_mom)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  mere "Alors, cette séance de révision ? Tu as pensé à acheter du goûter cette fois ?"

  if sdf_state==1:
    show screen show_char1(boy_flustered, 1.0, 1.0, zoom_boy)
    with dissolve
    player "..."
    player "Non... J'ai donné l'argent à quelqu'un dans la rue qui en avait plus besoin que moi..."
    mere "..."
    mere "Bon, au moins cette fois, c'était pour une bonne cause. Mais j'espère que tes amis ne vont pas t'en vouloir, tu leur avais quand même promis d'amener quelque chose !"
  elif sdf_state==2:
    show screen show_char1(boy_angry, 1.0, 1.0, zoom_boy)
    with dissolve

    player "Oui, oui, je l'ai fait cette fois !"
    player "Quand est-ce que tu vas arrêter de m'embêter avec ça, j'ai juste oublié une fois !!"

    mere "Pas besoin de t'énerver ! Tes amis devaient être contents que tu aies pensé à eux cette fois."
    mere "Tu sais, c'est important de tenir tes promesses si tu veux garder tes amis."

  show screen show_char1(boy_flustered, 1.0, 1.0, zoom_boy)
  with dissolve
  player "Oui, maman ..."

  if brioche_state==1:
    mere "Au fait, ton père était vraiment mécontent quand il a vu que tu avais mangé sa brioche."
    show screen show_char1(boy_flustered, 1.0, 1.0, zoom_boy)
    with dissolve
    player  "Je sais maman, mais je peux pas aller à l'école le ventre vide !"
    mere "Pense à aller t'excuser et évite que ça se reproduise."
  elif brioche_state==2:
    show screen show_char1(boy, 1.0, 1.0, zoom_boy)
    with dissolve
    mere "Au fait, tu es parti le ventre vide ce matin ?"
    player "Oui, j'ai vu qu'il ne restait qu'une brioche. Je l'ai laissée à papa."
    mere "C'est très gentil de ta part mon chéri."
  elif brioche_state==3:
    show screen show_char1(boy, 1.0, 1.0, zoom_boy)
    with dissolve
    mere "Ton père était content que tu lui aies laissé la moitié de la brioche. Il était étonné de cette réflexion venant de ta part."
    player "haha ! On en apprend tous les jours !"
    player "(Ou dans mon cas la nuit.)"
    mere "C'est bien mon chéri, tu deviens vraiment mature."
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve
  "..."
  "..."
  player "J'ai mal dormi hier soir, je vais aller me coucher tôt pour rattraper ça."
  mere "D'accord, chou."
  mere "Bonne nuit et fait de beaux rêves !"
  player "(J'espère.)"

  call hide_chars from _call_hide_chars_34



label nuit2:
  scene universe
  with dissolve

  show screen show_char(im.Flip(game_master_2, True), 0.0, 1.0, 1.0)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  gml "Ah te voilà enfin !"

  player "Je... Je suis au même endroit qu'hier ?"

  gml "Non pas du tout. Hier tu étais dans la dimension de mon frère. Il t'a raconté n'importe quoi et c'est à mon tour de
       t'expliquer comment je vois le monde et comment il devrait être régi."

  gml "Tu verras c'est bien plus réaliste que l'idée de mon idiot de frère.  Mon idée est l’incarnation même de la liberté. La liberté protégée par la liberté.
  C’est pas beau ça ? Tu verras c’est simple à comprendre."



  call hide_chars from _call_hide_chars_39

  scene plage
  with dissolve





  show screen show_char2(im_glace, 0.5, 1.0, zoom_glace)
  with dissolve

  narrateur "Jiyu claque des doigts et vous vous retrouvez sur une plage où on peut voir quelqu’un manger une glace."

  show screen show_char(im.Flip(game_master_2, True), 0.0, 1.0, 1.0)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  gml "Tu vois le mec là-bas qui mange une glace ? C’est John."
  gml "Pourquoi il a le droit de manger une glace ? Eh bien, c’est simple,
       il l’a achetée légitimement avec son argent et il ne dérange personne."



  call hide_chars from _call_hide_chars_47

  scene maison_martine
  with dissolve

  narrateur "Jiyu claque de nouveau des doigts et vous vous retrouvez cette fois dans un jardin où on voit un nain de jardin."

  show screen show_char(im.Flip(game_master_2, True), 0.0, 1.0, 1.0)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  gml "Là, on est devant la maison de Martine. Attends... "

  hide screen show_char
  with dissolve

  show screen show_char(im.Flip(game_master_2, True), 0.0, 1.0, 1.0)
  show screen show_char2(nain_de_jardin, 0.5, 1.0, zoom_nain)
  with dissolve

  gml "Lui, c’est le nain de jardin de Martine. Si John venait à prendre ce nain de jardin sans l’accord de Martine, comme je l'ai fait hehe, il entrave la liberté
      de propriété de Martine et donc son action est mauvaise."
  gml "Tu vois un peu l’idée ? Tes actions sont immorales uniquement si elles entravent la liberté de quelqu'un d'autre."
  gml "Mais si Martine est d’accord pour que John lui prenne son nain, alors il n’y a pas de problème."
  gml "Et comme ils n’embêtent personne, alors personne n’a le droit d’empêcher leur échange."
  gml "Bien."
  call hide_chars from _call_hide_chars_48

  scene universe
  with dissolve

  show screen show_char(im.Flip(game_master_2, True), 0.0, 1.0, 1.0)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve
  gml "Qu’est-ce que t'en penses jusque-là ?"
  menu:
    "Je suis d'accord":
      player "Je suis d’accord, du moment que l’on entrave pas la liberté de quelqu’un d’autre, on peut faire ce qu’on veut."
      gml "Ca fait plaisir de croiser des personnes avec un minimum d’intellect sur cette planète."
      gml "Bien, alors voyons ça sur un premier cas ultra simple."
    "Sans avis":
      player "Je suis plutôt sans avis. C’est encore trop tôt me faire une idée."
      gml "Je vois qu’il te faut plus d’exemples."
      gml "Bien, alors on va voir un premier cas ultra simple."
    "Pas d'accord":
      player "Je suis pas trop d’accord, je trouve ce principe limité, il faudrait l’accompagner de règles plus détaillées."
      gml "Tu verras, c’est une idée qui se gère par elle-même."
      gml "Bien, alors on va voir si je peux te convaincre. Premier cas ultra simple."

  gml "Dans l’immeuble de John le bruit dérange son voisinage à partir de 21h. Est-ce qu’il a le droit de jouer du piano dans l’après-midi ?"

  menu:
    "Oui":
      $ libertarianisme+=1
      player "Oui, il a le droit."
      gml "Bien, les locataires n'étant pas dérangés par le bruit du piano, il est tout à fait moral de la part de John de jouer du piano."
    "Non":
      player "Non, il n'a pas le droit"
      gml "Eh si, il a bien le droit de le faire."
      gml "Si ça avait été après 21h, il n’aurait pas eu le droit puisqu’il aurait entravé la liberté de dormir des autres locataires."

  gml "Maintenant, une situation un peu plus compliquée."
  gml "John souhaite acheter de la cocaïne afin de passer une bonne soirée. Pour cela,
       il se rend chez un dealeur qu'il connaît bien et qui lui vend de la cocaïne de qualité."
  gml " Est-ce que John a le droit de procéder à ce genre d'échange ? "

  menu:
    "Oui":
      $ libertarianisme+=1
      player "Oui, il n'entrave la liberté de personne ici."
      gml "Exactement ! On pourrait remettre en question le mode de vie de John qui n'est pas très sain mais concrètement,
	         l'achat qu'il fait n'atteint en rien à la liberté de qui que ce soit."
    "Non":
      player "Non, la vente et l'achat de drogues dures est illégal."
      gml "C'est peut-être illégal, mais John ne dérange personne. C'est ça le problème avec l'Etat, il se mêle de choses qui ne le
	         regardent pas !"

  gml "Bon, tu devrais avoir compris le concept. Passons à la suite. Que penses-tu de l'impôt ? "

  menu:
    "C'est nécessaire":
      player "C'est une taxe nécessaire pour assurer le bon fonctionnement de la société."
      gml "Mais tu n'as rien compris à ce que je te dis ! Si je gagne de l'argent à la sueur de mon front, je mérite d'en profiter entièrement."
      gml "Le gouvernement, en me taxant, atteint ma liberté de profiter librement de mon revenu. L'impôt est donc immoral et ne devrait pas exister."
      gml "Ah, moi qui te croyais plus malin que mon frère, au final, tu es tout aussi bête que lui..."
    "Cela ne devrait pas exister":
      $ libertarianisme+=1
      player "On ne devrait pas être taxé sur un revenu qu’on a légitimement gagné en travaillant."
      gml "Exactement ! Bravo, tu as tout compris ! Tu es plus malin que tu en a l'air au final. "
    "Je ne sais pas":
      player "Euuhhh... Je sais pas, j'ai jamais vraiment réfléchi à la question."
      gml "Bon sang, mais tu m'écoutes ou tu dors depuis le début ? L'impôt est une bêtise sans nom."
      gml "Si je gagne de l'argent à la sueur de mon front,
	        je mérite d'en profiter entièrement. Le gouvernement, en me taxant, atteint ma liberté de profiter librement de mon revenu."
      gml "L'impôt est donc immoral et ne devrait pas exister."

  if libertarianisme>=2:
    gml "Bien, tu m’as l’air d’avoir bien compris le concept."
    gml "Je te propose une petit mise en situation histoire de te convaincre entièrement."
    gml "Pour cette partie, tu vas travailler dans une maison de retraite."
  elif libertarianisme==1:
    gml "Bien, tu m’as l’air d’avoir plus ou moins compris le concept."
    gml "Je te propose une petit mise en situation histoire de te convaincre entièrement."
    gml "Pour cette partie, tu vas travailler dans une maison de retraite."
  else:
    gml "T’as vraiment pas l’air d’avoir compris ce que je te raconte."
    gml "On va faire une petite mise en situation pour te mettre les idées au clair."
    gml "Pour ça, tu vas travailler dans une maison de retraite."


  call hide_chars from _call_hide_chars_49

  scene EMS_devanture
  with dissolve

  narrateur "Jiyu claque des doigts et tu l'auras compris, j'espère, vous vous retrouvez devant une maison de retraite."

  show screen show_char(im.Flip(game_master_2, True), 0.0, 1.0, 1.0)
  show screen show_char1(boy_confused, 1.0, 1.0, zoom_boy)
  with dissolve

  gml "Bon, pour ça je vais pas venir avec toi, je déteste les vieux, moi."
  gml "Je te laisse t’annoncer à la réception. Dépêche-toi t’es sensé commencer dans 5 minutes et ne fuis pas, hein !"
  gml "C’est pas parce qu’on est dans un rêve que je peux pas te faire souffrir, hehe. Aller à plus !"

  hide screen show_char
  with dissolve

  player "Pfff, ils commencent à me fatiguer ces petits démons…"

  call hide_chars from _call_hide_chars_50

  scene EMS_reception
  with dissolve

  show screen show_char(im_receptioniste, 0.0, 1.0, zoom_receptioniste)
  show screen show_char1(boy_confused, 1.0, 1.0, zoom_boy)
  with dissolve

  receptioniste "Oh, salut [nom] !"

  player "Salut Murielle."

  receptioniste "T’en fais une des ces têtes t’as passé une mauvaise nuit ?"

  menu:
    "Ouai":
      player "On peut dire ça, ouai…"
      receptioniste "Bref, dépêche toi, tu commences dans 3 minutes. Chambre 548, Mme Raymond à doucher."
      show screen show_char1(boy_flustered, 1.0, 1.0, zoom_boy)
      with dissolve
      player "Dou... doucher !?"
    "Ironique":
      player "Je passe une mauvaise nuit en ce moment même."
      receptioniste "Tu te crois drôle ? Je t’ai déjà dit d’arrêter de me draguer, sale beauf."
      receptioniste "Dépêche-toi, tu commences dans 3 minutes. Chambre 548, Mme Raymond à doucher."
      show screen show_char1(boy_flustered, 1.0, 1.0, zoom_boy)
      with dissolve
      player "Dou... doucher !?"
    "...":
      player "..."
      receptioniste "T’as vraiment pas l’air en forme mais faut te ressaisir."
      receptioniste "Tu commences dans 3 minutes. Chambre 548 pour aider Mme Raymond à prendre sa douche."
      show screen show_char1(boy_flustered, 1.0, 1.0, zoom_boy)
      with dissolve
      player "Sa… sa douche !?"

  receptioniste "Bah oui, elle peut pas se doucher toute seule, fait pas le surpris. Allez, fonce !"

  call hide_chars from _call_hide_chars_51

  scene EMS_couloir
  with dissolve

  show screen show_char1(boy_nervous, 1.0, 1.0, zoom_boy)
  with dissolve

  player "(Ce métier m’a l’air d’être encore plus difficile que chirurgien…)"
  player "(Je connaissais le nom de Murielle sans l’avoir jamais vue en vrai. On dirait que comme dans l’autre rêve, je connais mon environnement magiquement.)"

  call hide_chars from _call_hide_chars_52

  scene EMS_chambre_raymond
  with dissolve


  show screen show_char(im_raymond, 0.0, 1.0, zoom_raymond)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Bonjour Mme Raymond."

  raymond "Monsieur, vous avez 2 minutes et 23 secondes de retard c’est inacceptable !"

  player "Ecoutez madame, on fait ce qu’on peut. Bon, allons-y."

  call hide_chars from _call_hide_chars_53

  scene black_background
  with dissolve

  scene EMS_chambre_raymond
  with dissolve

  show screen show_char1(boy_flustered, 1.0, 1.0, zoom_boy)
  with dissolve


  player "(Ouh là, je ne me suis pas trompé. C’était cent fois plus éprouvant que d’opérer à cœur ouvert.)"

  show screen show_char1(boy_confused, 1.0, 1.0, zoom_boy)
  with dissolve

  narrateur "Ton téléphone sonne."

  player "Allô ?"

  superieur "Oui [nom], tu dois aller dans la chambre de M.Dumas pour lui administrer ses médicaments, chambre 433."

  superieur "Oublie pas de prendre les médicament au rez-de-chaussée avant. J’en ai marre de te voir faire 10 allers-retours inutiles par jour. On perd du temps."

  menu:
    "Je fais ça tout de suite":
      player "Ca marche, je fais ça tout de suite."
      superieur "Fais vite pour une fois, ça te changera…"
      player "(Je ferais mieux de pas traîner.)"
    "Quels médicaments ?":
      player "Ok, je dois prendre quoi comme médicaments ?"
      superieur "Comme d’habitude, bon sang ! Tu vas vite devoir arrêter ce genre de questions si tu veux continuer à travailler ici."
      player "(Maintenant que j’y réfléchis, c’est Justine qui s’occupe des médicaments que je dois administrer… Je ferais mieux de me pas traîner.)"
    "10 allers-retours ?":
      superieur "Exactement 10. Tu as fait 10 aller-retours hier qui n’étaient pas du tout nécessaires. On en reparlera ce soir, crois-moi !"
      player "(Je ferais mieux de ne pas traîner.)"

  call hide_chars from _call_hide_chars_54

  scene EMS_pharmacie
  with dissolve

  show screen show_char(im.Flip(im_justine, True), 0.0, 1.0, zoom_justine)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Salut Justine, il me faudrait les médicaments quotidiens de M.Dumas, s’il-te-plaît."

  justine "Oui, ils sont déjà prêts. Tiens."
  justine "Oh et puis, essaye de discuter un moment avec lui. Je sais que le supérieur déteste ça, mais ça doit bientôt faire 10 ans que M.Dumas ne reçoit plus de visites...
           Le pauvre se sent tellement seul."

  player "(Bien-sûr, je ferais tout pour toi Justine.)"

  narrateur "Tu vérifies le contenu du récipient."

  show screen show_char1(boy_confused, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Mmmmh, on dirait qu’il manque les somnifères."

  justine "Mais c’est normal ça."

  justine "Les somnifères sont dans le petit coffre-fort juste à côté de la table de chevet, comme pour toutes les chambres."

  justine "Tu devrais avoir la clef dans ton trousseau de travail."

  player "Ah ok, bizarre, j’étais pas au courant."

  justine "Ca a été mis en place y’a quelques jours seulement."

  justine "On leur donne tellement de somnifères que la direction a jugé que ce serait plus efficace
          de mettre un stock directement dans chaque chambre plutôt que d'aller demander l’autorisation à la pharmacie tout le temps."

  justine "Par-contre ça fait qu’ils ne sont plus du tout réglementés, ils subissent le même contrôle qu’un vulgaire stock de mouchoirs, ahah."

  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Ah d’accord, merci pour l’info Justine et à bientôt !"
  justine "A plus [nom] !"

  call hide_chars from _call_hide_chars_55

  scene chambre_Dumas
  with dissolve

  show screen show_char(im_dumas, 0.0, 1.0, zoom_dumas)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Bonjours Monsieur Dumas, je viens pour vous donner vos médicaments."

  dumas "Merci bien vous êtes très aimable."

  menu:
    "Comment ça va ?":
      player "Comment vous allez aujourd'hui, Monsieur Dumas ?"
      dumas "Pas très bien, je ne peux presque plus me mouvoir, j’ai besoin d’assistance pour prendre mes médicaments, prendre ma douche, m’habiller, pour n’importe quoi !"
      dumas "C’est insupportable. Si vous saviez à quel point je m’ennuie."

      show screen show_char1(boy_confused, 1.0, 1.0, zoom_boy)
      with dissolve

      menu:
        "Que faites-vous, alors ?":
          player "Qu’est-ce que vous faites de vos journées, alors ?"
          dumas "Rien du tout. Cela fait plus de 10 ans que j’attends ma mort quotidiennement."
          player "Je suis sincèrement navré Monsieur Dumas…"
          player "Vous n’avez pas de famille ?"
          dumas "Mon fils unique venait régulièrement me rendre visite avec ses enfants."
          dumas "Au moins deux fois par semaine."
          dumas "Il cherchait même une plus grande maison pour me faire emménager chez lui."
          dumas "Il détestait me voir dans cette maison de retraite."
          dumas "Malheureusement, il est mort il y a 10 ans lors d’un accident de voiture."
          dumas "Il y avait… Il y avait ses deux enfants et sa femme dedans."
          dumas "En une fraction de seconde, je me suis retrouvé sans famille, plus seul que jamais."
    "Vous n'avez plus de visites ?":
      player "On m’a dit que vous n’aviez plus de visites. Comment ça se fait ?"
      dumas "Mon fils unique venait régulièrement me rendre visite avec ses enfants."
      dumas "Au moins deux fois par semaine."
      dumas "Il cherchait même une plus grande maison pour me faire emménager chez lui."
      dumas "Il détestait me voir dans cette maison de retraite."
      dumas "Malheureusement, il est mort il y a 10 ans lors d’un accident de voiture."
      show screen show_char1(boy_confused, 1.0, 1.0, zoom_boy)
      with dissolve
      dumas "Il y avait… il y avait ses deux enfants et sa femme dedans."
      dumas "En une fraction de seconde je me suis retrouvé sans famille, plus seul que jamais."
  menu:
    "Je peux faire quelque chose ?":
      player "Toutes mes condoléances Monsieur Dumas..."
      show screen show_char1(boy, 1.0, 1.0, zoom_boy)
      with dissolve
      player "Est-ce que je peux faire quelque chose pour vous ?"
      jump nuit2_e1
    "Cétait votre seul famille ?":
      player "Toutes mes condoléances Monsieur Dumas. C’était la seule famille que vous aviez ?"
      dumas "J’ai bien encore deux salopes de tantes mais croyez-moi, si elles venaient me rendre visite, ma situation serait encore pire."
      dumas "Elle sont insupportables ! Je préfère encore être seul que me faire critiquer des heures durant par ces vipères."
      player "Je peux bien comprendre ça..."

  dumas "..."
  player "..."
  dumas "Est-ce… est-ce que vous pourriez me rendre un service ?"
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve
  player "Bien-sûr Monsieur Dumas. De quoi avez-vous besoin ?"

label nuit2_e1:
  dumas "J’ai entendu dire que les somnifères ne sont plus contrôlés, c’est vrai ?"
  player "Tout à fait, on vient de m’en parler justement. Pourquoi ?"
  dumas "S’il vous plait, pourriez-vous m’en donner une dizaine que j’en finisse ?"

  show screen show_char1(boy_flustered, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Mais enfin, M.Dumas je peux p.."
  dumas "S’il vous plait … Je n’en peux plus."
  dumas "Cela fait des années qu’on ne me rend plus visite, des années que je suis seul à attendre l’inévitable."
  dumas "J’ai demandé un suicide assisté mais cette foutue association chrétienne ne veut rien entendre."
  dumas "Vous voyez bien mon état. 10 ans que c’est comme ça, 10 ans que ça dur et ça ne risque pas de s'améliorer."

  player "..."

  dumas "Tout ce que vous avez à faire, c’est me donner les somnifères. Je suis encore capable de les ingérer moi-même. Et vous ne risquez rien puisqu’ils ne sont plus contrôlés."
  dumas "S’il vous plait… aidez-moi."
  dumas "Aidez-moi à rejoindre ma famille."

  menu:
    "Donner les somnifères":
      $ suicide_assiste = True
      $ libertarianisme+=1
      show screen show_char1(boy_confused, 1.0, 1.0, zoom_boy)
      with dissolve
      player "Bon, tenez... Après tout, c’est votre choix, vous faites ce que vous voulez."
      dumas "Enfin.. Merci beaucoup Monsieur, merci beaucoup."
      jump nuit2_somni
    "Refuser de lui donner les somnifères":
      player "C’est pas mon problème. Je suis auxiliaire de santé, pas bourreau. Débrouillez-vous sans moi !"
      dumas "Non attendez !"
      dumas "ATTENDEEEEZ !"
      jump nuit2_non_somni

label nuit2_somni:
  call hide_chars from _call_hide_chars_56

  scene EMS_couloir
  with dissolve

  show screen show_char1(boy_sad, 1.0, 1.0, zoom_boy)
  with dissolve

  player "(J’ai fait le bon choix, mais ça reste perturbant d’aider quelqu’un à mourir.)"
  player "(J’espère qu’on ne va pas savoir que c’est moi qui l'ai aidé !)"

  call hide_chars from _call_hide_chars_57

  jump jour3

label nuit2_non_somni:
  call hide_chars from _call_hide_chars_58

  scene EMS_couloir
  with dissolve

  show screen show_char1(boy_angry, 1.0, 1.0, zoom_boy)
  with dissolve

  player "(Pour qui il se prend ??)"
  player "(C'est pas à moi de me salir les mains. Je n’y peux rien !)"
  player "(Si la maison de retraite ne veut pas l’aider, ils doivent bien avoir leurs raisons...)"

  call hide_chars from _call_hide_chars_59









label jour3:
  scene room_hero_night
  with dissolve
  narrateur "Tu te retrouve tout à coup dans ton lit."
  show screen show_char(im.Flip(boy_shocked, True), 0.0, 1.0, zoom_boy)
  with dissolve

  player "HAAAAAA !!!"

  narrateur "Il te faut un moment pour te rappeler qui tu es et où tu te trouves."

  player "*Halète* J'en peux plus ! Si ça continue, je vais devenir dingue !"
  player "Il m'a rendu fou avec ses délires de liberté ! Moi aussi je veux être libre !"
  player "Il faut absolument que je trouve une solution."

  mere "Tout va bien, chéri ? Je t'ai entendu crier !"

  player "Oui, oui, juste un mauvais rêve !"

  mere "Tu veux venir m'en parler ?"

  player "Non, ça va aller."

  mere "Fait vite, c'est bientôt l'heure de partir !"

  player "*Soupir* (Il faut vraiment que j'en parle à quelqu'un, mais ma mère va encore me dire que c'est juste le stress des examens et que je dois manger mieux...)"

  player "(Alors qui ? Emma ?)"

  player "(Si elle me croit, on pourrait chercher une solution ensemble après les cours ! Elle a toujours des bonnes idées.)"

  mere "[nom] ?"

  player "J'arrive !"


  call hide_chars from _call_hide_chars_35

  narrateur"Tu décides de ne rien dire à ta mère. Emma est ta meilleure amie, si quelqu'un peut te comprendre, c'est bien elle !"

label jour3_ecole:
  scene ecole_exterieur
  with dissolve

  show screen show_char(im.Flip(boy, True), 0.0, 1.0, zoom_boy)
  with dissolve

  player "(Pour une fois, je suis un peu en avance en cours.)"

  show screen show_char1(im_fumeur, 1.0, 1.0, zoom_fumeur)
  with dissolve

  show screen show_char(im.Flip(boy_angry, True), 0.0, 1.0, zoom_boy)
  with dissolve

  player "(Hum, je croyais que c'était interdit de fumer vers les écoles...)"

  hide screen show_char1
  show screen show_char(im.Flip(boy_nervous, True), 0.0, 1.0, zoom_boy)
  with dissolve


  player "(Bref, je commence à stresser... Et si Emma me prenait pour un fou ??)"
  player "(Mais non, on est amis depuis bien trop longtemps...)"
  player  "(Courage ! Je vais lui envoyer un message pour se retrouver après les cours.)"

  player "Hum... "
  player "'Coucou ! Est-ce que tu as du temps cet aprem pour que je te parle d'un truc ??'"
  player "'Ce serait cool si tu pouvais me retrouver après les cours. J'ai besoin de toi !'"

  player "Oui, autant faire simple. Envoyer !"

  player "Il reste plus qu'à attendre une réponse..."

  show screen show_char1(im_fumeur, 1.0, 1.0, zoom_fumeur)
  with dissolve

  show screen show_char(im.Flip(boy_angry, True), 0.0, 1.0, zoom_boy)
  with dissolve

  player "(Ah, il m'a envoyé sa fumée dans la tête !)"

  narrateur "Le fumeur jette sa cigarette dans un pot de fleur."

  player "(Est-ce que je lui dis quelque chose ?)"

  menu:
    "Non, rien, il a le droit de faire ce qu'il veux..." if libertarianisme>=3:
      show screen show_char(im.Flip(boy, True), 0.0, 1.0, zoom_boy)
      with dissolve
      player "(Non, rien, il a le droit de faire ce qu'il veux...)"
      fumeur "Bonne journée, gamin !"
      player "Ah ! A vous aussi..."
    "Lui demander de la jeter ailleurs":
      player "Monsieur ! Jeter des cigarettes dans les fleurs, c'est très mauvais écologiquement !"
      show screen show_char(im.Flip(boy, True), 0.0, 1.0, zoom_boy)
      with dissolve
      player "Est-ce que vous pouvez la jeter dans une poubelle ?"
      fumeur "Euh... Oui, okay..."
      player "Merci ! Bonne journée."
      fumeur "Ouais... A toi aussi."
    "Réprimander" if utilitarisme>=3:
      player "Monsieur ! Fumer c'est mauvais pour la santé ! Et en plus ça coûte super cher aux assurances tous les cancers..."
      fumeur "De quoi tu te mèles, gamin ! C'est ma vie et elle te regarde pas !"
      hide screen show_char1
      show screen show_char(im.Flip(boy_nervous, True), 0.0, 1.0, zoom_boy)
      with dissolve
      player "(Ah, peut-être que c'était pas la bonne méthode...)"

  hide screen show_char1
  with dissolve


  narrateur "Tu sens ton téléphone vibrer."

  show screen show_char(im.Flip(boy, True), 0.0, 1.0, zoom_boy)
  with dissolve

  player "(Ah c'est déjà la réponse d'Emma !)"
  player  "'Oui, pas de problème ! Retrouve-moi à la bibliothèque.'"

  show screen show_char1(teacherP, 1.0, 1.0, zoom_teacher)
  with dissolve

  teacher "[nom] ! Encore sur ton téléphone ?! Je te signale que les cours commencent dans 1 minute !"

  player "Ah, désolé.. J'arrive tout de suite !"

  teacher "Bon, je te retrouve en classe."

  call hide_chars from _call_hide_chars_36

label jour3_bibliotheque:

  scene bibliotheque
  with dissolve

  narrateur "La journée passe étonnament vite et te voilà déjà à la bibliothèque avec Emma. "

  show screen show_char(best_friend_neutral, 0.0, 3.0, zoom_best_friend)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  best_friend "[nom], te voilà ! Qu'est ce qui se passe ? Ca avait l'air important dans ton message."

  player "*Grande inspiration*"

  show screen show_char1(boy_flustered, 1.0, 1.0, zoom_boy)
  with dissolve

  menu:
    "Je veux pratiquer un exorcisme":
      player "J'ai besoin de ton aide pour faire un exorsisme ! Je crois que je suis maudit."
    "Je suis hanté":
      player "Je suis hanté par des sortes de dieux bizarres, j'ai besoin de ton aide pour m'en débarrasser !"
    "Je fais des rêves bizarres":
      player "J'ai besoin de toi pour trouver la cause de mes rêves bizarres et les arrêter."

  best_friend "Quoi ?? Attends, je comprends pas. Explique-moi tout depuis le début !"

  narrateur "Après de longues explications détaillées..."

  best_friend "..."

  player "Emma ?"

  best_friend  "..."

  player "Emma, dis quelque chose !"

  best_friend "Hum..."

  best_friend "Je dois avouer que j'ai de la peine à y croire mais si tu me dit que c'est vrai, alors je vais t'aider à trouver une solution !"

  player "Merci ! Je sais pas ce que je ferais sans toi !"

  best_friend "Mais non, mais non ! Bon, mettons-nous au boulot, il doit bien y avoir des livres sur les visions envoyées par des dieux dans cette bibliothèque !"

  best_friend "Tu prends cette étagère et moi celle d'à côté, okay ?"

  player "C'est parti !"

  call hide_chars from _call_hide_chars_37

  scene black_background
  with dissolve
  narrateur "La recherche de livres prend peu de temps, il y en a plein !"

  scene bibliotheque
  with dissolve

  show screen show_char(best_friend_neutral, 0.0, 3.0, zoom_best_friend)
  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  best_friend "Regarde cette pile de livres ! On va bien pouvoir trouver quelque chose là dedans !"

  call hide_chars from _call_hide_chars_38

  scene black_background
  with dissolve

  narrateur "Tu te lances avec espoir dans la lecture de cette pile de livres."

  scene bibliotheque
  with dissolve

  show screen show_char(best_friend_neutral, 0.0, 3.0, zoom_best_friend)
  show screen show_char1(boy_confused, 1.0, 1.0, zoom_boy)
  with dissolve

  player "Pffff, ce livre parle uniquement de dieux grecs... Je pense pas que ce soit utile."


  best_friend "[nom], viens vite ! Je crois que j'ai trouvé quelque chose !"

  show screen show_char(best_friend_neutral, 0.0, 3.0, zoom_best_friend)
  with dissolve

  best_friend "Ce livre parle d'un rituel qui permet d'invoquer des kami !"
  best_friend "Apparemment, c'était très utilisé pendant l'époque Edo pour communiquer avec divers dieux, dont Kamimusubi, le créateur divin."
  best_friend "Si on arrive à l'invoquer, il saura peut-être comment se débarrasser de ceux de tes rêves !"

  show screen show_char1(boy_happy, 1.0, 1.0, zoom_boy)
  with dissolve


  player  "Bravo Emma ! Il reste plus qu'à espèrer que ça marche !"

  show screen show_char1(boy, 1.0, 1.0, zoom_boy)
  with dissolve


  player "De quoi on va avoir besoin ?"

  best_friend "Hum... Ils parlent d'une offrande de gâteaux de riz aux algues et de sake... Puis ils disent de purifier l'air avec de l'encens..."
  best_friend "Et pour appeler le kami-sama, il nous faudra une cloche consacrée au dieu qu'on veut invoquer."

  menu:
    "Ca va être compliqué":
      player "ça va être compliqué de trouver tout ça..."
    "Bientôt libéré !":
      player "Plus que quelques étapes et je serais libéré de ces rêves !"
    "Dans le doute":
      player "Je doute que ça marche mais ça vaut la peine d'essayer..."

  best_friend "Je peux aller piquer des gâteaux de riz et du sake chez mes parents mais il va falloir aller acheter le reste."

  player "Va chez toi chercher les offrandes ! Je m'occupe de l'encens et de la cloche."

  best_friend "Très bien, j'y vais. On se retrouve ici dès qu'on a tout ce qu'il faut, okay ?"

  player "Oui, à toute !"

  hide screen show_char
  with dissolve

  player "Bon, où est-ce que je vais bien pouvoir trouver ces trucs... Je vais faire une recherche sur mon téléphone."
  player  "Ah, j'ai trouvé une boutique shinto pas loin d'ici ! Même s'ils n'ont pas exactement ce qu'il faut, ils pourront me renseigner."

  call hide_chars from _call_hide_chars_40

  scene black_background
  with dissolve

label jour3_rue_enfants:

  scene rue_avec_enfants
  with dissolve

  show screen show_char_pos3(boy_sad, 1400, 300, zoom_boy)
  with dissolve

  player  "Alors, je crois qu'il faut aller par là."

  show screen show_char_pos(im_enfant1, -100, 300, zoom_enfant1)
  show screen show_char_pos1(im_enfant2, 400, 300, zoom_enfant2)
  show screen show_char_pos2(im.Flip(im_enfant3, True), 800, 300, zoom_enfant3)
  with dissolve

  enfant1 "Laissez-moi tranquille, j'essaye de faire mes devoirs !"
  player  "Qu'est ce qu'il se passe ici ?"
  enfant2 "Hahah ! Le petit je-sais-tout prend de l'avance pour pouvoir bien lècher les pieds du prof !"
  enfant3 "De toute façon, tout le monde le déteste, il a rien d'autre à faire ! Et il faut bien qu'il fasse ses devoirs s'il veut garder sa place de chouchou !"
  enfant2 "Moi je sais pourquoi il veux absolument que le prof l'aime !"
  enfant3 "Vas-y !"
  enfant1 "Arrêtez..."
  enfant3 "J'ai entendu dire que son père l'a abandonné quand il était petit !"
  enfant1 "C'est pas vrai..."

  player "(Je peux quand même pas rester sans rien faire, non ?)"

  menu:
    "Partir" if utilitarisme>=2 and libertarianisme>=3:
      narrateur "Tu pars discrètement en évitant les enfants."
      jump jour3_rue
    "Aller à l'encontre des agresseurs" if utilitarisme>=2:
      player "Ca suffit, laissez ce garçon tranquille ! Ses histoires familiales ne vous concernent pas et si c'est un bon élève, tant mieux pour lui !"
      jump jour3_defense
    "Défendre le père":
      player "Si son père est parti, c'est qu'il avait ses raisons et elles ne vous regardent pas !"
      jump jour3_defense
    "Défendre l'enfant" if libertarianisme>=2:
      player "Ca suffit, laissez ce garçon tranquille ! Il a bien le droit de faire ses devoirs tranquille !"
      jump jour3_defense

label jour3_defense:

  show screen show_char_pos2(im_enfant3, 800, 300, zoom_enfant3)
  with dissolve

  enfant3 "Pfff, de quoi tu te mèle ?"
  enfant2 "Laisse tomber, on y va."

  hide screen show_char_pos1
  hide screen show_char_pos2
  with dissolve

  enfant1 "Merci d'avoir essayé, mais ils vont continuer à m'embêter tu sais...."
  player  "Il faut bien que quelqu'un leur disent un truc... Au moins, j'aurais essayé !"
  player "La prochaine fois, va voir un professeur !"
  enfant1 "Oui, peut-être..."
  player "Bon, je dois y aller. A plus."


label jour3_rue:

  call hide_chars from _call_hide_chars_41

  scene ruelle_sombre
  with dissolve

  show screen show_char(im.Flip(boy, True), 0.0, 1.0, zoom_boy)
  with dissolve

  player "(Avec ces histoires, je vais devoir me dépêcher d'aller acheter ce qu'il me faut pour l'invocation.)"
  player  "(Bon, où est le magasin ?)"
  player "(... C'est dans une petite rue pas loin. Je devrais vite y être.)"

  call hide_chars from _call_hide_chars_42

  scene avant_rue
  with dissolve

  show screen show_char(im.Flip(boy, True), 0.0, 1.0, zoom_boy)
  with dissolve

  player "(Cette ruelle est vraiment glauque, je serais jamais passé par là normalement...)"
  player "(Aller, courage, le magasin est juste là !)"

  call hide_chars from _call_hide_chars_43

  scene black_background
  with dissolve

  narrateur "Heureusement, le vendeur avait de l'encens de tous types et même la bonne cloche dans ses stocks. Tu payes et ressors, soulagé."

  scene parc
  with dissolve

  show screen show_char(boy, 0.0, 1.0, zoom_boy)
  with dissolve

  player "(Je pensais pas que ça serait si facile, il avait même la cloche consacrée !)"
  player "(Il me reste plus qu'à retourner à la bibliothèque, Emma doit déjà m'attendre.)"

  show screen show_char1(im_perso_louche, 1.0, 1.0, zoom_louche)
  with dissolve

  perso_louche "Eh petit !"

  show screen show_char(im.Flip(boy_shocked, True), 0.0, 1.0, zoom_boy)
  with dissolve

  perso_louche "Oui, toi !"
  perso_louche "J'ai entendu ce que tu disais au vendeur, tu cherche à avoir des visions, c'est ça ?"
  perso_louche "Approche, j'ai ce qu'il te faut..."

  menu:
    "Aller voir" if libertarianisme>=2:
      jump jour3_louche
    "Partir":
      player "Ca m'intéresse pas. Au revoir."
      show screen show_char(boy_shocked, 0.0, 1.0, zoom_boy)
      with dissolve
      perso_louche "Tu sais pas c'que tu rates..."
      narrateur "Sans un regard en arrière, tu te dépêche de quitter la ruelle pour retourner à la bibliothèque."
      jump jour3_soir_bibliotheque

label jour3_louche:

  player  "Qu'est ce que c'est ?"
  perso_louche  "Oh, juste des champignons, tout c'qu'il y a d'plus naturel..."
  perso_louche "Si tu les fais infuser et qu'tu bois le jus, t'es garantis d'avoir toutes sortes de visions, hehe."
  player "Est-ce que ça permet de parler avec les kami ?"
  perso_louche "Hehe, avec ça, tu parles avec qui tu veux, crois moi !"

  menu:
    "J'achète" if libertarianisme>=3:
      $ champi_achete = True
      player "Je veux bien essayer. C'est combien ?"
      perso_louche "T'as fait le bon choix, petit. Tiens, c'est 20 francs pour un champi magique !"
      player "Voilà... Au revoir."
      perso_louche "C'est ça..."
      player "(Je vais le garder de côté, comme ça, si le rituel ne marche pas, j'ai toujours une autre solution...)"
      narrateur "Tu mets le champignon en sécurité dans ton sac et repart pour ton rendez-vous avec Emma."
      jump jour3_soir_bibliotheque
    "Non merci":
      player "Ca m'intéresse pas. Au revoir."
      perso_louche "Tu sais pas c'que tu rates..."
      narrateur "Sans un regard en arrière, tu te dépêche de quitter la ruelle pour retourner à la bibliothèque."
      jump jour3_soir_bibliotheque
    "Non, mes parents seraient furieux !" if utilitarisme>=3:
      player "Non, si mes parents l'apprenent, ils me tueraient !"
      perso_louche "C'que tu fais dans ton coin regardes que toi, petit !"
      perso_louche "Bah, tant pis pour toi..."
      hide screen show_char1
      with dissolve
      player "(Jamais je pourrais décevoir ma famille comme ça... Même si ça me débarrassait des visions !)"
      jump jour3_soir_bibliotheque

label jour3_soir_bibliotheque:
  call hide_chars from _call_hide_chars_44

  scene bibliotheque_nuit
  with dissolve

  show screen show_char(boy, 0.4, 1.0, zoom_boy)
  show screen show_char1(best_friend_neutral, 0.1, 3.7, zoom_best_friend)
  with dissolve

  best_friend "Ah te voilà ! T'en as mis du temps, ça fait un moment que je t'attends."
  best_friend "J'ai trouvé tout ce que je devais chez moi !"
  best_friend "Et toi ? Tu as tout trouvé ?"

  player "Oui, on a tout ce qu'il nous faut !"
  player "Qu'est ce qu'il faut faire ensuite ?"

  best_friend "Alors... Il faut allumer l'encens et préparer les offrandes comme pour un invité."
  best_friend "Puis, quand tu seras prêt, il faudra sonner la cloche trois fois, en laissant bien le son s'éteindre entre chaque fois."
  best_friend "Et finalement, appeler le kami par cette formule rituelle : 'Kami-sama, réponds à ma prière et joins-toi à moi pour me libérer du poids de mes pêchés.'"
  best_friend "Tu as compris, [nom] ?"

  player "Oui."
  best_friend "D'après ce livre, le kami va décider s'il pense que tu es digne de sa visite et si c'est le cas, il devrait t'envoyer une vision dans ton sommeil, ou quelque chose comme ça.
  Cette partie est pas très claire..."
  player "Comment je saurais si ça a marché ?"
  best_friend "Hummm... Je penses que tu devras attendre cette nuit et tu verras bien..."

  player "..."

  best_friend "Ah, encore une chose ! Ils disent que tu peux aider le kami à trouver le chemin de tes rêves en l'appelant par son nom cinq fois."
  player "Donc s'il ne vient pas tout de suite, il suffit que je dise Kamimusubi cinq fois ?"
  best_friend "C'est ça."
  show screen show_char(boy_sad, 0.4, 1.0, zoom_boy)
  with dissolve


  player "J'espère vraiment que ça va marcher..."
  best_friend "Bon, assez discuté, il faut qu'on s'y mette ! Je devrais déjà être rentrée chez moi !"

  call hide_chars from _call_hide_chars_45

  scene black_background
  with dissolve

  narrateur "Vous préparez les offrandes et brulez l'encense."

  scene bibliotheque_nuit
  with dissolve

  show screen show_char(boy, 0.4, 1.0, zoom_boy)
  show screen show_char1(best_friend_neutral, 0.1, 3.0, zoom_best_friend)
  with dissolve

  best_friend "A toi, [nom]. Quand tu es prêt, sonne la cloche et dis les paroles rituelles."
  "Ding..."
  "..."
  "Ding..."
  "..."
  "Ding..."
  "..."

  player "Kami-sama, réponds à ma prière et joins-toi à moi pour me libérer du poids de mes pêchés."

  show screen show_char(boy_confused, 0.4, 1.0, zoom_boy)
  with dissolve

  player "..."
  best_friend "..."
  player "..."
  best_friend "Tu penses que ça a marché ?"
  player "Aucune idée..."
  best_friend "Tu verras bien cette nuit... S'il vient pas tout de suite, oublie pas que tu peux dire son nom pour l'appeler !"
  player "J'essayerais d'y penser !"
  player "Bon, je te laisse, à demain."
  best_friend "A demain ! Bonne chance !"

  call hide_chars from _call_hide_chars_46

label jour3_soir_maison:
  scene room_hero_night
  with dissolve

  show screen show_char(im.Flip(boy_happy, True), 0.0, 1.0, zoom_boy)
  with dissolve

  player "Dans quelques heures, tout ce calvaire sera enfin fini et je pourrai reprendre ma vie comme avant !"

  show screen show_char(im.Flip(boy_confused, True), 0.0, 1.0, zoom_boy)
  with dissolve

  player "Enfin, si le rituel a fonctionné..."
  show screen show_char(im.Flip(boy_flustered, True), 0.0, 1.0, zoom_boy)
  with dissolve
  player "Je suis trop stressé, je vais jamais réussir à m'endormir !"

  show screen show_char(im.Flip(boy_confused, True), 0.0, 1.0, zoom_boy)
  with dissolve

  if champi_achete:
    player "Mais au pire, si ça marche pas, j'ai toujours le champignon de cet aprem..."


  player  "Peut-être que si je répète la phrase d'invocation, il y aura plus de chance que Kamimusubi vienne ?"

  player "Kami-sama, réponds à ma prière et joins-toi à moi pour me libérer du poids de mes pêchés."

  player "Kami-sama, réponds à ma prière et joins-toi à moi pour me libérer du poids de mes pêchés."

  player "Kami-sama, répond... Répond à ma prière et..."

  player "Kami-sama..."

  call hide_chars from _call_hide_chars_60


label nuit3:
  scene universe
  with dissolve

  show screen show_char(game_master_1, 0.0, 1.0, 1.0)
  show screen show_char1(game_master_2, 1.0, 1.0, 1.0)
  with dissolve

  gmu "Non même ce que tu dis c’est n’importe quoi !"
  gml "Comment ça ? C’est toi qui dis de la merde !"
  gmu "Je suis ton aîné alors forcément que j’ai raison !"
  gml "Arrête de te prendre pour un grand. Tu as à peine 42 nanosecondes de plus que moi."
  gmu "Je sens que notre discussion va encore tourner en rond. Viens, on va demander l’avis à notre cobaye."

  show screen show_char2(boy_angry, 0.5, 1.0, zoom_boy)
  with dissolve
  gmu "Ah, le voilà !"
  gml "Alors, laquelle de nos idées t’as le plus séduit et convaincu ?"

  menu:
    "Idée de Shiawase" if (utilitarisme != 0 or libertarianisme != 0) :
      show screen show_char2(boy, 0.5, 1.0, zoom_boy)
      with dissolve
      player "Pour moi, les principes de ton frère sont les meilleures."
      gmu "Ah ah ah ! Alors on ne sait plus quoi dire ? Tu dois bien accepter que j’ai gagné !"
      gml "N’importe quoi ! Tu lui pas présenté les limites évidentes de ton idée."
      gml "C'est vraiment à moi de tout faire ici !"
      $ nuit3_utilitarisme_first = True
      jump nuit3_utilitarisme
    "Idée de Jiyu" if (utilitarisme != 0 or libertarianisme != 0) :
      show screen show_char2(boy, 0.5, 1.0, zoom_boy)
      with dissolve
      player "Je trouve tes principes plus intéressants que ceux de ton frère."
      gml "Ce résultat était prévisible. Je t’ai prouvé une nouvelle fois que je suis meilleure que toi."
      gmu "J’ai pas dit mon dernier mot ! On va voir comment le cobaye va réagir quand je lui montrerai les absurdités de ton idée."
      $ nuit3_libertarianisme_first = True
      jump nuit3_libertarianisme
    "Aucune" if (utilitarisme != 0 or libertarianisme != 0) :
      show screen show_char2(boy_sad, 0.5, 1.0, zoom_boy)
      with dissolve
      player "Aucune ! Je ne suis convaincu ni par l'un ni par l'autre."
      gml "Je sais comment régler ça. Je vais te montrer en quoi l’idée de mon frère est nulle."
      $ nuit3_libertarianisme_first = True
      jump nuit3_libertarianisme
    "Euh, c’est quoi déjà vos idées ?"  if (utilitarisme == 0 and libertarianisme == 0):
      show screen show_char2(boy_nervous, 0.5, 1.0, zoom_boy)
      with dissolve
      player "Euh, c’est quoi déjà vos idées ?"
      gml "Mais tu te fous de nous ??!!"
      gmu "On s’est fait chier à tout t’expliquer et toi t’en as rien à foutre."
      gml "Frangin, tu sais vraiment pas choisir les bonnes personnes. Je vais en chercher un autre avec un minimum d’intellect."
      gml "Tuons-le !"
      gmu "Bien dit !"
      jump gameover


label nuit3_utilitarisme:

  $ nuit3_utilitarisme_done = True

  gml "Pour te montrer une bonne fois pour toutes que les idées de mon frère sont stupides, je vais te mettre dans la peau du maire d’une ville en crise."
  gml "Bonne chance à toi !"

  hide screen show_char
  hide screen show_char1

  show screen show_char2(boy_nervous, 0.5, 1.0, zoom_boy)
  with dissolve

  player "Comment ça en cri.."

  call hide_chars from _call_hide_chars_61

  scene bureau_maire
  with dissolve

  show screen show_char(im_maire, 0.0, 1.0, zoom_maire)
  with dissolve

  assistante "Monsieur le maire vous êtes là ?"

  maire "Euuh… oui rentrez."

  narrateur "Une fois de plus tu te retrouve plongé dans une situation étrange sans explications."
  narrateur "Heureusement, tu commences à avoir l'habitude."

  show screen show_char1(im_assistante, 1.0, 1.0, zoom_assistante)
  with dissolve

  assistante "Monsieur le maire, c’est une catastrophe ! La sécheresse va durer plus longtemps que prévu !"

  maire "Est-ce qu’on aura assez d’eau pour les habitants de la ville ?"

  assistante "Non, nous avons sous-estimé la situation et nous avons eu une gestion de l’eau catastrophique."

  assistante "Jamais nous ne tiendrons tous jusqu'à la fin de la sécheresse."

  maire "Il n’y pas d’autres moyens de s’approvisionner en eau ?"

  assistante "Malheureusement, le temps que le prochain approvisionnement arrive, il sera déjà trop tard."

  maire "Est-ce que nous pouvons encore rationner l'eau pour que tout le monde puisse avoir au moins le nécessaire pour survivre ?"

  assistante "Même si nous distribuons l'eau au strict minimum, une partie de la population ne pourra pas survivre."

  assistante "Monsieur le maire, il vous faut prendre une décision maintenant."

  maire "Comment pourrait-on choisir qui devrait vivre ou mourir ? On va se mettre toute la ville à dos. Ce serait l’anarchie."
  maire "On ne pourrait pas réquisitionner l’eau des industries locales ?"

  assistante "On pourrait mais cela paralyserait l’économie et donnerait lieu à une crise économique. Il y a de fortes chances que la population soit encore plus en colère que si on en laissait simplement certains mourir… "

  maire "Qu'est ce que vous voulez dire ?"

  assistante "Eh bien..."
  assistante "Vous vous souvenez de ce quartier qui trouble régulièrement l'ordre public?"

  maire "Vous parlez de celui qui fait régulièrement des émeutes car les habitants pensent que nous n’en faisons pas assez
pour les intégrer à la ville ?"

  assistante "Exactement. Au début la majorité de la ville soutenait ce quartier."
  assistante "Il faut avouer que nous n'avions pas complètement
respecté nos promesses électorales."

  assistante "Mais récemment, ces émeutes ont fini par impacter les autres quartiers. Vitrines cassées, magasins vandalisés, voitures incendiées…"

  maire "Où voulez-vous en venir ?"

  assistante "Le soutient de la population envers ce quartier a fortement diminué. Beaucoup ont même exprimé leur mécontentement
et demandent des interventions plus musclées de la part de la police pour éviter ces débordements."

  assistante "Sur les réseaux sociaux nous avons déjà
recensé de nombreux messages de haine à l'encontre de ce quartier."
  assistante "Au vu du mécontentement général, si nous privons ce quartier d’eau pour le bien-être du plus grand nombre, la majorité de la ville devrait nous soutenir."

  assistante "C’est peut-être triste à dire, mais la majorité serait bien plus satisfaite qu’on sacrifie ce quartier qu’ils détestent plutôt qu’on paralyse l’économie."

  maire "On a le droit de faire ça ?"

  assistante "C'est vous le maire."

  assistante "Alors, quelle est votre décision, monsieur le maire ?"

  menu:
    "Assurer la stabilité de la ville en sacrifiant un quartier":
      $ sacrifice_quartier = True
      maire "Nous devons assurer la stabilité et la survie de la ville. Nous devons sacrifier ce quartier pour le bien de tous."
    "Nous allons faire ce choix aléatoirement":
      $ sacrifice_aleatoire = True
      maire "Ce n’est pas moral de sacrifier une minorité juste parce qu’elle ne plait pas à la ville. Nous ferons ce choix aléatoirement quitte à ce que ça ne plaise pas à tout le monde."
    "Réquisitionner l'eau des industries locales":
      $ sacrifice_economie = True
      maire "Nous allons réquisitionner l’eau des industries locales même si ça paralyse l’économie."

  call hide_chars from _call_hide_chars_62

  scene universe
  with dissolve
  show screen show_char1(game_master_2, 1.0, 1.0, 1.0)
  show screen show_char2(im.Flip(boy_confused, True), 0, 1.0, zoom_boy)
  with dissolve
  gml "Je crois que cette situation t'as bien permi de voir que le concept de bonheur majoritaire est débile."
  gml "Même un idiot comprendrait que ça peux pas marcher !"

  if(nuit3_utilitarisme_done and nuit3_libertarianisme_done):
    jump nuit3_suite

  show screen show_char2(boy_confused, 0.5, 1.0, zoom_boy)
  show screen show_char(game_master_1, 0.0, 1.0, 1.0)
  with dissolve
  gmu "Jiyu !"
  gmu "Si tu crois avoir gagné la partie avec ce rêve, tu te trompes."


label nuit3_libertarianisme:

  $ nuit3_libertarianisme_done = True

  gmu "On va aller au tribunal pour te présenter une nouvelle situation en lien avec l’idée de ma soeur."
  gmu "Cette fois, pas moyen que tu penses que c'est elle qui a les meilleures idées !"
  gmu "Pour cette situation, tu seras un juge."

  call hide_chars from _call_hide_chars_63

  scene exterieur_tribunal
  with dissolve

  show screen show_char(game_master_1, 0.0, 1.0, 1.0)
  show screen show_char1(im.Flip(im_juge, True), 1.0, 1.0, zoom_juge)
  with dissolve

  juge "Tiens, je suis vieux cette fois..."
  gmu "Je te félicite pour cette observation inutile."
  gmu "Bref, comme tu peux le voir, nous voici devant un tribunal."
  gmu "Prépare toi à juger une affaire très particulière."
  gmu "Tu verras bien que l'idée de Jiyu est nulle en pratique !"
  call hide_chars from _call_hide_chars_64

  scene tribunal
  with dissolve

  show screen show_char(im_journaliste1, 0.0, 1.0, zoom_journaliste1)
  with dissolve

  journaliste1 "Bonjour, nous voici en direct du tribunal pour cette affaire sordide qui a profondément choqué les habitants de tout un
village…"

  juge "(Mais qu’est qu’il est en train de me faire faire ??)"

  call hide_chars from _call_hide_chars_65


  scene siege_juge
  with dissolve

  show screen show_char(im_journaliste1, 0.0, 1.0, zoom_journaliste1)
  show screen show_char2(im_juge, 0.5, 1.0, zoom_juge)
  with dissolve

  journaliste1 "Monsieur le juge, que pensez-vous de cette affaire ?"

  show screen show_char1(im_journaliste2, 1.0, 1.0, zoom_journaliste2)
  with dissolve

  journaliste2 "Une autre question monsieur le juge, avec les chefs d’accusations qui pèsent sur le coupable, avez-vous déjà réfléchi
à une sanction ?"

  "La sécurité intervient et écarte les journalistes."

  hide screen show_char
  hide screen show_char1
  with dissolve

  juge "Bien, nous pouvons commencer."
  juge "La séance est ouverte. Présentez les chefs d’accusations."

  "Voici la situation. Gilbert a égorgé vivant son meilleur ami Justin, puis l’a empaillé avant de le stocker dans son grenier."

  "Justin lui avait dit qu’il souhaitait mourir et que son dernier souhait était de se faire égorger vivant puis empailler par un
taxidermiste."

  "Gilbert étant taxidermiste de profession, Justin lui as demandé son aide."
  "Gilbert s’est d'abord assuré que Justin possédait une bonne capacité de discernement en lui
demandant sa carte de vote ainsi qu’une attestation récente d’un psychologue qui affirmait qu’il avait pleine possession de ses moyens.
  "

  "Rassuré
  et puisque Justin était consentant en plus d'être son meilleur ami, Gilbert s’est exécuté."
  "Monsieur le juge, maintenant que vous avez toutes les informations, quel est votre verdict ?"

  menu:
    "Prison à vie":
      $ juge_perpetuite = True
      juge "Je le mets en prison à vie pour homicide volontaire."
    "Peine réduite":
      $ juge_reduction_peine = True
      juge "Je le mets en prison mais je réduis la peine car je dispose d’une preuve irréfutable que Justin était consentant et conscient de son acte."
    "Relaxation":
      $ juge_relaxation = True
      juge "Je choisis de le relaxer. L’acte de Gilbert a beau être extrême, il n’atteint la liberté de personne vu que Justin était consentant."

  call hide_chars from _call_hide_chars_66

  scene universe
  with dissolve

  show screen show_char(game_master_1, 0.0, 1.0, 1.0)
  show screen show_char2(boy_confused, 1.0, 1.0, zoom_boy)
  with dissolve
  gmu "Hahahahah, en tout cas on peut dire que cette situation t'as bien montré la débilité des idées de Jiyu !"
  gmu "Maintenant, t'est obligé d'être d'accord avec moi !"

  if(nuit3_libertarianisme_done and nuit3_utilitarisme_done):
    jump nuit3_suite

  show screen show_char2(boy_confused, 0.5, 1.0, zoom_boy)
  show screen show_char1(game_master_2, 1.0, 1.0, 1.0)
  with dissolve
  gml "Shiawase !"
  gml "Si tu crois avoir gagné la partie avec ce rêve, tu te trompes."

  jump nuit3_utilitarisme

label gameover:
  call hide_chars from _call_hide_chars_67

  scene black_background
  with dissolve

  narrateur "Ce n'était vraiment pas la bonne chose à dire !"
  narrateur "Tu as fait fort pour avoir mal répondu à toutes les questions."
  narrateur "Ou alors tu as un morale très spécifique !"
  narrateur "Dans tous les cas..."

  scene gameover
  with dissolve

  "GAMEOVER !"

  return

label nuit3_suite:

  call hide_chars from _call_hide_chars_68

  scene universe
  with dissolve

  show screen show_char(game_master_1, 0.0, 1.0, 1.0)
  show screen show_char1(game_master_2, 1.0, 1.0, 1.0)
  show screen show_char2(boy, 0.5, 1.0, zoom_boy)
  with dissolve

  if nuit3_utilitarisme_first :
    gmu "Non mais c’est quoi ce rêve à la con que tu lui as montré ?"
    gml "Hein ? On en parle du tien ? "
    gmu "Si c’est comme ça je vais lui montrer d’autres situations pour qu'il voie bien que mon idée, c'est la meilleure sans aucun doute !"
    gml "T'inquiète, je vais faire pareil ! J’en ai encore plein d’autres en stock."
  else :
    gml "Non mais c’est quoi ce rêve à la con que tu lui as montré ?"
    gmu "Hein ? On en parle du tien ? "
    gml "Si c’est comme ça je vais lui montrer d’autres situations pour qu'il voie bien que mon idée, c'est la meilleure sans aucun doute !"
    gmu "T'inquiète, je vais faire pareil ! J’en ai encore plein d’autres en stock."

  show screen show_char2(boy_angry, 0.5, 1.0, zoom_boy)
  with dissolve

  player "CA SUFFIT !!!"

  player "J’en ai marre de vous. Vous me pourrissez la vie et je vais me débarrasser de vous définitivement !"

  player "(Merde ! C'était quoi le rituel déjà ?)"

  player "KAMIMUSUBI ! KAMIMUSUBI ! KAMIMUSUBI !"

  player "..."

  gml "Frangin, je crois que le cobaye a craqué."

  player "(Je réessaie...)"

  player "KAMIMUSUBI ! KAMIMUSUBI ! KAMIMUSUBI !"

  gmu "Je crois aussi qu'il a pété les plombs. On en fait quoi ?"

  player "(Merde ! Ca marche pas !)"

  gml "Je pense qu’on va en chercher un nouveau et…"

  player "(Ah oui !!! C'était 5 fois....)"

  player "KAMIMUSUBI ! KAMIMUSUBI ! KAMIMUSUBI ! KAMIMUSUBI ! KAMIMUSUBI !"

  gmu "Allez, tuons-le !"

  call hide_chars from _call_hide_chars_69

  scene black_background
  with dissolve

  scene universe
  with dissolve

  show screen show_char(game_master_1, 0.0, 1.0, 0.6)
  show screen show_char1(game_master_2, 1.0, 1.0, 0.6)
  show screen show_char2(boy_confused, 0.77, 1.0, 0.15)
  show screen show_char3(im_kami, 0.3, 1.5, 1.5)
  with dissolve

  kami "Qu’est-ce que…"
  kami "Qu’est -ce que je fais la ?"
  kami "Hé ! Qu’est-ce VOUS faites là ?? "

  gmu "Ah mais … On fait rien de mal..."
  gml "Oui, on voulait juste… "

  kami "SILENCE !"
  kami "Je vous avais dit de toujours me demander avant d’entrer dans un rêve !"
  kami "C’est pas possible, je m’absente juste deux ans pour réfléchir à mes créations et on m’invoque à cause de vos conneries ! "

  gml "Maître ! On voulait vérifier nos théories !"

  kami "Vous pouvez faire ça sans faire chier un pauvre humain qui n’a rien demandé."
  gmu "Mais Maître..."
  kami "Suffit ! Allez zou, à la maison !"

  gml "Non Maître, ne faites p..."

  scene black_background
  with dissolve

  hide screen show_char
  hide screen show_char1

  scene universe
  with dissolve

  kami "Bon, maintenant on va pouvoir parler tranquillement."


  hide screen show_char2
  hide screen show_char3

  show screen show_char(boy_nervous, 1.0, 1.0, zoom_boy)
  show screen show_char1(im_kami, 0.1, 1.0, zoom_kami)
  with dissolve

  player "Putain, enfin !"

  show screen show_char(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  kami "Je suis vraiment désolé pour tout ce que ces deux crapules t’ont fait subir. Ils ont tellement de pouvoir et sont si immatures que c’est dur de les contenir."

  kami "Bon, je te dois au moins des explications pour ce qu'il t'es arrivé, petit."
  kami "Quand ces petits monstres ont décidé de se renseigner sur l’éthique des mortels, j’aurais dû me douter que ça allait dérailler."

  kami "Comme d’habitude, ils n'ont pas réussi à se mettre d’accord et ont commencé à se disputer."

  menu:
    "L’éthique des mortels ?":
      player "L’éthique des mortels ?"
      jump nuit3_suite_2
    "...":
      jump nuit3_suite_2

label nuit3_suite_2:
  kami "Shiawase a lu un livre sur l’utilitarisme et il est immédiatement devenu fan."
  kami "Mais comme ce n'est qu'un enfant, il a pris au mot tout ce qu'il a lu."
  kami "Je vais t'expliquer un peu mieux les idées de ce courant, humain."

  kami "L’utilitarisme est une doctrine morale dont le principe est d’agir de façon à maximiser le bien-être collectif."

  kami "Par là, il faut comprendre qu’il faut quantifier le bonheur ou le malheur que nos choix, nos actions ont généré afin de déterminer si notre comportement était bon ou mauvais."

  kami "Les utilitaristes considèrent que lorsque l’on fait un choix, s’il existe une autre possibilité où le bonheur total est plus grand, alors notre action était injuste."

  kami "Tu vois lors de ton premier rêve ..."

  if(choix_adultes):
    kami "Tu as choisi de t’occuper des trois adultes."
    kami "Ton choix était utilitariste car tu as préféré t’assurer de la survie de trois personnes plutôt que d’essayer de sauver un enfant qui allait surement mourir."
    kami "Tu as maximisé le bonheur global, humain."
  else:
    kami "Tu as choisi de t’occuper de l’enfant."
    kami "Ton choix n’était pas utilitariste car tu as préféré essayer de sauver un enfant qui était condamné d'avance plutôt que de t’assurer de la survie de trois personnes."
    kami "Ton choix n’a pas maximisé le bonheur global puisqu’au final aussi bien l’enfant qu'un adulte sont morts."

  kami "Le concept de l’utilitarisme est intéressant, mais comme tu l’as surement constaté, il a des limites."

  kami "D’abord, quantifier le bonheur est très subjectif."
  kami "Qu’est-ce que le bonheur ? Est-il le même pour tout le monde ? Quels critères prendre en compte ?"

  kami "Il y a beaucoup de situations où certains pensent que c’est l’option A qui maximise le bien-être tandis que d’autres pensent que c’est l’option B."
  kami "Ces divergences dans la façon d’estimer le bonheur ont donné lieu à de multiples variantes de l’utilitarisme."
  kami "Mais bon, au final, c'est impossible de dire qui est le plus juste puisque, soyons honnêtes, il est impossible de quantifier objectivement le bonheur."

  kami "De plus, la théorie utilitariste est fondée sur la conséquence."
  kami "Notre action est morale uniquement si les conséquences de celle-ci maximisent le bien-être."
  kami "Or tu te doutes bien que dans un univers aussi complexe que le nôtre, il est assez utopiste de penser qu’un simple humain pourrait estimer correctement toutes les conséquences de ses actes."

  menu:
    "En effet !":
      player "En effet !"
    "J'ai toujours réussi à calculer les conséquences de mes choix":
      player "Moi, j'ai toujours réussi à calculer les conséquences de mes choix"
      kami "Ahahahah, mais qu’est-ce que tu es bête, petit. Heureusement que tu m’as invoqué sinon les deux autres t’auraient certainement tué."
      show screen show_char(boy_flustered, 1.0, 1.0, zoom_boy)
      with dissolve
      player "…"

  show screen show_char(boy, 1.0, 1.0, zoom_boy)
  with dissolve

  kami "Pour finir l’utilitarisme se concentre tellement sur le bien-être global qu’il en oublie les minorités."
  kami "Imagine une société où exécuter publiquement les personnes appartenant à une minorité maximiserait le bien-être collectif."
  kami "Est-ce que l’action reste morale ?"
  kami "Je ne pense pas qu’on puisse bafouer la dignité humaine au nom du bonheur global."

  if(sacrifice_quartier):
    kami "Pourtant, juste avant, tu as choisi de sacrifier un quartier car cela convenait à la majorité."
    kami "Ton choix était totalement utilitariste mais était-il moral ?"
    kami "Ce pauvre quartier n’était pas plus responsable que les autres de la sécheresse alors pourquoi est-il le seul à en subir les conséquences ?"
    kami "Je ne pense pas que sacrifier des vies pour le confort du plus grand nombre soit la meilleure chose à faire…"
  elif(sacrifice_aleatoire):
    kami "Juste avant, tu as choisi de sélectionner aléatoirement les personnes qui n’auront pas d’eau."
    kami "Ton choix n’était pas utilitariste car sacrifier le quartier que la majorité déteste maximisait le bien-être."
    kami "Pourtant ta décision me parait plus juste car tu n’as discriminé personne et tu as bien remarqué que le quartier n’était pas plus responsable que les autres de la sécheresse."
  else:
    kami "Juste avant, tu as choisi de garantir la survie de tout le monde et de sacrifier l’économie de la ville."
    kami "Ton choix n’était pas utilitariste car la crise va surement fortement baisser le niveau de vie global ce qui ne maximise clairement pas le bien-être."
    kami "Pourtant ta décision me parait plus juste car tu n’as discriminé personne et tu as bien remarqué que le quartier n’était pas plus responsable que les autres de la sécheresse."

  kami "Toutefois le livre de Shiawase couvrait uniquement l’utilitarisme. Il existe plusieurs autres courants."

  kami "Jiyu lui est tombé sur un livre qui développe la théorie libertariste."
  kami "Le libertarisme ou libertarianisme, est un courant éthique qui prône une société où l’Etat n’aurait comme unique rôle de respecter les droits de l’Homme ainsi que le droit de propriété."
  kami "Selon les libertaristes, du moment que nos actions n’atteignent en rien la liberté des autres alors on a le droit de les faire."
  kami "Par conséquent ils considèrent l’impôt comme immoral puisqu’il enfreint notre liberté de disposer de notre revenu. Lors de ton second rêve :"

  if(suicide_assiste):
    kami "Tu as choisi de donner les somnifères à M.Dumas. C’est un choix libertariste puisque tu considères que M.Dumas a le droit de disposer de sa vie comme il l’entend."
    kami "C’est sa liberté et il ne dérange personne, même pas sa famille malheureusement."
  else:
    kami "Tu as refusé de donner les somnifères à M.Dumas. Ton choix n’est pas libertariste puisque tu as empêché M.Dumas de disposer de sa vie comme il l’entend."
    kami "Tu limites sa liberté alors que sa volonté ne dérange personne, même pas sa famille."

  kami "Tout comme l’utilitarisme, cette doctrine est intéressante et offre des pistes sur comment concevoir notre morale, mais elle comporte également de nombreuses limites."

  menu:
    "Des limites ?":
      player "Des limites ?"
      kami "En effet !"
      jump nuit3_suite_4
    "En fait, vous êtes wikipédia Monsieur ?":
      player "En fait, vous êtes wikipédia Monsieur ?"
      kami "Monsieur !? Je suis quand même le créateur de l’univers, wikipédia compris."
      kami "Je n’arrive pas à croire que tu oses te moquer de moi, tu ferais mieux de fermer ta grande bouche si tu tiens à l’humanité."
      player "D’accord. (Dieu a vraiment pas d’humour… oh ! est-ce qu’il sait que je pense ça !? J’espère pas…)"
      kami "..."
      kami "Bon, revenons à nos moutons, comme vous dites vous humains."
      jump nuit3_suite_4
    "...":
      jump nuit3_suite_4



label nuit3_suite_4:
  kami "D’abord, cette doctrine du libertarisme ne prend pas en compte les inégalités sociales."
  kami "Dans une société libertariste, les riches seraient encore plus privilégiés que maintenant puisqu’ils pourraient subvenir à tous leurs besoins sans jamais donner pour la collectivité publique."
  kami "Ainsi, toutes les aides sociales seraient extrêmement limitées, si ce n’est inexistantes."
  kami "D’après les idées libertaristes, on peut choisir de partager ou non car on mérite entièrement tout notre revenu."
  kami "Cela sous-entend qu’il n’y aurait pas de problèmes à laisser mourir une population de faim, même si on a largement les moyens de la nourrir."
  kami "De plus tous les contrats devraient être légaux."
  kami "Cela peut mener à des situations totalement inhumaines."
  kami "Par exemple, une personne pauvre en très grande difficulté, ne bénéficiant de presque aucune aide, pourrait se retrouver à devoir vendre son rein pour nourrir sa famille."
  kami "Bon, tu me diras que c'est déjà ce qui se passe dans votre monde."
  kami "Enfin, le libertarisme valorise tellement le consentement que ça en est dérangeant. Avec l’histoire du taxidermiste par exemple."

  if(juge_relaxation):
    kami "Tu as beau avoir acquitté Gilbert. Je me demande si c’était le bon choix."
    kami "Est-ce moral d’autoriser les crimes et les mutilations les plus sordides au nom du consentement et de la liberté de chacun ?"
    kami "Même si ce qu’a fait Gilbert était autorisé par son ami et qu’il n'a dérangé personne, je me demande si on a vraiment envie de laisser en liberté quelqu’un qui a empaillé un être humain."
  elif(juge_reduction_peine):
    kami "Tu as choisi de mettre Gilbert en prison avec peine réduite."
    kami "Même si au fond, Gilbert n’entravait pas la liberté des autres, tu as bien remarqué que ce n’était pas très moral de laisser en liberté quelqu’un qui a empaillé un être humain."
    kami "Comme quoi, il faut toujours réfléchir quand on fait un choix moral et pas bêtement appliquer une doctrine."
  else:
    kami "Tu as choisi de mettre Gilbert en prison."
    kami "Même si au fond, Gilbert n’entravait pas la liberté des autres, tu as bien remarqué que ce n’était pas très moral de laisser en liberté quelqu’un qui a empaillé un être humain."
    kami "Comme quoi, il faut toujours réfléchir quand on fait un choix moral et pas bêtement appliquer une doctrine."
    kami "Après, peut-être que tu as été un peu rude avec une peine pour homicide volontaire."
    kami "Gilbert était certes conscient de son acte, mais il s’était tout de même assuré du discernement de son ami avant de procéder."
    kami "Peut-être ne mérite-t-il pas la même sanction qu’un meurtrier qui a tué un pauvre innocent."

  kami "Au final, Shiawase et Jiyu sont venu t’embêter pour prouver que leur vision était la meilleure mais au fond, aucune ne l’est vraiment."
  kami "L’utilitarisme ou le libertarisme, ces deux doctrines offrent de bonnes pistes de réflexions sur la morale mais les deux sont limitées et c’est à toi, simple être humain, de réfléchir un minimum à tes choix et de ne pas appliquer bêtement une doctrine."
  kami "J'espère que cette histoire aura au moins eu le mérite de te faire réfléchir, petit."
  menu :
    "Oh oui, ça c'est sûr !":
        player "Oh oui, ça c'est sûr !"
        kami "Ah, peut-être qu'il y a de l'espoir pour les humains après tout."
    "Pas vraiment...":
        player "Pas vraiment..."
        kami "Alors je te conseille de t'y mettre dès maintenant !"
    "Mes idées sont meilleures !":
        player "Mes idées sont meilleures !"
        kami "Tu es bien bête si tu n'est même pas capable de te remettre en question !"
        kami "Parfois j'oublie à quel point les humains peuvent être étroits d'esprit..."

  kami "Enfin, si jamais l’éthique t’intéresse, humain, je te conseille de te renseigner sur le kantisme."
  kami "C’est aussi une doctrine morale mais assez différente que les deux que tu as vues et personnellement, je l’aime bien."

  menu:
    "J'en ai marre de l'éthique !":
      player "Ca devrait aller je suis un peu gavé de l’éthique là…"
      kami "Ah, je ne comprendrais jamais la paresse des humains."
    "Le kantisme ?":
      player "Le kantisme ? C’est noté je vais regarder ce que c’est ! Au point où j’en suis, autant être calé dans le domaine..."
      kami "HAHAHA, on dirait que t’es motivé, ça fait plaisir."

  kami "Je dois te laisser malheureusement. En tant que dieu-créateur, je suis assez demandé, vois-tu."
  kami "Navré pour Shiawase et Jiyu, ça n’arrivera plus ne t’en fais pas."
  kami "Adieu jeune humain !"
  kami "REVEILLE-TOI !"


  call hide_chars from _call_hide_chars_70

  label credits :

    scene black_background
    with dissolve

    ""

    scene credits
    with dissolve

    "Réalisé par : "
    "Antoine"
    "Colin"
    "Eva"
    "Valton"
    "Ylies"

    "Pour les visuels, les crédits sont sur la page https://schizoa.itch.io/ethiquest"

    "Ce jeu a été développé dans le cadre du cours de SHS 'Le jeu vidéo : média natif du numérique' donné à l'EPFL par Yannick Rochat et Selim Krichane"
    "Merci d'avoir joué à notre jeu !"


label post_credits :

    scene black_background
    with dissolve

    ""

    player "Je suis où ?"

    scene room_hero
    with dissolve

    show screen show_char1(boy, 1.0, 1.0, zoom_boy)
    with dissolve

    player "Ah ! Enfin, je retrouve ma chambre."
    player "Toutes ces histoires m'ont vraiment donné mal à la tête. J'espère en être débarassé pour de bon."
    player "J'ai appris plein de truc avec Kamimusubi, mais les deux autres ne savent vraiment pas s'y prendre."

    show screen show_char1(boy_angry, 1.0, 1.0, zoom_boy)
    with dissolve

    player "ILS ONT VOULU ME TUER !!!!"

    show screen show_char1(boy_nervous, 1.0, 1.0, zoom_boy)
    with dissolve

    player "*Soupir*..."

    show screen show_char1(boy, 1.0, 1.0, zoom_boy)
    with dissolve

    player "En tout cas, je suis pas près de les oublier."

    narrateur "Ton téléphone vibre."

    player "Tiens, un message !?"

    hide screen show_char1

    scene phone1
    with dissolve

    "Cher humain,\nJe viens de découvrir cette méthode de communication. C'est très pratique."

    player "C'est Kamimusubi !!!!"

    scene black_background
    with dissolve

    scene phone2
    with dissolve

    "En effet ! ;)"

    player "C'est sur que c'est plus efficace que les cauchemars."

    scene phone3
    with dissolve

    "Je voulais juste te faire un retour sur les points que t'ont rapporté tes choix."

    player "(Des points...)"

    if utilitarisme == 0 and libertarianisme == 1 :

        scene phone4_0_1
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_0_1
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_0_1
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_0_1
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 0 and libertarianisme == 2 :

        scene phone4_0_2
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_0_2
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_0_2
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_0_2
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 0 and libertarianisme == 3 :

        scene phone4_0_3
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_0_3
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_0_3
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_0_3
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 0 and libertarianisme == 4 :

        scene phone4_0_4
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_0_4
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_0_4
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_0_4
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 1 and libertarianisme == 0 :

        scene phone4_1_0
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_1_0
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_1_0
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_1_0
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 1 and libertarianisme == 1 :

        scene phone4_1_1
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_1_1
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_1_1
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_1_1
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 1 and libertarianisme == 2 :

        scene phone4_1_2
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_1_2
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_1_2
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_1_2
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 1 and libertarianisme == 3 :

        scene phone4_1_3
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_1_3
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_1_3
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_1_3
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 1 and libertarianisme == 4 :

        scene phone4_1_4
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_1_4
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_1_4
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_1_4
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 2 and libertarianisme == 0 :

        scene phone4_2_0
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_2_0
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_2_0
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_2_0
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 2 and libertarianisme == 1 :

        scene phone4_2_1
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_2_1
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_2_1
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_2_1
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 2 and libertarianisme == 2 :

        scene phone4_2_2
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_2_2
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_2_2
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_2_2
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 2 and libertarianisme == 3 :

        scene phone4_2_3
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_2_3
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_2_3
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_2_3
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 2 and libertarianisme == 4 :

        scene phone4_2_4
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_2_4
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_2_4
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_2_4
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 3 and libertarianisme == 0 :

        scene phone4_3_0
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_3_0
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_3_0
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_3_0
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 3 and libertarianisme == 1 :

        scene phone4_3_1
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_3_1
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_3_1
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_3_1
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 3 and libertarianisme == 2 :

        scene phone4_3_2
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_3_2
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_3_2
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_3_2
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 3 and libertarianisme == 3 :

        scene phone4_3_3
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_3_3
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_3_3
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_3_3
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 3 and libertarianisme == 4 :

        scene phone4_3_4
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_3_4
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_3_4
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_3_4
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 4 and libertarianisme == 0 :

        scene phone4_4_0
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_4_0
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_4_0
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_4_0
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 4 and libertarianisme == 1 :

        scene phone4_4_1
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_4_1
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_4_1
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_4_1
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 4 and libertarianisme == 2 :

        scene phone4_4_2
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_4_2
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_4_2
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_4_2
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 4 and libertarianisme == 3 :

        scene phone4_4_3
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_4_3
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_4_3
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_4_3
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."

    elif utilitarisme == 4 and libertarianisme == 4 :

        scene phone4_4_4
        with dissolve

        "Au final, tu as obtenu [utilitarisme] points en utilitarisme et [libertarianisme] points en libertarisme."

        scene phone5_4_4
        with dissolve

        "Si jamais tu veux faire d'autres choix et en observer les consequences, n'hésite pas à me contacter."

        scene phone6_4_4
        with dissolve

        "Je te laisse. J'ai encore perdu de vue Jiyu et Shiawase. A la prochaine ! *dragon*"

        scene phone7_4_4
        with dissolve

        "Je viens de découvrir les smileys !!! *smiley*"

        player "..."


    scene room_hero
    with dissolve

    show screen show_char1(boy, 1.0, 1.0, zoom_boy)
    with dissolve

    player "..."

    show screen show_char1(boy_happy, 1.0, 1.0, zoom_boy)
    with dissolve

    player "Kamimusubi m'envoie des émojis maintenant !!!!"
    player "Faut absolument que je raconte ça à Emma !"

    hide screen show_char1
    with dissolve

    ""

    scene fin
    with dissolve

    ""

    return




label hide_chars:

  hide screen show_char
  hide screen show_char1
  hide screen show_char2
  hide screen show_char3
  hide screen show_char_pos
  hide screen show_char_pos1
  hide screen show_char_pos2
  hide screen show_char_pos3
  with dissolve

  return

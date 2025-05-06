# Forgotten Hero.py
# Bansari Patel

# Forgotten Hero is a side-scroller game that has 2 levels. The objective of
# the levels are to make it to the end with the the highest score possible.
# The game has both boxes and chests that hold weapons and prizes that increase  your
# score and the weapon you're holding, while you are trying to reach the end
# there are spikes in the path and enemies who will keep following you if you don't kill them


from pygame import *
from random import *

screen=display.set_mode((1090,700))
init()

def play():

    level = 0

    #----------------------------IMAGES----------------------------

    backPics = ["back_layers_bbb.png","back_2.png"]
    backPic_one = image.load(backPics[level])
    backPic_one = backPic_one.convert()

    num = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    tile_img = [image.load("tiles/stone block.png"),image.load("tiles/grass_top.png"), image.load("tiles/grass_l.png"),
                image.load("tiles/grass_r.png"), image.load("tiles/grass_cornerr.png"), image.load("tiles/grass_cornerl.png"),
                image.load("tiles/dirt.png"), image.load("tiles/bar_1.png"), image.load('tiles/grass_cornerbl.png'),
                image.load("tiles/grass_cornerbr.png"),image.load("tiles/grass_bottom.png"),
                image.load("tiles/spikes.png"),
                image.load("tiles/twig.png"),
                image.load("tiles/tree_01.png"), image.load("tiles/tree_02.png")
                ]

    hel = ['h','f','e']
    health = [image.load("life/health.png"), image.load("life/full_heart.png"),image.load("life/empty_heart.png")]
    c_closed = image.load("tiles/closed_chest.png")
    c_open = image.load("tiles/open_chest.png")
    weapon_images = [image.load("life/w_0.png"),image.load("life/w_1.png"),image.load("life/w_2.png"),image.load("life/w_3.png"),image.load("life/weapon_holderrr.png")]
    chest_weap = [image.load("life/w_4.png"),image.load("life/w_5.png"),image.load("life/w_6.png"),image.load("life/w_7.png")]
    box_images = [image.load("life/healer.png"),image.load("life/score_0.png"),image.load("life/score_1.png"),image.load("life/box.png")]

    score_img = image.load("life/score.png")
    level_back = image.load('level_back.png')

    #--------------------------------FRAME/TYPE Positsions-------------------------------

    # positoins for the the players moves

    STANDR = 0
    STANDL = 1
    THROWR = 2
    THROWL = 3
    RIGHT = 4
    LEFT = 5
    UPR = 6
    UPL = 7
    DEATHR = 8
    DEATHL = 9
    DAMR = 10
    DAML = 11
    DAM_THROWR = 12
    DAM_THROWL = 13
    DAM_RIGHT = 14
    DAM_LEFT = 15
    DAM_UPR = 16
    DAM_UPL = 17

    # positions for the player list
    X = 0
    Y = 1
    MOVE = 2
    FRAME = 3
    VX = 4
    VY = 5
    FACING = 6
    GROUND = 7
    DEATH = 8
    COLLIDE_BAD = 9

    # positions for the weapon list
    WX = 0
    WY = 1
    WTYPE = 2
    WFRAME = 3
    WVX = 4
    WVY = 5
    WDAMAGE = 6
    WFACING = 7
    WL = 8
    WW = 9

    # positoins for the shot list
    SX = 0
    SY = 1
    STYPE = 2
    SFRAME = 3

    # positions for the player's rect sides in the list 'collide_spot'

    top_rect = 0
    left_rect = 1
    right_rect = 2
    bottom_rect = 3
    collide_spot=[0,0,0,0]

    starts = [(150,360),(50,0)]         # The player's starting position depending on the level

    def moveFighter(main,lives,life_timer):

        keys =  key.get_pressed()

        if main[DEATH] == False and END == False:       # To change the players facing for when it's image is beeing blitted
            if keys[K_RIGHT] and main[FACING]<1:
                main[FACING] +=1
            elif keys[K_LEFT] and main[FACING]>0:
                main[FACING] -=1

            if keys[K_RIGHT] or keys[K_LEFT] or keys[K_UP] or keys[K_SPACE]:        # If player is not standing
                if keys[K_RIGHT]:
                    main[VX] = 10
                    main[X] += main[VX]

                    if main[GROUND] == True :
                        if life_timer <=70:         # if the player is damaged the move will be from it's damaged collection
                            main[MOVE] = DAM_RIGHT
                        else:
                            main[MOVE] = RIGHT      # if the player is not damaged the normal right facing sprite will be chosen
                    else:                           # This is repeated
                        if life_timer <=70 :
                            main[MOVE] = DAM_UPR
                        else:
                            main[MOVE] = UPR
                    if keys[K_UP]:
                        if life_timer <=70 :
                            main[MOVE] = DAM_UPR
                        else:
                            main[MOVE] = UPR

                elif keys[K_LEFT] and main[X]>0:
                    main[VX] = -10
                    main[X] += main[VX]

                    if main[GROUND] == True:
                        if life_timer <=70 :
                            main[MOVE] = DAM_LEFT
                        else:
                            main[MOVE] = LEFT
                    else:
                        if life_timer <=70 :
                            main[MOVE] = DAM_UPL
                        else:
                            main[MOVE] = UPL

                    if keys[K_UP]:
                        if life_timer <=70 :
                            main[MOVE] = DAM_THROWL
                        else:
                            main[MOVE] = UPL

                else:
                    main[VX] = 0

                if keys[K_UP] and main[GROUND] == True:
                    main[VY] = -17
                    main[GROUND] = False

                if keys[K_SPACE]:
                    if main[FACING] == 0:
                        if life_timer <=70 :
                            main[MOVE] = DAM_THROWL
                        else:
                            main[MOVE] = THROWL # right facinf throw
                    if main[FACING] == 1:
                        if life_timer <=70 :
                            main[MOVE] = DAM_THROWR
                        else:
                            main[MOVE] = THROWR # left facing throw

            else:
                if main[FACING] == 0:
                    if life_timer <=70 :
                        main[MOVE] = DAML
                    else:
                        main[MOVE] = STANDL #standing facing right

                elif main[FACING] == 1:
                    if life_timer <=70 :
                        main[MOVE] = DAMR
                    else:
                        main[MOVE] = STANDR #standing facing the left


            if main[GROUND] == False and main[MOVE]!= THROWL and main[MOVE]!= THROWR:
                if main[FACING] == 0:
                    if life_timer <=70 :
                        main[MOVE] = DAM_UPL
                    else:
                        main[MOVE] =  UPL # right facing jump
                if main[FACING] == 1:
                    if life_timer <=70 :
                        main[MOVE] = DAM_UPR
                    else:
                        main[MOVE] = UPR #left main[FACING] jump

        main[Y]+= main[VY]          # gravity is added
        main[VY]+=1.5

        main[FRAME] = main[FRAME] + .3
        if main[FRAME] >= len(mainPics[main[MOVE]]):
            if main[DEATH] == False:        #sprite will repeat unless it is dead
                main[FRAME] = 0
            else:
                main[FRAME] = 4

    #============================Weapon================================


    def weapontype(weapon, main):

        keys =  key.get_pressed()
        for shot in shots:
            shot[3] = shot[3] + .4
            if shot[3] >= len(weapPics[shot[2] +shot[7]]):      # It's facing is added because thats the position the the changed direction of the weapon in in the weapon pics list
                shot[3] = 0


        weapon_damage = [1,3,2,1,2]
        weapon_vx = [12,14,15,13,9]
        weapon_vy = [0,0,-7,-3]
        weapon_length = [24,33,14,32]
        weapon_width = [9,24,14,10]

        pos = weapon[WTYPE]//2

        weapon[WDAMAGE] = weapon_damage[pos]        # Assigns the weapon it's properties according to the type lists
        weapon[WVX] = weapon_vx[pos]
        weapon[WL] = weapon_length[pos]
        weapon[WW] = weapon_width[pos]
        weapon[WFACING] = main[FACING]
        weapon[WVY] = weapon_vy[pos]

    def moveWeapon(weapon, main):

        weapon[0] = main[0]+24      # changes starting position so it comes form the middle of teh player
        weapon[1] = main[1]+20

        for shot in shots:
            if shot[WTYPE] == 4:
                shot[WY] += shot[WVY]       # gravity is added to this certain weapon
                shot[WVY] += 1.5

            if shot[WTYPE] == 6:            # reverse gravity is added to this certain weapon
                if shot[WVY] >-30:
                    shot[WY] += shot[WVY]

            if shot[7] == 0:
                shot[0] -= shot[4]          # if the facing is a 0 then velocity x is subtracted

            else:
                shot[0] += shot[4]          # if the facing is a 0 then velocity x is added

        for rec in shot_rects:
            for shot in shots:
                rec[0] = shot[0]            # so each shot has a rect that follows it to check for collisions
                rec[1] = shot[1]

    def shot_collide(shot_rects, tile_rects, bar_rects,shots, hits_c, all_enemies, trigger_spots,speeds,score):

        for tile in tile_rects:
            for rec in shot_rects:
                if rec.colliderect(tile):
                    hit = shot_rects.index(rec)
                    hits_c[0] = shot_rects[hit][0]
                    hits_c[1] = shot_rects[hit][1]
                    hits[2] = GRASS             # for the dirt affect when shot hits tiles

                    shots.remove(shots[hit])
                    shot_hit.append(hits_c)
                    shot_rects.remove(shot_rects[hit])

                if rec[0]> 5000 or rec[0]< -10:     # if the shot is out of range it is removed form list
                    out = shot_rects.index(rec)
                    if len(shots)>0:
                        shots.remove(shots[out])
                        shot_rects.remove(shot_rects[out])

        for bad in all_enemies:

            if bad[EY]>=750:        # if enemy falls it is considered ded and deleted
                enem = all_enemies.index(bad)
                trigger_spots.remove(trigger_spots[enem])
                speeds.remove(speeds[enem])
                all_enemies.remove(all_enemies[enem])

            for rec in shot_rects:
                enemy_rec = Rect(bad[EX], bad[EY], bad[ELEN], bad[EWID])

                if rec.colliderect(enemy_rec):
                    hit = shot_rects.index(rec)
                    hits_c[0] = shot_rects[hit][0]
                    hits_c[1] = shot_rects[hit][1]

                    enem = all_enemies.index(bad)

                    if bad[EHEALTH] >=0:        # if the shot hits an enemy, the enemy's health will decrease by the weapons power until the enemy hs no more health
                        bad[EHEALTH] -= shots[hit][WDAMAGE]

                    if bad[EHEALTH] < 0 :
                        trigger_spots.remove(trigger_spots[enem])
                        speeds.remove(speeds[enem])
                        score[0]+=bad[ESCORE]
                        all_enemies.remove(all_enemies[enem])

                    if len(shots)>0:
                        shots.remove(shots[hit])
                        shot_rects.remove(shot_rects[hit])

        for h in shot_hit:
            h[3] = h[3] + .4
            if h[3] >= len(shotPics[h[2]]):
                h[3] = 0
                shot_hit.remove(h)      # the shot is deleted after the after affects of teh dust id blitted

    #================================================================================================================

    def collide_spots(collide_spot,main, tile_rects, bar_rects,chest_rects, all_chests,weapon,all_boxes,box_rects,score,lives):

            collide_spot[top_rect] = Rect(main[X],main[Y],42,1)         # rectngles for all sides of player
            collide_spot[left_rect] = Rect(main[X],main[Y]+15,1,30)
            collide_spot[right_rect] = Rect(main[X]+42,main[Y]+15,1,30)
            collide_spot[bottom_rect] = Rect(main[X]+8,main[Y]+60,30,1)

            collision_types = {'top':False,'left':False,'right':False,'bottom':False}

            for tile in tile_rects:
                if collide_spot[top_rect].colliderect(tile):        # checks collisions for player
                    collision_types['top'] = True
                    main[VY] = 5
                if collide_spot[left_rect].colliderect(tile):
                    collision_types['left'] = True
                    main[X] = tile.x + 36
                if collide_spot[right_rect].colliderect(tile):
                    collision_types['right'] = True
                    main[X] = tile.x - 42
                if collide_spot[bottom_rect].colliderect(tile):
                    collision_types['bottom'] = True
                    if main[VY]>0:
                        main[GROUND] = True
                        main[VY] = 0
                        main[Y] = tile.y - 60
                if collide_spot[left_rect].colliderect(tile):
                    main[VX] = 10

            for bar in bar_rects:                           # checks collisions for player
                if collide_spot[bottom_rect].colliderect(bar):
                    collision_types['bottom']  = True
                    if main[VY]>0:
                        main[GROUND] = True
                        main[VY] = 0
                        main[Y] = bar.y - 60

            main_rect = Rect(main[X],main[Y],42,62)

            for c in all_chests:
                for chest in chest_rects:

                    if c[COPEN] == True and chest_rects.index(chest) == all_chests.index(c):        # If the chest is open but the item is not take
                        if main_rect.colliderect(chest) and c[CTAKEN] == False:
                            c[CTAKEN],weapon[WTYPE]= True,c[CTYPE]          # the current weapon is changed to teh one that is in the chest and teh score is added on
                            score[0]+=c[CSCORE]
                            c[CSCORE] = 0

                    if c[COPEN] == False and chest_rects.index(chest) == all_chests.index(c):       # if the chest is closed you can't go through it
                        if collide_spot[left_rect].colliderect(chest):
                            collision_types['left'] = True
                            main[X] = chest.x + 53
                        if collide_spot[right_rect].colliderect(chest):
                            collision_types['right'] = True
                            main[X] = chest.x - 53
                        if collide_spot[bottom_rect].colliderect(chest):
                            collision_types['bottom'] = True
                            if main[VY]>0:
                                main[GROUND] = True
                                main[VY] = 0
                                main[Y] = chest.y - 60

            for box in all_boxes:
                for rec in box_rects:
                    if box[BOPEN] == True and box_rects.index(rec) == all_boxes.index(box) and main_rect.colliderect(rec):      #if box is open but the item is not take
                        if box[BTYPE] == 0 and 0 in lives and box[BTAKEN] == False:         # if the item is teh health elixer, then a life is added on
                            score[0]+=box[BSCORE]
                            box[BSCORE] = 0
                            box[BTAKEN] = True
                            if 0 in lives:
                                lives.reverse()
                                zero_pos = lives.index(0)
                                lives[zero_pos] = 1
                                lives.reverse()
                                break

                        if box[BTYPE]!= 0 and box[BTAKEN] == False:
                            score[0]+=box[BSCORE]
                            box[BSCORE] = 0
                            box[BTAKEN] = True

                    if box[BOPEN] == False and box_rects.index(rec) == all_boxes.index(box):        # If the box is not opened the player can't go through it
                        if collide_spot[left_rect].colliderect(rec):
                            collision_types['left'] = True
                            main[X] = rec.x + 53
                        if collide_spot[right_rect].colliderect(rec):
                            collision_types['right'] = True
                            main[X] = rec.x - 53
                        if collide_spot[bottom_rect].colliderect(rec):
                            collision_types['bottom'] = True
                            if main[VY]>0:
                                main[GROUND] = True
                                main[VY] = 0
                                main[Y] = rec.y - 60

    def score_boost(lives,score):
        if score[0] >=5000 and score[0]<6000:       # if the score reaches 5000, an extra life will be added on for the plaer
            lives.reverse()
            lives.append(0)
            score[0]+=1000
            lives.reverse()

    #============================MAKE MOVES/SPRITES==================================

    def makeMove(name,start,end):
        move = []
        for i in range(start,end+1):
            move.append(image.load("%s/%s%03d.png" % (name,name,i)))
        return move

    def makeWeapon(name,start,end):
        weap = []
        for i in range(start,end+1):
            weap.append(image.load("%s/%s%03d.png" % (name,name,i)))
        return weap

    def makeSpark(name,start,end):
        spark = []
        for i in range(start,end+1):
            spark.append(image.load("%s/%s%03d.png" % (name,name,i)))
        return spark

    def makeEnemy(name,start,end):
        baddies = []
        for i in range(start,end+1):
            baddies.append(image.load("%s/%s%03d.png" % (name,name,i)))
        return baddies
#-------------------------------------------------------------------------------

    def load_map(path):
        f = open(path + '.txt','r')     # takes in notes file and makes each number into a string and makes a 2D list according to each row
        data = f.read()
        f.close()
        data = data.split('\n')
        game_map = []
        for row in data:
            game_map.append(list(row))
        #print(game_map)
        return game_map

    maps = ['map1','map2']
    game_map = load_map(maps[level])

    def fall(main, lives):
        heart_pos = 0           #if teh player falls past a certain point, damage is given
        for i in lives:
            if i == 1 :
                heart_pos = lives.index(i)

        if main[Y] >=750:
            lives[heart_pos] = 0

            if 1 in lives:
                main[X],main[Y] = 150,360
                main[DEATH] = False


    def Death(main, lives):
        if 1 not in lives:
            main[DEATH] = True
        else:
            main[DEATH] = False

        if main[DEATH] == True:
            if main[FACING] == 1:
                main[MOVE] = DEATHR
            if main[FACING] == 0:
                main[MOVE] = DEATHL

    #===============================================ENEMIES====================================================

    enemy = [500,0,0,0,0,1,0,0,0,0,33,58,0,0,0,450] #[x,y,vx,vy,damage, health, left_rect,right,top,bottom,length,width, type, frame,facing]
    EX = 0
    EY = 1
    EVX = 2
    EVY = 3
    EDAMAGE = 4
    EHEALTH = 5
    EL = 6
    ER = 7
    ET = 8
    EB = 9
    ELEN = 10
    EWID = 11
    ETYPE = 12
    EFRAME = 13
    EFACING = 14
    ESCORE = 15

    enemy_exes = [[1200,2000,3000,3000],[700,2082,3414,4100]]       # enemie x locations when spawned
    all_speeds = [[5,5,5,6],[5,5,5,5]]
    speeds = all_speeds[level]
    all_triggers = [[401,1100,2000,2350],[200,1770,2920,3600]]      # the x locations the player has to pass in order for the enemy's VX to be triggered
    trigger_spots = all_triggers[level]

    def spawn(enemy,main,all_enemies,enemy_exes,speeds, trigger_spots):
        en_x = enemy_exes[level]
        for new_x in en_x:
            x_pos = en_x.index(new_x)       # enemy attributes are being added on
            enemy[EX] = en_x[0]

            if enemy[EX] == 5:
                enemy[ETYPE] = 0

            enemy_c = enemy.copy()

            if len(en_x) > 0:
                all_enemies.append(enemy_c)
                en_x.remove(en_x[0])

        for trigger in trigger_spots:
            if main[X] >=trigger and len(all_enemies)>0:        # if the enemy is triggered it's speed increased
                x_pos = trigger_spots.index(trigger)
                all_enemies[x_pos][EVX] = speeds[x_pos]
                if all_enemies[x_pos][EVX] ==6:
                    all_enemies[x_pos][EDAMAGE] = 0

        for bad in all_enemies:
            bad[EFRAME] = bad[EFRAME] + .4
            if bad[EFRAME] >= len(enemyPics[bad[ETYPE] + bad[EFACING]]):
                if bad[EVX] !=0:
                    bad[EFRAME] = 0
                else:
                    bad[EFRAME] = 10


    def enemy_collide(tile_rects,all_enemies,life_timer,main):

        for bad in all_enemies:

            bad[EY] += bad[EVY]
            bad[EVY] +=1.5          #gravity is added for each enemy

            bad[EL] = Rect(bad[EX],bad[EY]+10,1,bad[EWID]-15)
            bad[ER] = Rect(bad[EX]+bad[ELEN],bad[EY]+10,1,bad[EWID]-15)
            bad[EB] = Rect(bad[EX]+3,bad[EY]+bad[EWID],bad[ELEN]-6,1)
            bad[ET] = Rect(bad[EX],bad[EY],bad[ELEN]+3,1)

            for tile in tile_rects:
                if bad[EB].colliderect(tile):       #checks for collisions and moves enemy accordingly
                    if bad[EVY]>0:
                        bad[EVY] = 0
                        bad[EY] = tile.y - 60

                if bad[EL].colliderect(tile) or bad[ER].colliderect(tile):
                    bad[EVY] = -12
                if life_timer%20 == 0 and main[DEATH] == True:      # the enemies jump when the player dies
                    bad[EVY] = -12
                if bad[ET].colliderect(tile):
                    bad[EVY] = 5

    def bad_damage(main, all_enemies, life_timer,spike_rects):

        main[COLLIDE_BAD] = False
        mainRect = Rect(main[X],main[Y], 42,62)
        heart_pos = 0

        for i in lives:
            if i == 1 :
                heart_pos = lives.index(i)

        for bad in all_enemies:
            dx = main[X] - bad[EX]
            if dx > 0 and main[COLLIDE_BAD] == False:
                bad[EFACING] = 0
                bad[X]+= bad[EVX]
            if dx < 0 and main[COLLIDE_BAD] == False:
                 bad[0] -= bad[2]
                 bad[EFACING] = 1

            enemy_rec = Rect(bad[EX], bad[EY], bad[ELEN], bad[EWID])

            if enemy_rec.colliderect(mainRect) and main[DEATH] == False:
                main[COLLIDE_BAD] = True
                if life_timer>=70:
                    lives[heart_pos] = 0        # player is pushed back when damaged
                    if dx > 0:
                        main[X]+=50
                    if dx < 0:
                        main[X]-=50

        for spike in spike_rects:
            top_rec = Rect(spike[0]+10,spike[1],spike[2],1)
            if collide_spot[bottom_rect].colliderect(top_rec):          # the spikes give damage when the players bottom interacts with it
                main[COLLIDE_BAD] = True
                if life_timer>=70:
                    lives[heart_pos] = 0
                    if main[DEATH] == False:
                        main[Y]-=40

#=========================================CHESTS/BOX==========================================

    chest = [0,0,53,38,-1,False,False,250] #x,y,l,w,type,open,taken,score
    chest_rects = []
    all_chests = []

    all_xchest_points = [[2424,3464],[680,2548]]
    all_ychest_points = [[540,187],[445,475]]

    xchest_points = all_xchest_points[level]
    ychest_points = all_ychest_points[level]

    CX = 0
    CY = 1
    CL = 2
    CW = 3
    CTYPE = 4
    COPEN = 5
    CTAKEN = 6
    CSCORE = 7

    def spawn_chests(chest, all_chests, chest_rects,shot_rects,main, xchest_points,ychest_points):

        random_weapon = [0,2,2,4,4,6]       # weapon types for teh chests are picked at random

        for x in xchest_points:

            chest[CX], chest[CY] = xchest_points[0],ychest_points[0]        # chest properties are added
            chest[CTYPE] = choice(random_weapon)

            chest_c = chest.copy()

            if len(xchest_points)>0:
                all_chests.append(chest_c)
                chest_rects.append(Rect(chest_c[CX],chest_c[CY],chest_c[CL],chest_c[CW]))

                xchest_points.remove(xchest_points[0])
                ychest_points.remove(ychest_points[0])

        for shot in shot_rects:
            for chest in chest_rects:
                if shot.colliderect(chest):
                    chest_pos = chest_rects.index(chest)
                    all_chests[chest_pos][COPEN] = True         # if the chest is hit, the contents can be taken

    #----


    box = [0,0,45,45,-1,False,False,0]
    box_rects = []
    all_boxes =[]

    all_xbox_points = [[64,1332,1695,2707,3793],[25,865,1891,2266,3157,4605]]
    all_ybox_points = [[405,565,372,277,370],[502,435,470,470,280,500]]

    xbox_points = all_xbox_points[level]
    ybox_points = all_ybox_points[level]
    score = [0]

    BX = 0
    BY = 1
    BL = 2
    BW = 3
    BTYPE = 4
    BOPEN = 5
    BTAKEN = 6
    BSCORE = 7


    def spawn_boxs(box,all_boxes,box_rects,shot_rects,main,xbox_points,ybox_points,score):

        rand_prize = [0,1,2]        # chest component posibiliies

        for x in xbox_points:
            box[BX],box[BY] = xbox_points[0],ybox_points[0]         #box properties are added
            box[BTYPE] = choice(rand_prize)

            if box[BTYPE] == 0:
                box[BSCORE] = 1000
            elif box[BTYPE] == 1:
                box[BSCORE] = 500
            elif box[BTYPE] == 2:
                box[BSCORE] = 500

            box_c = box.copy()

            if len(xbox_points)>0:          # all boxes that hold important values are added to all_boxes list
                all_boxes.append(box_c)
                box_rects.append(Rect(box_c[BX],box_c[BY],box_c[BL],box_c[BW]))

                xbox_points.remove(xbox_points[0])
                ybox_points.remove(ybox_points[0])

        for shot in shot_rects:
            for box in box_rects:
                if shot.colliderect(box):
                    box_pos = box_rects.index(box)
                    all_boxes[box_pos][BOPEN] = True        # if a shot hits the box, then the items are now attainable

    #===================================DRAW==========================================
    def drawScene(screen,main,game_map,shots,all_enemies,all_chests,score):

        move = main[MOVE]
        frame = int(main[FRAME])
        pic = mainPics[move][frame]

        back = [(60,28,36),(13,6,18)]
        screen.fill(back[level])

        screen.blit(backPic_one,(0-scroll[0],-200-scroll[1]))

        y = 0
        for layer in game_map:
            x = 0
            for tile in layer:          #each item in the game_map holds certain properties of rectangles and are blitted accordingly

                if tile != '0':
                    screen.blit(tile_img[num.index(tile)],(x*32-scroll[0], y*32-scroll[1]))
                if tile!= '0' and tile!= '8' and tile!= 'd'and tile!= 'e'and tile!= 'f':
                    square = Rect(x*32,y*32,32,32)
                    if square not in tile_rects:
                        tile_rects.append(square)
                if tile == 'c':
                    spike = Rect(x*32,y*32,45,45)
                    if spike not in spike_rects:
                        spike_rects.append(spike)
                if tile == '8':
                    b = Rect(x*32,y*32,64,16)
                    if b not in bar_rects:
                        bar_rects.append(b)
                x += 1
            y += 1

        if main[DEATH]==False:
            screen.blit(pic,(main[X] - scroll[0], main[Y] - scroll[1]))
        else:
            screen.blit(pic,(main[X]- scroll[0], main[Y]+12 - scroll[1]))

        for chest in all_chests:        # chest with different conditions are drawn
            if chest[COPEN] == False:
                screen.blit(c_closed,(chest[0]-scroll[0],chest[1]-scroll[1]))
            else:
                screen.blit(c_open,(chest[0]-scroll[0],chest[1]-scroll[1]))
                if chest[CTAKEN] == False and chest[COPEN] == True:
                    screen.blit(chest_weap[chest[CTYPE]//2],(chest[0]-scroll[0],chest[1]-25-scroll[1]))

        for box in all_boxes:           #boxes with different conditions are drawn, according if the item is taken or not etc.
            if box[BOPEN] == False:
                screen.blit(box_images[-1],(box[0]-scroll[0],box[1]-scroll[1]))
            else:
                if box[BTAKEN] == False and box[BOPEN] == True:
                    screen.blit(box_images[box[BTYPE]],(box[0]-scroll[0],box[1]+5-scroll[1]))

        for bad in all_enemies:
            etype = bad[ETYPE]          #draws all enemies while in the list
            eframe = int(bad[EFRAME])
            epic = enemyPics[etype+bad[EFACING]][eframe]
            screen.blit(epic,(bad[EX]-scroll[0],bad[EY]-scroll[1]))

        for shot in shots:
            wtype = shot[2]
            wframe = int(shot[3])   #draws all the shots taken
            wpic = weapPics[wtype+shot[7]][wframe]
            screen.blit(wpic,( shot[0] - scroll[0], shot[1] - scroll[1]))

        for spark in shot_hit:      # draws the dust cloud tht appears after a shot hits a tile
            stype = spark[2]
            sframe = int(spark[3])
            spic = shotPics[stype][sframe]
            screen.blit(spic, (spark[0]-scroll[0], spark[1] - scroll[1]))

    #-----------blits top headers in game -------
        screen.blit(health[0],(35,25))
        screen.blit(weapon_images[-1],(500,25))
        screen.blit(score_img,(960,25))
        screen.blit(weapon_images[weapon[WTYPE]//2],(539,67))

        lives_c = lives.copy()
        lives_c.reverse()

        x = 34
        for h in lives_c:       # the lives are drawn in reverse so that when player is damaged a life is taken starting from the end
            if h == 1:
                screen.blit(health[1], (x,60))
            if h ==0:
                screen.blit(health[2], (x,60))
            x+= 45

        score_f = font.Font("score_font.ttf",35)
        score_font = score_f.render((str(score[0])),False,(192,190,190))        # the score is drawn and according to the digit size its in a different spot

        if score[0]>=1000 and score[0]<=10000:
            screen.blit(score_font,(935,65))
        elif score[0] == 0:
            screen.blit(score_font,(988,65))
        elif score[0] >=10000:
            screen.blit(score_font,(910,65))
        else:
            screen.blit(score_font,(956,65))

        level_font = font.Font("title.ttf",45)
        level_quotes = ['Nice Job Hero!','Great Job, You Made it!']
        level_q = level_font.render((level_quotes[level]),False,(192,190,190))

        if END == True:
            screen.blit(level_back,(350,200))       #if player reaches to end they have the option to continue
            if level == 0:
                screen.blit(level_q,(450,250))
            else:
                screen.blit(level_q,(370,250))
            draw.rect(screen,(192,190,190),con_rect)
            screen.blit(continue_text,(505,358))

        fail_text = level_font.render(("Uh - Oh  You  Died"),False,(192,190,190))
        restart_text = continue_font.render(('Restart'),False,(18,18,18))
        restart_rect = Rect(485,350,170,50)

        if main[DEATH] == True:             #message is written if player dies
            screen.blit(level_back,(350,200))
            screen.blit(fail_text,(425,250))
            draw.rect(screen,(192,190,190),restart_rect)
            screen.blit(restart_text,(523,355))

        display.flip()

    #=================================================================================================

    mainPics = []
    mainPics.append(makeMove('main',1,4))
    mainPics.append(makeMove('main',5,8))
    mainPics.append(makeMove('main',9,12))
    mainPics.append(makeMove('main',13,16))
    mainPics.append(makeMove('main',17,22))
    mainPics.append(makeMove('main',23,28))
    mainPics.append(makeMove('main',30,30))
    mainPics.append(makeMove('main',33,33))
    mainPics.append(makeMove('main',35,39))
    mainPics.append(makeMove('main',40,44))
    mainPics.append(makeMove('main_dam',1,2))
    mainPics.append(makeMove('main_dam',3,4))
    mainPics.append(makeMove('main_dam',5,8))
    mainPics.append(makeMove('main_dam',9,12))
    mainPics.append(makeMove('main_dam',13,17))
    mainPics.append(makeMove('main_dam',18,22))
    mainPics.append(makeMove('main_dam',23,25))
    mainPics.append(makeMove('main_dam',26,28))


    # weapon type

    weapPics = []
    weapPics.append(makeWeapon('weapon',1,1))
    weapPics.append(makeWeapon('weapon',2,2))
    weapPics.append(makeWeapon('weapon',3,6))
    weapPics.append(makeWeapon('weapon',7,10))
    weapPics.append(makeWeapon('weapon',11,11))
    weapPics.append(makeWeapon('weapon',11,11))
    weapPics.append(makeWeapon('weapon',13,13))
    weapPics.append(makeWeapon('weapon',12,12))

    GRASS = 0
    ##STONE = 1

    shotPics = []
    shotPics.append(makeSpark('dust',1,5))
    shotPics.append(makeSpark('dust',6,10))


    #enemy

    BAD_1R = 0
    BAD_1L = 1

    enemyPics = []
    enemyPics.append(makeEnemy('bad',0,11))
    enemyPics.append(makeEnemy('bad',12,23))

    #==========================================================================================

    running = True
    myClock = time.Clock()

    main = [150,360,0,0,0,0,1,0,0,0] #[x,y,move,frame,vx,vy,facing, ground, death, collisions]
    weapon=[550,100,0,0,0,0,0,0,0,0]#[x,y,type,frame,vx,vy,damage, facing, l,w]

    all_enemies = []
    lives = [1,1,1]

    hits = [0,0,0,0]
    shot_hit = []


    true_scroll = [0,0]     #position of scroll

    tile_rects = []
    bar_rects = []
    spike_rects = []


    shots = []
    shot_rects = []
    shoot_timer = 15

    life_timer = 70

    sec = 0

    enemy_rec = []

    END = False


    level_font = font.Font("title.ttf",45)
    level_quotes = ['Nice Job Hero!','Congradulations You Won !!']
    level_q = level_font.render((level_quotes[level]),False,(192,190,190))

    continue_font = font.Font("sub_font.ttf",35)
    continue_text = continue_font.render(('Continue'),False,(18,18,18))
    con_rect = Rect(485,350,170,50)


    fail_text = level_font.render(("Uh-Oh You Died"),False,(192,190,190))
    restart_text = continue_font.render(('Restart'),False,(18,18,18))
    restart_rect = Rect(485,350,170,50)

    while running:

        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
            elif evnt.type == KEYDOWN and evnt.key == K_ESCAPE:
                running = False

            if evnt.type == KEYUP and evnt.key == K_SPACE and shoot_timer >=15 and main[DEATH] == False :
                shots.append(weapon_c)              # if the shoot timer was larger than 15 the shot would be added to the list
                shot_rects.append(Rect(weapon_c[0],weapon_c[1],weapon_c[8],weapon_c[9]))
                shoot_timer = 0         #shot_timer reset

        keys =  key.get_pressed()

        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()

        true_scroll[0] += (main[X]-true_scroll[0]-540)/10       #scroll followed the player while haing it positioned in the middle

        if main[X]>=5350:
            END = True

            if level == 1 and END == True:
                return "Won"

            elif END == True and con_rect.collidepoint(mx,my) and mb[0] == 1:       # conditions applied to changed to level 2
                level+=1
                cx,cy = starts[level][0],starts[level][1]
                main[X],main[Y] = cx,cy
                game_map = load_map(maps[level])
                backPic_one = image.load(backPics[level])
                backPic_one = backPic_one.convert()
                spike_rects.clear()
                bar_rects.clear()
                tile_rects.clear()
                trigger_spots = all_triggers[level]
                speeds = all_speeds[level]
                box_rects.clear()
                all_boxes.clear()
                chest_rects.clear()
                all_chests.clear()

                xchest_points = all_xchest_points[level]
                ychest_points = all_ychest_points[level]

                xbox_points = all_xbox_points[level]
                ybox_points = all_ybox_points[level]
                END = False

        if main[DEATH] == True and restart_rect.collidepoint(mx,my) and mb[0]==1:       # if player dies
                cx,cy = starts[level]
                main[X],main[Y] = cx,cy
                score[0] = 0
                lives = [1,1,1]
                main[DEATH] = False


        if true_scroll[0]<0:        # scroll would stop moving if it is at the start
            true_scroll[0] = 0
        if true_scroll[0] >=4250:   # scroll would stop moving if it is at end
            true_scroll[0] = 4250

        true_scroll[1] += (main[Y]-true_scroll[1]-381)/20 # divided by 20 to give it a delayed effect

        if true_scroll[1]>35:       # only panes up if player is above a certain level
            true_scroll[1] = 35

        scroll = true_scroll.copy()
        scroll[0] = int(true_scroll[0])
        scroll[1] = int(true_scroll[1])


        if main[DEATH] == True and sec < 30:    # screen shakes when player dies
            sec += 1
            scroll[0] += randint(0,8) - 4
            scroll[1] += randint(0,8) - 4

        if main[COLLIDE_BAD] == True and life_timer>=65 and main[DEATH] == False:       # screen shakes when damaged
            scroll[0] += randint(0,8) - 4
            scroll[1] += randint(0,8) - 4


        hits_c = hits.copy()
        weapon_c = weapon.copy()

        shoot_timer += 1

        if life_timer >=70 and main[COLLIDE_BAD] == True:       # timer so that player can't repeatedly get damaged
            life_timer = 0
        life_timer +=1

        weapontype(weapon, main)
        moveFighter(main,lives,life_timer)
        drawScene(screen,main,game_map,shots,all_enemies,all_chests,score)
        collide_spots(collide_spot,main, tile_rects, bar_rects,chest_rects,all_chests,weapon,all_boxes,box_rects,score,lives)
        moveWeapon(weapon, main)
        shot_collide(shot_rects, tile_rects, bar_rects, shots, hits_c, all_enemies,trigger_spots,speeds,score)
        fall(main, lives)
        bad_damage (main, all_enemies,life_timer,spike_rects )
        Death(main, lives)
        spawn(enemy,main,all_enemies,enemy_exes,speeds,trigger_spots)
        enemy_collide(tile_rects,all_enemies,life_timer,main)
        spawn_chests(chest, all_chests, chest_rects,shot_rects,main,xchest_points,ychest_points)
        spawn_boxs(box,all_boxes,box_rects,shot_rects,main,xbox_points,ybox_points,score)
        score_boost(lives,score)

        myClock.tick(60)

    return "Menu"

#---------------------------------------------------------
menu_back = image.load("menu_back.png")
def menu():
    running = True
    myClock = time.Clock()
    buttons = [Rect(465,y*100+250, 150, 55) for y in range(3)]
    button_text = ['Play','Instructions','Credits']
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                return "Exit"
        mpos = mouse.get_pos()
        mb = mouse.get_pressed()

        screen.blit(menu_back,(0,0))

        title_font = font.Font("title.ttf",82)
        sub_font = font.Font("sub_font.ttf",38)
        title = title_font.render(('Forgotten Hero'),False,(0,0,0))
        screen.blit(title,(300,100))

        sub_x = [510,455,490]
        for b in buttons:
            draw.line(screen,(0),(465,b[1]),(465+150,b[1]),3)
            draw.line(screen,(0),(465,b[1]+55),(465+150,b[1]+55),3)
            pos = (b[1]-250)//100

            if b.collidepoint(mpos):
                sub_text = sub_font.render((button_text[pos]),False,(255,255,255))
                screen.blit(sub_text,(sub_x[pos],b[1]+8))
                if mb[0]==1:
                    return button_text[pos]
            else:
                sub_text = sub_font.render((button_text[pos]),False,(61,61,61))
                screen.blit(sub_text,(sub_x[pos],b[1]+6))

        display.flip()

#=====================PAGES===================================

def instructions():
    running = True
    background = image.load("instructions.png")
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False
        screen.blit(background,(0,0))
        display.flip()
    return "Menu"       # returns back to menu when exit

def credit():

    running = True
    background = image.load("credits.png")
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False
        screen.blit(background,(0,0))
        display.flip()
    return "Menu"

def won():
    running = True
    background = image.load("won.png")
    while running:
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        if key.get_pressed()[27]: running = False
        screen.blit(background,(0,0))
        display.flip()
    return "Menu"

page = "Menu"

while page != 'Exit':
    if page == "Menu":
        page = menu()

    if page == "Play":
        page = play()

    if page == "Instructions":
        page = instructions()

    if page == 'Credits':
        page = credit()

    if page == "Won":
        page = won()
quit()

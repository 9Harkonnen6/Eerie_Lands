import pygame
import sys
import time
from pygame import mouse
from pygame.constants import MOUSEBUTTONDOWN
from pygame.draw import line
from standard_map_generator import *
from random import choice


# animation loader ----------------------------------------------------------------------------------- #
global animation_frames
def load_animation(path, frame_duration):
    global animation_frames
    animation_name = path.split('/')[-1]
    animation_frame_data = []
    n = 0
    for frame in frame_duration:
        animation_frame_id = animation_name + '_' + str(n)
        image_loc = path + '/' +animation_frame_id + '.png'
        animation_image = pygame.image.load(image_loc).convert_alpha()
        animation_image.set_colorkey((255, 255, 255))
        animation_frames[animation_frame_id] = animation_image.copy()

        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        n += 1

    return animation_frame_data



# window settings ------------------------------------------------------------------------------------- #
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Eerie Lands')
WINDOW_SIZE = (1440, 960)
main_screen = pygame.display.set_mode(size=(0, 0), flags=pygame.FULLSCREEN, depth=0, display=0)
display = pygame.Surface((1440, 960))
gui = pygame.Surface((1440, 960))
scroll = [0, 0]

# TILES ----------------------------------------------------------------------------------------------- #
grass = pygame.image.load('images/tilesets/grass/grass.png').convert()
grass_1 = pygame.image.load('images/tilesets/grass/grass_1.png').convert()
grass_2 = pygame.image.load('images/tilesets/grass/grass_2.png').convert()

corruption = pygame.image.load('images/tilesets/corruption/corruption.png').convert_alpha()
corruption_1 = pygame.image.load('images/tilesets/corruption/corruption_1.png').convert_alpha()
corruption_2 = pygame.image.load('images/tilesets/corruption/corruption_2.png').convert_alpha()
corruption_3 = pygame.image.load('images/tilesets/corruption/corruption_3.png').convert_alpha()

grass_addons = pygame.image.load('images/tilesets/grass_addons/grass_addons.png').convert_alpha()
grass_addons_1 = pygame.image.load('images/tilesets/grass_addons/grass_addons_1.png').convert_alpha()
grass_addons_2 = pygame.image.load('images/tilesets/grass_addons/grass_addons_2.png').convert_alpha()
grass_addons_3 = pygame.image.load('images/tilesets/grass_addons/grass_addons_3.png').convert_alpha()
grass_addons_4 = pygame.image.load('images/tilesets/grass_addons/grass_addons_4.png').convert_alpha()
grass_addons_5 = pygame.image.load('images/tilesets/grass_addons/grass_addons_5.png').convert_alpha()
grass_addons_6 = pygame.image.load('images/tilesets/grass_addons/grass_addons_6.png').convert_alpha()
grass_addons_7 = pygame.image.load('images/tilesets/grass_addons/grass_addons_7.png').convert_alpha()
grass_addons_8 = pygame.image.load('images/tilesets/grass_addons/grass_addons_8.png').convert_alpha()
grass_addons_9 = pygame.image.load('images/tilesets/grass_addons/grass_addons_9.png').convert_alpha()

bush = pygame.image.load('images/tilesets/grass_addons/bush.png').convert_alpha()
bush_1 = pygame.image.load('images/tilesets/grass_addons/bush_1.png').convert_alpha()
bush_2 = pygame.image.load('images/tilesets/grass_addons/bush_2.png').convert_alpha()
bush_3 = pygame.image.load('images/tilesets/grass_addons/bush_3.png').convert_alpha()
bush_4 = pygame.image.load('images/tilesets/grass_addons/bush_4.png').convert_alpha()
bush_5 = pygame.image.load('images/tilesets/grass_addons/bush_5.png').convert_alpha()
cane = pygame.image.load('images/tilesets/grass_addons/cane.png').convert_alpha()
roots = pygame.image.load('images/tilesets/grass_addons/roots.png').convert_alpha()
swamp_tree = pygame.image.load('images/tilesets/grass_addons/swamp_tree.png').convert_alpha()
tombstone = pygame.image.load('images/tilesets/grass_addons/tombstone.png').convert_alpha()
stone = pygame.image.load('images/tilesets/grass_addons/stone.png').convert_alpha()
mushroom = pygame.image.load('images/tilesets/grass_addons/mushroom.png').convert_alpha()
mushroom_1 = pygame.image.load('images/tilesets/grass_addons/mushroom_1.png').convert_alpha()
mushroom_2 = pygame.image.load('images/tilesets/grass_addons/mushroom_2.png').convert_alpha()

water = pygame.image.load('images/tilesets/water/water.png').convert_alpha()
water_1 = pygame.image.load('images/tilesets/water/water_1.png').convert_alpha()
water_2 = pygame.image.load('images/tilesets/water/water_2.png').convert_alpha()

dirt = pygame.image.load('images/tilesets/ground/ground.png').convert_alpha()
dirt_1 = pygame.image.load('images/tilesets/ground/ground_1.png').convert_alpha()
dirt_2 = pygame.image.load('images/tilesets/ground/ground_2.png').convert_alpha()

swamp = pygame.image.load('images/tilesets/swamp/swamp.png').convert_alpha()
swamp_1 = pygame.image.load('images/tilesets/swamp/swamp_1.png').convert_alpha()
swamp_2 = pygame.image.load('images/tilesets/swamp/swamp_2.png').convert_alpha()
swamp_3 = pygame.image.load('images/tilesets/swamp/swamp_3.png').convert_alpha()
swamp_water = pygame.image.load('images/tilesets/swamp/swamp_water.png').convert_alpha()
lilypads = pygame.image.load('images/tilesets/grass_addons/lilypads.png').convert_alpha()
swamp_tree = pygame.image.load('images/tilesets/grass_addons/swamp_tree_1.png').convert_alpha()

tree = pygame.image.load('images/tilesets/trees/tree.png').convert_alpha()
tree_1 = pygame.image.load('images/tilesets/trees/tree_1.png').convert_alpha()
tree_2 = pygame.image.load('images/tilesets/trees/tree_2.png').convert_alpha()
tree_3 = pygame.image.load('images/tilesets/trees/tree_3.png').convert_alpha()
tree_4 = pygame.image.load('images/tilesets/trees/tree_4.png').convert_alpha()

trunk = pygame.image.load('images/tilesets/grass_addons/trunk.png').convert_alpha()


fire = pygame.image.load('images/tilesets/fire.gif').convert_alpha()
transparent = pygame.image.load('images/tilesets/transparent.png').convert_alpha()
player = pygame.image.load('images/tilesets/human_1.png').convert_alpha()
target = pygame.image.load('images/tilesets/target.png').convert_alpha()
select = pygame.image.load('images/tilesets/select.png').convert_alpha()
enemy = pygame.image.load('images/tilesets/enemy.png').convert_alpha()


# demo tiles ----------------------------------------- #
concrete = pygame.image.load('images/tilesets/test_area/concrete.png').convert_alpha()
concrete_1 = pygame.image.load('images/tilesets/test_area/concrete_1.png').convert_alpha()
concrete_2 = pygame.image.load('images/tilesets/test_area/concrete_2.png').convert_alpha()

game_timer = 0

TILE_SIZE = grass.get_width()

tileset_dictionary = {0:[grass, grass_1, grass_2],
                      1:[water, water_1, water_2],
                      2:[dirt, dirt_1, dirt_2],
                      4:[swamp, swamp_1, swamp_2, swamp_water],
                      5:[corruption, corruption_1, corruption_2, corruption_3],
                      # FOREST
                      50:[tree, tree_1, tree_2, tree_3, tree_4],
                      # PLAINS
                      51:[grass_addons_4, grass_addons_5, grass_addons_6, bush, bush_2, bush_3],
                      # SWAMP
                      52:[grass_addons_7, grass_addons_8, bush_5, mushroom, mushroom_1, mushroom_2, trunk, swamp_tree, lilypads],
                      # DEMO
                      53:[concrete, concrete_1, concrete_2],
                      # UNDERGROUND
                      99:[transparent]}

selected_tile = [-1, -1]
target_pos = [-1, -1]
player_pos = [714, 462]

drawLine = False
movement_mode = False

#pygame.font.init()
font = pygame.font.SysFont("Arial", 18)

#biomes = ["deep_forest", "plains", "swamp", "corruption", "demo"]
generated_map = generate_chunk("plains")
game_map = {}

while True:
    events = pygame.event.get()
    mouse_events = pygame.mouse.get_pressed()

    # rendering TILES ----------------------------------------------------------------------------------------------- #
    display.fill((0, 0, 0))
    y = 0
    for row in generated_map[1]:
        x = 0
        for tile in row:
            display.blit(tileset_dictionary[int(str(tile)[:str(tile).index('.')])][(int(str(tile)[-1]))] , (x * TILE_SIZE + scroll[0], y * TILE_SIZE + scroll[1]))
            x += 1
        y += 1

    y = 0
    for row in generated_map[2]:
        x = 0
        for tile in row:
            if tile :
                display.blit(tileset_dictionary[int(str(tile)[:str(tile).index('.')])][(int(str(tile)[-1]))] , (x * TILE_SIZE + scroll[0], y * TILE_SIZE + scroll[1]))
            x += 1
        y += 1

    display.blit(player, (player_pos))
    display.blit(target, (target_pos[0]*42, target_pos[1]*42))
    display.blit(select, (selected_tile[0]*42, selected_tile[1]*42))
        

    # CURSOR --------------------------------------------------------------------------------------------------- #
    # - selecting tile -
    if pygame.mouse.get_pressed()[0] == True:
        mouse_pos = pygame.mouse.get_pos()
        selected_tile = [int(mouse_pos[0]/42), int(mouse_pos[1]/42)]


    # - moving player -
    if mouse_events[2]:
        movement_mode = True

    if movement_mode:
        mouse_pos = pygame.mouse.get_pos()
        line_pos = pygame.mouse.get_pos()
        target_pos = [int(mouse_pos[0]/42), int(mouse_pos[1]/42)]
        pygame.draw.line(display, (255, 255, 255), (734, 482), (line_pos))
           
        if movement_mode == True and mouse_events[2] == False:
            steps_to_go = [(17 - target_pos[0])*42, (11 - target_pos[1])*42]
            scroll[0] += (17 - target_pos[0])*42
            scroll[1] += (11 - target_pos[1])*42
            target_pos = [-1, -1]
            movement_mode = False
    
        print(mouse_pos, player_pos)

    # moving map ----------------------------------------------------------------------------------------------- #
    for event in events:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
               scroll[1] += 42

            if event.key == pygame.K_s:
               scroll[1] -= 42

            if event.key == pygame.K_a:
               scroll[0] += 42

            if event.key == pygame.K_d:
               scroll[0] -= 42
                                                        
    # clock and FPS ------------------------------------------------------------------------------------------- #
    clock.tick(60)
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("#ffffff"))
    display.blit(fps_text, (1410, 0))




    main_screen.blit(display, (0, 0))            
    pygame.display.update()

    # buttons ------------------------------------------------------------------------------------------------- #
    for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                selected_tile = [-1, -1]

            #elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            #    print("STATS")
            #    if stats_mode == False:
            #        stats_mode = True
            #    else:
            #        stats_mode = False
            #elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            #    print("BUILD MODE")
            #    if build_mode == False:
            #        build_mode = True
            #    else:
            #        build_mode = False

            else:
                pass
            
from PIL import ImageGrab
import pyautogui
import numpy as np
import random
import time
import sys
from datetime import datetime

def click_slot_one():
    random_click_within_bounds(647,253,662,265)

def click_slot_two():
    random_click_within_bounds(693,256,704,265)

def click_slot_three():
    random_click_within_bounds(733,253,747,264)

def click_slot_four():
    random_click_within_bounds(773,254,788,266)

def click_slot_five():
    random_click_within_bounds(644,289,663,302)

def click_slot_six():
    random_click_within_bounds(691,288,703,300)

def click_slot_seven():
    random_click_within_bounds(730,293,746,301)

def click_slot_eight():
    random_click_within_bounds(776,291,786,301)

def click_slot_nine():
    random_click_within_bounds(649,327,661,335)

def click_slot_ten():
    random_click_within_bounds(691,328,703,335)

def click_slot_eleven():
    random_click_within_bounds(731,328,745,336)

def click_slot_twelve():
    random_click_within_bounds(772,325,787,336)

def click_slot_thirteen():
    random_click_within_bounds(648,360,660,372)

def click_slot_fourteen():
    random_click_within_bounds(690,361,706,372)

def click_slot_fifteen():
    random_click_within_bounds(728,357,746,370)

def click_slot_sixteen():
    random_click_within_bounds(770,361,788,373)

def click_slot_seventeen():
    random_click_within_bounds(647,399,663,409)

def click_slot_eighteen():
    random_click_within_bounds(687,401,704,408)

def click_slot_nineteen():
    random_click_within_bounds(729,394,750,408)

def click_slot_twenty():
    random_click_within_bounds(774,394,790,412)

def click_slot_twentyone():
    random_click_within_bounds(647,432,661,446)

def click_slot_twentytwo():
    random_click_within_bounds(688,433,703,445)

def click_slot_twentythree():
    random_click_within_bounds(729,433,745,443)

def click_slot_twentyfour():
    random_click_within_bounds(770,436,785,447)

def click_slot_twentyfive():
    random_click_within_bounds(650,467,663,481)

def click_slot_twentysix():
    random_click_within_bounds(687,468,704,483)

def click_slot_twentyseven():
    random_click_within_bounds(730,468,745,481)

def click_slot_twentyeight():
    random_click_within_bounds(771,465,784,480)

def sleep(start, finish):
    random_time = random.uniform(start, finish)
    time.sleep(random_time)


def get_random_pixel_from_image(image_path):
    location = pyautogui.locateOnScreen(image_path)
    if location == None:
        return None
    random_x = random.uniform(location.left, location.left + (location.width * 0.5))
    random_y = random.uniform(location.top, location.top + (location.height * 0.5))
    return (random_x, random_y)


def get_random_pixel_from_colors(target_colors):
    top_left = (0, 0)
    bottom_right = pyautogui.size()
    screenshot = ImageGrab.grab(
        bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1])
    )
    screenshot = np.array(screenshot)
    matching_pixels = []
    for target_color in target_colors:
        result = np.where(np.all(screenshot == target_color, axis=-1))
        pixels = list(zip(result[1], result[0]))
        matching_pixels.extend(pixels)
    if len(matching_pixels) > 0:
        selected_pixel = random.choice(matching_pixels)
        return selected_pixel
    return None


def get_closest_pixel_from_magnet_cord(target_colors, magnet_cord):
    top_left = (0, 0)
    bottom_right = pyautogui.size()
    screenshot = ImageGrab.grab(
        bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1])
    )
    screenshot = np.array(screenshot)
    matching_pixels = []
    closest_distance = float("inf")
    closest_pixel = None

    for target_color in target_colors:
        result = np.where(np.all(screenshot == target_color, axis=-1))
        pixels = list(zip(result[1], result[0]))
        matching_pixels.extend(pixels)

    for pixel in matching_pixels:
        distance = np.linalg.norm(np.array(pixel) - np.array(magnet_cord))
        if distance < closest_distance:
            closest_distance = distance
            closest_pixel = pixel

    if closest_pixel is not None:
        return closest_pixel
    else:
        return None


def click_cords(cords) -> None:
    pyautogui.moveTo(cords[0], cords[1])
    pyautogui.click(cords[0], cords[1])


def right_click_cords(cords):
    pyautogui.moveTo(cords[0], cords[1])
    pyautogui.click(cords[0], cords[1], button="right")


def get_random_cord_from_all_images(list_of_image_names):
    cords = []
    for path in list_of_image_names:
        image_generator = pyautogui.locateAllOnScreen(path)
        for image in image_generator:
            random_x = random.randint(image.left, image.left + image.width)
            random_y = random.randint(image.top, image.top + image.height)
            cords.append((random_x, random_y))
    return cords

def logout():
    cords = (random.randint(711,726), random.randint(505,524))
    click_cords(cords)
    sleep(1,2)
    cords = (random.randint(798,805), random.randint(244,250))
    click_cords(cords)
    sleep(1,2)
    cords = (random.randint(663,773), random.randint(456,471))
    click_cords(cords)


def check_for_other_players():
    print('checking for other players on the map')
    for i in range(0,1):
        dot_cords = get_random_pixel_from_image('./dot.png')
        dot_2_cords = get_random_pixel_from_image('./dot.png')
        if dot_cords != None or dot_2_cords != None:
            print('located another player on the mini map')
            return True
    print('did not find a player on the mini map')
    return False

def hop_world():
    print('hopping worlds')
    click_cords((random.randint(713,728), random.randint(504,523)))
    sleep(1,2)
    click_cords((random.randint(796,812), random.randint(243,252)))
    sleep(1,2)
    click_cords((random.randint(663,772), random.randint(407,420)))
    sleep(1,2)
    click_cords((random.randint(626,781), random.randint(275,455)))
    sleep(10,11)

def vary_cords(cords):
    return ((cords[0] + random.randint(-3,3)), (cords[1] + random.randint(-3,3)))

def open_inventory():
    random_click_within_bounds(707,210,726,221)
    sleep(0,1)

def random_click_within_bounds(x1, y1, x2, y2, button='left'):
    if button == 'left':
        click_cords((random.randint(x1,x2), random.randint(y1,y2)))
    if button == 'right':
        right_click_cords((random.randint(x1,x2), random.randint(y1,y2)))

def random_hop_world():
    random_number = random.randint(0, 200)
    if random_number == 7:
        hop_world()

def click_compass():
    random_click_within_bounds(630,42,643,55)
    sleep(0,1)

def open_inv_if_needed():
    if get_random_pixel_from_image('./img/inv_open.png') == None:
        open_inventory()

def seconds_since_capture(start_time):
    current_time = time.time()
    seconds_elapsed = current_time - start_time
    return seconds_elapsed

def random_world_hop():
    random_roll = random.randint(0,20)
    print(f'random roll is {random_roll}')
    if random_roll == 7:
        hop_world()

def click_tree():
    tree_cords = get_closest_pixel_from_magnet_cord(TREE_COLORS,PLAYER_CORDS)
    if tree_cords != None:
        print('clicking a tree')
        click_cords(vary_cords(tree_cords))

def drop_inventory():
    print('dropping logs')
    actions = [click_slot_one,click_slot_two,click_slot_three,click_slot_four,click_slot_five,click_slot_six,click_slot_seven,click_slot_eight,click_slot_nine,click_slot_ten,click_slot_eleven,click_slot_twelve,click_slot_thirteen,click_slot_fourteen,click_slot_fifteen,click_slot_sixteen,click_slot_seventeen,click_slot_eighteen,click_slot_nineteen,click_slot_twenty,click_slot_twentyone,click_slot_twentytwo,click_slot_twentythree,click_slot_twentyfour,click_slot_twentyfive,click_slot_twentysix,click_slot_twentyseven,click_slot_twentyeight]
    random.shuffle(actions)
    pyautogui.keyDown('SHIFT')
    for action in actions:
        action()
        sleep(0.2,0.4)
    pyautogui.keyUp('SHIFT')

def tele_home():
    random_click_within_bounds(807,205,825,226)
    sleep(0.2,0.3)
    random_click_within_bounds(688,317,695,322)
    sleep(5,6)

def count_logs():
    return len(get_random_cord_from_all_images(['./img/log.png']))

def wait_for_tree_to_fall(starting_logs):
    print('waiting for tree to fall')
    sleep(5,6)
    if is_inventory_full():
        return
    if count_logs() == starting_logs:
        return
    wait_for_tree_to_fall(count_logs())

def is_inventory_full():
    if count_logs() == MAX_NUMBER_OF_LOGS:
        return True
    return False    

def walk_here(x1,y1,x2,y2,sleep_start,sleep_end):
    random_click_within_bounds(x1,y1,x2,y2,button='right')
    sleep(0.4,0.5)
    walk_here_cords = get_random_pixel_from_image('./img/walk_here.png')
    click_cords(walk_here_cords)
    sleep(sleep_start,sleep_end)


if len(sys.argv) > 1:

    if sys.argv[1] == '-p':
        print(pyautogui.position())
        exit()

    if sys.argv[1] == '-wood':
        TREE_COLORS = [(98,50,0),(96,53,0),(97,50,0)]
        PLAYER_CORDS = (329,198)
        LOOPS = 400
        MAX_NUMBER_OF_LOGS = 28
        open_inventory()
        for i in range(0, LOOPS):
            print(f'playing loop {i} of {LOOPS}')
            click_tree()
            wait_for_tree_to_fall(count_logs())
            if count_logs() == 28:
                drop_inventory()
            random_hop_world()
            open_inv_if_needed()
        logout()
    
    if sys.argv[1] == '-steal':
        LOOPS = 300
        for i in range(0,LOOPS):
            print(f'playing loop {i} of {LOOPS}')
            random_click_within_bounds(436,229,510,321,button='right')
            trap_cords = get_random_pixel_from_image('./img/traps.png')
            if trap_cords != None:
                click_cords(trap_cords)
            sleep(2,2.5)
            random_click_within_bounds(436,229,510,321)
            sleep(12,12.5)
            random_hop_world()
        logout()

    if sys.argv[1] == '-glass':
        LOOPS = 100
        for i in range(0,LOOPS):
            print(f'playing loop {i} of {LOOPS}')
            print(f'we are making a total of {LOOPS*27} orbs, and we have completed {i*27} so far')
            print('opening bank')
            random_click_within_bounds(441,242,506,300)
            sleep(1.2,1.3)
            print('checking if bank is open')
            if get_random_pixel_from_image('./img/bank_open.png') == None:
                print('bank not open, logging out')
                logout()
                exit()
            print('depositing orbs')
            slots = [click_slot_two,click_slot_three,click_slot_four,click_slot_five,click_slot_six,click_slot_seven,click_slot_eight,click_slot_nine,click_slot_ten,click_slot_eleven,click_slot_twelve,click_slot_thirteen,click_slot_fourteen,click_slot_fifteen,click_slot_sixteen,click_slot_seventeen,click_slot_eighteen,click_slot_nineteen,click_slot_twenty,click_slot_twentyone,click_slot_twentytwo,click_slot_twentythree,click_slot_twentyfour,click_slot_twentyfive,click_slot_twentysix,click_slot_twentyseven,click_slot_twentyeight]
            another_random_slot = random.choice(slots)
            another_random_slot()
            sleep(0.5,0.6)
            print('clicking the molten glass')
            random_click_within_bounds(493,125,508,137)
            sleep(0.5,0.6)
            print('exiting bank')
            pyautogui.press('ESC')
            sleep(0.5,0.6)
            print('clicking the blowpipe')
            click_slot_one()
            sleep(0.5,0.6)
            print('clicking the glass')
            random_slot = random.choice(slots)
            random_slot()
            sleep(0.5,0.6)
            print('clicking the molten glass crafting option')
            random_click_within_bounds(408,432,448,479)
            print('waiting for the glass to blow...')
            sleep(49,49.5)
        print('loop complete, logging out')
        logout()

    if sys.argv[1] == '-falcon':
        LOOPS = 1000
        CAUGHT_COLORS=[(65,196,81),(62,193,77),(93,226,104)]
        ANIMAL_COLORS=[(79,68,51),(95,85,71)]
        for i in range(0,LOOPS):
            print(f'playing loop {i} of {LOOPS}')
            print('looking for caught animal')
            caught_animal_cords = get_random_pixel_from_colors(CAUGHT_COLORS)
            if caught_animal_cords != None:
                print('found caught animal')
                click_cords
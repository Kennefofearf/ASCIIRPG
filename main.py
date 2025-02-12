import json
import os
import random
import re
from map import test_map

run = True
menu = True
play = True
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False

HP = 50
HPMAX = HP
ATK = 3
pot = 1
gold = 20
x = 0
y = 0

def display_test_map():
    for row in test_map:
        print(row)



y_len = len(test_map)-1
x_len = len(test_map[0])-1

biom = {
    ".": {
        "t": "PLAINS",
        "e": True},
    "8": {
        "t": "FOREST",
        "e": True},
    ".": {
        "t": "FIELDS",
        "e": True},
    "#": {
        "t": "SHOP",
        "e": False},
    "=": {
        "t": "BRIDGE",
        "e": True},
    "#": {
        "t": "TOWN",
        "e": False},
    "#": {
        "t": "MAYOR",
        "e": False},
    "^": {
        "t": "HILLS",
        "e": True},
    "A": {
        "t": "MOUNTAIN",
        "e": True},
    "0": {
        "t": "CAVE",
        "e": False}
    }

e_list = ["Rat", "Snake", "Kobold", "Wyrm"]

mobs = {
    "Rat": {
        "hp": 6,
        "at": 3,
        "go": 1
    },
    "Snake": {
        "hp": 9,
        "at": 5,
        "go": 3
    },
    "Kobold": {
        "hp": 15,
        "at": 7,
        "go": 10
    },
    "Wyrm": {
        "hp": 60,
        "at": 8,
        "go": 200
    }
}

current_tile = test_map[x][y]
print(current_tile)
name_of_tile = biom[current_tile]["t"]
print(name_of_tile)
enemy_tile = biom[current_tile]["e"]
print(enemy_tile)

def clear():
    os.system("cls")

def draw():
    print("xX--------------------Xx")

def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    f = open("player.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

def heal(amount):
    global HP
    if HP + amount < HPMAX:
        HP += amount
    else:
        HP = HPMAX
    print("Healed to: " + str(HP))

def shop():
    global buy, gold, pot, ATK

    while buy:
        clear()
        draw()
        print("S-H-O-P")
        draw()
        print("Gold: " + str(gold))
        print("Potions: " + str(pot))
        print("ATK: " + str(ATK))
        draw()
        print("1 - Buy POTION - 5 Gold")
        print("2 - UPGRADE WEAPON - 10 Gold")
        print("3 - LEAVE SHOP")
        draw()

        choice = input("# ")

        if choice == "1":
            if gold >= 5:
                pot += 1
                gold -= 5
                print("Bought 1 POTION")
            else:
                print("Not enough gold.")
            input("> ")
        elif choice == "2":
            if gold >= 10:
                ATK += 3
                gold -= 10
                print("Weapon upgraded (+3 ATK)")
            else:
                print("Not enough gold.")
            input("> ")
        elif choice == "3":
            buy = False

def mayor():
    global speak, key

    while speak:
        clear()
        draw()
        print("Hello," + name + ".")
        if ATK < 12:
            print("The wyrm's hide is still too durable for you to penetrate.")
            key = False
        else:
            print("You may have what it takes to fell the wyrm. Take this key to it's lair.")
            key = True
        draw()
        print("1 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            speak = False

def cave():
    global boss, key, fight

    while boss:
        clear()
        draw()
        print("You stand before the entrance to the dragon's lair.")
        draw()
        if key:
            print("1 - Use KEY and enter")
        print("2 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            if key:
                fight = True
                battle()
        elif choice == "2":
            boss = False


def battle():
    global fight, play, run, HP, pot, gold, boss

    if not boss:
        enemy = e_list[random.randint(0, 2)]
    else:
        enemy = "Wyrm"
    hp = mobs[enemy]["hp"]
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]

    while fight:
        clear()
        draw()
        print("A " + enemy + " appeared!")
        draw()
        print(enemy + ": " + str(hp))
        draw()
        print(name + ": " + str(HP) + "/" + str(HPMAX))
        print("POTIONS: " + str(pot))
        draw()
        print("a - ATTACK")
        if pot > 0:
            print("d - USE POTION")
        draw()

        choice = input("# ")

        if choice == "a":
            hp -= int(ATK)
            print(str(ATK) + " dmg to the " + enemy)
            if hp > 0:
                HP -= atk
                print(enemy + " deals " + str(atk) + " dmg")
            input("> ")
        elif choice == "d":
            if pot > 0:
                pot -= 1
                heal(30)
                HP -= atk
                print(enemy + " deals " + str(atk) + " dmg")
                input("> ")
            else:
                print("You have no potions")
            input("> ")

        if HP <= 0:
            print("Your vision clouds...")
            input("> ")
            clear()
            draw()
            fight = False
            play = False
            run = False
            print("There is no shame in defeat.")
            print("Death inevitably comes to warrior and peasant alike.")
            print("May the divine guide your soul to paradise.")
            draw()
            input("> ")

        if hp <= 0:
            print("The " + enemy + " is felled")
            input("> ")
            clear()
            draw()
            fight = False
            gold += g
            print("Gold: " + str(g))
            if random.randint(0, 100) < 30:
                pot += 1
                print("Potion: 1")
            if enemy == "Wyrm":
                draw()
                print("Congratulations! The Wyrm is slain!")
                print("YOU WIN")
                draw()
                boss = False
                play = False
                run = False
            input("> ")
            clear()
            draw()

while run:
    while menu:
        clear()
        draw()
        print("1. New Game")
        print("2. Load Game")
        print("3. Rules")
        print("4. Quit")
        draw()

        if rules:
            print("Just play it")
            rules = False
            choice = ""
            input("> ")

        choice = input("# ")

        if choice == "1":
            clear()
            name = input("# What is your name? ")
            menu = False
            play = True
        if choice == "2":
            clear()
            try:
                f = open("player.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 8:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    gold = int(load_list[4][:-1])
                    x = int(load_list[5][:-1])
                    y = int(load_list[6][:-1])
                    key = bool(load_list[7][:-1])
                    clear()
                    print("Welcome back, " + name + "!")
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Save file is corrupt!")
                    input("> ")
            except OSError:
                print("No loadable save file!")
                input("> ")
        if choice == "3":
            clear()
            rules = True
        if choice == "4":
            clear()
            quit()

    while play:
        save()
        clear()

        if not standing:
            if biom[test_map[y][x]]["e"]:
                if random.randint(0, 100) <= 30:
                    fight = True
                    battle()

        if play:

            draw()
            print("LOCATION: " + biom[test_map[y][x]]["t"])
            draw()
            print("Name: " + name)
            print("HP: " + str(HP) + "/" + str(HPMAX))
            print("ATK: " + str(ATK))
            print("Potions: " + str(pot))
            print("Gold: " + str(gold))
            print("COORD: ", x, y)
            draw()
            print("0 - Save and Quit")
            if y > 0:
                print("w - NORTH")
            if x < x_len:
                print("d - EAST")
            if y < y_len:
                print("s - SOUTH")
            if x > 0:
                print("a - WEST")
            if pot > 0:
                print("1 - POTION")
            if test_map[y][x] == "shop" or test_map[y][x] == "mayor" or test_map[y][x] == "cave":
                print("2 - ENTER")
            display_test_map()

            dest = input("# ")

            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == "w":
                if y > 0:
                    y -= 1
                standing = False
            elif dest == "d":
                if x < x_len:
                    x += 1
                standing = False
            elif dest == "s":
                if y < y_len:
                    y += 1
                standing = False
            elif dest == "a":
                if x > 0:
                    x -= 1
                standing = False
            elif dest == "1":
                if pot > 0:
                    pot -= 1
                    heal(30)
                else:
                    print("You have no potions. Your preparation is lacking")
                input("> ")
                standing = True
            elif dest == "2":
                if map[y][x] == "shop":
                    buy = True
                    shop()
                if map[y][x] == "mayor":
                    speak = True
                    mayor()
                if map[y][x] == "cave":
                    boss = True
                    cave()
            else:
                standing = True
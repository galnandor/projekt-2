from tkinter import *
import time
import random

winner = False  
red_horse_x = 0  
red_horse_y = 10  

blue_horse_x = 0
blue_horse_y = 80

yellow_horse_x = 0
yellow_horse_y = 150

black_horse_x = 0
black_horse_y = 220

orange_horse_x = 0
orange_horse_y = 290

grey_horse_x = 0
grey_horse_y = 360

game_running = False  # A játék futásának állapota

def start_game():
    global blue_horse_x, red_horse_x, yellow_horse_x, black_horse_x, orange_horse_x, grey_horse_x
    global winner, game_running

    if game_running:  # Ha a játék már fut, ne indítsuk újra
        return
    
    game_running = True  # A játék elindul
    winner = False  # A győztes visszaállítása

    while not winner:
        time.sleep(0.05)
        # Véletlenszerű mozgások
        random_move_blue_horse = random.randint(0, 20)
        random_move_red_horse = random.randint(0, 20)
        random_move_yellow_horse = random.randint(0, 20)
        random_move_black_horse = random.randint(0, 20)
        random_move_orange_horse = random.randint(0, 20)
        random_move_grey_horse = random.randint(0, 20)

        # A lovak X pozícióinak frissítése
        blue_horse_x += random_move_blue_horse
        red_horse_x += random_move_red_horse
        yellow_horse_x += random_move_yellow_horse
        black_horse_x += random_move_black_horse
        orange_horse_x += random_move_orange_horse
        grey_horse_x += random_move_grey_horse

        move_horses(random_move_red_horse, random_move_blue_horse, random_move_yellow_horse,
                    random_move_black_horse, random_move_orange_horse, random_move_grey_horse)
        main_screen.update()
        winner = check_winner()

    # Ha döntetlen, kiírjuk, ha nem, akkor a győztest
    if winner == "Tie":
        Label(main_screen, text=winner, font=('calibri', 20), fg="green").place(x=350, y=480)
    else:
        Label(main_screen, text=winner + " Wins !!", font=('calibri', 20), fg="green").place(x=350, y=480)
    
    game_running = False  # A játék vége

def move_horses(red_horse_random_move, blue_horse_random_move, yellow_horse_random_move,
                black_horse_random_move, orange_horse_random_move, grey_horse_random_move):
    canvas.move(red_horse, red_horse_random_move, 0)
    canvas.move(blue_horse, blue_horse_random_move, 0)
    canvas.move(yellow_horse, yellow_horse_random_move, 0)
    canvas.move(black_horse, black_horse_random_move, 0)
    canvas.move(orange_horse, orange_horse_random_move, 0)
    canvas.move(grey_horse, grey_horse_random_move, 0)

def check_winner():
    if blue_horse_x >= 800 and red_horse_x >= 800 and yellow_horse_x >= 800 and black_horse_x >= 800 and orange_horse_x >= 800 and grey_horse_x >= 800:
        return "Tie"  # Döntetlen
    if blue_horse_x >= 800:
        return "Blue Horse"
    if red_horse_x >= 800:
        return "Red Horse"
    if yellow_horse_x >= 800:
        return "Yellow Horse"
    if black_horse_x >= 800:
        return "Black Horse"
    if orange_horse_x >= 800:
        return "Orange Horse"
    if grey_horse_x >= 800:
        return "Grey Horse"
    return False

# Beállítjuk a fő ablakot
main_screen = Tk()
main_screen.title('Horse Racing')
main_screen.geometry('900x900')
main_screen.config(background='white')

# Beállítjuk a vászont
canvas = Canvas(main_screen, width=900, height=500, bg="white")
canvas.pack(pady=20)

# Képek importálása
red_horse_img = PhotoImage(file="./kepek/red-horse.png")
blue_horse_img = PhotoImage(file="./kepek/blue-horse.png")
yellow_horse_img = PhotoImage(file="./kepek/yellow-horse.png")
black_horse_img = PhotoImage(file="./kepek/black-horse.png")
orange_horse_img = PhotoImage(file="./kepek/orange-horse.png")
grey_horse_img = PhotoImage(file="./kepek/grey-horse.png")

# A képek átméretezése
red_horse_img = red_horse_img.zoom(15)
red_horse_img = red_horse_img.subsample(50)
blue_horse_img = blue_horse_img.zoom(15)
blue_horse_img = blue_horse_img.subsample(50)
yellow_horse_img = yellow_horse_img.zoom(15)
yellow_horse_img = yellow_horse_img.subsample(50)
black_horse_img = black_horse_img.zoom(15)
black_horse_img = black_horse_img.subsample(50)
orange_horse_img = orange_horse_img.zoom(15)
orange_horse_img = orange_horse_img.subsample(50)
grey_horse_img = grey_horse_img.zoom(15)
grey_horse_img = grey_horse_img.subsample(50)

# Képek hozzáadása a vászonhoz
red_horse = canvas.create_image(red_horse_x, red_horse_y, anchor=NW, image=red_horse_img)
blue_horse = canvas.create_image(blue_horse_x, blue_horse_y, anchor=NW, image=blue_horse_img)
yellow_horse = canvas.create_image(yellow_horse_x, yellow_horse_y, anchor=NW, image=yellow_horse_img)
black_horse = canvas.create_image(black_horse_x, black_horse_y, anchor=NW, image=black_horse_img)
orange_horse = canvas.create_image(orange_horse_x, orange_horse_y, anchor=NW, image=orange_horse_img)
grey_horse = canvas.create_image(grey_horse_x, grey_horse_y, anchor=NW, image=grey_horse_img)

# Címkék hozzáadása a képernyőhöz (szöveg)
l1 = Label(main_screen, text='Select your horse', font=('calibri', 20), bg="white")
l1.place(x=350, y=525)
l2 = Label(main_screen, text='Click play when ready!', font=('calibri', 20), bg='white')
l2.place(x=330, y=560)

b1 = Button(main_screen, text='Play!', height=2, width=15, bg='white', font=('calibri', 10), command=start_game)
b1.place(x=400, y=600)

# Restart gomb kezelése
def restart_race():
    global winner, game_running
    game_running = False  # Leállítjuk a játékot

    # Kezdő pozíciók visszaállítása
    global red_horse_x, blue_horse_x, yellow_horse_x, black_horse_x, orange_horse_x, grey_horse_x
    red_horse_x = 0
    blue_horse_x = 0
    yellow_horse_x = 0
    black_horse_x = 0
    orange_horse_x = 0
    grey_horse_x = 0

    winner = False  # Töröljük a győztest

    # Lovakat visszaállítjuk az új pozícióra
    canvas.coords(red_horse, red_horse_x, red_horse_y)
    canvas.coords(blue_horse, blue_horse_x, blue_horse_y)
    canvas.coords(yellow_horse, yellow_horse_x, yellow_horse_y)
    canvas.coords(black_horse, black_horse_x, black_horse_y)
    canvas.coords(orange_horse, orange_horse_x, orange_horse_y)
    canvas.coords(grey_horse, grey_horse_x, grey_horse_y)

    # Töröljük a győztes szöveget
    winner_label.config(text="")

# Restart gomb létrehozása
b2 = Button(main_screen, text='Restart', height=2, width=10, bg='white', font=('calibri', 10), command=restart_race)
b2.place(x=420, y=650)

# Győztes kijelzése
winner_label = Label(main_screen, text="", font=('calibri', 20), fg="green", bg="white")
winner_label.pack(pady=20)

# Fő alkalmazás indítása
main_screen.mainloop()

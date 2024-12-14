import tkinter as tk
import math
import time

# Funkcja do rysowania tarczy zegara
def draw_clock(canvas):
    # Rysowanie okręgu zegara
    canvas.create_oval(10, 10, 310, 310, fill="white", outline="black", width=4)

    # Rysowanie numerów na zegarze
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)  # Przesunięcie o 90 stopni, by 12 było na górze
        x = 150 + 120 * math.cos(angle)
        y = 150 + 120 * math.sin(angle)  # Zmiana kierunku sinusa, by 12 było na górze
        canvas.create_text(x, y, text=str(i), font=("Arial", 14, "bold"))

# Funkcja do rysowania wskazówek
def draw_hands(canvas, hours, minutes, seconds):
    # Wskaźnik godzin (wskazówka godzinowa porusza się zgodnie z ruchem wskazówek zegara)
    hour_angle = math.radians((hours % 12 + minutes / 60) * 30 - 90)  # Przesunięcie o 90 stopni
    hour_x = 150 + 50 * math.cos(hour_angle)
    hour_y = 150 + 50 * math.sin(hour_angle)
    canvas.coords(hour_hand, 150, 150, hour_x, hour_y)

    # Wskaźnik minut (wskazówka minutowa)
    minute_angle = math.radians((minutes + seconds / 60) * 6 - 90)  # Przesunięcie o 90 stopni
    minute_x = 150 + 90 * math.cos(minute_angle)  # Zwiększenie długości wskazówki minutowej
    minute_y = 150 + 90 * math.sin(minute_angle)
    canvas.coords(minute_hand, 150, 150, minute_x, minute_y)

    # Wskaźnik sekund (wskazówka sekundowa)
    second_angle = math.radians(seconds * 6 - 90)  # Przesunięcie o 90 stopni
    second_x = 150 + 90 * math.cos(second_angle)
    second_y = 150 + 90 * math.sin(second_angle)
    canvas.coords(second_hand, 150, 150, second_x, second_y)

# Funkcja do aktualizacji zegara
def update_clock(canvas):
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    draw_hands(canvas, hours, minutes, seconds)

    # Ponowna aktualizacja co sekundę
    canvas.after(1000, update_clock, canvas)

# Ustawienia głównego okna
root = tk.Tk()
root.title("Zegar Analogowy")
canvas = tk.Canvas(root, width=320, height=320, bg="lightgray")
canvas.pack()

# Rysowanie tarczy zegara
draw_clock(canvas)

# Rysowanie początkowych wskazówek
hour_hand = canvas.create_line(150, 150, 150, 80, width=6, fill="black")
minute_hand = canvas.create_line(150, 150, 150, 40, width=4, fill="black")  # Zmieniono długość na 90
second_hand = canvas.create_line(150, 150, 150, 30, width=2, fill="red")

# Uruchomienie zegara
update_clock(canvas)

# Uruchomienie głównej pętli
root.mainloop()

print(5-4.935)
#Umjesto očekivanog rezultata 0.065 dobili smo i znamenke 3 i 9 na šesnaestoj i sedamnaestoj decimali zbog toga što Python u memoriji ima samo znamenke 0 i 1, 
#zbog čega matematičke operacije izvšava u binarnom sustavu, što znači da može točno izračunati samo brojeve koji se mogu zapisati kao 1/(2^n), 
#ostalo su aproksimacije.
print(0.1+0.2+0.3)
#Sada ovisimo o broju bitova koje Python ima na raspolaganju. Za manji broj bitova se više različitih brojeva zapisuje binarno na isti način, a rezultat se
#u dekadski vraća aproksimacijiom koja je u ovom slučaju veća od savršenog rezultata za 10^-17.

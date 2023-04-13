# Kantega rPI Pico Game Jam – Q2 2023




## Introduksjon

I denne workshoppen skal vi programmere med MicroPython.

Alle gruppene får utdelt en Raspberry PI Pico med et lite LCD-panel.
MicroPython er ferdig installert på enheten.




## Oppgave 0: Klon dette repoet!

Det aller første du må gjøre er å klone dette GitHub-repoet.

Det kan f.eks. gjøres med å kjøre:

```
git clone https://github.com/kantega/picojam.git
```




## Oppgave 1: Oppsett av lokal toolchain

For å snakke med Pico'en, kopiere over filer, osv. bruker vi Python og det
lille programmet [rshell](https://github.com/dhylands/rshell).

Dette betyr at vi må starte med å gjøre litt oppsett på egen maskin...

For å komme i gang, kan du bruke følgende oppskrift (🤞):

1. Åpne en terminal
2. Sjekk at det går an å kjøre `python -V` 
3. Sjekk at det går an å kjøre `pip -V`
4. Installer rshell som en global pakke med `pip install rshell`
4. Sjekk at det går an å kjøre `rshell -V`

![Demo av de første stegene](./.other-assets/python-pip-check-rshell-install.gif)

Her er det dessverre flere ting som kan gå galt:

1. **Du mangler Python og/eller pip:** 
   Last ned Python med pip fra https://www.python.org/downloads/ 
2. **Du har installert Python og pip, men det er noe problemer med
   PATH-oppsettet i skallet du bruker:** 
   Dette er lett å fikse, men ofte litt forskjellige fra oppsett til oppsett.
   Spør en av arrangørene om hjelp!
3. **Du får ikke installert rshell, pga. manglende rettigheter:**
   Her er det egentlig like greit å bare bruke et såkalt *virtual environment*
   i stedet. Spør en av arrangørene om hjelp!

Når rshell er på plass, er så å si alt klart til å programmere PI'en.
Linux-brukere er nødt å gjøre et lite steg til.

#### 🐧 Linux-brukere: Legg deg selv inn i dialout-gruppa!
Kjører du Linux (yay!) må du legge deg selv inn i `dialout`-gruppa for å få lov
å snakke med PI'en over den virtuelle seriellporten. Dette kan gjøres med `sudo
adduser $USER dialout`, hvis du kjører et tålig vettugt skall.

Etter adduser-kommandoen kan/må du logge inn på nytt for å få aktivert
gruppetilhørigheten, eller du kan kjøre `newgrp dialout`, om du synes det blir
for mye bry å logge ut.




## Oppgave 2: Koble til PI-en og start en interaktiv Python-økt

Hvis du er kommet helt hit, er det på tide å koble PI-en til maskinen med
USB-kabelen.

Så fort PI-en koblet til med USB, kan du prøve å kjøre opp en interaktiv
Python-økt på PI-en, med kommandoen `rshell repl`.

Om alt funker, skal du raskt komme inn i en sesjon hvor du får kjøre 
små Python-snutter på PI-en.

For å hoppe ut av den interaktive økten, trykk CTRL-X. 

![Demo av rshell repl](./.other-assets/rshell-repl.gif)




## Oppgave 3: Last opp og kjør et skikkelig program på PI-en 

Nå er det på høy tid med litt skikkelig programmering på PI-en.

Vi har laget klar en fil som heter **example_basics.py**, hvor displayet,
knappene og joysticken på PI-en allerede er satt opp.

Åpne example_basics.py i din favoritt-editor (f.eks. VS Code, Vim eller
Microsoft Word) og se litt på koden.

Når du synes du skjønner sånn ca. hva som foregår, kan du kjøre følgende
to kommandoer for å laste opp alt av Python-filer i mappa til PI-en,
og starte programmet example_basics.


```
rshell cp *.py /pyboard 
rshell repl pyboard 'import example_basics~'
```




## Oppgave 4: Gamedev!

Det egentlig målet vårt med workshop'en er å selvfølgelig å gjøre litt
spillutvikling!

Dere står fritt til å lage hva dere vil, men det kan være lurt å hive seg ut på
en klone av en gammel arkade- eller retro-klassiker.

Å implementere en Pong-klone er en bra utfordring. Vi har gjort klart et 
minimalt utgangspunkt i filen `example_pong_todo.py`.

Snake er mer innvikla å kode enn Pong, men absolutt overkommelig. Tetris er en
retro-klassiker som er overraskende komplisert å implementere, men ikke umulig. 

Lykke til!


#### Enkelt – medium
- [Pong](https://en.wikipedia.org/wiki/Pong#/media/File:Pong_Game_Test2.gif)

#### Medium – vanskelig
- [Space Invaders](https://en.wikipedia.org/wiki/Space_Invaders#Gameplay)
- [Snake](https://en.wikipedia.org/wiki/Snake_(video_game_genre)#/media/File:Snake_can_be_completed.gif)
- [Pacman](https://en.wikipedia.org/wiki/Pac-Man#Gameplay)

#### Vanskelig
- Tetris

#### Umulig?
- Minimal 2D-plattformer (Mario)

#### Helt umulig?
- Minimal pseudo-3D-motor (Wolfenstein 3D)

import pygame
from player import Player

# Inizializza Pygame
pygame.init()

# Dimensioni dello schermo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colori
GREY = (100, 100, 100)

# Crea lo schermo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Titolo della finestra
pygame.display.set_caption("Road Fighter")

# === Creazione degli Sprite ===
# Un gruppo per contenere tutti gli sprite (oggetti di gioco)
all_sprites = pygame.sprite.Group()

# Creiamo il giocatore
player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
# Aggiungiamo il giocatore al gruppo di sprite
all_sprites.add(player)


# Game Loop
running = True
while running:
    # Gestione degli eventi (input)
    for event in pygame.event.get():
        # Controlla se l'utente ha chiuso la finestra
        if event.type == pygame.QUIT:
            running = False

        # Controlla se un tasto è stato PREMUTO
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -5 # Muovi a sinistra
            if event.key == pygame.K_RIGHT:
                player.speed_x = 5  # Muovi a destra

        # Controlla se un tasto è stato RILASCIATO
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.speed_x < 0:
                player.speed_x = 0 # Ferma il movimento
            if event.key == pygame.K_RIGHT and player.speed_x > 0:
                player.speed_x = 0 # Ferma il movimento

    # === Aggiornamento ===
    # Chiama il metodo update() su tutti gli sprite nel gruppo
    all_sprites.update()

    # === Disegno ===
    # Riempi lo schermo con il colore della strada
    screen.fill(GREY)
    # Disegna tutti gli sprite contenuti nel gruppo sullo schermo
    all_sprites.draw(screen)

    # Aggiorna la visualizzazione
    pygame.display.flip()

# Esci da Pygame
pygame.quit()

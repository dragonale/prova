import pygame
from player import Player

# --- Costanti e Impostazioni ---
# Dimensioni della finestra
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Fotogrammi al secondo (FPS)
FPS = 60
# Velocità del giocatore
PLAYER_SPEED = 5

# Colori
ROAD_COLOR = (100, 100, 100)

# --- Inizializzazione ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Road Fighter")
clock = pygame.time.Clock() # Oggetto Clock per il controllo degli FPS

# --- Creazione degli Sprite ---
all_sprites = pygame.sprite.Group()
player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
all_sprites.add(player)

# === Game Loop Principale ===
running = True
while running:
    # Controlla il framerate per far girare il gioco alla stessa velocità su ogni computer
    clock.tick(FPS)

    # --- Gestione degli Eventi (Input) ---
    for event in pygame.event.get():
        # L'utente ha chiuso la finestra
        if event.type == pygame.QUIT:
            running = False

        # Un tasto è stato PREMUTO
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -PLAYER_SPEED # Usa la costante
            if event.key == pygame.K_RIGHT:
                player.speed_x = PLAYER_SPEED  # Usa la costante

        # Un tasto è stato RILASCIATO
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.speed_x < 0:
                player.speed_x = 0
            if event.key == pygame.K_RIGHT and player.speed_x > 0:
                player.speed_x = 0

    # --- Aggiornamento Logica di Gioco ---
    all_sprites.update()

    # --- Disegno su Schermo ---
    screen.fill(ROAD_COLOR)
    all_sprites.draw(screen)

    # Aggiorna la visualizzazione
    pygame.display.flip()

# --- Uscita dal Gioco ---
pygame.quit()

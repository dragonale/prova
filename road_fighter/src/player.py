import pygame
import os

# --- Costanti del Giocatore ---
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 80
# Il colore non è più necessario, ma lo lasciamo per riferimento
# PLAYER_COLOR = (255, 0, 0)

# --- Percorsi per gli Asset ---
# __file__ è il percorso di questo file (player.py)
# os.path.dirname(__file__) è la cartella 'src'
# os.path.join(...) costruisce un percorso sicuro per ogni sistema operativo
assets_folder = os.path.join(os.path.dirname(__file__), '..', 'assets')
player_spritesheet_path = os.path.join(assets_folder, 'car_spritesheet.png')


class Player(pygame.sprite.Sprite):
    """
    Questa classe rappresenta l'auto del giocatore.
    """
    def __init__(self, screen_width, screen_height):
        # Chiama il costruttore della classe genitore (Sprite)
        super().__init__()

        # --- Aspetto del Giocatore ---
        # Carichiamo l'intero foglio di sprite
        self.spritesheet = pygame.image.load(player_spritesheet_path).convert_alpha()

        # Estraiamo un'immagine specifica dal foglio di sprite
        # Usiamo .subsurface(pygame.Rect(x, y, larghezza, altezza))
        # Le coordinate (x, y) sono il punto in alto a sinistra dell'immagine desiderata
        # Queste coordinate sono state trovate ispezionando l'immagine per isolare un'auto blu
        car_image_rect = pygame.Rect(40, 30, 420, 200)
        self.image_original = self.spritesheet.subsurface(car_image_rect)

        # Ruotiamo l'immagine originale per farla puntare verso l'alto
        rotated_image = pygame.transform.rotate(self.image_original, 90)
        # Alcuni asset sono disegnati 'a testa in giù', quindi li ribaltiamo verticalmente
        flipped_image = pygame.transform.flip(rotated_image, False, True)
        # Ora scaliamo l'immagine finale alle dimensioni del giocatore
        self.image = pygame.transform.scale(flipped_image, (PLAYER_WIDTH, PLAYER_HEIGHT))

        # --- Posizione e Rettangolo ("Hitbox") ---
        self.rect = self.image.get_rect()

        # Salviamo le dimensioni dello schermo per non far uscire il giocatore.
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Posizioniamo il giocatore inizialmente in basso e al centro.
        self.rect.centerx = screen_width / 2
        self.rect.bottom = screen_height - 40 # Un po' staccato dal fondo

        # --- Movimento ---
        self.speed_x = 0

    def update(self):
        """
        Questo metodo viene chiamato ad ogni frame per aggiornare la posizione del giocatore.
        """
        # Applica la velocità alla posizione x (orizzontale).
        self.rect.x += self.speed_x

        # Controlliamo che il giocatore non esca dai bordi dello schermo.
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width

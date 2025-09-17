import pygame

# --- Costanti del Giocatore ---
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 80
PLAYER_COLOR = (255, 0, 0) # Colore rosso

class Player(pygame.sprite.Sprite):
    """
    Questa classe rappresenta l'auto del giocatore.
    """
    def __init__(self, screen_width, screen_height):
        # Chiama il costruttore della classe genitore (Sprite)
        super().__init__()

        # --- Aspetto del Giocatore ---
        # Crea l'immagine del giocatore usando le costanti definite sopra.
        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.image.fill(PLAYER_COLOR)

        # --- Posizione e Rettangolo ("Hitbox") ---
        # Pygame usa gli oggetti Rect per gestire la posizione e le collisioni.
        self.rect = self.image.get_rect()

        # Salviamo le dimensioni dello schermo per non far uscire il giocatore.
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Posizioniamo il giocatore inizialmente in basso e al centro.
        self.rect.centerx = screen_width / 2
        self.rect.bottom = screen_height - 40 # Un po' staccato dal fondo

        # --- Movimento ---
        # La velocità iniziale del giocatore è 0.
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

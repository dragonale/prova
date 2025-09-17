import pygame

# Colore per il giocatore
RED = (255, 0, 0)

class Player(pygame.sprite.Sprite):
    """
    Questa classe rappresenta l'auto del giocatore.
    """
    def __init__(self, screen_width, screen_height):
        # Chiama il costruttore della classe genitore (Sprite)
        super().__init__()

        # --- Aspetto del Giocatore ---
        # Crea l'immagine del giocatore.
        # Per ora, è un semplice rettangolo.
        # In futuro, qui caricheremo un'immagine.
        self.image = pygame.Surface([50, 80]) # Larghezza 50, Altezza 80
        self.image.fill(RED)

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

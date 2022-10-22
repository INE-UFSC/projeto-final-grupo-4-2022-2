import math
import pygame.math

# Constantes da tela
SCREEN_SIZE = pygame.math.Vector2(1024, 768)

# Constantes entity
ASTEROID_TAG = "asteroid"
BULLET_TAG = "bullet"
PLAYER_TAG = "player"
ALIEN_TAG = "alien"

# Cores
ORANGE = (255, 128, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Constante apenas para a versão sem sprites
COLORS_DIC = {ASTEROID_TAG: RED, BULLET_TAG: GREEN,
          PLAYER_TAG: BLUE, ALIEN_TAG: ORANGE}

# Constantes player
PLAYER_SIZE = 10
MAX_VELOCITY_OF_PLAYER = 70
MAX_LIVES = 5

# Constantes asteroid (Só valores positivos)
SMALL_ASTEROID_SIZE = 8
MEDIUM_ASTEROID_SIZE = 16
BIG_ASTEROID_SIZE = 32

CORRECTION_CONSTANT = 800
SMALL_ASTEROID_VELOCITY = CORRECTION_CONSTANT / SMALL_ASTEROID_SIZE
MEDIUM_ASTEROID_VELOCITY = CORRECTION_CONSTANT / MEDIUM_ASTEROID_SIZE
BIG_ASTEROID_VELOCITY = CORRECTION_CONSTANT / BIG_ASTEROID_SIZE

# Constantes bullet
BULLET_SIZE = 2
VELOCITY_OF_BULLET = 10
BULLET_LIFE_TIME = 10

# Constantes Alien
ALIEN_SIZE = 10
ALIEN_VELOCITY = 40
MOVE_COOLDOWN = 3
ALIEN_SHOT_COOLDOWN = 5
DIRECTIONS = (pygame.math.Vector2(math.sqrt(2)/2, math.sqrt(2)/2),
              pygame.math.Vector2(1, 0),
              pygame.math.Vector2(math.sqrt(2)/2, -math.sqrt(2)/2))

# Constantes weapon
WEAPON_COOLDOWN = 1
MAX_AMMUNITION = 1000

# Constantes shooter
# So that the bullet does not spawn inside alien/player and trigger an unwanted on_collision
RADIUS_MULTIPLIER = 1.1

# Constantes score
DESTROY_SCORE = 10
TIME_SCORE = 5
TIME_TO_SCORE = 20

# Constants AlienSpawn
ALIEN_SPAWN_COOLDOWN = 5


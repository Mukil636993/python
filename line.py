import pygame
import math
import sys

pygame.init()

# --- Window setup ---
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG Enemy Line of Sight Detection")

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 60, 60)
GREEN = (60, 255, 60)
GRAY = (100, 100, 100)

# --- Game setup ---
clock = pygame.time.Clock()
FPS = 60

# --- Entities ---
player = pygame.Rect(100, 100, 30, 30)
enemy = pygame.Rect(600, 400, 30, 30)

walls = [
    pygame.Rect(200, 150, 400, 30),
    pygame.Rect(200, 300, 30, 300),
    pygame.Rect(500, 250, 30, 300),
]

PLAYER_SPEED = 3
ENEMY_SPEED = 2
DETECTION_RANGE = 300

# --- Functions ---
def line_intersects_rect(p1, p2, rect):
    """Check if a line between p1 and p2 intersects a given rect."""
    rect_lines = [
        ((rect.left, rect.top), (rect.right, rect.top)),
        ((rect.right, rect.top), (rect.right, rect.bottom)),
        ((rect.right, rect.bottom), (rect.left, rect.bottom)),
        ((rect.left, rect.bottom), (rect.left, rect.top)),
    ]
    for line in rect_lines:
        if lines_intersect(p1, p2, line[0], line[1]):
            return True
    return False

def ccw(A, B, C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def lines_intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

def has_line_of_sight(player, enemy, walls):
    """Check if there's a clear line of sight between player and enemy."""
    p1 = player.center
    p2 = enemy.center
    for wall in walls:
        if line_intersects_rect(p1, p2, wall):
            return False
    return True

def move_toward(rect, target_pos, speed):
    dx, dy = target_pos[0] - rect.centerx, target_pos[1] - rect.centery
    dist = math.hypot(dx, dy)
    if dist == 0:
        return
    dx, dy = dx / dist, dy / dist
    rect.x += dx * speed
    rect.y += dy * speed

# --- Death function ---
def player_died():
    """Show death screen and quit."""
    font = pygame.font.SysFont("arial", 64, bold=True)
    text = font.render("You Died!", True, WHITE)
    win.fill(RED)
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# --- Main loop ---
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    move_x, move_y = 0, 0
    if keys[pygame.K_w]: move_y = -PLAYER_SPEED
    if keys[pygame.K_s]: move_y = PLAYER_SPEED
    if keys[pygame.K_a]: move_x = -PLAYER_SPEED
    if keys[pygame.K_d]: move_x = PLAYER_SPEED

    # Move player and check wall collision
    player.x += move_x
    for wall in walls:
        if player.colliderect(wall):
            if move_x > 0: player.right = wall.left
            if move_x < 0: player.left = wall.right
    player.y += move_y
    for wall in walls:
        if player.colliderect(wall):
            if move_y > 0: player.bottom = wall.top
            if move_y < 0: player.top = wall.bottom

    # Enemy AI
    distance = math.hypot(player.centerx - enemy.centerx, player.centery - enemy.centery)
    if distance < DETECTION_RANGE and has_line_of_sight(player, enemy, walls):
        move_toward(enemy, player.center, ENEMY_SPEED)

    # --- Check for collision (death) ---
    if player.colliderect(enemy):
        player_died()

    # --- Drawing ---
    win.fill(WHITE)
    for wall in walls:
        pygame.draw.rect(win, GRAY, wall)

    pygame.draw.rect(win, GREEN, player)
    pygame.draw.rect(win, RED, enemy)

    # Debug: draw line of sight
    color = (0, 255, 0) if has_line_of_sight(player, enemy, walls) else (255, 0, 0)
    pygame.draw.line(win, color, player.center, enemy.center, 2)

    pygame.display.flip()

pygame.quit()

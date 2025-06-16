import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 20
BALL_COLOR = (0, 255, 255)  # Green ball
BACKGROUND_COLOR = (0, 0, 0)  # Black background
ACCELERATION = 0.5  # How fast the ball accelerates
FRICTION = 0.95    # Friction to slow the ball down over time

# Create screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Control Game")

# Initialize ball position and velocity
ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
velocity_x, velocity_y = 0, 0

# Target position for the ball to move toward (starts as the ball's position)
target_x, target_y = ball_x, ball_y

# Set the clock for controlling frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for mouse click to set the target position
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the target position to where the mouse clicked
            target_x, target_y = event.pos

    # Calculate the distance and angle to the target
    distance_x = target_x - ball_x
    distance_y = target_y - ball_y
    distance = math.hypot(distance_x, distance_y)

    if distance > 1:  # Only move if the ball is not at the target
        # Normalize the direction (unit vector)
        direction_x = distance_x / distance
        direction_y = distance_y / distance

        # Accelerate toward the target
        velocity_x += direction_x * ACCELERATION
        velocity_y += direction_y * ACCELERATION

    # Apply friction to reduce speed over time
    velocity_x *= FRICTION
    velocity_y *= FRICTION

    # Update ball position based on velocity
    ball_x += velocity_x
    ball_y += velocity_y

    # Fill the screen with background color
    screen.fill(BACKGROUND_COLOR)

    # Draw the ball at the updated position
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_x), int(ball_y)), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
import pygame
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    # Setting up display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Setting up frames and deltatime
    clock = pygame.time.Clock()
    dt = 0

    # Initializing groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Initializing player and add to groups
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Add asteroids to groups
    Asteroid.containers = (asteroids, updatable, drawable)

    # Add groups for asteroidfield - non-drawable and initialize
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()

    # Add shots to groups
    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for item in updatable:
            item.update(dt)

        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                exit(1)

        player.timer -= dt
        # Redraw screen
        pygame.display.flip()
        # Set waiting time so that game pauses for 1/60 seconds after iteration (60 fps)
        # Store deltatime (seconds since last time .tick was called)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

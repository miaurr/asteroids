# import constants
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
import pygame
from constants import *
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
  
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = (clock.tick(60)/1000)


if __name__ == "__main__":
    main()

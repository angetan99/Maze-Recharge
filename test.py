import time
import pygame
import random

pygame.init()

from pygame import K_RIGHT, K_LEFT, K_UP, K_DOWN, K_ESCAPE, QUIT

clock = pygame.time.Clock()

font = pygame.font.SysFont('freesansbold.tff', 32)

frame_rate = 60
start_time = 59

white = (255, 255, 255)
black = (0, 0, 0)

class Player:
    x = 10
    y = 10
    speed = 4

    def __init__(self):
        self.rect = pygame.Rect(0, 0, 30, 44)

    def moveRight(self):
        self.x = self.x + self.speed
        self.rect.x += self.speed

    def moveLeft(self):
        self.x = self.x - self.speed
        self.rect.x -= self.speed

    def moveUp(self):
        self.y = self.y - self.speed
        self.rect.y -= self.speed

    def moveDown(self):
        self.y = self.y + self.speed
        self.rect.y += self.speed

    def collides_with_obstacle(self, obstacles):
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle):
                return True
        return False


class Maze():
    def __init__(self):
        self.maze = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1,
                     1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1,
                     1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1,
                     1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1,
                     1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1,
                     1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1,
                     1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
                     0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
                     0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
                     1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
                     1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1,
                     1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1,
                     1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1,
                     1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1,
                     1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1,
                     1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1,
                     1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        self.wall_rects = []

    def draw(self, display_, image_):
        row = 0
        col = 0
        for i in range(0, 400):
            if i % 20 == 0:
                row = 30
                col = col + 30
            if self.maze[i] == 1:
                rect = pygame.Rect(row, col + 8, 22, 12)  # Create a rect for the wall tile
                self.wall_rects.append(rect)  # Add the rect to the list

                display_.blit(image_, (row, col))

            row = row + 30

class Obstacles():
    def __init__(self):
        self.obstacleMaze = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
                            0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,
                            0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
                            0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0,
                            0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0,
                            0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0,
                            0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0,
                            0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
                            1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1,
                            1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1,
                            0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
                            0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0,
                            0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0,
                            0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0,
                            0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0,
                            0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
                            0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,
                            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.obstaclerects = {}
        self.spawnFrequency = 3 # Spawn one more obstacle every three seconds
        self.alreadyDone = set()

    def addRandomObstacle(self):
        row = random.randint(0, 18)
        col = random.randint(0, 18)
        while row * 20 + col in self.obstaclerects.keys() or self.obstacleMaze[row * 20 + col] == 1:
            row = random.randint(0, 19)
            col = random.randint(0, 18)
        rect = pygame.Rect((row+1) * 30 + 30, (col+1) * 30 + 30, 20, 20)
        self.obstaclerects[row * 20 + col] = rect


class Boba:
    def __init__(self):
        self.rect = pygame.Rect(300, 120, 60, 60)

class Sleep:
    def __init__(self):
        self.rect = pygame.Rect(305, 480, 46, 55)

class Health:
    def __init__(self):
        self._health_ = None
        self._healthlist = []
        self._healthlist.append(pygame.image.load("health5.png"))
        self._healthlist.append(pygame.image.load("health4.png"))
        self._healthlist.append(pygame.image.load("health3.png"))
        self._healthlist.append(pygame.image.load("health2.png"))
        self._healthlist.append(pygame.image.load("health1.png"))
        self._healthlist.append(pygame.image.load("health0.png"))

    def draw_Health(self, display_, total_seconds):
        eye = total_seconds // 10
        health = self._healthlist[abs(eye-5)]
        DEFAULT_IMAGE_SIZE = (100, 20)
        health = pygame.transform.scale(health, DEFAULT_IMAGE_SIZE)
        self._health_ = health.convert()
        display_.blit(self._health_, (300, 5))


class App:
    windowWidth = 950
    windowHeight = 665
    player = 0

    def __init__(self):
        self._running = True
        self._display_ = None
        self._image_ = None
        self._block_ = None
        self.player = Player()
        self.maze = Maze()
        self._boba_ = None
        self._sleep_ = None
        self.health = Health()
        self._spike_ = None
        self.obstacle = Obstacles()
        self._instructions = None


    def on_init(self):
        pygame.init()
        self._display_ = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        self.rect = pygame.Rect(320, 320, 160, 160)
        self._bob_ = (300, 120, 60, 60)
        self._slep_ = (305, 480, 46,55)


        pygame.display.set_caption('Maze Recharge game')
        self._running = True
        image = pygame.image.load("mazecharacter (1).png")
        DEFAULT_IMAGE_SIZE = (17, 26)
        image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
        self._image_ = image.convert()

        crystal = pygame.image.load("crystal.png")
        DEFAULT_IMAGE_SIZE = (30, 30)
        crystal = pygame.transform.scale(crystal, DEFAULT_IMAGE_SIZE)
        self._block_ = crystal.convert()

        boba = pygame.image.load("boba.png")
        DEFAULT_IMAGE_SIZE = (60, 60)
        boba = pygame.transform.scale(boba, DEFAULT_IMAGE_SIZE)
        self._boba_ = boba.convert()

        sleep = pygame.image.load("sleep.png")
        DEFAULT_IMAGE_SIZE = (46,55)
        sleep = pygame.transform.scale(sleep, DEFAULT_IMAGE_SIZE)
        self._sleep_ = sleep.convert()

        spike = pygame.image.load("spike.png")
        DEFAULT_IMAGE_SIZE = (30, 30)
        spike = pygame.transform.scale(spike, DEFAULT_IMAGE_SIZE)
        self._spike_ = spike.convert()

        instructions = pygame.image.load("instructions.png")
        DEFAULT_IMAGE_SIZE = (250, 700)
        instructions = pygame.transform.scale(instructions, DEFAULT_IMAGE_SIZE)
        self._instructions = instructions.convert()


    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_.fill((0, 0, 0))
        self.maze.draw(self._display_, self._block_)  # Draw the maze first
        self._display_.blit(self._image_, (self.player.x, self.player.y))  # Draw the player
        self._display_.blit(self._boba_, (300, 120))
        self._display_.blit(self._sleep_, (305, 480))
        output = "Time left:"
        text = font.render(output, True, (255, 255, 255))
        self._display_.blit(text, [100, 5])
        self._display_.blit(self._instructions, (665, 50))

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        WIDTH = 950
        HEIGHT = 665
        frame_count = 0
        new_seconds = 0
        newVar = False
        Var = False
        prev_time = time.time()
        pastSpikes = []

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                if self.player.x < WIDTH:
                    self.player.moveRight()

            if keys[K_LEFT]:
                if self.player.x > 0:
                    self.player.moveLeft()

            if keys[K_UP]:
                if self.player.y > 0:
                    self.player.moveUp()

            if keys[K_DOWN]:
                if self.player.y < HEIGHT:
                    self.player.moveDown()

            if keys[K_ESCAPE]:
                self._running = False

            total_seconds = int(start_time - (frame_count // frame_rate) + new_seconds)
            if total_seconds < 0:
                total_seconds = 0
                self.player.y = 1000
                newFont = pygame.font.SysFont('freesansbold.tff', 80)
                text = newFont.render("Game Over", True, (230, 15, 15))
                self._display_.blit(text, [190, 300])

            if total_seconds >= 0 and self.player.x > 600:
                self.player.y = 1000
                total_seconds = 0
                newFont = pygame.font.SysFont('freesansbold.tff', 80)
                text = newFont.render("You Win!", True, (10, 255, 88))
                self._display_.blit(text, [190, 300])


            minutes = total_seconds // 60
            seconds = total_seconds % 60
            output_string = "{0:02}:{1:02}".format(minutes, seconds)

            text = font.render(output_string, True, (255, 255, 255))
            self._display_.blit(text, [202, 5.5])
            current_time = time.time()
            frame_count += (current_time - prev_time) * frame_rate
            prev_time = current_time
            clock.tick(frame_rate)

            self.health.draw_Health(self._display_, total_seconds)

            if self.player.rect.colliderect(self._slep_):
                if Var:
                    if keys[K_RIGHT]:
                        self.player.moveLeft()
                    elif keys[K_LEFT]:
                        self.player.moveRight()
                    elif keys[K_UP]:
                        self.player.moveDown()
                    elif keys[K_DOWN]:
                        self.player.moveUp()

                    new_seconds = 20
                    newVar = True
                else:
                    if keys[K_RIGHT]:
                        self.player.moveLeft()
                    elif keys[K_LEFT]:
                        self.player.moveRight()
                    elif keys[K_UP]:
                        self.player.moveDown()
                    elif keys[K_DOWN]:
                        self.player.moveUp()

                    new_seconds = 10
                    newVar = True

            if self.player.rect.colliderect(self._bob_):
                if newVar:
                    if keys[K_RIGHT]:
                        self.player.moveLeft()
                    elif keys[K_LEFT]:
                        self.player.moveRight()
                    elif keys[K_UP]:
                        self.player.moveDown()
                    elif keys[K_DOWN]:
                        self.player.moveUp()

                    new_seconds = 20
                    Var = True

                else:
                    if keys[K_RIGHT]:
                        self.player.moveLeft()
                    elif keys[K_LEFT]:
                        self.player.moveRight()
                    elif keys[K_UP]:
                        self.player.moveDown()
                    elif keys[K_DOWN]:
                        self.player.moveUp()

                    new_seconds = 10
                    Var = True


            for wall_rect in self.maze.wall_rects:
                if self.player.rect.colliderect(wall_rect):
                    if keys[K_RIGHT]:
                        self.player.moveLeft()
                    if keys[K_LEFT]:
                        self.player.moveRight()
                    if keys[K_UP]:
                        self.player.moveDown()
                    if keys[K_DOWN]:
                        self.player.moveUp()

            if len(self.obstacle.obstaclerects) < (start_time - total_seconds) // self.obstacle.spawnFrequency:
                self.obstacle.addRandomObstacle()

            for rect in self.obstacle.obstaclerects.values():
                self._display_.blit(self._spike_, (rect.x, rect.y))

            if self.player.collides_with_obstacle(self.obstacle.obstaclerects.values()):
                if keys[K_RIGHT]:
                    self.player.moveLeft()
                if keys[K_LEFT]:
                    self.player.moveRight()
                if keys[K_UP]:
                    self.player.moveDown()
                if keys[K_DOWN]:
                    self.player.moveUp()


            pygame.display.update()

            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_init()
    theApp.on_execute()
import pygame, random

from Player import Player

# SCALING = 0.3

class Vine(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        This class represents the vine in the game.
        :param x:
        :param y:
        """
        super().__init__()
        original_image = pygame.image.load(
            "images/new_vine.png"
        ).convert_alpha()
        self.image = pygame.transform.scale(
            original_image,
            (
                50,
                50,
                # int(original_image.get_width() * SCALING),
                # int(original_image.get_height() * SCALING),
            ),
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class VineGroup(pygame.sprite.Group):
    def __init__(self):
        """
        This class represents the vine group in the game.
        """
        super().__init__()
        self.vine_active=False
    
    def is_empty(self):
        return len(self.sprites()) == 0
    
    def insert_vine(self, x: int, y: int, size: int, screen_height: int):
        """
        This method inserts a vine to the vine group.
        :param x:
        :param y:
        :param size:
        :param screen_height:
        :return:
        """
        vine = self.select_vine_to_insert(x, y, size, screen_height)
        collision = pygame.sprite.spritecollideany(vine, self)
        if not collision:
            self.add(vine)
        else:
            if random.random() < 0.01:
                self.add(vine)

    def select_vine_to_insert(self, x: int, y: int, size: int, screen_height: int) -> Vine:
        """
        This method selects a vine to insert.
        :param x:
        :param y:
        :param size:
        :param screen_height:
        :return:
        """
        vine_x = x + size // 2 - 5
        vine_y = screen_height - 10 if self.is_empty() else (self.sprites()[0].rect.top + y) // 2
        vine = Vine(vine_x, vine_y)
        return vine

    def make_vine_to_top(self, player: Player):
        """
        This method makes the vine to the top.
        :param player:
        :return:
        """
        self.vine_active=True
        if self.is_empty():
            return
        # make every vine to the top
        for vine_x in range(0, 800, 50):
            for vine_y in range(600-50,0,-50):
                vine=Vine(vine_x,vine_y)
                self.add(vine)


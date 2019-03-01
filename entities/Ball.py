import pyglet
from system.Component import Component
import config


class Ball(Component):

    def __init__(self, *args, **kwargs):
        """
        Creates a sprite using a ball image.
        """
        super(Ball, self).__init__(*args, **kwargs)
        self.speed = kwargs.get('speed', 5)
        self.ball_image = pyglet.image.load('assets/ball.png')
        self.width = self.ball_image.width
        self.height = self.ball_image.height
        self.ball_sprite = pyglet.sprite.Sprite(self.ball_image, self.x, self.y)
        self.x_direction = 1
        self.y_direction = 1

        print('Ball Created')

    def update_self(self):
        """
        Increments x and y value and updates position.
        Also ensures that the ball does not leave the screen area by changing its axis direction
        :return:
        """
        self.x += (self.speed * self.x_direction)
        self.y += (self.speed * self.y_direction)
        self.ball_sprite

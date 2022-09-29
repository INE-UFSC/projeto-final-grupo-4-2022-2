from model.entities.bullet import Bullet
import utility.constants as CONST
import pygame

class RubberBullet(Bullet):

    def move(self, dt) -> None:
        body = self.get_body()

        position = body.get_position()
        if position.x < 0 or CONST.SCREEN_SIZE.x < position.x:

            new_x = -(self.get_body().get_velocity().x)
            y = self.get_body().get_velocity().y

            velocity_switch_x = pygame.Vector2(new_x, y)
            self.get_body().set_velocity(velocity_switch_x)

        if position.y < 0 or CONST.SCREEN_SIZE.y < position.y:

            x = self.get_body().get_velocity().x
            new_y = -(self.get_body().get_velocity().y)

            velocity_switch_x = pygame.Vector2(x, new_y)
            self.get_body().set_velocity(velocity_switch_x)

        body.set_position(body.get_position() + body.get_velocity()*dt)
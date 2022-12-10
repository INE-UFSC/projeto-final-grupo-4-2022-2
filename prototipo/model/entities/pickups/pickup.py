
from model.body import Body
from model.entities.abstractentity import Entity
from utility.constants.pickup_constants import PickUpConstants
from utility.data.image_loader import ImageLoader


class PickUp(Entity):

    def __init__(self, body: Body) -> None:
        super().__init__(body, PickUpConstants().tag)

    def destroy(self) -> None:
        pass

    def move(self, dt: float) -> None:
        pass

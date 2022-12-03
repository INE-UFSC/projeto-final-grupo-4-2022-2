
from model.body import Body
from model.entities.abstractentity import Entity
from utility.constants.pickup_constants import PickUpConstants
from utility.data.image_loader import ImageLoader


class PickUp(Entity):

    __original_image = ImageLoader().load(PickUpConstants().image_path,
                                          (PickUpConstants().size, PickUpConstants().size))

    def __init__(self, body: Body) -> None:
        super().__init__(body, PickUpConstants().tag)

        self.set_image(PickUp.__original_image)
        self.set_rect(self.get_image().get_rect())

    def destroy(self) -> None:
        pass

    def move(self, dt: float) -> None:
        pass

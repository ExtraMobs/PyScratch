import pygame

from ..misc.animation import Animation
from .shadingnode import ShadingNode


class HitBox:
    def __init__(self, child, rect):
        self.update(child, rect)

    def update(self, surface, rect):
        self.rect = pygame.FRect(surface.get_bounding_rect())
        self.rect.x += rect.x
        self.rect.y += rect.y


class Rotation:
    def __init__(self):
        self.angle = 0

    def update(self, target):
        if self.angle != 0:
            target.surface = pygame.transform.rotate(target.surface, self.angle)


class UpdateManager:
    def __init__(self, graphic_node):
        self.node = graphic_node
        self.surface_id = id(self.node.surface)
        self.animation_frame = None
        self.rotation_angle = None

    def update(self):
        animation_updated = False
        if is_same_surf := (self.surface_id == id(self.node.surface)):
            if self.node.animation is not None:
                self.node.animation.update()
                if (
                    animation_updated := (
                        new_animation_frame := self.node.animation.frame_index
                    )
                    != self.animation_frame
                ):
                    self.node.surface = self.node.animation.current_frame
                    self.surface_id = id(self.node.surface)
                    self.animation_frame = new_animation_frame

        if rotation_updated := (
            (new_rotation_angle := self.node.rotation.angle) != self.rotation_angle
            or not is_same_surf
        ):
            self.node.rotation.update(self)
            self.rotation_angle = new_rotation_angle

        if animation_updated or rotation_updated:
            self.node.rect.size = self.node.surface.get_size()

        self.node.shader_manager.update()


class GraphicNode(ShadingNode):
    surface = None
    rect = None
    offset = None
    bg = None

    hitbox = None
    animation = None
    rotation = None

    active = None
    visible = None

    def __init__(self, image):
        super().__init__()

        if type(image) is Animation:
            self.animation = image
            self.surface = image.current_frame
        else:
            self.surface = image
        self.rect = self.surface.get_frect()
        self.offset = pygame.Vector2(0, 0)
        self.hitbox = HitBox(self.surface, self.rect)
        self.rotation = Rotation()

        self.visible = True
        self.active = True

        self.__update_manager = UpdateManager(self)

    def update(self):
        if self.active:
            self.__update_manager.update()
            super().update()

    def draw(self, surface=None):
        if self.visible:
            self.shader_manager.draw(self.surface)
            self.hitbox.update(self.surface, self.rect)

            super().draw()

            if surface is None:
                surface = self.parent.surface
            surface.blit(
                self.surface,
                (self.rect.x + self.offset.x, self.rect.y + self.offset.y),
            )

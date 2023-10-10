import numpy
import pygame

from gameengine.misc.shader import FakeShader


class ColorMAShader(FakeShader):
    def __init__(self, color_m, color_a, cache_size=3):
        super().__init__()
        self.color_m = [color / 255 for color in color_m]
        self.color_a = list(color_a)
        self.cache_size = cache_size
        self.current_surf_ids = []

    def draw(self, target_surf):
        if not (surf_id := id(target_surf)) in self.current_surf_ids:
            self.current_surf_ids.append(surf_id)
            if len(self.current_surf_ids) > self.cache_size:
                del self.current_surf_ids[0]

            surf_array = pygame.surfarray.pixels3d(target_surf)
            surf_array_alpha = pygame.surfarray.pixels_alpha(target_surf)

            numpy.multiply(
                self.color_m,
                surf_array,
                surf_array,
                casting="unsafe",
            )
            if len(self.color_m) > 3:
                numpy.multiply(
                    sum(self.color_m[3:]),
                    surf_array_alpha,
                    surf_array_alpha,
                    casting="unsafe",
                )

            numpy.add(self.color_a[:3], surf_array, surf_array, casting="unsafe")
            if len(self.color_a) > 3:
                numpy.add(
                    sum(self.color_a[3:]),
                    surf_array_alpha,
                    surf_array_alpha,
                    casting="unsafe",
                )

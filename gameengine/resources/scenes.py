from typing import Any

from gameengine.nodes.scene import Scene

scenes = {}


def set(name: Any, scene_class: Scene) -> None:
    scenes[name] = scene_class


def add(**name_and_scene_class) -> None:
    scenes.update(name_and_scene_class)


def get(name: Any) -> Scene:
    return scenes[name]

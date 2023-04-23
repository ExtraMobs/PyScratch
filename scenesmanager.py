class ScenesManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene_id = None

    def set_scene(self, id_, scene):
        self.scenes[id_] = scene

    def set_scenes(self, *ids_and_scenes):
        if len(ids_and_scenes) % 2 != 0:
            raise Exception("args length are not peers")
        else:
            for index, id_or_scene in enumerate(ids_and_scenes):
                if index % 2 == 0:
                    id_ = id_or_scene
                else:
                    self.set_scene(id_, id_or_scene)

    def get_scene(self, id_):
        return self.scenes[id_]

    def get_scenes(self, *ids):
        to_return = []
        for id_ in ids:
            to_return.append(id_)
        return to_return

    def remove_scene(self, id_):
        del self.scenes[id_]

    def remove_scenes(self, *ids):
        for id_ in ids:
            self.remove_scene(id_)

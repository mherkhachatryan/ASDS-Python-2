class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x, y):
        print(f"Draw tree at {x, y} on {canvas}")


class TreeFactory:
    _tree_types = {}

    def get_tree_type(self, name, color, texture):
        key = self._get_key(name, color, texture)
        if not self._tree_types.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._tree_types[key] = TreeType(name, color, texture)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._tree_types[key]

    def _get_key(self, name, color, texture):
        return "_".join([name, color, texture])


class Tree:
    def __init__(self, x, y, type_: TreeType):
        self.x = x
        self.y = y
        self.type_ = type_

    def draw(self, canvas):
        self.type_.draw(canvas, self.x, self.y)


class Forest:
    trees = []

    def plant_tree(self, x, y, name, color, texture):
        type_ = TreeFactory().get_tree_type(name, color, texture)
        tree = Tree(x, y, type_)
        self.trees.append(tree)

    def draw(self, canvas):
        for tree in self.trees:
            tree.draw(canvas)


if __name__ == "__main__":
    forest = Forest()

    forest.plant_tree(1, 1, "beryoza", "green", "plain")

    forest.draw("screen")

    forest.plant_tree(1, 1, "beryoza", "green", "plain")


    forest.draw("screen")
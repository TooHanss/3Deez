class Cube:
    def __init__(self) -> None:
        self.tris = [
            # south
            [(0.0, 0.0, 0.0), (0.0, 1.0, 0.0), (1.0, 1.0, 0.0)],
            [(0.0, 0.0, 0.0), (1.0, 1.0, 0.0), (1.0, 0.0, 0.0)],
            # east
            [(1.0, 0.0, 0.0), (1.0, 1.0, 0.0), (1.0, 1.0, 1.0)],
            [(1.0, 0.0, 0.0), (1.0, 1.0, 1.0), (1.0, 0.0, 1.0)],
            # north
            [(1.0, 0.0, 1.0), (1.0, 1.0, 1.0), (0.0, 1.0, 1.0)],
            [(1.0, 0.0, 1.0), (0.0, 1.0, 1.0), (0.0, 0.0, 1.0)],
            # west
            [(0.0, 0.0, 1.0), (0.0, 1.0, 1.0), (0.0, 1.0, 0.0)],
            [(0.0, 0.0, 1.0), (0.0, 1.0, 0.0), (0.0, 0.0, 0.0)],
            # top
            [(0.0, 1.0, 0.0), (0.0, 1.0, 1.0), (1.0, 1.0, 1.0)],
            [(0.0, 1.0, 0.0), (1.0, 1.0, 1.0), (1.0, 1.0, 0.0)],
            # bottom
            [(1.0, 0.0, 1.0), (0.0, 0.0, 1.0), (0.0, 0.0, 0.0)],
            [(1.0, 0.0, 1.0), (0.0, 0.0, 0.0), (1.0, 0.0, 0.0)],
        ]


if __name__ == "__main__":
    cube = Cube()
    print("\033c", end="")
    for tri in cube.tris:
        print(tri)

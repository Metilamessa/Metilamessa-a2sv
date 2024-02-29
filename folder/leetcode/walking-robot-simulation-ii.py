class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.position = 0
        self.isOrigin = True
        self.moves = [(0, 0)] + [(i, 0) for i in range(1, width)] + [(width - 1, j) for j in range(1, height)] + [(i, height - 1) for i in range(width - 2, -1, -1)] + [(0, j) for j in range(height - 2, 0, -1)]
        self.directions = ['South'] + ['East'] * (width - 1) + ['North'] * (height - 1) + ['West'] * (width - 1) + ['South'] * (height - 2)

    def step(self, num: int) -> None:
        self.isOrigin = False
        self.position = (self.position + num) % len(self.moves)

    def getPos(self) -> List[int]:
        return self.moves[self.position]

    def getDir(self) -> str:
        return 'East' if self.isOrigin else self.directions[self.position]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
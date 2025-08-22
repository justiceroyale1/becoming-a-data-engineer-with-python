class Point:
    def __init__(self, x, y):
            self.x = x
            self.y = y

def display_point(point):
    match point:
        case Point(x = 0, y = 0):
            print("Origin")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case _:
            print("Not a point")

display_point(Point(0, 0))
display_point(Point(1, 0))
display_point(Point(0, 1))
display_point("Hello world!")
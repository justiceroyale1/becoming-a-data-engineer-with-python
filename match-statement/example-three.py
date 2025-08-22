def display_point(point):
    match point:
        case (0, 0):
            print('Origin')
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")

display_point((0, 0))
display_point((0, 1))
display_point((1, 0))
display_point((2, 3))
display_point('Hello')
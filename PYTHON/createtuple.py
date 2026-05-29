def show_coordinates(coords):
    if len(coords) != 2:
        return "Invalid coordinates"

    print(f"Coordinates: ({coords[0]}, {coords[1]})")

point = (12, 25)

show_coordinates(point)
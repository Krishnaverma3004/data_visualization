# shapes3d.py


PI = 3.1416

# ------------------ Cube ------------------
def cube_volume(side):
    return side ** 3

def cube_surface_area(side):
    return 6 * side ** 2

def cube_curved_surface_area(side):
    return 4 * side ** 2

# ------------------ Cuboid ------------------
def cuboid_volume(length, width, height):
    return length * width * height

def cuboid_surface_area(length, width, height):
    return 2 * (length*width + width*height + length*height)

def cuboid_curved_surface_area(length, width, height):
    return 2 * height * (length + width)

# ------------------ Cylinder ------------------
def cylinder_volume(radius, height):
    return PI * radius**2 * height

def cylinder_surface_area(radius, height):
    return 2 * PI * radius * (radius + height)

def cylinder_curved_surface_area(radius, height):
    return 2 * PI * radius * height

# ------------------ Cone ------------------
def cone_volume(radius, height):
    return (1/3) * PI * radius**2 * height

def cone_surface_area(radius, height):
    l = (radius**2 + height**2) ** 0.5  # slant height using **0.5
    return PI * radius * (radius + l)

def cone_curved_surface_area(radius, height):
    l = (radius**2 + height**2) ** 0.5  # slant height
    return PI * radius * l

# ------------------ Sphere ------------------
def sphere_volume(radius):
    return (4/3) * PI * radius**3

def sphere_surface_area(radius):
    return 4 * PI * radius**2

# ------------------ Hemisphere ------------------
def hemisphere_volume(radius):
    return (2/3) * PI * radius**3

def hemisphere_surface_area(radius):
    return 3 * PI * radius**2  # curved + base
from shape3D import (
    cylinder_volume, cylinder_curved_surface_area, cylinder_surface_area,
    cone_curved_surface_area, cone_surface_area, cone_volume,
    cuboid_curved_surface_area, cuboid_surface_area, cuboid_volume
)

# Cylinder
radius = float(input("Enter cylinder radius: "))
height = float(input("Enter cylinder height: "))

print("Cylinder Curved Surface Area:", cylinder_curved_surface_area(radius, height))
print("Cylinder Surface Area:", cylinder_surface_area(radius, height))
print("Cylinder Volume:", cylinder_volume(radius, height))

# Cone
radius_cone = float(input("Enter cone radius: "))
height_cone = float(input("Enter cone height: "))

print("Cone Curved Surface Area:", cone_curved_surface_area(radius_cone, height_cone))
print("Cone Surface Area:", cone_surface_area(radius_cone, height_cone))
print("Cone Volume:", cone_volume(radius_cone, height_cone))

# Cuboid
length = float(input("Enter cuboid length: "))
width = float(input("Enter cuboid width: "))
height_cuboid = float(input("Enter cuboid height: "))

print("Cuboid Curved Surface Area:", cuboid_curved_surface_area(length, width, height_cuboid))
print("Cuboid Surface Area:", cuboid_surface_area(length, width, height_cuboid))
print("Cuboid Volume:", cuboid_volume(length, width, height_cuboid))
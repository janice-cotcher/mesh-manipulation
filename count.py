from stl import mesh
before = "dog_thick_ears.stl"
after = "thick_ears_simplified.stl"

before_mesh = mesh.Mesh.from_file(before)
after_mesh = mesh.Mesh.from_file(after)

print(f"Before: {len(before_mesh)}")
print(f"After: {len(after_mesh)}")
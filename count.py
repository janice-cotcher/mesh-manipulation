from stl import mesh
before = "durins_door.stl"
after = "durins_door_simplified.stl"

before_mesh = mesh.Mesh.from_file(before)
after_mesh = mesh.Mesh.from_file(after)

print(f"Before: {len(before_mesh)}")
print(f"After: {len(after_mesh)}")
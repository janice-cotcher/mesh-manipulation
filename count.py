from stl import mesh
before = "dog.stl"
after = "decimatedMesh.stl"

before_mesh = mesh.Mesh.from_file(before)
after_mesh = mesh.Mesh.from_file(after)

print(f"Before: {len(before_mesh)}")
print(f"After: {len(after_mesh)}")
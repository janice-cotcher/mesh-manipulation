import sys
from stl import mesh
# Capture elements passed after the script name
before = sys.argv[1]
after = sys.argv[2]

before_mesh = mesh.Mesh.from_file(before)
after_mesh = mesh.Mesh.from_file(after)

print(f"Before: {len(before_mesh)}")
print(f"After: {len(after_mesh)}")
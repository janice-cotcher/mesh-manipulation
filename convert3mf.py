import meshlib.mrmeshpy as mr

# Load the 3MF file geometry
mesh = mr.loadMesh("input_model.3mf")

# Perform mesh operations if needed (e.g., healing, decimation)
# ...

# Export to a 3MF or an alternative format
mr.saveMesh(mesh, "output_model.3mf")

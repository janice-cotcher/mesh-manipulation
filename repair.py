import meshlib.mrmeshpy as mrmeshpy
import sys
from stl import mesh

input_file = sys.argv[1]
output_file = sys.argv[2]

# mesh to be repair and/or remeshed
mesh = mrmeshpy.loadMesh(input_file)

# Find single edge for each hole in the mesh
hole_edges = mesh.topology.findHoleRepresentiveEdges()
 
# Filling parameters
params = mrmeshpy.FillHoleParams()
params.metric = mrmeshpy.getUniversalMetric(mesh)
 
# Alternatively, mrmeshpy.fillHoles(mesh, hole_edges, params) fills all holes at once.
for e in hole_edges:
    # Fill hole represented by `e`
    mrmeshpy.fillHole(mesh, e, params)

# you can set various parameters for the resolving process; see the documentation for more info
params = mrmeshpy.FixMeshDegeneraciesParams()
params.maxDeviation = 1e-5 * mesh.computeBoundingBox().diagonal()
params.tinyEdgeLength = 1e-3
 
mrmeshpy.fixMeshDegeneracies(mesh, params)

# Optimize Mesh by repacking
mesh.packOptimally()

# Decimate parameters
settings = mrmeshpy.DecimateSettings()

# Decimation stop threshold
settings.maxError = 0.05 # Maximum error when decimation stops

# Number of parts to simultaneous process
settings.subdivideParts = 8

# Decimate mesh
mrmeshpy.decimateMesh(mesh, settings)

# Save result
mrmeshpy.saveMesh(mesh, output_file)

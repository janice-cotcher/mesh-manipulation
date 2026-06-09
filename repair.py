import meshlib.mrmeshpy as mrmeshpy
import sys
from stl import mesh
# Capture elements passed after the script name
input_file = sys.argv[1]
output_file = sys.argv[2]

# Load an imperfect or broken 3D model
mesh = mrmeshpy.loadMesh(input_file)

# Find single edge for each hole in mesh
hole_edges = mesh.topology.findHoleRepresentiveEdges()
 
# Setup filling parameters
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

# Repack mesh optimally.
# It's not necessary but highly recomrmeshpyended to achieve the best performance in parallel processing
mesh.packOptimally()

# Setup decimate parameters
settings = mrmeshpy.DecimateSettings()

# Decimation stop thresholds, you may specify one or both
# settings.maxDeletedFaces = 1000000 # Number of faces to be deleted
settings.maxError = 0.05 # Maximum error when decimation stops

# Number of parts to simultaneous processing, greatly improves performance by cost of minor quality loss.
# Recomrmeshpyended to set to number of CPU cores or more available for the best performance
settings.subdivideParts = 8

# Decimate mesh
mrmeshpy.decimateMesh(mesh, settings)

# Save result
mrmeshpy.saveMesh(mesh, output_file)

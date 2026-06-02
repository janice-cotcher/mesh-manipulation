import meshlib.mrmeshpy as mrmeshpy

# 1. Load the SVG file as polylines
polyline_path = "durins_door.svg"
polylines = mrmeshpy.LinesLoad.fromSvg(polyline_path)
contours = polylines.contours()


# 2. Triangulate the contours to create a flat mesh
# By default, this generates a Mesh object from the 2D closed paths
# # Create an empty bit set for faces
# faces = mrmeshpy.FaceBitSet()
# faces.setAll(True)

# # Extrude the 2D mesh into a 3D solid block
# # distance controls how thick the 3D extrusion will be ($thickness$)
# extruded_mesh = mrmeshpy.offsetMesh(mesh, distance=5.0)

# # 3. Export the resulting mesh (e.g., to an STL or OBJ file)
# mrmeshpy.saveMesh(extruded_mesh, "output_mesh.stl")

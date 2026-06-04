import meshlib.mrmeshpy as mrmeshpy

# 1. Load the SVG file as polylines
polyline_path = "durins_door.svg"
polylines = mrmeshpy.LinesLoad.fromSvg(polyline_path)
contours = polylines.contours()
count = 0
for contour in contours:
    # print(type(contour))
    for item in contour:
        for point in item:
            print(point)
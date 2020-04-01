import bpy

solved_state = {
'Cube': Vector((0.0, 0.0, 0.0)),
'Cube.001': Vector((2.0, 0.0, 0.0)),
'Cube.002': Vector((-2.0, 0.0, 0.0)),
'Cube.003': Vector((0.0, 2.0, 0.0)),
'Cube.004': Vector((2.0, 2.0, 0.0)),
'Cube.005': Vector((-2.0, 2.0, 0.0)),
'Cube.006': Vector((0.0, -2.0, 0.0)),
'Cube.007': Vector((2.0, -2.0, 0.0)),
'Cube.008': Vector((-2.0, -2.0, 0.0)),
'Cube.009': Vector((0.0, 0.0, 2.0)),
'Cube.010': Vector((2.0, 0.0, 2.0)),
'Cube.011': Vector((-2.0, 0.0, 2.0)),
'Cube.012': Vector((0.0, 2.0, 2.0)),
'Cube.013': Vector((2.0, 2.0, 2.0)),
'Cube.014': Vector((-2.0, 2.0, 2.0)),
'Cube.015': Vector((0.0, -2.0, 2.0)),
'Cube.016': Vector((2.0, -2.0, 2.0)),
'Cube.017': Vector((-2.0, -2.0, 2.0)),
'Cube.018': Vector((0.0, 0.0, -2.0)),
'Cube.019': Vector((2.0, 0.0, -2.0)),
'Cube.020': Vector((-2.0, 0.0, -2.0)),
'Cube.021': Vector((0.0, 2.0, -2.0)),
'Cube.022': Vector((2.0, 2.0, -2.0)),
'Cube.023': Vector((-2.0, 2.0, -2.0)),
'Cube.024': Vector((0.0, -2.0, -2.0)),
'Cube.025': Vector((2.0, -2.0, -2.0)),
'Cube.026': Vector((-2.0, -2.0, -2.0))
}

bpy.ops.object.select_all(action='SELECT')

mani = str(input())
ax,pl,arg = manipulation[mani]
rotation(ax,pl,arg)

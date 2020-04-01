import bpy
import math

def rotation(axis, place,arg=math.pi/2):
    l = ("x", "y", "z")
    index = l.index(axis)
    bpy.ops.object.select_all(action='DESELECT')
    for obj in bpy.data.objects:
        if round(obj.location[index]) == place and obj.name.startswith("Cube"):
            obj.select_set(state=True)
    input_axis = str.upper(axis)
    input_list_axis = [i == str(axis) for i in l]
    return bpy.ops.transform.rotate(value=math.pi/2,
                            orient_axis=input_axis,
                            orient_type='GLOBAL',
                            orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)),
                            orient_matrix_type='GLOBAL',
                            constraint_axis=input_list_axis,
                            mirror=True,
                            use_proportional_edit=False,
                            proportional_edit_falloff='SMOOTH',
                            proportional_size=1,
                            use_proportional_connected=False,
                            use_proportional_projected=False)



manipulation = {
"U": ("z",2,math.pi/2),
"U2": ("z",2,math.pi),
"U3": ("z",2,math.pi/2),
"B": ("x",-2,math.pi/2),
"B2": ("x",-2,math.pi),
"B3": ("x",-2,math.pi/2),
"D": ("z",-2,math.pi/2),
"D2": ("z",-2,math.pi),
"D3": ("z",-2,math.pi/2),
"F": ("x",2,math.pi/2),
"F2": ("x",2,math.pi),
"F3": ("x",2,math.pi/2),
"L": ("y",-2,math.pi/2),
"L2": ("y",-2,math.pi),
"L3": ("y",-2,math.pi/2),
"R": ("y",2,math.pi/2),
"R2": ("y",2,math.pi),
"R3": ("y",2,math.pi/2),
}

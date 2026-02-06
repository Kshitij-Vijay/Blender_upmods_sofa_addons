import bpy
import os
from .compass import *
from mathutils import Vector

def world_bounds(obj):
    corners = [obj.matrix_world @ Vector(c) for c in obj.bound_box]
    xs = [v.x for v in corners]
    zs = [v.z for v in corners]
    return min(xs), max(xs), min(zs), max(zs)



def delete_object_by_name(obj_name):
    """
    Deletes an object from the scene and Blender data by its name.
    Returns True if deleted, False if not found.
    """

    obj = bpy.data.objects.get(obj_name)

    if not obj:
        print(f"Object '{obj_name}' not found")
        return False

    # Unlink from all collections
    for col in obj.users_collection:
        col.objects.unlink(obj)

    # Remove object data
    bpy.data.objects.remove(obj)

    return True


def insert_headboard(loc):
    blend_path, object_name = loc.split("::", 1)

    # Remove old one
    delete_object_by_name("headboard")

    with bpy.data.libraries.load(blend_path, link=False) as (data_from, data_to):
        data_to.objects = [object_name]

    obj = data_to.objects[0]
    bpy.context.collection.objects.link(obj)

    # Rename immediately
    obj.name = "headboard"

    # 🔧 NORMALIZE TRANSFORMS (CRITICAL)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    obj.select_set(False)

    # Reset transform cleanly
    obj.location = (0, 0, 0)
    obj.rotation_euler = (0, 0, 0)
    obj.scale = (1, 1, 1)

    # --- COMPUTE BOUNDS ---
    h_min_x, h_max_x, h_min_z, h_max_z = world_bounds(obj)
    h_half_x = (h_max_x - h_min_x) / 2
    h_half_z = (h_max_z - h_min_z) / 2

    frame = bpy.data.objects["Frame"]
    f_min_x, _, f_min_z, _ = world_bounds(frame)

    # 🔧 WORLD-SPACE MOVE (THIS IS THE KEY)
    obj.matrix_world.translation.x = f_min_x
    obj.matrix_world.translation.z = f_min_z

    return obj

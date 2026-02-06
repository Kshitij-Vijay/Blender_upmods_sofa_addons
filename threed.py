import bpy
import os
from .compass import *


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
    """
    Inserts an object from another .blend file into the current scene.

    loc format:
    C:\\path\\to\\file.blend::ObjectName
    """

    if "::" not in loc:
        raise ValueError("Invalid loc format. Expected 'path.blend::ObjectName'")

    # Split the location string
    blend_path, object_name = loc.split("::", 1)

    # Normalize Windows path
    blend_path = os.path.normpath(blend_path)

    delete_object_by_name("headboard")

    # Load (append) the object
    with bpy.data.libraries.load(blend_path, link=False) as (data_from, data_to):
        if object_name not in data_from.objects:
            raise ValueError(f"Object '{object_name}' not found in {blend_path}")
        data_to.objects = [object_name]

    # Link object to active collection
    from mathutils import Vector

    for obj in data_to.objects:
        if obj is not None:
            bpy.context.collection.objects.link(obj)

            # Rename
            obj.name = "headboard"

            # 🔧 Normalize transforms FIRST
            obj.rotation_euler = (0, 0, 0)
            obj.scale = (1, 1, 1)

            # --- compute bounds AFTER normalization ---
            u = max_x("headboard")
            d = min_x("headboard")
            c = (u - d) / 2

            a = (max_z("headboard") - min_z("headboard")) / 2

            # 🔧 WORLD-SPACE placement (IMPORTANT)
            mw = obj.matrix_world
            mw.translation.x = min_x("Frame") - c
            mw.translation.z = min_z("Frame") + a
            obj.matrix_world = mw

            return obj


    return None

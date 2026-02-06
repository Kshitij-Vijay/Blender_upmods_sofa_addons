import bpy
from mathutils import Vector

def min_x(obj_name):
    """
    Returns the most negative X (minimum X) world-space coordinate
    of the given object.
    """

    obj = bpy.data.objects.get(obj_name)
    if not obj:
        raise ValueError(f"Object '{obj_name}' not found")

    # Convert bounding box corners to world space
    world_corners = [
        obj.matrix_world @ Vector(corner)
        for corner in obj.bound_box
    ]

    # Get minimum X value
    min_x = min(v.x for v in world_corners)

    return min_x


def max_x(obj_name):
    """
    Returns the most pos X (minimum X) world-space coordinate
    of the given object.
    """

    obj = bpy.data.objects.get(obj_name)
    if not obj:
        raise ValueError(f"Object '{obj_name}' not found")

    # Convert bounding box corners to world space
    world_corners = [
        obj.matrix_world @ Vector(corner)
        for corner in obj.bound_box
    ]

    # Get minimum X value
    max_x = max(v.x for v in world_corners)

    return max_x



def max_y(obj_name):

    obj = bpy.data.objects.get(obj_name)
    if not obj:
        raise ValueError(f"Object '{obj_name}' not found")

    # Convert bounding box corners to world space
    world_corners = [
        obj.matrix_world @ Vector(corner)
        for corner in obj.bound_box
    ]

    # Get minimum X value
    max_y = max(v.y for v in world_corners)

    return max_y



def min_y(obj_name):

    obj = bpy.data.objects.get(obj_name)
    if not obj:
        raise ValueError(f"Object '{obj_name}' not found")

    # Convert bounding box corners to world space
    world_corners = [
        obj.matrix_world @ Vector(corner)
        for corner in obj.bound_box
    ]

    # Get minimum X value
    min_y = min(v.y for v in world_corners)

    return min_y


def max_z(obj_name):

    obj = bpy.data.objects.get(obj_name)
    if not obj:
        raise ValueError(f"Object '{obj_name}' not found")

    # Convert bounding box corners to world space
    world_corners = [
        obj.matrix_world @ Vector(corner)
        for corner in obj.bound_box
    ]

    # Get minimum X value
    max_z = max(v.z for v in world_corners)

    return max_z


def min_z(obj_name):

    obj = bpy.data.objects.get(obj_name)
    if not obj:
        raise ValueError(f"Object '{obj_name}' not found")

    # Convert bounding box corners to world space
    world_corners = [
        obj.matrix_world @ Vector(corner)
        for corner in obj.bound_box
    ]

    # Get minimum X value
    min_z = min(v.z for v in world_corners)

    return min_z

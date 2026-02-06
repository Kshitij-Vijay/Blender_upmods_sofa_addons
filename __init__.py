# __init__.py

bl_info = {
    "name": "Upmods Sofa",
    "author": "You",
    "version": (1, 0),
    "blender": (4, 5, 0),
    "location": "View3D > Sidebar > MySQL",
    "description": "MySQL Items Viewer",
    "category": "3D View"
}


import bpy
from .properties import BlenderItem
from .operators import MYSQL_OT_load_items
from .panel import MYSQL_PT_items_panel

classes = (
    BlenderItem,
    MYSQL_OT_load_items,
    MYSQL_PT_items_panel
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.mysql_items = bpy.props.CollectionProperty(type=BlenderItem)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.mysql_items

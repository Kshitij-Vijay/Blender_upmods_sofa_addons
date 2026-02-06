# properties.py

import bpy

class BlenderItem(bpy.types.PropertyGroup):
    id: bpy.props.IntProperty()
    name: bpy.props.StringProperty()
    type: bpy.props.StringProperty()
    price: bpy.props.FloatProperty()
    location: bpy.props.StringProperty()


def register_properties():
    bpy.types.Scene.mysql_items = bpy.props.CollectionProperty(type=BlenderItem)

    bpy.types.Scene.selected_headboard_id = bpy.props.IntProperty(default=-1)
    bpy.types.Scene.selected_cot_id = bpy.props.IntProperty(default=-1)


def unregister_properties():
    del bpy.types.Scene.mysql_items
    del bpy.types.Scene.selected_headboard_id
    del bpy.types.Scene.selected_cot_id

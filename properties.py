# properties.py

import bpy

class BlenderItem(bpy.types.PropertyGroup):
    id: bpy.props.IntProperty()
    name: bpy.props.StringProperty()
    type: bpy.props.StringProperty()
    price: bpy.props.FloatProperty()
    location: bpy.props.StringProperty()

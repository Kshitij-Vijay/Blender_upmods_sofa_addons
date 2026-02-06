# operators.py

import bpy
from .db import fetch_items

class MYSQL_OT_load_items(bpy.types.Operator):
    bl_idname = "mysql.load_items"
    bl_label = "Load Items from MySQL"

    def execute(self, context):
        scene = context.scene
        scene.mysql_items.clear()

        for item in fetch_items():
            new = scene.mysql_items.add()
            new.id = item.id
            new.name = item.name
            new.type = item.type
            new.price = item.price
            new.location = item.location

        self.report({'INFO'}, "Items loaded from MySQL")
        return {'FINISHED'}

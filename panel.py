# panel.py

import bpy

class MYSQL_PT_items_panel(bpy.types.Panel):
    bl_label = "Load Items from UPMODS"
    bl_idname = "MYSQL_PT_items_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "UPMODS"


    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.operator("mysql.load_items")

        for item in scene.mysql_items:
            box = layout.box()
            box.label(text=f"{item.name} ({item.type})")
            box.label(text=f"Price: {item.price}")
            box.label(text=f"Location: {item.location}")

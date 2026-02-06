# operators.py
import bpy
from .threed import insert_headboard


class UPMODS_OT_select_headboard(bpy.types.Operator):
    bl_idname = "upmods.select_headboard"
    bl_label = "Select Headboard"
    bl_options = {'REGISTER', 'UNDO'}

    item_id: bpy.props.IntProperty()
    headboard_path: bpy.props.StringProperty()

    def execute(self, context):
        # Store selection
        context.scene.selected_headboard_id = self.item_id

        # Call your function with the passed-in path
        insert_headboard(self.headboard_path)

        return {'FINISHED'}



class UPMODS_OT_select_cot(bpy.types.Operator):
    bl_idname = "upmods.select_cot"
    bl_label = "Select Cot"

    item_id: bpy.props.IntProperty()

    def execute(self, context):
        context.scene.selected_cot_id = self.item_id
        return {'FINISHED'}

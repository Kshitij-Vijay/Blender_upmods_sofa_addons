# operators.py
import bpy


class UPMODS_OT_select_headboard(bpy.types.Operator):
    bl_idname = "upmods.select_headboard"
    bl_label = "Select Headboard"

    item_id: bpy.props.IntProperty()

    def execute(self, context):
        context.scene.selected_headboard_id = self.item_id
        return {'FINISHED'}


class UPMODS_OT_select_cot(bpy.types.Operator):
    bl_idname = "upmods.select_cot"
    bl_label = "Select Cot"

    item_id: bpy.props.IntProperty()

    def execute(self, context):
        context.scene.selected_cot_id = self.item_id
        return {'FINISHED'}

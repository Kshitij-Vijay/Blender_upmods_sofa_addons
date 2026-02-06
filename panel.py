# panel.py
import bpy
from .db import fetch_items
from .threed import insert_headboard


def get_item_by_id(items, item_id):
    for item in items:
        if item.id == item_id:
            return item
    return None


# ---------------- HEADBOARDS ----------------
class UPMODS_PT_headboards(bpy.types.Panel):
    bl_label = "Headboards"
    bl_idname = "UPMODS_PT_headboards"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "UPMODS"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        items = fetch_items()
        headboards = [i for i in items if i.type.lower() == "headboard"]

        if not headboards:
            layout.label(text="No headboards available")
            return

        for item in headboards:
            box = layout.box()
            row = box.row()
            row.label(text=item.name)
            row.label(text=f"₹ {item.price}")

            op = box.operator(
                "upmods.select_headboard",
                text="Select"
            )
            op.item_id = item.id

            # ✅ PASS THE PATH HERE
            op.headboard_path = item.location



# ---------------- COTS ----------------
class UPMODS_PT_cots(bpy.types.Panel):
    bl_label = "Cots"
    bl_idname = "UPMODS_PT_cots"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "UPMODS"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        items = fetch_items()
        cots = [i for i in items if i.type.lower() == "cot"]

        if not cots:
            layout.label(text="No cots available")
            return

        for item in cots:
            box = layout.box()
            row = box.row()
            row.label(text=item.name)
            row.label(text=f"₹ {item.price}")

            op = box.operator("upmods.select_cot", text="Select")
            op.item_id = item.id


# ---------------- PRICE PANEL ----------------
class UPMODS_PT_price(bpy.types.Panel):
    bl_label = "Price"
    bl_idname = "UPMODS_PT_price"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "UPMODS"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        items = fetch_items()

        headboard = get_item_by_id(items, scene.selected_headboard_id)
        cot = get_item_by_id(items, scene.selected_cot_id)

        total = 0.0

        if headboard:
            layout.label(text=f"Headboard: {headboard.name}")
            layout.label(text=f"₹ {headboard.price}")
            total += headboard.price

        if cot:
            layout.separator()
            layout.label(text=f"Cot: {cot.name}")
            layout.label(text=f"₹ {cot.price}")            
            total += cot.price

        layout.separator()
        layout.label(text=f"Total: ₹ {total}")

# __init__.py
import bpy

from .panel import (
    UPMODS_PT_headboards,
    UPMODS_PT_cots,
    UPMODS_PT_price,
)
from .operators import (
    UPMODS_OT_select_headboard,
    UPMODS_OT_select_cot,
)

classes = (
    UPMODS_PT_headboards,
    UPMODS_PT_cots,
    UPMODS_PT_price,
    UPMODS_OT_select_headboard,
    UPMODS_OT_select_cot,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # ✅ Scene properties (PUT IT HERE)
    bpy.types.Scene.selected_headboard_id = bpy.props.IntProperty(
        name="Selected Headboard ID",
        default=-1
    )

    bpy.types.Scene.selected_cot_id = bpy.props.IntProperty(
        name="Selected Cot ID",
        default=-1
    )


def unregister():
    # ✅ Always clean up properties
    del bpy.types.Scene.selected_headboard_id
    del bpy.types.Scene.selected_cot_id

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

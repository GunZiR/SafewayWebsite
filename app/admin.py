from django.contrib import admin
# from mptt.admin import MPTTModelAdmin
from feincms.admin import tree_editor
from feincms.admin.item_editor import ItemEditor

from .models import (TailGateTailLift,
                     CoolingSystem,
                     LogisticProduct,
                     DumpHoist,
                     Accessory,
                     AccessoriesStatus)

class TreeAdmin(tree_editor.TreeEditor):
    pass


# Register your models here.
admin.site.register(TailGateTailLift, TreeAdmin)
admin.site.register(CoolingSystem, TreeAdmin)
admin.site.register(LogisticProduct, TreeAdmin)
admin.site.register(DumpHoist, TreeAdmin)
admin.site.register(Accessory)
admin.site.register(AccessoriesStatus)
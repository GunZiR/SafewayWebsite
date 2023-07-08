from django.contrib import admin
# from mptt.admin import MPTTModelAdmin
from feincms.admin import tree_editor

from .models import (TailGateTailLift,
                     CoolingSystem,
                     LogisticProduct,
                     DumpHoist)

class ModelAdmin(tree_editor.TreeEditor):
    pass

# Register your models here.
admin.site.register(TailGateTailLift, ModelAdmin)
admin.site.register(CoolingSystem, ModelAdmin)
admin.site.register(LogisticProduct, ModelAdmin)
admin.site.register(DumpHoist, ModelAdmin)
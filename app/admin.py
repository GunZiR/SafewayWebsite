from django.contrib import admin
from feincms.admin import tree_editor
from parler.admin import TranslatableAdmin, TranslatableModelForm
from mptt.forms import MPTTAdminForm

from .models import (TailGateTailLift,
                     CoolingSystem,
                     LogisticProduct,
                     DumpHoist,
                     Accessory,
                     AccessoriesStatus)

class CategoryAdminForm(MPTTAdminForm, TranslatableModelForm):
    pass


class TreeAdmin(tree_editor.TreeEditor, TranslatableAdmin):
    form = CategoryAdminForm
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('slug',)}  # needed for translated fields


# Register your models here.
admin.site.register(TailGateTailLift, TreeAdmin)
admin.site.register(CoolingSystem, TreeAdmin)
admin.site.register(LogisticProduct, TreeAdmin)
admin.site.register(DumpHoist, TreeAdmin)
admin.site.register(Accessory, TranslatableAdmin)
admin.site.register(AccessoriesStatus)
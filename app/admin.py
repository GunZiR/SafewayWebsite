from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (TailGateTailLift,
                     CoolingSystem,
                     LogisticProducts,
                     DumpHoist)


# Register your models here.
admin.site.register(TailGateTailLift, MPTTModelAdmin)
admin.site.register(CoolingSystem, MPTTModelAdmin)
admin.site.register(LogisticProducts, MPTTModelAdmin)
admin.site.register(DumpHoist, MPTTModelAdmin)
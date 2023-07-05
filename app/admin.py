from django.contrib import admin
from .models.tail_gate_tail_lift_model import TailGateTailLiftType, TailGateTailLiftSize, TailGateTailLiftBox, TailGateTailLiftProduct 

# Register your models here.
admin.site.register(TailGateTailLiftType)
admin.site.register(TailGateTailLiftSize)
admin.site.register(TailGateTailLiftBox)
admin.site.register(TailGateTailLiftProduct)
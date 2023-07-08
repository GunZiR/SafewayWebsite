from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# ===================================================: Tail Gate & Tail Lift :================================================
class TailGateTailLift(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField()
    image_src = models.ImageField(upload_to='images/', null=True, blank=True)
    
    class Meta:
        ordering = ['tree_id']

    def __str__(self):
        return self.name
    
    

# ======================================================: Cooling System :====================================================
class CoolingSystem(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField()
    image_src = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        ordering = ['tree_id']

    def __str__(self):
        return self.name
    

# ===================================================: Logistic Products :================================================
class LogisticProduct(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField()
    image_src = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        ordering = ['tree_id']

    def __str__(self):
        return self.name
    

# ===================================================: Dump Hoist :================================================
class DumpHoist(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField()
    image_src = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        ordering = ['tree_id']

    def __str__(self):
        return self.name
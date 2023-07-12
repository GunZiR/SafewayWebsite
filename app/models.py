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
    
    def get_last_child(self):
        children = self.get_children()
        if children.exists():
            last_child = children.last()
            return last_child
        return None
    

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
    

# ===================================================: Dump Hoist :==================================================
class DumpHoist(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField()
    image_src = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        ordering = ['tree_id']

    def __str__(self):
        return self.name


# =====================================================: Accessory :==================================================
class Accessory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_src = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name


class AccessoriesStatus(models.Model):
    name = models.ForeignKey(TailGateTailLift, on_delete=models.CASCADE)
    remote = models.BooleanField(verbose_name='Remote')
    aluminium_gate = models.BooleanField(verbose_name='Aluminium Gate')
    short_gate = models.BooleanField(verbose_name='Short Gate')
    long_gate = models.BooleanField(verbose_name='Long Gate')
    two_fold_gate = models.BooleanField(verbose_name='Two Fold Gate')
    three_fold_gate = models.BooleanField(verbose_name='Three Fold Gate')
    wheel_protector = models.BooleanField(verbose_name='Wheel Protector')
    metal_plate = models.BooleanField(verbose_name='Metal Plate')
    more_cylinder = models.BooleanField(verbose_name='More Cylinder')

    def __str__(self):
        return f'{self.name} status'
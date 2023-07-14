from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from parler.models import TranslatableModel, TranslatedFields

from .managers import CategoryManager

# ===================================================: Tail Gate & Tail Lift :================================================
class TailGateTailLift(MPTTModel, TranslatableModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    image_src = models.ImageField(upload_to='images/tailgatetaillift/', null=True, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    translations = TranslatedFields(
        description = models.TextField(),
    )
    
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
    
    objects = CategoryManager()

# ======================================================: Cooling System :====================================================
class CoolingSystem(MPTTModel, TranslatableModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    image_src = models.ImageField(upload_to='images/coolingsystem/', null=True, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    translations = TranslatedFields(
        description = models.TextField(),
    )
    
    class Meta:
        ordering = ['tree_id']

    def __str__(self):
        return self.name

    objects = CategoryManager()
    

# ===================================================: Logistic Products :================================================
class LogisticProduct(MPTTModel, TranslatableModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    image_src = models.ImageField(upload_to='images/logisticproduct/', null=True, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    translations = TranslatedFields(
        description = models.TextField(),
    )
    
    class Meta:
        ordering = ['tree_id']

    def __str__(self):
        return self.name

    objects = CategoryManager()
    

# ===================================================: Dump Hoist :==================================================
class DumpHoist(MPTTModel, TranslatableModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    image_src = models.ImageField(upload_to='images/dumphoist/', null=True, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    translations = TranslatedFields(
        description = models.TextField(),
    )

    class Meta:
        ordering = ['tree_id']

    def __str__(self):
        return self.name

    objects = CategoryManager()
    
# =====================================================: Accessory :==================================================
class Accessory(TranslatableModel):
    name = models.CharField(max_length=255)
    translations = TranslatedFields(
        description = models.TextField(),
    )
    slug = models.SlugField(null=True, blank=True)
    image_src = models.ImageField(upload_to='images/accessory', null=True, blank=True)

    def __str__(self):
        return self.name


class AccessoriesStatus(models.Model):
    name = models.ForeignKey(TailGateTailLift, on_delete=models.CASCADE)
    remote = models.BooleanField(verbose_name='Remote')
    aluminium_gate = models.BooleanField(verbose_name='Aluminium Gate')
    short_gate = models.BooleanField(verbose_name='Short Gate')
    long_gate = models.BooleanField(verbose_name='Long Gate')
    two_fold_gate = models.BooleanField(verbose_name='2 Fold Gate')
    three_fold_gate = models.BooleanField(verbose_name='3 Fold Gate')
    wheel_protector = models.BooleanField(verbose_name='Wheel Protector')
    metal_plate = models.BooleanField(verbose_name='Side Protection Bar')
    more_cylinder = models.BooleanField(verbose_name='Addition Cylinder')
    stainless_floor = models.BooleanField(verbose_name='Stainless Floor')
    stall = models.BooleanField(verbose_name='Stall')

    def __str__(self):
        return f'{self.name} status'
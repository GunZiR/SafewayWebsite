from django.db import models

# ===================================================: Tail Gate & Tail Lift type :================================================
class TailGateTailLiftType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_src = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

# ===================================================: Tail Gate & Tail Lift size :================================================
class TailGateTailLiftSize(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(TailGateTailLiftType, on_delete=models.CASCADE)
    description = models.TextField()
    image_src = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

# ===================================================: Tail Gate & Tail Lift box :================================================
class TailGateTailLiftBox(models.Model):
    name = models.CharField(max_length=100)
    size = models.ForeignKey(TailGateTailLiftSize, on_delete=models.CASCADE)
    description = models.TextField()
    image_src = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

# ===================================================: Tail Gate & Tail Lift product :================================================
class TailGateTailLiftProduct(models.Model):
    name = models.CharField(max_length=100)
    box = models.ForeignKey(TailGateTailLiftBox, on_delete=models.CASCADE)
    description = models.TextField()
    image_src = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
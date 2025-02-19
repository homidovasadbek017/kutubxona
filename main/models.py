from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Talaba(models.Model):
    name = models.CharField(max_length=255)
    guruh = models.CharField(max_length=100, blank=True, null=True)
    kurs = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    kitob_soni = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'


class Muallif(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    name = models.CharField(max_length=255)
    jinsi = models.CharField(max_length=10, choices=gender_choices)
    birth_date = models.DateField(blank=True, null=True)
    kitoblar_soni = models.PositiveSmallIntegerField(blank=True, null=True)
    tirik = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Muallif'
        verbose_name_plural = 'Mualliflar'


class Kitob(models.Model):
    name = models.CharField(max_length=255)
    janri = models.CharField(max_length=100, blank=True, null=True)
    sahifa = models.PositiveSmallIntegerField(blank=True, null=True)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kitob'
        verbose_name_plural = 'Kitoblar'


class Kutubxonachi(models.Model):
    name = models.CharField(max_length=255)
    ish_vaqti = models.DurationField(default=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kutubxonachi'
        verbose_name_plural = 'Kutubxonachilar'


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.SET_NULL, null=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.SET_NULL, null=True)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.SET_NULL, null=True)
    olingan_sana = models.DateTimeField(auto_now_add=True)
    qaytardi = models.BooleanField(default=False)
    qaytarish_sana = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.talaba.name} - {self.kitob.name}"

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Recordlar'

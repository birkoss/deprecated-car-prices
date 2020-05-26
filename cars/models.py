from django.db import models

from config.helpers import slugify_model


class PaymentTerm(models.Model):
    payment = models.ForeignKey(
        'Payment',
        on_delete=models.PROTECT,
        null=True
    )

    term = models.IntegerField()
    rate = models.FloatField()
    discount = models.FloatField()
    residual = models.FloatField()


class Payment(models.Model):
    payment_type = models.ForeignKey(
        'PaymentType',
        on_delete=models.PROTECT,
        null=True
    )

    trim = models.ForeignKey(
        'Trim',
        on_delete=models.PROTECT,
        null=True
    )

    msrp = models.FloatField()
    delivery = models.FloatField()
    taxes = models.FloatField()
    discount = models.FloatField()

    date_added = models.DateTimeField(auto_now=True)

    # Only ONE payment per PaymentType can be pending at anytime
    is_pending = models.BooleanField(default=True)

    is_valid = models.BooleanField(default=False)


class PaymentType(models.Model):
    name = models.CharField(max_length=255, default='')
    slug = models.SlugField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug.strip():
            self.slug = slugify_model(PaymentType, self.__str__())
        super(PaymentType, self).save()


class Trim(models.Model):
    model = models.ForeignKey(
        'Model',
        on_delete=models.PROTECT,
        null=True
    )

    name = models.CharField(max_length=255, default='')
    slug = models.SlugField(max_length=255, blank=True, default='')

    nice_name = models.CharField(max_length=255, default='')
    foreign_id = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        name = self.model.__str__() + " "
        if self.nice_name != "":
            name += self.nice_name
        else:
            name += self.name
        return name

    def save(self, *args, **kwargs):
        if not self.slug.strip():
            self.slug = slugify_model(Trim, self.__str__())
        super(Trim, self).save()


class Model(models.Model):
    make = models.ForeignKey(
        'Make',
        on_delete=models.PROTECT,
        null=True
    )

    name = models.CharField(max_length=255, default='')
    slug = models.SlugField(blank=True, default='')

    year = models.CharField(max_length=4, default='')

    def __str__(self):
        return self.make.name + " " + self.get_model_name()

    def save(self, *args, **kwargs):
        if not self.slug.strip():
            self.slug = slugify_model(Model, self.get_model_name())
        super(Model, self).save()

    def get_model_name(self):
        return self.name + " " + self.year


class Make(models.Model):
    name = models.CharField(max_length=255, default='')
    slug = models.SlugField(blank=True, default='')

    token = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug.strip():
            self.slug = slugify_model(Make, self.name)
        super(Make, self).save()

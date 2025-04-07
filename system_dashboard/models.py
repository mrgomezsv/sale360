from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import Decimal

class Partner(models.Model):
    name = models.CharField('Nombre', max_length=200)
    vat = models.CharField('NIT/RUC', max_length=20, blank=True)
    street = models.CharField('Dirección', max_length=200, blank=True)
    phone = models.CharField('Teléfono', max_length=20, blank=True)
    email = models.EmailField('Correo electrónico', blank=True)
    is_customer = models.BooleanField('Es cliente', default=True)
    is_vendor = models.BooleanField('Es proveedor', default=False)
    active = models.BooleanField('Activo', default=True)
    created_at = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de actualización', auto_now=True)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.name

class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('product', 'Almacenable'),
        ('service', 'Servicio'),
        ('consu', 'Consumible'),
    ]

    name = models.CharField('Nombre', max_length=200)
    code = models.CharField('Código', max_length=50, blank=True)
    type = models.CharField('Tipo', max_length=20, choices=PRODUCT_TYPE_CHOICES, default='product')
    list_price = models.DecimalField('Precio de venta', max_digits=10, decimal_places=2, default=0.0)
    standard_price = models.DecimalField('Costo', max_digits=10, decimal_places=2, default=0.0)
    description = models.TextField('Descripción', blank=True)
    active = models.BooleanField('Activo', default=True)
    created_at = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de actualización', auto_now=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f'[{self.code}] {self.name}' if self.code else self.name

class SaleOrder(models.Model):
    STATE_CHOICES = [
        ('draft', 'Borrador'),
        ('sent', 'Presupuesto enviado'),
        ('sale', 'Pedido de venta'),
        ('done', 'Bloqueado'),
        ('cancel', 'Cancelado'),
    ]

    name = models.CharField('Referencia', max_length=50, default='Nuevo')
    partner_id = models.ForeignKey(Partner, verbose_name='Cliente', on_delete=models.CASCADE)
    date_order = models.DateTimeField('Fecha del pedido', default=timezone.now)
    validity_date = models.DateField('Fecha de validez', null=True, blank=True)
    user_id = models.ForeignKey(User, verbose_name='Comercial', on_delete=models.CASCADE)
    state = models.CharField('Estado', max_length=20, choices=STATE_CHOICES, default='draft')
    note = models.TextField('Términos y condiciones', blank=True)
    amount_untaxed = models.DecimalField('Base imponible', max_digits=10, decimal_places=2, default=0.0)
    amount_tax = models.DecimalField('Impuestos', max_digits=10, decimal_places=2, default=0.0)
    amount_total = models.DecimalField('Total', max_digits=10, decimal_places=2, default=0.0)
    currency_id = models.CharField('Moneda', max_length=3, default='USD')
    created_at = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de actualización', auto_now=True)

    class Meta:
        verbose_name = 'Pedido de venta'
        verbose_name_plural = 'Pedidos de venta'

    def __str__(self):
        return self.name

    def calculate_amounts(self):
        lines = self.order_line.all()
        self.amount_untaxed = sum(line.price_subtotal for line in lines)
        self.amount_tax = sum(line.price_tax for line in lines)
        self.amount_total = self.amount_untaxed + self.amount_tax
        self.save()

class SaleOrderLine(models.Model):
    order_id = models.ForeignKey(SaleOrder, verbose_name='Pedido', related_name='order_line', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, verbose_name='Producto', on_delete=models.CASCADE)
    name = models.TextField('Descripción')
    product_uom_qty = models.DecimalField('Cantidad', max_digits=10, decimal_places=2, default=1.0)
    price_unit = models.DecimalField('Precio unitario', max_digits=10, decimal_places=2, default=0.0)
    discount = models.DecimalField('Descuento (%)', max_digits=5, decimal_places=2, default=0.0)
    tax_rate = models.DecimalField('Tasa de impuesto (%)', max_digits=5, decimal_places=2, default=13.0)
    price_subtotal = models.DecimalField('Subtotal', max_digits=10, decimal_places=2, default=0.0)
    price_tax = models.DecimalField('Impuesto', max_digits=10, decimal_places=2, default=0.0)
    price_total = models.DecimalField('Total', max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de actualización', auto_now=True)

    class Meta:
        verbose_name = 'Línea de pedido'
        verbose_name_plural = 'Líneas de pedido'

    def __str__(self):
        return f'{self.order_id.name} - {self.product_id.name}'

    def calculate_amounts(self):
        # Calcula el subtotal sin descuento
        subtotal_before_discount = self.product_uom_qty * self.price_unit
        
        # Aplica el descuento
        discount_amount = subtotal_before_discount * (self.discount / Decimal('100.0'))
        self.price_subtotal = subtotal_before_discount - discount_amount
        
        # Calcula el impuesto
        self.price_tax = self.price_subtotal * (self.tax_rate / Decimal('100.0'))
        
        # Calcula el total
        self.price_total = self.price_subtotal + self.price_tax
        self.save()

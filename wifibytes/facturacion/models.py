# encoding:utf-8

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from cliente.models import *
from catalogo.models import *
from omv.models import *
from tinymce.models import HTMLField
from datetime import datetime
from catalogo.models import Articulo
from django.db.models.signals import post_save
from django.dispatch import receiver


class Consumo(models.Model):
    codconsumo = models.IntegerField(
        primary_key=True, verbose_name=("Codigo Consumo"),
        null=False, editable=False)
    codcliente = models.ForeignKey(
        Cliente, verbose_name=("Codigo Cliente"),
        related_name='Consumo_Cliente',on_delete=models.PROTECT)
    fecha_mes = models.DateField(
        verbose_name=("Fecha"), null=True, blank=True)
    dia_inicio = models.DateField(
        verbose_name=("dia_inicio"), null=True, blank=True)
    dia_final = models.DateField(
        verbose_name=("dia_final"), null=True, blank=True)
    totaleuros = models.FloatField(
        verbose_name=("Total Euros"),  blank=True, default=0.0)

    def __str__(self):
        return str(self.codpago)

    def save(self, *args, **kwargs):

        if not self.codpago:
            no = Consumo.objects.count()
            if no == 0:
                self.codpago = 1
            else:
                self.codpago = self.__class__.objects.all().order_by(
                    "-codpago")[0].codpago + 1
        super(FormasPago, self).save(*args, **kwargs)


class FormasPago(models.Model):

    codpago = models.IntegerField(primary_key=True, editable=False)
    nombre = models.CharField(verbose_name="Nombre [ES]", max_length=250)
    nombre_va = models.CharField(verbose_name="Nombre [VA]", max_length=250, blank=True)
    descripcion = models.TextField(
        verbose_name="Descripción [ES]", null=True, blank=True)
    descripcion_va = models.TextField(
        verbose_name="Descripción [VA]", null=True, blank=True)
    cod_eneboo = models.CharField(
        verbose_name="Código Eneboo", null=True, blank=True, max_length=50
    )
    activa = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name = "Métodos de Pago"

    def save(self, *args, **kwargs):

        if not self.codpago:
            no = FormasPago.objects.count()
            if no == 0:
                self.codpago = 1
            else:
                self.codpago = self.__class__.objects.all().order_by(
                    "-codpago")[0].codpago + 1

        super(FormasPago, self).save(*args, **kwargs)


class FormasEnvio(models.Model):

    idEnvio = models.IntegerField(primary_key=True, editable=False)
    nombre = models.CharField(verbose_name="Nombre [ES]", max_length=250)
    nombre_va = models.CharField(verbose_name="Nombre [VA]", max_length=250, blank=True)
    descripcion = models.TextField(
        verbose_name="Descripción [ES]", null=True, blank=True)
    descripcion_va = models.TextField(
        verbose_name="Descripción [VA]", null=True, blank=True)
    precio = models.FloatField(verbose_name="Precio")

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name = "Métodos de envío"

    def save(self, *args, **kwargs):

        if not self.idEnvio:
            no = FormasEnvio.objects.count()
            if no == 0:
                self.idEnvio = 1
            else:
                self.idEnvio = self.__class__.objects.all().order_by(
                    "-idEnvio")[0].idEnvio + 1

        super(FormasEnvio, self).save(*args, **kwargs)


class PedidoCli(models.Model):

    estados = (
        (0, ('En proceso')),
        (1, ('Enviado')),
        (2, ('Entregado')),
        (3, ('Cancelado'))
    )
    idpedido = models.IntegerField(primary_key=True, editable=False)

    codcliente = models.ForeignKey(Cliente, verbose_name=("Codigo Cliente"),
                                   related_name='PedidoCli_Cliente',on_delete=models.PROTECT)

    cifnif = models.CharField(verbose_name=("CIFNIF"), max_length=20,
                              null=True, blank=True, editable=True)

    nombrecliente = models.CharField(verbose_name=("Nombre Cliente"),
                                     max_length=100, null=True, blank=True,
                                     editable=True)
    # apellidocliente = models.CharField(
    #    verbose_name=("Apellido Cliente"), max_length=100, null=True,
    #    blank=True, editable=True)

    coddir = models.ForeignKey(DirClientes, verbose_name=("Codigo Dirección"),
                               related_name='PedidoCli_DirClientes',on_delete=models.PROTECT)

    direccion = models.CharField(verbose_name=(
        "Dirección"), max_length=100,  null=True, blank=True, editable=True)

    provincia = models.CharField(verbose_name=("Provincia"), max_length=100,
                                 null=True, blank=True, editable=True)

    idprovincia = models.CharField(verbose_name=("Id Provincia"),
                                   max_length=100, null=True, editable=False)

    ciudad = models.CharField(verbose_name=("Ciudad"), max_length=100,
                              null=True, blank=True, editable=True)
    codpostal = models.CharField(verbose_name=(
        "Codigo Postal"), max_length=10, null=True, blank=True, editable=True)

    nombreclienteFacturacion = models.CharField(
        verbose_name=("Nombre Cliente Facturacion"),
        max_length=100, null=True, blank=True, editable=True
    )

    cifnifFacturacion = models.CharField(
        verbose_name=("CIFNIF Facturacion"), max_length=20,
        null=True, blank=True, editable=True
    )

    # apartado = models.CharField(verbose_name=("Apartado"), max_length=10,
    #                             null=True, blank=True, editable=True)
    codpais = models.CharField(verbose_name=("Codigo Pais"), max_length=20,
                               null=True, blank=True, editable=True)

    coddirEnvio = models.ForeignKey(DirClientes,
                                    verbose_name=("Codigo Dirección Envío"),
                                    related_name='PedidoCli_DirClientesEnvio',on_delete=models.PROTECT)

    direccionEnvio = models.CharField(verbose_name=("Dirección de Envío"),
                                      max_length=200,  null=True,
                                      blank=True, editable=True)

    provinciaEnvio = models.CharField(verbose_name=("Provincia de envío"),
                                      max_length=100, null=True, blank=True,
                                      editable=True)

    idprovinciaEnvio = models.CharField(
        verbose_name=("Id Provincia de Envío"), max_length=100, null=True,
        editable=False)

    ciudadEnvio = models.CharField(verbose_name=("Ciudad de Envío"),
                                   max_length=100, null=True, blank=True,
                                   editable=True)

    codpostalEnvio = models.CharField(verbose_name=("Codigo Postal de Envío"),
                                      max_length=10, null=True, blank=True,
                                      editable=True)

    codpago = models.ForeignKey(
        FormasPago, verbose_name=("Formas de Pago - TPV"),
        null=True, blank=True,on_delete=models.SET_NULL)

    codigo = models.CharField(
        verbose_name=("Codigo"), max_length=13, null=True, blank=True)
    # codserie = models.CharField(
    #     verbose_name=("Codigo Serie"), max_length=2, null=True, blank=True)
    # coddivisa = models.CharField(
    #     verbose_name=("Codigo divisa"), max_length=3, null=True, blank=True)
    tasaconv = models.FloatField(
        verbose_name=("Tasa conv"),
        validators=[MinValueValidator(0.5), MaxValueValidator(1000.5)],
        blank=True, default=0.5)

    codejercicio = models.CharField(verbose_name=("Codigo Ejercicio"),
                                    max_length=4, null=True, blank=True)

    irpf = models.FloatField(
        verbose_name=("IRPF"),
        validators=[MinValueValidator(0.5), MaxValueValidator(1000.5)],
        blank=True, default=0.5)
    totaleuros = models.FloatField(
        verbose_name=("Total Euros"),
        validators=[MinValueValidator(0.5), MaxValueValidator(1006.5)],
        blank=True, default=0.5)

    total = models.FloatField(
        verbose_name=("Total"),
        validators=[MinValueValidator(0.5), MaxValueValidator(1006.5)],
        blank=True, default=0.5)

    totaliva = models.FloatField(
        verbose_name=("Iva"),
        validators=[MinValueValidator(0.5), MaxValueValidator(1006.5)],
        blank=True, default=0.5)

    neto = models.FloatField(
        verbose_name=("Neto"),
        validators=[MinValueValidator(0.5), MaxValueValidator(1006.5)],
        blank=True, default=0.5)

    porcomision = models.FloatField(
        verbose_name=("Por comisión"),
        validators=[MinValueValidator(0.5), MaxValueValidator(1006.5)],
        blank=True, default=0.5)

    idpresupuesto = models.IntegerField(
        verbose_name=("Id presupuesto"), default=0, blank=True)

    observaciones = HTMLField(null=True, blank=True)

    servido = models.CharField(
        verbose_name=("Servido"), max_length=10, null=True, blank=True)

    editable = models.NullBooleanField(
        verbose_name=("Editable"), default=0, blank=True)

    codalmacen = models.CharField(
        verbose_name=("Codigo almacen"), max_length=4, null=True, blank=True)

    # totalrecargo = models.FloatField(
    #     validators=[MinValueValidator(0.5), MaxValueValidator(6.5)])
    # codagente = models.CharField(max_length = 10)
    # recfinanciero = models.FloatField(
    #     validators=[MinValueValidator(0.5), MaxValueValidator(6.5)],
    #     blank = False)
    # totalirpf = models.FloatField(
    #     validators=[MinValueValidator(0.5), MaxValueValidator(6.5)],
    #     blank = False)

    fechasalida = models.DateField(
        verbose_name=("Fecha Salida"), null=True,  blank=True)
    numero = models.CharField(
        verbose_name=("Numero"), max_length=12, null=True, blank=True)
    fecha = models.DateField(verbose_name=("Fecha"), null=True, blank=True)
    formaEnvio = models.ForeignKey(FormasEnvio,
                                   verbose_name=("Forma de envío"),
                                   related_name='PedidoCli_FormasEnvio',on_delete=models.PROTECT)

    formaPago = models.ForeignKey(FormasPago, verbose_name=("Forma de pago"),
                                  related_name='PedidoCli_FormasPago',on_delete=models.PROTECT)

    estado = models.IntegerField(verbose_name=("Estado del pedido"),
                                 choices=estados, null=False, blank=False,
                                 default=0)

    pagado = models.BooleanField(null=False, default=False, blank=False)

    created_at = models.IntegerField(default=0, editable=False)
    updated_at = models.IntegerField(default=0, editable=False)

    generar_factura = models.BooleanField(
        verbose_name=("Generar Factura"),
        null=False,
        default=False,
        blank=False
    )

    class Meta:
        verbose_name = "Pedido"

    def __str__(self):
        return str(self.idpedido)

    def save(self, *args, **kwargs):
        # print 'NUM PEDIDOS ', PedidoCli.objects.all().count()
        self.updated_at = int(format(datetime.now(), 'U'))

        try:  # Existe el objeto
            currentObject = PedidoCli.objects.get(
                idpedido=self.idpedido
            )
            print('EXISTE')
        except PedidoCli.DoesNotExist:
            print('NO EXISTE')
            if not self.idpedido:
                self.created_at = int(format(datetime.now(), 'U'))
                no = PedidoCli.objects.count()
                if no == 0:
                    self.idpedido = 900000
                else:
                    actual = self.__class__.objects.all().order_by(
                        "-idpedido")[0].idpedido
                    if actual < 900000:
                        nuevo = 900000
                    else:
                        nuevo = actual + 1
                    self.idpedido = nuevo

                no = PedidoCli.objects.filter(pk__gte=900000).count()
                self.numero = no + 1

                self.created_at = int(format(datetime.now(), 'U'))
                self.fecha = datetime.today()

                if self.codcliente:
                    self.cifnif = self.codcliente.cifnif
                    self.nombrecliente = self.codcliente.nombre
                    self.apellidocliente = self.codcliente.apellido

                    dircli = DirClientes.objects.get(pk=self.coddir.id)
                    self.direccion = dircli.direccion
                    self.codpais = dircli.codpais
                    self.ciudad = dircli.ciudad
                    self.provincia = dircli.provincia
                    self.apartado = dircli.apartado
                    self.codpostal = dircli.codpostal
                    self.nombreclienteFacturacion = dircli.nombre
                    self.cifnifFacturacion = dircli.cifnif

                    dircli = DirClientes.objects.get(pk=self.coddirEnvio.id)
                    self.direccionEnvio = dircli.direccion
                    self.ciudadEnvio = dircli.ciudad
                    self.provinciaEnvio = dircli.provincia
                    self.codpostalEnvio = dircli.codpostal

        neto = (self.total * 100) / 121
        totaliva = self.total - neto
        self.neto = round(neto, 2)
        self.totaliva = round(totaliva, 2)
        self.generar_factura = True

        super(PedidoCli, self).save(*args, **kwargs)


# Generar Factura al guardar pedido -- Campos desde Pedido o por defecto
@receiver(post_save, sender=PedidoCli, dispatch_uid="generar_factura")
def generar_factura(sender, instance, created, **kwargs):
    pedido = instance

    # Generar Factura solo desde API
    if not pedido.generar_factura:
        return

    try:
        factura = facturasCli.objects.get(idpedido=pedido)
    except facturasCli.DoesNotExist:
        factura = facturasCli()

    factura.idpedido = pedido
    factura.codigo = pedido.codigo
    factura.numero = pedido.numero
    factura.totaleuros = pedido.totaleuros
    factura.hora = datetime.now()
    factura.direccion = ""
    factura.codpago = FormasPago.objects.get(pk=1)  # Cambiar
    factura.codejercicio = ""
    factura.total = pedido.total
    factura.ciudad = pedido.ciudad
    factura.codpostal = pedido.codpostal
    factura.automatica = False
    factura.nombrecliente = pedido.nombrecliente
    factura.observaciones = pedido.observaciones
    factura.codcliente = pedido.codcliente
    factura.totaliva = pedido.totaliva
    factura.idprovincia = pedido.idprovinciaEnvio
    factura.fecha = datetime.now()
    factura.neto = pedido.neto
    factura.codpais = None
    factura.deabono = False
    factura.editable = False
    factura.codalmacen = None
    factura.coddir = pedido.coddirEnvio
    factura.cifnif = pedido.cifnif
    factura.nogenerarasiento = False
    factura.idfacturarect = None
    factura.provincia = pedido.provincia
    factura.codigorect = None
    factura.totalrecargo = None
    factura.codagente = None
    factura.recfinanciero = 0
    factura.idpagodevol = 0
    factura.totalirpf = 0
    factura.apartado = None
    factura.codserie = 0
    factura.porcomision = None
    factura.irpf = 0
    factura.idasiento = None
    factura.tpv = False
    factura.tasaconv = 0
    print('\n[GENERAR FACTURA]')
    print('------------------------------')
    print(factura)
    print('------------------------------')
    try:
        factura.save()
        print('[FACTURA GENERADA]  idpedido=> ', factura.idpedido)
    except Exception as error:
        print (error)
        print('[ERROR] => Generando Factura')


class Impuesto(models.Model):

    codimpuesto = models.CharField(primary_key=True, editable=True,
                                   max_length=10)
    recargo = models.FloatField(verbose_name="Recargo", blank=False)
    descripcion = models.CharField(
        verbose_name=("Descripción"), max_length=50)

    iva = models.FloatField(
        verbose_name=("IVA"),
        validators=[MinValueValidator(0.5), MaxValueValidator(1000.5)],
        blank=False)

    def __str__(self):
        return str(self.codimpuesto)

    def save(self, *args, **kwargs):

        if not self.codimpuesto:
            no = Impuesto.objects.count()
            if no == 0:
                self.codimpuesto = 1
            else:
                self.codimpuesto = self.__class__.objects.all().order_by(
                    "-codimpuesto")[0].codimpuesto + 1

        super(Impuesto, self).save(*args, **kwargs)


class LineaPedidoCli(models.Model):
    idlinea = models.IntegerField(primary_key=True, editable=False)

    pvpsindto = models.FloatField(
        verbose_name=("pvpsindto"),
        validators=[MinValueValidator(0.5), MaxValueValidator(1000.5)],
        null=True, blank=True, editable=True)

    pvpunitario = models.FloatField(
        verbose_name=("pvpunitario"),
        validators=[MinValueValidator(0.5), MaxValueValidator(1000.5)],
        null=True, blank=True, editable=True)

    referencia = models.ForeignKey(Articulo, verbose_name=("referencia"),
                                   related_name='LineaPedidoCli_Articulo',on_delete=models.PROTECT)

    cantidad = models.FloatField(
        verbose_name=("cantidad"),
        validators=[MinValueValidator(0.5), MaxValueValidator(1000.5)],
        null=True, blank=True)

    pvptotal = models.FloatField(
        verbose_name=("pvptotal"),
        validators=[MinValueValidator(0.5), MaxValueValidator(1000.5)],
        null=True, blank=True)

    descripcion = models.CharField(
        verbose_name=("descripcion"), max_length=100, null=True, blank=True)

    idpedido = models.ForeignKey(PedidoCli, verbose_name=("idpedido"),
                                 related_name='LineaPedidoCli_PedidoCli',on_delete=models.PROTECT)

    idlineapresupuesto = models.IntegerField(
        verbose_name=("idlineapresupuesto"), default=0, editable=False)

    codimpuesto = models.ForeignKey(Impuesto, verbose_name=("codimpuesto"),
                                    related_name='LineaPedidoCli_Impuesto',
                                    default='IVA18%',on_delete=models.PROTECT)

    cerrada = models.BooleanField(default=False, verbose_name=("cerrada"))

    porcomision = models.FloatField(verbose_name=("porcomision"), null=True,
                                    blank=True)

    iva = models.FloatField(
        verbose_name=("IVA"),
        validators=[MinValueValidator(0.5), MaxValueValidator(1000.5)],
        null=True, blank=True)

    totalenalbaran = models.FloatField(
        verbose_name=("totalenalbaran"),
        validators=[MinValueValidator(0.5), MaxValueValidator(1000.5)],
        null=True, blank=True)

    def __str__(self):
        return 'art: %s - > lin: %s ped: %s ' % (
            str(self.referencia), str(self.idlinea), str(self.idpedido))

    def save(self, *args, **kwargs):
        try:  # Existe el objeto
            currentObject = LineaPedidoCli.objects.get(
                idlinea=self.idlinea
            )
        except LineaPedidoCli.DoesNotExist:
            if not self.idlinea:
                self.created_at = int(format(datetime.now(), 'U'))
                no = LineaPedidoCli.objects.count()
                if no == 0:
                    self.idlinea = 900000
                else:
                    actual = self.__class__.objects.all().order_by(
                        "-idlinea")[0].idlinea
                    if actual < 900000:
                        nuevo = 900000
                    else:
                        nuevo = actual + 1
                    self.idlinea = nuevo

        super(LineaPedidoCli, self).save(*args, **kwargs)


class facturasCli(models.Model):
    idfactura = models.IntegerField(primary_key=True, null=False)
    idpedido = models.ForeignKey(PedidoCli, null=True, blank=False,on_delete=models.SET_NULL)
    codigo = models.CharField(max_length=12, null=False, blank=False)
    numero = models.CharField(max_length=12, null=False, blank=False)
    totaleuros = models.FloatField(null=False, blank=False)
    hora = models.TimeField(null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    codpago = models.ForeignKey(FormasPago, null=False, blank=False,on_delete=models.PROTECT)
    codejercicio = models.CharField(max_length=4, null=False, blank=False)
    total = models.FloatField(null=False, blank=False)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    codpostal = models.CharField(max_length=10, null=True, blank=True)
    automatica = models.BooleanField(default=True)
    nombrecliente = models.CharField(max_length=100, null=False, blank=False)
    observaciones = models.TextField(null=True, blank=True)
    codcliente = models.ForeignKey('cliente.Cliente', null=True, blank=True,on_delete=models.SET_NULL)
    totaliva = models.FloatField(null=False, blank=False)
    idprovincia = models.ForeignKey('geo.Provincia', null=True, blank=True,on_delete=models.SET_NULL)
    fecha = models.DateField(null=False, blank=False)
    neto = models.FloatField(null=False, blank=False)
    codpais = models.ForeignKey('geo.Pais', null=True, blank=True,on_delete=models.SET_NULL)
    deabono = models.BooleanField(default=False)
    editable = models.BooleanField(default=False)
    codalmacen = models.CharField(max_length=4, null=True, blank=True)
    coddir = models.ForeignKey(
        'cliente.DirClientes', related_name="factura_direccion", null=True,
        blank=True,on_delete=models.SET_NULL)
    cifnif = models.CharField(max_length=20, null=False, blank=False)
    nogenerarasiento = models.BooleanField(default=True)
    idfacturarect = models.IntegerField(null=True, blank=True)
    provincia = models.CharField(max_length=100, null=True, blank=True)
    codigorect = models.CharField(max_length=12, null=True, blank=True)
    totalrecargo = models.FloatField(null=True, blank=True)
    codagente = models.CharField(max_length=10, null=True, blank=True)
    recfinanciero = models.FloatField(null=False, blank=False)
    idpagodevol = models.IntegerField(null=True, blank=True)
    totalirpf = models.FloatField(null=False, blank=False)
    apartado = models.CharField(max_length=10, null=True, blank=True)
    codserie = models.CharField(max_length=2, null=False, blank=False)
    porcomision = models.FloatField(null=True, blank=True)
    irpf = models.FloatField(null=False)
    idasiento = models.IntegerField(null=True, blank=True)
    tpv = models.BooleanField(default=False)
    tasaconv = models.FloatField(null=False, blank=False)

    def __str__(self):
        return str(self.idfactura)

    def save(self, *args, **kwargs):
        try:  # Existe el objeto
            currentObject = facturasCli.objects.get(
                idfactura=self.idfactura
            )
        except facturasCli.DoesNotExist:
            if not self.idfactura:
                # self.created_at = int(format(datetime.now(), u'U'))
                print('GUARDAR FACTURA')
                self.idfactura = str(self.idpedido)

                if not self.codigo:
                    self.codigo = str(self.idpedido)
                '''
                no = facturasCli.objects.count()
                if no == 0:
                    self.idfactura = 900000
                else:
                    actual = self.__class__.objects.all().order_by(
                        "-idfactura")[0].idfactura
                    if actual < 900000:
                        nuevo = 900000
                    else:
                        nuevo = actual + 1
                    self.idfactura = nuevo
                '''

        lineasFactura = lineasfacturascli.objects.filter(idfactura=self)
        if lineasFactura.count() <= 0:
            if self.idpedido:
                lineasPedidos = LineaPedidoCli.objects.filter(idpedido_id=self.idpedido)
                for lineaPedido in lineasPedidos:
                    lineaFactura = lineasfacturascli.objects.create(
                        idfactura=self,
                        pvptotal=lineaPedido.pvptotal,
                        cantidad=lineaPedido.cantidad,
                        irpf=None,
                        recargo=None,
                        descripcion=lineaPedido.descripcion,
                        dtolineal=0,
                        idalbaran=None,
                        codimpuesto=None,
                        porcomision=lineaPedido.porcomision,
                        iva=lineaPedido.iva,
                        dtopor=0,
                        pvpsindto=0,
                        idliquidacio=None,
                        pvpunitario=lineaPedido.pvpunitario,
                        referencia=lineaPedido.referencia
                    )

            print('no hay lineas facturas')

        super(facturasCli, self).save(*args, **kwargs)


class lineasfacturascli(models.Model):
    idlinea = models.IntegerField(primary_key=True, null=False, editable=False)
    idfactura = models.ForeignKey(facturasCli, null=False, blank=False,on_delete=models.PROTECT)
    pvptotal = models.FloatField(null=False, blank=False, default=0)
    cantidad = models.FloatField(null=False, blank=False, default=0)
    irpf = models.FloatField(null=True, blank=True, default=0)
    recargo = models.FloatField(null=True, blank=True, default=0)
    dtolineal = models.FloatField(null=False, blank=False, default=0)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    idalbaran = models.IntegerField(null=True, blank=True)
    codimpuesto = models.CharField(max_length=10, null=True, blank=True)
    porcomision = models.FloatField(null=True, blank=True, default=0)
    iva = models.FloatField(null=True, blank=True)
    dtopor = models.FloatField(null=False, blank=False, default=0)
    pvpsindto = models.FloatField(null=False, blank=False, default=0)
    idliquidacio = models.IntegerField(null=True, blank=True)
    pvpunitario = models.FloatField(null=False, blank=False, default=0)
    referencia = models.ForeignKey('catalogo.Articulo',
                                   null=False, blank=False,on_delete=models.PROTECT)

    def __str__(self):
        return str(str(self.idlinea) + ' - ' + str(self.idfactura))

    def save(self, *args, **kwargs):
        try:  # Existe el objeto
            currentObject = lineasfacturascli.objects.get(
                idlinea=self.idlinea
            )
        except lineasfacturascli.DoesNotExist:
            if not self.idlinea:
                self.created_at = int(format(datetime.now(), 'U'))
                no = lineasfacturascli.objects.count()
                if no == 0:
                    self.idlinea = 900000
                else:
                    actual = self.__class__.objects.all().order_by(
                        "-idlinea")[0].idlinea
                    if actual < 900000:
                        nuevo = 900000
                    else:
                        nuevo = actual + 1
                    self.idlinea = nuevo

        if not self.descripcion and self.referencia:
            self.descripcion = self.referencia.descripcion

        super(lineasfacturascli, self).save(*args, **kwargs)


@receiver(post_save, sender=facturasCli, dispatch_uid="generar_linea_factura")
def generar_linea_factura(sender, instance, created, **kwargs):

    factura = instance
    lineasPedido = LineaPedidoCli.objects.filter(idpedido_id=factura.idpedido)

    # Borrar lineas existentes en factura
    lineasFactura = lineasfacturascli.objects.filter(idfactura=factura)
    lineasFactura.delete()

    for lineaPedido in lineasPedido:
        # Crear linea Factura
        if lineaPedido.pvptotal is None:  # En pedido puede ser null...
            lineaPedido.pvptotal = 0

        lineaFactura = lineasfacturascli.objects.create(
            idfactura=factura,
            pvptotal=lineaPedido.pvptotal,
            cantidad=lineaPedido.cantidad,
            irpf=None,
            recargo=None,
            descripcion=lineaPedido.descripcion,
            dtolineal=0,
            idalbaran=None,
            codimpuesto=None,
            porcomision=lineaPedido.porcomision,
            iva=lineaPedido.iva,
            dtopor=0,
            pvpsindto=0,
            idliquidacio=None,
            pvpunitario=lineaPedido.pvpunitario,
            referencia=lineaPedido.referencia
        )
        # codimpuesto y pvpsindto diferente tipo de datos

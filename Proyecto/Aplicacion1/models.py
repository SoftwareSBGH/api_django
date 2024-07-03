# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Auditoria(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.
    modulo = models.CharField(db_column='MODULO', max_length=100)  # Field name made lowercase.
    accion = models.CharField(db_column='ACCION', max_length=50)  # Field name made lowercase.
    cvebod = models.IntegerField(db_column='CVEBOD')  # Field name made lowercase.
    cvemov = models.IntegerField(db_column='CVEMOV')  # Field name made lowercase.
    sermov = models.CharField(db_column='SERMOV', max_length=2)  # Field name made lowercase.
    folmov = models.IntegerField(db_column='FOLMOV')  # Field name made lowercase.
    maquina = models.CharField(db_column='MAQUINA', max_length=100)  # Field name made lowercase.
    maquinaip = models.CharField(db_column='MAQUINAIP', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Auditoria'


class Bitacoracosto(models.Model):
    cveprod = models.CharField(max_length=50)
    numref = models.CharField(max_length=20)
    costoact = models.DecimalField(max_digits=19, decimal_places=4)
    nvocosto = models.DecimalField(max_digits=19, decimal_places=4)
    cospro = models.DecimalField(max_digits=19, decimal_places=4)
    fechaact = models.DateTimeField()
    login = models.CharField(max_length=20)
    equipo = models.CharField(max_length=50)
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'BitacoraCosto'


class Bitacoraprevta(models.Model):
    cveprod = models.CharField(max_length=50)
    numref = models.CharField(max_length=20)
    ultcosto = models.DecimalField(max_digits=19, decimal_places=4)
    cospro = models.DecimalField(max_digits=19, decimal_places=4)
    porcact1 = models.DecimalField(max_digits=19, decimal_places=4)
    porcact2 = models.DecimalField(max_digits=19, decimal_places=4)
    porcact3 = models.DecimalField(max_digits=19, decimal_places=4)
    porcact4 = models.DecimalField(max_digits=19, decimal_places=4)
    porcact5 = models.DecimalField(max_digits=19, decimal_places=4)
    porcact6 = models.DecimalField(max_digits=19, decimal_places=4)
    subpreciovta = models.DecimalField(max_digits=19, decimal_places=4)
    subpreciovta2 = models.DecimalField(max_digits=19, decimal_places=4)
    subpreciovta3 = models.DecimalField(max_digits=19, decimal_places=4)
    subpreciovta4 = models.DecimalField(max_digits=19, decimal_places=4)
    subpreciovta5 = models.DecimalField(max_digits=19, decimal_places=4)
    subpreciovta6 = models.DecimalField(max_digits=19, decimal_places=4)
    porciva = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps1 = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps2 = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps3 = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps4 = models.DecimalField(max_digits=19, decimal_places=4)
    subpreciovta1nvo = models.DecimalField(max_digits=19, decimal_places=4)
    subpreciovta2nvo = models.DecimalField(max_digits=19, decimal_places=4)
    subpreciovta3nvo = models.DecimalField(max_digits=19, decimal_places=4)
    subpreciovta4nvo = models.DecimalField(max_digits=19, decimal_places=4)
    subpreciovta5nvo = models.DecimalField(max_digits=19, decimal_places=4)
    subpreciovta6nvo = models.DecimalField(max_digits=19, decimal_places=4)
    porcact1nvo = models.DecimalField(max_digits=19, decimal_places=4)
    porcact2nvo = models.DecimalField(max_digits=19, decimal_places=4)
    porcact3nvo = models.DecimalField(max_digits=19, decimal_places=4)
    porcact4nvo = models.DecimalField(max_digits=19, decimal_places=4)
    porcact5nvo = models.DecimalField(max_digits=19, decimal_places=4)
    porcact6nvo = models.DecimalField(max_digits=19, decimal_places=4)
    fechaact = models.DateTimeField()
    login = models.CharField(max_length=20)
    equipo = models.CharField(max_length=50)
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'BitacoraPreVta'


class Bitacorapromos(models.Model):
    cveprod = models.CharField(max_length=80)
    numref = models.CharField(max_length=50)
    desprod = models.CharField(max_length=800)
    fechainipromo = models.DateTimeField()
    fechafinpromo = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'BitacoraPromos'


class Bitacoravalvtas(models.Model):
    cveprod = models.CharField(max_length=80)
    numref = models.CharField(max_length=80)
    desprod = models.CharField(max_length=800)
    fechainival = models.DateTimeField()
    cantidad = models.IntegerField()
    fechafinval = models.DateTimeField(db_column='Fechafinval')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BitacoravalVtas'


class Canales(models.Model):
    cve_canal = models.IntegerField(db_column='Cve_Canal')  # Field name made lowercase.
    des_canal = models.CharField(db_column='Des_Canal', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descorta_canal = models.CharField(db_column='DesCorta_Canal', max_length=10, blank=True, null=True)  # Field name made lowercase.
    baja = models.BooleanField(db_column='Baja')  # Field name made lowercase.
    fecha_alta = models.DateTimeField(db_column='Fecha_Alta', blank=True, null=True)  # Field name made lowercase.
    id_canal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CANALES'


class Catbod(models.Model):
    cvebod = models.IntegerField(db_column='CVEBOD')  # Field name made lowercase.
    desbod = models.CharField(db_column='DESBOD', max_length=80)  # Field name made lowercase.
    dirbod = models.CharField(db_column='DIRBOD', max_length=80)  # Field name made lowercase.
    colbod = models.CharField(db_column='COLBOD', max_length=80)  # Field name made lowercase.
    cveciu = models.IntegerField(db_column='CVECIU')  # Field name made lowercase.
    telbod = models.CharField(db_column='TELBOD', max_length=25)  # Field name made lowercase.
    faxbod = models.CharField(db_column='FAXBOD', max_length=25)  # Field name made lowercase.
    resbod = models.CharField(db_column='RESBOD', max_length=80)  # Field name made lowercase.
    clabod = models.SmallIntegerField(db_column='CLABOD')  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.
    exisneg = models.BooleanField(db_column='EXISNEG')  # Field name made lowercase.
    lispre = models.SmallIntegerField(db_column='LISPRE')  # Field name made lowercase.
    exismov = models.BooleanField(db_column='EXISMOV')  # Field name made lowercase.
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CATBOD'


class Catche(models.Model):
    cveche = models.IntegerField(db_column='CVECHE')  # Field name made lowercase.
    desche = models.CharField(db_column='DESCHE', max_length=50)  # Field name made lowercase.
    cveban = models.IntegerField(db_column='CVEBAN')  # Field name made lowercase.
    numcta = models.CharField(db_column='NUMCTA', max_length=30)  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATCHE'


class Catcia(models.Model):
    cvecia = models.IntegerField(db_column='CVECIA')  # Field name made lowercase.
    nomcia = models.CharField(db_column='NOMCIA', max_length=80)  # Field name made lowercase.
    ciucia = models.CharField(db_column='CIUCIA', max_length=80)  # Field name made lowercase.
    dircia = models.CharField(db_column='DIRCIA', max_length=80)  # Field name made lowercase.
    estcia = models.CharField(db_column='ESTCIA', max_length=80)  # Field name made lowercase.
    telcia = models.CharField(db_column='TELCIA', max_length=25)  # Field name made lowercase.
    rfccia = models.CharField(db_column='RFCCIA', max_length=15)  # Field name made lowercase.
    razcia = models.CharField(db_column='RAZCIA', max_length=80)  # Field name made lowercase.
    cveciu = models.IntegerField(db_column='CVECIU')  # Field name made lowercase.
    faxcia = models.CharField(db_column='FAXCIA', max_length=25)  # Field name made lowercase.
    cvebod = models.IntegerField(db_column='CVEBOD')  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.
    textocia = models.SmallIntegerField(db_column='TEXTOCIA')  # Field name made lowercase.
    modprecio1 = models.BooleanField(db_column='MODPRECIO1')  # Field name made lowercase.
    lineasfact = models.SmallIntegerField(db_column='LINEASFACT')  # Field name made lowercase.
    vtaafectainv = models.BooleanField(db_column='VTAAFECTAINV')  # Field name made lowercase.
    factconsec = models.BooleanField(db_column='FACTCONSEC')  # Field name made lowercase.
    factfolioseriebod = models.BooleanField(db_column='FACTFOLIOSERIEBOD')  # Field name made lowercase.
    credito = models.BooleanField(db_column='CREDITO')  # Field name made lowercase.
    desctodetcli = models.BooleanField(db_column='DESCTODETCLI')  # Field name made lowercase.
    comdetven = models.BooleanField(db_column='COMDETVEN')  # Field name made lowercase.
    bloqueamovtos = models.BooleanField(db_column='BLOQUEAMOVTOS')  # Field name made lowercase.
    actprecio = models.SmallIntegerField(db_column='ACTPRECIO')  # Field name made lowercase.
    formatonota = models.SmallIntegerField(db_column='FORMATONOTA')  # Field name made lowercase.
    restringelogin = models.BooleanField(db_column='RESTRINGELOGIN')  # Field name made lowercase.
    redondeaimportes = models.BooleanField(db_column='REDONDEAIMPORTES')  # Field name made lowercase.
    decimales = models.SmallIntegerField(db_column='DECIMALES')  # Field name made lowercase.
    descomponerpaquetes = models.BooleanField(db_column='DESCOMPONERPAQUETES')  # Field name made lowercase.
    reparatecnico = models.BooleanField(db_column='REPARATECNICO')  # Field name made lowercase.
    cxcnotas = models.BooleanField(db_column='CXCNOTAS')  # Field name made lowercase.
    diasrenta = models.IntegerField(db_column='DIASRENTA')  # Field name made lowercase.
    numfactvencrentas = models.IntegerField(db_column='NUMFACTVENCRENTAS')  # Field name made lowercase.
    limitecredito = models.DecimalField(db_column='LIMITECREDITO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    numfactvencventas = models.IntegerField(db_column='NUMFACTVENCVENTAS')  # Field name made lowercase.
    numfactvencrepara = models.IntegerField(db_column='NUMFACTVENCREPARA')  # Field name made lowercase.
    numfactvencrenova = models.IntegerField(db_column='NUMFACTVENCRENOVA')  # Field name made lowercase.
    numvtascambiomovto = models.IntegerField(db_column='NUMVTASCAMBIOMOVTO')  # Field name made lowercase.
    ventaa = models.IntegerField(db_column='VENTAA')  # Field name made lowercase.
    ventab = models.IntegerField(db_column='VENTAB')  # Field name made lowercase.
    regimen = models.IntegerField(db_column='REGIMEN')  # Field name made lowercase.
    codigop = models.CharField(db_column='CODIGOP', max_length=5)  # Field name made lowercase.
    numint = models.CharField(db_column='NUMINT', max_length=10)  # Field name made lowercase.
    numext = models.CharField(db_column='NUMEXT', max_length=10)  # Field name made lowercase.
    colonia = models.CharField(db_column='COLONIA', max_length=50)  # Field name made lowercase.
    pwscer = models.CharField(db_column='PWSCER', max_length=15)  # Field name made lowercase.
    paiscia = models.CharField(db_column='PAISCIA', max_length=20)  # Field name made lowercase.
    seriefac = models.CharField(db_column='SERIEFAC', max_length=3)  # Field name made lowercase.
    certificado = models.CharField(db_column='CERTIFICADO', max_length=100)  # Field name made lowercase.
    llave = models.CharField(db_column='LLAVE', max_length=100)  # Field name made lowercase.
    rutafac = models.CharField(db_column='RUTAFAC', max_length=200)  # Field name made lowercase.
    rutalogo = models.CharField(db_column='RUTALOGO', max_length=200)  # Field name made lowercase.
    serieimporte = models.CharField(db_column='SERIEIMPORTE', max_length=2)  # Field name made lowercase.
    correofac = models.CharField(max_length=50)
    pwsmail = models.CharField(max_length=15)
    smtp = models.CharField(max_length=20)
    puertomail = models.IntegerField()
    asuntomail = models.CharField(max_length=50)
    textomail = models.CharField(max_length=100)
    movfaccli = models.IntegerField()
    movfaccie = models.IntegerField()
    usertimbrado = models.CharField(max_length=50)
    pwstimbrado = models.CharField(max_length=50)
    genfaccierret = models.BooleanField()
    oficina = models.IntegerField()
    validaimpptovta = models.BooleanField()
    cantimpdoc = models.IntegerField()
    validaimpcortes = models.BooleanField()
    cantimpcortes = models.IntegerField()
    validaimpdoc = models.BooleanField()
    cantdocimp = models.IntegerField()
    userme = models.CharField(max_length=50)
    passme = models.CharField(max_length=50)
    userax = models.CharField(max_length=50)
    passax = models.CharField(max_length=50)
    idaxios = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'CATCIA'


class Catciu(models.Model):
    cveciu = models.IntegerField(db_column='CVECIU', primary_key=True)  # Field name made lowercase.
    nomciu = models.CharField(db_column='NOMCIU', max_length=80)  # Field name made lowercase.
    cveedo = models.IntegerField(db_column='CVEEDO')  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATCIU'


class Catcli(models.Model):
    cvecli = models.IntegerField(db_column='CVECLI')  # Field name made lowercase.
    nomcli = models.CharField(db_column='NOMCLI', max_length=80)  # Field name made lowercase.
    nomcli2 = models.CharField(db_column='NOMCLI2', max_length=80)  # Field name made lowercase.
    dircli = models.CharField(db_column='DIRCLI', max_length=80)  # Field name made lowercase.
    colcli = models.CharField(db_column='COLCLI', max_length=80)  # Field name made lowercase.
    cveciu = models.IntegerField(db_column='CVECIU')  # Field name made lowercase.
    cvegrucli = models.IntegerField(db_column='CVEGRUCLI')  # Field name made lowercase.
    limcred = models.DecimalField(db_column='LIMCRED', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tiprfc = models.SmallIntegerField(db_column='TIPRFC')  # Field name made lowercase.
    rfc1 = models.CharField(db_column='RFC1', max_length=4)  # Field name made lowercase.
    rfc2 = models.CharField(db_column='RFC2', max_length=6)  # Field name made lowercase.
    rfc3 = models.CharField(db_column='RFC3', max_length=3)  # Field name made lowercase.
    fecalt = models.DateTimeField(db_column='FECALT')  # Field name made lowercase.
    curpcli = models.CharField(db_column='CURPCLI', max_length=18)  # Field name made lowercase.
    emailcli = models.CharField(db_column='EMAILCLI', max_length=50)  # Field name made lowercase.
    tel1cli = models.CharField(db_column='TEL1CLI', max_length=25)  # Field name made lowercase.
    tel2cli = models.CharField(db_column='TEL2CLI', max_length=25)  # Field name made lowercase.
    faxcli = models.CharField(db_column='FAXCLI', max_length=25)  # Field name made lowercase.
    contac = models.CharField(db_column='CONTAC', max_length=80)  # Field name made lowercase.
    dircontac = models.CharField(db_column='DIRCONTAC', max_length=80)  # Field name made lowercase.
    telcontac = models.CharField(db_column='TELCONTAC', max_length=25)  # Field name made lowercase.
    emailcontac = models.CharField(db_column='EMAILCONTAC', max_length=50)  # Field name made lowercase.
    observa = models.TextField(db_column='OBSERVA')  # Field name made lowercase. This field type is a guess.
    cpcli = models.CharField(db_column='CPCLI', max_length=6)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.
    diascred = models.IntegerField(db_column='DIASCRED')  # Field name made lowercase.
    ctaconcli = models.CharField(db_column='CTACONCLI', max_length=50)  # Field name made lowercase.
    dircli2 = models.CharField(db_column='DIRCLI2', max_length=160)  # Field name made lowercase.
    porcdesc = models.DecimalField(db_column='PORCDESC', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cvegrucli2 = models.IntegerField(db_column='CVEGRUCLI2')  # Field name made lowercase.
    cvegrucli3 = models.IntegerField(db_column='CVEGRUCLI3')  # Field name made lowercase.
    cvegrucli4 = models.IntegerField(db_column='CVEGRUCLI4')  # Field name made lowercase.
    cvegrucli5 = models.IntegerField(db_column='CVEGRUCLI5')  # Field name made lowercase.
    cvegrucli6 = models.IntegerField(db_column='CVEGRUCLI6')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATCLI'


class Catedo(models.Model):
    cveedo = models.IntegerField(db_column='CVEEDO', primary_key=True)  # Field name made lowercase.
    nomedo = models.CharField(db_column='NOMEDO', max_length=80)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATEDO'


class Catfam(models.Model):
    cvedepto = models.IntegerField()
    cveseccion = models.IntegerField()
    cvefam = models.IntegerField(db_column='CVEFAM')  # Field name made lowercase.
    desfam = models.CharField(db_column='DESFAM', max_length=80)  # Field name made lowercase.
    ivafam = models.DecimalField(db_column='IVAFAM', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.
    numdias = models.SmallIntegerField(db_column='NUMDIAS')  # Field name made lowercase.
    campo1 = models.SmallIntegerField(db_column='CAMPO1')  # Field name made lowercase.
    tipocampo1 = models.BooleanField(db_column='TIPOCAMPO1')  # Field name made lowercase.
    campo2 = models.SmallIntegerField(db_column='CAMPO2')  # Field name made lowercase.
    tipocampo2 = models.BooleanField(db_column='TIPOCAMPO2')  # Field name made lowercase.
    campo3 = models.SmallIntegerField(db_column='CAMPO3')  # Field name made lowercase.
    tipocampo3 = models.BooleanField(db_column='TIPOCAMPO3')  # Field name made lowercase.
    campo4 = models.SmallIntegerField(db_column='CAMPO4')  # Field name made lowercase.
    tipocampo4 = models.BooleanField(db_column='TIPOCAMPO4')  # Field name made lowercase.
    comision = models.FloatField(db_column='COMISION')  # Field name made lowercase.
    desfam2 = models.CharField(db_column='DESFAM2', max_length=80)  # Field name made lowercase.
    ieps = models.DecimalField(db_column='IEPS', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ivafamret = models.DecimalField(db_column='IVAFAMRET', max_digits=19, decimal_places=4)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='EMPRESA')  # Field name made lowercase.
    cobraiva = models.BooleanField()
    cobraieps = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CATFAM'


class Catgastosop(models.Model):
    cve_concepto = models.IntegerField()
    descrip_concepto = models.CharField(max_length=150)
    tipogasto = models.IntegerField()
    ctagasto = models.CharField(max_length=15)
    provgasto = models.IntegerField()
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CATGASTOSOP'


class Catgrucli(models.Model):
    cvegrucli = models.IntegerField(db_column='CVEGRUCLI')  # Field name made lowercase.
    desgrucli = models.CharField(db_column='DESGRUCLI', max_length=80)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATGRUCLI'


class Catgrup(models.Model):
    cvegrup = models.CharField(db_column='CVEGRUP', max_length=15)  # Field name made lowercase.
    nomgrup = models.CharField(db_column='NOMGRUP', max_length=80)  # Field name made lowercase.
    pervis = models.BooleanField(db_column='PERVIS')  # Field name made lowercase.
    catemp = models.BooleanField(db_column='CATEMP')  # Field name made lowercase.
    impemp = models.BooleanField(db_column='IMPEMP')  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.
    autpedcom = models.BooleanField(db_column='AUTPEDCOM')  # Field name made lowercase.
    diascred = models.BooleanField(db_column='DIASCRED')  # Field name made lowercase.
    fechadocto = models.BooleanField(db_column='FECHADOCTO')  # Field name made lowercase.
    modifpreciovta = models.BooleanField(db_column='MODIFPRECIOVTA')  # Field name made lowercase.
    graficas = models.BooleanField(db_column='GRAFICAS')  # Field name made lowercase.
    limitecred = models.BooleanField(db_column='LIMITECRED')  # Field name made lowercase.
    porcdesccte = models.BooleanField(db_column='PORCDESCCTE')  # Field name made lowercase.
    cvegruclino = models.IntegerField(db_column='CveGruCliNo')  # Field name made lowercase.
    modifvtaspagos = models.BooleanField(db_column='MODIFVTASPAGOS')  # Field name made lowercase.
    saldopantent = models.BooleanField(db_column='SALDOPANTENT')  # Field name made lowercase.
    produccpreprod = models.BooleanField(db_column='PRODUCCPREPROD')  # Field name made lowercase.
    produccautprod = models.BooleanField(db_column='PRODUCCAUTPROD')  # Field name made lowercase.
    produccprod = models.BooleanField(db_column='PRODUCCPROD')  # Field name made lowercase.
    produccstaprod = models.BooleanField(db_column='PRODUCCSTAPROD')  # Field name made lowercase.
    produccstagral = models.BooleanField(db_column='PRODUCCSTAGRAL')  # Field name made lowercase.
    impcortesant = models.BooleanField(db_column='IMPCORTESANT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATGRUP'


class Catgruprov(models.Model):
    cvegruprov = models.IntegerField(db_column='CVEGRUPROV')  # Field name made lowercase.
    desgruprov = models.CharField(db_column='DESGRUPROV', max_length=80)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATGRUPROV'


class Catmar(models.Model):
    cvemar = models.IntegerField(db_column='CVEMAR')  # Field name made lowercase.
    desmar = models.CharField(db_column='DESMAR', max_length=80)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CATMAR'


class Catmon(models.Model):
    cvemon = models.IntegerField(db_column='CVEMON')  # Field name made lowercase.
    desmon = models.CharField(db_column='DESMON', max_length=80)  # Field name made lowercase.
    simmon = models.CharField(db_column='SIMMON', max_length=3)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATMON'


class Catmov(models.Model):
    cvemov = models.IntegerField(db_column='CVEMOV')  # Field name made lowercase.
    desmov = models.CharField(db_column='DESMOV', max_length=80)  # Field name made lowercase.
    tipmov = models.SmallIntegerField(db_column='TIPMOV')  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATMOV'


class Catprod(models.Model):
    cveprod = models.CharField(db_column='CVEPROD', max_length=20)  # Field name made lowercase.
    desprod = models.CharField(db_column='DESPROD', max_length=800)  # Field name made lowercase.
    fecalta = models.DateTimeField(db_column='FECALTA')  # Field name made lowercase.
    cveuni = models.CharField(db_column='CVEUNI', max_length=4)  # Field name made lowercase.
    cvefam = models.IntegerField(db_column='CVEFAM')  # Field name made lowercase.
    cvemar = models.IntegerField(db_column='CVEMAR')  # Field name made lowercase.
    desmod = models.CharField(db_column='DESMOD', max_length=80)  # Field name made lowercase.
    desubi = models.CharField(db_column='DESUBI', max_length=80)  # Field name made lowercase.
    tipprod = models.BooleanField(db_column='TIPPROD')  # Field name made lowercase.
    edoprod = models.BooleanField(db_column='EDOPROD')  # Field name made lowercase.
    paqprod = models.BooleanField(db_column='PAQPROD')  # Field name made lowercase.
    codbar = models.CharField(db_column='CODBAR', max_length=20)  # Field name made lowercase.
    numobj = models.IntegerField(db_column='NUMOBJ')  # Field name made lowercase.
    observa = models.TextField(db_column='OBSERVA')  # Field name made lowercase. This field type is a guess.
    foto = models.BinaryField(db_column='FOTO')  # Field name made lowercase.
    fecmodprec = models.DateTimeField(db_column='FECMODPREC')  # Field name made lowercase.
    lispre1 = models.DecimalField(db_column='LISPRE1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre2 = models.DecimalField(db_column='LISPRE2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre3 = models.DecimalField(db_column='LISPRE3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre4 = models.DecimalField(db_column='LISPRE4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre5 = models.DecimalField(db_column='LISPRE5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre6 = models.DecimalField(db_column='LISPRE6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    minprod = models.DecimalField(db_column='MINPROD', max_digits=19, decimal_places=4)  # Field name made lowercase.
    maxprod = models.DecimalField(db_column='MAXPROD', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cveprodprov = models.CharField(db_column='CVEPRODPROV', max_length=20)  # Field name made lowercase.
    manserie = models.BooleanField(db_column='MANSERIE')  # Field name made lowercase.
    mankilom = models.BooleanField(db_column='MANKILOM')  # Field name made lowercase.
    manrenta = models.BooleanField(db_column='MANRENTA')  # Field name made lowercase.
    diaini1 = models.DecimalField(db_column='DIAINI1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    diafin1 = models.DecimalField(db_column='DIAFIN1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    diatoler1 = models.DecimalField(db_column='DIATOLER1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    diaprec1 = models.DecimalField(db_column='DIAPREC1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    diaini2 = models.DecimalField(db_column='DIAINI2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    diafin2 = models.DecimalField(db_column='DIAFIN2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    diatoler2 = models.DecimalField(db_column='DIATOLER2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    diaprec2 = models.DecimalField(db_column='DIAPREC2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    diaini3 = models.DecimalField(db_column='DIAINI3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    diafin3 = models.DecimalField(db_column='DIAFIN3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    diatoler3 = models.DecimalField(db_column='DIATOLER3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    diaprec3 = models.DecimalField(db_column='DIAPREC3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    diaini4 = models.DecimalField(db_column='DIAINI4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    diafin4 = models.DecimalField(db_column='DIAFIN4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    diatoler4 = models.DecimalField(db_column='DIATOLER4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    diaprec4 = models.DecimalField(db_column='DIAPREC4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    displun = models.BooleanField(db_column='DISPLUN')  # Field name made lowercase.
    dispmar = models.BooleanField(db_column='DISPMAR')  # Field name made lowercase.
    dispmie = models.BooleanField(db_column='DISPMIE')  # Field name made lowercase.
    dispjue = models.BooleanField(db_column='DISPJUE')  # Field name made lowercase.
    dispvie = models.BooleanField(db_column='DISPVIE')  # Field name made lowercase.
    dispsab = models.BooleanField(db_column='DISPSAB')  # Field name made lowercase.
    dispdom = models.BooleanField(db_column='DISPDOM')  # Field name made lowercase.
    kilommantto = models.DecimalField(db_column='KILOMMANTTO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    rentasmantto = models.DecimalField(db_column='RENTASMANTTO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    numsemmantto = models.DecimalField(db_column='NUMSEMMANTTO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.
    factoractprecio = models.DecimalField(db_column='FACTORACTPRECIO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fleteactprecio = models.DecimalField(db_column='FLETEACTPRECIO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    codbar2 = models.CharField(db_column='CODBAR2', max_length=20)  # Field name made lowercase.
    codbar3 = models.CharField(db_column='CODBAR3', max_length=20)  # Field name made lowercase.
    codbar4 = models.CharField(db_column='CODBAR4', max_length=20)  # Field name made lowercase.
    impcodbarpos = models.BooleanField(db_column='IMPCODBARPOS')  # Field name made lowercase.
    factoractprecio2 = models.DecimalField(db_column='FACTORACTPRECIO2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    factoractprecio3 = models.DecimalField(db_column='FACTORACTPRECIO3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    factoractprecio4 = models.DecimalField(db_column='FACTORACTPRECIO4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    factoractprecio5 = models.DecimalField(db_column='FACTORACTPRECIO5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    factoractprecio6 = models.DecimalField(db_column='FACTORACTPRECIO6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    detalle = models.BooleanField(db_column='Detalle')  # Field name made lowercase.
    listado1 = models.BooleanField(db_column='Listado1')  # Field name made lowercase.
    listado2 = models.BooleanField(db_column='Listado2')  # Field name made lowercase.
    listado3 = models.BooleanField(db_column='Listado3')  # Field name made lowercase.
    listado4 = models.BooleanField(db_column='Listado4')  # Field name made lowercase.
    precioadic = models.DecimalField(db_column='PrecioAdic', max_digits=19, decimal_places=4)  # Field name made lowercase.
    listado5 = models.BooleanField(db_column='Listado5')  # Field name made lowercase.
    casco = models.DecimalField(db_column='Casco', max_digits=19, decimal_places=4)  # Field name made lowercase.
    asientos = models.DecimalField(db_column='Asientos', max_digits=19, decimal_places=4)  # Field name made lowercase.
    respaldos = models.DecimalField(db_column='Respaldos', max_digits=19, decimal_places=4)  # Field name made lowercase.
    otros1 = models.DecimalField(db_column='Otros1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    otros2 = models.DecimalField(db_column='Otros2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioadic2 = models.DecimalField(db_column='PrecioAdic2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    listadocol1 = models.BooleanField(db_column='ListadoCol1')  # Field name made lowercase.
    listadocol2 = models.BooleanField(db_column='ListadoCol2')  # Field name made lowercase.
    listado6 = models.BooleanField(db_column='Listado6')  # Field name made lowercase.
    otros3 = models.DecimalField(db_column='Otros3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    listadocol3 = models.BooleanField(db_column='ListadoCol3')  # Field name made lowercase.
    tienda = models.BooleanField(db_column='Tienda')  # Field name made lowercase.
    mayoreo = models.BooleanField(db_column='Mayoreo')  # Field name made lowercase.
    colormad1 = models.DecimalField(db_column='ColorMad1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    colormad2 = models.DecimalField(db_column='ColorMad2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    colormad3 = models.DecimalField(db_column='ColorMad3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    caducidad = models.BooleanField(db_column='Caducidad')  # Field name made lowercase.
    nivelcontrol = models.SmallIntegerField(db_column='NivelControl')  # Field name made lowercase.
    cvebodiniprod = models.IntegerField(db_column='CveBodIniProd')  # Field name made lowercase.
    precvtaimpinc = models.BooleanField(db_column='PrecVtaImpInc')  # Field name made lowercase.
    ml = models.DecimalField(max_digits=19, decimal_places=4)
    hl = models.DecimalField(max_digits=19, decimal_places=4)
    peso = models.DecimalField(max_digits=19, decimal_places=4)
    tarima = models.IntegerField()
    cvesap = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CATPROD'


class Catprodr(models.Model):
    cveprod = models.CharField(db_column='CVEPROD', max_length=20)  # Field name made lowercase.
    desprod = models.CharField(db_column='DESPROD', max_length=800)  # Field name made lowercase.
    fecalta = models.DateTimeField(db_column='FECALTA')  # Field name made lowercase.
    cveuni = models.CharField(db_column='CVEUNI', max_length=4)  # Field name made lowercase.
    cvefam = models.IntegerField(db_column='CVEFAM')  # Field name made lowercase.
    cvemar = models.IntegerField(db_column='CVEMAR')  # Field name made lowercase.
    desmod = models.CharField(db_column='DESMOD', max_length=80)  # Field name made lowercase.
    desubi = models.CharField(db_column='DESUBI', max_length=80)  # Field name made lowercase.
    tipprod = models.BooleanField(db_column='TIPPROD')  # Field name made lowercase.
    edoprod = models.BooleanField(db_column='EDOPROD')  # Field name made lowercase.
    paqprod = models.BooleanField(db_column='PAQPROD')  # Field name made lowercase.
    codbar = models.CharField(db_column='CODBAR', max_length=20)  # Field name made lowercase.
    numobj = models.IntegerField(db_column='NUMOBJ')  # Field name made lowercase.
    observa = models.TextField(db_column='OBSERVA')  # Field name made lowercase. This field type is a guess.
    fecmodprec = models.DateTimeField(db_column='FECMODPREC')  # Field name made lowercase.
    lispre1 = models.DecimalField(db_column='LISPRE1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre2 = models.DecimalField(db_column='LISPRE2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre3 = models.DecimalField(db_column='LISPRE3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre4 = models.DecimalField(db_column='LISPRE4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre5 = models.DecimalField(db_column='LISPRE5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre6 = models.DecimalField(db_column='LISPRE6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    minprod = models.DecimalField(db_column='MINPROD', max_digits=19, decimal_places=4)  # Field name made lowercase.
    maxprod = models.DecimalField(db_column='MAXPROD', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cveprodprov = models.CharField(db_column='CVEPRODPROV', max_length=20)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.
    factoractprecio = models.DecimalField(db_column='FACTORACTPRECIO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fleteactprecio = models.DecimalField(db_column='FLETEACTPRECIO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    codbar2 = models.CharField(db_column='CODBAR2', max_length=20)  # Field name made lowercase.
    codbar3 = models.CharField(db_column='CODBAR3', max_length=20)  # Field name made lowercase.
    codbar4 = models.CharField(db_column='CODBAR4', max_length=20)  # Field name made lowercase.
    impcodbarpos = models.BooleanField(db_column='IMPCODBARPOS')  # Field name made lowercase.
    factoractprecio2 = models.DecimalField(db_column='FACTORACTPRECIO2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    factoractprecio3 = models.DecimalField(db_column='FACTORACTPRECIO3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    factoractprecio4 = models.DecimalField(db_column='FACTORACTPRECIO4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    factoractprecio5 = models.DecimalField(db_column='FACTORACTPRECIO5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    factoractprecio6 = models.DecimalField(db_column='FACTORACTPRECIO6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    detalle = models.BooleanField(db_column='Detalle')  # Field name made lowercase.
    listado1 = models.BooleanField(db_column='Listado1')  # Field name made lowercase.
    listado2 = models.BooleanField(db_column='Listado2')  # Field name made lowercase.
    listado3 = models.BooleanField(db_column='Listado3')  # Field name made lowercase.
    listado4 = models.BooleanField(db_column='Listado4')  # Field name made lowercase.
    precioadic = models.DecimalField(db_column='PrecioAdic', max_digits=19, decimal_places=4)  # Field name made lowercase.
    listado5 = models.BooleanField(db_column='Listado5')  # Field name made lowercase.
    casco = models.DecimalField(db_column='Casco', max_digits=19, decimal_places=4)  # Field name made lowercase.
    otros1 = models.DecimalField(db_column='Otros1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    otros2 = models.DecimalField(db_column='Otros2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioadic2 = models.DecimalField(db_column='PrecioAdic2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    listado6 = models.BooleanField(db_column='Listado6')  # Field name made lowercase.
    otros3 = models.DecimalField(db_column='Otros3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tienda = models.BooleanField(db_column='Tienda')  # Field name made lowercase.
    mayoreo = models.BooleanField(db_column='Mayoreo')  # Field name made lowercase.
    caducidad = models.BooleanField(db_column='Caducidad')  # Field name made lowercase.
    ml = models.DecimalField(max_digits=19, decimal_places=4)
    hl = models.DecimalField(max_digits=19, decimal_places=4)
    peso = models.DecimalField(max_digits=19, decimal_places=4)
    tarima = models.IntegerField()
    cvesap = models.CharField(max_length=50)
    codbar5 = models.CharField(max_length=20)
    codbar6 = models.CharField(max_length=20)
    codbar7 = models.CharField(max_length=20)
    cvegpo_pres = models.IntegerField()
    cve_pres = models.IntegerField()
    claveprodser = models.CharField(max_length=50)
    cveunidad = models.CharField(max_length=50)
    cveimpuesto = models.CharField(max_length=50)
    cvetipofactor = models.CharField(max_length=50)
    impuestos = models.DecimalField(max_digits=19, decimal_places=4)
    cospro = models.DecimalField(max_digits=19, decimal_places=4)
    ultcos = models.DecimalField(max_digits=19, decimal_places=4)
    validacosto = models.BooleanField()
    numref = models.CharField(max_length=50)
    escalable = models.BooleanField()
    fechainiescala = models.DateTimeField()
    fechafinescala = models.DateTimeField()
    promocion = models.BooleanField()
    fechainipromo = models.DateTimeField()
    fechafinpromo = models.DateTimeField()
    agrupado = models.BooleanField()
    cvedepto = models.IntegerField()
    cveseccion = models.IntegerField()
    cvesubfam = models.IntegerField()
    porciva = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps1 = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps2 = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps3 = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps4 = models.DecimalField(max_digits=19, decimal_places=4)
    cveimptoc = models.IntegerField()
    cveimptov = models.IntegerField()
    fechaactcosto = models.DateTimeField(db_column='FECHAACTCOSTO')  # Field name made lowercase.
    desprodcorta = models.CharField(max_length=400)
    promocionar = models.BooleanField()
    cvelinea = models.IntegerField()
    vtasauto = models.IntegerField()
    cveprodprov2 = models.IntegerField()
    cveprodprov3 = models.IntegerField()
    cveprodprov4 = models.IntegerField()
    cveprodprov5 = models.IntegerField()
    cveprodprov6 = models.IntegerField()
    cveprodprov7 = models.IntegerField()
    cveprodprov8 = models.IntegerField()
    fechacad = models.DateTimeField()
    cenvase = models.BooleanField()
    cantidade = models.IntegerField()
    precioe = models.DecimalField(max_digits=19, decimal_places=4)
    img = models.BooleanField()
    imgprod = models.BinaryField(blank=True, null=True)
    facturar = models.BooleanField()
    vigencia = models.BooleanField()
    cvetippaq = models.IntegerField()
    validavtas = models.BooleanField()
    fechainival = models.DateTimeField(db_column='fechainiVal')  # Field name made lowercase.
    numref2 = models.CharField(max_length=50)
    vigescala = models.BooleanField()
    vigpromo = models.BooleanField()
    fecmod = models.DateTimeField()
    clasvta = models.IntegerField()
    valvtas = models.IntegerField()
    tarimas = models.BooleanField()
    pzastari = models.IntegerField()
    cvetarima = models.CharField(max_length=50)
    cveenvaces = models.CharField(max_length=50)
    cvebodtari = models.IntegerField()
    cvebodenva = models.IntegerField()
    envaces = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CATPRODR'


class Catprodreje(models.Model):
    cveprod = models.CharField(db_column='CVEPROD', max_length=20)  # Field name made lowercase.
    desprod = models.CharField(db_column='DESPROD', max_length=800)  # Field name made lowercase.
    fecalta = models.DateTimeField(db_column='FECALTA')  # Field name made lowercase.
    cveuni = models.CharField(db_column='CVEUNI', max_length=4)  # Field name made lowercase.
    cvefam = models.IntegerField(db_column='CVEFAM')  # Field name made lowercase.
    cvemar = models.IntegerField(db_column='CVEMAR')  # Field name made lowercase.
    desmod = models.CharField(db_column='DESMOD', max_length=80)  # Field name made lowercase.
    desubi = models.CharField(db_column='DESUBI', max_length=80)  # Field name made lowercase.
    tipprod = models.BooleanField(db_column='TIPPROD')  # Field name made lowercase.
    edoprod = models.BooleanField(db_column='EDOPROD')  # Field name made lowercase.
    paqprod = models.BooleanField(db_column='PAQPROD')  # Field name made lowercase.
    codbar = models.CharField(db_column='CODBAR', max_length=20)  # Field name made lowercase.
    numobj = models.IntegerField(db_column='NUMOBJ')  # Field name made lowercase.
    observa = models.TextField(db_column='OBSERVA')  # Field name made lowercase. This field type is a guess.
    fecmodprec = models.DateTimeField(db_column='FECMODPREC')  # Field name made lowercase.
    lispre1 = models.DecimalField(db_column='LISPRE1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre2 = models.DecimalField(db_column='LISPRE2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre3 = models.DecimalField(db_column='LISPRE3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre4 = models.DecimalField(db_column='LISPRE4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre5 = models.DecimalField(db_column='LISPRE5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre6 = models.DecimalField(db_column='LISPRE6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    minprod = models.DecimalField(db_column='MINPROD', max_digits=19, decimal_places=4)  # Field name made lowercase.
    maxprod = models.DecimalField(db_column='MAXPROD', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cveprodprov = models.CharField(db_column='CVEPRODPROV', max_length=20)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.
    factoractprecio = models.DecimalField(db_column='FACTORACTPRECIO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fleteactprecio = models.DecimalField(db_column='FLETEACTPRECIO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    codbar2 = models.CharField(db_column='CODBAR2', max_length=20)  # Field name made lowercase.
    codbar3 = models.CharField(db_column='CODBAR3', max_length=20)  # Field name made lowercase.
    codbar4 = models.CharField(db_column='CODBAR4', max_length=20)  # Field name made lowercase.
    impcodbarpos = models.BooleanField(db_column='IMPCODBARPOS')  # Field name made lowercase.
    factoractprecio2 = models.DecimalField(db_column='FACTORACTPRECIO2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    factoractprecio3 = models.DecimalField(db_column='FACTORACTPRECIO3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    factoractprecio4 = models.DecimalField(db_column='FACTORACTPRECIO4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    factoractprecio5 = models.DecimalField(db_column='FACTORACTPRECIO5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    factoractprecio6 = models.DecimalField(db_column='FACTORACTPRECIO6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    detalle = models.BooleanField(db_column='Detalle')  # Field name made lowercase.
    listado1 = models.BooleanField(db_column='Listado1')  # Field name made lowercase.
    listado2 = models.BooleanField(db_column='Listado2')  # Field name made lowercase.
    listado3 = models.BooleanField(db_column='Listado3')  # Field name made lowercase.
    listado4 = models.BooleanField(db_column='Listado4')  # Field name made lowercase.
    precioadic = models.DecimalField(db_column='PrecioAdic', max_digits=19, decimal_places=4)  # Field name made lowercase.
    listado5 = models.BooleanField(db_column='Listado5')  # Field name made lowercase.
    casco = models.DecimalField(db_column='Casco', max_digits=19, decimal_places=4)  # Field name made lowercase.
    otros1 = models.DecimalField(db_column='Otros1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    otros2 = models.DecimalField(db_column='Otros2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    precioadic2 = models.DecimalField(db_column='PrecioAdic2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    listado6 = models.BooleanField(db_column='Listado6')  # Field name made lowercase.
    otros3 = models.DecimalField(db_column='Otros3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tienda = models.BooleanField(db_column='Tienda')  # Field name made lowercase.
    mayoreo = models.BooleanField(db_column='Mayoreo')  # Field name made lowercase.
    caducidad = models.BooleanField(db_column='Caducidad')  # Field name made lowercase.
    ml = models.DecimalField(max_digits=19, decimal_places=4)
    hl = models.DecimalField(max_digits=19, decimal_places=4)
    peso = models.DecimalField(max_digits=19, decimal_places=4)
    tarima = models.IntegerField()
    cvesap = models.CharField(max_length=50)
    codbar5 = models.CharField(max_length=20)
    codbar6 = models.CharField(max_length=20)
    codbar7 = models.CharField(max_length=20)
    cvegpo_pres = models.IntegerField()
    cve_pres = models.IntegerField()
    claveprodser = models.CharField(max_length=50)
    cveunidad = models.CharField(max_length=50)
    cveimpuesto = models.CharField(max_length=50)
    cvetipofactor = models.CharField(max_length=50)
    impuestos = models.DecimalField(max_digits=19, decimal_places=4)
    cospro = models.DecimalField(max_digits=19, decimal_places=4)
    ultcos = models.DecimalField(max_digits=19, decimal_places=4)
    validacosto = models.BooleanField()
    numref = models.CharField(max_length=50)
    escalable = models.BooleanField()
    fechainiescala = models.DateTimeField()
    fechafinescala = models.DateTimeField()
    promocion = models.BooleanField()
    fechainipromo = models.DateTimeField()
    fechafinpromo = models.DateTimeField()
    agrupado = models.BooleanField()
    cvedepto = models.IntegerField()
    cveseccion = models.IntegerField()
    cvesubfam = models.IntegerField()
    porciva = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps1 = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps2 = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps3 = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps4 = models.DecimalField(max_digits=19, decimal_places=4)
    cveimptoc = models.IntegerField()
    cveimptov = models.IntegerField()
    fechaactcosto = models.DateTimeField(db_column='FECHAACTCOSTO')  # Field name made lowercase.
    desprodcorta = models.CharField(max_length=400)
    promocionar = models.BooleanField()
    cvelinea = models.IntegerField()
    vtasauto = models.IntegerField()
    cveprodprov2 = models.IntegerField()
    cveprodprov3 = models.IntegerField()
    cveprodprov4 = models.IntegerField()
    cveprodprov5 = models.IntegerField()
    cveprodprov6 = models.IntegerField()
    cveprodprov7 = models.IntegerField()
    cveprodprov8 = models.IntegerField()
    fechacad = models.DateTimeField()
    cenvase = models.BooleanField()
    cantidade = models.IntegerField(blank=True, null=True)
    precioe = models.DecimalField(max_digits=19, decimal_places=4)
    img = models.BooleanField()
    imgprod = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CATPRODREJE'


class Catprov(models.Model):
    cveprov = models.IntegerField(db_column='CVEPROV')  # Field name made lowercase.
    nomprov = models.CharField(db_column='NOMPROV', max_length=80)  # Field name made lowercase.
    razprov = models.CharField(db_column='RAZPROV', max_length=80)  # Field name made lowercase.
    dirprov = models.CharField(db_column='DIRPROV', max_length=80)  # Field name made lowercase.
    colprov = models.CharField(db_column='COLPROV', max_length=80)  # Field name made lowercase.
    cveciu = models.CharField(db_column='CVECIU', max_length=80)  # Field name made lowercase.
    cveedo = models.CharField(db_column='CVEEDO', max_length=80, blank=True, null=True)  # Field name made lowercase.
    cvegruprov = models.IntegerField(db_column='CVEGRUPROV')  # Field name made lowercase.
    tiprfc = models.BooleanField(db_column='TIPRFC')  # Field name made lowercase.
    rfccar = models.CharField(db_column='RFCCAR', max_length=4)  # Field name made lowercase.
    rfcnum = models.CharField(db_column='RFCNUM', max_length=6)  # Field name made lowercase.
    rfchom = models.CharField(db_column='RFCHOM', max_length=3)  # Field name made lowercase.
    fecprov = models.DateTimeField(db_column='FECPROV')  # Field name made lowercase.
    curprov = models.CharField(db_column='CURPROV', max_length=25)  # Field name made lowercase.
    emailprov = models.CharField(db_column='EMAILPROV', max_length=50)  # Field name made lowercase.
    tel1prov = models.CharField(db_column='TEL1PROV', max_length=25)  # Field name made lowercase.
    tel2prov = models.CharField(db_column='TEL2PROV', max_length=25)  # Field name made lowercase.
    faxprov = models.CharField(db_column='FAXPROV', max_length=25)  # Field name made lowercase.
    contprov = models.CharField(db_column='CONTPROV', max_length=80)  # Field name made lowercase.
    dircontprov = models.CharField(db_column='DIRCONTPROV', max_length=80)  # Field name made lowercase.
    telcontprov = models.CharField(db_column='TELCONTPROV', max_length=25)  # Field name made lowercase.
    emailcontprov = models.CharField(db_column='EMAILCONTPROV', max_length=50)  # Field name made lowercase.
    obsprov = models.TextField(db_column='OBSPROV')  # Field name made lowercase. This field type is a guess.
    limcred = models.DecimalField(db_column='LIMCRED', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ctaprov = models.CharField(db_column='CTAPROV', max_length=30)  # Field name made lowercase.
    cveban = models.IntegerField(db_column='CVEBAN')  # Field name made lowercase.
    cpprov = models.CharField(db_column='CPPROV', max_length=6)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.
    diascred = models.IntegerField(db_column='DIASCRED')  # Field name made lowercase.
    condpago = models.CharField(db_column='CONDPAGO', max_length=150)  # Field name made lowercase.
    ctaconprov = models.CharField(db_column='CTACONPROV', max_length=50)  # Field name made lowercase.
    modprecvtadirec = models.BooleanField(db_column='ModPrecVtaDirec')  # Field name made lowercase.
    ctaprov2 = models.CharField(db_column='CTAPROV2', max_length=30)  # Field name made lowercase.
    cveban2 = models.IntegerField(db_column='CVEBAN2')  # Field name made lowercase.
    ctaprov3 = models.CharField(db_column='CTAPROV3', max_length=30)  # Field name made lowercase.
    cveban3 = models.IntegerField(db_column='CVEBAN3')  # Field name made lowercase.
    ctaprov4 = models.CharField(db_column='CTAPROV4', max_length=30)  # Field name made lowercase.
    cveban4 = models.IntegerField(db_column='CVEBAN4')  # Field name made lowercase.
    ctaconta = models.CharField(db_column='CTACONTA', max_length=25)  # Field name made lowercase.
    rfc = models.CharField(db_column='RFC', max_length=20)  # Field name made lowercase.
    ctacontapri = models.CharField(max_length=25)
    ctacontasec = models.CharField(max_length=25)
    actpredir = models.BooleanField()
    porcact = models.DecimalField(max_digits=19, decimal_places=4)
    impactpre = models.DecimalField(max_digits=19, decimal_places=4)
    tipopago = models.IntegerField()
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CATPROV'


class Catpun(models.Model):
    cvepun = models.IntegerField(db_column='CVEPUN')  # Field name made lowercase.
    despun = models.CharField(db_column='DESPUN', max_length=80)  # Field name made lowercase.
    imppun = models.DecimalField(db_column='IMPPUN', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATPUN'


class Cattpgo(models.Model):
    cvetippag = models.IntegerField(db_column='CVETIPPAG')  # Field name made lowercase.
    destippag = models.CharField(db_column='DESTIPPAG', max_length=80)  # Field name made lowercase.
    tiptran = models.SmallIntegerField(db_column='TIPTRAN')  # Field name made lowercase.
    obstippag = models.CharField(db_column='OBSTIPPAG', max_length=80)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATTPGO'


class Catuni(models.Model):
    cveuni = models.IntegerField(db_column='CVEUNI')  # Field name made lowercase.
    desuni = models.CharField(db_column='DESUNI', max_length=80)  # Field name made lowercase.
    decuni = models.BooleanField(db_column='DECUNI')  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATUNI'


class Catven(models.Model):
    cveven = models.IntegerField(db_column='CVEVEN')  # Field name made lowercase.
    nomven = models.CharField(db_column='NOMVEN', max_length=80)  # Field name made lowercase.
    dirven = models.CharField(db_column='DIRVEN', max_length=80)  # Field name made lowercase.
    colven = models.CharField(db_column='COLVEN', max_length=80)  # Field name made lowercase.
    cpven = models.CharField(db_column='CPVEN', max_length=6)  # Field name made lowercase.
    cveciuven = models.IntegerField(db_column='CVECIUVEN')  # Field name made lowercase.
    telven = models.CharField(db_column='TELVEN', max_length=25)  # Field name made lowercase.
    fecven = models.DateTimeField(db_column='FECVEN')  # Field name made lowercase.
    emailven = models.CharField(db_column='EMAILVEN', max_length=50)  # Field name made lowercase.
    tipcomven = models.SmallIntegerField(db_column='TIPCOMVEN')  # Field name made lowercase.
    porccomven = models.DecimalField(db_column='PORCCOMVEN', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.
    impcomven = models.DecimalField(db_column='IMPCOMVEN', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cvecom = models.IntegerField(db_column='CVECOM')  # Field name made lowercase.
    index_rut = models.IntegerField()
    descripcion_rut = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'CATVEN'


class Cospro(models.Model):
    cvebod = models.IntegerField(db_column='CVEBOD')  # Field name made lowercase.
    fecmov = models.DateTimeField(db_column='FecMov')  # Field name made lowercase.
    cveprod = models.CharField(db_column='CveProd', max_length=20)  # Field name made lowercase.
    costo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cant = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cospro = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COSPRO'


class Caducidades(models.Model):
    cveprod = models.CharField(db_column='CveProd', max_length=20)  # Field name made lowercase.
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    feccad = models.DateTimeField(db_column='FecCad')  # Field name made lowercase.
    cantent = models.DecimalField(db_column='CantEnt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantsal = models.DecimalField(db_column='CantSal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechahora = models.DateTimeField(db_column='FechaHora')  # Field name made lowercase.
    cvebodent = models.IntegerField(db_column='CveBodEnt')  # Field name made lowercase.
    cvemovent = models.IntegerField(db_column='CveMovEnt')  # Field name made lowercase.
    sermovent = models.CharField(db_column='SerMovEnt', max_length=2)  # Field name made lowercase.
    folmovent = models.IntegerField(db_column='FolMovEnt')  # Field name made lowercase.
    cvebodsal = models.IntegerField(db_column='CveBodSal')  # Field name made lowercase.
    cvemovsal = models.IntegerField(db_column='CveMovSal')  # Field name made lowercase.
    sermovsal = models.CharField(db_column='SerMovSal', max_length=2)  # Field name made lowercase.
    folmovsal = models.IntegerField(db_column='FolMovSal')  # Field name made lowercase.
    obsent = models.CharField(db_column='ObsEnt', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Caducidades'


class Cargaexistencia(models.Model):
    numref = models.CharField(max_length=50)
    desprod = models.CharField(max_length=800)
    existencia = models.IntegerField()
    encontrado = models.BooleanField()
    stockmin = models.IntegerField()
    stockmax = models.IntegerField()
    ucosto = models.DecimalField(max_digits=19, decimal_places=4)
    cospro = models.DecimalField(max_digits=19, decimal_places=4)
    precio1 = models.DecimalField(db_column='Precio1', max_digits=18, decimal_places=10)  # Field name made lowercase.
    precio2 = models.DecimalField(max_digits=19, decimal_places=4)
    precio3 = models.DecimalField(db_column='Precio3', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CargaExistencia'


class Catautomoviles(models.Model):
    cveauto = models.IntegerField(db_column='CveAuto')  # Field name made lowercase.
    fechaalta = models.DateTimeField(db_column='FechaAlta')  # Field name made lowercase.
    desauto = models.CharField(db_column='DesAuto', max_length=150)  # Field name made lowercase.
    cvemarca = models.IntegerField(db_column='CveMarca')  # Field name made lowercase.
    modelo = models.IntegerField(db_column='Modelo')  # Field name made lowercase.
    placas = models.CharField(db_column='Placas', max_length=15)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=20)  # Field name made lowercase.
    cvetipocomb = models.IntegerField(db_column='CveTipoComb')  # Field name made lowercase.
    numseriech = models.CharField(db_column='NumSerieCh', max_length=100)  # Field name made lowercase.
    numseriem = models.CharField(db_column='NumSerieM', max_length=100)  # Field name made lowercase.
    kilometraje = models.IntegerField(db_column='Kilometraje')  # Field name made lowercase.
    estatus = models.BooleanField(db_column='Estatus')  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=15)  # Field name made lowercase.
    fechamov = models.DateTimeField(db_column='Fechamov')  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CatAutomoviles'


class Catban(models.Model):
    cveban = models.IntegerField(db_column='CVEBAN')  # Field name made lowercase.
    nomban = models.CharField(db_column='NOMBAN', max_length=80)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CatBan'


class Catclascli(models.Model):
    cveclascli = models.IntegerField()
    desclacli = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'CatClasCli'


class Catconductores(models.Model):
    empresa = models.IntegerField()
    cveconductor = models.IntegerField()
    nomconductor = models.CharField(max_length=100)
    ife = models.CharField(max_length=50)
    numlic = models.CharField(max_length=50)
    tipolic = models.CharField(max_length=10)
    fechavence = models.DateTimeField()
    login = models.CharField(max_length=10)
    fecharegistro = models.DateTimeField()
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CatConductores'


class Catcuentascontable1(models.Model):
    numcta = models.CharField(max_length=50)
    descta = models.CharField(max_length=100)
    cvetipocta = models.IntegerField()
    cvenaturaleza = models.IntegerField()
    activa = models.BooleanField()
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CatCuentasContable1'


class Catcuentascontables2(models.Model):
    cvectapri = models.CharField(max_length=50)
    desctapri = models.CharField(max_length=100)
    cvectasec = models.CharField(max_length=80)
    desctasec = models.CharField(max_length=100)
    cvetipoctasec = models.IntegerField()
    cvetiponatsec = models.IntegerField()
    activa = models.BooleanField()
    usuario = models.CharField(max_length=50)
    fechacrecion = models.DateTimeField(blank=True, null=True)
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CatCuentasContables2'


class Catdefinepromo(models.Model):
    cvedefinepromo = models.IntegerField()
    desdefinepromo = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'CatDefinepromo'


class Catdeptos(models.Model):
    cvedepto = models.IntegerField()
    desdepto = models.CharField(max_length=50)
    activo = models.BooleanField()
    usuario = models.CharField(max_length=15)
    fechacreacion = models.DateTimeField()
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CatDeptos'


class Catgironegocio(models.Model):
    cvegironeg = models.IntegerField()
    destiponeg = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'CatGiroNegocio'


class Catlinea(models.Model):
    cvemarca = models.IntegerField()
    cvelinea = models.IntegerField()
    deslinea = models.CharField(max_length=50)
    fechacreacion = models.DateTimeField()
    login = models.CharField(max_length=25)
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CatLinea'


class Catlispre(models.Model):
    cvelista = models.IntegerField()
    deslista = models.CharField(db_column='Deslista', max_length=20)  # Field name made lowercase.
    activa = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CatLisPre'


class Catmarcaenfriadores(models.Model):
    cvemarca = models.IntegerField()
    descmarca = models.CharField(max_length=50)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CatMarcaEnfriadores'


class Catmoviles(models.Model):
    cvemovil = models.IntegerField()
    descmovil = models.CharField(max_length=30)
    activo = models.BooleanField()
    imei = models.CharField(db_column='IMEI', max_length=20)  # Field name made lowercase.
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'CatMoviles'


class Catnatcta(models.Model):
    cvenaturaleza = models.IntegerField()
    desnaturaleza = models.CharField(max_length=80)
    activa = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CatNatCta'


class Catpreventa(models.Model):
    cvepreventa = models.IntegerField()
    despreventa = models.CharField(max_length=800)
    cvereparto = models.IntegerField()
    desreparto = models.CharField(max_length=80)
    activo = models.BooleanField()
    fechacre = models.DateTimeField()
    usercre = models.CharField(max_length=20)
    lunes = models.BooleanField()
    martes = models.BooleanField()
    miercoles = models.BooleanField()
    jueves = models.BooleanField()
    viernes = models.BooleanField()
    sabado = models.BooleanField()
    domingo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CatPreventa'


class Catpromotores(models.Model):
    numero_promotor = models.IntegerField()
    nombre_promotor = models.CharField(max_length=50)
    nombre = models.CharField(max_length=20)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20)
    direccion = models.CharField(max_length=80)
    numero_ext = models.IntegerField(db_column='Numero_ext')  # Field name made lowercase.
    numero_int = models.IntegerField()
    colonia = models.CharField(max_length=15)
    ciudad = models.IntegerField()
    poblacion = models.IntegerField(db_column='Poblacion')  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.
    sexo = models.CharField(max_length=1)
    telefono1 = models.IntegerField(db_column='Telefono1')  # Field name made lowercase.
    telefono2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CatPromotores'


class Catprovcli(models.Model):
    cveprovcli = models.IntegerField()
    desprovcli = models.CharField(db_column='desprovCli', max_length=80)  # Field name made lowercase.
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CatProvCli'


class Catrefaccionaria(models.Model):
    empresa = models.IntegerField()
    cverefaccionaria = models.IntegerField()
    nomrefaccionaria = models.CharField(max_length=100)
    dirrefaccionaria = models.CharField(max_length=150)
    telrefaccionaria = models.CharField(max_length=20)
    contacto = models.CharField(max_length=50)
    login = models.CharField(max_length=15)
    fechareg = models.DateTimeField()
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CatRefaccionaria'


class Catreparto(models.Model):
    cvereparto = models.IntegerField()
    desreparto = models.CharField(max_length=80)
    activo = models.BooleanField()
    fechacre = models.DateTimeField()
    usercre = models.CharField(max_length=20)
    lunes = models.BooleanField()
    martes = models.BooleanField()
    miercoles = models.BooleanField()
    jueves = models.BooleanField()
    viernes = models.BooleanField()
    sabado = models.BooleanField()
    domingo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CatReparto'


class Catsecciones(models.Model):
    cvedepto = models.IntegerField()
    cveseccion = models.IntegerField()
    desseccion = models.CharField(max_length=80)
    activo = models.BooleanField()
    usuario = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField()
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CatSecciones'


class Catservicios(models.Model):
    empresa = models.IntegerField()
    cveservicio = models.IntegerField()
    desservicio = models.CharField(max_length=80)
    impservicio = models.DecimalField(max_digits=19, decimal_places=4)
    login = models.CharField(max_length=15)
    fechareg = models.DateTimeField()
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CatServicios'


class Catsubfamilias(models.Model):
    cvedepto = models.IntegerField()
    cveseccion = models.IntegerField()
    cvefam = models.IntegerField()
    cvesubfam = models.IntegerField()
    dessubfam = models.CharField(max_length=80)
    activo = models.BooleanField()
    usuario = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField()
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CatSubFamilias'


class Cattaller(models.Model):
    empresa = models.IntegerField()
    cvetaller = models.IntegerField()
    destaller = models.CharField(max_length=80)
    dirtaller = models.CharField(max_length=80)
    teltaller = models.CharField(max_length=15)
    contacto = models.CharField(max_length=50)
    login = models.CharField(max_length=20)
    fechareg = models.DateTimeField()
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CatTaller'


class Cattippaq(models.Model):
    cvetippaq = models.IntegerField()
    destippaq = models.CharField(max_length=25)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CatTipPaq'


class Cattippromo(models.Model):
    cvepromo = models.IntegerField()
    despromo = models.CharField(max_length=100)
    cvetipocomprap = models.IntegerField()
    cvedefinepromo = models.IntegerField()
    activa = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CatTipPromo'


class Cattipoalmacen(models.Model):
    tipo_almacen = models.IntegerField()
    desc_tipo = models.CharField(db_column='Desc_tipo', max_length=20)  # Field name made lowercase.
    activa = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CatTipoAlmacen'


class Cattipocta(models.Model):
    cvetipocta = models.IntegerField()
    destipocta = models.CharField(max_length=80)
    activa = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CatTipoCta'


class Cattipoenfriador(models.Model):
    cvetipo = models.IntegerField()
    desctipo = models.CharField(max_length=50)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CatTipoEnfriador'


class Cattiponegocio(models.Model):
    cvetiponeg = models.IntegerField()
    destiponeg = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'CatTipoNegocio'


class CattipoCliente(models.Model):
    cve_tipo = models.IntegerField()
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CatTipo_cliente'


class Cattipomovprod(models.Model):
    cvetipomovprod = models.IntegerField()
    destipomovprod = models.CharField(max_length=50)
    aplicacosto = models.BooleanField()
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CatTipomovProd'


class Catturnosvta(models.Model):
    numturno = models.IntegerField()
    desturno = models.CharField(max_length=50)
    periodo = models.IntegerField()
    fechacreacion = models.DateTimeField()
    login = models.CharField(max_length=20)
    sercierret = models.CharField(db_column='sercierreT', max_length=10)  # Field name made lowercase.
    folcierret = models.IntegerField(db_column='folcierreT')  # Field name made lowercase.
    abierto = models.BooleanField()
    indice = models.BooleanField()
    usuario = models.CharField(max_length=20)
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CatTurnosVta'


class Catclientes(models.Model):
    numero_cliente = models.IntegerField()
    eventual = models.BooleanField(blank=True, null=True)
    tipo_cliente = models.IntegerField(blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True)
    razon_cliente = models.CharField(max_length=80, blank=True, null=True)
    nombre_comercial = models.CharField(max_length=80, blank=True, null=True)
    direccion_cliente = models.CharField(max_length=80, blank=True, null=True)
    numero_exterior = models.IntegerField(blank=True, null=True)
    colonia = models.CharField(max_length=50, blank=True, null=True)
    municipio = models.IntegerField()
    cpostal = models.IntegerField()
    ciudad = models.CharField(max_length=80, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    pais = models.IntegerField(blank=True, null=True)
    rfc = models.CharField(max_length=15, blank=True, null=True)
    curp = models.CharField(max_length=30, blank=True, null=True)
    telefono1 = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    contacto = models.CharField(max_length=40, blank=True, null=True)
    dueño_empresa = models.CharField(max_length=40, blank=True, null=True)
    foto_cliente = models.BinaryField(blank=True, null=True)
    latitud = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    longitud = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    documento1 = models.BinaryField(blank=True, null=True)
    documento2 = models.BinaryField(blank=True, null=True)
    documento3 = models.BinaryField(blank=True, null=True)
    documento4 = models.BinaryField(blank=True, null=True)
    limite_credito = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    plazo = models.IntegerField(blank=True, null=True)
    dias_apartado = models.IntegerField(blank=True, null=True)
    lista_precios = models.IntegerField(blank=True, null=True)
    descuento_cliente = models.IntegerField(blank=True, null=True)
    cadena_cliente = models.IntegerField(blank=True, null=True)
    giro_cliente = models.IntegerField(blank=True, null=True)
    zona = models.IntegerField(blank=True, null=True)
    ruta = models.IntegerField(blank=True, null=True)
    grupo_comisiones = models.IntegerField(blank=True, null=True)
    lineas_captura = models.IntegerField(blank=True, null=True)
    periodo_visita = models.CharField(max_length=50, blank=True, null=True)
    pronto_pago = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    lun = models.BooleanField(blank=True, null=True)
    mart = models.BooleanField(blank=True, null=True)
    mier = models.BooleanField(blank=True, null=True)
    juev = models.BooleanField(blank=True, null=True)
    vier = models.BooleanField(blank=True, null=True)
    sab = models.BooleanField(blank=True, null=True)
    dom = models.BooleanField(blank=True, null=True)
    cuenta_contable = models.IntegerField(blank=True, null=True)
    rfc_facturacion = models.CharField(max_length=15, blank=True, null=True)
    nombre_facturacion = models.CharField(max_length=50, blank=True, null=True)
    direccion_facturacion = models.CharField(max_length=80, blank=True, null=True)
    numero_facturacion = models.IntegerField(blank=True, null=True)
    colonia_facturacion = models.CharField(max_length=50, blank=True, null=True)
    municipio_facturacion = models.IntegerField(blank=True, null=True)
    cpostal_facturacion = models.IntegerField(blank=True, null=True)
    ciudad_facturacion = models.CharField(max_length=80, blank=True, null=True)
    estado_facturacion = models.IntegerField(blank=True, null=True)
    pais_facturacion = models.IntegerField(blank=True, null=True)
    entrecalleycalle_facturacion = models.CharField(max_length=80, blank=True, null=True)
    telefono_facturacion = models.CharField(max_length=20, blank=True, null=True)
    email_facturacion = models.CharField(max_length=40, blank=True, null=True)
    nombre_negocio = models.CharField(max_length=80, blank=True, null=True)
    direccion_negocio = models.CharField(max_length=80, blank=True, null=True)
    numero_exterior_negocio = models.IntegerField(blank=True, null=True)
    colonia_negocio = models.CharField(max_length=50, blank=True, null=True)
    municipio_negocio = models.IntegerField(blank=True, null=True)
    ciudad_negocio = models.CharField(max_length=80, blank=True, null=True)
    estado_negocio = models.IntegerField(blank=True, null=True)
    fecha_cambioestatus = models.DateField(blank=True, null=True)
    fecha_mantenimiento = models.DateField(blank=True, null=True)
    fecha_visita = models.DateField(blank=True, null=True)
    rev_facvenci = models.BooleanField(blank=True, null=True)
    mayor_uncredito = models.BooleanField(blank=True, null=True)
    cobra_ruta = models.BooleanField(blank=True, null=True)
    fecha_baja = models.DateTimeField(blank=True, null=True)
    baja = models.BooleanField(blank=True, null=True)
    saldo_cli = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Catclientes'


class Catcombv(models.Model):
    cvecombv = models.IntegerField()
    descombv = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Catcombv'


class CatestatusClientes(models.Model):
    cve_estatus = models.IntegerField()
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Catestatus_clientes'


class Catmarv(models.Model):
    cvemarv = models.IntegerField()
    desmarv = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Catmarv'


class Cattipobod(models.Model):
    cvetipobod = models.IntegerField()
    destipobod = models.CharField(max_length=50)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Cattipobod'


class Cattipocomprapromo(models.Model):
    cvetipocomprap = models.IntegerField()
    destipocomprap = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'Cattipocomprapromo'


class Cierresdia(models.Model):
    sercierre = models.CharField(max_length=3)
    folcierre = models.IntegerField()
    numturno = models.IntegerField(db_column='numTurno')  # Field name made lowercase.
    desturno = models.CharField(db_column='DesTurno', max_length=50)  # Field name made lowercase.
    caja = models.CharField(db_column='Caja', max_length=20)  # Field name made lowercase.
    cajero = models.CharField(db_column='Cajero', max_length=20)  # Field name made lowercase.
    fechainicio = models.DateTimeField(db_column='FechaInicio')  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='FechaFin')  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=4)  # Field name made lowercase.
    folioini = models.IntegerField(db_column='FolioIni')  # Field name made lowercase.
    foliofin = models.IntegerField(db_column='FolioFin')  # Field name made lowercase.
    tickets = models.IntegerField(db_column='Tickets')  # Field name made lowercase.
    vtaefectivo = models.DecimalField(db_column='VtaEfectivo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vtacheque = models.DecimalField(db_column='vtaCheque', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vtatransferencias = models.DecimalField(db_column='vtaTransferencias', max_digits=19, decimal_places=4)  # Field name made lowercase.
    vtatarjetas = models.DecimalField(db_column='Vtatarjetas', max_digits=19, decimal_places=4)  # Field name made lowercase.
    totalvta = models.DecimalField(db_column='TotalVta', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cancelaciones = models.DecimalField(max_digits=19, decimal_places=4)
    vtaneta = models.DecimalField(db_column='VtaNeta', max_digits=19, decimal_places=4)  # Field name made lowercase.
    totalret = models.DecimalField(db_column='TotalRet', max_digits=19, decimal_places=4)  # Field name made lowercase.
    difventa = models.DecimalField(db_column='DifVenta', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ticketefec = models.IntegerField(db_column='TicketEfec')  # Field name made lowercase.
    ticketche = models.IntegerField(db_column='TicketChe')  # Field name made lowercase.
    tickettrans = models.IntegerField(db_column='TicketTrans')  # Field name made lowercase.
    tickettarje = models.IntegerField(db_column='TicketTarje')  # Field name made lowercase.
    tickettotal = models.IntegerField(db_column='TicketTotal')  # Field name made lowercase.
    ticketcan = models.IntegerField(db_column='TicketCan')  # Field name made lowercase.
    ticketnetos = models.IntegerField(db_column='TicketNetos')  # Field name made lowercase.
    ticketretiros = models.IntegerField(db_column='TicketRetiros')  # Field name made lowercase.
    base0 = models.DecimalField(db_column='Base0', max_digits=19, decimal_places=4)  # Field name made lowercase.
    base16 = models.DecimalField(db_column='Base16', max_digits=19, decimal_places=4)  # Field name made lowercase.
    baseieps1 = models.DecimalField(db_column='Baseieps1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    baseieps2 = models.DecimalField(db_column='Baseieps2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    baseieps3 = models.DecimalField(db_column='Baseieps3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    baseieps4 = models.DecimalField(db_column='Baseieps4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porciva = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps1 = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps2 = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps3 = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps4 = models.DecimalField(max_digits=19, decimal_places=4)
    impiva = models.DecimalField(max_digits=19, decimal_places=4)
    impieps1 = models.DecimalField(max_digits=19, decimal_places=4)
    impieps2 = models.DecimalField(max_digits=19, decimal_places=4)
    impieps3 = models.DecimalField(max_digits=19, decimal_places=4)
    impieps4 = models.DecimalField(max_digits=19, decimal_places=4)
    cerrado = models.BooleanField()
    usercerro = models.CharField(max_length=20)
    fechacerro = models.DateTimeField()
    contabilizado = models.BooleanField()
    userconta = models.CharField(max_length=20)
    fechaconta = models.DateTimeField()
    ingbancos = models.BooleanField(db_column='IngBancos')  # Field name made lowercase.
    useringbanco = models.CharField(max_length=20)
    fechaingbanco = models.DateTimeField()
    empresa = models.IntegerField()
    nomequipo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'CierresDia'


class Cierresturno(models.Model):
    sercierre = models.CharField(max_length=10, blank=True, null=True)
    folcierre = models.IntegerField(blank=True, null=True)
    numturno = models.IntegerField(db_column='numTurno', blank=True, null=True)  # Field name made lowercase.
    desturno = models.CharField(db_column='DesTurno', max_length=50, blank=True, null=True)  # Field name made lowercase.
    caja = models.CharField(db_column='Caja', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cajero = models.CharField(db_column='Cajero', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fechainicio = models.DateTimeField(db_column='FechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='FechaFin', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=20, blank=True, null=True)  # Field name made lowercase.
    folioini = models.IntegerField(db_column='FolioIni', blank=True, null=True)  # Field name made lowercase.
    foliofin = models.IntegerField(db_column='FolioFin', blank=True, null=True)  # Field name made lowercase.
    tickets = models.IntegerField(db_column='Tickets', blank=True, null=True)  # Field name made lowercase.
    vtaefectivo = models.DecimalField(db_column='VtaEfectivo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vtacheque = models.DecimalField(db_column='vtaCheque', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vtatransferencias = models.DecimalField(db_column='vtaTransferencias', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vtatarjetas = models.DecimalField(db_column='Vtatarjetas', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalvta = models.DecimalField(db_column='TotalVta', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cancelaciones = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    vtaneta = models.DecimalField(db_column='VtaNeta', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalret = models.DecimalField(db_column='TotalRet', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    difventa = models.DecimalField(db_column='DifVenta', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ticketefec = models.IntegerField(db_column='TicketEfec', blank=True, null=True)  # Field name made lowercase.
    ticketche = models.IntegerField(db_column='TicketChe', blank=True, null=True)  # Field name made lowercase.
    tickettrans = models.IntegerField(db_column='TicketTrans', blank=True, null=True)  # Field name made lowercase.
    tickettarje = models.IntegerField(db_column='TicketTarje', blank=True, null=True)  # Field name made lowercase.
    tickettotal = models.IntegerField(db_column='TicketTotal', blank=True, null=True)  # Field name made lowercase.
    ticketcan = models.IntegerField(db_column='TicketCan', blank=True, null=True)  # Field name made lowercase.
    ticketnetos = models.IntegerField(db_column='TicketNetos', blank=True, null=True)  # Field name made lowercase.
    ticketretiros = models.IntegerField(db_column='TicketRetiros', blank=True, null=True)  # Field name made lowercase.
    base0 = models.DecimalField(db_column='Base0', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base16 = models.DecimalField(db_column='Base16', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    baseieps1 = models.DecimalField(db_column='Baseieps1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    baseieps2 = models.DecimalField(db_column='Baseieps2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    baseieps3 = models.DecimalField(db_column='Baseieps3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    baseieps4 = models.DecimalField(db_column='Baseieps4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porciva = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    porcieps1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    porcieps2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    porcieps3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    porcieps4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impiva = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impieps1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impieps2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impieps3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impieps4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cerrado = models.BooleanField(blank=True, null=True)
    usercerro = models.CharField(max_length=20, blank=True, null=True)
    fechacerro = models.DateTimeField(blank=True, null=True)
    contabilizado = models.BooleanField(blank=True, null=True)
    userconta = models.CharField(max_length=20, blank=True, null=True)
    fechaconta = models.DateTimeField(blank=True, null=True)
    ingbancos = models.BooleanField(db_column='IngBancos', blank=True, null=True)  # Field name made lowercase.
    useringbanco = models.CharField(max_length=20, blank=True, null=True)
    fechaingbanco = models.DateTimeField(blank=True, null=True)
    empresa = models.IntegerField(blank=True, null=True)
    nomequipo = models.CharField(max_length=50, blank=True, null=True)
    timbrado = models.BooleanField(blank=True, null=True)
    uuid = models.CharField(max_length=50, blank=True, null=True)
    fecha_timbrado = models.DateTimeField(blank=True, null=True)
    seriefac = models.CharField(max_length=10, blank=True, null=True)
    foliofac = models.IntegerField(blank=True, null=True)
    impfacturado = models.DecimalField(max_digits=18, decimal_places=10)
    impnf = models.DecimalField(max_digits=18, decimal_places=10)
    base0nf = models.DecimalField(max_digits=18, decimal_places=10)
    base16nf = models.DecimalField(max_digits=18, decimal_places=10)
    base8nf = models.DecimalField(max_digits=18, decimal_places=10)
    base265nf = models.DecimalField(max_digits=18, decimal_places=10)
    base53nf = models.DecimalField(max_digits=18, decimal_places=10)
    ivanf = models.DecimalField(max_digits=18, decimal_places=10)
    ieps8nf = models.DecimalField(max_digits=18, decimal_places=10)
    ieps265nf = models.DecimalField(max_digits=18, decimal_places=10)
    ieps53nf = models.DecimalField(max_digits=18, decimal_places=10)
    subtotalc = models.DecimalField(max_digits=18, decimal_places=10)
    subtotalnf = models.DecimalField(max_digits=18, decimal_places=10)
    baseieps03 = models.DecimalField(max_digits=18, decimal_places=10)
    baseieps06 = models.DecimalField(max_digits=18, decimal_places=10)
    baseieps25 = models.DecimalField(max_digits=18, decimal_places=10)
    baseieps30 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps03 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps06 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps25 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps30 = models.DecimalField(max_digits=18, decimal_places=10)

    class Meta:
        managed = False
        db_table = 'CierresTurno'


class Clientes(models.Model):
    cvecli = models.IntegerField()
    nomcliente = models.CharField(max_length=200)
    direccioncli = models.CharField(max_length=150)
    rfc = models.CharField(max_length=30)
    colonia = models.CharField(max_length=100)
    cp = models.CharField(max_length=15)
    numint = models.IntegerField()
    numext = models.IntegerField()
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    delegacion = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)
    fechaalta = models.DateTimeField()
    login = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    moneda = models.CharField(max_length=5)
    metodopago = models.CharField(max_length=5)
    pais = models.CharField(max_length=5)
    relacioncfdi = models.CharField(max_length=5)
    formapago = models.CharField(max_length=5)
    usocfdi = models.CharField(max_length=5)
    cta = models.CharField(max_length=15)
    paisnf = models.CharField(max_length=50)
    index_ruta = models.IntegerField()
    nombre_cliente = models.CharField(max_length=200)
    cuentaconta = models.CharField(max_length=50)
    empresa = models.IntegerField()
    tipoperfis = models.IntegerField()
    lisprecio = models.IntegerField()
    subctaconta = models.CharField(max_length=50)
    fechamod = models.DateTimeField()
    porcincre = models.DecimalField(max_digits=19, decimal_places=4)
    impincre = models.DecimalField(max_digits=19, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'Clientes'


class Controllocal(models.Model):
    cve_contlocal = models.IntegerField(db_column='Cve_ContLocal')  # Field name made lowercase.
    des_controllocal = models.CharField(db_column='Des_ControlLocal', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ControlLocal'


class Controlnegocio(models.Model):
    cve_contnego = models.IntegerField(db_column='Cve_ContNego')  # Field name made lowercase.
    des_contnego = models.CharField(db_column='Des_ContNego', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ControlNegocio'


class Detmovtos(models.Model):
    cvebod = models.IntegerField(db_column='CveBod')  # Field name made lowercase.
    folmov = models.IntegerField(db_column='FolMov')  # Field name made lowercase.
    cvemov = models.IntegerField(db_column='CveMov')  # Field name made lowercase.
    sermov = models.CharField(db_column='SerMov', max_length=10)  # Field name made lowercase.
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    cveprod = models.CharField(db_column='CveProd', max_length=20)  # Field name made lowercase.
    cant = models.DecimalField(db_column='Cant', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre = models.IntegerField(db_column='LisPre')  # Field name made lowercase.
    porcdesc = models.DecimalField(db_column='PorcDesc', max_digits=19, decimal_places=4)  # Field name made lowercase.
    preuni = models.DecimalField(db_column='PreUni', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impsub = models.DecimalField(db_column='ImpSub', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porciva = models.DecimalField(db_column='PorcIva', max_digits=18, decimal_places=6)  # Field name made lowercase.
    impiva = models.DecimalField(db_column='ImpIva', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cospro = models.DecimalField(db_column='CosPro', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ultcos = models.DecimalField(db_column='UltCos', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cveprodprov = models.CharField(db_column='CVEPRODPROV', max_length=20)  # Field name made lowercase.
    desprod = models.CharField(db_column='DesProd', max_length=800)  # Field name made lowercase.
    numdias = models.IntegerField(db_column='NumDias')  # Field name made lowercase.
    cantren = models.DecimalField(db_column='CantRen', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantsaldo = models.DecimalField(db_column='CantSaldo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantult = models.DecimalField(db_column='CantUlt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantdev = models.DecimalField(db_column='CantDev', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantdevsaldo = models.DecimalField(db_column='CantDevSaldo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantdevult = models.DecimalField(db_column='CantDevUlt', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fleteprov = models.DecimalField(db_column='FLETEPROV', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcdesc2 = models.DecimalField(db_column='PorcDesc2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcdesc3 = models.DecimalField(db_column='PorcDesc3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcdesc4 = models.DecimalField(db_column='PorcDesc4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcdesc5 = models.DecimalField(db_column='PorcDesc5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcdesc6 = models.DecimalField(db_column='PorcDesc6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    imptotreg = models.DecimalField(db_column='ImpTotReg', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impotros = models.DecimalField(db_column='ImpOtros', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cvecolmad1 = models.CharField(db_column='CveColMad1', max_length=20)  # Field name made lowercase.
    cvecolmad2 = models.CharField(db_column='CveColMad2', max_length=20)  # Field name made lowercase.
    tela1 = models.CharField(db_column='Tela1', max_length=20)  # Field name made lowercase.
    tela2 = models.CharField(db_column='Tela2', max_length=20)  # Field name made lowercase.
    tela3 = models.CharField(db_column='Tela3', max_length=20)  # Field name made lowercase.
    tela4 = models.CharField(db_column='Tela4', max_length=20)  # Field name made lowercase.
    tela5 = models.CharField(db_column='Tela5', max_length=20)  # Field name made lowercase.
    observa = models.CharField(db_column='Observa', max_length=255)  # Field name made lowercase.
    cvecolmad3 = models.CharField(db_column='CveColMad3', max_length=20)  # Field name made lowercase.
    tela6 = models.CharField(db_column='Tela6', max_length=20)  # Field name made lowercase.
    idref = models.IntegerField(db_column='IdRef')  # Field name made lowercase.
    preunidesc = models.DecimalField(db_column='PreUniDesc', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadiccolmad1 = models.DecimalField(db_column='ImpAdicColMad1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadiccolmad2 = models.DecimalField(db_column='ImpAdicColMad2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadiccolmad3 = models.DecimalField(db_column='ImpAdicColMad3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadictela1 = models.DecimalField(db_column='ImpAdicTela1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadictela2 = models.DecimalField(db_column='ImpAdicTela2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadictela3 = models.DecimalField(db_column='ImpAdicTela3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadictela4 = models.DecimalField(db_column='ImpAdicTela4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadictela5 = models.DecimalField(db_column='ImpAdicTela5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadictela6 = models.DecimalField(db_column='ImpAdicTela6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desctotela1 = models.DecimalField(db_column='DesctoTela1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desctotela2 = models.DecimalField(db_column='DesctoTela2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desctotela3 = models.DecimalField(db_column='DesctoTela3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desctotela4 = models.DecimalField(db_column='DesctoTela4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desctotela5 = models.DecimalField(db_column='DesctoTela5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desctotela6 = models.DecimalField(db_column='DesctoTela6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cveprodcli = models.CharField(db_column='CveProdCli', max_length=20)  # Field name made lowercase.
    entregadotienda = models.BooleanField(db_column='EntregadoTienda')  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=50)  # Field name made lowercase.
    cvedoc = models.IntegerField(db_column='CveDoc')  # Field name made lowercase.
    numreceta = models.CharField(db_column='NumReceta', max_length=50)  # Field name made lowercase.
    observareceta = models.CharField(db_column='ObservaReceta', max_length=200)  # Field name made lowercase.
    porcieps = models.DecimalField(db_column='PorcIEPS', max_digits=18, decimal_places=6)  # Field name made lowercase.
    ieps = models.DecimalField(db_column='IEPS', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcivaret = models.DecimalField(db_column='PorcIVARet', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impivaret = models.DecimalField(db_column='ImpIVARet', max_digits=19, decimal_places=4)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa')  # Field name made lowercase.
    preciovta = models.DecimalField(db_column='PrecioVta', max_digits=19, decimal_places=4)  # Field name made lowercase.
    totalprod = models.DecimalField(db_column='Totalprod', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechamov = models.DateTimeField()
    porceieps2 = models.DecimalField(db_column='PorceIEPS2', max_digits=18, decimal_places=6)  # Field name made lowercase.
    impieps2 = models.DecimalField(db_column='ImpIEPS2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porceieps3 = models.DecimalField(db_column='PorceIEPS3', max_digits=18, decimal_places=6)  # Field name made lowercase.
    impieps3 = models.DecimalField(db_column='ImpIEPS3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porceieps4 = models.DecimalField(db_column='PorceIEPS4', max_digits=18, decimal_places=6)  # Field name made lowercase.
    impieps4 = models.DecimalField(db_column='ImpIEPS4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    baseiva0 = models.DecimalField(db_column='Baseiva0', max_digits=19, decimal_places=4)  # Field name made lowercase.
    baseiva16 = models.DecimalField(db_column='Baseiva16', max_digits=19, decimal_places=4)  # Field name made lowercase.
    baseieps1 = models.DecimalField(db_column='Baseieps1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    baseieps2 = models.DecimalField(db_column='Baseieps2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    baseieps3 = models.DecimalField(db_column='Baseieps3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    baseieps4 = models.DecimalField(db_column='Baseieps4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cveuni = models.IntegerField()
    flete = models.DecimalField(max_digits=19, decimal_places=4)
    impdesc1 = models.DecimalField(max_digits=19, decimal_places=4)
    impdesc2 = models.DecimalField(max_digits=19, decimal_places=4)
    impdesc3 = models.DecimalField(max_digits=19, decimal_places=4)
    costoneto = models.DecimalField(max_digits=19, decimal_places=4)
    paq = models.BooleanField()
    ocosto = models.DecimalField(max_digits=19, decimal_places=4)
    cvemovprod = models.IntegerField()
    desmovprod = models.CharField(max_length=50)
    turno = models.IntegerField()
    sercierre = models.CharField(max_length=10)
    folcierre = models.IntegerField()
    cierreturno = models.BooleanField()
    cierredia = models.BooleanField()
    transaccion = models.CharField(db_column='Transaccion', max_length=50)  # Field name made lowercase.
    tipomov = models.IntegerField()
    caja = models.IntegerField()
    cveimptoiva = models.CharField(max_length=3)
    cveimptoieps = models.CharField(max_length=3)
    tasa = models.CharField(max_length=4)
    numref = models.CharField(max_length=50)
    transmitida = models.BooleanField()
    cancelado = models.BooleanField()
    facturado = models.BooleanField()
    login = models.CharField(max_length=20)
    cvetipmovvta = models.IntegerField()
    factura = models.BooleanField()
    porceieps5 = models.DecimalField(db_column='PorceIEPS5', max_digits=18, decimal_places=6)  # Field name made lowercase.
    impieps5 = models.DecimalField(db_column='ImpIEPS5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    baseieps5 = models.DecimalField(db_column='Baseieps5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porceieps6 = models.DecimalField(db_column='PorceIEPS6', max_digits=18, decimal_places=6)  # Field name made lowercase.
    impieps6 = models.DecimalField(db_column='ImpIEPS6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    baseieps6 = models.DecimalField(db_column='Baseieps6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porceieps7 = models.DecimalField(db_column='PorceIEPS7', max_digits=18, decimal_places=6)  # Field name made lowercase.
    impieps7 = models.DecimalField(db_column='ImpIEPS7', max_digits=19, decimal_places=4)  # Field name made lowercase.
    baseieps7 = models.DecimalField(db_column='Baseieps7', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porceieps8 = models.DecimalField(db_column='PorceIEPS8', max_digits=18, decimal_places=6)  # Field name made lowercase.
    impieps8 = models.DecimalField(db_column='ImpIEPS8', max_digits=19, decimal_places=4)  # Field name made lowercase.
    baseieps8 = models.DecimalField(db_column='Baseieps8', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DETMOVTOS'


class Detmovtosr(models.Model):
    cvebod = models.IntegerField(db_column='CveBod', blank=True, null=True)  # Field name made lowercase.
    folmov = models.IntegerField(db_column='FolMov', blank=True, null=True)  # Field name made lowercase.
    cvemov = models.IntegerField(db_column='CveMov', blank=True, null=True)  # Field name made lowercase.
    sermov = models.CharField(db_column='SerMov', max_length=5, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    cveprod = models.CharField(db_column='CveProd', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cant = models.DecimalField(db_column='Cant', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lispre = models.IntegerField(db_column='LisPre', blank=True, null=True)  # Field name made lowercase.
    porcdesc = models.DecimalField(db_column='PorcDesc', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    preuni = models.DecimalField(db_column='PreUni', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impsub = models.DecimalField(db_column='ImpSub', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porciva = models.DecimalField(db_column='PorcIva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impiva = models.DecimalField(db_column='ImpIva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cospro = models.DecimalField(db_column='CosPro', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ultcos = models.DecimalField(db_column='UltCos', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cveprodprov = models.CharField(db_column='CVEPRODPROV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    desprod = models.CharField(db_column='DesProd', max_length=800, blank=True, null=True)  # Field name made lowercase.
    numdias = models.IntegerField(db_column='NumDias', blank=True, null=True)  # Field name made lowercase.
    cantren = models.DecimalField(db_column='CantRen', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantsaldo = models.DecimalField(db_column='CantSaldo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantult = models.DecimalField(db_column='CantUlt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantdev = models.DecimalField(db_column='CantDev', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantdevsaldo = models.DecimalField(db_column='CantDevSaldo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantdevult = models.DecimalField(db_column='CantDevUlt', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fleteprov = models.DecimalField(db_column='FLETEPROV', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcdesc2 = models.DecimalField(db_column='PorcDesc2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcdesc3 = models.DecimalField(db_column='PorcDesc3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcdesc4 = models.DecimalField(db_column='PorcDesc4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcdesc5 = models.DecimalField(db_column='PorcDesc5', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcdesc6 = models.DecimalField(db_column='PorcDesc6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imptotreg = models.DecimalField(db_column='ImpTotReg', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impotros = models.DecimalField(db_column='ImpOtros', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cvecolmad1 = models.CharField(db_column='CveColMad1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cvecolmad2 = models.CharField(db_column='CveColMad2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tela1 = models.CharField(db_column='Tela1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tela2 = models.CharField(db_column='Tela2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tela3 = models.CharField(db_column='Tela3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tela4 = models.CharField(db_column='Tela4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tela5 = models.CharField(db_column='Tela5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    observa = models.CharField(db_column='Observa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cvecolmad3 = models.CharField(db_column='CveColMad3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tela6 = models.CharField(db_column='Tela6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idref = models.IntegerField(db_column='IdRef', blank=True, null=True)  # Field name made lowercase.
    preunidesc = models.DecimalField(db_column='PreUniDesc', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impadiccolmad1 = models.DecimalField(db_column='ImpAdicColMad1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impadiccolmad2 = models.DecimalField(db_column='ImpAdicColMad2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impadiccolmad3 = models.DecimalField(db_column='ImpAdicColMad3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impadictela1 = models.DecimalField(db_column='ImpAdicTela1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impadictela2 = models.DecimalField(db_column='ImpAdicTela2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impadictela3 = models.DecimalField(db_column='ImpAdicTela3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impadictela4 = models.DecimalField(db_column='ImpAdicTela4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impadictela5 = models.DecimalField(db_column='ImpAdicTela5', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impadictela6 = models.DecimalField(db_column='ImpAdicTela6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    desctotela1 = models.DecimalField(db_column='DesctoTela1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    desctotela2 = models.DecimalField(db_column='DesctoTela2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    desctotela3 = models.DecimalField(db_column='DesctoTela3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    desctotela4 = models.DecimalField(db_column='DesctoTela4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    desctotela5 = models.DecimalField(db_column='DesctoTela5', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    desctotela6 = models.DecimalField(db_column='DesctoTela6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cveprodcli = models.CharField(db_column='CveProdCli', max_length=20, blank=True, null=True)  # Field name made lowercase.
    entregadotienda = models.BooleanField(db_column='EntregadoTienda', blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cvedoc = models.IntegerField(db_column='CveDoc', blank=True, null=True)  # Field name made lowercase.
    numreceta = models.CharField(db_column='NumReceta', max_length=50, blank=True, null=True)  # Field name made lowercase.
    observareceta = models.CharField(db_column='ObservaReceta', max_length=200, blank=True, null=True)  # Field name made lowercase.
    porcieps = models.DecimalField(db_column='PorcIEPS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ieps = models.DecimalField(db_column='IEPS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcivaret = models.DecimalField(db_column='PorcIVARet', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impivaret = models.DecimalField(db_column='ImpIVARet', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    preciovta = models.DecimalField(db_column='PrecioVta', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalprod = models.DecimalField(db_column='Totalprod', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fechamov = models.DateTimeField(blank=True, null=True)
    porceieps2 = models.DecimalField(db_column='PorceIEPS2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impieps2 = models.DecimalField(db_column='ImpIEPS2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porceieps3 = models.DecimalField(db_column='PorceIEPS3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impieps3 = models.DecimalField(db_column='ImpIEPS3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porceieps4 = models.DecimalField(db_column='PorceIEPS4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impieps4 = models.DecimalField(db_column='ImpIEPS4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    baseiva0 = models.DecimalField(db_column='Baseiva0', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    baseiva16 = models.DecimalField(db_column='Baseiva16', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    baseieps1 = models.DecimalField(db_column='Baseieps1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    baseieps2 = models.DecimalField(db_column='Baseieps2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    baseieps3 = models.DecimalField(db_column='Baseieps3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    baseieps4 = models.DecimalField(db_column='Baseieps4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cveuni = models.IntegerField(blank=True, null=True)
    flete = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impdesc1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impdesc2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impdesc3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    costoneto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    paq = models.BooleanField(blank=True, null=True)
    ocosto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cvemovprod = models.IntegerField(blank=True, null=True)
    desmovprod = models.CharField(max_length=50, blank=True, null=True)
    turno = models.IntegerField(blank=True, null=True)
    sercierre = models.CharField(max_length=10, blank=True, null=True)
    folcierre = models.IntegerField(blank=True, null=True)
    cierreturno = models.BooleanField(blank=True, null=True)
    cierredia = models.BooleanField(blank=True, null=True)
    transaccion = models.CharField(max_length=50, blank=True, null=True)
    tipomov = models.IntegerField(blank=True, null=True)
    caja = models.IntegerField(blank=True, null=True)
    cveimptoiva = models.CharField(max_length=3, blank=True, null=True)
    cveimptoieps = models.CharField(max_length=3, blank=True, null=True)
    tasa = models.CharField(max_length=4, blank=True, null=True)
    numref = models.CharField(max_length=50, blank=True, null=True)
    transmitida = models.BooleanField(blank=True, null=True)
    cancelado = models.BooleanField(blank=True, null=True)
    facturado = models.BooleanField(blank=True, null=True)
    login = models.CharField(max_length=20, blank=True, null=True)
    cvetipmovvta = models.IntegerField(blank=True, null=True)
    factura = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DETMOVTOSR'


class Detpagosprog(models.Model):
    cvebod = models.IntegerField(db_column='CVEBOD')  # Field name made lowercase.
    cveprov = models.IntegerField(db_column='CVEPROV')  # Field name made lowercase.
    cvemov = models.IntegerField(db_column='CVEMOV')  # Field name made lowercase.
    sermov = models.CharField(db_column='SERMOV', max_length=2)  # Field name made lowercase.
    folmov = models.IntegerField(db_column='FOLMOV')  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    cvetpgo = models.IntegerField(db_column='CVETPGO')  # Field name made lowercase.
    fecvenc = models.DateTimeField(db_column='FECVENC')  # Field name made lowercase.
    imptot = models.DecimalField(db_column='IMPTOT', max_digits=19, decimal_places=4)  # Field name made lowercase.
    imppag = models.DecimalField(db_column='IMPPAG', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fecpag = models.DateTimeField(db_column='FECPAG')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DETPAGOSPROG'


class Detpedidos(models.Model):
    folped = models.IntegerField(db_column='FOLPED')  # Field name made lowercase.
    cveped = models.SmallIntegerField(db_column='CVEPED')  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    cveprod = models.CharField(db_column='CVEPROD', max_length=20)  # Field name made lowercase.
    cant = models.DecimalField(db_column='CANT', max_digits=19, decimal_places=4)  # Field name made lowercase.
    lispre = models.IntegerField(db_column='LISPRE')  # Field name made lowercase.
    porcdesc = models.DecimalField(db_column='PORCDESC', max_digits=19, decimal_places=4)  # Field name made lowercase.
    preuni = models.DecimalField(db_column='PREUNI', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impsub = models.DecimalField(db_column='IMPSUB', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porciva = models.DecimalField(db_column='PORCIVA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impiva = models.DecimalField(db_column='IMPIVA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desprod = models.CharField(db_column='DESPROD', max_length=800)  # Field name made lowercase.
    cveprodprov = models.CharField(db_column='CVEPRODPROV', max_length=20)  # Field name made lowercase.
    numdias = models.IntegerField(db_column='NumDias')  # Field name made lowercase.
    porcdesc2 = models.DecimalField(db_column='PorcDesc2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcdesc3 = models.DecimalField(db_column='PorcDesc3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcdesc4 = models.DecimalField(db_column='PorcDesc4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcdesc5 = models.DecimalField(db_column='PorcDesc5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcdesc6 = models.DecimalField(db_column='PorcDesc6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cvecolmad1 = models.CharField(db_column='CveColMad1', max_length=20)  # Field name made lowercase.
    cvecolmad2 = models.CharField(db_column='CveColMad2', max_length=20)  # Field name made lowercase.
    tela1 = models.CharField(db_column='Tela1', max_length=20)  # Field name made lowercase.
    tela2 = models.CharField(db_column='Tela2', max_length=20)  # Field name made lowercase.
    tela3 = models.CharField(db_column='Tela3', max_length=20)  # Field name made lowercase.
    tela4 = models.CharField(db_column='Tela4', max_length=20)  # Field name made lowercase.
    tela5 = models.CharField(db_column='Tela5', max_length=20)  # Field name made lowercase.
    observa = models.CharField(db_column='Observa', max_length=255)  # Field name made lowercase.
    cvecolmad3 = models.CharField(db_column='CveColMad3', max_length=20)  # Field name made lowercase.
    tela6 = models.CharField(db_column='Tela6', max_length=20)  # Field name made lowercase.
    idref = models.IntegerField(db_column='IdRef')  # Field name made lowercase.
    preunidesc = models.DecimalField(db_column='PreUniDesc', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadiccolmad1 = models.DecimalField(db_column='ImpAdicColMad1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadiccolmad2 = models.DecimalField(db_column='ImpAdicColMad2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadiccolmad3 = models.DecimalField(db_column='ImpAdicColMad3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadictela1 = models.DecimalField(db_column='ImpAdicTela1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadictela2 = models.DecimalField(db_column='ImpAdicTela2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadictela3 = models.DecimalField(db_column='ImpAdicTela3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadictela4 = models.DecimalField(db_column='ImpAdicTela4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadictela5 = models.DecimalField(db_column='ImpAdicTela5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impadictela6 = models.DecimalField(db_column='ImpAdicTela6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desctotela1 = models.DecimalField(db_column='DesctoTela1', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desctotela2 = models.DecimalField(db_column='DesctoTela2', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desctotela3 = models.DecimalField(db_column='DesctoTela3', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desctotela4 = models.DecimalField(db_column='DesctoTela4', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desctotela5 = models.DecimalField(db_column='DesctoTela5', max_digits=19, decimal_places=4)  # Field name made lowercase.
    desctotela6 = models.DecimalField(db_column='DesctoTela6', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cveprodcli = models.CharField(db_column='CveProdCli', max_length=20)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=50)  # Field name made lowercase.
    porcieps = models.DecimalField(db_column='PorcIEPS', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ieps = models.DecimalField(db_column='IEPS', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcivaret = models.DecimalField(db_column='PorcIVARet', max_digits=19, decimal_places=4)  # Field name made lowercase.
    impivaret = models.DecimalField(db_column='ImpIVARet', max_digits=19, decimal_places=4)  # Field name made lowercase.
    nomproy = models.CharField(db_column='NomProy', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DETPEDIDOS'


class Detprodpaq(models.Model):
    cvepaq = models.CharField(db_column='CVEPAQ', max_length=20)  # Field name made lowercase.
    cveprod = models.CharField(db_column='CVEPROD', max_length=20)  # Field name made lowercase.
    cant = models.DecimalField(db_column='CANT', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcpaq = models.DecimalField(db_column='PORCPAQ', max_digits=19, decimal_places=4)  # Field name made lowercase.
    activo = models.BooleanField()
    numref = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'DETPRODPAQ'


class Detprodpaq2(models.Model):
    cvepaq = models.CharField(db_column='CVEPAQ', max_length=20)  # Field name made lowercase.
    cveprod = models.CharField(db_column='CVEPROD', max_length=20)  # Field name made lowercase.
    cant = models.DecimalField(db_column='CANT', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcpaq = models.DecimalField(db_column='PORCPAQ', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DETPRODPAQ2'


class Detprodprov(models.Model):
    cveprod = models.CharField(db_column='CVEPROD', max_length=20)  # Field name made lowercase.
    cveprov = models.IntegerField(db_column='CVEPROV')  # Field name made lowercase.
    porcdesc = models.DecimalField(db_column='PORCDESC', max_digits=19, decimal_places=4)  # Field name made lowercase.
    flete = models.DecimalField(db_column='FLETE', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DETPRODPROV'


class Detprodpun(models.Model):
    cveprod = models.CharField(db_column='CVEPROD', max_length=20)  # Field name made lowercase.
    cvepun = models.IntegerField(db_column='CVEPUN')  # Field name made lowercase.
    cant = models.DecimalField(db_column='CANT', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DETPRODPUN'


class Datostemp(models.Model):
    referencia = models.CharField(max_length=50)
    codbar = models.CharField(max_length=25)
    codsat = models.CharField(max_length=25)
    desprod = models.CharField(max_length=100)
    cospro = models.DecimalField(max_digits=19, decimal_places=4)
    ultcos = models.DecimalField(max_digits=19, decimal_places=4)
    preciovta = models.DecimalField(max_digits=19, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'DatosTemp'


class Detfacturas(models.Model):
    cvebod = models.IntegerField(blank=True, null=True)
    seriefac = models.CharField(db_column='Seriefac', max_length=5, blank=True, null=True)  # Field name made lowercase.
    foliofac = models.IntegerField(db_column='Foliofac', blank=True, null=True)  # Field name made lowercase.
    cveprodserv = models.IntegerField(db_column='cveprodServ', blank=True, null=True)  # Field name made lowercase.
    cveprod = models.CharField(max_length=15, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    cveuni = models.CharField(max_length=20, blank=True, null=True)
    desuni = models.CharField(max_length=20, blank=True, null=True)
    desprod = models.CharField(max_length=180, blank=True, null=True)
    preuni = models.DecimalField(db_column='Preuni', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cveimp = models.CharField(max_length=10, blank=True, null=True)
    desimp = models.CharField(max_length=10, blank=True, null=True)
    impiva = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impieps = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impsub = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fdia = models.IntegerField(blank=True, null=True)
    base8 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps8 = models.DecimalField(max_digits=18, decimal_places=10)
    base265 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps265 = models.DecimalField(max_digits=18, decimal_places=10)
    base53 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps53 = models.DecimalField(max_digits=18, decimal_places=10)
    base3 = models.DecimalField(max_digits=18, decimal_places=10)
    base6 = models.DecimalField(max_digits=18, decimal_places=10)
    base25 = models.DecimalField(max_digits=18, decimal_places=10)
    base30 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps3 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps6 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps25 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps30 = models.DecimalField(max_digits=18, decimal_places=10)

    class Meta:
        managed = False
        db_table = 'DetFacturas'


class Detgrupoemp(models.Model):
    cvegrupoemp = models.IntegerField()
    cveemprea = models.IntegerField()
    nomempresa = models.CharField(max_length=100)
    servidorr = models.CharField(max_length=50)
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'DetGrupoemp'


class Detimportes(models.Model):
    serie = models.CharField(max_length=10)
    folio = models.IntegerField(db_column='Folio')  # Field name made lowercase.
    cveprod = models.CharField(max_length=50)
    desprod = models.CharField(max_length=400)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=19, decimal_places=4)
    importe = models.DecimalField(max_digits=19, decimal_places=4)
    fechagenera = models.DateTimeField()
    usuario = models.CharField(max_length=20)
    cancelado = models.BooleanField()
    fechacancela = models.DateTimeField()
    usercancela = models.CharField(max_length=20)
    fechavigencia = models.DateField()
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'DetImportes'


class Detpromo(models.Model):
    empresa = models.IntegerField()
    cvepromo = models.IntegerField()
    cvegruposuc = models.IntegerField()
    cvegrupoprod = models.IntegerField()
    tipopromo = models.IntegerField(db_column='tipoPromo')  # Field name made lowercase.
    activa = models.BooleanField()
    cveprod = models.CharField(max_length=20)
    despromo = models.CharField(max_length=800)
    venta = models.IntegerField()
    regalo = models.IntegerField()
    numero_piezas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'DetPromo'


class Detpromociones(models.Model):
    cveprod = models.CharField(max_length=50)
    cvetippromo = models.IntegerField()
    cvetipcompromo = models.IntegerField()
    cvedefinepromo = models.IntegerField()
    cantprod = models.IntegerField()
    cvegpoprod = models.IntegerField()
    cantregala = models.IntegerField()
    gporegala = models.IntegerField()
    prefijasi = models.DecimalField(max_digits=19, decimal_places=4)
    prefijaci = models.DecimalField(max_digits=19, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'DetPromociones'


class Detallepagosprov(models.Model):
    cveprov = models.IntegerField()
    folmov = models.IntegerField(db_column='Folmov')  # Field name made lowercase.
    cvemov = models.IntegerField()
    numdoc = models.CharField(db_column='NumDoc', max_length=50)  # Field name made lowercase.
    fechapago = models.DateField()
    monto = models.DecimalField(max_digits=19, decimal_places=4)
    observacion = models.CharField(max_length=50)
    login = models.CharField(max_length=15)
    fechacreacion = models.DateTimeField()
    empresa = models.IntegerField()
    almacen = models.IntegerField()
    pagado = models.BooleanField()
    folpago = models.IntegerField()
    numdocpag = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'DetallePagosProv'


class Detallerecargas(models.Model):
    id = models.IntegerField()
    fechahora_recarga = models.DateTimeField(blank=True, null=True)
    compañia = models.CharField(max_length=40, blank=True, null=True)
    tipo_recarga = models.CharField(max_length=30, blank=True, null=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    monto = models.CharField(max_length=10, blank=True, null=True)
    utilidad = models.CharField(max_length=20, blank=True, null=True)
    autorizacion = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    comentarios = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=30, blank=True, null=True)
    puntoacceso = models.CharField(max_length=50, blank=True, null=True)
    rcode = models.CharField(max_length=30, blank=True, null=True)
    exitosa = models.CharField(max_length=20, blank=True, null=True)
    fechacorta = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DetalleRecargas'


class Detescalables(models.Model):
    folioescala = models.IntegerField()
    desescala = models.CharField(max_length=80)
    gpoemp = models.IntegerField()
    gpoprod = models.IntegerField()
    cveprod = models.CharField(max_length=20)
    desprod = models.CharField(max_length=800)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=19, decimal_places=4)
    caducidad = models.BooleanField()
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()
    vigente = models.BooleanField()
    enviado = models.BooleanField()
    fechaenvio = models.DateTimeField()
    userenvio = models.CharField(max_length=50)
    feccrea = models.DateTimeField()
    fecmod = models.DateTimeField()
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Detescalables'


class Detescalables1(models.Model):
    folioescala = models.IntegerField()
    desescala = models.CharField(max_length=80)
    gpoemp = models.IntegerField()
    gpoprod = models.IntegerField()
    cveprod = models.CharField(max_length=20)
    desprod = models.CharField(max_length=800)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=19, decimal_places=4)
    caducidad = models.BooleanField()
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()
    vigente = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Detescalables1'


class Detescalablesa(models.Model):
    folioescala = models.IntegerField()
    desescala = models.CharField(max_length=80)
    gpoemp = models.IntegerField()
    gpoprod = models.IntegerField()
    cveprod = models.CharField(max_length=20)
    desprod = models.CharField(max_length=800)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=19, decimal_places=4)
    caducidad = models.BooleanField()
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()
    vigente = models.BooleanField()
    enviado = models.BooleanField()
    fechaenvio = models.DateTimeField()
    userenvio = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'DetescalablesA'


class Detescalablesb(models.Model):
    folioescala = models.IntegerField()
    desescala = models.CharField(max_length=80)
    gpoemp = models.IntegerField()
    gpoprod = models.IntegerField()
    cveprod = models.CharField(max_length=20)
    desprod = models.CharField(max_length=800)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=19, decimal_places=4)
    caducidad = models.BooleanField()
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()
    vigente = models.BooleanField()
    enviado = models.BooleanField()
    fechaenvio = models.DateTimeField()
    userenvio = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'DetescalablesB'


class Detgruposproductos(models.Model):
    foliogrupo = models.IntegerField()
    cveprod = models.CharField(max_length=20)
    desprod = models.CharField(max_length=800)
    cantidad = models.IntegerField()
    fecha_creacion = models.DateTimeField()
    empresa = models.IntegerField()
    enviado = models.BooleanField()
    fechaenvio = models.DateTimeField()
    userenvio = models.CharField(max_length=50)
    fecmod = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Detgruposproductos'


class Detgruposproductos1(models.Model):
    foliogrupo = models.IntegerField()
    cveprod = models.CharField(max_length=20)
    desprod = models.CharField(max_length=800)
    cantidad = models.IntegerField()
    fecha_creacion = models.DateTimeField()
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Detgruposproductos1'


class Detgruposproductosa(models.Model):
    foliogrupo = models.IntegerField()
    cveprod = models.CharField(max_length=20)
    desprod = models.CharField(max_length=800)
    cantidad = models.IntegerField()
    fecha_creacion = models.DateTimeField()
    empresa = models.IntegerField()
    enviado = models.BooleanField()
    fechaenvio = models.DateTimeField()
    userenvio = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'DetgruposproductosA'


class Detmovmueble(models.Model):
    empresa = models.IntegerField(db_column='Empresa')  # Field name made lowercase.
    seriemov = models.CharField(max_length=3)
    foliomov = models.IntegerField()
    tipomov = models.IntegerField()
    index_rut = models.IntegerField()
    codigo_mueble = models.IntegerField()
    desc_mueble = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    activo = models.BooleanField()
    cancelado = models.BooleanField()
    comodatado = models.BooleanField()
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    serie = models.CharField(max_length=30)
    consecutivo = models.CharField(max_length=15)
    codigoe_enfriador = models.CharField(max_length=15)
    entregado = models.BooleanField(db_column='Entregado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Detmovmueble'


class Existe(models.Model):
    cveprod = models.CharField(db_column='CVEPROD', max_length=20)  # Field name made lowercase.
    cvebod = models.IntegerField(db_column='CVEBOD')  # Field name made lowercase.
    existe = models.DecimalField(db_column='EXISTE', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fecinv = models.DateTimeField(db_column='FECINV')  # Field name made lowercase.
    ultcos = models.DecimalField(db_column='ULTCOS', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cospro = models.DecimalField(db_column='COSPRO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    exifis = models.DecimalField(db_column='EXIFIS', max_digits=19, decimal_places=4)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='EMPRESA')  # Field name made lowercase.
    corregida = models.IntegerField()
    referencia = models.CharField(max_length=50)
    referencia2 = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'EXISTE'


class Existecomer(models.Model):
    cveprod = models.CharField(db_column='CVEPROD', max_length=20)  # Field name made lowercase.
    cvebod = models.IntegerField(db_column='CVEBOD')  # Field name made lowercase.
    existe = models.DecimalField(db_column='EXISTE', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fecinv = models.DateTimeField(db_column='FECINV')  # Field name made lowercase.
    ultcos = models.DecimalField(db_column='ULTCOS', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cospro = models.DecimalField(db_column='COSPRO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    exifis = models.DecimalField(db_column='EXIFIS', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EXISTECOMER'


class Empleados(models.Model):
    numero_empleado = models.IntegerField()
    ctrolant = models.IntegerField(blank=True, null=True)
    nombre_empleado = models.CharField(max_length=50, blank=True, null=True)
    tipocontrato = models.CharField(max_length=1, blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    numeroseguro = models.CharField(max_length=15, blank=True, null=True)
    reg_patr = models.CharField(max_length=18, blank=True, null=True)
    curp_empleado = models.CharField(max_length=18, blank=True, null=True)
    rfc_empleado = models.CharField(max_length=15, blank=True, null=True)
    clave_depto = models.CharField(max_length=3, blank=True, null=True)
    clave_puesto = models.IntegerField(blank=True, null=True)
    fecha_baja = models.CharField(max_length=10, blank=True, null=True)
    direccion_empleado = models.CharField(max_length=150, blank=True, null=True)
    colonia_empleado = models.CharField(max_length=70, blank=True, null=True)
    ciudad_empleado = models.CharField(max_length=70, blank=True, null=True)
    telefono_empleado = models.CharField(max_length=20, blank=True, null=True)
    celular_empleado = models.CharField(max_length=20, blank=True, null=True)
    audita = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    despacho = models.BooleanField(db_column='Despacho')  # Field name made lowercase.
    socio = models.IntegerField(db_column='Socio')  # Field name made lowercase.
    socio1 = models.IntegerField()
    socio2 = models.IntegerField()
    email = models.CharField(max_length=80)
    fecha_licencia = models.DateTimeField()
    fecha_examen = models.DateTimeField()
    numero_autobus = models.IntegerField()
    recaudacion = models.BooleanField()
    foto_empleado = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Empleados'


class EmpleadosDoctos(models.Model):
    numero_empleado = models.IntegerField()
    clave_docto = models.IntegerField()
    entregado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Empleados_Doctos'


class EmpleadosOtrosdatos(models.Model):
    numero_empleado = models.IntegerField()
    vigencia_licencia = models.DateTimeField(blank=True, null=True)
    dias_vigencia = models.IntegerField(blank=True, null=True)
    numero_autobus = models.CharField(max_length=10, blank=True, null=True)
    clave_socio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Empleados_OtrosDatos'


class EmpleadosDocucaduca(models.Model):
    numero_empleado = models.IntegerField()
    fechahora_movimiento = models.DateTimeField()
    fecha_expira = models.DateTimeField()
    usuario_movimiento = models.IntegerField()
    observacion = models.CharField(max_length=100)
    tipo_docu = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'Empleados_docucaduca'


class EmpleadosMovimientos(models.Model):
    numero_empleado = models.IntegerField()
    fechahora_movimiento = models.DateTimeField()
    fecha_movimiento = models.DateTimeField()
    tipo_movimiento = models.CharField(max_length=1)
    usuario_movimiento = models.IntegerField()
    observaciones = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'Empleados_movimientos'


class Empresa(models.Model):
    empresa = models.IntegerField(db_column='Empresa')  # Field name made lowercase.
    razon_social = models.CharField(db_column='Razon_Social', max_length=100, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    colonia = models.CharField(db_column='Colonia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefonos = models.CharField(db_column='Telefonos', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=50, blank=True, null=True)
    rfc = models.CharField(db_column='RFC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    otros1 = models.CharField(max_length=50, blank=True, null=True)
    otros2 = models.CharField(max_length=50, blank=True, null=True)
    otros3 = models.CharField(max_length=50, blank=True, null=True)
    logo = models.BinaryField(blank=True, null=True)
    rubro = models.FloatField(blank=True, null=True)
    smtp = models.CharField(db_column='SMTP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usuario_smtp = models.CharField(db_column='USUARIO_SMTP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password_smtp = models.CharField(db_column='PASSWORD_SMTP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(max_length=100, blank=True, null=True)
    licencia = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Empresa'


class Empresas(models.Model):
    cvecia = models.IntegerField()
    nomcia = models.CharField(max_length=100)
    activa = models.BooleanField()
    bdcia = models.CharField(max_length=15)
    userbd = models.CharField(max_length=15)
    pwsbd = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Empresas'


class Enfriadores(models.Model):
    id = models.IntegerField()
    cve_inventario = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    serie = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    obsoleto = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Enfriadores'


class Escalable(models.Model):
    folioescala = models.IntegerField()
    desescala = models.CharField(max_length=100)
    gposuc = models.IntegerField()
    dessuc = models.CharField(max_length=100)
    gpoprod = models.IntegerField()
    desgpoprod = models.CharField(max_length=100)
    cantescala = models.IntegerField()
    impescala = models.DecimalField(max_digits=19, decimal_places=4)
    cadescala = models.BooleanField()
    fechaini = models.DateTimeField()
    fechafin = models.DateTimeField()
    vigente = models.BooleanField()
    enviado = models.BooleanField()
    fechaenvio = models.DateTimeField()
    userenvio = models.CharField(max_length=50)
    feccrea = models.DateTimeField()
    fecmod = models.DateTimeField()
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Escalable'


class Escalable1(models.Model):
    folioescala = models.IntegerField()
    desescala = models.CharField(max_length=100)
    gposuc = models.IntegerField()
    dessuc = models.CharField(max_length=100)
    gpoprod = models.IntegerField()
    desgpoprod = models.CharField(max_length=100)
    cantescala = models.IntegerField()
    impescala = models.DecimalField(max_digits=19, decimal_places=4)
    cadescala = models.BooleanField()
    fechaini = models.DateTimeField()
    fechafin = models.DateTimeField()
    vigente = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Escalable1'


class Escalablea(models.Model):
    folioescala = models.IntegerField()
    desescala = models.CharField(max_length=100)
    gposuc = models.IntegerField()
    dessuc = models.CharField(max_length=100)
    gpoprod = models.IntegerField()
    desgpoprod = models.CharField(max_length=100)
    cantescala = models.IntegerField()
    impescala = models.DecimalField(max_digits=19, decimal_places=4)
    cadescala = models.BooleanField()
    fechaini = models.DateTimeField()
    fechafin = models.DateTimeField()
    vigente = models.BooleanField()
    enviado = models.BooleanField()
    fechaenvio = models.DateTimeField()
    userenvio = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'EscalableA'


class Facturas(models.Model):
    empresa = models.IntegerField(blank=True, null=True)
    cvebod = models.IntegerField(blank=True, null=True)
    seriefac = models.CharField(max_length=5, blank=True, null=True)
    foliofac = models.IntegerField(db_column='FolioFac', blank=True, null=True)  # Field name made lowercase.
    cvemov = models.IntegerField(blank=True, null=True)
    cvecli = models.IntegerField(blank=True, null=True)
    cveusuario = models.CharField(max_length=10, blank=True, null=True)
    importesub = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impdesc = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impiva = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    impieps = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    imptotal = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    porciva = models.FloatField(blank=True, null=True)
    porcieps = models.FloatField(blank=True, null=True)
    impletras = models.CharField(max_length=100, blank=True, null=True)
    cvemoneda = models.CharField(max_length=5, blank=True, null=True)
    cvemetpago = models.CharField(max_length=5, blank=True, null=True)
    cvepais = models.CharField(max_length=5, blank=True, null=True)
    cverelaciocfdi = models.CharField(max_length=5, blank=True, null=True)
    cvefmapago = models.CharField(db_column='cvefmaPago', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cveusocfdi = models.CharField(max_length=5, blank=True, null=True)
    cuenta = models.CharField(max_length=15, blank=True, null=True)
    fechagenera = models.DateTimeField(db_column='fechaGenera', blank=True, null=True)  # Field name made lowercase.
    timbrada = models.BooleanField(blank=True, null=True)
    uuid = models.CharField(db_column='UUID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fechatimbrado = models.DateTimeField(blank=True, null=True)
    cancelada = models.BooleanField(blank=True, null=True)
    fechacancelada = models.DateTimeField(blank=True, null=True)
    usercancela = models.CharField(max_length=15, blank=True, null=True)
    folioticket = models.IntegerField(db_column='FolioTicket', blank=True, null=True)  # Field name made lowercase.
    fdia = models.IntegerField(blank=True, null=True)
    base8 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps8 = models.DecimalField(max_digits=18, decimal_places=10)
    base265 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps265 = models.DecimalField(max_digits=18, decimal_places=10)
    base53 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps53 = models.DecimalField(max_digits=18, decimal_places=10)
    base3 = models.DecimalField(max_digits=18, decimal_places=10)
    base6 = models.DecimalField(max_digits=18, decimal_places=10)
    base25 = models.DecimalField(max_digits=18, decimal_places=10)
    base30 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps3 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps6 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps25 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps30 = models.DecimalField(max_digits=18, decimal_places=10)
    baseivaci = models.DecimalField(max_digits=18, decimal_places=6)
    baseivasi = models.DecimalField(max_digits=18, decimal_places=6)
    base0 = models.DecimalField(max_digits=18, decimal_places=6)
    base16 = models.DecimalField(max_digits=18, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'Facturas'


class Facturasrep(models.Model):
    empresa = models.IntegerField()
    cvebod = models.IntegerField()
    seriefac = models.CharField(max_length=5)
    foliofac = models.IntegerField(db_column='FolioFac')  # Field name made lowercase.
    cvemov = models.IntegerField()
    cvecli = models.IntegerField()
    cveusuario = models.CharField(max_length=10)
    importesub = models.DecimalField(max_digits=19, decimal_places=4)
    impdesc = models.DecimalField(max_digits=19, decimal_places=4)
    impiva = models.DecimalField(max_digits=19, decimal_places=4)
    impieps = models.DecimalField(max_digits=19, decimal_places=4)
    imptotal = models.DecimalField(max_digits=19, decimal_places=4)
    porciva = models.FloatField()
    porcieps = models.FloatField()
    impletras = models.CharField(max_length=100)
    cvemoneda = models.CharField(max_length=5)
    cvemetpago = models.CharField(max_length=5)
    cvepais = models.CharField(max_length=5)
    cverelaciocfdi = models.CharField(max_length=5)
    cvefmapago = models.CharField(db_column='cvefmaPago', max_length=5)  # Field name made lowercase.
    cveusocfdi = models.CharField(max_length=5)
    cuenta = models.CharField(max_length=15)
    fechagenera = models.DateTimeField(db_column='fechaGenera')  # Field name made lowercase.
    timbrada = models.BooleanField()
    uuid = models.CharField(db_column='UUID', max_length=50)  # Field name made lowercase.
    fechatimbrado = models.DateTimeField()
    cancelada = models.BooleanField()
    fechacancelada = models.DateTimeField()
    usercancela = models.CharField(max_length=15)
    folioticket = models.IntegerField(db_column='FolioTicket')  # Field name made lowercase.
    fdia = models.IntegerField()
    base8 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps8 = models.DecimalField(max_digits=18, decimal_places=10)
    base265 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps265 = models.DecimalField(max_digits=18, decimal_places=10)
    base53 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps53 = models.DecimalField(max_digits=18, decimal_places=10)
    base3 = models.DecimalField(max_digits=18, decimal_places=10)
    base6 = models.DecimalField(max_digits=18, decimal_places=10)
    base25 = models.DecimalField(max_digits=18, decimal_places=10)
    base30 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps3 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps6 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps25 = models.DecimalField(max_digits=18, decimal_places=10)
    ieps30 = models.DecimalField(max_digits=18, decimal_places=10)
    baseivaci = models.DecimalField(max_digits=18, decimal_places=6)
    baseivasi = models.DecimalField(max_digits=18, decimal_places=6)
    base0 = models.DecimalField(max_digits=18, decimal_places=6)
    base16 = models.DecimalField(max_digits=18, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'FacturasRep'


class Filtros(models.Model):
    cve_filtro = models.IntegerField()
    des_filtro = models.CharField(max_length=25)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Filtros'


class Filtroscatprod(models.Model):
    cvefiltro = models.IntegerField()
    desfiltro = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'FiltrosCatProd'


class Foliosdoc(models.Model):
    empresa = models.IntegerField()
    almacen = models.IntegerField()
    cvemov = models.IntegerField()
    desmov = models.CharField(max_length=100)
    sermov = models.CharField(db_column='Sermov', max_length=5)  # Field name made lowercase.
    folmov = models.IntegerField()
    tipmov = models.IntegerField()
    login = models.CharField(max_length=50)
    fechacreacion = models.DateTimeField()
    caja = models.IntegerField()
    cvemovre = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'FoliosDoc'


class Fondofijo(models.Model):
    cvefon = models.IntegerField(db_column='CveFon')  # Field name made lowercase.
    impfon = models.DecimalField(db_column='ImpFon', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fecfon = models.DateTimeField(db_column='FecFon')  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=20)  # Field name made lowercase.
    cvebod = models.IntegerField(db_column='CveBod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FondoFijo'


class Giros(models.Model):
    cve_giro = models.IntegerField(db_column='Cve_Giro')  # Field name made lowercase.
    des_giro = models.CharField(db_column='Des_Giro', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descorta_giro = models.CharField(db_column='DesCorta_Giro', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cve_canal = models.IntegerField(db_column='Cve_Canal', blank=True, null=True)  # Field name made lowercase.
    baja = models.BooleanField(db_column='Baja', blank=True, null=True)  # Field name made lowercase.
    fecha_alta = models.DateTimeField(db_column='Fecha_Alta', blank=True, null=True)  # Field name made lowercase.
    id_giro = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'GIROS'


class Gastooperacion(models.Model):
    foliogasto = models.IntegerField()
    numcomprobante = models.CharField(max_length=50)
    fechagasto = models.DateField()
    cvegasto = models.IntegerField()
    ctagasto = models.CharField(max_length=15)
    tipogasto = models.IntegerField()
    formapago = models.IntegerField()
    tipomoneda = models.IntegerField()
    cvebanco = models.IntegerField()
    cvechequera = models.IntegerField()
    numcheque = models.CharField(max_length=15)
    subtotal = models.DecimalField(max_digits=19, decimal_places=4)
    porceiva = models.DecimalField(max_digits=19, decimal_places=4)
    impiva = models.DecimalField(max_digits=19, decimal_places=4)
    porceieps = models.DecimalField(max_digits=19, decimal_places=4)
    impieps = models.DecimalField(max_digits=19, decimal_places=4)
    porcotro = models.DecimalField(max_digits=19, decimal_places=4)
    impotro = models.DecimalField(max_digits=19, decimal_places=4)
    imptotal = models.DecimalField(max_digits=19, decimal_places=4)
    fecharegistro = models.DateTimeField()
    usuario = models.CharField(max_length=15)
    equiporeg = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'GastoOperacion'


class Gdocontrol(models.Model):
    cve_gdocont = models.IntegerField(db_column='Cve_GdoCont')  # Field name made lowercase.
    des_gdocont = models.CharField(db_column='Des_GdoCont', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GdoControl'


class Gpomarcafachada(models.Model):
    cve_marfach = models.IntegerField(db_column='Cve_MarFach')  # Field name made lowercase.
    des_marfach = models.CharField(db_column='Des_MarFach', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GpoMarcaFachada'


class GrupoPresentacion(models.Model):
    cve_grupop = models.IntegerField()
    descripcion_grupp = models.CharField(max_length=50, blank=True, null=True)
    descorta_grupp = models.CharField(max_length=20, blank=True, null=True)
    id_gpresentacion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Grupo_Presentacion'


class Gruposproductos(models.Model):
    cvegrupoprod = models.IntegerField()
    desgruppoprod = models.CharField(max_length=100)
    activo = models.BooleanField()
    usuario = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField()
    empresa = models.IntegerField()
    enviado = models.BooleanField()
    fechaenvio = models.DateTimeField()
    userenvio = models.CharField(max_length=50)
    fecmod = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'GruposProductos'


class Gruposproductos1(models.Model):
    cvegrupoprod = models.IntegerField()
    desgruppoprod = models.CharField(max_length=100)
    activo = models.BooleanField()
    usuario = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField()
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'GruposProductos1'


class Gruposproductosa(models.Model):
    cvegrupoprod = models.IntegerField()
    desgruppoprod = models.CharField(max_length=100)
    activo = models.BooleanField()
    usuario = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField()
    empresa = models.IntegerField()
    enviado = models.BooleanField()
    fechaenvio = models.DateTimeField()
    userenvio = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'GruposProductosA'


class Hexiste(models.Model):
    fechadia = models.DateField(blank=True, null=True)
    cveprod = models.CharField(max_length=50, blank=True, null=True)
    cvebod = models.IntegerField(blank=True, null=True)
    existe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    fecinv = models.DateTimeField(blank=True, null=True)
    ultcos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cospro = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    exifis = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    empresa = models.IntegerField(blank=True, null=True)
    numref = models.CharField(max_length=50, blank=True, null=True)
    fechainv = models.DateTimeField(blank=True, null=True)
    logininv = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HEXISTE'


class Identidades(models.Model):
    cve_cadena = models.IntegerField(db_column='Cve_Cadena')  # Field name made lowercase.
    des_cadena = models.CharField(db_column='Des_Cadena', max_length=35, blank=True, null=True)  # Field name made lowercase.
    descorta_cadena = models.CharField(db_column='DesCorta_Cadena', max_length=10, blank=True, null=True)  # Field name made lowercase.
    id_identidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'IDENTIDADES'


class Identidad(models.Model):
    cve_identi = models.IntegerField(db_column='Cve_Identi')  # Field name made lowercase.
    des_identi = models.CharField(db_column='Des_Identi', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Identidad'


class Kardex(models.Model):
    clave = models.CharField(db_column='CLAVE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    folmov = models.IntegerField(db_column='FOLMOV')  # Field name made lowercase.
    sermov = models.CharField(db_column='SERMOV', max_length=2)  # Field name made lowercase.
    cvemov = models.IntegerField(db_column='CVEMOV')  # Field name made lowercase.
    desmov = models.CharField(db_column='DESMOV', max_length=80)  # Field name made lowercase.
    tipmov = models.IntegerField(db_column='TIPMOV')  # Field name made lowercase.
    cvebod = models.IntegerField(db_column='CVEBOD')  # Field name made lowercase.
    desbod = models.CharField(db_column='DESBOD', max_length=80)  # Field name made lowercase.
    cveprod = models.CharField(db_column='CVEPROD', max_length=20)  # Field name made lowercase.
    desprod = models.CharField(db_column='DESPROD', max_length=80)  # Field name made lowercase.
    cveuni = models.CharField(db_column='CVEUNI', max_length=4)  # Field name made lowercase.
    desuni = models.CharField(db_column='DESUNI', max_length=80)  # Field name made lowercase.
    cvefam = models.IntegerField(db_column='CVEFAM')  # Field name made lowercase.
    desfam = models.CharField(db_column='DESFAM', max_length=80)  # Field name made lowercase.
    cvemar = models.IntegerField(db_column='CVEMAR')  # Field name made lowercase.
    desmar = models.CharField(db_column='DESMAR', max_length=80)  # Field name made lowercase.
    cant = models.DecimalField(db_column='CANT', max_digits=19, decimal_places=4)  # Field name made lowercase.
    preuni = models.DecimalField(db_column='PREUNI', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ultcos = models.DecimalField(db_column='ULTCOS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cospro = models.DecimalField(db_column='COSPRO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fecmov = models.DateTimeField(db_column='FECMOV')  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    tipotras = models.CharField(db_column='TipoTras', max_length=1)  # Field name made lowercase.
    observ = models.CharField(db_column='OBSERV', max_length=999, blank=True, null=True)  # Field name made lowercase.
    razon = models.CharField(db_column='RAZON', max_length=88, blank=True, null=True)  # Field name made lowercase.
    direc = models.TextField(db_column='DIREC')  # Field name made lowercase. This field type is a guess.
    vtaafectainv = models.IntegerField(db_column='VTAAFECTAINV')  # Field name made lowercase.
    cantult = models.DecimalField(db_column='CANTULT', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KARDEX'


class Loginapp(models.Model):
    numero_empleado = models.IntegerField()
    password_empleado = models.CharField(max_length=8, blank=True, null=True)
    nivel = models.IntegerField()
    nombre = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'Loginapp'


class Movtos(models.Model):
    cvebod = models.IntegerField(db_column='CveBod', blank=True, null=True)  # Field name made lowercase.
    folmov = models.IntegerField(db_column='FolMov', blank=True, null=True)  # Field name made lowercase.
    cvemov = models.IntegerField(db_column='CveMov', blank=True, null=True)  # Field name made lowercase.
    sermov = models.CharField(db_column='SerMov', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ordcom = models.IntegerField(db_column='OrdCom', blank=True, null=True)  # Field name made lowercase.
    numdoc = models.CharField(db_column='NumDoc', max_length=40, blank=True, null=True)  # Field name made lowercase.
    fecmov = models.DateTimeField(db_column='FecMov', blank=True, null=True)  # Field name made lowercase.
    cveprovcli = models.IntegerField(db_column='CveProvCli', blank=True, null=True)  # Field name made lowercase.
    diascred = models.IntegerField(db_column='DiasCred', blank=True, null=True)  # Field name made lowercase.
    impmov = models.DecimalField(db_column='ImpMov', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impdes = models.DecimalField(db_column='ImpDes', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcdesc = models.DecimalField(db_column='PorcDesc', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impfle = models.DecimalField(db_column='ImpFle', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impsub = models.DecimalField(db_column='ImpSub', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impiva = models.DecimalField(db_column='ImpIva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porciva = models.DecimalField(db_column='PorcIva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imptot = models.DecimalField(db_column='ImpTot', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cveven = models.IntegerField(db_column='CveVen', blank=True, null=True)  # Field name made lowercase.
    folref = models.IntegerField(db_column='FolRef', blank=True, null=True)  # Field name made lowercase.
    cvemovref = models.IntegerField(db_column='CveMovRef', blank=True, null=True)  # Field name made lowercase.
    sermovref = models.CharField(db_column='SerMovRef', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cvebodref = models.IntegerField(db_column='CveBodRef', blank=True, null=True)  # Field name made lowercase.
    cveboddes = models.IntegerField(db_column='CveBodDes', blank=True, null=True)  # Field name made lowercase.
    observ = models.TextField(db_column='Observ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    implet = models.CharField(db_column='ImpLet', max_length=300, blank=True, null=True)  # Field name made lowercase.
    facturada = models.BooleanField(db_column='Facturada', blank=True, null=True)  # Field name made lowercase.
    cancelada = models.BooleanField(db_column='Cancelada', blank=True, null=True)  # Field name made lowercase.
    devuelto = models.BooleanField(db_column='Devuelto', blank=True, null=True)  # Field name made lowercase.
    afectado = models.BooleanField(db_column='Afectado', blank=True, null=True)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL', blank=True, null=True)  # Field name made lowercase.
    cvecli = models.IntegerField(db_column='CVECLI', blank=True, null=True)  # Field name made lowercase.
    rentado = models.BooleanField(db_column='RENTADO', blank=True, null=True)  # Field name made lowercase.
    cveven2 = models.IntegerField(db_column='CVEVEN2', blank=True, null=True)  # Field name made lowercase.
    direc = models.TextField(db_column='DIREC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecenv = models.DateTimeField(db_column='FECENV', blank=True, null=True)  # Field name made lowercase.
    numdias = models.IntegerField(db_column='NumDias', blank=True, null=True)  # Field name made lowercase.
    cvemovorig = models.IntegerField(db_column='CveMovOrig', blank=True, null=True)  # Field name made lowercase.
    sermovorig = models.CharField(db_column='SerMovOrig', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cvebodorig = models.IntegerField(db_column='CveBodOrig', blank=True, null=True)  # Field name made lowercase.
    folmovorig = models.IntegerField(db_column='FolMovOrig', blank=True, null=True)  # Field name made lowercase.
    credito = models.BooleanField(db_column='Credito', blank=True, null=True)  # Field name made lowercase.
    folreq = models.IntegerField(db_column='FolReq', blank=True, null=True)  # Field name made lowercase.
    reqext = models.BooleanField(db_column='ReqExt', blank=True, null=True)  # Field name made lowercase.
    reqcont = models.BooleanField(db_column='ReqCont', blank=True, null=True)  # Field name made lowercase.
    fecentrep = models.DateTimeField(db_column='FecEntRep', blank=True, null=True)  # Field name made lowercase.
    autorizarep = models.BooleanField(db_column='AutorizaRep', blank=True, null=True)  # Field name made lowercase.
    persautorizarep = models.CharField(db_column='PersAutorizaRep', max_length=80, blank=True, null=True)  # Field name made lowercase.
    fecautrep = models.DateTimeField(db_column='FecAutRep', blank=True, null=True)  # Field name made lowercase.
    repentregada = models.BooleanField(db_column='RepEntregada', blank=True, null=True)  # Field name made lowercase.
    repfecentrega = models.DateTimeField(db_column='RepFecEntrega', blank=True, null=True)  # Field name made lowercase.
    repfecgtia = models.DateTimeField(db_column='RepFecGtia', blank=True, null=True)  # Field name made lowercase.
    unidadv = models.CharField(db_column='UnidadV', max_length=25, blank=True, null=True)  # Field name made lowercase.
    marcav = models.CharField(db_column='MarcaV', max_length=25, blank=True, null=True)  # Field name made lowercase.
    placasv = models.CharField(db_column='PlacasV', max_length=12, blank=True, null=True)  # Field name made lowercase.
    kilomv = models.DecimalField(db_column='KilomV', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    maniobras = models.DecimalField(db_column='Maniobras', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mermas = models.DecimalField(db_column='Mermas', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    origen1 = models.CharField(db_column='Origen1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remitente = models.CharField(db_column='Remitente', max_length=100, blank=True, null=True)  # Field name made lowercase.
    domicilio1 = models.CharField(db_column='Domicilio1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    origen2 = models.CharField(db_column='Origen2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    destinatario = models.CharField(db_column='Destinatario', max_length=100, blank=True, null=True)  # Field name made lowercase.
    domicilio2 = models.CharField(db_column='Domicilio2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cvemon = models.IntegerField(db_column='CveMon', blank=True, null=True)  # Field name made lowercase.
    cvetippag = models.IntegerField(db_column='CveTipPag', blank=True, null=True)  # Field name made lowercase.
    dfrazsoc = models.CharField(db_column='DFRazSoc', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dfrfc = models.CharField(db_column='DFRFC', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dfdir = models.CharField(db_column='DFDir', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dfcol = models.CharField(db_column='DFCol', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dfciu = models.CharField(db_column='DFCiu', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dfedo = models.CharField(db_column='DFEdo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dfemail = models.CharField(db_column='DFEmail', max_length=250, blank=True, null=True)  # Field name made lowercase.
    nomproy = models.CharField(db_column='NomProy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dfobserva = models.CharField(db_column='DFObserva', max_length=500, blank=True, null=True)  # Field name made lowercase.
    entregatotal = models.BooleanField(db_column='EntregaTotal', blank=True, null=True)  # Field name made lowercase.
    dfcvemon = models.IntegerField(db_column='DFCveMon', blank=True, null=True)  # Field name made lowercase.
    dftipfact = models.SmallIntegerField(db_column='DFTipFact', blank=True, null=True)  # Field name made lowercase.
    dfcp = models.CharField(db_column='DFCP', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dfcuentapago = models.CharField(db_column='DFCuentaPago', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dftippag = models.SmallIntegerField(db_column='DFTipPag', blank=True, null=True)  # Field name made lowercase.
    factcvetippag = models.IntegerField(db_column='FactCveTipPag', blank=True, null=True)  # Field name made lowercase.
    factnumcuenta = models.CharField(db_column='FactNumCuenta', max_length=50, blank=True, null=True)  # Field name made lowercase.
    porcieps = models.DecimalField(db_column='PorcIEPS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ieps = models.DecimalField(db_column='IEPS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcivaret = models.DecimalField(db_column='PorcIVARet', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impivaret = models.DecimalField(db_column='ImpIVARet', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    porfacturar = models.BooleanField(blank=True, null=True)
    base0 = models.DecimalField(db_column='Base0', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base16 = models.DecimalField(db_column='Base16', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imptoiva = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    poriva = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    baseieps1 = models.DecimalField(db_column='Baseieps1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imptoieps1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    porieps1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    baseieps2 = models.DecimalField(db_column='Baseieps2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imptoieps2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    porieps2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    baseieps3 = models.DecimalField(db_column='Baseieps3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imptoieps3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    porieps3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    baseieps4 = models.DecimalField(db_column='Baseieps4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imptoieps4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    porieps4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    uuid = models.CharField(db_column='UUID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fechafac = models.DateTimeField(db_column='FECHAFAC', blank=True, null=True)  # Field name made lowercase.
    usuariofac = models.CharField(db_column='USUARIOFAC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    retirado = models.BooleanField(blank=True, null=True)
    transmitida = models.BooleanField(blank=True, null=True)
    turno = models.IntegerField(blank=True, null=True)
    sercierre = models.CharField(max_length=10, blank=True, null=True)
    folcierre = models.IntegerField(blank=True, null=True)
    cierreturno = models.BooleanField(blank=True, null=True)
    cierredia = models.BooleanField(blank=True, null=True)
    empresaori = models.IntegerField(blank=True, null=True)
    empresades = models.IntegerField(blank=True, null=True)
    incluircorte = models.BooleanField(blank=True, null=True)
    transaccion = models.CharField(db_column='Transaccion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tipomov = models.IntegerField(blank=True, null=True)
    caja = models.IntegerField(blank=True, null=True)
    pagada = models.BooleanField()
    seriepago = models.CharField(max_length=15)
    foliopago = models.IntegerField()
    fechapago = models.DateTimeField()
    userpago = models.CharField(max_length=50)
    fechaprogpag = models.DateTimeField()
    tefectivo = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    ttarjeta = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    ttransferencia = models.DecimalField(max_digits=18, decimal_places=10, blank=True, null=True)
    cveconductor = models.IntegerField(blank=True, null=True)
    cveauto = models.IntegerField(blank=True, null=True)
    baseieps5 = models.DecimalField(max_digits=19, decimal_places=4)
    imptoieps5 = models.DecimalField(max_digits=19, decimal_places=4)
    porieps5 = models.DecimalField(max_digits=19, decimal_places=4)
    baseieps6 = models.DecimalField(max_digits=19, decimal_places=4)
    imptoieps6 = models.DecimalField(max_digits=19, decimal_places=4)
    porieps6 = models.DecimalField(max_digits=19, decimal_places=4)
    baseieps7 = models.DecimalField(max_digits=19, decimal_places=4)
    imptoieps7 = models.DecimalField(max_digits=19, decimal_places=4)
    porieps7 = models.DecimalField(max_digits=19, decimal_places=4)
    baseieps8 = models.DecimalField(max_digits=19, decimal_places=4)
    imptoieps8 = models.DecimalField(max_digits=19, decimal_places=4)
    porieps8 = models.DecimalField(max_digits=19, decimal_places=4)
    userproce = models.CharField(max_length=50)
    fechaproce = models.DateTimeField()
    sermovproce = models.CharField(max_length=15)
    folmovproce = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'MOVTOS'


class Movtosr(models.Model):
    cvebod = models.IntegerField(db_column='CveBod', blank=True, null=True)  # Field name made lowercase.
    folmov = models.IntegerField(db_column='FolMov', blank=True, null=True)  # Field name made lowercase.
    cvemov = models.IntegerField(db_column='CveMov', blank=True, null=True)  # Field name made lowercase.
    sermov = models.CharField(db_column='SerMov', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ordcom = models.IntegerField(db_column='OrdCom', blank=True, null=True)  # Field name made lowercase.
    numdoc = models.CharField(db_column='NumDoc', max_length=40, blank=True, null=True)  # Field name made lowercase.
    fecmov = models.DateTimeField(db_column='FecMov', blank=True, null=True)  # Field name made lowercase.
    cveprovcli = models.IntegerField(db_column='CveProvCli', blank=True, null=True)  # Field name made lowercase.
    diascred = models.IntegerField(db_column='DiasCred', blank=True, null=True)  # Field name made lowercase.
    impmov = models.DecimalField(db_column='ImpMov', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impdes = models.DecimalField(db_column='ImpDes', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcdesc = models.DecimalField(db_column='PorcDesc', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impfle = models.DecimalField(db_column='ImpFle', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impsub = models.DecimalField(db_column='ImpSub', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impiva = models.DecimalField(db_column='ImpIva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porciva = models.DecimalField(db_column='PorcIva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imptot = models.DecimalField(db_column='ImpTot', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cveven = models.IntegerField(db_column='CveVen', blank=True, null=True)  # Field name made lowercase.
    folref = models.IntegerField(db_column='FolRef', blank=True, null=True)  # Field name made lowercase.
    cvemovref = models.IntegerField(db_column='CveMovRef', blank=True, null=True)  # Field name made lowercase.
    sermovref = models.CharField(db_column='SerMovRef', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cvebodref = models.IntegerField(db_column='CveBodRef', blank=True, null=True)  # Field name made lowercase.
    cveboddes = models.IntegerField(db_column='CveBodDes', blank=True, null=True)  # Field name made lowercase.
    observ = models.TextField(db_column='Observ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    implet = models.CharField(db_column='ImpLet', max_length=300, blank=True, null=True)  # Field name made lowercase.
    facturada = models.BooleanField(db_column='Facturada', blank=True, null=True)  # Field name made lowercase.
    cancelada = models.BooleanField(db_column='Cancelada', blank=True, null=True)  # Field name made lowercase.
    devuelto = models.BooleanField(db_column='Devuelto', blank=True, null=True)  # Field name made lowercase.
    afectado = models.BooleanField(db_column='Afectado', blank=True, null=True)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL', blank=True, null=True)  # Field name made lowercase.
    cvecli = models.IntegerField(db_column='CVECLI', blank=True, null=True)  # Field name made lowercase.
    rentado = models.BooleanField(db_column='RENTADO', blank=True, null=True)  # Field name made lowercase.
    cveven2 = models.IntegerField(db_column='CVEVEN2', blank=True, null=True)  # Field name made lowercase.
    direc = models.TextField(db_column='DIREC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecenv = models.DateTimeField(db_column='FECENV', blank=True, null=True)  # Field name made lowercase.
    numdias = models.IntegerField(db_column='NumDias', blank=True, null=True)  # Field name made lowercase.
    cvemovorig = models.IntegerField(db_column='CveMovOrig', blank=True, null=True)  # Field name made lowercase.
    sermovorig = models.CharField(db_column='SerMovOrig', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cvebodorig = models.IntegerField(db_column='CveBodOrig', blank=True, null=True)  # Field name made lowercase.
    folmovorig = models.IntegerField(db_column='FolMovOrig', blank=True, null=True)  # Field name made lowercase.
    credito = models.BooleanField(db_column='Credito', blank=True, null=True)  # Field name made lowercase.
    folreq = models.IntegerField(db_column='FolReq', blank=True, null=True)  # Field name made lowercase.
    reqext = models.BooleanField(db_column='ReqExt', blank=True, null=True)  # Field name made lowercase.
    reqcont = models.BooleanField(db_column='ReqCont', blank=True, null=True)  # Field name made lowercase.
    fecentrep = models.DateTimeField(db_column='FecEntRep', blank=True, null=True)  # Field name made lowercase.
    autorizarep = models.BooleanField(db_column='AutorizaRep', blank=True, null=True)  # Field name made lowercase.
    persautorizarep = models.CharField(db_column='PersAutorizaRep', max_length=80, blank=True, null=True)  # Field name made lowercase.
    fecautrep = models.DateTimeField(db_column='FecAutRep', blank=True, null=True)  # Field name made lowercase.
    repentregada = models.BooleanField(db_column='RepEntregada', blank=True, null=True)  # Field name made lowercase.
    repfecentrega = models.DateTimeField(db_column='RepFecEntrega', blank=True, null=True)  # Field name made lowercase.
    repfecgtia = models.DateTimeField(db_column='RepFecGtia', blank=True, null=True)  # Field name made lowercase.
    unidadv = models.CharField(db_column='UnidadV', max_length=25, blank=True, null=True)  # Field name made lowercase.
    marcav = models.CharField(db_column='MarcaV', max_length=25, blank=True, null=True)  # Field name made lowercase.
    placasv = models.CharField(db_column='PlacasV', max_length=12, blank=True, null=True)  # Field name made lowercase.
    kilomv = models.DecimalField(db_column='KilomV', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    maniobras = models.DecimalField(db_column='Maniobras', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mermas = models.DecimalField(db_column='Mermas', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    origen1 = models.CharField(db_column='Origen1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remitente = models.CharField(db_column='Remitente', max_length=100, blank=True, null=True)  # Field name made lowercase.
    domicilio1 = models.CharField(db_column='Domicilio1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    origen2 = models.CharField(db_column='Origen2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    destinatario = models.CharField(db_column='Destinatario', max_length=100, blank=True, null=True)  # Field name made lowercase.
    domicilio2 = models.CharField(db_column='Domicilio2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cvemon = models.IntegerField(db_column='CveMon', blank=True, null=True)  # Field name made lowercase.
    cvetippag = models.IntegerField(db_column='CveTipPag', blank=True, null=True)  # Field name made lowercase.
    dfrazsoc = models.CharField(db_column='DFRazSoc', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dfrfc = models.CharField(db_column='DFRFC', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dfdir = models.CharField(db_column='DFDir', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dfcol = models.CharField(db_column='DFCol', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dfciu = models.CharField(db_column='DFCiu', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dfedo = models.CharField(db_column='DFEdo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dfemail = models.CharField(db_column='DFEmail', max_length=250, blank=True, null=True)  # Field name made lowercase.
    nomproy = models.CharField(db_column='NomProy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dfobserva = models.CharField(db_column='DFObserva', max_length=500, blank=True, null=True)  # Field name made lowercase.
    entregatotal = models.BooleanField(db_column='EntregaTotal', blank=True, null=True)  # Field name made lowercase.
    dfcvemon = models.IntegerField(db_column='DFCveMon', blank=True, null=True)  # Field name made lowercase.
    dftipfact = models.SmallIntegerField(db_column='DFTipFact', blank=True, null=True)  # Field name made lowercase.
    dfcp = models.CharField(db_column='DFCP', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dfcuentapago = models.CharField(db_column='DFCuentaPago', max_length=250, blank=True, null=True)  # Field name made lowercase.
    dftippag = models.SmallIntegerField(db_column='DFTipPag', blank=True, null=True)  # Field name made lowercase.
    factcvetippag = models.IntegerField(db_column='FactCveTipPag', blank=True, null=True)  # Field name made lowercase.
    factnumcuenta = models.CharField(db_column='FactNumCuenta', max_length=50, blank=True, null=True)  # Field name made lowercase.
    porcieps = models.DecimalField(db_column='PorcIEPS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ieps = models.DecimalField(db_column='IEPS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcivaret = models.DecimalField(db_column='PorcIVARet', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    impivaret = models.DecimalField(db_column='ImpIVARet', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    empresa = models.IntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.
    porfacturar = models.BooleanField(blank=True, null=True)
    base0 = models.DecimalField(db_column='Base0', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base16 = models.DecimalField(db_column='Base16', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imptoiva = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    poriva = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    baseieps1 = models.DecimalField(db_column='Baseieps1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imptoieps1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    porieps1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    baseieps2 = models.DecimalField(db_column='Baseieps2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imptoieps2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    porieps2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    baseieps3 = models.DecimalField(db_column='Baseieps3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imptoieps3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    porieps3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    baseieps4 = models.DecimalField(db_column='Baseieps4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imptoieps4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    porieps4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    uuid = models.CharField(db_column='UUID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fechafac = models.DateTimeField(db_column='FECHAFAC', blank=True, null=True)  # Field name made lowercase.
    usuariofac = models.CharField(db_column='USUARIOFAC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    retirado = models.BooleanField(blank=True, null=True)
    transmitida = models.BooleanField(blank=True, null=True)
    turno = models.IntegerField(blank=True, null=True)
    sercierre = models.CharField(max_length=10, blank=True, null=True)
    folcierre = models.IntegerField(blank=True, null=True)
    cierreturno = models.BooleanField(blank=True, null=True)
    cierredia = models.BooleanField(blank=True, null=True)
    empresaori = models.IntegerField(blank=True, null=True)
    empresades = models.IntegerField(blank=True, null=True)
    incluircorte = models.BooleanField(blank=True, null=True)
    transaccion = models.CharField(max_length=50, blank=True, null=True)
    tipomov = models.IntegerField(blank=True, null=True)
    caja = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MOVTOSR'


class Movmuebles(models.Model):
    empresa = models.IntegerField(db_column='Empresa')  # Field name made lowercase.
    seriemov = models.CharField(db_column='Seriemov', max_length=3)  # Field name made lowercase.
    foliomov = models.IntegerField(db_column='FolioMov')  # Field name made lowercase.
    tipomov = models.IntegerField()
    fechamov = models.DateTimeField()
    cvecli = models.CharField(max_length=10)
    index_ruta = models.IntegerField()
    desc_ruta = models.CharField(max_length=10)
    cveven = models.IntegerField()
    observacion = models.CharField(max_length=100)
    ref1 = models.CharField(max_length=50)
    ref2 = models.CharField(max_length=50)
    activo = models.BooleanField()
    cancelado = models.BooleanField()
    comodatado = models.BooleanField()
    entregado = models.BooleanField(db_column='Entregado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Movmuebles'


class Muebles(models.Model):
    index_mue = models.IntegerField()
    usuario = models.CharField(max_length=50)
    descripcion_mue = models.CharField(max_length=250, blank=True, null=True)
    controla_noserie = models.FloatField(blank=True, null=True)
    des_corta = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Muebles'


class Notascred(models.Model):
    sernot = models.CharField(db_column='SERNOT', max_length=2)  # Field name made lowercase.
    folnot = models.IntegerField(db_column='FOLNOT')  # Field name made lowercase.
    tipnot = models.SmallIntegerField(db_column='TIPNOT')  # Field name made lowercase.
    fecnot = models.DateTimeField(db_column='FECNOT')  # Field name made lowercase.
    impnot = models.DecimalField(db_column='IMPNOT', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ivanot = models.DecimalField(db_column='IVANOT', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porciva = models.DecimalField(db_column='PORCIVA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    totnot = models.DecimalField(db_column='TOTNOT', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cvebod = models.IntegerField(db_column='CVEBOD')  # Field name made lowercase.
    cvemov = models.IntegerField(db_column='CVEMOV')  # Field name made lowercase.
    folmov = models.IntegerField(db_column='FOLMOV')  # Field name made lowercase.
    sermov = models.CharField(db_column='SERMOV', max_length=2)  # Field name made lowercase.
    cveprovcli = models.CharField(db_column='CVEPROVCLI', max_length=15)  # Field name made lowercase.
    obsnot = models.TextField(db_column='OBSNOT')  # Field name made lowercase. This field type is a guess.
    tipmov = models.SmallIntegerField(db_column='TIPMOV')  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=20)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    cancelada = models.BooleanField(db_column='CANCELADA')  # Field name made lowercase.
    porcieps = models.DecimalField(db_column='PORCIEPS', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ieps = models.DecimalField(db_column='IEPS', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOTASCRED'


class Nivesocioeco(models.Model):
    cve_socioeco = models.IntegerField(db_column='Cve_socioeco')  # Field name made lowercase.
    des_socioeco = models.CharField(db_column='Des_socioeco', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NiveSocioeco'


class Noexiste(models.Model):
    numref = models.CharField(max_length=50)
    desprod = models.CharField(max_length=800)
    existencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'NoExiste'


class Pronostico(models.Model):
    cvebod = models.IntegerField()
    desbod = models.CharField(max_length=80)
    cvemov = models.IntegerField()
    desmov = models.CharField(max_length=80)
    sermov = models.CharField(max_length=2)
    folmov = models.IntegerField()
    fecmov = models.DateTimeField()
    fecvenc = models.DateTimeField(blank=True, null=True)
    diasvenc = models.IntegerField(db_column='DiasVenc', blank=True, null=True)  # Field name made lowercase.
    cveprovcli = models.IntegerField()
    nomcli = models.CharField(max_length=80)
    nomcli2 = models.CharField(max_length=80)
    tipo = models.IntegerField()
    imptot = models.DecimalField(max_digits=19, decimal_places=4)
    pagos = models.DecimalField(max_digits=19, decimal_places=4)
    cveciu = models.IntegerField()
    nomciu = models.CharField(max_length=80)
    cveedo = models.IntegerField()
    nomedo = models.CharField(max_length=80)
    cvegrucli = models.IntegerField()
    desgrucli = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'PRONOSTICO'


class Pais(models.Model):
    id = models.CharField(max_length=5)
    cve_pais = models.CharField(max_length=5, blank=True, null=True)
    des_pais = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pais'


class ParametrosPos(models.Model):
    empresa = models.IntegerField(db_column='Empresa')  # Field name made lowercase.
    equipo = models.CharField(max_length=50)
    bodega = models.IntegerField(db_column='Bodega')  # Field name made lowercase.
    cliente = models.IntegerField(db_column='Cliente')  # Field name made lowercase.
    lista_precio = models.IntegerField()
    movto = models.IntegerField()
    serie = models.CharField(db_column='Serie', max_length=10)  # Field name made lowercase.
    montoretiro = models.DecimalField(max_digits=19, decimal_places=4)
    caja = models.IntegerField(db_column='Caja')  # Field name made lowercase.
    retiros = models.BooleanField()
    usuario = models.CharField(max_length=50)
    fechaalta = models.DateTimeField()
    tipomov = models.IntegerField()
    cvemovimp = models.IntegerField()
    sermovimp = models.CharField(max_length=10)
    diasimp = models.IntegerField()
    numticket = models.IntegerField()
    movcierret = models.IntegerField()
    sercierret = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Parametros_Pos'


class Permisos(models.Model):
    perfil = models.IntegerField(db_column='Perfil')  # Field name made lowercase.
    descperfil = models.CharField(max_length=20)
    almacenc = models.BooleanField(db_column='almacenC')  # Field name made lowercase.
    almacenm = models.BooleanField(db_column='almacenM')  # Field name made lowercase.
    almacene = models.BooleanField(db_column='almacenE')  # Field name made lowercase.
    almaceni = models.BooleanField(db_column='almacenI')  # Field name made lowercase.
    bancoc = models.BooleanField(db_column='bancoC')  # Field name made lowercase.
    bancom = models.BooleanField(db_column='bancoM')  # Field name made lowercase.
    bancoe = models.BooleanField(db_column='bancoE')  # Field name made lowercase.
    bancoi = models.BooleanField(db_column='bancoI')  # Field name made lowercase.
    bonificacionesc = models.BooleanField()
    bonifiicacionesm = models.BooleanField()
    bonificacionese = models.BooleanField()
    bonificacionesi = models.BooleanField()
    chequerac = models.BooleanField(db_column='chequeraC')  # Field name made lowercase.
    chequeram = models.BooleanField(db_column='chequeraM')  # Field name made lowercase.
    chequerae = models.BooleanField(db_column='chequeraE')  # Field name made lowercase.
    chequerai = models.BooleanField(db_column='chequeraI')  # Field name made lowercase.
    ciudadesc = models.BooleanField(db_column='ciudadesC')  # Field name made lowercase.
    ciudadesm = models.BooleanField(db_column='ciudadesM')  # Field name made lowercase.
    ciudade = models.BooleanField(db_column='ciudadE')  # Field name made lowercase.
    ciudadi = models.BooleanField(db_column='ciudadI')  # Field name made lowercase.
    clientesc = models.BooleanField(db_column='clientesC')  # Field name made lowercase.
    clientesm = models.BooleanField(db_column='clientesM')  # Field name made lowercase.
    clientese = models.BooleanField(db_column='clientesE')  # Field name made lowercase.
    clientesi = models.BooleanField(db_column='clientesI')  # Field name made lowercase.
    comicionesc = models.BooleanField(db_column='comicionesC')  # Field name made lowercase.
    comicionesm = models.BooleanField(db_column='comicionesM')  # Field name made lowercase.
    comicionese = models.BooleanField(db_column='comicionesE')  # Field name made lowercase.
    comicionesi = models.BooleanField(db_column='comicionesI')  # Field name made lowercase.
    descuentosc = models.BooleanField(db_column='descuentosC')  # Field name made lowercase.
    descuentosm = models.BooleanField(db_column='descuentosM')  # Field name made lowercase.
    descuentose = models.BooleanField(db_column='descuentosE')  # Field name made lowercase.
    descuentosi = models.BooleanField(db_column='descuentosI')  # Field name made lowercase.
    estadosc = models.BooleanField(db_column='estadosC')  # Field name made lowercase.
    estadosm = models.BooleanField(db_column='estadosM')  # Field name made lowercase.
    estadose = models.BooleanField(db_column='estadosE')  # Field name made lowercase.
    estadosi = models.BooleanField(db_column='estadosI')  # Field name made lowercase.
    familiac = models.BooleanField(db_column='familiaC')  # Field name made lowercase.
    familiam = models.BooleanField(db_column='familiaM')  # Field name made lowercase.
    familiae = models.BooleanField(db_column='familiaE')  # Field name made lowercase.
    familiai = models.BooleanField(db_column='familiaI')  # Field name made lowercase.
    gastosfijosc = models.BooleanField(db_column='gastosfijosC')  # Field name made lowercase.
    gastosfijosm = models.BooleanField(db_column='gastosfijosM')  # Field name made lowercase.
    gastosfijose = models.BooleanField(db_column='gastosfijosE')  # Field name made lowercase.
    gastosijosi = models.BooleanField(db_column='gastosijosI')  # Field name made lowercase.
    grupodeclientec = models.BooleanField(db_column='grupodeclienteC')  # Field name made lowercase.
    grupodeclientem = models.BooleanField(db_column='grupodeclienteM')  # Field name made lowercase.
    gropodeclientee = models.BooleanField(db_column='gropodeclienteE')  # Field name made lowercase.
    grupodeclientei = models.BooleanField(db_column='grupodeclienteI')  # Field name made lowercase.
    grupodeproveedorc = models.BooleanField(db_column='grupodeproveedorC')  # Field name made lowercase.
    grupodeproveedorm = models.BooleanField(db_column='grupodeproveedorM')  # Field name made lowercase.
    grupodeproveedore = models.BooleanField(db_column='grupodeproveedorE')  # Field name made lowercase.
    grupodeproveedori = models.BooleanField(db_column='grupodeproveedorI')  # Field name made lowercase.
    marcasc = models.BooleanField(db_column='marcasC')  # Field name made lowercase.
    marcasm = models.BooleanField(db_column='marcasM')  # Field name made lowercase.
    marcase = models.BooleanField(db_column='marcasE')  # Field name made lowercase.
    marcasi = models.BooleanField(db_column='marcasI')  # Field name made lowercase.
    modenac = models.BooleanField(db_column='modenaC')  # Field name made lowercase.
    monedam = models.BooleanField(db_column='monedaM')  # Field name made lowercase.
    monedae = models.BooleanField(db_column='monedaE')  # Field name made lowercase.
    monedai = models.BooleanField(db_column='monedaI')  # Field name made lowercase.
    movilesc = models.BooleanField(db_column='movilesC')  # Field name made lowercase.
    movilesm = models.BooleanField(db_column='movilesM')  # Field name made lowercase.
    movilese = models.BooleanField(db_column='movilesE')  # Field name made lowercase.
    movilesi = models.BooleanField(db_column='movilesI')  # Field name made lowercase.
    movimientosc = models.BooleanField(db_column='movimientosC')  # Field name made lowercase.
    movimientosm = models.BooleanField(db_column='movimientosM')  # Field name made lowercase.
    movimientose = models.BooleanField(db_column='movimientosE')  # Field name made lowercase.
    movimientosi = models.BooleanField(db_column='movimientosI')  # Field name made lowercase.
    productosc = models.BooleanField(db_column='productosC')  # Field name made lowercase.
    productosm = models.BooleanField(db_column='productosM')  # Field name made lowercase.
    productose = models.BooleanField(db_column='productosE')  # Field name made lowercase.
    productosi = models.BooleanField(db_column='productosI')  # Field name made lowercase.
    proveeedoresc = models.BooleanField()
    proveedoresm = models.BooleanField()
    proveedoorese = models.BooleanField()
    proveedoresi = models.BooleanField()
    promocionesc = models.BooleanField(db_column='promocionesC')  # Field name made lowercase.
    promocionesm = models.BooleanField(db_column='promocionesM')  # Field name made lowercase.
    promocionese = models.BooleanField(db_column='promocionesE')  # Field name made lowercase.
    promocionesi = models.BooleanField(db_column='promocionesI')  # Field name made lowercase.
    puntoc = models.BooleanField(db_column='puntoC')  # Field name made lowercase.
    puntom = models.BooleanField(db_column='puntoM')  # Field name made lowercase.
    puntoe = models.BooleanField(db_column='puntoE')  # Field name made lowercase.
    puntoi = models.BooleanField(db_column='puntoI')  # Field name made lowercase.
    tipodepagoc = models.BooleanField(db_column='tipodepagoC')  # Field name made lowercase.
    tipodepagom = models.BooleanField(db_column='tipodepagoM')  # Field name made lowercase.
    tipodepagoe = models.BooleanField(db_column='tipodepagoE')  # Field name made lowercase.
    tipodepagoi = models.BooleanField(db_column='tipodepagoI')  # Field name made lowercase.
    unidaddemedidac = models.BooleanField(db_column='unidaddemedidaC')  # Field name made lowercase.
    unidaddemedidam = models.BooleanField(db_column='unidaddemedidaM')  # Field name made lowercase.
    unidaddemedidae0 = models.BooleanField(db_column='unidaddemedidaE0')  # Field name made lowercase.
    unidaddemedidai = models.BooleanField(db_column='unidaddemedidaI')  # Field name made lowercase.
    vendedoresc = models.BooleanField(db_column='vendedoresC')  # Field name made lowercase.
    vendedoresm = models.BooleanField(db_column='vendedoresM')  # Field name made lowercase.
    vendedorese = models.BooleanField(db_column='vendedoresE')  # Field name made lowercase.
    vendedoresi = models.BooleanField(db_column='vendedoresI')  # Field name made lowercase.
    datodecompañiac = models.BooleanField(db_column='datodecompañiaC')  # Field name made lowercase.
    datodecompañiam = models.BooleanField(db_column='datodecompañiaM')  # Field name made lowercase.
    datodecompañiae = models.BooleanField(db_column='datodecompañiaE')  # Field name made lowercase.
    datodecompañiai = models.BooleanField(db_column='datodecompañiaI')  # Field name made lowercase.
    usuariosc = models.BooleanField(db_column='usuariosC')  # Field name made lowercase.
    usuariosm = models.BooleanField(db_column='usuariosM')  # Field name made lowercase.
    usuarioe = models.BooleanField(db_column='usuarioE')  # Field name made lowercase.
    usuariosi = models.BooleanField(db_column='usuariosI')  # Field name made lowercase.
    comprasc = models.BooleanField(db_column='comprasC')  # Field name made lowercase.
    comprasm = models.BooleanField(db_column='comprasM')  # Field name made lowercase.
    comprase = models.BooleanField(db_column='comprasE')  # Field name made lowercase.
    comprasi = models.BooleanField(db_column='comprasI')  # Field name made lowercase.
    entradasc = models.BooleanField(db_column='entradasC')  # Field name made lowercase.
    entrdasm = models.BooleanField(db_column='entrdasM')  # Field name made lowercase.
    entrdase = models.BooleanField(db_column='entrdasE')  # Field name made lowercase.
    entrdasi = models.BooleanField(db_column='entrdasI')  # Field name made lowercase.
    movenfriadoresc = models.BooleanField(db_column='movenfriadoresC')  # Field name made lowercase.
    movenfriadoresm = models.BooleanField(db_column='movenfriadoresM')  # Field name made lowercase.
    movenfriadorese = models.BooleanField(db_column='movenfriadoresE')  # Field name made lowercase.
    movenfriadoresi = models.BooleanField(db_column='movenfriadoresI')  # Field name made lowercase.
    devolcomprac = models.BooleanField(db_column='devolcompraC')  # Field name made lowercase.
    devolcompram = models.BooleanField(db_column='devolcompraM')  # Field name made lowercase.
    devolcomprae = models.BooleanField(db_column='devolcompraE')  # Field name made lowercase.
    devolcomprai = models.BooleanField(db_column='devolcompraI')  # Field name made lowercase.
    devolrentac = models.BooleanField(db_column='devolrentaC')  # Field name made lowercase.
    devolrentam = models.BooleanField(db_column='devolrentaM')  # Field name made lowercase.
    devolrentae = models.BooleanField(db_column='devolrentaE')  # Field name made lowercase.
    devolrentai = models.BooleanField(db_column='devolrentaI')  # Field name made lowercase.
    devolventac = models.BooleanField(db_column='devolventaC')  # Field name made lowercase.
    devolventam = models.BooleanField(db_column='devolventaM')  # Field name made lowercase.
    devolventae = models.BooleanField(db_column='devolventaE')  # Field name made lowercase.
    devolventai = models.BooleanField(db_column='devolventaI')  # Field name made lowercase.
    facturacionc = models.BooleanField(db_column='facturacionC')  # Field name made lowercase.
    facturacionm = models.BooleanField(db_column='facturacionM')  # Field name made lowercase.
    facturacione = models.BooleanField(db_column='facturacionE')  # Field name made lowercase.
    facturacioni = models.BooleanField(db_column='facturacionI')  # Field name made lowercase.
    cotizaciondecomprac = models.BooleanField(db_column='cotizaciondecompraC')  # Field name made lowercase.
    cotizaciondecompram = models.BooleanField(db_column='cotizaciondecompraM')  # Field name made lowercase.
    cotizaciondecomprae = models.BooleanField(db_column='cotizaciondecompraE')  # Field name made lowercase.
    cotizaciondecomprai = models.BooleanField(db_column='cotizaciondecompraI')  # Field name made lowercase.
    cotizaciondeventac = models.BooleanField(db_column='cotizaciondeventaC')  # Field name made lowercase.
    cotizaciondeventam = models.BooleanField(db_column='cotizaciondeventaM')  # Field name made lowercase.
    cotizaciondeventae = models.BooleanField(db_column='cotizaciondeventaE')  # Field name made lowercase.
    cotizaciondeventai = models.BooleanField(db_column='cotizaciondeventaI')  # Field name made lowercase.
    cotizacionventamayoreoc = models.BooleanField(db_column='cotizacionventamayoreoC')  # Field name made lowercase.
    cotizacionventamayoreom = models.BooleanField(db_column='cotizacionventamayoreoM')  # Field name made lowercase.
    cotizacionventamayoreoe = models.BooleanField(db_column='cotizacionventamayoreoE')  # Field name made lowercase.
    cotizacionventamayoreoi = models.BooleanField(db_column='cotizacionventamayoreoI')  # Field name made lowercase.
    cotizacionrentac = models.BooleanField(db_column='cotizacionrentaC')  # Field name made lowercase.
    cotizacionrentam = models.BooleanField(db_column='cotizacionrentaM')  # Field name made lowercase.
    cotizacionrentae = models.BooleanField(db_column='cotizacionrentaE')  # Field name made lowercase.
    cotizacionrentai = models.BooleanField(db_column='cotizacionrentaI')  # Field name made lowercase.
    renovacionrentac = models.BooleanField(db_column='renovacionrentaC')  # Field name made lowercase.
    renovacionrentam = models.BooleanField(db_column='renovacionrentaM')  # Field name made lowercase.
    renovacionrentae = models.BooleanField(db_column='renovacionrentaE')  # Field name made lowercase.
    renovacionrentai = models.BooleanField(db_column='renovacionrentaI')  # Field name made lowercase.
    rentasc = models.BooleanField(db_column='rentasC')  # Field name made lowercase.
    rentasm = models.BooleanField(db_column='rentasM')  # Field name made lowercase.
    rentase = models.BooleanField(db_column='rentasE')  # Field name made lowercase.
    rentasi = models.BooleanField(db_column='rentasI')  # Field name made lowercase.
    salidarentasc = models.BooleanField(db_column='salidarentasC')  # Field name made lowercase.
    salidarentasm = models.BooleanField(db_column='salidarentasM')  # Field name made lowercase.
    salidarentase = models.BooleanField(db_column='salidarentasE')  # Field name made lowercase.
    salidarentasi = models.BooleanField(db_column='salidarentasI')  # Field name made lowercase.
    salidaventasc = models.BooleanField(db_column='salidaventasC')  # Field name made lowercase.
    salidaventasm = models.BooleanField(db_column='salidaventasM')  # Field name made lowercase.
    salidaventase = models.BooleanField(db_column='salidaventasE')  # Field name made lowercase.
    salidaventasi = models.BooleanField(db_column='salidaventasI')  # Field name made lowercase.
    salidareparacionc = models.BooleanField(db_column='salidareparacionC')  # Field name made lowercase.
    salidareparacionm = models.BooleanField(db_column='salidareparacionM')  # Field name made lowercase.
    salidareparacione = models.BooleanField(db_column='salidareparacionE')  # Field name made lowercase.
    salidareparacioni = models.BooleanField(db_column='salidareparacionI')  # Field name made lowercase.
    salidasc = models.BooleanField(db_column='salidasC')  # Field name made lowercase.
    salidasm = models.BooleanField(db_column='salidasM')  # Field name made lowercase.
    salidase = models.BooleanField(db_column='salidasE')  # Field name made lowercase.
    salidasi = models.BooleanField(db_column='salidasI')  # Field name made lowercase.
    traspasosc = models.BooleanField(db_column='traspasosC')  # Field name made lowercase.
    traspasosm = models.BooleanField(db_column='traspasosM')  # Field name made lowercase.
    traspasose = models.BooleanField(db_column='traspasosE')  # Field name made lowercase.
    traspasosi = models.BooleanField(db_column='traspasosI')  # Field name made lowercase.
    ventasc = models.BooleanField(db_column='ventasC')  # Field name made lowercase.
    ventasm = models.BooleanField(db_column='ventasM')  # Field name made lowercase.
    ventase = models.BooleanField(db_column='ventasE')  # Field name made lowercase.
    ventasi = models.BooleanField(db_column='ventasI')  # Field name made lowercase.
    ventasfletec = models.BooleanField(db_column='ventasfleteC')  # Field name made lowercase.
    ventasfletem = models.BooleanField(db_column='ventasfleteM')  # Field name made lowercase.
    ventasfletee = models.BooleanField(db_column='ventasfleteE')  # Field name made lowercase.
    ventasfletei = models.BooleanField(db_column='ventasfleteI')  # Field name made lowercase.
    ventasmayoreoc = models.BooleanField(db_column='ventasmayoreoC')  # Field name made lowercase.
    ventasmayoreom = models.BooleanField(db_column='ventasmayoreoM')  # Field name made lowercase.
    ventasmayoreoe = models.BooleanField(db_column='ventasmayoreoE')  # Field name made lowercase.
    ventasmayoreoi = models.BooleanField(db_column='ventasmayoreoI')  # Field name made lowercase.
    puntodeventac = models.BooleanField(db_column='puntodeventaC')  # Field name made lowercase.
    puntodeventam = models.BooleanField(db_column='puntodeventaM')  # Field name made lowercase.
    puntodeventae = models.BooleanField(db_column='puntodeventaE')  # Field name made lowercase.
    puntodeventai = models.BooleanField(db_column='puntodeventaI')  # Field name made lowercase.
    requisicionc = models.BooleanField(db_column='requisicionC')  # Field name made lowercase.
    requisicionm = models.BooleanField(db_column='requisicionM')  # Field name made lowercase.
    requisicione = models.BooleanField(db_column='requisicionE')  # Field name made lowercase.
    requisicioni = models.BooleanField(db_column='requisicionI')  # Field name made lowercase.
    reparacionc = models.BooleanField(db_column='reparacionC')  # Field name made lowercase.
    reparacionm = models.BooleanField(db_column='reparacionM')  # Field name made lowercase.
    reparacione = models.BooleanField(db_column='reparacionE')  # Field name made lowercase.
    reparacioni = models.BooleanField(db_column='reparacionI')  # Field name made lowercase.
    entregarepc = models.BooleanField(db_column='entregarepC')  # Field name made lowercase.
    entregarepm = models.BooleanField(db_column='entregarepM')  # Field name made lowercase.
    entregarepe = models.BooleanField(db_column='entregarepE')  # Field name made lowercase.
    entregarepi = models.BooleanField(db_column='entregarepI')  # Field name made lowercase.
    anticiposc = models.BooleanField(db_column='anticiposC')  # Field name made lowercase.
    anticiposm = models.BooleanField(db_column='anticiposM')  # Field name made lowercase.
    anticipose = models.BooleanField(db_column='anticiposE')  # Field name made lowercase.
    anticiposi = models.BooleanField(db_column='anticiposI')  # Field name made lowercase.
    notasdeceditoc = models.BooleanField(db_column='notasdeceditoC')  # Field name made lowercase.
    notasdeceditom = models.BooleanField(db_column='notasdeceditoM')  # Field name made lowercase.
    notasdeceditoe = models.BooleanField(db_column='notasdeceditoE')  # Field name made lowercase.
    notasdeceditoi = models.BooleanField(db_column='notasdeceditoI')  # Field name made lowercase.
    pagoclientesc = models.BooleanField(db_column='pagoclientesC')  # Field name made lowercase.
    pagoclientesm = models.BooleanField(db_column='pagoclientesM')  # Field name made lowercase.
    pagoclientese = models.BooleanField(db_column='pagoclientesE')  # Field name made lowercase.
    pagoclientesi = models.BooleanField(db_column='pagoclientesI')  # Field name made lowercase.
    cobranzaclientec = models.BooleanField(db_column='cobranzaclienteC')  # Field name made lowercase.
    cobranzaclientem = models.BooleanField(db_column='cobranzaclienteM')  # Field name made lowercase.
    cobranzaclientee = models.BooleanField(db_column='cobranzaclienteE')  # Field name made lowercase.
    cobranzaclientei = models.BooleanField(db_column='cobranzaclienteI')  # Field name made lowercase.
    nominavendedoresc = models.BooleanField(db_column='nominavendedoresC')  # Field name made lowercase.
    nominavendedoresm = models.BooleanField(db_column='nominavendedoresM')  # Field name made lowercase.
    nominavendedorese = models.BooleanField(db_column='nominavendedoresE')  # Field name made lowercase.
    nominavendedoresi = models.BooleanField(db_column='nominavendedoresI')  # Field name made lowercase.
    pagosmultiplesc = models.BooleanField(db_column='pagosmultiplesC')  # Field name made lowercase.
    pagosmultiplesm = models.BooleanField(db_column='pagosmultiplesM')  # Field name made lowercase.
    pagosmultiplese = models.BooleanField(db_column='pagosmultiplesE')  # Field name made lowercase.
    pagosmultiplesi = models.BooleanField(db_column='pagosmultiplesI')  # Field name made lowercase.
    notasdecreditoc = models.BooleanField(db_column='notasdecreditoC')  # Field name made lowercase.
    notasdecreditom = models.BooleanField(db_column='notasdecreditoM')  # Field name made lowercase.
    notasdecreditoe = models.BooleanField(db_column='notasdecreditoE')  # Field name made lowercase.
    notasdecreditoi = models.BooleanField(db_column='notasdecreditoI')  # Field name made lowercase.
    pagogastosfijosc = models.BooleanField(db_column='pagogastosfijosC')  # Field name made lowercase.
    pagogastosfijosm = models.BooleanField(db_column='pagogastosfijosM')  # Field name made lowercase.
    pagogastosfijose = models.BooleanField(db_column='pagogastosfijosE')  # Field name made lowercase.
    pagogastosfijosi = models.BooleanField(db_column='pagogastosfijosI')  # Field name made lowercase.
    pagoproveedoresc = models.BooleanField(db_column='pagoproveedoresC')  # Field name made lowercase.
    pagoproveedoresm = models.BooleanField(db_column='pagoproveedoresM')  # Field name made lowercase.
    pagoproveedorese = models.BooleanField(db_column='pagoproveedoresE')  # Field name made lowercase.
    pagoproveedoresi = models.BooleanField(db_column='pagoproveedoresI')  # Field name made lowercase.
    ventasrutasc = models.BooleanField(db_column='ventasrutasC')  # Field name made lowercase.
    ventasrutasm = models.BooleanField(db_column='ventasrutasM')  # Field name made lowercase.
    ventasrutase = models.BooleanField(db_column='ventasrutasE')  # Field name made lowercase.
    ventasrutasi = models.BooleanField(db_column='ventasrutasI')  # Field name made lowercase.
    distribuciondeclientesc = models.BooleanField(db_column='distribuciondeclientesC')  # Field name made lowercase.
    distribuciondeclientesm = models.BooleanField(db_column='distribuciondeclientesM')  # Field name made lowercase.
    distribuciondeclientese = models.BooleanField(db_column='distribuciondeclientesE')  # Field name made lowercase.
    distribuciondeclientesi = models.BooleanField(db_column='distribuciondeclientesI')  # Field name made lowercase.
    cattipoclientec = models.BooleanField()
    cattipoclientem = models.BooleanField()
    cattipoclientee = models.BooleanField()
    cattipoclientei = models.BooleanField()
    cattipogastoc = models.BooleanField()
    cattipogastom = models.BooleanField()
    cattipogastoe = models.BooleanField()
    cattipogastoi = models.BooleanField()
    catlisprec = models.BooleanField()
    catlisprem = models.BooleanField()
    catlispree = models.BooleanField()
    catlisprei = models.BooleanField()
    catclasbodc = models.BooleanField()
    catclasbodm = models.BooleanField()
    catclasbode = models.BooleanField()
    catclasbodi = models.BooleanField()
    catimpvtac = models.BooleanField()
    catimpvtam = models.BooleanField()
    catimpvtae = models.BooleanField()
    catimpvtai = models.BooleanField()
    catimpcomc = models.BooleanField()
    catimpcomm = models.BooleanField()
    catimpcome = models.BooleanField()
    catimpcomi = models.BooleanField()
    catvehiculosc = models.BooleanField()
    catvehiculosm = models.BooleanField()
    catvehiculose = models.BooleanField()
    catvehiculosi = models.BooleanField()
    modultcosto = models.BooleanField()
    modprevta = models.BooleanField()
    fechacorte = models.BooleanField()
    usercorte = models.BooleanField()
    cierresvta = models.BooleanField()
    cierredia = models.BooleanField()
    conductorc = models.BooleanField()
    conductorm = models.BooleanField()
    conductore = models.BooleanField()
    conductori = models.BooleanField()
    mecanicoc = models.BooleanField()
    mecanicom = models.BooleanField()
    mecanicoe = models.BooleanField()
    mecanicoi = models.BooleanField()
    refaccionc = models.BooleanField()
    refaccionm = models.BooleanField()
    refaccione = models.BooleanField()
    refaccioni = models.BooleanField()
    servicioc = models.BooleanField()
    serviciom = models.BooleanField()
    servicioe = models.BooleanField()
    servicioi = models.BooleanField()
    tallerc = models.BooleanField()
    tallerm = models.BooleanField()
    tallere = models.BooleanField()
    talleri = models.BooleanField()
    foliodoctos = models.BooleanField(db_column='folioDoctos')  # Field name made lowercase.
    deptos = models.BooleanField()
    secciones = models.BooleanField()
    subfam = models.BooleanField()
    lineas = models.BooleanField()
    agrupaprod = models.BooleanField()
    sucursales = models.BooleanField()
    asucursales = models.BooleanField()
    configuraciones = models.BooleanField(db_column='Configuraciones')  # Field name made lowercase.
    canventa = models.BooleanField()
    mermasc = models.BooleanField()
    promociones = models.BooleanField()
    corteparcial = models.BooleanField()
    permisos = models.BooleanField()
    reportes = models.BooleanField()
    calimpto = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Permisos'


class Permisos2(models.Model):
    usuario = models.CharField(max_length=20)
    invfisico = models.BooleanField(db_column='invFisico')  # Field name made lowercase.
    facturacli = models.BooleanField()
    facturaglobal = models.BooleanField()
    cancompra = models.BooleanField()
    canventa = models.BooleanField()
    repfacturas = models.BooleanField(db_column='repFacturas')  # Field name made lowercase.
    reimprimet = models.BooleanField()
    catproductosm = models.BooleanField()
    revisamov = models.BooleanField()
    catproductos = models.BooleanField()
    catgastoso = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Permisos2'


class Precioimportes(models.Model):
    cveuni = models.IntegerField()
    precio = models.DecimalField(max_digits=19, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'PrecioImportes'


class Presentaciones(models.Model):
    cve_presentacion = models.IntegerField(db_column='Cve_Presentacion')  # Field name made lowercase.
    des_presentacion = models.CharField(db_column='Des_Presentacion', max_length=40, blank=True, null=True)  # Field name made lowercase.
    fecha_alta = models.DateField(db_column='Fecha_Alta', blank=True, null=True)  # Field name made lowercase.
    cve_grupop = models.IntegerField(blank=True, null=True)
    id_presentacion = models.IntegerField()
    marca = models.IntegerField(db_column='Marca')  # Field name made lowercase.
    grupo_marca = models.IntegerField(db_column='Grupo_Marca')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Presentaciones'


class Promociones(models.Model):
    foliopromo = models.IntegerField()
    tipopromo = models.IntegerField()
    tipocompra = models.IntegerField()
    definepromo = models.IntegerField()
    gpoprod = models.IntegerField()
    cveprod = models.CharField(max_length=50)
    desprod = models.CharField(max_length=800)
    cantidad = models.IntegerField()
    paga = models.IntegerField()
    fijaprecio = models.DecimalField(max_digits=19, decimal_places=4)
    regala = models.IntegerField()
    gporeg = models.IntegerField()
    descunitario = models.DecimalField(max_digits=19, decimal_places=4)
    preciototal = models.DecimalField(max_digits=19, decimal_places=4)
    descripcion = models.CharField(max_length=200)
    vigencia = models.BooleanField()
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()
    vigente = models.BooleanField()
    enviado = models.BooleanField()
    fechaenvio = models.DateTimeField()
    userenvio = models.CharField(max_length=50)
    fecrea = models.DateTimeField()
    fecmod = models.DateTimeField()
    empresa = models.IntegerField()
    gpoprod2 = models.IntegerField()
    cantvta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Promociones'


class Promociones1(models.Model):
    foliopromo = models.IntegerField()
    tipopromo = models.IntegerField()
    tipocompra = models.IntegerField()
    definepromo = models.IntegerField()
    gpoprod = models.IntegerField()
    cveprod = models.CharField(max_length=50)
    desprod = models.CharField(max_length=800)
    cantidad = models.IntegerField()
    paga = models.IntegerField()
    fijaprecio = models.DecimalField(max_digits=19, decimal_places=4)
    regala = models.IntegerField()
    gporeg = models.IntegerField()
    descunitario = models.DecimalField(max_digits=19, decimal_places=4)
    preciototal = models.DecimalField(max_digits=19, decimal_places=4)
    descripcion = models.CharField(max_length=200)
    vigencia = models.BooleanField()
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()
    vigente = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Promociones1'


class Promocionesa(models.Model):
    foliopromo = models.IntegerField()
    tipopromo = models.IntegerField()
    tipocompra = models.IntegerField()
    definepromo = models.IntegerField()
    gpoprod = models.IntegerField()
    cveprod = models.CharField(max_length=50)
    desprod = models.CharField(max_length=800)
    cantidad = models.IntegerField()
    paga = models.IntegerField()
    fijaprecio = models.DecimalField(max_digits=19, decimal_places=4)
    regala = models.IntegerField()
    gporeg = models.IntegerField()
    descunitario = models.DecimalField(max_digits=19, decimal_places=4)
    preciototal = models.DecimalField(max_digits=19, decimal_places=4)
    descripcion = models.CharField(max_length=200)
    vigencia = models.BooleanField()
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()
    vigente = models.BooleanField()
    enviado = models.BooleanField()
    fechaenvio = models.DateTimeField()
    userenvio = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'PromocionesA'


class Promos(models.Model):
    empresa = models.IntegerField()
    cvepromo = models.IntegerField()
    despromo = models.CharField(max_length=100)
    cvegruposuc = models.IntegerField()
    activa = models.BooleanField()
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()
    usuario = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Promos'


class Resexiste(models.Model):
    fechadiar = models.DateField()
    realizado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'RESEXISTE'


class Razonexclusividad(models.Model):
    cve_razexclu = models.IntegerField(db_column='Cve_RazExclu')  # Field name made lowercase.
    des_razexclu = models.CharField(db_column='Des_RazExclu', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RazonExclusividad'


class Recargasrutas(models.Model):
    index_rut = models.IntegerField()
    index_alm = models.IntegerField()
    fecha = models.DateTimeField()
    cantidad = models.IntegerField()
    pro_codigo = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'RecargasRutas'


class Retirosptovta(models.Model):
    folret = models.IntegerField()
    usuario = models.CharField(max_length=20)
    fecharetiro = models.DateTimeField()
    montoretiro = models.DecimalField(max_digits=19, decimal_places=4)
    impreal = models.DecimalField(max_digits=19, decimal_places=4)
    diferencia = models.DecimalField(db_column='Diferencia', max_digits=19, decimal_places=4)  # Field name made lowercase.
    empresa = models.IntegerField()
    sercierre = models.CharField(max_length=10)
    folcierre = models.IntegerField()
    almacen = models.IntegerField()
    turno = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Retirosptovta'


class Rutas(models.Model):
    index_rut = models.FloatField(db_column='Index_rut')  # Field name made lowercase.
    index_suc = models.FloatField(db_column='Index_suc')  # Field name made lowercase.
    usuario = models.CharField(max_length=50)
    fecha_usu = models.DateTimeField(db_column='FECHA_USU')  # Field name made lowercase.
    descripcion_rut = models.CharField(db_column='Descripcion_rut', max_length=200, blank=True, null=True)  # Field name made lowercase.
    vendedor = models.CharField(max_length=100, blank=True, null=True)
    tabla_comision = models.FloatField(blank=True, null=True)
    index_alm = models.FloatField(blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True)
    tipocorte = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Rutas'


class Serfoldoc(models.Model):
    cvedocto = models.IntegerField()
    desdoc = models.CharField(db_column='Desdoc', max_length=50)  # Field name made lowercase.
    serdoc = models.CharField(db_column='Serdoc', max_length=5)  # Field name made lowercase.
    foldoc = models.IntegerField(db_column='Foldoc')  # Field name made lowercase.
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'SerFolDoc'


class TablasBonificaciones(models.Model):
    index_bon = models.IntegerField()
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pro_codigo = models.CharField(db_column='Pro_codigo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tipo = models.FloatField(blank=True, null=True)
    monto = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Tablas_bonificaciones'


class Tipocalle(models.Model):
    cve_tipcalle = models.IntegerField(db_column='Cve_TipCalle')  # Field name made lowercase.
    des_tipocalle = models.CharField(db_column='Des_TipoCalle', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoCalle'


class Tipopromo(models.Model):
    tipopromo = models.IntegerField()
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    activa = models.BooleanField()
    fechacreacion = models.DateTimeField()
    usuario = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'TipoPromo'


class Tipozona(models.Model):
    cve_tipzon = models.IntegerField(db_column='Cve_TipZon')  # Field name made lowercase.
    des_tipzon = models.CharField(db_column='Des_TipZon', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoZona'


class Tiposmov(models.Model):
    cvetipo = models.IntegerField()
    destipo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'TiposMov'


class Users(models.Model):
    login = models.CharField(db_column='LOGIN', max_length=20)  # Field name made lowercase.
    pass_field = models.CharField(db_column='PASS', max_length=20)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    nombre = models.CharField(db_column='NOMBRE', max_length=80)  # Field name made lowercase.
    puesto = models.CharField(db_column='PUESTO', max_length=80)  # Field name made lowercase.
    cvegrup = models.CharField(db_column='CVEGRUP', max_length=15)  # Field name made lowercase.
    change = models.BooleanField(db_column='CHANGE')  # Field name made lowercase.
    foto = models.CharField(db_column='FOTO', max_length=100)  # Field name made lowercase.
    fechareal = models.DateTimeField(db_column='FECHAREAL')  # Field name made lowercase.
    cveven = models.IntegerField(db_column='CVEVEN')  # Field name made lowercase.
    movcom = models.IntegerField(db_column='MovCom')  # Field name made lowercase.
    movdevcom = models.IntegerField(db_column='MovDevCom')  # Field name made lowercase.
    movdevren = models.IntegerField(db_column='MovDevRen')  # Field name made lowercase.
    movdevven = models.IntegerField(db_column='MovDevVen')  # Field name made lowercase.
    movent = models.IntegerField(db_column='MovEnt')  # Field name made lowercase.
    movfac = models.IntegerField(db_column='MovFac')  # Field name made lowercase.
    movren = models.IntegerField(db_column='MovRen')  # Field name made lowercase.
    movsal = models.IntegerField(db_column='MovSal')  # Field name made lowercase.
    movtra = models.IntegerField(db_column='MovTra')  # Field name made lowercase.
    movven = models.IntegerField(db_column='MovVen')  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=2)  # Field name made lowercase.
    cvebod = models.IntegerField(db_column='CveBod')  # Field name made lowercase.
    movrep = models.IntegerField(db_column='MovRep')  # Field name made lowercase.
    restcvebod = models.BooleanField(db_column='RestCveBod')  # Field name made lowercase.
    restcvemov = models.BooleanField(db_column='RestCveMov')  # Field name made lowercase.
    restsermov = models.BooleanField(db_column='RestSerMov')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERS'


class Usuarios(models.Model):
    empleado = models.CharField(max_length=50)
    nivel = models.CharField(max_length=9)
    password_empleado = models.CharField(max_length=20)
    nombre_empleado = models.CharField(max_length=80)
    perfil = models.IntegerField()
    puesto = models.CharField(max_length=50)
    vendedor = models.IntegerField()
    comer = models.BooleanField()
    evento = models.BooleanField()
    hielo = models.BooleanField()
    rarras = models.BooleanField()
    cambiapass = models.BooleanField()
    index_rut = models.IntegerField()
    correo = models.CharField(max_length=80)
    pwscorreo = models.CharField(max_length=50)
    tipocorreo = models.IntegerField()
    smtpcorreo = models.CharField(max_length=50)
    puertocorreo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Usuarios'


class Android2017(models.Model):
    id_venta = models.IntegerField()
    folio = models.CharField(max_length=50, blank=True, null=True)
    ruta = models.CharField(max_length=50, blank=True, null=True)
    index_cli = models.CharField(max_length=50, blank=True, null=True)
    pro_codigo = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    monto = models.CharField(max_length=50, blank=True, null=True)
    factura = models.CharField(max_length=50, blank=True, null=True)
    credito = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'android_2017'


class Aumentos(models.Model):
    clienteid = models.IntegerField()
    importeorig = models.FloatField()
    importenuevo = models.FloatField()
    porcaumento = models.FloatField()
    fecha = models.DateTimeField()
    ruta = models.IntegerField()
    fechareal = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'aumentos'


class CClaveprodserv(models.Model):
    c_claveprodserv = models.CharField(db_column='c_ClaveProdServ', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_ClaveProdServ'


class CClaveunidad(models.Model):
    id_unidad = models.CharField(max_length=50)
    c_claveunidad = models.CharField(db_column='c_ClaveUnidad', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_ClaveUnidad'


class CCodigopostal(models.Model):
    c_codigopostal = models.CharField(db_column='c_CodigoPostal', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_estado = models.CharField(db_column='c_Estado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_municipio = models.CharField(db_column='c_Municipio', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_localidad = models.CharField(db_column='c_Localidad', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_CodigoPostal'


class CImpuesto(models.Model):
    c_impuesto = models.CharField(db_column='c_Impuesto', max_length=5)  # Field name made lowercase.
    descripcion = models.CharField(max_length=10, blank=True, null=True)
    retencion = models.BooleanField(blank=True, null=True)
    traslado = models.BooleanField(blank=True, null=True)
    local_federal = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_Impuesto'


class CMetodopago(models.Model):
    c_metodopago = models.CharField(db_column='c_MetodoPago', max_length=10)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_MetodoPago'


class CMoneda(models.Model):
    c_moneda = models.CharField(db_column='c_Moneda', max_length=10, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    decimales = models.CharField(max_length=50, blank=True, null=True)
    porcentaje_vaciacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_Moneda'


class CPais(models.Model):
    c_pais = models.CharField(db_column='c_Pais', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_Pais'


class CRegimenfiscal(models.Model):
    c_regimenfiscal = models.CharField(db_column='c_RegimenFiscal', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    fisica = models.BooleanField(blank=True, null=True)
    moral = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_RegimenFiscal'


class CTipofactor(models.Model):
    id_tipo = models.IntegerField()
    c_tipofactor = models.CharField(db_column='c_TipoFactor', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_TipoFactor'


class CTiporelacion(models.Model):
    c_tiporelacion = models.CharField(db_column='c_TipoRelacion', max_length=10, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'c_TipoRelacion'


class CUsocfdi(models.Model):
    c_usocfdi = models.CharField(db_column='c_UsoCFDI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=400, blank=True, null=True)
    fisica = models.BooleanField(blank=True, null=True)
    moral = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_UsoCFDI'


class CFormapago(models.Model):
    c_formapago = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_formapago'


class Cargadatcat(models.Model):
    numref = models.CharField(max_length=50)
    desprod = models.CharField(max_length=800)
    cvedepto = models.IntegerField()
    cveseccion = models.IntegerField()
    numref2 = models.TextField()

    class Meta:
        managed = False
        db_table = 'cargadatcat'


class Catmecanicos(models.Model):
    empresa = models.IntegerField()
    cvemecanico = models.IntegerField()
    nommecanico = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    contacto = models.CharField(max_length=50)
    login = models.CharField(max_length=15)
    fechareg = models.DateTimeField()
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'catMecanicos'


class Catsucursales(models.Model):
    cveempresa = models.IntegerField()
    nomempresa = models.CharField(max_length=100)
    activa = models.BooleanField()
    servidor = models.CharField(max_length=50)
    nombase = models.CharField(max_length=50)
    nomuser = models.CharField(max_length=50)
    pass_field = models.CharField(db_column='pass', max_length=50)  # Field renamed because it was a Python reserved word.
    usuario = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'catSucursales'


class Catimpuestosc(models.Model):
    cveimptc = models.IntegerField()
    desimptc = models.CharField(max_length=80)
    porcivac = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps1c = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps2c = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps3c = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps4c = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps5c = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps6c = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps7c = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps8c = models.DecimalField(max_digits=18, decimal_places=6)
    activoc = models.BooleanField()
    empresa = models.IntegerField()
    tipoimp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catimpuestosc'


class Catimpuestosc88(models.Model):
    cveimptc = models.IntegerField()
    desimptc = models.CharField(max_length=80)
    porcivac = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps1c = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps2c = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps3c = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps4c = models.DecimalField(max_digits=19, decimal_places=4)
    activoc = models.BooleanField()
    empresa = models.IntegerField()
    tipoimp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catimpuestosc88'


class Catimpuestosv(models.Model):
    cveimptv = models.IntegerField()
    desimptv = models.CharField(max_length=80)
    cveimptoivav = models.CharField(max_length=5)
    descveimptoivav = models.CharField(max_length=10)
    cvetipofactorivav = models.CharField(max_length=2)
    descvetipofactorivav = models.CharField(max_length=10)
    porcimptoivasat = models.DecimalField(max_digits=18, decimal_places=6)
    porcivav = models.DecimalField(max_digits=18, decimal_places=6)
    cveimptoieps1v = models.CharField(max_length=5)
    descveimptoieps1v = models.CharField(max_length=10)
    cvetipofactorieps1v = models.CharField(max_length=2)
    descvetipofactorieps1v = models.CharField(max_length=10)
    porcimptoieps1satv = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps1v = models.DecimalField(max_digits=19, decimal_places=4)
    cveimptoieps2v = models.CharField(max_length=5)
    descveimptoieps2v = models.CharField(max_length=10)
    cvetipofactorieps2v = models.CharField(max_length=2)
    descvetipofactorieps2v = models.CharField(max_length=10)
    porcimptoieps2satv = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps2v = models.DecimalField(max_digits=19, decimal_places=4)
    cveimptoieps3v = models.CharField(max_length=5)
    descveimptoieps3v = models.CharField(max_length=10)
    cvetipofactorieps3v = models.CharField(max_length=2)
    descvetipofactorieps3v = models.CharField(max_length=10)
    porcimptoieps3satv = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps3v = models.DecimalField(max_digits=19, decimal_places=4)
    cveimptoieps4v = models.CharField(max_length=5)
    descveimptoieps4v = models.CharField(max_length=10)
    cvetipofactorieps4v = models.CharField(max_length=2)
    descvetipofactorieps4v = models.CharField(max_length=10)
    porcimptoieps4satv = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps4v = models.DecimalField(max_digits=19, decimal_places=4)
    cveimptoieps5v = models.CharField(max_length=5)
    descveimptoieps5v = models.CharField(max_length=10)
    cvetipofactorieps5v = models.CharField(max_length=2)
    descvetipofactorieps5v = models.CharField(max_length=10)
    porcimptoieps5satv = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps5v = models.DecimalField(max_digits=19, decimal_places=4)
    cveimptoieps6v = models.CharField(max_length=5)
    descveimptoieps6v = models.CharField(max_length=10)
    cvetipofactorieps6v = models.CharField(max_length=2)
    descvetipofactorieps6v = models.CharField(max_length=10)
    porcimptoieps6satv = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps6v = models.DecimalField(max_digits=19, decimal_places=4)
    cveimptoieps7v = models.CharField(max_length=5)
    descveimptoieps7v = models.CharField(max_length=10)
    cvetipofactorieps7v = models.CharField(max_length=2)
    descvetipofactorieps7v = models.CharField(max_length=10)
    porcimptoieps7satv = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps7v = models.DecimalField(max_digits=19, decimal_places=4)
    cveimptoieps8v = models.CharField(max_length=5)
    descveimptoieps8v = models.CharField(max_length=10)
    cvetipofactorieps8v = models.CharField(max_length=2)
    descvetipofactorieps8v = models.CharField(max_length=10)
    porcimptoieps8satv = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps8v = models.DecimalField(max_digits=19, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catimpuestosv'


class Catimpuestosv88(models.Model):
    cveimptv = models.IntegerField()
    desimptv = models.CharField(max_length=80)
    cveimptoivav = models.CharField(max_length=5)
    descveimptoivav = models.CharField(max_length=10)
    cvetipofactorivav = models.CharField(max_length=2)
    descvetipofactorivav = models.CharField(max_length=10)
    porcimptoivasat = models.DecimalField(max_digits=18, decimal_places=6)
    porcivav = models.DecimalField(max_digits=19, decimal_places=4)
    cveimptoieps1v = models.CharField(max_length=5)
    descveimptoieps1v = models.CharField(max_length=10)
    cvetipofactorieps1v = models.CharField(max_length=2)
    descvetipofactorieps1v = models.CharField(max_length=10)
    porcimptoieps1satv = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps1v = models.DecimalField(max_digits=19, decimal_places=4)
    cveimptoieps2v = models.CharField(max_length=5)
    descveimptoieps2v = models.CharField(max_length=10)
    cvetipofactorieps2v = models.CharField(max_length=2)
    descvetipofactorieps2v = models.CharField(max_length=10)
    porcimptoieps2satv = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps2v = models.DecimalField(max_digits=19, decimal_places=4)
    cveimptoieps3v = models.CharField(max_length=5)
    descveimptoieps3v = models.CharField(max_length=10)
    cvetipofactorieps3v = models.CharField(max_length=2)
    descvetipofactorieps3v = models.CharField(max_length=10)
    porcimptoieps3satv = models.DecimalField(max_digits=18, decimal_places=6)
    porcieps3v = models.DecimalField(max_digits=19, decimal_places=4)
    cveimptoieps4v = models.CharField(max_length=5)
    descveimptoieps4v = models.CharField(max_length=10)
    cvetipofactorieps4v = models.CharField(max_length=2)
    descvetipofactorieps4v = models.CharField(max_length=10)
    porcimptoieps4satv = models.DecimalField(max_digits=19, decimal_places=4)
    porcieps4v = models.DecimalField(max_digits=19, decimal_places=4)
    activov = models.BooleanField()
    empresa = models.IntegerField()
    tipoimp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catimpuestosv88'


class Catprodeje(models.Model):
    referencia = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    ucosto = models.DecimalField(max_digits=19, decimal_places=4)
    pcosto = models.DecimalField(max_digits=19, decimal_places=4)
    imptoc = models.IntegerField()
    imptov = models.IntegerField()
    cveprodserv = models.CharField(max_length=10)
    unidad = models.CharField(max_length=5)
    existencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catprodeje'


class Cattipogasto(models.Model):
    cvetipo = models.IntegerField()
    destipo = models.CharField(max_length=50)
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cattipogasto'


class Clisubotexx(models.Model):
    cvereparto = models.IntegerField()
    cvepreventa = models.IntegerField()
    index_cli = models.CharField(max_length=20)
    razonsocial_cli = models.CharField(max_length=500)
    nom_cliente = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'clisubotexx'


class Detmovcomodato(models.Model):
    empresa = models.IntegerField(db_column='Empresa')  # Field name made lowercase.
    seriec = models.CharField(max_length=3)
    folioc = models.IntegerField()
    seriemov = models.CharField(max_length=3)
    foliomov = models.IntegerField()
    tipomov = models.IntegerField()
    index_rut = models.IntegerField()
    codigo_mueble = models.IntegerField()
    desc_mueble = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    activo = models.BooleanField()
    cancelado = models.BooleanField()
    comodatado = models.BooleanField()
    marca = models.CharField(max_length=25)
    modelo = models.CharField(max_length=25)
    serie = models.CharField(max_length=30)
    consecutivo = models.CharField(max_length=15)
    codigoe_enfriador = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'detmovcomodato'


class Entidad(models.Model):
    cve_ent = models.CharField(max_length=3, blank=True, null=True)
    nom_ent = models.CharField(max_length=100, blank=True, null=True)
    nom_abr = models.CharField(max_length=10, blank=True, null=True)
    cve_pais = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entidad'


class FoliosDoctos(models.Model):
    clave_docto = models.IntegerField()
    descripcion_docto = models.CharField(db_column='Descripcion_docto', max_length=50)  # Field name made lowercase.
    serie_docto = models.CharField(max_length=10)
    folio_docto = models.IntegerField()
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'folios_doctos'


class Gruposempresas(models.Model):
    cvegrupoemp = models.IntegerField()
    nomgruppoemp = models.CharField(max_length=100)
    activo = models.BooleanField()
    usuario = models.CharField(max_length=10)
    fechacreacion = models.DateTimeField()
    empresa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gruposempresas'


class Invfisicomovil(models.Model):
    cveprod = models.CharField(max_length=20)
    desprod = models.CharField(max_length=800)
    existe = models.IntegerField()
    existe_fisica = models.IntegerField()
    diferencia = models.IntegerField()
    costo = models.DecimalField(max_digits=19, decimal_places=4)
    costototal = models.DecimalField(max_digits=19, decimal_places=4)
    cvemov = models.IntegerField()
    desccmov = models.CharField(max_length=50)
    folmov = models.IntegerField()
    observacion = models.CharField(max_length=50)
    usuario = models.CharField(max_length=15)
    fechacreacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'invfisicomovil'


class Invfisicos(models.Model):
    folio_inventario = models.IntegerField()
    empresa = models.IntegerField(db_column='Empresa')  # Field name made lowercase.
    bodega = models.IntegerField()
    cveprod = models.CharField(max_length=20)
    existe_sistema = models.IntegerField()
    existe_fisico = models.IntegerField()
    diferencia = models.IntegerField()
    costo = models.DecimalField(max_digits=19, decimal_places=4)
    costo_total = models.DecimalField(max_digits=19, decimal_places=4)
    usuario = models.CharField(max_length=15)
    fecha_inventario = models.DateTimeField()
    cvemov = models.IntegerField()
    descmov = models.CharField(max_length=25)
    folmov = models.IntegerField()
    observacion = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'invfisicos'


class Mgcli(models.Model):
    index_cli = models.CharField(db_column='Index_cli', max_length=20)  # Field name made lowercase.
    index_suc = models.FloatField(db_column='Index_suc')  # Field name made lowercase.
    index_clas1 = models.IntegerField(blank=True, null=True)
    usuario = models.CharField(max_length=50)
    fecha_usu = models.DateTimeField(db_column='FECHA_USU')  # Field name made lowercase.
    index_est = models.IntegerField(db_column='index_EST', blank=True, null=True)  # Field name made lowercase.
    index_est_env = models.IntegerField(db_column='index_EST_env', blank=True, null=True)  # Field name made lowercase.
    index_mun = models.IntegerField(blank=True, null=True)
    index_mun_env = models.IntegerField(blank=True, null=True)
    index_pais = models.IntegerField(blank=True, null=True)
    index_clas2 = models.IntegerField(blank=True, null=True)
    index_env = models.IntegerField(blank=True, null=True)
    index_grupocomision = models.IntegerField(blank=True, null=True)
    razonsocial_cli = models.CharField(db_column='Razonsocial_cli', max_length=200, blank=True, null=True)  # Field name made lowercase.
    index_ciu = models.IntegerField(blank=True, null=True)
    index_ciu_env = models.IntegerField(blank=True, null=True)
    direccion_cli = models.CharField(db_column='Direccion_cli', max_length=250, blank=True, null=True)  # Field name made lowercase.
    index_grupdes = models.IntegerField(blank=True, null=True)
    direccion_cli_env = models.CharField(db_column='Direccion_cli_env', max_length=250, blank=True, null=True)  # Field name made lowercase.
    atiende = models.CharField(db_column='Atiende', max_length=100, blank=True, null=True)  # Field name made lowercase.
    atiende_env = models.CharField(db_column='Atiende_env', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rfc_cli = models.CharField(db_column='RFC_cli', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefono_cli = models.CharField(max_length=100, blank=True, null=True)
    telefono_cli_env = models.CharField(max_length=100, blank=True, null=True)
    saldo_cli = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    clas = models.CharField(db_column='CLAS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    index_cadena = models.FloatField(blank=True, null=True)
    nombrecomercial_env = models.CharField(max_length=100, blank=True, null=True)
    index_clas = models.FloatField(blank=True, null=True)
    cta_contable = models.CharField(max_length=30, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)
    index_rut = models.FloatField(blank=True, null=True)
    estatus = models.FloatField(blank=True, null=True)
    plazo_cli = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    limitecredito_cli = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    nombre_comercial = models.CharField(db_column='Nombre_Comercial', max_length=200, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=150, blank=True, null=True)
    email_env = models.CharField(max_length=30, blank=True, null=True)
    curp = models.CharField(max_length=20, blank=True, null=True)
    documentos = models.CharField(max_length=100, blank=True, null=True)
    dueño_empresa = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    cp_env = models.CharField(max_length=5, blank=True, null=True)
    mayor_un_credito = models.FloatField(blank=True, null=True)
    sucursal = models.CharField(max_length=100, blank=True, null=True)
    cobra_ruta = models.FloatField(blank=True, null=True)
    colonia_cli = models.CharField(max_length=100, blank=True, null=True)
    colonia_cli_env = models.CharField(max_length=100, blank=True, null=True)
    ultima_compra = models.DateTimeField(blank=True, null=True)
    horario_venta = models.CharField(max_length=150, blank=True, null=True)
    periodo = models.FloatField(blank=True, null=True)
    lu = models.FloatField(blank=True, null=True)
    ma = models.FloatField(blank=True, null=True)
    mi = models.FloatField(blank=True, null=True)
    ju = models.FloatField(blank=True, null=True)
    vi = models.FloatField(blank=True, null=True)
    sa = models.FloatField(blank=True, null=True)
    do = models.FloatField(blank=True, null=True)
    index_cli_sec = models.FloatField(blank=True, null=True)
    facturas_vencidad = models.FloatField(blank=True, null=True)
    facturas_vencidas = models.FloatField(blank=True, null=True)
    dias_apartados = models.FloatField(blank=True, null=True)
    dias_apartado = models.FloatField(blank=True, null=True)
    lineas = models.FloatField(blank=True, null=True)
    envio_mismo_fiscal = models.FloatField(blank=True, null=True)
    eventual = models.BooleanField(blank=True, null=True)
    pronto_pago = models.FloatField(blank=True, null=True)
    apartado_cotizacion = models.FloatField(blank=True, null=True)
    aparta_cotizacion = models.FloatField(blank=True, null=True)
    genera_flete = models.FloatField(blank=True, null=True)
    index_poliza = models.CharField(max_length=50, blank=True, null=True)
    direccion_envio = models.CharField(max_length=250, blank=True, null=True)
    index_pais_env = models.FloatField(blank=True, null=True)
    entre_calles = models.CharField(max_length=200, blank=True, null=True)
    formato_factura = models.CharField(max_length=100, blank=True, null=True)
    codigo_proveedor = models.CharField(max_length=100, blank=True, null=True)
    lun_rev = models.FloatField(blank=True, null=True)
    mar_rev = models.FloatField(blank=True, null=True)
    min_rev = models.FloatField(blank=True, null=True)
    jue_rev = models.FloatField(blank=True, null=True)
    vie_rev = models.FloatField(blank=True, null=True)
    sab_rev = models.FloatField(blank=True, null=True)
    dom_rev = models.FloatField(blank=True, null=True)
    lun_cob = models.FloatField(blank=True, null=True)
    mar_cob = models.FloatField(blank=True, null=True)
    min_cob = models.FloatField(blank=True, null=True)
    jue_cob = models.FloatField(blank=True, null=True)
    vie_cob = models.FloatField(blank=True, null=True)
    sab_cob = models.FloatField(blank=True, null=True)
    dom_cob = models.FloatField(blank=True, null=True)
    lu_rev = models.FloatField(blank=True, null=True)
    ma_rev = models.FloatField(blank=True, null=True)
    mi_rev = models.FloatField(blank=True, null=True)
    ju_rev = models.FloatField(blank=True, null=True)
    vi_rev = models.FloatField(blank=True, null=True)
    sa_rev = models.FloatField(blank=True, null=True)
    do_rev = models.FloatField(blank=True, null=True)
    lu_cob = models.FloatField(blank=True, null=True)
    ma_cob = models.FloatField(blank=True, null=True)
    mi_cob = models.FloatField(blank=True, null=True)
    ju_cob = models.FloatField(blank=True, null=True)
    vi_cob = models.FloatField(blank=True, null=True)
    sa_cob = models.FloatField(blank=True, null=True)
    do_cob = models.FloatField(blank=True, null=True)
    horario_revision = models.CharField(max_length=200, blank=True, null=True)
    dom = models.FloatField(blank=True, null=True)
    horario_cobranza = models.CharField(max_length=200, blank=True, null=True)
    dv = models.CharField(max_length=20, blank=True, null=True)
    captura1 = models.CharField(max_length=50, blank=True, null=True)
    captura2 = models.CharField(max_length=50, blank=True, null=True)
    captura3 = models.CharField(max_length=50, blank=True, null=True)
    configurable1 = models.CharField(max_length=50, blank=True, null=True)
    configurable2 = models.CharField(max_length=50, blank=True, null=True)
    configurable3 = models.CharField(max_length=50, blank=True, null=True)
    ultimo_mantenimiento = models.DateTimeField(blank=True, null=True)
    ultima_venta = models.DateTimeField(blank=True, null=True)
    ultima_visita = models.DateTimeField(blank=True, null=True)
    no_exterior = models.CharField(max_length=100, blank=True, null=True)
    no_interior = models.CharField(max_length=100, blank=True, null=True)
    configurable4 = models.CharField(max_length=50, blank=True, null=True)
    cant_comprada = models.IntegerField(db_column='CANT_COMPRADA', blank=True, null=True)  # Field name made lowercase.
    compra_promedio = models.IntegerField(db_column='COMPRA_PROMEDIO', blank=True, null=True)  # Field name made lowercase.
    cuentaincobrable = models.BooleanField(db_column='Cuentaincobrable')  # Field name made lowercase.
    cant_incobrable = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    exclusivo = models.BooleanField(blank=True, null=True)
    c_exclusivo = models.CharField(max_length=150, blank=True, null=True)
    fechaini_exc = models.DateTimeField(blank=True, null=True)
    fechafin_exc = models.DateTimeField(blank=True, null=True)
    notaretenida = models.BooleanField(blank=True, null=True)
    demandado = models.BooleanField(blank=True, null=True)
    fecha_demanda = models.DateTimeField(blank=True, null=True)
    comentario_demanda = models.TextField(blank=True, null=True)  # This field type is a guess.
    facturacfdi = models.SmallIntegerField(blank=True, null=True)
    metododepago = models.CharField(max_length=50, blank=True, null=True)
    nocuenta = models.CharField(db_column='NoCuenta', max_length=15, blank=True, null=True)  # Field name made lowercase.
    condicion = models.CharField(db_column='Condicion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rfc_fac = models.CharField(db_column='RFC_fac', max_length=50, blank=True, null=True)  # Field name made lowercase.
    razonsocial_cli_fac = models.CharField(db_column='Razonsocial_cli_fac', max_length=200, blank=True, null=True)  # Field name made lowercase.
    direccion_cli_fac = models.CharField(max_length=250, blank=True, null=True)
    no_exterior_fac = models.CharField(max_length=50, blank=True, null=True)
    colonia_cli_fac = models.CharField(max_length=100, blank=True, null=True)
    index_ciu_fac = models.IntegerField(blank=True, null=True)
    index_mun_fac = models.IntegerField(blank=True, null=True)
    index_est_fac = models.IntegerField(blank=True, null=True)
    cp_fac = models.CharField(max_length=5, blank=True, null=True)
    email_fac = models.CharField(max_length=150, blank=True, null=True)
    tipocliente = models.SmallIntegerField(blank=True, null=True)
    nombrecomercial_neg = models.CharField(max_length=200, blank=True, null=True)
    direccion_cli_neg = models.CharField(max_length=250, blank=True, null=True)
    no_exterior_neg = models.CharField(max_length=50, blank=True, null=True)
    colonia_cli_neg = models.CharField(max_length=100, blank=True, null=True)
    index_ciu_neg = models.IntegerField(blank=True, null=True)
    index_mun_neg = models.IntegerField(blank=True, null=True)
    index_est_neg = models.IntegerField(blank=True, null=True)
    fecha_baja = models.DateTimeField(blank=True, null=True)
    juridico = models.BooleanField(blank=True, null=True)
    fecha_juridico = models.DateTimeField(blank=True, null=True)
    comentario_juridico = models.TextField(blank=True, null=True)  # This field type is a guess.
    pagotransferencia = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgcli'


class MgcproActivos(models.Model):
    pro_codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    estado = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mgcpro_activos'


class Movcomodato(models.Model):
    empresa = models.IntegerField(db_column='Empresa')  # Field name made lowercase.
    seriec = models.CharField(db_column='Seriec', max_length=3)  # Field name made lowercase.
    folioc = models.IntegerField(db_column='Folioc')  # Field name made lowercase.
    seriemov = models.CharField(db_column='Seriemov', max_length=3)  # Field name made lowercase.
    foliomov = models.IntegerField(db_column='FolioMov')  # Field name made lowercase.
    tipomov = models.IntegerField(db_column='Tipomov')  # Field name made lowercase.
    fechamov = models.DateTimeField()
    cvecli = models.CharField(max_length=10)
    index_ruta = models.IntegerField()
    desc_ruta = models.CharField(max_length=10)
    cveven = models.IntegerField()
    observacion = models.CharField(max_length=100)
    ref1 = models.CharField(max_length=100)
    ref2 = models.CharField(max_length=100)
    activo = models.BooleanField()
    cancelado = models.BooleanField()
    comodatado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'movcomodato'


class Municipio(models.Model):
    cve_ent = models.IntegerField(blank=True, null=True)
    cve_mun = models.CharField(max_length=5, blank=True, null=True)
    nom_mun = models.CharField(max_length=100, blank=True, null=True)
    cve_cab = models.CharField(max_length=5, blank=True, null=True)
    nom_cab = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipio'


class Productos(models.Model):
    pro_codigo = models.CharField(db_column='Pro_codigo', max_length=20)  # Field name made lowercase.
    usuario = models.CharField(max_length=50)
    fecha_usu = models.DateTimeField(db_column='FECHA_USU')  # Field name made lowercase.
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    unidadcontrol = models.CharField(max_length=20, blank=True, null=True)
    index_moneda = models.IntegerField(blank=True, null=True)
    index_clas1 = models.FloatField(blank=True, null=True)
    index_clas2 = models.FloatField(blank=True, null=True)
    index_clas3 = models.FloatField(blank=True, null=True)
    minimo = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    noserie = models.FloatField(blank=True, null=True)
    montobonifica = models.FloatField(blank=True, null=True)
    maximo = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    margen = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ultimafechaventa = models.DateTimeField(blank=True, null=True)
    ultimafechamov = models.DateTimeField(blank=True, null=True)
    pedido = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tipoarticulos = models.FloatField(blank=True, null=True)
    produccion = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    garantia = models.FloatField(blank=True, null=True)
    costeo = models.FloatField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    pzaxcaja = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    prov_index = models.FloatField()
    tipo = models.FloatField(blank=True, null=True)
    forma = models.FloatField(blank=True, null=True)
    costopromedio = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    unidadadicional = models.FloatField(blank=True, null=True)
    imp1 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    preciofraccion = models.FloatField(blank=True, null=True)
    precio1 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    precio2 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    precio3 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    precio4 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    min1 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    min2 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    min3 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    min4 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    ultimocosto = models.FloatField(blank=True, null=True)
    desc_corta = models.CharField(max_length=20, blank=True, null=True)
    codigo_envase = models.CharField(max_length=20, blank=True, null=True)
    tarima = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    peso = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    envase = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tarima2 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tarima3 = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fraccion_entero = models.FloatField(blank=True, null=True)
    codigo_suelto = models.CharField(max_length=20, blank=True, null=True)
    codigo_barras = models.CharField(max_length=20, blank=True, null=True)
    costoestandar = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    prov_alterno = models.FloatField(blank=True, null=True)
    omite_pedimento = models.FloatField(blank=True, null=True)
    foto = models.BinaryField(blank=True, null=True)
    descripcion_foto = models.TextField(blank=True, null=True)
    cta_contable = models.CharField(max_length=50, blank=True, null=True)
    estatus = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'productos'


class TiposMovimientosMuebles(models.Model):
    index_mov = models.IntegerField()
    descripcion_mov = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.FloatField(blank=True, null=True)
    movimiento_alta = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_movimientos_muebles'


class UbicacionClientes(models.Model):
    id_ubicacion = models.IntegerField()
    index_cli = models.CharField(max_length=50, blank=True, null=True)
    latitud = models.CharField(max_length=50, blank=True, null=True)
    longitud = models.CharField(max_length=50, blank=True, null=True)
    tipo_cliente = models.CharField(max_length=50, blank=True, null=True)
    descripcion_ruta = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ubicacion_clientes'


class VisitaClientes(models.Model):
    id_visita = models.IntegerField()
    index_cli = models.CharField(max_length=50, blank=True, null=True)
    latitud = models.CharField(max_length=50, blank=True, null=True)
    longitud = models.CharField(max_length=50, blank=True, null=True)
    tipo_cliente = models.CharField(max_length=50, blank=True, null=True)
    descripcion_ruta = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visita_clientes'

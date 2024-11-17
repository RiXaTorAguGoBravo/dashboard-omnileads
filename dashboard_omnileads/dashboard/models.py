from django.db import models


class OmnileadsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using('omnileads')
    
    def using_omnileads(self):
        return self.get_queryset()
    

class ReportesAppLlamadalog(models.Model):
    time = models.DateTimeField()
    callid = models.CharField()
    campana = models.ForeignKey('OminicontactoAppCampana', on_delete=models.DO_NOTHING)
    event = models.CharField()
    numero_marcado = models.CharField()

    objects = OmnileadsManager()

    class Meta:
        managed = False
        db_table = 'reportes_app_llamadalog'


class OminicontactoAppCampana(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField()

    objects = OmnileadsManager()

    class Meta:
        managed = False
        db_table = 'ominicontacto_app_campana'


class OminicontactoAppCampanaSupervisors(models.Model):
    campana = models.ForeignKey('OminicontactoAppCampana', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('OminicontactoAppUser', on_delete=models.DO_NOTHING)

    objects = OmnileadsManager()

    class Meta:
        managed = False
        db_table = 'ominicontacto_app_campana_supervisors'


class OminicontactoAppAgenteprofile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField('OminicontactoAppUser', on_delete=models.DO_NOTHING)

    objects = OmnileadsManager()

    class Meta:
        managed = False
        db_table = 'ominicontacto_app_agenteprofile'


class OminicontactoAppUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField()
    email = models.CharField()

    objects = OmnileadsManager()

    class Meta:
        managed = False
        db_table = 'ominicontacto_app_user'

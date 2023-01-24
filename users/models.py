from django.db import models
import datetime

# Create your models here.


class User(models.Model):
    # Campos con modo verboso
    # Se pueden poner en minusculas ya que Django se encarga de
    # darles la correcta ortografia
    first_name = models.CharField('nombre', max_length=30)
    last_name = models.CharField('apellido', max_length=50)
    # Si se pone Car sin comillas da error porque
    # la clase Car esta definida despues que la de User
    # por eso hay que ponerla con comillas
    # Para establecer una relacion ManyToMany
    cars = models.ManyToManyField('Car', verbose_name='carros del usuario')

    # Definir propiedades para un objeto
    @property
    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'

    # Para especificar como queremos que se muestre el objeto
    # para que no se muestre Object(...etc)
    def __str__(self):
        return self.get_fullname

    # Se pueden sobreescribir metodos de la clase Model
    def save(self, *args, **kwargs):
        print('Estamos guardando!')
        super().save(args, kwargs)


STATUS_CHOICES = {
    ('R', 'Reviewed'),
    ('N', 'Not Reviewed'),
    ('E', 'Error'),
    ('A', 'Accepted')
}


class WebSite(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(unique=True)
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    # Para establecer una relacion OneToOne
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # Se puede definir logica de negocio en los modelos
    def was_released_last_week(self):
        if self.release_date < datetime.date(2023, 1, 24):
            return 'Released before last week'
        else:
            return 'Released this week'

    # Esta clase se utiliza para atributos que no sean
    # parte del objeto, pero que si afectan a la tabla
    # en la BD
    class Meta:
        # Para definir el orden en el que van a estar los
        # WebSites en la BD
        ordering = ['rating']  # Ordena los campos por su cantidad de ratings
        db_table = 'website_custom_table_name'  # Define el nombre de la BD
        verbose_name = 'Sitio Web'
        verbose_name_plural = 'Sitios Web'


class Car(models.Model):
    # Este atributo es la llave primaria de Car
    name = models.CharField(max_length=40, primary_key=True)

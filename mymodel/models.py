from django.db import models

# Create your models here.
class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_starts = models.IntegerField()

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        return self.name

class Mobile(models.Model):
    number = models.CharField(max_length=20, primary_key=True)
    belongs_to = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class Bank(models.Model):
    name = models.CharField(max_length=100)
    customers = models.ManyToManyField(Person)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return self.person.name + " " + self.group.name

class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "Oxen" # for plural in admin page

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True # this is abstract class
        ordering = ["name"]

class Student(CommonInfo):

    class Meta(CommonInfo.Meta):
        db_table = "student_info"

    def __str__(self):
        return self.name

class Ancestor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Descendant(models.Model):
    name = models.CharField(max_length=50)
    ancestors = models.ManyToManyField( Ancestor,
                related_name = "%(app_label)s_%(class)s_related",
                related_query_name = "%(app_label)s_%(class)ss")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class ChildA(Descendant):
    pass

class ChildB(Descendant):
    city = models.CharField(max_length=100)


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

class Restaurant(Place):
#class Restaurant(models.Model):
#    place_ptr = models.OneToOneField( Place, on_delete = models.CASCADE,
#                parent_link = True )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

class Location(Place):
    class Meta:
        proxy = True

    def greetings(self):
        print("hellooo, this is in %s" % (self.name,))

class Base1(models.Model):
    base1_id = models.AutoField(primary_key=True)

class Base2(models.Model):
    base2_id = models.AutoField(primary_key=True)

class MyObj(Base1, Base2):
    pass

class BlogManager(models.Manager):

    def get_queryset(self):
        # print('....... From Blog Manager .......')
        return super().get_queryset()

class Blog(models.Model):
    # fields
    name = models.CharField(max_length=200)
    tagline = models.TextField(null = True)

    # managers
    objects = BlogManager()

    # methods
    def __str__(self):
        return self.name

class CityManager(models.Manager):

    def get_queryset(self):
        # print('..... City Manager .....')
        return super().get_queryset()


class City(models.Model):
    # fields
    name = models.CharField(max_length=200)

    # managers
    objects = CityManager()

    # methods
    def __str__(self):
        return self.name

class AuthorManager(models.Manager):
    def get_queryset(self):
        # print("..... From Author Manager .....")
        return super().get_queryset()

class Author(models.Model):
    name = models.CharField(max_length=200, null = True)
    email = models.EmailField()
    age = models.PositiveIntegerField(default=0)
    hometown = models.ForeignKey(City, on_delete = models.SET_NULL,
                    blank=True, null=True)

    objects = AuthorManager()

    def __str__(self):
        return self.name if self.name else 'null'

class EntryManager(models.Manager):

    def get_queryset(self):
        # print('....... From Entry Manager .......')
        return super().get_queryset()

class Entry(models.Model):
    # fields
    blog = models.ForeignKey( Blog, on_delete = models.CASCADE, null=True)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField(blank=True, null=True)
    mod_date = models.DateField(blank=True, null=True)
    authors = models.ManyToManyField(Author)
    n_comments = models.PositiveIntegerField(default=0)
    n_pingbacks = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(default=0)

    # managers
    #objects = models.Manager()
    entries = EntryManager()
    objects = entries

    # methods
    def __str__(self):
        return self.headline

class EntryDetail(models.Model):
    entry = models.OneToOneField(Entry, on_delete = models.CASCADE,
    related_name = 'detail')
    details = models.TextField()

    def __str__(self):
        return self.details

class p_manager(models.Manager):
    def total_member(self):
        return self.model.appear.all().count()

class AwardedPublisher(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(num_awards__gte = 10)

class PublisherQuerySet(models.QuerySet):
    def good_company(self):
        return self.filter(num_awards__gte = 10)

    def bad_company(self):
        return self.filter(num_awards__lt = 10)

class PublisherManager(models.Manager):
    def get_queryset(self):
        return PublisherQuerySet(self.model, using=self.db)

    def good_company(self):
        return self.get_queryset().good_company()

    def bad_company(self):
        return self.get_queryset().bad_company()

class ModelManager(models.Manager):
    pass

class Publisher(models.Model):

    # managers
    objects = models.Manager()
    appear = models.Manager()
    publish = p_manager()
    nice_member = AwardedPublisher()
    grab_data = PublisherManager()
    publisher_queryset = PublisherQuerySet.as_manager()
    model_manager = ModelManager.from_queryset(PublisherQuerySet)()

    # fields
    name = models.CharField(max_length=100)
    num_awards = models.PositiveIntegerField(default=0)
    location = models.ForeignKey(City, on_delete = models.SET_NULL,
                blank=True, null=True)

    # methods
    def __str__(self):
        return self.name if self.name else 'null'

class Book(models.Model):
    title = models.CharField(max_length=300)
    pages = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    rating = models.FloatField(default=0)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete = models.CASCADE)
    pub_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title if self.title else 'null'

class Store(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    registered_user = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name if self.name else 'null'

def age_validator(value):
    from django.core.exceptions import ValidationError
    if value < 17:
        raise ValidationError('age must be 17 or more')

class Visitor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[age_validator])

    def __str__(self):
        return self.name

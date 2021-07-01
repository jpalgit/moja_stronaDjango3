from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
#  from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='published')


class Post(models.Model):
    STAN_POSTA = (
        ('draft', 'roboczy'),
        ('published', 'opublikowany')
    )

    autor = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_posts')
    tytul = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique_for_date='data_publikacji')
    tresc = RichTextUploadingField()
    #  tags = TaggableManager()  # od teraz tags to manager - operacje na tagach
    kategoria = models.CharField(max_length=255)
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    data_publikacji = models.DateTimeField(default=timezone.now)
    data_aktualizacji = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STAN_POSTA,
                              default='draft')
    objects = models.Manager()  # Menedżer domyślny.
    opublikowane = PublishedManager()  # Menedżer niestandardowy -wydala opublikowane

    class Meta:
        ordering = ('-data_publikacji',)

    def __str__(self):
        return self.tytul

# W uproszczeniu - przedstawiciel twojego obiektu
# gdy potrzebujesz go zobrazować w postaci tekstu (stringa), czyli co się pokaże gdy zaządasz
# wyświetlenia obiektu Post !!!!
# Możesz zdefiniować sobie o wiele bardziej skomplikowany schemat
# # def __str__(self):
#     return ' Tytuł %s Napisał: %s Data utworzenia %s' % (self.title, self.author, self.data_utworzenia)
#
# W wyniku czego zarządając gdziekolwiek wyświetlenie  tego obiektu otrzymasz coś takiego:
# "Książka Granica autorstwa Zofia Nałkowska wydana przez Państwowy Instytut Wydawniczy"

# a tu utworzenie adresu url na podstawie nazwy do wykorzystania w szablonach
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.data_publikacji.year,
                             self.data_publikacji.strftime('%m'),
                             self.data_publikacji.strftime('%d'),
                             self.slug])
# =============komentarze=========================

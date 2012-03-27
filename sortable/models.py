from django.db import models

class Sortable(models.Model):

    position = models.IntegerField(blank=True, help_text='Used for sorting')

    class Meta:
        abstract = True
        ordering = ('position',)

    def save(self, *args, **kwargs):
        """
        autoincrement sorting
        we do not care about concurrency on this project in this case
        django is not able to use a second autoincrement field beside the primary key :(
        """
        if self.position is None:
            try:
                last = self.__class__.objects.order_by('-position')[0]
                self.position = last.position + 1
            except IndexError:
                self.position = 0

        return super(Sortable, self).save(*args, **kwargs)
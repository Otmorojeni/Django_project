from django.db import models


class Theme(models.Model):
    """Модель тематики"""

    name = models.CharField(max_length=150, unique=True)

    def __str__(self) -> str:
        return self.name
    

class Brand(models.Model):
    """Модель бренда"""

    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
    

class Kit(models.Model):
    """Модель набора"""

    article = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=150)
    theme = models.ForeignKey(
        Theme, 
        on_delete=models.CASCADE,
        related_name='kits'
    )
    details_count = models.PositiveIntegerField()
    release_year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.article} {self.name}'
    

class Review(models.Model):
    """Модель отзыва"""

    kit = models.ForeignKey(
        Kit,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    reviewer_name = models.CharField(max_length=150)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Отзыв для {self.kit.name} от {self.reviewer_name}'
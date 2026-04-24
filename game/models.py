from django.db import models


class Panel(models.Model):
    number = models.PositiveIntegerField(
        unique=True, verbose_name="Номер панели (как в книге)"
    )
    title = models.CharField(
        max_length=200, blank=True, verbose_name="Название сцены"
    )
    image = models.ImageField(
        upload_to="panels/",
        verbose_name="Изображение панели (WebP)",
        help_text="Загружайте картинки в формате .webp",
    )
    description = models.TextField(
        blank=True, verbose_name="Текст / диалоги на панели"
    )
    is_start = models.BooleanField(
        default=False, verbose_name="Начальная панель"
    )
    is_end = models.BooleanField(
        default=False, verbose_name="Финальная панель (смерть/победа)"
    )

    class Meta:
        ordering = ["number"]
        verbose_name = "Панель комикса"
        verbose_name_plural = "Панели комикса"

    def __str__(self):
        return f"№{self.number}: {self.title or 'Без названия'}"


class Choice(models.Model):
    from_panel = models.ForeignKey(
        Panel,
        on_delete=models.CASCADE,
        related_name="choices",
        verbose_name="От панели",
    )
    to_panel = models.ForeignKey(
        Panel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="incoming_choices",
        verbose_name="К панели",
    )
    text = models.CharField(
        max_length=500, verbose_name="Текст выбора действия"
    )
    condition = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Условие (опционально)",
        help_text="Например: «нужен нож» или «ОЗ > 50»",
    )

    class Meta:
        verbose_name = "Вариант выбора"
        verbose_name_plural = "Варианты выбора"

    def __str__(self):
        to = self.to_panel.number if self.to_panel else "Конец"
        return f"{self.from_panel.number} → {to}: {self.text[:45]}"

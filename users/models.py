from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Введите email")
    avatar = models.ImageField(
        upload_to="users/avatars/", blank=True, null=True, verbose_name="Аватар", help_text="Загрузите аватар"
    )
    phone_number = PhoneNumberField(blank=True, null=True, verbose_name="Телефон", help_text="Введите номер телефона")
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город", help_text="Введите город")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    from lms.models import Course, Lesson

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь",
                             help_text="Выберите пользователя", related_name="payments", blank=True, null=True)
    date = models.DateField(verbose_name="Дата оплаты", auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name="Оплаченный курс",
                               help_text="Выберите курс", blank=True, null=True, related_name="payments")
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name="Оплаченный урок",
                               help_text="Выберите урок", blank=True, null=True, related_name="payments")
    amount = models.PositiveIntegerField(verbose_name="Сумма оплаты", help_text="Введите сумму оплаты")

    PAYMENT_METHODS = [
        ("cash", "Наличные"),
        ("transfer_to_account", "Перевод на счет"),
    ]
    payment_method = models.CharField(choices=PAYMENT_METHODS, max_length=50, verbose_name="Способ оплаты",
                                      help_text="Выберите способ оплаты", default="transfer_to_account")

    session_id = models.CharField(max_length=255, verbose_name="ID сессии", help_text="Введите ID сессии", blank=True,
                                  null=True)
    link = models.URLField(max_length=400, verbose_name="Ссылка на оплату", help_text="Добавьте ссылку на оплату",
                           blank=True, null=True)

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f'{self.user.email} за "{self.course.name if self.course else self.lesson.name}"'

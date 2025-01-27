import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название курса', max_length=100, verbose_name='Курс')),
                ('description', models.TextField(blank=True, help_text='Введите описание курса', null=True, verbose_name='Описание курса')),
                ('preview', models.ImageField(blank=True, help_text='Загрузите превью курса', null=True, upload_to='media/img/', verbose_name='Превью курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название урока', max_length=100, verbose_name='Урок')),
                ('description', models.TextField(blank=True, help_text='Введите описание урока', null=True, verbose_name='Описание урока')),
                ('preview', models.ImageField(blank=True, help_text='Загрузите превью урока', null=True, upload_to='media/img/', verbose_name='Превью урока')),
                ('video_link', models.CharField(help_text='Добавьте ссылку на урок', verbose_name='Ссылка на урок')),
                ('course', models.ForeignKey(blank=True, help_text='Выберите курс', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='lms.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]

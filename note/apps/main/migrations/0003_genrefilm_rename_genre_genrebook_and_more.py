# Generated by Django 4.0.5 on 2022-07-23 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreFilm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Жанр фильма',
                'verbose_name_plural': 'Жанры фильма',
            },
        ),
        migrations.RenameModel(
            old_name='Genre',
            new_name='GenreBook',
        ),
        migrations.AlterModelOptions(
            name='genrebook',
            options={'verbose_name': 'Жанр книги', 'verbose_name_plural': 'Жанры книги'},
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='film',
            name='last_hour',
        ),
        migrations.RemoveField(
            model_name='film',
            name='last_minute',
        ),
        migrations.RemoveField(
            model_name='film',
            name='last_serie',
        ),
        migrations.AddField(
            model_name='book',
            name='emotional_heaviness',
            field=models.CharField(choices=[('Флафф', 'Флафф'), ('Нейтрально', 'Нейтрально'), ('Стекло', 'Стекло')], default='Нейтрально', max_length=10),
        ),
        migrations.AddField(
            model_name='book',
            name='genre_book',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='main.genrebook', verbose_name='Жанры'),
        ),
        migrations.AddField(
            model_name='film',
            name='emotional_heaviness',
            field=models.CharField(choices=[('Флафф', 'Флафф'), ('Нейтрально', 'Нейтрально'), ('Стекло', 'Стекло')], default='Нейтрально', max_length=10),
        ),
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('status', models.CharField(choices=[('Планирую', 'Планирую'), ('Смотрю', 'Смотрю'), ('Просмотрено', 'Просмотрено'), ('Заброшено', 'Заброшено')], default='Планирую', max_length=11)),
                ('emotional_heaviness', models.CharField(choices=[('Флафф', 'Флафф'), ('Нейтрально', 'Нейтрально'), ('Стекло', 'Стекло')], default='Нейтрально', max_length=10)),
                ('link', models.TextField(verbose_name='Ссылка')),
                ('last_serie', models.IntegerField(default=1, verbose_name='Последняя серия')),
                ('created_date', models.DateTimeField()),
                ('genre_film', models.ManyToManyField(help_text='Select a genre for this film', to='main.genrefilm', verbose_name='Жанры')),
                ('id_for_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'ordering': ['-created_date'],
            },
        ),
        migrations.AddField(
            model_name='film',
            name='genre_film',
            field=models.ManyToManyField(help_text='Select a genre for this film', to='main.genrefilm', verbose_name='Жанры'),
        ),
    ]

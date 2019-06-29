# Generated by Django 2.2.2 on 2019-06-29 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('published', models.CharField(max_length=4)),
                ('file', models.FileField(blank=True, null=True, upload_to='books')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='covers')),
                ('description', models.TextField(blank=True, max_length=5000, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Author')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
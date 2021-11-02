# Generated by Django 3.2.5 on 2021-11-02 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('the_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200, null=True)),
                ('peep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='the_app.person')),
            ],
        ),
        migrations.DeleteModel(
            name='Trait',
        ),
    ]

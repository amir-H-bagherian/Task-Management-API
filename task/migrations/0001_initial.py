# Generated by Django 4.2.4 on 2023-08-19 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TimeField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'TODO'), (2, 'IN_PROGRESS'), (3, 'DONE')], default=1, verbose_name='Task Status')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('assigned_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Assigned User')),
            ],
        ),
    ]

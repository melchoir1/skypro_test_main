
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='debt',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=25, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Задолженность'),
        ),
    ]

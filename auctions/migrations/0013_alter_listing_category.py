import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',

            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='auctions.category'),
        ),
    ]

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date',
            new_name='order_date',
        ),
    ]
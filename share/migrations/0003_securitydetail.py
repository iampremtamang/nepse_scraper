# Generated by Django 4.1.4 on 2022-12-17 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_security_traded'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityDetail',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('symbol', models.CharField(db_index=True, max_length=20, primary_key=True, serialize=False)),
                ('sector', models.CharField(max_length=100)),
                ('shares_outstanding', models.IntegerField(default=0)),
                ('market_price', models.FloatField(default=0)),
                ('percentage_change', models.FloatField(default=0)),
                ('high', models.FloatField(default=0)),
                ('low', models.FloatField(default=0)),
                ('avg_180_day', models.FloatField(default=0)),
                ('avg_120_day', models.FloatField(default=0)),
                ('one_year_yield', models.FloatField(default=0)),
                ('eps', models.FloatField(default=0)),
                ('pe_ratio', models.FloatField(default=0)),
                ('book_value', models.FloatField(default=0)),
                ('pbv_value', models.FloatField(default=0)),
                ('divident_percent', models.FloatField(default=0)),
                ('bonus_percentage', models.FloatField(default=0)),
                ('avg_30_day_volume', models.FloatField(default=0)),
                ('market_capitalization', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'Securities Detail',
                'ordering': ('symbol',),
            },
        ),
    ]
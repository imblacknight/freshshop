# Generated by Django 2.0.7 on 2019-04-11 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fs_goods', '0001_initial'),
        ('fs_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_detail_price', models.CharField(max_length=100)),
                ('order_detail_count', models.IntegerField()),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fs_goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('order_status', models.BooleanField(default=False)),
                ('order_total_price', models.CharField(max_length=100)),
                ('order_address', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fs_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fs_order.OrderInfo'),
        ),
    ]

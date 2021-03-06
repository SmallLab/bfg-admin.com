# Generated by Django 3.1.4 on 2020-12-02 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import mainadmin.mainhelpers.MainImgTypeField
import mainadmin.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link_name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('icon_style', models.CharField(default='', max_length=50)),
                ('is_icon_img', models.BooleanField(default=False)),
                ('max_num', models.SmallIntegerField(default=1)),
                ('paid_num', models.SmallIntegerField(default=5)),
            ],
            options={
                'db_table': 'mainbfg_categories',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='NotificationTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('text_message', models.CharField(default='', max_length=100)),
                ('data_send_sms', models.TextField()),
                ('data_send_email', models.TextField()),
                ('is_send', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'mainbfg_regions',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='TypeSentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link_name', models.CharField(default='', max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'mainbfg_typesentence',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_id', models.SmallIntegerField()),
                ('category_id', models.SmallIntegerField()),
                ('sub_id', models.SmallIntegerField(default=0)),
                ('autor', models.CharField(error_messages={'max_length': 'Required error'}, max_length=30)),
                ('caption', models.CharField(max_length=50)),
                ('region_id', models.SmallIntegerField()),
                ('full_adress', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('web_site', models.CharField(blank=True, max_length=250)),
                ('is_webstore', models.BooleanField(default=False)),
                ('description', models.TextField(max_length=1000)),
                ('meta_info', models.CharField(blank=True, max_length=500)),
                ('main_img', mainadmin.mainhelpers.MainImgTypeField.MainImgTypeField(blank=True, default='nophoto.png', upload_to=mainadmin.models.custom_directory_path)),
                ('dirname_img', models.CharField(blank=True, default='', max_length=15)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('stop_time', models.DateTimeField(blank=True)),
                ('status', models.SmallIntegerField(default=0)),
                ('type_s', models.SmallIntegerField(default=0)),
                ('type_img_s', models.CharField(blank=True, max_length=300)),
                ('views', models.IntegerField(default=0)),
                ('phone_views', models.IntegerField(default=0)),
                ('text_message', models.CharField(blank=True, max_length=1000)),
                ('is_paid', models.BooleanField(default=False)),
                ('start_time_paid', models.DateTimeField(auto_now_add=True)),
                ('end_time_paid', models.DateTimeField(auto_now_add=True)),
                ('on_moderation', models.BooleanField(default=False)),
                ('link_name', models.CharField(max_length=550)),
                ('identifier', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentences', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'mainbfg_sentence',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('favorite_num', models.SmallIntegerField(blank=True, default=0)),
                ('is_subscrabtion', models.BooleanField(default=False)),
                ('is_subscriber', models.BooleanField(default=False)),
                ('facebook_id', models.BigIntegerField(blank=True, default=0)),
                ('vk_id', models.IntegerField(blank=True, default=0)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'mainbfg_profile',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_path', models.CharField(blank=True, max_length=250)),
                ('sentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='mainadmin.sentence')),
            ],
            options={
                'db_table': 'mainbfg_image',
            },
        ),
    ]

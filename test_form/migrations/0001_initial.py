# Generated by Django 4.0.4 on 2022-06-23 13:28

from django.db import migrations, models
import test_form.utils.rename_upload


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loguser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=32, verbose_name='账号')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('gender', models.CharField(max_length=1)),
                ('hobby', models.CharField(max_length=20)),
                ('hair', models.CharField(max_length=1)),
                ('img', models.ImageField(blank=True, null=True, storage=test_form.utils.rename_upload.RenameUpload(), upload_to='loguser_image')),
            ],
        ),
    ]

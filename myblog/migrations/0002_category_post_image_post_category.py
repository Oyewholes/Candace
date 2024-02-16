# Generated by Django 4.2.3 on 2024-01-29 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myblog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="Random", max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(
                default="default_image.jpg", upload_to="blog_pics/"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="myblog.category",
            ),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-12 20:16

from django.apps.registry import Apps
from django.db import migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor

from authentik.common.saml import constants


def update_algorithms(apps: Apps, schema_editor: BaseDatabaseSchemaEditor):
    SAMLProvider = apps.get_model("authentik_providers_saml", "SAMLProvider")
    signature_translation_map = {
        "rsa-sha1": constants.RSA_SHA1,
        "rsa-sha256": constants.RSA_SHA256,
        "ecdsa-sha256": constants.RSA_SHA256,
        "dsa-sha1": constants.DSA_SHA1,
    }
    digest_translation_map = {
        "sha1": constants.SHA1,
        "sha256": constants.SHA256,
    }

    for source in SAMLProvider.objects.all():
        source.signature_algorithm = signature_translation_map.get(
            source.signature_algorithm, constants.RSA_SHA256
        )
        source.digest_algorithm = digest_translation_map.get(
            source.digest_algorithm, constants.SHA256
        )
        source.save()


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_providers_saml", "0008_auto_20201112_1036"),
    ]

    operations = [
        migrations.AlterField(
            model_name="samlprovider",
            name="digest_algorithm",
            field=models.CharField(
                choices=[
                    (constants.SHA1, "SHA1"),
                    (constants.SHA256, "SHA256"),
                    (constants.SHA384, "SHA384"),
                    (constants.SHA512, "SHA512"),
                ],
                default=constants.SHA256,
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="samlprovider",
            name="signature_algorithm",
            field=models.CharField(
                choices=[
                    (constants.RSA_SHA1, "RSA-SHA1"),
                    (constants.RSA_SHA256, "RSA-SHA256"),
                    (constants.RSA_SHA384, "RSA-SHA384"),
                    (constants.RSA_SHA512, "RSA-SHA512"),
                    (constants.DSA_SHA1, "DSA-SHA1"),
                ],
                default=constants.RSA_SHA256,
                max_length=50,
            ),
        ),
    ]

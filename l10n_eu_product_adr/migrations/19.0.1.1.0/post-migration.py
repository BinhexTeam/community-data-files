# Copyright 2026 Binhex
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    core = env.ref("uom.product_uom_milliliter", raise_if_not_found=False)
    if core:
        for xmlid in [
            "l10n_eu_product_adr.product_uom_mililiter",
            "l10n_eu_product_adr.product_uom_milliliter",
        ]:
            old = env.ref(xmlid, raise_if_not_found=False)
            if old and old.id != core.id:
                openupgrade.logged_query(
                    env.cr,
                    "UPDATE adr_goods SET limited_quantity_uom_id = %s WHERE limited_quantity_uom_id = %s",  # noqa: E501
                    (core.id, old.id),
                )
    openupgrade.delete_records_safely_by_xml_id(
        env,
        [
            "l10n_eu_product_adr.product_uom_mililiter",
            "l10n_eu_product_adr.product_uom_milliliter",
        ],
    )

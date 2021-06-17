# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
#
# Invenio-Vocabularies is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Vocabulary affiliations."""

from invenio_records_resources.factories.factory import RecordTypeFactory

from ...services.permissions import PermissionPolicy
from .schema import AffiliationSchema

affiliation_record_type = RecordTypeFactory(
    "Affiliation",
    AffiliationSchema,
    permission_policy_cls=PermissionPolicy,
    endpoint_route='/affiliations'
)

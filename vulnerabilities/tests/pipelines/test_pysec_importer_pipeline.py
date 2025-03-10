#
# Copyright (c) nexB Inc. and others. All rights reserved.
# VulnerableCode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/aboutcode-org/vulnerablecode for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#

import json
from pathlib import Path
from unittest import TestCase

from vulnerabilities.importers.osv import parse_advisory_data
from vulnerabilities.tests.util_tests import VULNERABLECODE_REGEN_TEST_FIXTURES as REGEN
from vulnerabilities.tests.util_tests import check_results_against_json

TEST_DATA = Path(__file__).parent.parent / "test_data" / "pysec"


class TestPyPIImporter(TestCase):
    def test_to_advisories_with_summary(self):
        with open(TEST_DATA / "pysec-advisories_with_summary.json") as f:
            mock_response = json.load(f)
        results = parse_advisory_data(mock_response, ["pypi"], "https://test.com").to_dict()

        expected_file = TEST_DATA / "pysec-advisories_with_summary-expected.json"
        check_results_against_json(
            results=results,
            expected_file=expected_file,
            regen=REGEN,
        )

    def test_to_advisories_without_summary(self):
        with open(TEST_DATA / "pysec-advisories_without_summary.json") as f:
            mock_response = json.load(f)

        results = parse_advisory_data(mock_response, ["pypi"], "https://test.com").to_dict()

        expected_file = TEST_DATA / "pysec-advisories_without_summary-expected.json"
        check_results_against_json(
            results=results,
            expected_file=expected_file,
            regen=REGEN,
        )

    def test_to_advisories_with_cwe(self):
        with open(TEST_DATA / "pysec-advisory_with_cwe.json") as f:
            mock_response = json.load(f)

        results = parse_advisory_data(
            raw_data=mock_response, supported_ecosystems=["pypi"], advisory_url="https://tes.com"
        ).to_dict()

        expected_file = TEST_DATA / "pysec-advisories_with_cwe-expected.json"
        check_results_against_json(
            results=results,
            expected_file=expected_file,
            regen=REGEN,
        )

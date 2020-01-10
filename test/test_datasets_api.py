# coding: utf-8

"""
    MINT Data Catalog

    API Documentation for MINT Data Catalog  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: danf@usc.edu
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import datacatalog
from datacatalog.api.datasets_api import DatasetsApi  # noqa: E501
from datacatalog.rest import ApiException


class TestDatasetsApi(unittest.TestCase):
    """DatasetsApi unit test stubs"""

    def setUp(self):
        self.api = datacatalog.api.datasets_api.DatasetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_dataset_resources(self):
        """Test case for dataset_resources

        List all resources for this dataset  # noqa: E501
        """
        pass

    def test_dataset_standard_variables(self):
        """Test case for dataset_standard_variables

        List all standard_variables for this dataset  # noqa: E501
        """
        pass

    def test_dataset_variables(self):
        """Test case for dataset_variables

        List all variables for this dataset  # noqa: E501
        """
        pass

    def test_datasets_search(self):
        """Test case for datasets_search

        Full-text search of datasets  # noqa: E501
        """
        pass

    def test_find_datasets(self):
        """Test case for find_datasets

        Search datasets by name, id, or standard variables  # noqa: E501
        """
        pass

    def test_get_dataset_info(self):
        """Test case for get_dataset_info

        Detailed information about the dataset  # noqa: E501
        """
        pass

    def test_register_datasets(self):
        """Test case for register_datasets

        Create dataset record(s)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

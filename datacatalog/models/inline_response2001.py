# coding: utf-8

"""
    MINT Data Catalog

    API Documentation for MINT Data Catalog  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: danf@usc.edu
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse2001(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'dataset': 'InlineResponse2001Dataset'
    }

    attribute_map = {
        'dataset': 'dataset'
    }

    def __init__(self, dataset=None):  # noqa: E501
        """InlineResponse2001 - a model defined in OpenAPI"""  # noqa: E501

        self._dataset = None
        self.discriminator = None

        if dataset is not None:
            self.dataset = dataset

    @property
    def dataset(self):
        """Gets the dataset of this InlineResponse2001.  # noqa: E501


        :return: The dataset of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001Dataset
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InlineResponse2001.


        :param dataset: The dataset of this InlineResponse2001.  # noqa: E501
        :type: InlineResponse2001Dataset
        """

        self._dataset = dataset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

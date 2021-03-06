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


class InlineResponse200DatasetStandardVariables(object):
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
        'standard_variable_id': 'str',
        'standard_variable_name': 'str',
        'standard_variable_uri': 'str'
    }

    attribute_map = {
        'standard_variable_id': 'standard_variable_id',
        'standard_variable_name': 'standard_variable_name',
        'standard_variable_uri': 'standard_variable_uri'
    }

    def __init__(self, standard_variable_id=None, standard_variable_name=None, standard_variable_uri=None):  # noqa: E501
        """InlineResponse200DatasetStandardVariables - a model defined in OpenAPI"""  # noqa: E501

        self._standard_variable_id = None
        self._standard_variable_name = None
        self._standard_variable_uri = None
        self.discriminator = None

        if standard_variable_id is not None:
            self.standard_variable_id = standard_variable_id
        if standard_variable_name is not None:
            self.standard_variable_name = standard_variable_name
        if standard_variable_uri is not None:
            self.standard_variable_uri = standard_variable_uri

    @property
    def standard_variable_id(self):
        """Gets the standard_variable_id of this InlineResponse200DatasetStandardVariables.  # noqa: E501


        :return: The standard_variable_id of this InlineResponse200DatasetStandardVariables.  # noqa: E501
        :rtype: str
        """
        return self._standard_variable_id

    @standard_variable_id.setter
    def standard_variable_id(self, standard_variable_id):
        """Sets the standard_variable_id of this InlineResponse200DatasetStandardVariables.


        :param standard_variable_id: The standard_variable_id of this InlineResponse200DatasetStandardVariables.  # noqa: E501
        :type: str
        """

        self._standard_variable_id = standard_variable_id

    @property
    def standard_variable_name(self):
        """Gets the standard_variable_name of this InlineResponse200DatasetStandardVariables.  # noqa: E501


        :return: The standard_variable_name of this InlineResponse200DatasetStandardVariables.  # noqa: E501
        :rtype: str
        """
        return self._standard_variable_name

    @standard_variable_name.setter
    def standard_variable_name(self, standard_variable_name):
        """Sets the standard_variable_name of this InlineResponse200DatasetStandardVariables.


        :param standard_variable_name: The standard_variable_name of this InlineResponse200DatasetStandardVariables.  # noqa: E501
        :type: str
        """

        self._standard_variable_name = standard_variable_name

    @property
    def standard_variable_uri(self):
        """Gets the standard_variable_uri of this InlineResponse200DatasetStandardVariables.  # noqa: E501


        :return: The standard_variable_uri of this InlineResponse200DatasetStandardVariables.  # noqa: E501
        :rtype: str
        """
        return self._standard_variable_uri

    @standard_variable_uri.setter
    def standard_variable_uri(self, standard_variable_uri):
        """Sets the standard_variable_uri of this InlineResponse200DatasetStandardVariables.


        :param standard_variable_uri: The standard_variable_uri of this InlineResponse200DatasetStandardVariables.  # noqa: E501
        :type: str
        """

        self._standard_variable_uri = standard_variable_uri

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
        if not isinstance(other, InlineResponse200DatasetStandardVariables):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

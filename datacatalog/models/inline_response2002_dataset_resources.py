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


class InlineResponse2002DatasetResources(object):
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
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_data_url': 'str',
        'resource_created_at': 'datetime'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_data_url': 'resource_data_url',
        'resource_created_at': 'resource_created_at'
    }

    def __init__(self, resource_id=None, resource_name=None, resource_data_url=None, resource_created_at=None):  # noqa: E501
        """InlineResponse2002DatasetResources - a model defined in OpenAPI"""  # noqa: E501

        self._resource_id = None
        self._resource_name = None
        self._resource_data_url = None
        self._resource_created_at = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_data_url is not None:
            self.resource_data_url = resource_data_url
        if resource_created_at is not None:
            self.resource_created_at = resource_created_at

    @property
    def resource_id(self):
        """Gets the resource_id of this InlineResponse2002DatasetResources.  # noqa: E501


        :return: The resource_id of this InlineResponse2002DatasetResources.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this InlineResponse2002DatasetResources.


        :param resource_id: The resource_id of this InlineResponse2002DatasetResources.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this InlineResponse2002DatasetResources.  # noqa: E501


        :return: The resource_name of this InlineResponse2002DatasetResources.  # noqa: E501
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this InlineResponse2002DatasetResources.


        :param resource_name: The resource_name of this InlineResponse2002DatasetResources.  # noqa: E501
        :type: str
        """

        self._resource_name = resource_name

    @property
    def resource_data_url(self):
        """Gets the resource_data_url of this InlineResponse2002DatasetResources.  # noqa: E501


        :return: The resource_data_url of this InlineResponse2002DatasetResources.  # noqa: E501
        :rtype: str
        """
        return self._resource_data_url

    @resource_data_url.setter
    def resource_data_url(self, resource_data_url):
        """Sets the resource_data_url of this InlineResponse2002DatasetResources.


        :param resource_data_url: The resource_data_url of this InlineResponse2002DatasetResources.  # noqa: E501
        :type: str
        """

        self._resource_data_url = resource_data_url

    @property
    def resource_created_at(self):
        """Gets the resource_created_at of this InlineResponse2002DatasetResources.  # noqa: E501


        :return: The resource_created_at of this InlineResponse2002DatasetResources.  # noqa: E501
        :rtype: datetime
        """
        return self._resource_created_at

    @resource_created_at.setter
    def resource_created_at(self, resource_created_at):
        """Sets the resource_created_at of this InlineResponse2002DatasetResources.


        :param resource_created_at: The resource_created_at of this InlineResponse2002DatasetResources.  # noqa: E501
        :type: datetime
        """

        self._resource_created_at = resource_created_at

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
        if not isinstance(other, InlineResponse2002DatasetResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

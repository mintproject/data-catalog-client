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


class InlineResponse2005Dataset(object):
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
        'name': 'str',
        'dataset_id': 'str',
        'resource_type': 'str',
        'data_url': 'str',
        'metadata': 'object',
        'created_at': 'datetime'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'name': 'name',
        'dataset_id': 'dataset_id',
        'resource_type': 'resource_type',
        'data_url': 'data_url',
        'metadata': 'metadata',
        'created_at': 'created_at'
    }

    def __init__(self, resource_id=None, name=None, dataset_id=None, resource_type=None, data_url=None, metadata=None, created_at=None):  # noqa: E501
        """InlineResponse2005Dataset - a model defined in OpenAPI"""  # noqa: E501

        self._resource_id = None
        self._name = None
        self._dataset_id = None
        self._resource_type = None
        self._data_url = None
        self._metadata = None
        self._created_at = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if name is not None:
            self.name = name
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if resource_type is not None:
            self.resource_type = resource_type
        if data_url is not None:
            self.data_url = data_url
        if metadata is not None:
            self.metadata = metadata
        if created_at is not None:
            self.created_at = created_at

    @property
    def resource_id(self):
        """Gets the resource_id of this InlineResponse2005Dataset.  # noqa: E501


        :return: The resource_id of this InlineResponse2005Dataset.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this InlineResponse2005Dataset.


        :param resource_id: The resource_id of this InlineResponse2005Dataset.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def name(self):
        """Gets the name of this InlineResponse2005Dataset.  # noqa: E501


        :return: The name of this InlineResponse2005Dataset.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2005Dataset.


        :param name: The name of this InlineResponse2005Dataset.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def dataset_id(self):
        """Gets the dataset_id of this InlineResponse2005Dataset.  # noqa: E501

        record_id of the dataset that this resource belongs to  # noqa: E501

        :return: The dataset_id of this InlineResponse2005Dataset.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this InlineResponse2005Dataset.

        record_id of the dataset that this resource belongs to  # noqa: E501

        :param dataset_id: The dataset_id of this InlineResponse2005Dataset.  # noqa: E501
        :type: str
        """

        self._dataset_id = dataset_id

    @property
    def resource_type(self):
        """Gets the resource_type of this InlineResponse2005Dataset.  # noqa: E501


        :return: The resource_type of this InlineResponse2005Dataset.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this InlineResponse2005Dataset.


        :param resource_type: The resource_type of this InlineResponse2005Dataset.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def data_url(self):
        """Gets the data_url of this InlineResponse2005Dataset.  # noqa: E501


        :return: The data_url of this InlineResponse2005Dataset.  # noqa: E501
        :rtype: str
        """
        return self._data_url

    @data_url.setter
    def data_url(self, data_url):
        """Sets the data_url of this InlineResponse2005Dataset.


        :param data_url: The data_url of this InlineResponse2005Dataset.  # noqa: E501
        :type: str
        """

        self._data_url = data_url

    @property
    def metadata(self):
        """Gets the metadata of this InlineResponse2005Dataset.  # noqa: E501


        :return: The metadata of this InlineResponse2005Dataset.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this InlineResponse2005Dataset.


        :param metadata: The metadata of this InlineResponse2005Dataset.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse2005Dataset.  # noqa: E501


        :return: The created_at of this InlineResponse2005Dataset.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse2005Dataset.


        :param created_at: The created_at of this InlineResponse2005Dataset.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

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
        if not isinstance(other, InlineResponse2005Dataset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    Flagr

    Flagr is a feature flagging, A/B testing and dynamic configuration microservice  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PutFlagRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'description': 'str',
        'data_records_enabled': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'data_records_enabled': 'dataRecordsEnabled'
    }

    def __init__(self, description=None, data_records_enabled=None):  # noqa: E501
        """PutFlagRequest - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._data_records_enabled = None
        self.discriminator = None

        self.description = description
        if data_records_enabled is not None:
            self.data_records_enabled = data_records_enabled

    @property
    def description(self):
        """Gets the description of this PutFlagRequest.  # noqa: E501


        :return: The description of this PutFlagRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PutFlagRequest.


        :param description: The description of this PutFlagRequest.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if description is not None and len(description) < 1:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def data_records_enabled(self):
        """Gets the data_records_enabled of this PutFlagRequest.  # noqa: E501

        enabled data records will get data logging in the metrics pipeline, for example, kafka.  # noqa: E501

        :return: The data_records_enabled of this PutFlagRequest.  # noqa: E501
        :rtype: bool
        """
        return self._data_records_enabled

    @data_records_enabled.setter
    def data_records_enabled(self, data_records_enabled):
        """Sets the data_records_enabled of this PutFlagRequest.

        enabled data records will get data logging in the metrics pipeline, for example, kafka.  # noqa: E501

        :param data_records_enabled: The data_records_enabled of this PutFlagRequest.  # noqa: E501
        :type: bool
        """

        self._data_records_enabled = data_records_enabled

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, PutFlagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
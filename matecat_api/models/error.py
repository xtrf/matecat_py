# coding: utf-8

"""
    MateCat API

    We developed a set of Rest API to let you integrate Matecat in your translation management system or in any other application. Use our API to create projects and check their status.  # noqa: E501

    OpenAPI spec version: 2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Error(object):
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
        'errors': 'list[ErrorErrors]',
        'data': 'list[object]'
    }

    attribute_map = {
        'errors': 'errors',
        'data': 'data'
    }

    def __init__(self, errors=None, data=None):  # noqa: E501
        """Error - a model defined in Swagger"""  # noqa: E501
        self._errors = None
        self._data = None
        self.discriminator = None
        if errors is not None:
            self.errors = errors
        if data is not None:
            self.data = data

    @property
    def errors(self):
        """Gets the errors of this Error.  # noqa: E501


        :return: The errors of this Error.  # noqa: E501
        :rtype: list[ErrorErrors]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this Error.


        :param errors: The errors of this Error.  # noqa: E501
        :type: list[ErrorErrors]
        """

        self._errors = errors

    @property
    def data(self):
        """Gets the data of this Error.  # noqa: E501

        This property contains any debug data that can serve for better understanding of the error  # noqa: E501

        :return: The data of this Error.  # noqa: E501
        :rtype: list[object]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Error.

        This property contains any debug data that can serve for better understanding of the error  # noqa: E501

        :param data: The data of this Error.  # noqa: E501
        :type: list[object]
        """

        self._data = data

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
        if issubclass(Error, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
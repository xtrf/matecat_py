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

class ReviseIssue(object):
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
        'allowed': 'float',
        'found': 'int'
    }

    attribute_map = {
        'allowed': 'allowed',
        'found': 'found'
    }

    def __init__(self, allowed=None, found=None):  # noqa: E501
        """ReviseIssue - a model defined in Swagger"""  # noqa: E501
        self._allowed = None
        self._found = None
        self.discriminator = None
        if allowed is not None:
            self.allowed = allowed
        if found is not None:
            self.found = found

    @property
    def allowed(self):
        """Gets the allowed of this ReviseIssue.  # noqa: E501


        :return: The allowed of this ReviseIssue.  # noqa: E501
        :rtype: float
        """
        return self._allowed

    @allowed.setter
    def allowed(self, allowed):
        """Sets the allowed of this ReviseIssue.


        :param allowed: The allowed of this ReviseIssue.  # noqa: E501
        :type: float
        """

        self._allowed = allowed

    @property
    def found(self):
        """Gets the found of this ReviseIssue.  # noqa: E501


        :return: The found of this ReviseIssue.  # noqa: E501
        :rtype: int
        """
        return self._found

    @found.setter
    def found(self, found):
        """Sets the found of this ReviseIssue.


        :param found: The found of this ReviseIssue.  # noqa: E501
        :type: int
        """

        self._found = found

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
        if issubclass(ReviseIssue, dict):
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
        if not isinstance(other, ReviseIssue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

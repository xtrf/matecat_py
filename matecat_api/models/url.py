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

class Url(object):
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
        'password': 'str',
        'translate_url': 'str',
        'revise_url': 'str'
    }

    attribute_map = {
        'password': 'password',
        'translate_url': 'translate_url',
        'revise_url': 'revise_url'
    }

    def __init__(self, password=None, translate_url=None, revise_url=None):  # noqa: E501
        """Url - a model defined in Swagger"""  # noqa: E501
        self._password = None
        self._translate_url = None
        self._revise_url = None
        self.discriminator = None
        if password is not None:
            self.password = password
        if translate_url is not None:
            self.translate_url = translate_url
        if revise_url is not None:
            self.revise_url = revise_url

    @property
    def password(self):
        """Gets the password of this Url.  # noqa: E501


        :return: The password of this Url.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Url.


        :param password: The password of this Url.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def translate_url(self):
        """Gets the translate_url of this Url.  # noqa: E501


        :return: The translate_url of this Url.  # noqa: E501
        :rtype: str
        """
        return self._translate_url

    @translate_url.setter
    def translate_url(self, translate_url):
        """Sets the translate_url of this Url.


        :param translate_url: The translate_url of this Url.  # noqa: E501
        :type: str
        """

        self._translate_url = translate_url

    @property
    def revise_url(self):
        """Gets the revise_url of this Url.  # noqa: E501


        :return: The revise_url of this Url.  # noqa: E501
        :rtype: str
        """
        return self._revise_url

    @revise_url.setter
    def revise_url(self, revise_url):
        """Sets the revise_url of this Url.


        :param revise_url: The revise_url of this Url.  # noqa: E501
        :type: str
        """

        self._revise_url = revise_url

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
        if issubclass(Url, dict):
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
        if not isinstance(other, Url):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

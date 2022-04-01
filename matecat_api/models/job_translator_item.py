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

class JobTranslatorItem(object):
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
        'id': 'int',
        'translator': 'Translator'
    }

    attribute_map = {
        'id': 'id',
        'translator': 'translator'
    }

    def __init__(self, id=None, translator=None):  # noqa: E501
        """JobTranslatorItem - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._translator = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if translator is not None:
            self.translator = translator

    @property
    def id(self):
        """Gets the id of this JobTranslatorItem.  # noqa: E501


        :return: The id of this JobTranslatorItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobTranslatorItem.


        :param id: The id of this JobTranslatorItem.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def translator(self):
        """Gets the translator of this JobTranslatorItem.  # noqa: E501


        :return: The translator of this JobTranslatorItem.  # noqa: E501
        :rtype: Translator
        """
        return self._translator

    @translator.setter
    def translator(self, translator):
        """Sets the translator of this JobTranslatorItem.


        :param translator: The translator of this JobTranslatorItem.  # noqa: E501
        :type: Translator
        """

        self._translator = translator

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
        if issubclass(JobTranslatorItem, dict):
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
        if not isinstance(other, JobTranslatorItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

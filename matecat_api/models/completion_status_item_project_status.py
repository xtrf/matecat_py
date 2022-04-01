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

class CompletionStatusItemProjectStatus(object):
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
        'revise': 'list[CompletionStatusItemProjectStatusRevise]',
        'translate': 'list[CompletionStatusItemProjectStatusRevise]',
        'id': 'str',
        'completed': 'bool'
    }

    attribute_map = {
        'revise': 'revise',
        'translate': 'translate',
        'id': 'id',
        'completed': 'completed'
    }

    def __init__(self, revise=None, translate=None, id=None, completed=None):  # noqa: E501
        """CompletionStatusItemProjectStatus - a model defined in Swagger"""  # noqa: E501
        self._revise = None
        self._translate = None
        self._id = None
        self._completed = None
        self.discriminator = None
        if revise is not None:
            self.revise = revise
        if translate is not None:
            self.translate = translate
        if id is not None:
            self.id = id
        if completed is not None:
            self.completed = completed

    @property
    def revise(self):
        """Gets the revise of this CompletionStatusItemProjectStatus.  # noqa: E501


        :return: The revise of this CompletionStatusItemProjectStatus.  # noqa: E501
        :rtype: list[CompletionStatusItemProjectStatusRevise]
        """
        return self._revise

    @revise.setter
    def revise(self, revise):
        """Sets the revise of this CompletionStatusItemProjectStatus.


        :param revise: The revise of this CompletionStatusItemProjectStatus.  # noqa: E501
        :type: list[CompletionStatusItemProjectStatusRevise]
        """

        self._revise = revise

    @property
    def translate(self):
        """Gets the translate of this CompletionStatusItemProjectStatus.  # noqa: E501


        :return: The translate of this CompletionStatusItemProjectStatus.  # noqa: E501
        :rtype: list[CompletionStatusItemProjectStatusRevise]
        """
        return self._translate

    @translate.setter
    def translate(self, translate):
        """Sets the translate of this CompletionStatusItemProjectStatus.


        :param translate: The translate of this CompletionStatusItemProjectStatus.  # noqa: E501
        :type: list[CompletionStatusItemProjectStatusRevise]
        """

        self._translate = translate

    @property
    def id(self):
        """Gets the id of this CompletionStatusItemProjectStatus.  # noqa: E501


        :return: The id of this CompletionStatusItemProjectStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompletionStatusItemProjectStatus.


        :param id: The id of this CompletionStatusItemProjectStatus.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def completed(self):
        """Gets the completed of this CompletionStatusItemProjectStatus.  # noqa: E501


        :return: The completed of this CompletionStatusItemProjectStatus.  # noqa: E501
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this CompletionStatusItemProjectStatus.


        :param completed: The completed of this CompletionStatusItemProjectStatus.  # noqa: E501
        :type: bool
        """

        self._completed = completed

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
        if issubclass(CompletionStatusItemProjectStatus, dict):
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
        if not isinstance(other, CompletionStatusItemProjectStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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

class TranslationVersion(object):
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
        'id_segment': 'int',
        'id_job': 'int',
        'translation': 'str',
        'version_number': 'str',
        'propagated_from': 'int',
        'created_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'id_segment': 'id_segment',
        'id_job': 'id_job',
        'translation': 'translation',
        'version_number': 'version_number',
        'propagated_from': 'propagated_from',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, id_segment=None, id_job=None, translation=None, version_number=None, propagated_from=None, created_at=None):  # noqa: E501
        """TranslationVersion - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._id_segment = None
        self._id_job = None
        self._translation = None
        self._version_number = None
        self._propagated_from = None
        self._created_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if id_segment is not None:
            self.id_segment = id_segment
        if id_job is not None:
            self.id_job = id_job
        if translation is not None:
            self.translation = translation
        if version_number is not None:
            self.version_number = version_number
        if propagated_from is not None:
            self.propagated_from = propagated_from
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this TranslationVersion.  # noqa: E501


        :return: The id of this TranslationVersion.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TranslationVersion.


        :param id: The id of this TranslationVersion.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def id_segment(self):
        """Gets the id_segment of this TranslationVersion.  # noqa: E501


        :return: The id_segment of this TranslationVersion.  # noqa: E501
        :rtype: int
        """
        return self._id_segment

    @id_segment.setter
    def id_segment(self, id_segment):
        """Sets the id_segment of this TranslationVersion.


        :param id_segment: The id_segment of this TranslationVersion.  # noqa: E501
        :type: int
        """

        self._id_segment = id_segment

    @property
    def id_job(self):
        """Gets the id_job of this TranslationVersion.  # noqa: E501


        :return: The id_job of this TranslationVersion.  # noqa: E501
        :rtype: int
        """
        return self._id_job

    @id_job.setter
    def id_job(self, id_job):
        """Sets the id_job of this TranslationVersion.


        :param id_job: The id_job of this TranslationVersion.  # noqa: E501
        :type: int
        """

        self._id_job = id_job

    @property
    def translation(self):
        """Gets the translation of this TranslationVersion.  # noqa: E501


        :return: The translation of this TranslationVersion.  # noqa: E501
        :rtype: str
        """
        return self._translation

    @translation.setter
    def translation(self, translation):
        """Sets the translation of this TranslationVersion.


        :param translation: The translation of this TranslationVersion.  # noqa: E501
        :type: str
        """

        self._translation = translation

    @property
    def version_number(self):
        """Gets the version_number of this TranslationVersion.  # noqa: E501


        :return: The version_number of this TranslationVersion.  # noqa: E501
        :rtype: str
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this TranslationVersion.


        :param version_number: The version_number of this TranslationVersion.  # noqa: E501
        :type: str
        """

        self._version_number = version_number

    @property
    def propagated_from(self):
        """Gets the propagated_from of this TranslationVersion.  # noqa: E501


        :return: The propagated_from of this TranslationVersion.  # noqa: E501
        :rtype: int
        """
        return self._propagated_from

    @propagated_from.setter
    def propagated_from(self, propagated_from):
        """Sets the propagated_from of this TranslationVersion.


        :param propagated_from: The propagated_from of this TranslationVersion.  # noqa: E501
        :type: int
        """

        self._propagated_from = propagated_from

    @property
    def created_at(self):
        """Gets the created_at of this TranslationVersion.  # noqa: E501


        :return: The created_at of this TranslationVersion.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TranslationVersion.


        :param created_at: The created_at of this TranslationVersion.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

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
        if issubclass(TranslationVersion, dict):
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
        if not isinstance(other, TranslationVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
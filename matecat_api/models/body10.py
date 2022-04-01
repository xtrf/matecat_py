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

class Body10(object):
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
        'version_number': 'str',
        'id_segment': 'str',
        'id_job': 'str',
        'id_category': 'str',
        'severity': 'str',
        'translation_version': 'str',
        'target_text': 'str',
        'start_node': 'str',
        'start_offset': 'str',
        'end_node': 'str',
        'end_offset': 'str',
        'is_full_segment': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'version_number': 'version_number',
        'id_segment': 'id_segment',
        'id_job': 'id_job',
        'id_category': 'id_category',
        'severity': 'severity',
        'translation_version': 'translation_version',
        'target_text': 'target_text',
        'start_node': 'start_node',
        'start_offset': 'start_offset',
        'end_node': 'end_node',
        'end_offset': 'end_offset',
        'is_full_segment': 'is_full_segment',
        'comment': 'comment'
    }

    def __init__(self, version_number=None, id_segment=None, id_job=None, id_category=None, severity=None, translation_version=None, target_text=None, start_node=None, start_offset=None, end_node=None, end_offset=None, is_full_segment=None, comment=None):  # noqa: E501
        """Body10 - a model defined in Swagger"""  # noqa: E501
        self._version_number = None
        self._id_segment = None
        self._id_job = None
        self._id_category = None
        self._severity = None
        self._translation_version = None
        self._target_text = None
        self._start_node = None
        self._start_offset = None
        self._end_node = None
        self._end_offset = None
        self._is_full_segment = None
        self._comment = None
        self.discriminator = None
        self.version_number = version_number
        self.id_segment = id_segment
        self.id_job = id_job
        self.id_category = id_category
        self.severity = severity
        self.translation_version = translation_version
        self.target_text = target_text
        self.start_node = start_node
        self.start_offset = start_offset
        self.end_node = end_node
        self.end_offset = end_offset
        self.is_full_segment = is_full_segment
        self.comment = comment

    @property
    def version_number(self):
        """Gets the version_number of this Body10.  # noqa: E501


        :return: The version_number of this Body10.  # noqa: E501
        :rtype: str
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this Body10.


        :param version_number: The version_number of this Body10.  # noqa: E501
        :type: str
        """
        if version_number is None:
            raise ValueError("Invalid value for `version_number`, must not be `None`")  # noqa: E501

        self._version_number = version_number

    @property
    def id_segment(self):
        """Gets the id_segment of this Body10.  # noqa: E501


        :return: The id_segment of this Body10.  # noqa: E501
        :rtype: str
        """
        return self._id_segment

    @id_segment.setter
    def id_segment(self, id_segment):
        """Sets the id_segment of this Body10.


        :param id_segment: The id_segment of this Body10.  # noqa: E501
        :type: str
        """
        if id_segment is None:
            raise ValueError("Invalid value for `id_segment`, must not be `None`")  # noqa: E501

        self._id_segment = id_segment

    @property
    def id_job(self):
        """Gets the id_job of this Body10.  # noqa: E501


        :return: The id_job of this Body10.  # noqa: E501
        :rtype: str
        """
        return self._id_job

    @id_job.setter
    def id_job(self, id_job):
        """Sets the id_job of this Body10.


        :param id_job: The id_job of this Body10.  # noqa: E501
        :type: str
        """
        if id_job is None:
            raise ValueError("Invalid value for `id_job`, must not be `None`")  # noqa: E501

        self._id_job = id_job

    @property
    def id_category(self):
        """Gets the id_category of this Body10.  # noqa: E501


        :return: The id_category of this Body10.  # noqa: E501
        :rtype: str
        """
        return self._id_category

    @id_category.setter
    def id_category(self, id_category):
        """Sets the id_category of this Body10.


        :param id_category: The id_category of this Body10.  # noqa: E501
        :type: str
        """
        if id_category is None:
            raise ValueError("Invalid value for `id_category`, must not be `None`")  # noqa: E501

        self._id_category = id_category

    @property
    def severity(self):
        """Gets the severity of this Body10.  # noqa: E501


        :return: The severity of this Body10.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Body10.


        :param severity: The severity of this Body10.  # noqa: E501
        :type: str
        """
        if severity is None:
            raise ValueError("Invalid value for `severity`, must not be `None`")  # noqa: E501

        self._severity = severity

    @property
    def translation_version(self):
        """Gets the translation_version of this Body10.  # noqa: E501


        :return: The translation_version of this Body10.  # noqa: E501
        :rtype: str
        """
        return self._translation_version

    @translation_version.setter
    def translation_version(self, translation_version):
        """Sets the translation_version of this Body10.


        :param translation_version: The translation_version of this Body10.  # noqa: E501
        :type: str
        """
        if translation_version is None:
            raise ValueError("Invalid value for `translation_version`, must not be `None`")  # noqa: E501

        self._translation_version = translation_version

    @property
    def target_text(self):
        """Gets the target_text of this Body10.  # noqa: E501


        :return: The target_text of this Body10.  # noqa: E501
        :rtype: str
        """
        return self._target_text

    @target_text.setter
    def target_text(self, target_text):
        """Sets the target_text of this Body10.


        :param target_text: The target_text of this Body10.  # noqa: E501
        :type: str
        """
        if target_text is None:
            raise ValueError("Invalid value for `target_text`, must not be `None`")  # noqa: E501

        self._target_text = target_text

    @property
    def start_node(self):
        """Gets the start_node of this Body10.  # noqa: E501


        :return: The start_node of this Body10.  # noqa: E501
        :rtype: str
        """
        return self._start_node

    @start_node.setter
    def start_node(self, start_node):
        """Sets the start_node of this Body10.


        :param start_node: The start_node of this Body10.  # noqa: E501
        :type: str
        """
        if start_node is None:
            raise ValueError("Invalid value for `start_node`, must not be `None`")  # noqa: E501

        self._start_node = start_node

    @property
    def start_offset(self):
        """Gets the start_offset of this Body10.  # noqa: E501


        :return: The start_offset of this Body10.  # noqa: E501
        :rtype: str
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        """Sets the start_offset of this Body10.


        :param start_offset: The start_offset of this Body10.  # noqa: E501
        :type: str
        """
        if start_offset is None:
            raise ValueError("Invalid value for `start_offset`, must not be `None`")  # noqa: E501

        self._start_offset = start_offset

    @property
    def end_node(self):
        """Gets the end_node of this Body10.  # noqa: E501


        :return: The end_node of this Body10.  # noqa: E501
        :rtype: str
        """
        return self._end_node

    @end_node.setter
    def end_node(self, end_node):
        """Sets the end_node of this Body10.


        :param end_node: The end_node of this Body10.  # noqa: E501
        :type: str
        """
        if end_node is None:
            raise ValueError("Invalid value for `end_node`, must not be `None`")  # noqa: E501

        self._end_node = end_node

    @property
    def end_offset(self):
        """Gets the end_offset of this Body10.  # noqa: E501


        :return: The end_offset of this Body10.  # noqa: E501
        :rtype: str
        """
        return self._end_offset

    @end_offset.setter
    def end_offset(self, end_offset):
        """Sets the end_offset of this Body10.


        :param end_offset: The end_offset of this Body10.  # noqa: E501
        :type: str
        """
        if end_offset is None:
            raise ValueError("Invalid value for `end_offset`, must not be `None`")  # noqa: E501

        self._end_offset = end_offset

    @property
    def is_full_segment(self):
        """Gets the is_full_segment of this Body10.  # noqa: E501


        :return: The is_full_segment of this Body10.  # noqa: E501
        :rtype: str
        """
        return self._is_full_segment

    @is_full_segment.setter
    def is_full_segment(self, is_full_segment):
        """Sets the is_full_segment of this Body10.


        :param is_full_segment: The is_full_segment of this Body10.  # noqa: E501
        :type: str
        """
        if is_full_segment is None:
            raise ValueError("Invalid value for `is_full_segment`, must not be `None`")  # noqa: E501

        self._is_full_segment = is_full_segment

    @property
    def comment(self):
        """Gets the comment of this Body10.  # noqa: E501


        :return: The comment of this Body10.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Body10.


        :param comment: The comment of this Body10.  # noqa: E501
        :type: str
        """
        if comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")  # noqa: E501

        self._comment = comment

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
        if issubclass(Body10, dict):
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
        if not isinstance(other, Body10):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

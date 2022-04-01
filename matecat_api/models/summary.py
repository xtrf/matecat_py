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

class Summary(object):
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
        'name': 'str',
        'status': 'str',
        'in_queue_before': 'str',
        'total_segments': 'str',
        'segments_analyzed': 'str',
        'total_raw_wc': 'str',
        'total_standard_wc': 'str',
        'total_fast_wc': 'str',
        'total_tm_wc': 'str',
        'total_payable': 'str'
    }

    attribute_map = {
        'name': 'NAME',
        'status': 'STATUS',
        'in_queue_before': 'IN_QUEUE_BEFORE',
        'total_segments': 'TOTAL_SEGMENTS',
        'segments_analyzed': 'SEGMENTS_ANALYZED',
        'total_raw_wc': 'TOTAL_RAW_WC',
        'total_standard_wc': 'TOTAL_STANDARD_WC',
        'total_fast_wc': 'TOTAL_FAST_WC',
        'total_tm_wc': 'TOTAL_TM_WC',
        'total_payable': 'TOTAL_PAYABLE'
    }

    def __init__(self, name=None, status=None, in_queue_before=None, total_segments=None, segments_analyzed=None, total_raw_wc=None, total_standard_wc=None, total_fast_wc=None, total_tm_wc=None, total_payable=None):  # noqa: E501
        """Summary - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._status = None
        self._in_queue_before = None
        self._total_segments = None
        self._segments_analyzed = None
        self._total_raw_wc = None
        self._total_standard_wc = None
        self._total_fast_wc = None
        self._total_tm_wc = None
        self._total_payable = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if in_queue_before is not None:
            self.in_queue_before = in_queue_before
        if total_segments is not None:
            self.total_segments = total_segments
        if segments_analyzed is not None:
            self.segments_analyzed = segments_analyzed
        if total_raw_wc is not None:
            self.total_raw_wc = total_raw_wc
        if total_standard_wc is not None:
            self.total_standard_wc = total_standard_wc
        if total_fast_wc is not None:
            self.total_fast_wc = total_fast_wc
        if total_tm_wc is not None:
            self.total_tm_wc = total_tm_wc
        if total_payable is not None:
            self.total_payable = total_payable

    @property
    def name(self):
        """Gets the name of this Summary.  # noqa: E501

        A list of objects containing error message at system wide level. Every error has a negative numeric code and a textual message ( currently the only error reported is the wrong version number in config.inc.php file and happens only after Matecat updates, so you should never see it ).  # noqa: E501

        :return: The name of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Summary.

        A list of objects containing error message at system wide level. Every error has a negative numeric code and a textual message ( currently the only error reported is the wrong version number in config.inc.php file and happens only after Matecat updates, so you should never see it ).  # noqa: E501

        :param name: The name of this Summary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this Summary.  # noqa: E501

        The status the project is from analysis perspective. NEW - just created, not analyzed yet, FAST_OK - preliminary (fast) analysis completed, now running translations (\"TM\") analysis, DONE - analysis complete.  # noqa: E501

        :return: The status of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Summary.

        The status the project is from analysis perspective. NEW - just created, not analyzed yet, FAST_OK - preliminary (fast) analysis completed, now running translations (\"TM\") analysis, DONE - analysis complete.  # noqa: E501

        :param status: The status of this Summary.  # noqa: E501
        :type: str
        """
        allowed_values = ["NEW", "FAST_OK", "DONE"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def in_queue_before(self):
        """Gets the in_queue_before of this Summary.  # noqa: E501

        Number of segments belonging to other projects that are being analyzed before yours; it's the wait time for you.  # noqa: E501

        :return: The in_queue_before of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._in_queue_before

    @in_queue_before.setter
    def in_queue_before(self, in_queue_before):
        """Sets the in_queue_before of this Summary.

        Number of segments belonging to other projects that are being analyzed before yours; it's the wait time for you.  # noqa: E501

        :param in_queue_before: The in_queue_before of this Summary.  # noqa: E501
        :type: str
        """

        self._in_queue_before = in_queue_before

    @property
    def total_segments(self):
        """Gets the total_segments of this Summary.  # noqa: E501

        number of segments belonging to your project.  # noqa: E501

        :return: The total_segments of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._total_segments

    @total_segments.setter
    def total_segments(self, total_segments):
        """Sets the total_segments of this Summary.

        number of segments belonging to your project.  # noqa: E501

        :param total_segments: The total_segments of this Summary.  # noqa: E501
        :type: str
        """

        self._total_segments = total_segments

    @property
    def segments_analyzed(self):
        """Gets the segments_analyzed of this Summary.  # noqa: E501

        analysis progress, on TOTAL_SEGMENTS  # noqa: E501

        :return: The segments_analyzed of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._segments_analyzed

    @segments_analyzed.setter
    def segments_analyzed(self, segments_analyzed):
        """Sets the segments_analyzed of this Summary.

        analysis progress, on TOTAL_SEGMENTS  # noqa: E501

        :param segments_analyzed: The segments_analyzed of this Summary.  # noqa: E501
        :type: str
        """

        self._segments_analyzed = segments_analyzed

    @property
    def total_raw_wc(self):
        """Gets the total_raw_wc of this Summary.  # noqa: E501

        number of words (word count) of your project, as extracted by the textual parsers  # noqa: E501

        :return: The total_raw_wc of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._total_raw_wc

    @total_raw_wc.setter
    def total_raw_wc(self, total_raw_wc):
        """Sets the total_raw_wc of this Summary.

        number of words (word count) of your project, as extracted by the textual parsers  # noqa: E501

        :param total_raw_wc: The total_raw_wc of this Summary.  # noqa: E501
        :type: str
        """

        self._total_raw_wc = total_raw_wc

    @property
    def total_standard_wc(self):
        """Gets the total_standard_wc of this Summary.  # noqa: E501

        word count, minus the sentences that are repeated  # noqa: E501

        :return: The total_standard_wc of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._total_standard_wc

    @total_standard_wc.setter
    def total_standard_wc(self, total_standard_wc):
        """Sets the total_standard_wc of this Summary.

        word count, minus the sentences that are repeated  # noqa: E501

        :param total_standard_wc: The total_standard_wc of this Summary.  # noqa: E501
        :type: str
        """

        self._total_standard_wc = total_standard_wc

    @property
    def total_fast_wc(self):
        """Gets the total_fast_wc of this Summary.  # noqa: E501

        word count, minus the sentences that are partially repeated  # noqa: E501

        :return: The total_fast_wc of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._total_fast_wc

    @total_fast_wc.setter
    def total_fast_wc(self, total_fast_wc):
        """Sets the total_fast_wc of this Summary.

        word count, minus the sentences that are partially repeated  # noqa: E501

        :param total_fast_wc: The total_fast_wc of this Summary.  # noqa: E501
        :type: str
        """

        self._total_fast_wc = total_fast_wc

    @property
    def total_tm_wc(self):
        """Gets the total_tm_wc of this Summary.  # noqa: E501

        word count, with sentences found in the cloud translation memory discounted from the total; this depends on the percentage of overlapping between the sentences of your project and the past translations  # noqa: E501

        :return: The total_tm_wc of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._total_tm_wc

    @total_tm_wc.setter
    def total_tm_wc(self, total_tm_wc):
        """Sets the total_tm_wc of this Summary.

        word count, with sentences found in the cloud translation memory discounted from the total; this depends on the percentage of overlapping between the sentences of your project and the past translations  # noqa: E501

        :param total_tm_wc: The total_tm_wc of this Summary.  # noqa: E501
        :type: str
        """

        self._total_tm_wc = total_tm_wc

    @property
    def total_payable(self):
        """Gets the total_payable of this Summary.  # noqa: E501

        total word count, after analysis.  # noqa: E501

        :return: The total_payable of this Summary.  # noqa: E501
        :rtype: str
        """
        return self._total_payable

    @total_payable.setter
    def total_payable(self, total_payable):
        """Sets the total_payable of this Summary.

        total word count, after analysis.  # noqa: E501

        :param total_payable: The total_payable of this Summary.  # noqa: E501
        :type: str
        """

        self._total_payable = total_payable

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
        if issubclass(Summary, dict):
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
        if not isinstance(other, Summary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class JobsStatus(object):
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
        'langpairs': 'object',
        'job_url': 'object',
        'job_quality_details': 'list[object]',
        'quality_overall': 'object'
    }

    attribute_map = {
        'langpairs': 'langpairs',
        'job_url': 'job-url',
        'job_quality_details': 'job-quality-details',
        'quality_overall': 'quality-overall'
    }

    def __init__(self, langpairs=None, job_url=None, job_quality_details=None, quality_overall=None):  # noqa: E501
        """JobsStatus - a model defined in Swagger"""  # noqa: E501
        self._langpairs = None
        self._job_url = None
        self._job_quality_details = None
        self._quality_overall = None
        self.discriminator = None
        if langpairs is not None:
            self.langpairs = langpairs
        if job_url is not None:
            self.job_url = job_url
        if job_quality_details is not None:
            self.job_quality_details = job_quality_details
        if quality_overall is not None:
            self.quality_overall = quality_overall

    @property
    def langpairs(self):
        """Gets the langpairs of this JobsStatus.  # noqa: E501

        the language pairs for your project; an entry for every chunk in the project, with the id-password combination as key and the language pair as the value  # noqa: E501

        :return: The langpairs of this JobsStatus.  # noqa: E501
        :rtype: object
        """
        return self._langpairs

    @langpairs.setter
    def langpairs(self, langpairs):
        """Sets the langpairs of this JobsStatus.

        the language pairs for your project; an entry for every chunk in the project, with the id-password combination as key and the language pair as the value  # noqa: E501

        :param langpairs: The langpairs of this JobsStatus.  # noqa: E501
        :type: object
        """

        self._langpairs = langpairs

    @property
    def job_url(self):
        """Gets the job_url of this JobsStatus.  # noqa: E501

        the links to the chunks of the project; an entry for every chunk in the project, with the id-password combination as key and the link to the chunk as the value.  # noqa: E501

        :return: The job_url of this JobsStatus.  # noqa: E501
        :rtype: object
        """
        return self._job_url

    @job_url.setter
    def job_url(self, job_url):
        """Sets the job_url of this JobsStatus.

        the links to the chunks of the project; an entry for every chunk in the project, with the id-password combination as key and the link to the chunk as the value.  # noqa: E501

        :param job_url: The job_url of this JobsStatus.  # noqa: E501
        :type: object
        """

        self._job_url = job_url

    @property
    def job_quality_details(self):
        """Gets the job_quality_details of this JobsStatus.  # noqa: E501

        a structure containing, for each chunk, an array of 5 objects, each object is a quality check performed on the job; the object contains the type of the check (Typing, Translation, Terminology, Language Quality, Style), the quantity of errors found, the allowed errors threshold and the rating given by the errors/threshold ratio (same as quality-overall)  # noqa: E501

        :return: The job_quality_details of this JobsStatus.  # noqa: E501
        :rtype: list[object]
        """
        return self._job_quality_details

    @job_quality_details.setter
    def job_quality_details(self, job_quality_details):
        """Sets the job_quality_details of this JobsStatus.

        a structure containing, for each chunk, an array of 5 objects, each object is a quality check performed on the job; the object contains the type of the check (Typing, Translation, Terminology, Language Quality, Style), the quantity of errors found, the allowed errors threshold and the rating given by the errors/threshold ratio (same as quality-overall)  # noqa: E501

        :param job_quality_details: The job_quality_details of this JobsStatus.  # noqa: E501
        :type: list[object]
        """

        self._job_quality_details = job_quality_details

    @property
    def quality_overall(self):
        """Gets the quality_overall of this JobsStatus.  # noqa: E501

        the overall quality rating for each chunk (Very good, Good, Acceptable, Poor, Fail)  # noqa: E501

        :return: The quality_overall of this JobsStatus.  # noqa: E501
        :rtype: object
        """
        return self._quality_overall

    @quality_overall.setter
    def quality_overall(self, quality_overall):
        """Sets the quality_overall of this JobsStatus.

        the overall quality rating for each chunk (Very good, Good, Acceptable, Poor, Fail)  # noqa: E501

        :param quality_overall: The quality_overall of this JobsStatus.  # noqa: E501
        :type: object
        """

        self._quality_overall = quality_overall

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
        if issubclass(JobsStatus, dict):
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
        if not isinstance(other, JobsStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

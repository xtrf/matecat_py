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

class Body(object):
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
        'files': 'str',
        'project_name': 'str',
        'source_lang': 'str',
        'target_lang': 'str',
        'tms_engine': 'int',
        'mt_engine': 'int',
        'private_tm_key': 'str',
        'subject': 'str',
        'segmentation_rule': 'str',
        'owner_email': 'str',
        'due_date': 'str',
        'id_team': 'str',
        'lexiqa': 'str',
        'speech2text': 'int',
        'get_public_matches': 'str',
        'pretranslate_100': 'int',
        'metadata': 'str'
    }

    attribute_map = {
        'files': 'files',
        'project_name': 'project_name',
        'source_lang': 'source_lang',
        'target_lang': 'target_lang',
        'tms_engine': 'tms_engine',
        'mt_engine': 'mt_engine',
        'private_tm_key': 'private_tm_key',
        'subject': 'subject',
        'segmentation_rule': 'segmentation_rule',
        'owner_email': 'owner_email',
        'due_date': 'due_date',
        'id_team': 'id_team',
        'lexiqa': 'lexiqa',
        'speech2text': 'speech2text',
        'get_public_matches': 'get_public_matches',
        'pretranslate_100': 'pretranslate_100',
        'metadata': 'metadata'
    }

    def __init__(self, files=None, project_name=None, source_lang=None, target_lang=None, tms_engine=1, mt_engine=1, private_tm_key=None, subject='general', segmentation_rule=None, owner_email='anonymous', due_date=None, id_team=None, lexiqa='0', speech2text=0, get_public_matches='true', pretranslate_100=0, metadata=None):  # noqa: E501
        """Body - a model defined in Swagger"""  # noqa: E501
        self._files = None
        self._project_name = None
        self._source_lang = None
        self._target_lang = None
        self._tms_engine = None
        self._mt_engine = None
        self._private_tm_key = None
        self._subject = None
        self._segmentation_rule = None
        self._owner_email = None
        self._due_date = None
        self._id_team = None
        self._lexiqa = None
        self._speech2text = None
        self._get_public_matches = None
        self._pretranslate_100 = None
        self._metadata = None
        self.discriminator = None
        self.files = files
        self.project_name = project_name
        self.source_lang = source_lang
        self.target_lang = target_lang
        if tms_engine is not None:
            self.tms_engine = tms_engine
        if mt_engine is not None:
            self.mt_engine = mt_engine
        if private_tm_key is not None:
            self.private_tm_key = private_tm_key
        if subject is not None:
            self.subject = subject
        if segmentation_rule is not None:
            self.segmentation_rule = segmentation_rule
        if owner_email is not None:
            self.owner_email = owner_email
        if due_date is not None:
            self.due_date = due_date
        if id_team is not None:
            self.id_team = id_team
        if lexiqa is not None:
            self.lexiqa = lexiqa
        if speech2text is not None:
            self.speech2text = speech2text
        if get_public_matches is not None:
            self.get_public_matches = get_public_matches
        if pretranslate_100 is not None:
            self.pretranslate_100 = pretranslate_100
        if metadata is not None:
            self.metadata = metadata

    @property
    def files(self):
        """Gets the files of this Body.  # noqa: E501

        The file(s) to be uploaded. You may also upload your own translation memories (TMX).  # noqa: E501

        :return: The files of this Body.  # noqa: E501
        :rtype: str
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Body.

        The file(s) to be uploaded. You may also upload your own translation memories (TMX).  # noqa: E501

        :param files: The files of this Body.  # noqa: E501
        :type: str
        """
        if files is None:
            raise ValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = files

    @property
    def project_name(self):
        """Gets the project_name of this Body.  # noqa: E501

        The name of the project you want create.  # noqa: E501

        :return: The project_name of this Body.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this Body.

        The name of the project you want create.  # noqa: E501

        :param project_name: The project_name of this Body.  # noqa: E501
        :type: str
        """
        if project_name is None:
            raise ValueError("Invalid value for `project_name`, must not be `None`")  # noqa: E501

        self._project_name = project_name

    @property
    def source_lang(self):
        """Gets the source_lang of this Body.  # noqa: E501

        RFC 5646 language+region Code ( en-US case sensitive ) as specified in W3C standards.  # noqa: E501

        :return: The source_lang of this Body.  # noqa: E501
        :rtype: str
        """
        return self._source_lang

    @source_lang.setter
    def source_lang(self, source_lang):
        """Sets the source_lang of this Body.

        RFC 5646 language+region Code ( en-US case sensitive ) as specified in W3C standards.  # noqa: E501

        :param source_lang: The source_lang of this Body.  # noqa: E501
        :type: str
        """
        if source_lang is None:
            raise ValueError("Invalid value for `source_lang`, must not be `None`")  # noqa: E501

        self._source_lang = source_lang

    @property
    def target_lang(self):
        """Gets the target_lang of this Body.  # noqa: E501

        RFC 5646 language+region Code ( en-US case sensitive ) as specified in W3C standards. Multiple languages must be comma separated ( it-IT,fr-FR,es-ES case sensitive)  # noqa: E501

        :return: The target_lang of this Body.  # noqa: E501
        :rtype: str
        """
        return self._target_lang

    @target_lang.setter
    def target_lang(self, target_lang):
        """Sets the target_lang of this Body.

        RFC 5646 language+region Code ( en-US case sensitive ) as specified in W3C standards. Multiple languages must be comma separated ( it-IT,fr-FR,es-ES case sensitive)  # noqa: E501

        :param target_lang: The target_lang of this Body.  # noqa: E501
        :type: str
        """
        if target_lang is None:
            raise ValueError("Invalid value for `target_lang`, must not be `None`")  # noqa: E501

        self._target_lang = target_lang

    @property
    def tms_engine(self):
        """Gets the tms_engine of this Body.  # noqa: E501

        Identifier for Memory Server 0 means disabled, 1 means MyMemory)  # noqa: E501

        :return: The tms_engine of this Body.  # noqa: E501
        :rtype: int
        """
        return self._tms_engine

    @tms_engine.setter
    def tms_engine(self, tms_engine):
        """Sets the tms_engine of this Body.

        Identifier for Memory Server 0 means disabled, 1 means MyMemory)  # noqa: E501

        :param tms_engine: The tms_engine of this Body.  # noqa: E501
        :type: int
        """

        self._tms_engine = tms_engine

    @property
    def mt_engine(self):
        """Gets the mt_engine of this Body.  # noqa: E501

        Identifier for Machine Translation Service 0 means disabled, 1 means get MT from MyMemory).  # noqa: E501

        :return: The mt_engine of this Body.  # noqa: E501
        :rtype: int
        """
        return self._mt_engine

    @mt_engine.setter
    def mt_engine(self, mt_engine):
        """Sets the mt_engine of this Body.

        Identifier for Machine Translation Service 0 means disabled, 1 means get MT from MyMemory).  # noqa: E501

        :param mt_engine: The mt_engine of this Body.  # noqa: E501
        :type: int
        """

        self._mt_engine = mt_engine

    @property
    def private_tm_key(self):
        """Gets the private_tm_key of this Body.  # noqa: E501

        Private key(s) for MyMemory.  If a TMX file is uploaded and no key is provided, a new key will be created. - Existing MyMemory private keys or new to create a new key. - Multiple keys must be comma separated. Up to 5 keys allowed. (xxx345cvf,new,s342f234fc) - If you want to set read, write or both on your private key you can add after the key 'r' for read, 'w' for write or 'rw' for both  separated by ':' (xxx345cvf:r,new:w,s342f234fc:rw) - Only available if tms_engine is set to 1 or if is not used  # noqa: E501

        :return: The private_tm_key of this Body.  # noqa: E501
        :rtype: str
        """
        return self._private_tm_key

    @private_tm_key.setter
    def private_tm_key(self, private_tm_key):
        """Sets the private_tm_key of this Body.

        Private key(s) for MyMemory.  If a TMX file is uploaded and no key is provided, a new key will be created. - Existing MyMemory private keys or new to create a new key. - Multiple keys must be comma separated. Up to 5 keys allowed. (xxx345cvf,new,s342f234fc) - If you want to set read, write or both on your private key you can add after the key 'r' for read, 'w' for write or 'rw' for both  separated by ':' (xxx345cvf:r,new:w,s342f234fc:rw) - Only available if tms_engine is set to 1 or if is not used  # noqa: E501

        :param private_tm_key: The private_tm_key of this Body.  # noqa: E501
        :type: str
        """

        self._private_tm_key = private_tm_key

    @property
    def subject(self):
        """Gets the subject of this Body.  # noqa: E501

        The subject of the project you want to create.  # noqa: E501

        :return: The subject of this Body.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Body.

        The subject of the project you want to create.  # noqa: E501

        :param subject: The subject of this Body.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def segmentation_rule(self):
        """Gets the segmentation_rule of this Body.  # noqa: E501

        The segmentation rule you want to use to parse your file.  # noqa: E501

        :return: The segmentation_rule of this Body.  # noqa: E501
        :rtype: str
        """
        return self._segmentation_rule

    @segmentation_rule.setter
    def segmentation_rule(self, segmentation_rule):
        """Sets the segmentation_rule of this Body.

        The segmentation rule you want to use to parse your file.  # noqa: E501

        :param segmentation_rule: The segmentation_rule of this Body.  # noqa: E501
        :type: str
        """

        self._segmentation_rule = segmentation_rule

    @property
    def owner_email(self):
        """Gets the owner_email of this Body.  # noqa: E501

        The email of the owner of the project. This parameter is deprecated and being replaced by authentication headers.  # noqa: E501

        :return: The owner_email of this Body.  # noqa: E501
        :rtype: str
        """
        return self._owner_email

    @owner_email.setter
    def owner_email(self, owner_email):
        """Sets the owner_email of this Body.

        The email of the owner of the project. This parameter is deprecated and being replaced by authentication headers.  # noqa: E501

        :param owner_email: The owner_email of this Body.  # noqa: E501
        :type: str
        """

        self._owner_email = owner_email

    @property
    def due_date(self):
        """Gets the due_date of this Body.  # noqa: E501

        If you want to set a due date for your project, send this param with a timestamp  # noqa: E501

        :return: The due_date of this Body.  # noqa: E501
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this Body.

        If you want to set a due date for your project, send this param with a timestamp  # noqa: E501

        :param due_date: The due_date of this Body.  # noqa: E501
        :type: str
        """

        self._due_date = due_date

    @property
    def id_team(self):
        """Gets the id_team of this Body.  # noqa: E501

        The team you want to assign this project  # noqa: E501

        :return: The id_team of this Body.  # noqa: E501
        :rtype: str
        """
        return self._id_team

    @id_team.setter
    def id_team(self, id_team):
        """Sets the id_team of this Body.

        The team you want to assign this project  # noqa: E501

        :param id_team: The id_team of this Body.  # noqa: E501
        :type: str
        """

        self._id_team = id_team

    @property
    def lexiqa(self):
        """Gets the lexiqa of this Body.  # noqa: E501

        Enable lexiQA QA check. Requires purchase of a license from lexiQA.  # noqa: E501

        :return: The lexiqa of this Body.  # noqa: E501
        :rtype: str
        """
        return self._lexiqa

    @lexiqa.setter
    def lexiqa(self, lexiqa):
        """Sets the lexiqa of this Body.

        Enable lexiQA QA check. Requires purchase of a license from lexiQA.  # noqa: E501

        :param lexiqa: The lexiqa of this Body.  # noqa: E501
        :type: str
        """

        self._lexiqa = lexiqa

    @property
    def speech2text(self):
        """Gets the speech2text of this Body.  # noqa: E501

        Improved accessibility thanks to a speech-to-text component to dictate your translations instead of typing them.  # noqa: E501

        :return: The speech2text of this Body.  # noqa: E501
        :rtype: int
        """
        return self._speech2text

    @speech2text.setter
    def speech2text(self, speech2text):
        """Sets the speech2text of this Body.

        Improved accessibility thanks to a speech-to-text component to dictate your translations instead of typing them.  # noqa: E501

        :param speech2text: The speech2text of this Body.  # noqa: E501
        :type: int
        """

        self._speech2text = speech2text

    @property
    def get_public_matches(self):
        """Gets the get_public_matches of this Body.  # noqa: E501

        Enable suggestions from the Public TM  # noqa: E501

        :return: The get_public_matches of this Body.  # noqa: E501
        :rtype: str
        """
        return self._get_public_matches

    @get_public_matches.setter
    def get_public_matches(self, get_public_matches):
        """Sets the get_public_matches of this Body.

        Enable suggestions from the Public TM  # noqa: E501

        :param get_public_matches: The get_public_matches of this Body.  # noqa: E501
        :type: str
        """
        allowed_values = ["true", "false"]  # noqa: E501
        if get_public_matches not in allowed_values:
            raise ValueError(
                "Invalid value for `get_public_matches` ({0}), must be one of {1}"  # noqa: E501
                .format(get_public_matches, allowed_values)
            )

        self._get_public_matches = get_public_matches

    @property
    def pretranslate_100(self):
        """Gets the pretranslate_100 of this Body.  # noqa: E501

        Pre-translate 100% matches from TM  # noqa: E501

        :return: The pretranslate_100 of this Body.  # noqa: E501
        :rtype: int
        """
        return self._pretranslate_100

    @pretranslate_100.setter
    def pretranslate_100(self, pretranslate_100):
        """Sets the pretranslate_100 of this Body.

        Pre-translate 100% matches from TM  # noqa: E501

        :param pretranslate_100: The pretranslate_100 of this Body.  # noqa: E501
        :type: int
        """

        self._pretranslate_100 = pretranslate_100

    @property
    def metadata(self):
        """Gets the metadata of this Body.  # noqa: E501


        :return: The metadata of this Body.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Body.


        :param metadata: The metadata of this Body.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

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
        if issubclass(Body, dict):
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
        if not isinstance(other, Body):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

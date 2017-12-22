# coding: utf-8

"""
    Modelstore

    Machine Learning model store api   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: noonefornow@nowhere.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import pprint
import re  # noqa: F401

import six


class ModelData(object):
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
        'model_url': 'str',
        'version': 'float'
    }

    attribute_map = {
        'name': 'name',
        'model_url': 'modelUrl',
        'version': 'version'
    }

    def __init__(self, name=None, model_url=None, version=None):  # noqa: E501
        """ModelData - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._model_url = None
        self._version = None
        self.discriminator = None

        self.name = name
        self.model_url = model_url
        self.version = version

    @property
    def name(self):
        """Gets the name of this ModelData.  # noqa: E501


        :return: The name of this ModelData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelData.


        :param name: The name of this ModelData.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def model_url(self):
        """Gets the model_url of this ModelData.  # noqa: E501


        :return: The model_url of this ModelData.  # noqa: E501
        :rtype: str
        """
        return self._model_url

    @model_url.setter
    def model_url(self, model_url):
        """Sets the model_url of this ModelData.


        :param model_url: The model_url of this ModelData.  # noqa: E501
        :type: str
        """
        if model_url is None:
            raise ValueError("Invalid value for `model_url`, must not be `None`")  # noqa: E501

        self._model_url = model_url

    @property
    def version(self):
        """Gets the version of this ModelData.  # noqa: E501


        :return: The version of this ModelData.  # noqa: E501
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ModelData.


        :param version: The version of this ModelData.  # noqa: E501
        :type: float
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModelData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
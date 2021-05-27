# coding: utf-8

#
# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.
#

import pprint
import re  # noqa: F401
import six
import typing
from enum import Enum


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union, Any
    from datetime import datetime


class Challenge(object):
    """
    An Challenge completed by the user on the given day.


    :param id: A UUID identifying the Challenge.
    :type id: (optional) str
    :param name: A human-readable string describing the challenge the user completed.
    :type name: (optional) str
    :param object_type: An enumerated string describing what domain the challenge falls into. Values include &#39;ACTIVITY&#39;, &#39;SLEEP&#39;, &#39;MINDFULNESS&#39;, and &#39;NUTRITION&#39;.
    :type object_type: (optional) str
    :param start_date: The date the user started the Challenge, encoded as YYYY-MM-DD.
    :type start_date: (optional) str
    :param completion_date: The date the Challenge ended, encoded in YYYY-MM-DD.
    :type completion_date: (optional) str
    :param timestamp: The timestamp for when the Challenge was synced in extended ISO 8601 date/time format (yyyy-mm-ddThh:mm:ss.mmmZ).
    :type timestamp: (optional) str

    """
    deserialized_types = {
        'id': 'str',
        'name': 'str',
        'object_type': 'str',
        'start_date': 'str',
        'completion_date': 'str',
        'timestamp': 'str'
    }  # type: Dict

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'object_type': 'type',
        'start_date': 'startDate',
        'completion_date': 'completionDate',
        'timestamp': 'timestamp'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, id=None, name=None, object_type=None, start_date=None, completion_date=None, timestamp=None):
        # type: (Optional[str], Optional[str], Optional[str], Optional[str], Optional[str], Optional[str]) -> None
        """An Challenge completed by the user on the given day.

        :param id: A UUID identifying the Challenge.
        :type id: (optional) str
        :param name: A human-readable string describing the challenge the user completed.
        :type name: (optional) str
        :param object_type: An enumerated string describing what domain the challenge falls into. Values include &#39;ACTIVITY&#39;, &#39;SLEEP&#39;, &#39;MINDFULNESS&#39;, and &#39;NUTRITION&#39;.
        :type object_type: (optional) str
        :param start_date: The date the user started the Challenge, encoded as YYYY-MM-DD.
        :type start_date: (optional) str
        :param completion_date: The date the Challenge ended, encoded in YYYY-MM-DD.
        :type completion_date: (optional) str
        :param timestamp: The timestamp for when the Challenge was synced in extended ISO 8601 date/time format (yyyy-mm-ddThh:mm:ss.mmmZ).
        :type timestamp: (optional) str
        """
        self.__discriminator_value = None  # type: str

        self.id = id
        self.name = name
        self.object_type = object_type
        self.start_date = start_date
        self.completion_date = completion_date
        self.timestamp = timestamp

    def to_dict(self):
        # type: () -> Dict[str, object]
        """Returns the model properties as a dict"""
        result = {}  # type: Dict

        for attr, _ in six.iteritems(self.deserialized_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else
                    x.value if isinstance(x, Enum) else x,
                    value
                ))
            elif isinstance(value, Enum):
                result[attr] = value.value
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else
                    (item[0], item[1].value)
                    if isinstance(item[1], Enum) else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        # type: () -> str
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        # type: () -> str
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are equal"""
        if not isinstance(other, Challenge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other

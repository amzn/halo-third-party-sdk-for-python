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


class SleepDuration(object):
    """
    An object containing sleep duration data.


    :param total: Total time spent in various sleep stages over the course of the night in second.
    :type total: (optional) float
    :param in_bed: Total time spent in bed over the course of the night in seconds.
    :type in_bed: (optional) float
    :param awake_after_sleep: Total time spent awake after falling asleep in seconds.
    :type awake_after_sleep: (optional) float
    :param light_sleep: The total duration of time spent in light sleep in seconds.
    :type light_sleep: (optional) float
    :param deep_sleep: The total duration of time spent in deep sleep in seconds.
    :type deep_sleep: (optional) float
    :param rem_sleep: The total duration of time spent in REM sleep in seconds.
    :type rem_sleep: (optional) float

    """
    deserialized_types = {
        'total': 'float',
        'in_bed': 'float',
        'awake_after_sleep': 'float',
        'light_sleep': 'float',
        'deep_sleep': 'float',
        'rem_sleep': 'float'
    }  # type: Dict

    attribute_map = {
        'total': 'total',
        'in_bed': 'inBed',
        'awake_after_sleep': 'awakeAfterSleep',
        'light_sleep': 'lightSleep',
        'deep_sleep': 'deepSleep',
        'rem_sleep': 'remSleep'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, total=None, in_bed=None, awake_after_sleep=None, light_sleep=None, deep_sleep=None, rem_sleep=None):
        # type: (Optional[float], Optional[float], Optional[float], Optional[float], Optional[float], Optional[float]) -> None
        """An object containing sleep duration data.

        :param total: Total time spent in various sleep stages over the course of the night in second.
        :type total: (optional) float
        :param in_bed: Total time spent in bed over the course of the night in seconds.
        :type in_bed: (optional) float
        :param awake_after_sleep: Total time spent awake after falling asleep in seconds.
        :type awake_after_sleep: (optional) float
        :param light_sleep: The total duration of time spent in light sleep in seconds.
        :type light_sleep: (optional) float
        :param deep_sleep: The total duration of time spent in deep sleep in seconds.
        :type deep_sleep: (optional) float
        :param rem_sleep: The total duration of time spent in REM sleep in seconds.
        :type rem_sleep: (optional) float
        """
        self.__discriminator_value = None  # type: str

        self.total = total
        self.in_bed = in_bed
        self.awake_after_sleep = awake_after_sleep
        self.light_sleep = light_sleep
        self.deep_sleep = deep_sleep
        self.rem_sleep = rem_sleep

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
        if not isinstance(other, SleepDuration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other

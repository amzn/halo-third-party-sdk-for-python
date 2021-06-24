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
    from halo_third_party_sdk_model.sleep_score import SleepScore as SleepScore_4065bcdd
    from halo_third_party_sdk_model.sleep_duration import SleepDuration as SleepDuration_e0139bf7


class Sleep(object):
    """
    An object including the sleep data for the user on the given day.


    :param timestamp: The timestamp for when the data was synced in extended ISO 8601 date/time format (yyyy-mm-ddThh:mm:ss.mmmZ).
    :type timestamp: (optional) str
    :param score: 
    :type score: (optional) halo_third_party_sdk_model.sleep_score.SleepScore
    :param duration: 
    :type duration: (optional) halo_third_party_sdk_model.sleep_duration.SleepDuration
    :param efficiency: Percentage of time in bed that a user is asleep.
    :type efficiency: (optional) float
    :param onset_latency: Time to fall asleep in seconds.
    :type onset_latency: (optional) float
    :param number_of_awakenings: The number of times awoken during sleep for 5 or more minutes.
    :type number_of_awakenings: (optional) int
    :param modified: A boolean flag denoting if this sleep session information was modified by the user.
    :type modified: (optional) bool

    """
    deserialized_types = {
        'timestamp': 'str',
        'score': 'halo_third_party_sdk_model.sleep_score.SleepScore',
        'duration': 'halo_third_party_sdk_model.sleep_duration.SleepDuration',
        'efficiency': 'float',
        'onset_latency': 'float',
        'number_of_awakenings': 'int',
        'modified': 'bool'
    }  # type: Dict

    attribute_map = {
        'timestamp': 'timestamp',
        'score': 'score',
        'duration': 'duration',
        'efficiency': 'efficiency',
        'onset_latency': 'onsetLatency',
        'number_of_awakenings': 'numberOfAwakenings',
        'modified': 'modified'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, timestamp=None, score=None, duration=None, efficiency=None, onset_latency=None, number_of_awakenings=None, modified=None):
        # type: (Optional[str], Optional[SleepScore_4065bcdd], Optional[SleepDuration_e0139bf7], Optional[float], Optional[float], Optional[int], Optional[bool]) -> None
        """An object including the sleep data for the user on the given day.

        :param timestamp: The timestamp for when the data was synced in extended ISO 8601 date/time format (yyyy-mm-ddThh:mm:ss.mmmZ).
        :type timestamp: (optional) str
        :param score: 
        :type score: (optional) halo_third_party_sdk_model.sleep_score.SleepScore
        :param duration: 
        :type duration: (optional) halo_third_party_sdk_model.sleep_duration.SleepDuration
        :param efficiency: Percentage of time in bed that a user is asleep.
        :type efficiency: (optional) float
        :param onset_latency: Time to fall asleep in seconds.
        :type onset_latency: (optional) float
        :param number_of_awakenings: The number of times awoken during sleep for 5 or more minutes.
        :type number_of_awakenings: (optional) int
        :param modified: A boolean flag denoting if this sleep session information was modified by the user.
        :type modified: (optional) bool
        """
        self.__discriminator_value = None  # type: str

        self.timestamp = timestamp
        self.score = score
        self.duration = duration
        self.efficiency = efficiency
        self.onset_latency = onset_latency
        self.number_of_awakenings = number_of_awakenings
        self.modified = modified

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
        if not isinstance(other, Sleep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other

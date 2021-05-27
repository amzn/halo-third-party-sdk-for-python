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
    from halo_third_party_sdk_model.heart_rate import HeartRate as HeartRate_b817caf
    from halo_third_party_sdk_model.calorie_info import CalorieInfo as CalorieInfo_dfedd4eb
    from halo_third_party_sdk_model.step_info import StepInfo as StepInfo_c3062745


class ActivitySession(object):
    """
    An activity sessions completed by the user on the given day.


    :param id: A UUID identifying the activity session.
    :type id: (optional) str
    :param object_type: The type of activity that was completed.
    :type object_type: (optional) str
    :param start_date_time: The date and time the activity started, encoded in ISO8601 date/time format (yyyy-mm-ddThh:mm:ss.mmmZ).
    :type start_date_time: (optional) str
    :param end_date_time: The date and time the activity ended, encoded in ISO8601 date/time format (yyyy-mm-ddThh:mm:ss.mmmZ).
    :type end_date_time: (optional) str
    :param modified: A boolean flag denoting if this session information was modified by the user.
    :type modified: (optional) bool
    :param automatic: A boolean flag denoting if the session was automatically tracked (true) or manually entered.
    :type automatic: (optional) bool
    :param step_info: 
    :type step_info: (optional) halo_third_party_sdk_model.step_info.StepInfo
    :param heart_rate: 
    :type heart_rate: (optional) halo_third_party_sdk_model.heart_rate.HeartRate
    :param timestamp: The timestamp for when the session and associated data (e.g. heart rate) was synced in extended ISO 8601 date/time format (yyyy-mm-ddThh:mm:ss.mmmZ).
    :type timestamp: (optional) str
    :param calorie_info: 
    :type calorie_info: (optional) halo_third_party_sdk_model.calorie_info.CalorieInfo

    """
    deserialized_types = {
        'id': 'str',
        'object_type': 'str',
        'start_date_time': 'str',
        'end_date_time': 'str',
        'modified': 'bool',
        'automatic': 'bool',
        'step_info': 'halo_third_party_sdk_model.step_info.StepInfo',
        'heart_rate': 'halo_third_party_sdk_model.heart_rate.HeartRate',
        'timestamp': 'str',
        'calorie_info': 'halo_third_party_sdk_model.calorie_info.CalorieInfo'
    }  # type: Dict

    attribute_map = {
        'id': 'id',
        'object_type': 'type',
        'start_date_time': 'startDateTime',
        'end_date_time': 'endDateTime',
        'modified': 'modified',
        'automatic': 'automatic',
        'step_info': 'stepInfo',
        'heart_rate': 'heartRate',
        'timestamp': 'timestamp',
        'calorie_info': 'calorieInfo'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, id=None, object_type=None, start_date_time=None, end_date_time=None, modified=None, automatic=None, step_info=None, heart_rate=None, timestamp=None, calorie_info=None):
        # type: (Optional[str], Optional[str], Optional[str], Optional[str], Optional[bool], Optional[bool], Optional[StepInfo_c3062745], Optional[HeartRate_b817caf], Optional[str], Optional[CalorieInfo_dfedd4eb]) -> None
        """An activity sessions completed by the user on the given day.

        :param id: A UUID identifying the activity session.
        :type id: (optional) str
        :param object_type: The type of activity that was completed.
        :type object_type: (optional) str
        :param start_date_time: The date and time the activity started, encoded in ISO8601 date/time format (yyyy-mm-ddThh:mm:ss.mmmZ).
        :type start_date_time: (optional) str
        :param end_date_time: The date and time the activity ended, encoded in ISO8601 date/time format (yyyy-mm-ddThh:mm:ss.mmmZ).
        :type end_date_time: (optional) str
        :param modified: A boolean flag denoting if this session information was modified by the user.
        :type modified: (optional) bool
        :param automatic: A boolean flag denoting if the session was automatically tracked (true) or manually entered.
        :type automatic: (optional) bool
        :param step_info: 
        :type step_info: (optional) halo_third_party_sdk_model.step_info.StepInfo
        :param heart_rate: 
        :type heart_rate: (optional) halo_third_party_sdk_model.heart_rate.HeartRate
        :param timestamp: The timestamp for when the session and associated data (e.g. heart rate) was synced in extended ISO 8601 date/time format (yyyy-mm-ddThh:mm:ss.mmmZ).
        :type timestamp: (optional) str
        :param calorie_info: 
        :type calorie_info: (optional) halo_third_party_sdk_model.calorie_info.CalorieInfo
        """
        self.__discriminator_value = None  # type: str

        self.id = id
        self.object_type = object_type
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.modified = modified
        self.automatic = automatic
        self.step_info = step_info
        self.heart_rate = heart_rate
        self.timestamp = timestamp
        self.calorie_info = calorie_info

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
        if not isinstance(other, ActivitySession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other

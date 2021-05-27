#
# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the
# License.
#

__pip_package_name__ = 'halo-third-party-sdk-events'
__description__ = ('The Halo Third Party SDK Events package provides support for '
                   'verifying the authenticity of events.')
__url__ = 'https://github.com/amzn/halo-third-party-sdk-for-python'
__version__ = '1.0.0'
__author__ = 'Amazon Halo'
__author_email__ = 'healthtech-partner-engineering-support@amazon.com'
__license__ = 'Apache 2.0'
__keywords__ = ['Halo SDK', 'Amazon Halo']
__install_requires__ = ["halo-third-party-sdk-model>=1.0.0",
                        "cryptography>=3.2", "certvalidator>=0.11.1",
                        "freezegun>=0.3.15"]


# -*- coding: utf-8 -*-
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
import os

#: Header key to be used, to retrieve request header that contains the
#: URL for the certificate chain needed to verify the request signature.
SIGNATURE_CERT_CHAIN_URL_HEADER = "SignatureCertChainUrl"

#: Header key to be used, to retrieve request header that contains the
#: request signature.
SIGNATURE_HEADER = "SignatureSha256"

#: Case insensitive protocol to be checked on signature certificate url.
CERT_CHAIN_URL_PROTOCOL = "https"

#: Case insensitive hostname to be checked on signature certificate url.
CERT_CHAIN_URL_HOSTNAME = "s3.amazonaws.com"

#: Path presence to be checked on signature certificate url.
CERT_CHAIN_URL_STARTPATHS = [
    "{0}healthtech.api-alpha{0}".format(os.path.sep),
    "{0}healthtech.api-beta{0}".format(os.path.sep),
    "{0}healthtech.api{0}".format(os.path.sep)
]

#: Port to be checked on signature certificate url.
CERT_CHAIN_URL_PORT = 443

#: Domain presence check in Subject Alternative Names (SANs) of
#: signing certificate.
CERT_CHAIN_DOMAINS = [
    "na-alpha.events.partners.healthtech.a2z.com",
    "na-beta.events.partners.healthtech.a2z.com",
    "na.events.partners.healthtech.a2z.com",
    "na.events.partners.amazonhealthtech.com"
]

#: Character encoding used in the request.
CHARACTER_ENCODING = "utf-8"

#: Maximum allowable tolerance in request timestamp.
MAX_NORMAL_REQUEST_TOLERANCE_IN_MILLIS = 150000

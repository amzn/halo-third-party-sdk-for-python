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
import typing
from halo_third_party_sdk_model import RequestEnvelope

from .serialize import DefaultSerializer
from .verifier import RequestVerifier, TimestampVerifier

if typing.TYPE_CHECKING:
    from typing import Dict, Any, List
    from .verifier import AbstractVerifier


class EventVerificationHandler(object):
    """Event Verifier Handler for Halo events.

    This class can be used by third party developers to verify the
    authenticity of events.

    The boolean verify_signature variable configures if the request signature is 
    verified for each input request. The boolean verify_timestamp configures if the
    request timestamp is verified for each input request. Additionally,
    an optional list of verifiers can also be provided, to be applied
    on the input request.

    The `verify_request_and_dispatch` method provides the dispatch
    functionality that can be used as an entry point for skill
    invocation as web service.
    """
    def __init__(
            self, verify_signature=True,
            verify_timestamp=True, verifiers=None):
        # type: (EventVerificationHandler, bool, bool, List[AbstractVerifier]) -> None
        """.

        The boolean verify_signature variable configures if the request
        signature is verified for each input request. The boolean 
        verify_timestamp configures if the request timestamp is verified
        for each input request. Additionally, an optional list of verifiers
        can also be provided, to be applied on the input request.

        :param verify_signature: Enable request signature verification
        :type verify_signature: bool
        :param verify_timestamp: Enable request timestamp verification
        :type verify_timestamp: bool
        :param verifiers: Optional list of verifiers that needs to be
            applied to the input request
        :type verifiers: list[
            halo_third_party_sdk.verifiers.AbstractVerifier]
        """
        self._serializer = DefaultSerializer()
        self._verifiers = []  # type: List[AbstractVerifier]

        if verify_signature:
            self._verifiers.append(RequestVerifier())

        if verify_timestamp:
            self._verifiers.append(TimestampVerifier())

        if verifiers is not None:
            self._verifiers.extend(verifiers)


    def verify_request_and_dispatch(
            self, http_request_headers, http_request_body):
        # type: (Dict[str, Any], str) -> None
        """Entry point for event verification

        This method takes in the input request headers and request body,
        handles the deserialization of the input request to
        the :py:class:`halo_third_party_sdk_model.request_envelope.RequestEnvelope`
        object, and runs the input through registered verifiers

        :param http_request_headers: Request headers of the input
            request to the webservice
        :type http_request_headers: Dict[str, Any]
        :param http_request_body: Raw request body of the input request
            to the webservice
        :type http_request_body: str
        :return: Serialized response object returned by the skill
            instance, when invoked with the input request
        :rtype: str
        :raises: :py:class:`HaloSdkException`
            when skill deserialization, verification, invocation or
            serialization fails
        """
        request_envelope = self._serializer.deserialize(
            payload=http_request_body, obj_type=RequestEnvelope)

        for verifier in self._verifiers:
            verifier.verify(
                headers=http_request_headers,
                serialized_request_env=http_request_body,
                deserialized_request_env=request_envelope)

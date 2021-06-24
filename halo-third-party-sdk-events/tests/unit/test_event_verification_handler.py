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
import unittest

from halo_third_party_sdk_events.event_verification_handler import (
    EventVerificationHandler)
from halo_third_party_sdk_events.verifier import (
    RequestVerifier, TimestampVerifier, AbstractVerifier,
    VerificationException)

try:
    import mock
except ImportError:
    from unittest import mock


class TestEventVerificationHandler(unittest.TestCase):
    def setUp(self):
        self.mock_verifier = mock.MagicMock(spec=AbstractVerifier)

    def test_event_verification_handler_init_with_no_verifiers(self):
        test_event_verification_handler = EventVerificationHandler(verify_signature=False, verify_timestamp=False)

        default_verifiers = test_event_verification_handler._verifiers

        self.assertEqual(
            len(default_verifiers), 0,
            "Event verification handler initialized invalid number of "
            "default verifiers")

    def test_event_verification_handler_init_with_default_verifiers(self):
        test_event_verification_handler = EventVerificationHandler()

        default_verifiers = test_event_verification_handler._verifiers

        self.assertEqual(
            len(default_verifiers), 2,
            "Event verification handler initialized invalid number of "
            "default verifiers")

        for verifier in default_verifiers:
            if not (isinstance(verifier, RequestVerifier) or
                    isinstance(verifier, TimestampVerifier)):
                self.fail(
                    "Event verification handler initialized invalid verifier "
                    "when left as default")

    def test_event_verification_handler_init_with_verifiers_set_correctly(
            self):
        test_verifier = mock.MagicMock(spec=AbstractVerifier)
        test_verifier.return_value = "Test"
        test_event_verification_handler = EventVerificationHandler(
            verify_signature=None, verify_timestamp=None, 
            verifiers=[test_verifier()]
        )

        default_verifiers = test_event_verification_handler._verifiers

        self.assertEqual(
            len(default_verifiers), 1,
            "Event verification handler initialized invalid number of "
            "verifiers, when an input list is passed")

        for verifier in default_verifiers:
            self.assertEqual(
                verifier, "Test",
                "Webservice skill handler initialized invalid verifier "
                "when an input list is passed")

    def test_event_verification_handler_init_default_with_verifiers_set_correctly(
            self):
        test_verifier = mock.MagicMock(spec=AbstractVerifier)
        test_verifier.return_value = "Test"
        test_event_verification_handler = EventVerificationHandler(verifiers=[test_verifier()])

        default_verifiers = test_event_verification_handler._verifiers

        self.assertEqual(
            len(default_verifiers), 3,
            "Event verification handler initialized invalid number of "
            "verifiers, when an input list is passed")

    def test_event_verification_handler_init_timestamp_check_disabled(self):
        test_event_verification_handler = EventVerificationHandler(verify_timestamp=False)

        default_verifiers = test_event_verification_handler._verifiers

        self.assertEqual(
            len(default_verifiers), 1,
            "Event verification handler initialized invalid number of "
            "default verifiers, when timestamp verification env property is "
            "disabled")

        verifier = default_verifiers[0]
        self.assertIsInstance(
            verifier, RequestVerifier,
            "Event verification handler initialized invalid default verifier, "
            "when request timestamp verification env property is set to false")

    def test_event_verification_handler_init_signature_check_disabled(self):
        test_event_verification_handler = EventVerificationHandler(verify_signature=False)

        default_verifiers = test_event_verification_handler._verifiers

        self.assertEqual(
            len(default_verifiers), 1,
            "Event verification handler initialized invalid number of "
            "default verifiers, when signature verification env property is "
            "disabled")

        verifier = default_verifiers[0]
        self.assertIsInstance(
            verifier, TimestampVerifier,
            "Event verification handler initialized invalid default verifier, "
            "when request signature verification env property is set to false")

    def test_event_verification_handler_dispatch_verification_failure_throw_exc(
            self):
        self.mock_verifier.verify.side_effect = VerificationException(
            "test verification exception")
        test_event_verification_handler = EventVerificationHandler(
            verify_signature=False, verify_timestamp=False,
            verifiers=[self.mock_verifier]
        )

        with self.assertRaises(VerificationException) as exc:
            test_event_verification_handler.verify_request_and_dispatch(
                http_request_headers=None, http_request_body=None)

        self.assertIn(
            "test verification exception", str(exc.exception),
            "Event verification handler didn't raise verification exception "
            "during skill dispatch")

    def test_event_verification_handler_dispatch_runs_verification_skill_invoke(
            self):
        try:
            test_event_verification_handler = EventVerificationHandler(
                verify_signature=False,
                verify_timestamp=False, verifiers=[self.mock_verifier])
            test_event_verification_handler.verify_request_and_dispatch(
                http_request_headers=None, http_request_body=None)
        except:
            self.fail(
                "Event verification handler failed request verification "
                "and request dispatch for a valid input request")


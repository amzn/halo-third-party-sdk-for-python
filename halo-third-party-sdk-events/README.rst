===================================================================================
Halo Third Party SDK Events - Base components for verifying Halo Events
===================================================================================

Halo Third Party SDK Events package is an extension package that will let developers verify the authenticity of events.

What is Halo Third Party SDK for Python
----------------------------------------

The Halo Third Party SDK for Python makes it easier for you to verify events and allows you to spend more time on implementing features and less on writing boiler-plate code.

Quick Start
-----------

Installation
~~~~~~~~~~~~~

.. important::

    `cryptography` is a dependency for this package. If you have not
    already installed
    `cryptography <https://cryptography.io/en/latest/>`_, you might need to
    install additional prerequisites as detailed in the
    `cryptography installation guide <https://cryptography.io/en/latest/installation/>`_
    for your operating system.

Assuming that you have Python and ``virtualenv`` installed, you can
install the package from PyPi as follows:

.. code-block:: sh

    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install halo-third-party-sdk-events

This package is not installed along-side `halo-third-party-sdk-events` standard distribution,
and has to be installed separately.


Usage and Getting Started
-------------------------

**Example usage**

.. code-block:: sh

    # 1. Import the necessary modules.
    import halo_third_party_sdk_events.event_verification_handler

    # 2. Create handler object, if no arguments supplied both time and signature verifiers are used.
    verifier = halo_third_party_sdk_events.event_verification_handler.EventVerificationHandler()

    # 3. Call verify request with request headers and event body.
    verifier.verify_request_and_dispatch(requestHeaders, body)


Opening Issues
--------------
For bug reports, feature requests and questions, we would like to hear about it. Search the [existing issues](https://github.com/amzn/halo-third-party-sdk-for-python/issues) and try to make sure your problem doesn’t already exist before opening a new issue. It’s helpful if you include the version of the SDK and Python you are using. Please include a stack trace and reduced repro case when appropriate.

License
-------
This SDK is distributed under the Apache License, Version 2.0, see LICENSE for more information.

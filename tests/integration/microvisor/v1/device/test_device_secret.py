# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class DeviceSecretTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.microvisor.v1.devices("UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .device_secrets.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://microvisor.twilio.com/v1/Devices/UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Secrets',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "secrets": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://microvisor.twilio.com/v1/Devices/UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Secrets?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://microvisor.twilio.com/v1/Devices/UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Secrets?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "secrets"
                }
            }
            '''
        ))

        actual = self.client.microvisor.v1.devices("UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .device_secrets.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "secrets": [
                    {
                        "device_sid": "UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "key": "first",
                        "date_rotated": "2021-01-01T12:34:56Z",
                        "url": "https://microvisor.twilio.com/v1/Devices/UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Secrets/first"
                    },
                    {
                        "device_sid": "UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "key": "second",
                        "date_rotated": "2021-01-01T12:34:57Z",
                        "url": "https://microvisor.twilio.com/v1/Devices/UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Secrets/second"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://microvisor.twilio.com/v1/Devices/UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Secrets?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://microvisor.twilio.com/v1/Devices/UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Secrets?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "secrets"
                }
            }
            '''
        ))

        actual = self.client.microvisor.v1.devices("UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .device_secrets.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.microvisor.v1.devices("UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .device_secrets("key").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://microvisor.twilio.com/v1/Devices/UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Secrets/key',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "device_sid": "UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "key": "first",
                "date_rotated": "2021-01-01T12:34:57Z",
                "url": "https://microvisor.twilio.com/v1/Devices/UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Secrets/first"
            }
            '''
        ))

        actual = self.client.microvisor.v1.devices("UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .device_secrets("key").fetch()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.microvisor.v1.devices("UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .device_secrets.create(key="key", value="value")

        values = {'Key': "key", 'Value': "value", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://microvisor.twilio.com/v1/Devices/UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Secrets',
            data=values,
        ))

    def test_create_account_secret_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "device_sid": "UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "key": "first",
                "date_rotated": "2021-01-01T12:34:56Z",
                "url": "https://microvisor.twilio.com/v1/Devices/UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Secrets/first"
            }
            '''
        ))

        actual = self.client.microvisor.v1.devices("UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .device_secrets.create(key="key", value="value")

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.microvisor.v1.devices("UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .device_secrets("key").update(value="value")

        values = {'Value': "value", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://microvisor.twilio.com/v1/Devices/UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Secrets/key',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "device_sid": "UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "key": "first",
                "date_rotated": "2021-01-01T12:34:56Z",
                "url": "https://microvisor.twilio.com/v1/Devices/UVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Secrets/first"
            }
            '''
        ))

        actual = self.client.microvisor.v1.devices("UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .device_secrets("key").update(value="value")

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.microvisor.v1.devices("UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .device_secrets("key").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://microvisor.twilio.com/v1/Devices/UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Secrets/key',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.microvisor.v1.devices("UVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .device_secrets("key").delete()

        self.assertTrue(actual)
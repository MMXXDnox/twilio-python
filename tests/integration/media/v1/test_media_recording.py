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


class MediaRecordingTestCase(IntegrationTestCase):

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.media.v1.media_recording("KVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://media.twilio.com/v1/MediaRecordings/KVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.media.v1.media_recording("KVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.media.v1.media_recording("KVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://media.twilio.com/v1/MediaRecordings/KVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "duration": 2147483647,
                "format": "mp4",
                "links": {
                    "media": "https://media.twilio.com/v1/MediaRecordings/KVcafebabecafebabecafebabecafebabe/Media",
                    "timed_metadata": "https://media.twilio.com/v1/MediaRecordings/KVcafebabecafebabecafebabecafebabe/TimedMetadata"
                },
                "processor_sid": "ZXcafebabecafebabecafebabecafebabe",
                "resolution": "640x480",
                "source_sid": "RMcafebabecafebabecafebabecafebabe",
                "sid": "KVcafebabecafebabecafebabecafebabe",
                "media_size": 2147483648,
                "status": "completed",
                "status_callback": "https://www.example.com",
                "status_callback_method": "POST",
                "url": "https://media.twilio.com/v1/MediaRecordings/KVcafebabecafebabecafebabecafebabe"
            }
            '''
        ))

        actual = self.client.media.v1.media_recording("KVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.media.v1.media_recording.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://media.twilio.com/v1/MediaRecordings',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 10,
                    "first_page_url": "https://media.twilio.com/v1/MediaRecordings?Status=processing&SourceSid=RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&ProcessorSid=ZXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&Order=asc&PageSize=10&Page=0",
                    "previous_page_url": null,
                    "url": "https://media.twilio.com/v1/MediaRecordings?Status=processing&SourceSid=RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&ProcessorSid=ZXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&Order=asc&PageSize=10&Page=0",
                    "next_page_url": null,
                    "key": "media_recordings"
                },
                "media_recordings": []
            }
            '''
        ))

        actual = self.client.media.v1.media_recording.list()

        self.assertIsNotNone(actual)

    def test_read_items_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 10,
                    "first_page_url": "https://media.twilio.com/v1/MediaRecordings?Status=completed&SourceSid=RMcafebabecafebabecafebabecafebabe&ProcessorSid=ZXcafebabecafebabecafebabecafebabe&Order=desc&PageSize=10&Page=0",
                    "previous_page_url": null,
                    "url": "https://media.twilio.com/v1/MediaRecordings?Status=completed&SourceSid=RMcafebabecafebabecafebabecafebabe&ProcessorSid=ZXcafebabecafebabecafebabecafebabe&Order=desc&PageSize=10&Page=0",
                    "next_page_url": null,
                    "key": "media_recordings"
                },
                "media_recordings": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "duration": 1000,
                        "format": "mp4",
                        "links": {
                            "media": "https://media.twilio.com/v1/MediaRecordings/KVcafebabecafebabecafebabecafebabe/Media",
                            "timed_metadata": "https://media.twilio.com/v1/MediaRecordings/KVcafebabecafebabecafebabecafebabe/TimedMetadata"
                        },
                        "processor_sid": "ZXcafebabecafebabecafebabecafebabe",
                        "resolution": "640x480",
                        "source_sid": "RMcafebabecafebabecafebabecafebabe",
                        "sid": "KVcafebabecafebabecafebabecafebabe",
                        "media_size": 1000,
                        "status": "completed",
                        "status_callback": "https://www.example.com",
                        "status_callback_method": "POST",
                        "url": "https://media.twilio.com/v1/MediaRecordings/KVcafebabecafebabecafebabecafebabe"
                    }
                ]
            }
            '''
        ))

        actual = self.client.media.v1.media_recording.list()

        self.assertIsNotNone(actual)

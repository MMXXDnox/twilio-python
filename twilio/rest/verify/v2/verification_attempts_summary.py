# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class VerificationAttemptsSummaryList(ListResource):

    def __init__(self, version):
        """
        Initialize the VerificationAttemptsSummaryList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryList
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryList
        """
        super(VerificationAttemptsSummaryList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self):
        """
        Constructs a VerificationAttemptsSummaryContext

        :returns: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryContext
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryContext
        """
        return VerificationAttemptsSummaryContext(self._version, )

    def __call__(self):
        """
        Constructs a VerificationAttemptsSummaryContext

        :returns: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryContext
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryContext
        """
        return VerificationAttemptsSummaryContext(self._version, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.VerificationAttemptsSummaryList>'


class VerificationAttemptsSummaryPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the VerificationAttemptsSummaryPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryPage
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryPage
        """
        super(VerificationAttemptsSummaryPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of VerificationAttemptsSummaryInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryInstance
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryInstance
        """
        return VerificationAttemptsSummaryInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.VerificationAttemptsSummaryPage>'


class VerificationAttemptsSummaryContext(InstanceContext):

    def __init__(self, version):
        """
        Initialize the VerificationAttemptsSummaryContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryContext
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryContext
        """
        super(VerificationAttemptsSummaryContext, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Attempts/Summary'.format(**self._solution)

    def fetch(self, service_sid=values.unset, date_created_after=values.unset,
              date_created_before=values.unset, country=values.unset,
              channel=values.unset, destination_prefix=values.unset):
        """
        Fetch the VerificationAttemptsSummaryInstance

        :param unicode service_sid: Filter the verification attempts considered on the summary by verify service.
        :param datetime date_created_after: Consider verification attempts create after this date on the summary.
        :param datetime date_created_before: Consider verification attempts created before this date on the summary.
        :param unicode country: Filter verification attempts considered on the summary by destination country.
        :param VerificationAttemptsSummaryInstance.Channels channel: Filter verification attempts considered on the summary by communication channel.
        :param unicode destination_prefix: Filters the attempts considered on the summary by destination prefix.

        :returns: The fetched VerificationAttemptsSummaryInstance
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryInstance
        """
        data = values.of({
            'ServiceSid': service_sid,
            'DateCreatedAfter': serialize.iso8601_datetime(date_created_after),
            'DateCreatedBefore': serialize.iso8601_datetime(date_created_before),
            'Country': country,
            'Channel': channel,
            'DestinationPrefix': destination_prefix,
        })

        payload = self._version.fetch(method='GET', uri=self._uri, params=data, )

        return VerificationAttemptsSummaryInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.VerificationAttemptsSummaryContext {}>'.format(context)


class VerificationAttemptsSummaryInstance(InstanceResource):

    class Channels(object):
        SMS = "sms"
        CALL = "call"
        EMAIL = "email"
        WHATSAPP = "whatsapp"

    def __init__(self, version, payload):
        """
        Initialize the VerificationAttemptsSummaryInstance

        :returns: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryInstance
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryInstance
        """
        super(VerificationAttemptsSummaryInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'total_attempts': deserialize.integer(payload.get('total_attempts')),
            'total_converted': deserialize.integer(payload.get('total_converted')),
            'total_unconverted': deserialize.integer(payload.get('total_unconverted')),
            'conversion_rate_percentage': deserialize.decimal(payload.get('conversion_rate_percentage')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: VerificationAttemptsSummaryContext for this VerificationAttemptsSummaryInstance
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryContext
        """
        if self._context is None:
            self._context = VerificationAttemptsSummaryContext(self._version, )
        return self._context

    @property
    def total_attempts(self):
        """
        :returns: Total of attempts made.
        :rtype: unicode
        """
        return self._properties['total_attempts']

    @property
    def total_converted(self):
        """
        :returns: Total of attempts confirmed by the end user.
        :rtype: unicode
        """
        return self._properties['total_converted']

    @property
    def total_unconverted(self):
        """
        :returns: Total of attempts made that were not confirmed by the end user.
        :rtype: unicode
        """
        return self._properties['total_unconverted']

    @property
    def conversion_rate_percentage(self):
        """
        :returns: Percentage of the confirmed messages over the total.
        :rtype: unicode
        """
        return self._properties['conversion_rate_percentage']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, service_sid=values.unset, date_created_after=values.unset,
              date_created_before=values.unset, country=values.unset,
              channel=values.unset, destination_prefix=values.unset):
        """
        Fetch the VerificationAttemptsSummaryInstance

        :param unicode service_sid: Filter the verification attempts considered on the summary by verify service.
        :param datetime date_created_after: Consider verification attempts create after this date on the summary.
        :param datetime date_created_before: Consider verification attempts created before this date on the summary.
        :param unicode country: Filter verification attempts considered on the summary by destination country.
        :param VerificationAttemptsSummaryInstance.Channels channel: Filter verification attempts considered on the summary by communication channel.
        :param unicode destination_prefix: Filters the attempts considered on the summary by destination prefix.

        :returns: The fetched VerificationAttemptsSummaryInstance
        :rtype: twilio.rest.verify.v2.verification_attempts_summary.VerificationAttemptsSummaryInstance
        """
        return self._proxy.fetch(
            service_sid=service_sid,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            country=country,
            channel=channel,
            destination_prefix=destination_prefix,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.VerificationAttemptsSummaryInstance {}>'.format(context)

# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class InsightsQuestionnairesList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the InsightsQuestionnairesList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesList
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesList
        """
        super(InsightsQuestionnairesList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Insights/QM/Questionnaires'.format(**self._solution)

    def create(self, name, description=values.unset, active=values.unset,
               question_ids=values.unset, token=values.unset):
        """
        Create the InsightsQuestionnairesInstance

        :param unicode name: The questionnaire name
        :param unicode description: The questionnaire description
        :param bool active: Is questionnaire enabled ?
        :param list[unicode] question_ids: The questionnaire question ids list
        :param unicode token: The Token HTTP request header

        :returns: The created InsightsQuestionnairesInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesInstance
        """
        data = values.of({
            'Name': name,
            'Description': description,
            'Active': active,
            'QuestionIds': serialize.map(question_ids, lambda e: e),
        })
        headers = values.of({'Token': token, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers, )

        return InsightsQuestionnairesInstance(self._version, payload, )

    def stream(self, include_inactive=values.unset, token=values.unset, limit=None,
               page_size=None):
        """
        Streams InsightsQuestionnairesInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param bool include_inactive: Include Inactive
        :param unicode token: The Token HTTP request header
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(include_inactive=include_inactive, token=token, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, include_inactive=values.unset, token=values.unset, limit=None,
             page_size=None):
        """
        Lists InsightsQuestionnairesInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param bool include_inactive: Include Inactive
        :param unicode token: The Token HTTP request header
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesInstance]
        """
        return list(self.stream(
            include_inactive=include_inactive,
            token=token,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, include_inactive=values.unset, token=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of InsightsQuestionnairesInstance records from the API.
        Request is executed immediately

        :param bool include_inactive: Include Inactive
        :param unicode token: The Token HTTP request header
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsQuestionnairesInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesPage
        """
        data = values.of({
            'IncludeInactive': include_inactive,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        headers = values.of({'Token': token, })

        response = self._version.page(method='GET', uri=self._uri, params=data, headers=headers, )

        return InsightsQuestionnairesPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of InsightsQuestionnairesInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InsightsQuestionnairesInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return InsightsQuestionnairesPage(self._version, response, self._solution)

    def get(self, id):
        """
        Constructs a InsightsQuestionnairesContext

        :param id: Unique Questionnaire ID

        :returns: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesContext
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesContext
        """
        return InsightsQuestionnairesContext(self._version, id=id, )

    def __call__(self, id):
        """
        Constructs a InsightsQuestionnairesContext

        :param id: Unique Questionnaire ID

        :returns: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesContext
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesContext
        """
        return InsightsQuestionnairesContext(self._version, id=id, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesList>'


class InsightsQuestionnairesPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the InsightsQuestionnairesPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesPage
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesPage
        """
        super(InsightsQuestionnairesPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of InsightsQuestionnairesInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesInstance
        """
        return InsightsQuestionnairesInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesPage>'


class InsightsQuestionnairesContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, id):
        """
        Initialize the InsightsQuestionnairesContext

        :param Version version: Version that contains the resource
        :param id: Unique Questionnaire ID

        :returns: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesContext
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesContext
        """
        super(InsightsQuestionnairesContext, self).__init__(version)

        # Path Solution
        self._solution = {'id': id, }
        self._uri = '/Insights/QM/Questionnaires/{id}'.format(**self._solution)

    def update(self, active, name=values.unset, description=values.unset,
               question_ids=values.unset, token=values.unset):
        """
        Update the InsightsQuestionnairesInstance

        :param bool active: Is questionnaire enabled ?
        :param unicode name: The questionnaire name
        :param unicode description: The questionnaire description
        :param list[unicode] question_ids: The questionnaire question ids list
        :param unicode token: The Token HTTP request header

        :returns: The updated InsightsQuestionnairesInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesInstance
        """
        data = values.of({
            'Active': active,
            'Name': name,
            'Description': description,
            'QuestionIds': serialize.map(question_ids, lambda e: e),
        })
        headers = values.of({'Token': token, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers, )

        return InsightsQuestionnairesInstance(self._version, payload, id=self._solution['id'], )

    def delete(self, token=values.unset):
        """
        Deletes the InsightsQuestionnairesInstance

        :param unicode token: The Token HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of({'Token': token, })

        return self._version.delete(method='DELETE', uri=self._uri, headers=headers, )

    def fetch(self, token=values.unset):
        """
        Fetch the InsightsQuestionnairesInstance

        :param unicode token: The Token HTTP request header

        :returns: The fetched InsightsQuestionnairesInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesInstance
        """
        headers = values.of({'Token': token, })

        payload = self._version.fetch(method='GET', uri=self._uri, headers=headers, )

        return InsightsQuestionnairesInstance(self._version, payload, id=self._solution['id'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesContext {}>'.format(context)


class InsightsQuestionnairesInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, id=None):
        """
        Initialize the InsightsQuestionnairesInstance

        :returns: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesInstance
        """
        super(InsightsQuestionnairesInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'id': payload.get('id'),
            'name': payload.get('name'),
            'description': payload.get('description'),
            'active': payload.get('active'),
            'questions': payload.get('questions'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'id': id or self._properties['id'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: InsightsQuestionnairesContext for this InsightsQuestionnairesInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesContext
        """
        if self._context is None:
            self._context = InsightsQuestionnairesContext(self._version, id=self._solution['id'], )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource and owns this Flex Insights
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def id(self):
        """
        :returns: The questionnaire id
        :rtype: unicode
        """
        return self._properties['id']

    @property
    def name(self):
        """
        :returns: The category name.
        :rtype: unicode
        """
        return self._properties['name']

    @property
    def description(self):
        """
        :returns: The questionnaire description
        :rtype: unicode
        """
        return self._properties['description']

    @property
    def active(self):
        """
        :returns: Is questionnaire enabled ?
        :rtype: bool
        """
        return self._properties['active']

    @property
    def questions(self):
        """
        :returns: The questions list
        :rtype: list[dict]
        """
        return self._properties['questions']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def update(self, active, name=values.unset, description=values.unset,
               question_ids=values.unset, token=values.unset):
        """
        Update the InsightsQuestionnairesInstance

        :param bool active: Is questionnaire enabled ?
        :param unicode name: The questionnaire name
        :param unicode description: The questionnaire description
        :param list[unicode] question_ids: The questionnaire question ids list
        :param unicode token: The Token HTTP request header

        :returns: The updated InsightsQuestionnairesInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesInstance
        """
        return self._proxy.update(
            active,
            name=name,
            description=description,
            question_ids=question_ids,
            token=token,
        )

    def delete(self, token=values.unset):
        """
        Deletes the InsightsQuestionnairesInstance

        :param unicode token: The Token HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(token=token, )

    def fetch(self, token=values.unset):
        """
        Fetch the InsightsQuestionnairesInstance

        :param unicode token: The Token HTTP request header

        :returns: The fetched InsightsQuestionnairesInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires.InsightsQuestionnairesInstance
        """
        return self._proxy.fetch(token=token, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesInstance {}>'.format(context)
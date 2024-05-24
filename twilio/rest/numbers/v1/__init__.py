r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Optional
from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.numbers.v1.bulk_eligibility import BulkEligibilityList
from twilio.rest.numbers.v1.eligibility import EligibilityList
from twilio.rest.numbers.v1.porting_port_in import PortingPortInList
from twilio.rest.numbers.v1.porting_port_in_phone_number import (
    PortingPortInPhoneNumberList,
)
from twilio.rest.numbers.v1.porting_portability import PortingPortabilityList
from twilio.rest.numbers.v1.porting_webhook_configuration import (
    PortingWebhookConfigurationList,
)
from twilio.rest.numbers.v1.porting_webhook_configuration_delete import (
    PortingWebhookConfigurationDeleteList,
)
from twilio.rest.numbers.v1.porting_webhook_configuration_fetch import (
    PortingWebhookConfigurationFetchList,
)


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Numbers

        :param domain: The Twilio.numbers domain
        """
        super().__init__(domain, "v1")
        self._bulk_eligibilities: Optional[BulkEligibilityList] = None
        self._eligibilities: Optional[EligibilityList] = None
        self._porting_port_ins: Optional[PortingPortInList] = None
        self._porting_port_in_phone_number: Optional[PortingPortInPhoneNumberList] = (
            None
        )
        self._porting_portabilities: Optional[PortingPortabilityList] = None
        self._porting_webhook_configurations: Optional[
            PortingWebhookConfigurationList
        ] = None
        self._porting_webhook_configurations_delete: Optional[
            PortingWebhookConfigurationDeleteList
        ] = None
        self._porting_webhook_configuration_fetch: Optional[
            PortingWebhookConfigurationFetchList
        ] = None

    @property
    def bulk_eligibilities(self) -> BulkEligibilityList:
        if self._bulk_eligibilities is None:
            self._bulk_eligibilities = BulkEligibilityList(self)
        return self._bulk_eligibilities

    @property
    def eligibilities(self) -> EligibilityList:
        if self._eligibilities is None:
            self._eligibilities = EligibilityList(self)
        return self._eligibilities

    @property
    def porting_port_ins(self) -> PortingPortInList:
        if self._porting_port_ins is None:
            self._porting_port_ins = PortingPortInList(self)
        return self._porting_port_ins

    @property
    def porting_port_in_phone_number(self) -> PortingPortInPhoneNumberList:
        if self._porting_port_in_phone_number is None:
            self._porting_port_in_phone_number = PortingPortInPhoneNumberList(self)
        return self._porting_port_in_phone_number

    @property
    def porting_portabilities(self) -> PortingPortabilityList:
        if self._porting_portabilities is None:
            self._porting_portabilities = PortingPortabilityList(self)
        return self._porting_portabilities

    @property
    def porting_webhook_configurations(self) -> PortingWebhookConfigurationList:
        if self._porting_webhook_configurations is None:
            self._porting_webhook_configurations = PortingWebhookConfigurationList(self)
        return self._porting_webhook_configurations

    @property
    def porting_webhook_configurations_delete(
        self,
    ) -> PortingWebhookConfigurationDeleteList:
        if self._porting_webhook_configurations_delete is None:
            self._porting_webhook_configurations_delete = (
                PortingWebhookConfigurationDeleteList(self)
            )
        return self._porting_webhook_configurations_delete

    @property
    def porting_webhook_configuration_fetch(
        self,
    ) -> PortingWebhookConfigurationFetchList:
        if self._porting_webhook_configuration_fetch is None:
            self._porting_webhook_configuration_fetch = (
                PortingWebhookConfigurationFetchList(self)
            )
        return self._porting_webhook_configuration_fetch

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V1>"

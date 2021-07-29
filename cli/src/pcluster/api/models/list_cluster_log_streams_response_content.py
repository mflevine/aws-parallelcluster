# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from pcluster.api import util
from pcluster.api.models.base_model_ import Model
from pcluster.api.models.log_stream import LogStream  # noqa: E501


class ListClusterLogStreamsResponseContent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, next_token=None, items=None):  # noqa: E501
        """ListClusterLogStreamsResponseContent - a model defined in OpenAPI

        :param next_token: The next_token of this ListClusterLogStreamsResponseContent.  # noqa: E501
        :type next_token: str
        :param items: The items of this ListClusterLogStreamsResponseContent.  # noqa: E501
        :type items: List[LogStream]
        """
        self.openapi_types = {"next_token": str, "items": List[LogStream]}

        self.attribute_map = {"next_token": "nextToken", "items": "items"}

        self._next_token = next_token
        self._items = items

    @classmethod
    def from_dict(cls, dikt) -> "ListClusterLogStreamsResponseContent":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListClusterLogStreamsResponseContent of this ListClusterLogStreamsResponseContent.  # noqa: E501
        :rtype: ListClusterLogStreamsResponseContent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def next_token(self):
        """Gets the next_token of this ListClusterLogStreamsResponseContent.

        Token to use for paginated requests.  # noqa: E501

        :return: The next_token of this ListClusterLogStreamsResponseContent.
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this ListClusterLogStreamsResponseContent.

        Token to use for paginated requests.  # noqa: E501

        :param next_token: The next_token of this ListClusterLogStreamsResponseContent.
        :type next_token: str
        """

        self._next_token = next_token

    @property
    def items(self):
        """Gets the items of this ListClusterLogStreamsResponseContent.


        :return: The items of this ListClusterLogStreamsResponseContent.
        :rtype: List[LogStream]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ListClusterLogStreamsResponseContent.


        :param items: The items of this ListClusterLogStreamsResponseContent.
        :type items: List[LogStream]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items
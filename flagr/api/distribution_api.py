# coding: utf-8

"""
    Flagr

    Flagr is a feature flagging, A/B testing and dynamic configuration microservice. The base path for all the APIs is \"/api/v1\".   # noqa: E501

    OpenAPI spec version: 1.1.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from flagr.api_client import ApiClient


class DistributionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def find_distributions(self, flag_id, segment_id, **kwargs):  # noqa: E501
        """find_distributions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_distributions(flag_id, segment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int flag_id: numeric ID of the flag (required)
        :param int segment_id: numeric ID of the segment (required)
        :return: list[Distribution]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.find_distributions_with_http_info(flag_id, segment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.find_distributions_with_http_info(flag_id, segment_id, **kwargs)  # noqa: E501
            return data

    def find_distributions_with_http_info(self, flag_id, segment_id, **kwargs):  # noqa: E501
        """find_distributions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_distributions_with_http_info(flag_id, segment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int flag_id: numeric ID of the flag (required)
        :param int segment_id: numeric ID of the segment (required)
        :return: list[Distribution]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flag_id', 'segment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_distributions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flag_id' is set
        if ('flag_id' not in params or
                params['flag_id'] is None):
            raise ValueError("Missing the required parameter `flag_id` when calling `find_distributions`")  # noqa: E501
        # verify the required parameter 'segment_id' is set
        if ('segment_id' not in params or
                params['segment_id'] is None):
            raise ValueError("Missing the required parameter `segment_id` when calling `find_distributions`")  # noqa: E501

        if 'flag_id' in params and params['flag_id'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `flag_id` when calling `find_distributions`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'segment_id' in params and params['segment_id'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `segment_id` when calling `find_distributions`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'flag_id' in params:
            path_params['flagID'] = params['flag_id']  # noqa: E501
        if 'segment_id' in params:
            path_params['segmentID'] = params['segment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/flags/{flagID}/segments/{segmentID}/distributions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Distribution]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_distributions(self, flag_id, segment_id, body, **kwargs):  # noqa: E501
        """put_distributions  # noqa: E501

        replace the distribution with the new setting  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_distributions(flag_id, segment_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int flag_id: numeric ID of the flag (required)
        :param int segment_id: numeric ID of the segment (required)
        :param PutDistributionsRequest body: array of distributions (required)
        :return: list[Distribution]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_distributions_with_http_info(flag_id, segment_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.put_distributions_with_http_info(flag_id, segment_id, body, **kwargs)  # noqa: E501
            return data

    def put_distributions_with_http_info(self, flag_id, segment_id, body, **kwargs):  # noqa: E501
        """put_distributions  # noqa: E501

        replace the distribution with the new setting  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_distributions_with_http_info(flag_id, segment_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int flag_id: numeric ID of the flag (required)
        :param int segment_id: numeric ID of the segment (required)
        :param PutDistributionsRequest body: array of distributions (required)
        :return: list[Distribution]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flag_id', 'segment_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_distributions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'flag_id' is set
        if ('flag_id' not in params or
                params['flag_id'] is None):
            raise ValueError("Missing the required parameter `flag_id` when calling `put_distributions`")  # noqa: E501
        # verify the required parameter 'segment_id' is set
        if ('segment_id' not in params or
                params['segment_id'] is None):
            raise ValueError("Missing the required parameter `segment_id` when calling `put_distributions`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_distributions`")  # noqa: E501

        if 'flag_id' in params and params['flag_id'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `flag_id` when calling `put_distributions`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'segment_id' in params and params['segment_id'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `segment_id` when calling `put_distributions`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'flag_id' in params:
            path_params['flagID'] = params['flag_id']  # noqa: E501
        if 'segment_id' in params:
            path_params['segmentID'] = params['segment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/flags/{flagID}/segments/{segmentID}/distributions', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Distribution]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

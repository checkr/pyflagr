# flagr.TagApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag**](TagApi.md#create_tag) | **POST** /flags/{flagID}/tags | 
[**delete_tag**](TagApi.md#delete_tag) | **DELETE** /flags/{flagID}/tags/{tagID} | 
[**find_all_tags**](TagApi.md#find_all_tags) | **GET** /tags | 
[**find_tags**](TagApi.md#find_tags) | **GET** /flags/{flagID}/tags | 


# **create_tag**
> Tag create_tag(flag_id, body)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.TagApi()
flag_id = 789 # int | numeric ID of the flag
body = flagr.CreateTagRequest() # CreateTagRequest | create a tag

try:
    api_response = api_instance.create_tag(flag_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->create_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 
 **body** | [**CreateTagRequest**](CreateTagRequest.md)| create a tag | 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(flag_id, tag_id)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.TagApi()
flag_id = 789 # int | numeric ID of the flag
tag_id = 789 # int | numeric ID of the tag

try:
    api_instance.delete_tag(flag_id, tag_id)
except ApiException as e:
    print("Exception when calling TagApi->delete_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 
 **tag_id** | **int**| numeric ID of the tag | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_tags**
> list[Tag] find_all_tags(limit=limit, offset=offset, value_like=value_like)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.TagApi()
limit = 789 # int | the numbers of tags to return (optional)
offset = 789 # int | return tags given the offset, it should usually set together with limit (optional)
value_like = 'value_like_example' # str | return tags partially matching given value (optional)

try:
    api_response = api_instance.find_all_tags(limit=limit, offset=offset, value_like=value_like)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->find_all_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| the numbers of tags to return | [optional] 
 **offset** | **int**| return tags given the offset, it should usually set together with limit | [optional] 
 **value_like** | **str**| return tags partially matching given value | [optional] 

### Return type

[**list[Tag]**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_tags**
> list[Tag] find_tags(flag_id)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.TagApi()
flag_id = 789 # int | numeric ID of the flag

try:
    api_response = api_instance.find_tags(flag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->find_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 

### Return type

[**list[Tag]**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


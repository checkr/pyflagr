# flagr.DistributionApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_distributions**](DistributionApi.md#find_distributions) | **GET** /flags/{flagID}/segments/{segmentID}/distributions | 
[**put_distributions**](DistributionApi.md#put_distributions) | **PUT** /flags/{flagID}/segments/{segmentID}/distributions | 


# **find_distributions**
> list[Distribution] find_distributions(flag_id, segment_id)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.DistributionApi()
flag_id = 789 # int | numeric ID of the flag
segment_id = 789 # int | numeric ID of the segment

try:
    api_response = api_instance.find_distributions(flag_id, segment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->find_distributions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 
 **segment_id** | **int**| numeric ID of the segment | 

### Return type

[**list[Distribution]**](Distribution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_distributions**
> list[Distribution] put_distributions(flag_id, segment_id, body)



replace the distribution with the new setting

### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.DistributionApi()
flag_id = 789 # int | numeric ID of the flag
segment_id = 789 # int | numeric ID of the segment
body = flagr.PutDistributionsRequest() # PutDistributionsRequest | array of distributions

try:
    api_response = api_instance.put_distributions(flag_id, segment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DistributionApi->put_distributions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 
 **segment_id** | **int**| numeric ID of the segment | 
 **body** | [**PutDistributionsRequest**](PutDistributionsRequest.md)| array of distributions | 

### Return type

[**list[Distribution]**](Distribution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


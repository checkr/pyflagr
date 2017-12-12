# flagr.SegmentApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_segment**](SegmentApi.md#create_segment) | **POST** /flags/{flagID}/segments | 
[**delete_segment**](SegmentApi.md#delete_segment) | **DELETE** /flags/{flagID}/segments/{segmentID} | 
[**find_segments**](SegmentApi.md#find_segments) | **GET** /flags/{flagID}/segments | 
[**put_segment**](SegmentApi.md#put_segment) | **PUT** /flags/{flagID}/segments/{segmentID} | 
[**put_segments_reorder**](SegmentApi.md#put_segments_reorder) | **PUT** /flags/{flagID}/segments/reorder | 


# **create_segment**
> Segment create_segment(flag_id, body)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.SegmentApi()
flag_id = 789 # int | numeric ID of the flag to get
body = flagr.CreateSegmentRequest() # CreateSegmentRequest | create a segment under a flag

try:
    api_response = api_instance.create_segment(flag_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentApi->create_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag to get | 
 **body** | [**CreateSegmentRequest**](CreateSegmentRequest.md)| create a segment under a flag | 

### Return type

[**Segment**](Segment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_segment**
> delete_segment(flag_id, segment_id)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.SegmentApi()
flag_id = 789 # int | numeric ID of the flag
segment_id = 789 # int | numeric ID of the segment

try:
    api_instance.delete_segment(flag_id, segment_id)
except ApiException as e:
    print("Exception when calling SegmentApi->delete_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 
 **segment_id** | **int**| numeric ID of the segment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_segments**
> list[Segment] find_segments(flag_id)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.SegmentApi()
flag_id = 789 # int | numeric ID of the flag to get

try:
    api_response = api_instance.find_segments(flag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentApi->find_segments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag to get | 

### Return type

[**list[Segment]**](Segment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_segment**
> Segment put_segment(flag_id, segment_id, body)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.SegmentApi()
flag_id = 789 # int | numeric ID of the flag
segment_id = 789 # int | numeric ID of the segment
body = flagr.PutSegmentRequest() # PutSegmentRequest | update a segment

try:
    api_response = api_instance.put_segment(flag_id, segment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentApi->put_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 
 **segment_id** | **int**| numeric ID of the segment | 
 **body** | [**PutSegmentRequest**](PutSegmentRequest.md)| update a segment | 

### Return type

[**Segment**](Segment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_segments_reorder**
> put_segments_reorder(flag_id, body)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.SegmentApi()
flag_id = 789 # int | numeric ID of the flag
body = flagr.PutSegmentReorderRequest() # PutSegmentReorderRequest | reorder segments

try:
    api_instance.put_segments_reorder(flag_id, body)
except ApiException as e:
    print("Exception when calling SegmentApi->put_segments_reorder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 
 **body** | [**PutSegmentReorderRequest**](PutSegmentReorderRequest.md)| reorder segments | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


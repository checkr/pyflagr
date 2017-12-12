# flagr.ConstraintApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_constraint**](ConstraintApi.md#create_constraint) | **POST** /flags/{flagID}/segments/{segmentID}/constraints | 
[**delete_constraint**](ConstraintApi.md#delete_constraint) | **DELETE** /flags/{flagID}/segments/{segmentID}/constraints/{constraintID} | 
[**find_constraints**](ConstraintApi.md#find_constraints) | **GET** /flags/{flagID}/segments/{segmentID}/constraints | 
[**put_constraint**](ConstraintApi.md#put_constraint) | **PUT** /flags/{flagID}/segments/{segmentID}/constraints/{constraintID} | 


# **create_constraint**
> Constraint create_constraint(flag_id, segment_id, body)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.ConstraintApi()
flag_id = 789 # int | numeric ID of the flag
segment_id = 789 # int | numeric ID of the segment
body = flagr.CreateConstraintRequest() # CreateConstraintRequest | create a constraint

try:
    api_response = api_instance.create_constraint(flag_id, segment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConstraintApi->create_constraint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 
 **segment_id** | **int**| numeric ID of the segment | 
 **body** | [**CreateConstraintRequest**](CreateConstraintRequest.md)| create a constraint | 

### Return type

[**Constraint**](Constraint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_constraint**
> delete_constraint(flag_id, segment_id, constraint_id)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.ConstraintApi()
flag_id = 789 # int | numeric ID of the flag
segment_id = 789 # int | numeric ID of the segment
constraint_id = 789 # int | numeric ID of the constraint

try:
    api_instance.delete_constraint(flag_id, segment_id, constraint_id)
except ApiException as e:
    print("Exception when calling ConstraintApi->delete_constraint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 
 **segment_id** | **int**| numeric ID of the segment | 
 **constraint_id** | **int**| numeric ID of the constraint | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_constraints**
> list[Constraint] find_constraints(flag_id, segment_id)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.ConstraintApi()
flag_id = 789 # int | numeric ID of the flag
segment_id = 789 # int | numeric ID of the segment

try:
    api_response = api_instance.find_constraints(flag_id, segment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConstraintApi->find_constraints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 
 **segment_id** | **int**| numeric ID of the segment | 

### Return type

[**list[Constraint]**](Constraint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_constraint**
> Constraint put_constraint(flag_id, segment_id, constraint_id, body)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.ConstraintApi()
flag_id = 789 # int | numeric ID of the flag
segment_id = 789 # int | numeric ID of the segment
constraint_id = 789 # int | numeric ID of the constraint
body = flagr.CreateConstraintRequest() # CreateConstraintRequest | create a constraint

try:
    api_response = api_instance.put_constraint(flag_id, segment_id, constraint_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConstraintApi->put_constraint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 
 **segment_id** | **int**| numeric ID of the segment | 
 **constraint_id** | **int**| numeric ID of the constraint | 
 **body** | [**CreateConstraintRequest**](CreateConstraintRequest.md)| create a constraint | 

### Return type

[**Constraint**](Constraint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


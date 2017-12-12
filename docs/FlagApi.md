# flagr.FlagApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_flag**](FlagApi.md#create_flag) | **POST** /flags | 
[**delete_flag**](FlagApi.md#delete_flag) | **DELETE** /flags/{flagID} | 
[**find_flags**](FlagApi.md#find_flags) | **GET** /flags | 
[**get_flag**](FlagApi.md#get_flag) | **GET** /flags/{flagID} | 
[**get_flag_snapshots**](FlagApi.md#get_flag_snapshots) | **GET** /flags/{flagID}/snapshots | 
[**put_flag**](FlagApi.md#put_flag) | **PUT** /flags/{flagID} | 
[**set_flag_enabled**](FlagApi.md#set_flag_enabled) | **PUT** /flags/{flagID}/enabled | 


# **create_flag**
> Flag create_flag(body)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.FlagApi()
body = flagr.CreateFlagRequest() # CreateFlagRequest | create a flag

try:
    api_response = api_instance.create_flag(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlagApi->create_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFlagRequest**](CreateFlagRequest.md)| create a flag | 

### Return type

[**Flag**](Flag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_flag**
> delete_flag(flag_id)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.FlagApi()
flag_id = 789 # int | numeric ID of the flag

try:
    api_instance.delete_flag(flag_id)
except ApiException as e:
    print("Exception when calling FlagApi->delete_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_flags**
> list[Flag] find_flags()



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.FlagApi()

try:
    api_response = api_instance.find_flags()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlagApi->find_flags: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Flag]**](Flag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flag**
> Flag get_flag(flag_id)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.FlagApi()
flag_id = 789 # int | numeric ID of the flag to get

try:
    api_response = api_instance.get_flag(flag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlagApi->get_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag to get | 

### Return type

[**Flag**](Flag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flag_snapshots**
> list[FlagSnapshot] get_flag_snapshots(flag_id)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.FlagApi()
flag_id = 789 # int | numeric ID of the flag to get

try:
    api_response = api_instance.get_flag_snapshots(flag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlagApi->get_flag_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag to get | 

### Return type

[**list[FlagSnapshot]**](FlagSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_flag**
> Flag put_flag(flag_id, body)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.FlagApi()
flag_id = 789 # int | numeric ID of the flag to get
body = flagr.PutFlagRequest() # PutFlagRequest | update a flag

try:
    api_response = api_instance.put_flag(flag_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlagApi->put_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag to get | 
 **body** | [**PutFlagRequest**](PutFlagRequest.md)| update a flag | 

### Return type

[**Flag**](Flag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_flag_enabled**
> Flag set_flag_enabled(flag_id, body)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.FlagApi()
flag_id = 789 # int | numeric ID of the flag to get
body = flagr.SetFlagEnabledRequest() # SetFlagEnabledRequest | set flag enabled state

try:
    api_response = api_instance.set_flag_enabled(flag_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlagApi->set_flag_enabled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag to get | 
 **body** | [**SetFlagEnabledRequest**](SetFlagEnabledRequest.md)| set flag enabled state | 

### Return type

[**Flag**](Flag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


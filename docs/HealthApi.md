# flagr.HealthApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](HealthApi.md#get_health) | **GET** /health | 


# **get_health**
> Health get_health()



Check if Flagr is healthy

### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.HealthApi()

try:
    api_response = api_instance.get_health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->get_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Health**](Health.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


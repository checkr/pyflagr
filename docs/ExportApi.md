# flagr.ExportApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_export_eval_cache_json**](ExportApi.md#get_export_eval_cache_json) | **GET** /export/eval_cache/json | 
[**get_export_sqlite**](ExportApi.md#get_export_sqlite) | **GET** /export/sqlite | 


# **get_export_eval_cache_json**
> object get_export_eval_cache_json()



Export JSON format of the eval cache dump

### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.ExportApi()

try:
    api_response = api_instance.get_export_eval_cache_json()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->get_export_eval_cache_json: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_export_sqlite**
> file get_export_sqlite()



Export sqlite3 format of the db dump, which is converted from the main database.

### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.ExportApi()

try:
    api_response = api_instance.get_export_sqlite()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->get_export_sqlite: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


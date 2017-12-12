# flagr.VariantApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_variant**](VariantApi.md#create_variant) | **POST** /flags/{flagID}/variants | 
[**delete_variant**](VariantApi.md#delete_variant) | **DELETE** /flags/{flagID}/variants/{variantID} | 
[**find_variants**](VariantApi.md#find_variants) | **GET** /flags/{flagID}/variants | 
[**put_variant**](VariantApi.md#put_variant) | **PUT** /flags/{flagID}/variants/{variantID} | 


# **create_variant**
> Variant create_variant(flag_id, body)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.VariantApi()
flag_id = 789 # int | numeric ID of the flag
body = flagr.CreateVariantRequest() # CreateVariantRequest | create a variant

try:
    api_response = api_instance.create_variant(flag_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariantApi->create_variant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 
 **body** | [**CreateVariantRequest**](CreateVariantRequest.md)| create a variant | 

### Return type

[**Variant**](Variant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_variant**
> delete_variant(flag_id, variant_id)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.VariantApi()
flag_id = 789 # int | numeric ID of the flag
variant_id = 789 # int | numeric ID of the variant

try:
    api_instance.delete_variant(flag_id, variant_id)
except ApiException as e:
    print("Exception when calling VariantApi->delete_variant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 
 **variant_id** | **int**| numeric ID of the variant | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_variants**
> list[Variant] find_variants(flag_id)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.VariantApi()
flag_id = 789 # int | numeric ID of the flag

try:
    api_response = api_instance.find_variants(flag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariantApi->find_variants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 

### Return type

[**list[Variant]**](Variant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_variant**
> Variant put_variant(flag_id, variant_id, body)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.VariantApi()
flag_id = 789 # int | numeric ID of the flag
variant_id = 789 # int | numeric ID of the variant
body = flagr.PutVariantRequest() # PutVariantRequest | update a variant

try:
    api_response = api_instance.put_variant(flag_id, variant_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariantApi->put_variant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **int**| numeric ID of the flag | 
 **variant_id** | **int**| numeric ID of the variant | 
 **body** | [**PutVariantRequest**](PutVariantRequest.md)| update a variant | 

### Return type

[**Variant**](Variant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


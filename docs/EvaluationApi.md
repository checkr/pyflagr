# flagr.EvaluationApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_evaluation**](EvaluationApi.md#post_evaluation) | **POST** /evaluation | 
[**post_evaluation_batch**](EvaluationApi.md#post_evaluation_batch) | **POST** /evaluation/batch | 


# **post_evaluation**
> EvalResult post_evaluation(body)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.EvaluationApi()
body = flagr.EvalContext() # EvalContext | evalution context

try:
    api_response = api_instance.post_evaluation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationApi->post_evaluation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EvalContext**](EvalContext.md)| evalution context | 

### Return type

[**EvalResult**](EvalResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_evaluation_batch**
> EvaluationBatchResponse post_evaluation_batch(body)



### Example
```python
from __future__ import print_function
import time
import flagr
from flagr.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = flagr.EvaluationApi()
body = flagr.EvaluationBatchRequest() # EvaluationBatchRequest | evalution batch request

try:
    api_response = api_instance.post_evaluation_batch(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationApi->post_evaluation_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EvaluationBatchRequest**](EvaluationBatchRequest.md)| evalution batch request | 

### Return type

[**EvaluationBatchResponse**](EvaluationBatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


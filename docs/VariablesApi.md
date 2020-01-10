# datacatalog.VariablesApi

All URIs are relative to *https://api.mint-data-catalog.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_variable_info**](VariablesApi.md#get_variable_info) | **POST** /variables/get_variable_info | Detailed information about the variable
[**register_variables**](VariablesApi.md#register_variables) | **POST** /datasets/register_variables | Create variable record(s)


# **get_variable_info**
> InlineResponse2006 get_variable_info(body)

Detailed information about the variable

### Example

```python
from __future__ import print_function
import time
import datacatalog
from datacatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = datacatalog.VariablesApi()
body = datacatalog.InlineObject10() # InlineObject10 | 

try:
    # Detailed information about the variable
    api_response = api_instance.get_variable_info(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariablesApi->get_variable_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineObject10**](InlineObject10.md)|  | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid input (check error message(s) to correct it) |  -  |
**500** | Internal error - please contact Dan Feldman danf@usc.edu |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_variables**
> register_variables(body)

Create variable record(s)

### Example

```python
from __future__ import print_function
import time
import datacatalog
from datacatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = datacatalog.VariablesApi()
body = datacatalog.InlineObject7() # InlineObject7 | 

try:
    # Create variable record(s)
    api_instance.register_variables(body)
except ApiException as e:
    print("Exception when calling VariablesApi->register_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineObject7**](InlineObject7.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid input (check error message(s) to correct it) |  -  |
**500** | Internal error - please contact Dan Feldman danf@usc.edu |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# datacatalog.StandardVariablesApi

All URIs are relative to *https://api.mint-data-catalog.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_standard_variable_info**](StandardVariablesApi.md#get_standard_variable_info) | **POST** /standard_variables/get_standard_variable_info | Detailed information about the standard variable
[**register_standard_variables**](StandardVariablesApi.md#register_standard_variables) | **POST** /knowledge_graph/register_standard_variables | Create standard_variable record(s)


# **get_standard_variable_info**
> InlineResponse2007 get_standard_variable_info(body)

Detailed information about the standard variable

### Example

```python
from __future__ import print_function
import time
import datacatalog
from datacatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = datacatalog.StandardVariablesApi()
body = datacatalog.InlineObject12() # InlineObject12 | 

try:
    # Detailed information about the standard variable
    api_response = api_instance.get_standard_variable_info(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StandardVariablesApi->get_standard_variable_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineObject12**](InlineObject12.md)|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

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

# **register_standard_variables**
> register_standard_variables(body)

Create standard_variable record(s)

### Example

```python
from __future__ import print_function
import time
import datacatalog
from datacatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = datacatalog.StandardVariablesApi()
body = datacatalog.InlineObject11() # InlineObject11 | 

try:
    # Create standard_variable record(s)
    api_instance.register_standard_variables(body)
except ApiException as e:
    print("Exception when calling StandardVariablesApi->register_standard_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineObject11**](InlineObject11.md)|  | 

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


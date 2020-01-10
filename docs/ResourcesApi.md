# datacatalog.ResourcesApi

All URIs are relative to *https://api.mint-data-catalog.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_resource_info**](ResourcesApi.md#get_resource_info) | **POST** /resources/get_resource_info | Detailed information about the resource
[**register_resources**](ResourcesApi.md#register_resources) | **POST** /datasets/register_resources | Create resource record(s)


# **get_resource_info**
> InlineResponse2005 get_resource_info(body)

Detailed information about the resource

### Example

```python
from __future__ import print_function
import time
import datacatalog
from datacatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = datacatalog.ResourcesApi()
body = datacatalog.InlineObject9() # InlineObject9 | 

try:
    # Detailed information about the resource
    api_response = api_instance.get_resource_info(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->get_resource_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineObject9**](InlineObject9.md)|  | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

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

# **register_resources**
> register_resources(body)

Create resource record(s)

### Example

```python
from __future__ import print_function
import time
import datacatalog
from datacatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = datacatalog.ResourcesApi()
body = datacatalog.InlineObject8() # InlineObject8 | 

try:
    # Create resource record(s)
    api_instance.register_resources(body)
except ApiException as e:
    print("Exception when calling ResourcesApi->register_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineObject8**](InlineObject8.md)|  | 

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


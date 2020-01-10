# datacatalog.DatasetsApi

All URIs are relative to *https://api.mint-data-catalog.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataset_resources**](DatasetsApi.md#dataset_resources) | **POST** /datasets/dataset_resources | List all resources for this dataset
[**dataset_standard_variables**](DatasetsApi.md#dataset_standard_variables) | **POST** /datasets/dataset_standard_variables | List all standard_variables for this dataset
[**dataset_variables**](DatasetsApi.md#dataset_variables) | **POST** /datasets/dataset_variables | List all variables for this dataset
[**datasets_search**](DatasetsApi.md#datasets_search) | **POST** /datasets/search | Full-text search of datasets
[**find_datasets**](DatasetsApi.md#find_datasets) | **POST** /find_datasets | Search datasets by name, id, or standard variables
[**get_dataset_info**](DatasetsApi.md#get_dataset_info) | **POST** /datasets/get_dataset_info | Detailed information about the dataset
[**register_datasets**](DatasetsApi.md#register_datasets) | **POST** /datasets/register_datasets | Create dataset record(s)


# **dataset_resources**
> InlineResponse2002 dataset_resources(body)

List all resources for this dataset

### Example

```python
from __future__ import print_function
import time
import datacatalog
from datacatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = datacatalog.DatasetsApi()
body = datacatalog.InlineObject3() # InlineObject3 | 

try:
    # List all resources for this dataset
    api_response = api_instance.dataset_resources(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->dataset_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineObject3**](InlineObject3.md)|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

# **dataset_standard_variables**
> InlineResponse200 dataset_standard_variables(body)

List all standard_variables for this dataset

### Example

```python
from __future__ import print_function
import time
import datacatalog
from datacatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = datacatalog.DatasetsApi()
body = datacatalog.InlineObject1() # InlineObject1 | 

try:
    # List all standard_variables for this dataset
    api_response = api_instance.dataset_standard_variables(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->dataset_standard_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineObject1**](InlineObject1.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **dataset_variables**
> InlineResponse2001 dataset_variables(body)

List all variables for this dataset

### Example

```python
from __future__ import print_function
import time
import datacatalog
from datacatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = datacatalog.DatasetsApi()
body = datacatalog.InlineObject2() # InlineObject2 | 

try:
    # List all variables for this dataset
    api_response = api_instance.dataset_variables(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->dataset_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineObject2**](InlineObject2.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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

# **datasets_search**
> InlineResponse2004 datasets_search(body)

Full-text search of datasets

### Example

```python
from __future__ import print_function
import time
import datacatalog
from datacatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = datacatalog.DatasetsApi()
body = datacatalog.InlineObject5() # InlineObject5 | 

try:
    # Full-text search of datasets
    api_response = api_instance.datasets_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->datasets_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineObject5**](InlineObject5.md)|  | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **find_datasets**
> InlineResponse2004 find_datasets(body)

Search datasets by name, id, or standard variables

### Example

```python
from __future__ import print_function
import time
import datacatalog
from datacatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = datacatalog.DatasetsApi()
body = datacatalog.InlineObject6() # InlineObject6 | 

try:
    # Search datasets by name, id, or standard variables
    api_response = api_instance.find_datasets(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->find_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineObject6**](InlineObject6.md)|  | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **get_dataset_info**
> InlineResponse2003 get_dataset_info(body)

Detailed information about the dataset

### Example

```python
from __future__ import print_function
import time
import datacatalog
from datacatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = datacatalog.DatasetsApi()
body = datacatalog.InlineObject4() # InlineObject4 | 

try:
    # Detailed information about the dataset
    api_response = api_instance.get_dataset_info(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasetsApi->get_dataset_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineObject4**](InlineObject4.md)|  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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

# **register_datasets**
> register_datasets(body)

Create dataset record(s)

### Example

```python
from __future__ import print_function
import time
import datacatalog
from datacatalog.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = datacatalog.DatasetsApi()
body = datacatalog.InlineObject() # InlineObject | 

try:
    # Create dataset record(s)
    api_instance.register_datasets(body)
except ApiException as e:
    print("Exception when calling DatasetsApi->register_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineObject**](InlineObject.md)|  | 

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


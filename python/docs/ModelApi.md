# swagger_client.ModelApi

All URIs are relative to *https://virtserver.swaggerhub.com/roboblocks/models/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_model**](ModelApi.md#add_model) | **POST** /model | Add a new model
[**delete_model_by_id**](ModelApi.md#delete_model_by_id) | **DELETE** /model/id/{modelId} | Deletes a model by Id
[**delete_model_by_name**](ModelApi.md#delete_model_by_name) | **DELETE** /model/name/{modelName} | Deletes a model by name
[**find_models_by_status**](ModelApi.md#find_models_by_status) | **GET** /model/findByStatus | Finds Model by status
[**find_models_by_tags**](ModelApi.md#find_models_by_tags) | **GET** /model/findByTags | Finds Models by tags
[**get_model_by_id**](ModelApi.md#get_model_by_id) | **GET** /model/id/{modelId} | Find model by ID
[**get_model_by_name**](ModelApi.md#get_model_by_name) | **GET** /model/name/{modelName} | Find model by Name
[**update_model**](ModelApi.md#update_model) | **PUT** /model | Update an existing model
[**update_model_with_form**](ModelApi.md#update_model_with_form) | **POST** /model/id/{modelId} | Updates a model in the store with form data
[**upload_file**](ModelApi.md#upload_file) | **POST** /model/{modelId}/uploadModel | uploads the model data


# **add_model**
> add_model(body)

Add a new model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: modelstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ModelApi(swagger_client.ApiClient(configuration))
body = swagger_client.Model() # Model | Model to be stored

try:
    # Add a new model
    api_instance.add_model(body)
except ApiException as e:
    print("Exception when calling ModelApi->add_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model**](Model.md)| Model to be stored | 

### Return type

void (empty response body)

### Authorization

[modelstore_auth](../README.md#modelstore_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model_by_id**
> delete_model_by_id(model_id, api_key=api_key)

Deletes a model by Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: modelstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ModelApi(swagger_client.ApiClient(configuration))
model_id = 789 # int | Model id to delete
api_key = 'api_key_example' # str |  (optional)

try:
    # Deletes a model by Id
    api_instance.delete_model_by_id(model_id, api_key=api_key)
except ApiException as e:
    print("Exception when calling ModelApi->delete_model_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| Model id to delete | 
 **api_key** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[modelstore_auth](../README.md#modelstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model_by_name**
> delete_model_by_name(model_name, api_key=api_key)

Deletes a model by name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: modelstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ModelApi(swagger_client.ApiClient(configuration))
model_name = 'model_name_example' # str | Model name to delete
api_key = 'api_key_example' # str |  (optional)

try:
    # Deletes a model by name
    api_instance.delete_model_by_name(model_name, api_key=api_key)
except ApiException as e:
    print("Exception when calling ModelApi->delete_model_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**| Model name to delete | 
 **api_key** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[modelstore_auth](../README.md#modelstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_models_by_status**
> list[Model] find_models_by_status(status)

Finds Model by status

Multiple status values can be provided with comma separated strings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: modelstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ModelApi(swagger_client.ApiClient(configuration))
status = ['status_example'] # list[str] | Status values that need to be considered for filter

try:
    # Finds Model by status
    api_response = api_instance.find_models_by_status(status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->find_models_by_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**list[str]**](str.md)| Status values that need to be considered for filter | 

### Return type

[**list[Model]**](Model.md)

### Authorization

[modelstore_auth](../README.md#modelstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_models_by_tags**
> list[Model] find_models_by_tags(tags)

Finds Models by tags

Muliple tags can be provided with comma separated strings. Use\\ \\ tag1, tag2, tag3 for testing.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: modelstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ModelApi(swagger_client.ApiClient(configuration))
tags = ['tags_example'] # list[str] | Tags to filter by

try:
    # Finds Models by tags
    api_response = api_instance.find_models_by_tags(tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->find_models_by_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**list[str]**](str.md)| Tags to filter by | 

### Return type

[**list[Model]**](Model.md)

### Authorization

[modelstore_auth](../README.md#modelstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_by_id**
> Model get_model_by_id(model_id)

Find model by ID

Returns a model of a version with a specific ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ModelApi(swagger_client.ApiClient(configuration))
model_id = 789 # int | ID of the model to return

try:
    # Find model by ID
    api_response = api_instance.get_model_by_id(model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->get_model_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| ID of the model to return | 

### Return type

[**Model**](Model.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_by_name**
> Model get_model_by_name(model_name)

Find model by Name

Returns the best model by Name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ModelApi(swagger_client.ApiClient(configuration))
model_name = 'model_name_example' # str | Name of the model to return

try:
    # Find model by Name
    api_response = api_instance.get_model_by_name(model_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->get_model_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**| Name of the model to return | 

### Return type

[**Model**](Model.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model**
> update_model(body)

Update an existing model

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: modelstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ModelApi(swagger_client.ApiClient(configuration))
body = swagger_client.Model() # Model | Model object to be added to the store

try:
    # Update an existing model
    api_instance.update_model(body)
except ApiException as e:
    print("Exception when calling ModelApi->update_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model**](Model.md)| Model object to be added to the store | 

### Return type

void (empty response body)

### Authorization

[modelstore_auth](../README.md#modelstore_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model_with_form**
> update_model_with_form(model_id, name=name, status=status)

Updates a model in the store with form data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: modelstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ModelApi(swagger_client.ApiClient(configuration))
model_id = 789 # int | ID of the model that needs to be updated
name = 'name_example' # str | Updated name of the model (optional)
status = 'status_example' # str | Updated status of the model (optional)

try:
    # Updates a model in the store with form data
    api_instance.update_model_with_form(model_id, name=name, status=status)
except ApiException as e:
    print("Exception when calling ModelApi->update_model_with_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| ID of the model that needs to be updated | 
 **name** | **str**| Updated name of the model | [optional] 
 **status** | **str**| Updated status of the model | [optional] 

### Return type

void (empty response body)

### Authorization

[modelstore_auth](../README.md#modelstore_auth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> ApiResponse upload_file(model_id, additional_metadata=additional_metadata, file=file)

uploads the model data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: modelstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ModelApi(swagger_client.ApiClient(configuration))
model_id = 789 # int | ID of Model to update
additional_metadata = 'additional_metadata_example' # str | Additional data to pass to server (optional)
file = '/path/to/file.txt' # file | file to upload (optional)

try:
    # uploads the model data
    api_response = api_instance.upload_file(model_id, additional_metadata=additional_metadata, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **int**| ID of Model to update | 
 **additional_metadata** | **str**| Additional data to pass to server | [optional] 
 **file** | **file**| file to upload | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[modelstore_auth](../README.md#modelstore_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


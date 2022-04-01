# matecat_api.GlossaryApi

All URIs are relative to *https://virtserver.swaggerhub.com/xtrf/Matecat/2.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_glossaries_export_tm_key_get**](GlossaryApi.md#api_v2_glossaries_export_tm_key_get) | **GET** /api/v2/glossaries/export/{tm_key} | Download Glossary
[**api_v2_glossaries_import_post**](GlossaryApi.md#api_v2_glossaries_import_post) | **POST** /api/v2/glossaries/import/ | Import Glossary
[**api_v2_glossaries_import_status_tm_key_get**](GlossaryApi.md#api_v2_glossaries_import_status_tm_key_get) | **GET** /api/v2/glossaries/import/status/{tm_key} | Glossary Upload status.

# **api_v2_glossaries_export_tm_key_get**
> api_v2_glossaries_export_tm_key_get(tm_key)

Download Glossary

download Glossary

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.GlossaryApi()
tm_key = 'tm_key_example' # str | The tm key.

try:
    # Download Glossary
    api_instance.api_v2_glossaries_export_tm_key_get(tm_key)
except ApiException as e:
    print("Exception when calling GlossaryApi->api_v2_glossaries_export_tm_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tm_key** | **str**| The tm key. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_glossaries_import_post**
> api_v2_glossaries_import_post(files, name, tm_key)

Import Glossary

Import glossary file (.xlsx)

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.GlossaryApi()
files = 'files_example' # str | 
name = 'name_example' # str | 
tm_key = 'tm_key_example' # str | 

try:
    # Import Glossary
    api_instance.api_v2_glossaries_import_post(files, name, tm_key)
except ApiException as e:
    print("Exception when calling GlossaryApi->api_v2_glossaries_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files** | **str**|  | 
 **name** | **str**|  | 
 **tm_key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_glossaries_import_status_tm_key_get**
> UploadGlossaryStatusObject api_v2_glossaries_import_status_tm_key_get(tm_key, name=name)

Glossary Upload status.

Glossary Upload status.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.GlossaryApi()
tm_key = 'tm_key_example' # str | The tm key.
name = 'name_example' # str | The file name. (optional)

try:
    # Glossary Upload status.
    api_response = api_instance.api_v2_glossaries_import_status_tm_key_get(tm_key, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlossaryApi->api_v2_glossaries_import_status_tm_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tm_key** | **str**| The tm key. | 
 **name** | **str**| The file name. | [optional] 

### Return type

[**UploadGlossaryStatusObject**](UploadGlossaryStatusObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


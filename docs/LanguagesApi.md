# matecat_api.LanguagesApi

All URIs are relative to *https://virtserver.swaggerhub.com/xtrf/Matecat/2.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_languages_get**](LanguagesApi.md#api_v2_languages_get) | **GET** /api/v2/languages | Supported languages list.

# **api_v2_languages_get**
> Languages api_v2_languages_get()

Supported languages list.

List of supported languages.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.LanguagesApi()

try:
    # Supported languages list.
    api_response = api_instance.api_v2_languages_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->api_v2_languages_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Languages**](Languages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


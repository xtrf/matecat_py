# matecat_api.TMKeysApi

All URIs are relative to *https://virtserver.swaggerhub.com/xtrf/Matecat/2.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_keys_list_get**](TMKeysApi.md#api_v2_keys_list_get) | **GET** /api/v2/keys/list | Retrieve private TM keys list.

# **api_v2_keys_list_get**
> KeysList api_v2_keys_list_get()

Retrieve private TM keys list.

Retrieve private TM keys list.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.TMKeysApi()

try:
    # Retrieve private TM keys list.
    api_response = api_instance.api_v2_keys_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TMKeysApi->api_v2_keys_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**KeysList**](KeysList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# matecat_api.OptionsApi

All URIs are relative to *https://virtserver.swaggerhub.com/xtrf/Matecat/2.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_jobs_id_job_password_options_post**](OptionsApi.md#api_v2_jobs_id_job_password_options_post) | **POST** /api/v2/jobs/{id_job}/{password}/options | Update Options

# **api_v2_jobs_id_job_password_options_post**
> Options api_v2_jobs_id_job_password_options_post(id_job, password, speech2text=speech2text, tag_projection=tag_projection, lexiqa=lexiqa)

Update Options

Update Options (speech2text, guess tags, lexiqa)

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.OptionsApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)
speech2text = true # bool |  (optional)
tag_projection = true # bool |  (optional)
lexiqa = true # bool |  (optional)

try:
    # Update Options
    api_response = api_instance.api_v2_jobs_id_job_password_options_post(id_job, password, speech2text=speech2text, tag_projection=tag_projection, lexiqa=lexiqa)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptionsApi->api_v2_jobs_id_job_password_options_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job (Translate password) | 
 **speech2text** | **bool**|  | [optional] 
 **tag_projection** | **bool**|  | [optional] 
 **lexiqa** | **bool**|  | [optional] 

### Return type

[**Options**](Options.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


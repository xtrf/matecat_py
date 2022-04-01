# matecat_api.TranslationVersionsApi

All URIs are relative to *https://virtserver.swaggerhub.com/xtrf/Matecat/2.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_jobs_id_job_password_segments_id_segment_translation_versions_get**](TranslationVersionsApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_versions_get) | **GET** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-versions | Segment versions
[**api_v2_jobs_id_job_password_segments_id_segment_translation_versions_version_number_get**](TranslationVersionsApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_versions_version_number_get) | **GET** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-versions/{version_number} | Get a Segment translation version
[**api_v2_jobs_id_job_password_translation_versions_get**](TranslationVersionsApi.md#api_v2_jobs_id_job_password_translation_versions_get) | **GET** /api/v2/jobs/{id_job}/{password}/translation-versions | Project translation versions

# **api_v2_jobs_id_job_password_segments_id_segment_translation_versions_get**
> TranslationVersions api_v2_jobs_id_job_password_segments_id_segment_translation_versions_get(id_job, password, id_segment)

Segment versions

Segment versions

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.TranslationVersionsApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)
id_segment = 'id_segment_example' # str | The id of the segment

try:
    # Segment versions
    api_response = api_instance.api_v2_jobs_id_job_password_segments_id_segment_translation_versions_get(id_job, password, id_segment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationVersionsApi->api_v2_jobs_id_job_password_segments_id_segment_translation_versions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job (Translate password) | 
 **id_segment** | **str**| The id of the segment | 

### Return type

[**TranslationVersions**](TranslationVersions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_id_job_password_segments_id_segment_translation_versions_version_number_get**
> TranslationVersion api_v2_jobs_id_job_password_segments_id_segment_translation_versions_version_number_get(id_job, password, id_segment, version_number)

Get a Segment translation version

Get a Segment translation version

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.TranslationVersionsApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)
id_segment = 'id_segment_example' # str | The id of the segment
version_number = 'version_number_example' # str | The version number

try:
    # Get a Segment translation version
    api_response = api_instance.api_v2_jobs_id_job_password_segments_id_segment_translation_versions_version_number_get(id_job, password, id_segment, version_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationVersionsApi->api_v2_jobs_id_job_password_segments_id_segment_translation_versions_version_number_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job (Translate password) | 
 **id_segment** | **str**| The id of the segment | 
 **version_number** | **str**| The version number | 

### Return type

[**TranslationVersion**](TranslationVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_id_job_password_translation_versions_get**
> TranslationVersions api_v2_jobs_id_job_password_translation_versions_get(id_job, password)

Project translation versions

Project translation versions

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.TranslationVersionsApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)

try:
    # Project translation versions
    api_response = api_instance.api_v2_jobs_id_job_password_translation_versions_get(id_job, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationVersionsApi->api_v2_jobs_id_job_password_translation_versions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job (Translate password) | 

### Return type

[**TranslationVersions**](TranslationVersions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# matecat_api.JobApi

All URIs are relative to *https://virtserver.swaggerhub.com/xtrf/Matecat/2.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_jobs_id_job_password_stats_get**](JobApi.md#api_v1_jobs_id_job_password_stats_get) | **GET** /api/v1/jobs/{id_job}/{password}/stats | Statistics
[**api_v2_jobs_id_job_password_active_post**](JobApi.md#api_v2_jobs_id_job_password_active_post) | **POST** /api/v2/jobs/{id_job}/{password}/active | Active API
[**api_v2_jobs_id_job_password_archive_post**](JobApi.md#api_v2_jobs_id_job_password_archive_post) | **POST** /api/v2/jobs/{id_job}/{password}/archive | Archive API
[**api_v2_jobs_id_job_password_cancel_post**](JobApi.md#api_v2_jobs_id_job_password_cancel_post) | **POST** /api/v2/jobs/{id_job}/{password}/cancel | Cancel API
[**api_v2_jobs_id_job_password_comments_get**](JobApi.md#api_v2_jobs_id_job_password_comments_get) | **GET** /api/v2/jobs/{id_job}/{password}/comments | Get segment comments in a job
[**api_v2_jobs_id_job_password_get**](JobApi.md#api_v2_jobs_id_job_password_get) | **GET** /api/v2/jobs/{id_job}/{password} | Job Info
[**api_v2_jobs_id_job_password_options_post**](JobApi.md#api_v2_jobs_id_job_password_options_post) | **POST** /api/v2/jobs/{id_job}/{password}/options | Update Options
[**api_v2_jobs_id_job_password_quality_report_get**](JobApi.md#api_v2_jobs_id_job_password_quality_report_get) | **GET** /api/v2/jobs/{id_job}/{password}/quality-report | Quality report
[**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_get**](JobApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_get) | **GET** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues/{id_issue}/comments | Get comments
[**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_post**](JobApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_post) | **POST** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues/{id_issue}/comments | Add comment to a translation issue
[**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_delete**](JobApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_delete) | **DELETE** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues/{id_issue} | Delete a translation Issue
[**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_post**](JobApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_post) | **POST** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues/{id_issue} | Update translation issues
[**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_post**](JobApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_post) | **POST** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues | Create translation issues
[**api_v2_jobs_id_job_password_segments_id_segment_translation_versions_get**](JobApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_versions_get) | **GET** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-versions | Segment versions
[**api_v2_jobs_id_job_password_segments_id_segment_translation_versions_version_number_get**](JobApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_versions_version_number_get) | **GET** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-versions/{version_number} | Get a Segment translation version
[**api_v2_jobs_id_job_password_translation_issues_get**](JobApi.md#api_v2_jobs_id_job_password_translation_issues_get) | **GET** /api/v2/jobs/{id_job}/{password}/translation-issues | Project translation issues
[**api_v2_jobs_id_job_password_translation_versions_get**](JobApi.md#api_v2_jobs_id_job_password_translation_versions_get) | **GET** /api/v2/jobs/{id_job}/{password}/translation-versions | Project translation versions
[**api_v2_jobs_id_job_password_translator_get**](JobApi.md#api_v2_jobs_id_job_password_translator_get) | **GET** /api/v2/jobs/{id_job}/{password}/translator | Gets the translator assigned to a job
[**api_v2_jobs_id_job_password_translator_post**](JobApi.md#api_v2_jobs_id_job_password_translator_post) | **POST** /api/v2/jobs/{id_job}/{password}/translator | Assigns a job to a translator
[**t_mx_id_job_password_post**](JobApi.md#t_mx_id_job_password_post) | **POST** /TMX/{id_job}/{password} | Download Job TMX
[**translation_id_job_password_get**](JobApi.md#translation_id_job_password_get) | **GET** /translation/{id_job}/{password} | Download Translation

# **api_v1_jobs_id_job_password_stats_get**
> Stats api_v1_jobs_id_job_password_stats_get(id_job, password)

Statistics

Statistics

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job

try:
    # Statistics
    api_response = api_instance.api_v1_jobs_id_job_password_stats_get(id_job, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->api_v1_jobs_id_job_password_stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job | 

### Return type

[**Stats**](Stats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_id_job_password_active_post**
> ChangeStatus api_v2_jobs_id_job_password_active_post(id_job, password)

Active API

API to active a Job

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job

try:
    # Active API
    api_response = api_instance.api_v2_jobs_id_job_password_active_post(id_job, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_active_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job | 

### Return type

[**ChangeStatus**](ChangeStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_id_job_password_archive_post**
> ChangeStatus api_v2_jobs_id_job_password_archive_post(id_job, password)

Archive API

API to archive a Job

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job

try:
    # Archive API
    api_response = api_instance.api_v2_jobs_id_job_password_archive_post(id_job, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_archive_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job | 

### Return type

[**ChangeStatus**](ChangeStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_id_job_password_cancel_post**
> ChangeStatus api_v2_jobs_id_job_password_cancel_post(id_job, password)

Cancel API

API to cancel a Job

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job

try:
    # Cancel API
    api_response = api_instance.api_v2_jobs_id_job_password_cancel_post(id_job, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job | 

### Return type

[**ChangeStatus**](ChangeStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_id_job_password_comments_get**
> Comments api_v2_jobs_id_job_password_comments_get(id_job, password, from_id=from_id)

Get segment comments in a job

Gets the list of comments on all job segments.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job
from_id = 56 # int | Only return records starting from this id included (optional)

try:
    # Get segment comments in a job
    api_response = api_instance.api_v2_jobs_id_job_password_comments_get(id_job, password, from_id=from_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job | 
 **from_id** | **int**| Only return records starting from this id included | [optional] 

### Return type

[**Comments**](Comments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_id_job_password_get**
> Chunk api_v2_jobs_id_job_password_get(id_job, password)

Job Info

Get all information about a Job

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)

try:
    # Job Info
    api_response = api_instance.api_v2_jobs_id_job_password_get(id_job, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job (Translate password) | 

### Return type

[**Chunk**](Chunk.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = matecat_api.JobApi()
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
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_options_post: %s\n" % e)
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

# **api_v2_jobs_id_job_password_quality_report_get**
> QualityReport api_v2_jobs_id_job_password_quality_report_get(id_job, password)

Quality report

Quality report

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job

try:
    # Quality report
    api_response = api_instance.api_v2_jobs_id_job_password_quality_report_get(id_job, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_quality_report_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job | 

### Return type

[**QualityReport**](QualityReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_get**
> api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_get(id_job, password, id_segment, id_issue)

Get comments

Get comments

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)
id_segment = 'id_segment_example' # str | The id of the segment
id_issue = 'id_issue_example' # str | The id of the issue

try:
    # Get comments
    api_instance.api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_get(id_job, password, id_segment, id_issue)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job (Translate password) | 
 **id_segment** | **str**| The id of the segment | 
 **id_issue** | **str**| The id of the issue | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_post**
> api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_post(comment, id_qa_entry, source_page, uid, id_job, password, id_segment, id_issue)

Add comment to a translation issue

Create a comment translation issue

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
comment = 'comment_example' # str | 
id_qa_entry = 'id_qa_entry_example' # str | 
source_page = 'source_page_example' # str | 
uid = 'uid_example' # str | 
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)
id_segment = 'id_segment_example' # str | The id of the segment
id_issue = 'id_issue_example' # str | The id of the issue

try:
    # Add comment to a translation issue
    api_instance.api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_post(comment, id_qa_entry, source_page, uid, id_job, password, id_segment, id_issue)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment** | **str**|  | 
 **id_qa_entry** | **str**|  | 
 **source_page** | **str**|  | 
 **uid** | **str**|  | 
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job (Translate password) | 
 **id_segment** | **str**| The id of the segment | 
 **id_issue** | **str**| The id of the issue | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_delete**
> Issue api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_delete(id_job, password, id_segment, id_issue)

Delete a translation Issue

Delete a translation Issue

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)
id_segment = 'id_segment_example' # str | The id of the segment
id_issue = 'id_issue_example' # str | The id of the issue

try:
    # Delete a translation Issue
    api_response = api_instance.api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_delete(id_job, password, id_segment, id_issue)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job (Translate password) | 
 **id_segment** | **str**| The id of the segment | 
 **id_issue** | **str**| The id of the issue | 

### Return type

[**Issue**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_post**
> api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_post(rebutted_at, id_job, password, id_segment, id_issue)

Update translation issues

Update translation issues

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
rebutted_at = 'rebutted_at_example' # str | 
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)
id_segment = 'id_segment_example' # str | The id of the segment
id_issue = 'id_issue_example' # str | 

try:
    # Update translation issues
    api_instance.api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_post(rebutted_at, id_job, password, id_segment, id_issue)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rebutted_at** | **str**|  | 
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job (Translate password) | 
 **id_segment** | **str**| The id of the segment | 
 **id_issue** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_id_job_password_segments_id_segment_translation_issues_post**
> Issue api_v2_jobs_id_job_password_segments_id_segment_translation_issues_post(version_number, id_segment2, id_job2, id_category, severity, translation_version, target_text, start_node, start_offset, end_node, end_offset, is_full_segment, comment, id_job, password, id_segment)

Create translation issues

Create translation issues

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
version_number = 'version_number_example' # str | 
id_segment2 = 'id_segment_example' # str | 
id_job2 = 'id_job_example' # str | 
id_category = 'id_category_example' # str | 
severity = 'severity_example' # str | 
translation_version = 'translation_version_example' # str | 
target_text = 'target_text_example' # str | 
start_node = 'start_node_example' # str | 
start_offset = 'start_offset_example' # str | 
end_node = 'end_node_example' # str | 
end_offset = 'end_offset_example' # str | 
is_full_segment = 'is_full_segment_example' # str | 
comment = 'comment_example' # str | 
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)
id_segment = 'id_segment_example' # str | The id of the segment

try:
    # Create translation issues
    api_response = api_instance.api_v2_jobs_id_job_password_segments_id_segment_translation_issues_post(version_number, id_segment2, id_job2, id_category, severity, translation_version, target_text, start_node, start_offset, end_node, end_offset, is_full_segment, comment, id_job, password, id_segment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_segments_id_segment_translation_issues_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_number** | **str**|  | 
 **id_segment2** | **str**|  | 
 **id_job2** | **str**|  | 
 **id_category** | **str**|  | 
 **severity** | **str**|  | 
 **translation_version** | **str**|  | 
 **target_text** | **str**|  | 
 **start_node** | **str**|  | 
 **start_offset** | **str**|  | 
 **end_node** | **str**|  | 
 **end_offset** | **str**|  | 
 **is_full_segment** | **str**|  | 
 **comment** | **str**|  | 
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job (Translate password) | 
 **id_segment** | **str**| The id of the segment | 

### Return type

[**Issue**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = matecat_api.JobApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)
id_segment = 'id_segment_example' # str | The id of the segment

try:
    # Segment versions
    api_response = api_instance.api_v2_jobs_id_job_password_segments_id_segment_translation_versions_get(id_job, password, id_segment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_segments_id_segment_translation_versions_get: %s\n" % e)
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
api_instance = matecat_api.JobApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)
id_segment = 'id_segment_example' # str | The id of the segment
version_number = 'version_number_example' # str | The version number

try:
    # Get a Segment translation version
    api_response = api_instance.api_v2_jobs_id_job_password_segments_id_segment_translation_versions_version_number_get(id_job, password, id_segment, version_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_segments_id_segment_translation_versions_version_number_get: %s\n" % e)
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

# **api_v2_jobs_id_job_password_translation_issues_get**
> TranslationIssues api_v2_jobs_id_job_password_translation_issues_get(id_job, password)

Project translation issues

Project translation issues

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)

try:
    # Project translation issues
    api_response = api_instance.api_v2_jobs_id_job_password_translation_issues_get(id_job, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_translation_issues_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job (Translate password) | 

### Return type

[**TranslationIssues**](TranslationIssues.md)

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
api_instance = matecat_api.JobApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)

try:
    # Project translation versions
    api_response = api_instance.api_v2_jobs_id_job_password_translation_versions_get(id_job, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_translation_versions_get: %s\n" % e)
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

# **api_v2_jobs_id_job_password_translator_get**
> JobTranslatorItem api_v2_jobs_id_job_password_translator_get(id_job, password)

Gets the translator assigned to a job

Gets the translator assigned to a job.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job

try:
    # Gets the translator assigned to a job
    api_response = api_instance.api_v2_jobs_id_job_password_translator_get(id_job, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_translator_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job | 

### Return type

[**JobTranslatorItem**](JobTranslatorItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_jobs_id_job_password_translator_post**
> JobTranslatorItem api_v2_jobs_id_job_password_translator_post(email, delivery_date, timezone, id_job, password)

Assigns a job to a translator

Assigns a job to a translator.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
email = 'email_example' # str | 
delivery_date = 56 # int | 
timezone = 'timezone_example' # str | 
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job

try:
    # Assigns a job to a translator
    api_response = api_instance.api_v2_jobs_id_job_password_translator_post(email, delivery_date, timezone, id_job, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->api_v2_jobs_id_job_password_translator_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **delivery_date** | **int**|  | 
 **timezone** | **str**|  | 
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job | 

### Return type

[**JobTranslatorItem**](JobTranslatorItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **t_mx_id_job_password_post**
> t_mx_id_job_password_post(id_job, password)

Download Job TMX

Download the Job TMX 

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)

try:
    # Download Job TMX
    api_instance.t_mx_id_job_password_post(id_job, password)
except ApiException as e:
    print("Exception when calling JobApi->t_mx_id_job_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job (Translate password) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translation_id_job_password_get**
> translation_id_job_password_get(id_job, password)

Download Translation

Download the Job translation

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.JobApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job

try:
    # Download Translation
    api_instance.translation_id_job_password_get(id_job, password)
except ApiException as e:
    print("Exception when calling JobApi->translation_id_job_password_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_job** | **str**| The id of the job | 
 **password** | **str**| The password of the job | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


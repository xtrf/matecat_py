# matecat_api.TranslationIssuesApi

All URIs are relative to *https://virtserver.swaggerhub.com/xtrf/Matecat/2.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_get**](TranslationIssuesApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_get) | **GET** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues/{id_issue}/comments | Get comments
[**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_post**](TranslationIssuesApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_post) | **POST** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues/{id_issue}/comments | Add comment to a translation issue
[**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_delete**](TranslationIssuesApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_delete) | **DELETE** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues/{id_issue} | Delete a translation Issue
[**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_post**](TranslationIssuesApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_post) | **POST** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues/{id_issue} | Update translation issues
[**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_post**](TranslationIssuesApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_post) | **POST** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues | Create translation issues
[**api_v2_jobs_id_job_password_translation_issues_get**](TranslationIssuesApi.md#api_v2_jobs_id_job_password_translation_issues_get) | **GET** /api/v2/jobs/{id_job}/{password}/translation-issues | Project translation issues

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
api_instance = matecat_api.TranslationIssuesApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)
id_segment = 'id_segment_example' # str | The id of the segment
id_issue = 'id_issue_example' # str | The id of the issue

try:
    # Get comments
    api_instance.api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_get(id_job, password, id_segment, id_issue)
except ApiException as e:
    print("Exception when calling TranslationIssuesApi->api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_get: %s\n" % e)
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
api_instance = matecat_api.TranslationIssuesApi()
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
    print("Exception when calling TranslationIssuesApi->api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_post: %s\n" % e)
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
api_instance = matecat_api.TranslationIssuesApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)
id_segment = 'id_segment_example' # str | The id of the segment
id_issue = 'id_issue_example' # str | The id of the issue

try:
    # Delete a translation Issue
    api_response = api_instance.api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_delete(id_job, password, id_segment, id_issue)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationIssuesApi->api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_delete: %s\n" % e)
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
api_instance = matecat_api.TranslationIssuesApi()
rebutted_at = 'rebutted_at_example' # str | 
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)
id_segment = 'id_segment_example' # str | The id of the segment
id_issue = 'id_issue_example' # str | 

try:
    # Update translation issues
    api_instance.api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_post(rebutted_at, id_job, password, id_segment, id_issue)
except ApiException as e:
    print("Exception when calling TranslationIssuesApi->api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_post: %s\n" % e)
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
api_instance = matecat_api.TranslationIssuesApi()
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
    print("Exception when calling TranslationIssuesApi->api_v2_jobs_id_job_password_segments_id_segment_translation_issues_post: %s\n" % e)
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
api_instance = matecat_api.TranslationIssuesApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job (Translate password)

try:
    # Project translation issues
    api_response = api_instance.api_v2_jobs_id_job_password_translation_issues_get(id_job, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationIssuesApi->api_v2_jobs_id_job_password_translation_issues_get: %s\n" % e)
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


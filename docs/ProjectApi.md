# matecat_api.ProjectApi

All URIs are relative to *https://virtserver.swaggerhub.com/xtrf/Matecat/2.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_change_project_password_post**](ProjectApi.md#api_change_project_password_post) | **POST** /api/change_project_password | Change password
[**api_status_get**](ProjectApi.md#api_status_get) | **GET** /api/status | Retrieve the status of a project
[**api_v1_new_post**](ProjectApi.md#api_v1_new_post) | **POST** /api/v1/new | Create new Project on Matecat in detached mode
[**api_v2_projects_id_project_password_active_post**](ProjectApi.md#api_v2_projects_id_project_password_active_post) | **POST** /api/v2/projects/{id_project}/{password}/active | Active API
[**api_v2_projects_id_project_password_archive_post**](ProjectApi.md#api_v2_projects_id_project_password_archive_post) | **POST** /api/v2/projects/{id_project}/{password}/archive | Archive API
[**api_v2_projects_id_project_password_cancel_post**](ProjectApi.md#api_v2_projects_id_project_password_cancel_post) | **POST** /api/v2/projects/{id_project}/{password}/cancel | Cancel API
[**api_v2_projects_id_project_password_completion_status_get**](ProjectApi.md#api_v2_projects_id_project_password_completion_status_get) | **GET** /api/v2/projects/{id_project}/{password}/completion_status | Shows project completion statuses
[**api_v2_projects_id_project_password_creation_status_get**](ProjectApi.md#api_v2_projects_id_project_password_creation_status_get) | **GET** /api/v2/projects/{id_project}/{password}/creation_status | Shows creation status of a project
[**api_v2_projects_id_project_password_due_date_delete**](ProjectApi.md#api_v2_projects_id_project_password_due_date_delete) | **DELETE** /api/v2/projects/{id_project}/{password}/due_date | Delete due date
[**api_v2_projects_id_project_password_due_date_post**](ProjectApi.md#api_v2_projects_id_project_password_due_date_post) | **POST** /api/v2/projects/{id_project}/{password}/due_date | Create due date
[**api_v2_projects_id_project_password_due_date_put**](ProjectApi.md#api_v2_projects_id_project_password_due_date_put) | **PUT** /api/v2/projects/{id_project}/{password}/due_date | Update due date
[**api_v2_projects_id_project_password_get**](ProjectApi.md#api_v2_projects_id_project_password_get) | **GET** /api/v2/projects/{id_project}/{password} | Get project information
[**api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_apply_post**](ProjectApi.md#api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_apply_post) | **POST** /api/v2/projects/{id_project}/{password}/jobs/{id_job}/{job_password}/split/{num_split}/apply | Split Job
[**api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_check_post**](ProjectApi.md#api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_check_post) | **POST** /api/v2/projects/{id_project}/{password}/jobs/{id_job}/{job_password}/split/{num_split}/check | Split Check
[**api_v2_projects_id_project_password_jobs_id_job_merge_post**](ProjectApi.md#api_v2_projects_id_project_password_jobs_id_job_merge_post) | **POST** /api/v2/projects/{id_project}/{password}/jobs/{id_job}/merge | Merge
[**api_v2_projects_id_project_password_urls_get**](ProjectApi.md#api_v2_projects_id_project_password_urls_get) | **GET** /api/v2/projects/{id_project}/{password}/urls | Urls of a Project

# **api_change_project_password_post**
> ChangePasswordResponse api_change_project_password_post(id_project, old_pass, new_pass)

Change password

Change the password of a project.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.ProjectApi()
id_project = 56 # int | 
old_pass = 'old_pass_example' # str | 
new_pass = 'new_pass_example' # str | 

try:
    # Change password
    api_response = api_instance.api_change_project_password_post(id_project, old_pass, new_pass)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_change_project_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_project** | **int**|  | 
 **old_pass** | **str**|  | 
 **new_pass** | **str**|  | 

### Return type

[**ChangePasswordResponse**](ChangePasswordResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_status_get**
> Status api_status_get(id_project, project_pass)

Retrieve the status of a project

Check Status of a created Project With HTTP POST ( application/x-www-form-urlencoded ) protocol

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.ProjectApi()
id_project = 56 # int | The identifier of the project, should be the value returned by the /new method.
project_pass = 'project_pass_example' # str | The password associated with the project, should be the value returned by the /new method ( associated with the id_project )

try:
    # Retrieve the status of a project
    api_response = api_instance.api_status_get(id_project, project_pass)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_project** | **int**| The identifier of the project, should be the value returned by the /new method. | 
 **project_pass** | **str**| The password associated with the project, should be the value returned by the /new method ( associated with the id_project ) | 

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_new_post**
> NewProject api_v1_new_post(files, project_name, source_lang, target_lang, tms_engine, mt_engine, private_tm_key, subject, segmentation_rule, owner_email, due_date, id_team, lexiqa, speech2text, get_public_matches, pretranslate_100, metadata)

Create new Project on Matecat in detached mode

Create new Project on Matecat With HTTP POST ( multipart/form-data ) protocol. new has a maximum file size limit of 200 MB per file and a max number of files of 600. This API will process the project creation in background. Client can poll the v1 project creation status API to be notified when the project is actually created.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.ProjectApi()
files = 'files_example' # str | 
project_name = 'project_name_example' # str | 
source_lang = 'source_lang_example' # str | 
target_lang = 'target_lang_example' # str | 
tms_engine = 56 # int | 
mt_engine = 56 # int | 
private_tm_key = 'private_tm_key_example' # str | 
subject = 'subject_example' # str | 
segmentation_rule = 'segmentation_rule_example' # str | 
owner_email = 'owner_email_example' # str | 
due_date = 'due_date_example' # str | 
id_team = 'id_team_example' # str | 
lexiqa = 'lexiqa_example' # str | 
speech2text = 56 # int | 
get_public_matches = 'get_public_matches_example' # str | 
pretranslate_100 = 56 # int | 
metadata = 'metadata_example' # str | 

try:
    # Create new Project on Matecat in detached mode
    api_response = api_instance.api_v1_new_post(files, project_name, source_lang, target_lang, tms_engine, mt_engine, private_tm_key, subject, segmentation_rule, owner_email, due_date, id_team, lexiqa, speech2text, get_public_matches, pretranslate_100, metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v1_new_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files** | **str**|  | 
 **project_name** | **str**|  | 
 **source_lang** | **str**|  | 
 **target_lang** | **str**|  | 
 **tms_engine** | **int**|  | 
 **mt_engine** | **int**|  | 
 **private_tm_key** | **str**|  | 
 **subject** | **str**|  | 
 **segmentation_rule** | **str**|  | 
 **owner_email** | **str**|  | 
 **due_date** | **str**|  | 
 **id_team** | **str**|  | 
 **lexiqa** | **str**|  | 
 **speech2text** | **int**|  | 
 **get_public_matches** | **str**|  | 
 **pretranslate_100** | **int**|  | 
 **metadata** | **str**|  | 

### Return type

[**NewProject**](NewProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_project_password_active_post**
> ChangeStatus api_v2_projects_id_project_password_active_post(id_project, password)

Active API

API to active a Project

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.ProjectApi()
id_project = 'id_project_example' # str | The id of the project
password = 'password_example' # str | The password of the project

try:
    # Active API
    api_response = api_instance.api_v2_projects_id_project_password_active_post(id_project, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_projects_id_project_password_active_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_project** | **str**| The id of the project | 
 **password** | **str**| The password of the project | 

### Return type

[**ChangeStatus**](ChangeStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_project_password_archive_post**
> ChangeStatus api_v2_projects_id_project_password_archive_post(id_project, password)

Archive API

API to archive a Project

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.ProjectApi()
id_project = 'id_project_example' # str | The id of the project
password = 'password_example' # str | The password of the project

try:
    # Archive API
    api_response = api_instance.api_v2_projects_id_project_password_archive_post(id_project, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_projects_id_project_password_archive_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_project** | **str**| The id of the project | 
 **password** | **str**| The password of the project | 

### Return type

[**ChangeStatus**](ChangeStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_project_password_cancel_post**
> ChangeStatus api_v2_projects_id_project_password_cancel_post(id_project, password)

Cancel API

API to cancel a Project

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.ProjectApi()
id_project = 'id_project_example' # str | The id of the project
password = 'password_example' # str | The password of the project

try:
    # Cancel API
    api_response = api_instance.api_v2_projects_id_project_password_cancel_post(id_project, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_projects_id_project_password_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_project** | **str**| The id of the project | 
 **password** | **str**| The password of the project | 

### Return type

[**ChangeStatus**](ChangeStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_project_password_completion_status_get**
> CompletionStatusItem api_v2_projects_id_project_password_completion_status_get(id_project, password)

Shows project completion statuses

Shows project completion statuses, it is related to the phases defined by the click on Marked As Completed button.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.ProjectApi()
id_project = 56 # int | The id of the project
password = 'password_example' # str | The password of the project

try:
    # Shows project completion statuses
    api_response = api_instance.api_v2_projects_id_project_password_completion_status_get(id_project, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_projects_id_project_password_completion_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_project** | **int**| The id of the project | 
 **password** | **str**| The password of the project | 

### Return type

[**CompletionStatusItem**](CompletionStatusItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_project_password_creation_status_get**
> ProjectCreationStatus api_v2_projects_id_project_password_creation_status_get(id_project, password)

Shows creation status of a project

Shows creation status of a project.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.ProjectApi()
id_project = 'id_project_example' # str | The id of the project
password = 'password_example' # str | The password of the project

try:
    # Shows creation status of a project
    api_response = api_instance.api_v2_projects_id_project_password_creation_status_get(id_project, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_projects_id_project_password_creation_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_project** | **str**| The id of the project | 
 **password** | **str**| The password of the project | 

### Return type

[**ProjectCreationStatus**](ProjectCreationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_project_password_due_date_delete**
> Project api_v2_projects_id_project_password_due_date_delete(id_project, password)

Delete due date

Delete due date given a project

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.ProjectApi()
id_project = 'id_project_example' # str | The id of the project
password = 'password_example' # str | The password of the project

try:
    # Delete due date
    api_response = api_instance.api_v2_projects_id_project_password_due_date_delete(id_project, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_projects_id_project_password_due_date_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_project** | **str**| The id of the project | 
 **password** | **str**| The password of the project | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_project_password_due_date_post**
> Project api_v2_projects_id_project_password_due_date_post(due_date, id_project, password)

Create due date

Create due date given a project

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.ProjectApi()
due_date = 56 # int | 
id_project = 'id_project_example' # str | The id of the project
password = 'password_example' # str | The password of the project

try:
    # Create due date
    api_response = api_instance.api_v2_projects_id_project_password_due_date_post(due_date, id_project, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_projects_id_project_password_due_date_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **due_date** | **int**|  | 
 **id_project** | **str**| The id of the project | 
 **password** | **str**| The password of the project | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_project_password_due_date_put**
> Project api_v2_projects_id_project_password_due_date_put(body, id_project, password)

Update due date

Update due date given a project

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.ProjectApi()
body = matecat_api.Body2() # Body2 | Date you want to set as due date. Date must be in the future
id_project = 'id_project_example' # str | The id of the project
password = 'password_example' # str | The password of the project

try:
    # Update due date
    api_response = api_instance.api_v2_projects_id_project_password_due_date_put(body, id_project, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_projects_id_project_password_due_date_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)| Date you want to set as due date. Date must be in the future | 
 **id_project** | **str**| The id of the project | 
 **password** | **str**| The password of the project | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_project_password_get**
> Project api_v2_projects_id_project_password_get(id_project, password)

Get project information

Retrieve information on the specified Project

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.ProjectApi()
id_project = 56 # int | The project ID
password = 'password_example' # str | The project Password

try:
    # Get project information
    api_response = api_instance.api_v2_projects_id_project_password_get(id_project, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_projects_id_project_password_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_project** | **int**| The project ID | 
 **password** | **str**| The project Password | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_apply_post**
> Split api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_apply_post(id_project, password, id_job, job_password, num_split, split_values=split_values)

Split Job

Check a job can be splitted

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.ProjectApi()
id_project = 'id_project_example' # str | The id of the project
password = 'password_example' # str | The password of the project
id_job = 'id_job_example' # str | The id of the job
job_password = 'job_password_example' # str | The password of the job
num_split = 56 # int | Number of chuck you want to split
split_values = [3.4] # list[float] |  (optional)

try:
    # Split Job
    api_response = api_instance.api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_apply_post(id_project, password, id_job, job_password, num_split, split_values=split_values)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_apply_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_project** | **str**| The id of the project | 
 **password** | **str**| The password of the project | 
 **id_job** | **str**| The id of the job | 
 **job_password** | **str**| The password of the job | 
 **num_split** | **int**| Number of chuck you want to split | 
 **split_values** | [**list[float]**](float.md)|  | [optional] 

### Return type

[**Split**](Split.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_check_post**
> Split api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_check_post(id_project, password, id_job, job_password, num_split)

Split Check

Check a job can be splitted

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.ProjectApi()
id_project = 'id_project_example' # str | The id of the project
password = 'password_example' # str | The password of the project
id_job = 'id_job_example' # str | The id of the job
job_password = 'job_password_example' # str | The password of the job
num_split = 56 # int | Number of chuck you want to split

try:
    # Split Check
    api_response = api_instance.api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_check_post(id_project, password, id_job, job_password, num_split)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_check_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_project** | **str**| The id of the project | 
 **password** | **str**| The password of the project | 
 **id_job** | **str**| The id of the job | 
 **job_password** | **str**| The password of the job | 
 **num_split** | **int**| Number of chuck you want to split | 

### Return type

[**Split**](Split.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_project_password_jobs_id_job_merge_post**
> api_v2_projects_id_project_password_jobs_id_job_merge_post(id_project, password, id_job)

Merge

Merge a splitted project

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.ProjectApi()
id_project = 'id_project_example' # str | The id of the project
password = 'password_example' # str | The password of the project
id_job = 'id_job_example' # str | 

try:
    # Merge
    api_instance.api_v2_projects_id_project_password_jobs_id_job_merge_post(id_project, password, id_job)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_projects_id_project_password_jobs_id_job_merge_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_project** | **str**| The id of the project | 
 **password** | **str**| The password of the project | 
 **id_job** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_project_password_urls_get**
> Urls api_v2_projects_id_project_password_urls_get(id_project, password)

Urls of a Project

Urls of a Project

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.ProjectApi()
id_project = 'id_project_example' # str | The id of the project
password = 'password_example' # str | The password of the project

try:
    # Urls of a Project
    api_response = api_instance.api_v2_projects_id_project_password_urls_get(id_project, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->api_v2_projects_id_project_password_urls_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_project** | **str**| The id of the project | 
 **password** | **str**| The password of the project | 

### Return type

[**Urls**](Urls.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# matecat_api.TeamsApi

All URIs are relative to *https://virtserver.swaggerhub.com/xtrf/Matecat/2.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_teams_get**](TeamsApi.md#api_v2_teams_get) | **GET** /api/v2/teams | List available teams
[**api_v2_teams_id_team_members_get**](TeamsApi.md#api_v2_teams_id_team_members_get) | **GET** /api/v2/teams/{id_team}/members | List team members
[**api_v2_teams_id_team_members_id_member_delete**](TeamsApi.md#api_v2_teams_id_team_members_id_member_delete) | **DELETE** /api/v2/teams/{id_team}/members/{id_member} | List team members
[**api_v2_teams_id_team_members_post**](TeamsApi.md#api_v2_teams_id_team_members_post) | **POST** /api/v2/teams/{id_team}/members | Create new team memberships
[**api_v2_teams_id_team_projects_get**](TeamsApi.md#api_v2_teams_id_team_projects_get) | **GET** /api/v2/teams/{id_team}/projects | Get the list of projects in a team
[**api_v2_teams_id_team_projects_id_project_get**](TeamsApi.md#api_v2_teams_id_team_projects_id_project_get) | **GET** /api/v2/teams/{id_team}/projects/{id_project} | Get a project in a team scope
[**api_v2_teams_id_team_projects_id_project_put**](TeamsApi.md#api_v2_teams_id_team_projects_id_project_put) | **PUT** /api/v2/teams/{id_team}/projects/{id_project} | Update a team&#x27;s project
[**api_v2_teams_id_team_projects_project_name_get**](TeamsApi.md#api_v2_teams_id_team_projects_project_name_get) | **GET** /api/v2/teams/{id_team}/projects/{project_name} | Get projects in a team scope
[**api_v2_teams_id_team_put**](TeamsApi.md#api_v2_teams_id_team_put) | **PUT** /api/v2/teams/{id_team} | Update team
[**api_v2_teams_post**](TeamsApi.md#api_v2_teams_post) | **POST** /api/v2/teams | Create a new team

# **api_v2_teams_get**
> TeamList api_v2_teams_get()

List available teams

Returns a list of all teams the current user is member of.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.TeamsApi()

try:
    # List available teams
    api_response = api_instance.api_v2_teams_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->api_v2_teams_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TeamList**](TeamList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_teams_id_team_members_get**
> TeamMembersList api_v2_teams_id_team_members_get(id_team)

List team members

List team members.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.TeamsApi()
id_team = 56 # int | 

try:
    # List team members
    api_response = api_instance.api_v2_teams_id_team_members_get(id_team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->api_v2_teams_id_team_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_team** | **int**|  | 

### Return type

[**TeamMembersList**](TeamMembersList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_teams_id_team_members_id_member_delete**
> TeamMembersList api_v2_teams_id_team_members_id_member_delete(id_team, id_member)

List team members

List team members.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.TeamsApi()
id_team = 56 # int | 
id_member = 56 # int | Id of the user to remove from team

try:
    # List team members
    api_response = api_instance.api_v2_teams_id_team_members_id_member_delete(id_team, id_member)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->api_v2_teams_id_team_members_id_member_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_team** | **int**|  | 
 **id_member** | **int**| Id of the user to remove from team | 

### Return type

[**TeamMembersList**](TeamMembersList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_teams_id_team_members_post**
> TeamMembersList api_v2_teams_id_team_members_post(id_team, members=members)

Create new team memberships

Create new team memberships.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.TeamsApi()
id_team = 56 # int | 
members = ['members_example'] # list[str] |  (optional)

try:
    # Create new team memberships
    api_response = api_instance.api_v2_teams_id_team_members_post(id_team, members=members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->api_v2_teams_id_team_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_team** | **int**|  | 
 **members** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**TeamMembersList**](TeamMembersList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_teams_id_team_projects_get**
> ProjectList api_v2_teams_id_team_projects_get(id_team)

Get the list of projects in a team

Get the list of projects in a team.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.TeamsApi()
id_team = 56 # int | 

try:
    # Get the list of projects in a team
    api_response = api_instance.api_v2_teams_id_team_projects_get(id_team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->api_v2_teams_id_team_projects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_team** | **int**|  | 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_teams_id_team_projects_id_project_get**
> ProjectItem api_v2_teams_id_team_projects_id_project_get(id_team, id_project)

Get a project in a team scope

Get a project in a team scope.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.TeamsApi()
id_team = 56 # int | 
id_project = 56 # int | 

try:
    # Get a project in a team scope
    api_response = api_instance.api_v2_teams_id_team_projects_id_project_get(id_team, id_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->api_v2_teams_id_team_projects_id_project_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_team** | **int**|  | 
 **id_project** | **int**|  | 

### Return type

[**ProjectItem**](ProjectItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_teams_id_team_projects_id_project_put**
> ProjectItem api_v2_teams_id_team_projects_id_project_put(body, id_team, id_project)

Update a team's project

Updates a team's project.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.TeamsApi()
body = matecat_api.Body9() # Body9 | Parameters in JSON Body
id_team = 56 # int | 
id_project = 56 # int | 

try:
    # Update a team's project
    api_response = api_instance.api_v2_teams_id_team_projects_id_project_put(body, id_team, id_project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->api_v2_teams_id_team_projects_id_project_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body9**](Body9.md)| Parameters in JSON Body | 
 **id_team** | **int**|  | 
 **id_project** | **int**|  | 

### Return type

[**ProjectItem**](ProjectItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_teams_id_team_projects_project_name_get**
> ProjectsItems api_v2_teams_id_team_projects_project_name_get(id_team, project_name)

Get projects in a team scope

Get projects in a team scope by name.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.TeamsApi()
id_team = 56 # int | 
project_name = 'project_name_example' # str | The name can also be a part of a project name

try:
    # Get projects in a team scope
    api_response = api_instance.api_v2_teams_id_team_projects_project_name_get(id_team, project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->api_v2_teams_id_team_projects_project_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_team** | **int**|  | 
 **project_name** | **str**| The name can also be a part of a project name | 

### Return type

[**ProjectsItems**](ProjectsItems.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_teams_id_team_put**
> TeamItem api_v2_teams_id_team_put(body, id_team)

Update team

Update team.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.TeamsApi()
body = matecat_api.Body7() # Body7 | Parameters in JSON Body
id_team = 56 # int | 

try:
    # Update team
    api_response = api_instance.api_v2_teams_id_team_put(body, id_team)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->api_v2_teams_id_team_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body7**](Body7.md)| Parameters in JSON Body | 
 **id_team** | **int**|  | 

### Return type

[**TeamItem**](TeamItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_teams_post**
> TeamItem api_v2_teams_post(type, name, members)

Create a new team

Creates a new team.

### Example
```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.TeamsApi()
type = 'type_example' # str | 
name = 'name_example' # str | 
members = ['members_example'] # list[str] | 

try:
    # Create a new team
    api_response = api_instance.api_v2_teams_post(type, name, members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->api_v2_teams_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **name** | **str**|  | 
 **members** | [**list[str]**](str.md)|  | 

### Return type

[**TeamItem**](TeamItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


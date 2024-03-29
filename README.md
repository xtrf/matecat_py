> **Warning**
> This is auto-generated library based on Matecat API. This is deprecated and will not be maintained anymore - XTRF does not guarantee that this code will work as intended (or at all) and cannot be held responsible for the results of running that it. 

# matecat-api
We developed a set of Rest API to let you integrate Matecat in your translation management system or in any other application. Use our API to create projects and check their status.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import matecat_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import matecat_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import matecat_api
from matecat_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = matecat_api.EnginesApi(matecat_api.ApiClient(configuration))

try:
    # Retrieve personal engine list.
    api_response = api_instance.api_v2_engines_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnginesApi->api_v2_engines_list_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/xtrf/Matecat/2.0.1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EnginesApi* | [**api_v2_engines_list_get**](docs/EnginesApi.md#api_v2_engines_list_get) | **GET** /api/v2/engines/list | Retrieve personal engine list.
*GlossaryApi* | [**api_v2_glossaries_export_tm_key_get**](docs/GlossaryApi.md#api_v2_glossaries_export_tm_key_get) | **GET** /api/v2/glossaries/export/{tm_key} | Download Glossary
*GlossaryApi* | [**api_v2_glossaries_import_post**](docs/GlossaryApi.md#api_v2_glossaries_import_post) | **POST** /api/v2/glossaries/import/ | Import Glossary
*GlossaryApi* | [**api_v2_glossaries_import_status_tm_key_get**](docs/GlossaryApi.md#api_v2_glossaries_import_status_tm_key_get) | **GET** /api/v2/glossaries/import/status/{tm_key} | Glossary Upload status.
*JobApi* | [**api_v1_jobs_id_job_password_stats_get**](docs/JobApi.md#api_v1_jobs_id_job_password_stats_get) | **GET** /api/v1/jobs/{id_job}/{password}/stats | Statistics
*JobApi* | [**api_v2_jobs_id_job_password_active_post**](docs/JobApi.md#api_v2_jobs_id_job_password_active_post) | **POST** /api/v2/jobs/{id_job}/{password}/active | Active API
*JobApi* | [**api_v2_jobs_id_job_password_archive_post**](docs/JobApi.md#api_v2_jobs_id_job_password_archive_post) | **POST** /api/v2/jobs/{id_job}/{password}/archive | Archive API
*JobApi* | [**api_v2_jobs_id_job_password_cancel_post**](docs/JobApi.md#api_v2_jobs_id_job_password_cancel_post) | **POST** /api/v2/jobs/{id_job}/{password}/cancel | Cancel API
*JobApi* | [**api_v2_jobs_id_job_password_comments_get**](docs/JobApi.md#api_v2_jobs_id_job_password_comments_get) | **GET** /api/v2/jobs/{id_job}/{password}/comments | Get segment comments in a job
*JobApi* | [**api_v2_jobs_id_job_password_get**](docs/JobApi.md#api_v2_jobs_id_job_password_get) | **GET** /api/v2/jobs/{id_job}/{password} | Job Info
*JobApi* | [**api_v2_jobs_id_job_password_options_post**](docs/JobApi.md#api_v2_jobs_id_job_password_options_post) | **POST** /api/v2/jobs/{id_job}/{password}/options | Update Options
*JobApi* | [**api_v2_jobs_id_job_password_quality_report_get**](docs/JobApi.md#api_v2_jobs_id_job_password_quality_report_get) | **GET** /api/v2/jobs/{id_job}/{password}/quality-report | Quality report
*JobApi* | [**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_get**](docs/JobApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_get) | **GET** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues/{id_issue}/comments | Get comments
*JobApi* | [**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_post**](docs/JobApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_post) | **POST** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues/{id_issue}/comments | Add comment to a translation issue
*JobApi* | [**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_delete**](docs/JobApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_delete) | **DELETE** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues/{id_issue} | Delete a translation Issue
*JobApi* | [**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_post**](docs/JobApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_post) | **POST** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues/{id_issue} | Update translation issues
*JobApi* | [**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_post**](docs/JobApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_post) | **POST** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues | Create translation issues
*JobApi* | [**api_v2_jobs_id_job_password_segments_id_segment_translation_versions_get**](docs/JobApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_versions_get) | **GET** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-versions | Segment versions
*JobApi* | [**api_v2_jobs_id_job_password_segments_id_segment_translation_versions_version_number_get**](docs/JobApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_versions_version_number_get) | **GET** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-versions/{version_number} | Get a Segment translation version
*JobApi* | [**api_v2_jobs_id_job_password_translation_issues_get**](docs/JobApi.md#api_v2_jobs_id_job_password_translation_issues_get) | **GET** /api/v2/jobs/{id_job}/{password}/translation-issues | Project translation issues
*JobApi* | [**api_v2_jobs_id_job_password_translation_versions_get**](docs/JobApi.md#api_v2_jobs_id_job_password_translation_versions_get) | **GET** /api/v2/jobs/{id_job}/{password}/translation-versions | Project translation versions
*JobApi* | [**api_v2_jobs_id_job_password_translator_get**](docs/JobApi.md#api_v2_jobs_id_job_password_translator_get) | **GET** /api/v2/jobs/{id_job}/{password}/translator | Gets the translator assigned to a job
*JobApi* | [**api_v2_jobs_id_job_password_translator_post**](docs/JobApi.md#api_v2_jobs_id_job_password_translator_post) | **POST** /api/v2/jobs/{id_job}/{password}/translator | Assigns a job to a translator
*JobApi* | [**t_mx_id_job_password_post**](docs/JobApi.md#t_mx_id_job_password_post) | **POST** /TMX/{id_job}/{password} | Download Job TMX
*JobApi* | [**translation_id_job_password_get**](docs/JobApi.md#translation_id_job_password_get) | **GET** /translation/{id_job}/{password} | Download Translation
*LanguagesApi* | [**api_v2_languages_get**](docs/LanguagesApi.md#api_v2_languages_get) | **GET** /api/v2/languages | Supported languages list.
*OptionsApi* | [**api_v2_jobs_id_job_password_options_post**](docs/OptionsApi.md#api_v2_jobs_id_job_password_options_post) | **POST** /api/v2/jobs/{id_job}/{password}/options | Update Options
*ProjectApi* | [**api_change_project_password_post**](docs/ProjectApi.md#api_change_project_password_post) | **POST** /api/change_project_password | Change password
*ProjectApi* | [**api_status_get**](docs/ProjectApi.md#api_status_get) | **GET** /api/status | Retrieve the status of a project
*ProjectApi* | [**api_v1_new_post**](docs/ProjectApi.md#api_v1_new_post) | **POST** /api/v1/new | Create new Project on Matecat in detached mode
*ProjectApi* | [**api_v2_projects_id_project_password_active_post**](docs/ProjectApi.md#api_v2_projects_id_project_password_active_post) | **POST** /api/v2/projects/{id_project}/{password}/active | Active API
*ProjectApi* | [**api_v2_projects_id_project_password_archive_post**](docs/ProjectApi.md#api_v2_projects_id_project_password_archive_post) | **POST** /api/v2/projects/{id_project}/{password}/archive | Archive API
*ProjectApi* | [**api_v2_projects_id_project_password_cancel_post**](docs/ProjectApi.md#api_v2_projects_id_project_password_cancel_post) | **POST** /api/v2/projects/{id_project}/{password}/cancel | Cancel API
*ProjectApi* | [**api_v2_projects_id_project_password_completion_status_get**](docs/ProjectApi.md#api_v2_projects_id_project_password_completion_status_get) | **GET** /api/v2/projects/{id_project}/{password}/completion_status | Shows project completion statuses
*ProjectApi* | [**api_v2_projects_id_project_password_creation_status_get**](docs/ProjectApi.md#api_v2_projects_id_project_password_creation_status_get) | **GET** /api/v2/projects/{id_project}/{password}/creation_status | Shows creation status of a project
*ProjectApi* | [**api_v2_projects_id_project_password_due_date_delete**](docs/ProjectApi.md#api_v2_projects_id_project_password_due_date_delete) | **DELETE** /api/v2/projects/{id_project}/{password}/due_date | Delete due date
*ProjectApi* | [**api_v2_projects_id_project_password_due_date_post**](docs/ProjectApi.md#api_v2_projects_id_project_password_due_date_post) | **POST** /api/v2/projects/{id_project}/{password}/due_date | Create due date
*ProjectApi* | [**api_v2_projects_id_project_password_due_date_put**](docs/ProjectApi.md#api_v2_projects_id_project_password_due_date_put) | **PUT** /api/v2/projects/{id_project}/{password}/due_date | Update due date
*ProjectApi* | [**api_v2_projects_id_project_password_get**](docs/ProjectApi.md#api_v2_projects_id_project_password_get) | **GET** /api/v2/projects/{id_project}/{password} | Get project information
*ProjectApi* | [**api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_apply_post**](docs/ProjectApi.md#api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_apply_post) | **POST** /api/v2/projects/{id_project}/{password}/jobs/{id_job}/{job_password}/split/{num_split}/apply | Split Job
*ProjectApi* | [**api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_check_post**](docs/ProjectApi.md#api_v2_projects_id_project_password_jobs_id_job_job_password_split_num_split_check_post) | **POST** /api/v2/projects/{id_project}/{password}/jobs/{id_job}/{job_password}/split/{num_split}/check | Split Check
*ProjectApi* | [**api_v2_projects_id_project_password_jobs_id_job_merge_post**](docs/ProjectApi.md#api_v2_projects_id_project_password_jobs_id_job_merge_post) | **POST** /api/v2/projects/{id_project}/{password}/jobs/{id_job}/merge | Merge
*ProjectApi* | [**api_v2_projects_id_project_password_urls_get**](docs/ProjectApi.md#api_v2_projects_id_project_password_urls_get) | **GET** /api/v2/projects/{id_project}/{password}/urls | Urls of a Project
*QualityReportApi* | [**api_v2_jobs_id_job_password_quality_report_get**](docs/QualityReportApi.md#api_v2_jobs_id_job_password_quality_report_get) | **GET** /api/v2/jobs/{id_job}/{password}/quality-report | Quality report
*TMKeysApi* | [**api_v2_keys_list_get**](docs/TMKeysApi.md#api_v2_keys_list_get) | **GET** /api/v2/keys/list | Retrieve private TM keys list.
*TeamsApi* | [**api_v2_teams_get**](docs/TeamsApi.md#api_v2_teams_get) | **GET** /api/v2/teams | List available teams
*TeamsApi* | [**api_v2_teams_id_team_members_get**](docs/TeamsApi.md#api_v2_teams_id_team_members_get) | **GET** /api/v2/teams/{id_team}/members | List team members
*TeamsApi* | [**api_v2_teams_id_team_members_id_member_delete**](docs/TeamsApi.md#api_v2_teams_id_team_members_id_member_delete) | **DELETE** /api/v2/teams/{id_team}/members/{id_member} | List team members
*TeamsApi* | [**api_v2_teams_id_team_members_post**](docs/TeamsApi.md#api_v2_teams_id_team_members_post) | **POST** /api/v2/teams/{id_team}/members | Create new team memberships
*TeamsApi* | [**api_v2_teams_id_team_projects_get**](docs/TeamsApi.md#api_v2_teams_id_team_projects_get) | **GET** /api/v2/teams/{id_team}/projects | Get the list of projects in a team
*TeamsApi* | [**api_v2_teams_id_team_projects_id_project_get**](docs/TeamsApi.md#api_v2_teams_id_team_projects_id_project_get) | **GET** /api/v2/teams/{id_team}/projects/{id_project} | Get a project in a team scope
*TeamsApi* | [**api_v2_teams_id_team_projects_id_project_put**](docs/TeamsApi.md#api_v2_teams_id_team_projects_id_project_put) | **PUT** /api/v2/teams/{id_team}/projects/{id_project} | Update a team&#x27;s project
*TeamsApi* | [**api_v2_teams_id_team_projects_project_name_get**](docs/TeamsApi.md#api_v2_teams_id_team_projects_project_name_get) | **GET** /api/v2/teams/{id_team}/projects/{project_name} | Get projects in a team scope
*TeamsApi* | [**api_v2_teams_id_team_put**](docs/TeamsApi.md#api_v2_teams_id_team_put) | **PUT** /api/v2/teams/{id_team} | Update team
*TeamsApi* | [**api_v2_teams_post**](docs/TeamsApi.md#api_v2_teams_post) | **POST** /api/v2/teams | Create a new team
*TranslationIssuesApi* | [**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_get**](docs/TranslationIssuesApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_get) | **GET** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues/{id_issue}/comments | Get comments
*TranslationIssuesApi* | [**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_post**](docs/TranslationIssuesApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_comments_post) | **POST** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues/{id_issue}/comments | Add comment to a translation issue
*TranslationIssuesApi* | [**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_delete**](docs/TranslationIssuesApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_delete) | **DELETE** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues/{id_issue} | Delete a translation Issue
*TranslationIssuesApi* | [**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_post**](docs/TranslationIssuesApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_id_issue_post) | **POST** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues/{id_issue} | Update translation issues
*TranslationIssuesApi* | [**api_v2_jobs_id_job_password_segments_id_segment_translation_issues_post**](docs/TranslationIssuesApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_issues_post) | **POST** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-issues | Create translation issues
*TranslationIssuesApi* | [**api_v2_jobs_id_job_password_translation_issues_get**](docs/TranslationIssuesApi.md#api_v2_jobs_id_job_password_translation_issues_get) | **GET** /api/v2/jobs/{id_job}/{password}/translation-issues | Project translation issues
*TranslationVersionsApi* | [**api_v2_jobs_id_job_password_segments_id_segment_translation_versions_get**](docs/TranslationVersionsApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_versions_get) | **GET** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-versions | Segment versions
*TranslationVersionsApi* | [**api_v2_jobs_id_job_password_segments_id_segment_translation_versions_version_number_get**](docs/TranslationVersionsApi.md#api_v2_jobs_id_job_password_segments_id_segment_translation_versions_version_number_get) | **GET** /api/v2/jobs/{id_job}/{password}/segments/{id_segment}/translation-versions/{version_number} | Get a Segment translation version
*TranslationVersionsApi* | [**api_v2_jobs_id_job_password_translation_versions_get**](docs/TranslationVersionsApi.md#api_v2_jobs_id_job_password_translation_versions_get) | **GET** /api/v2/jobs/{id_job}/{password}/translation-versions | Project translation versions

## Documentation For Models

 - [Body](docs/Body.md)
 - [Body1](docs/Body1.md)
 - [Body10](docs/Body10.md)
 - [Body11](docs/Body11.md)
 - [Body12](docs/Body12.md)
 - [Body13](docs/Body13.md)
 - [Body14](docs/Body14.md)
 - [Body2](docs/Body2.md)
 - [Body3](docs/Body3.md)
 - [Body4](docs/Body4.md)
 - [Body5](docs/Body5.md)
 - [Body6](docs/Body6.md)
 - [Body7](docs/Body7.md)
 - [Body8](docs/Body8.md)
 - [Body9](docs/Body9.md)
 - [ChangePasswordResponse](docs/ChangePasswordResponse.md)
 - [ChangeStatus](docs/ChangeStatus.md)
 - [Chunk](docs/Chunk.md)
 - [Comment](docs/Comment.md)
 - [Comments](docs/Comments.md)
 - [CompletionStatusItem](docs/CompletionStatusItem.md)
 - [CompletionStatusItemProjectStatus](docs/CompletionStatusItemProjectStatus.md)
 - [CompletionStatusItemProjectStatusRevise](docs/CompletionStatusItemProjectStatusRevise.md)
 - [DataStatus](docs/DataStatus.md)
 - [Engine](docs/Engine.md)
 - [EnginesList](docs/EnginesList.md)
 - [Error](docs/Error.md)
 - [ErrorErrors](docs/ErrorErrors.md)
 - [ExtendedJob](docs/ExtendedJob.md)
 - [ExtendedJobItem](docs/ExtendedJobItem.md)
 - [Files](docs/Files.md)
 - [Issue](docs/Issue.md)
 - [Job](docs/Job.md)
 - [JobFile](docs/JobFile.md)
 - [JobTranslatorItem](docs/JobTranslatorItem.md)
 - [JobUrl](docs/JobUrl.md)
 - [Jobs](docs/Jobs.md)
 - [JobsStatus](docs/JobsStatus.md)
 - [Key](docs/Key.md)
 - [KeysList](docs/KeysList.md)
 - [Language](docs/Language.md)
 - [Languages](docs/Languages.md)
 - [NewProject](docs/NewProject.md)
 - [Options](docs/Options.md)
 - [OutsourceConfirmation](docs/OutsourceConfirmation.md)
 - [PendingInvitation](docs/PendingInvitation.md)
 - [Project](docs/Project.md)
 - [ProjectCreationStatus](docs/ProjectCreationStatus.md)
 - [ProjectItem](docs/ProjectItem.md)
 - [ProjectList](docs/ProjectList.md)
 - [ProjectsItems](docs/ProjectsItems.md)
 - [QualityReport](docs/QualityReport.md)
 - [QualitySummary](docs/QualitySummary.md)
 - [QualitySummaryReviseIssues](docs/QualitySummaryReviseIssues.md)
 - [ReviseIssue](docs/ReviseIssue.md)
 - [Segment](docs/Segment.md)
 - [Split](docs/Split.md)
 - [SplitData](docs/SplitData.md)
 - [SplitDataChunks](docs/SplitDataChunks.md)
 - [Stats](docs/Stats.md)
 - [Status](docs/Status.md)
 - [Summary](docs/Summary.md)
 - [Team](docs/Team.md)
 - [TeamItem](docs/TeamItem.md)
 - [TeamList](docs/TeamList.md)
 - [TeamMember](docs/TeamMember.md)
 - [TeamMembersList](docs/TeamMembersList.md)
 - [Total](docs/Total.md)
 - [Totals](docs/Totals.md)
 - [TranslationIssues](docs/TranslationIssues.md)
 - [TranslationVersion](docs/TranslationVersion.md)
 - [TranslationVersions](docs/TranslationVersions.md)
 - [Translator](docs/Translator.md)
 - [UploadGlossaryStatus](docs/UploadGlossaryStatus.md)
 - [UploadGlossaryStatusObject](docs/UploadGlossaryStatusObject.md)
 - [Url](docs/Url.md)
 - [Urls](docs/Urls.md)
 - [UrlsJob](docs/UrlsJob.md)
 - [UrlsJobs](docs/UrlsJobs.md)
 - [User](docs/User.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author



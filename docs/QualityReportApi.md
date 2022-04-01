# matecat_api.QualityReportApi

All URIs are relative to *https://virtserver.swaggerhub.com/xtrf/Matecat/2.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_jobs_id_job_password_quality_report_get**](QualityReportApi.md#api_v2_jobs_id_job_password_quality_report_get) | **GET** /api/v2/jobs/{id_job}/{password}/quality-report | Quality report

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
api_instance = matecat_api.QualityReportApi()
id_job = 'id_job_example' # str | The id of the job
password = 'password_example' # str | The password of the job

try:
    # Quality report
    api_response = api_instance.api_v2_jobs_id_job_password_quality_report_get(id_job, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityReportApi->api_v2_jobs_id_job_password_quality_report_get: %s\n" % e)
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


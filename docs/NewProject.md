# NewProject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Return the creation status of the project. The statuses can be:OK indicating that the creation worked.FAIL indicating that the creation is failed. | [optional] 
**id_project** | **str** | Return the unique id of the project just created. If creation status is FAIL this key will simply be omitted from the result. | [optional] 
**project_pass** | **str** | Return the password of the project just created. If creation status is FAIL this key will simply be omitted from the result. | [optional] 
**new_keys** | **str** | If you specified new as one or more value in the private_tm_key parameter, the new created keys are returned as CSV string (4rcf34rc,r34rcfewf3r2). Otherwise empty string is returned | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


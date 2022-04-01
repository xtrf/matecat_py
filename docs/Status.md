# Status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **list[object]** | A list of objects containing error message at system wide level. Every error has a negative numeric code and a textual message ( currently the only error reported is the wrong version number in config.inc.php file and happens only after Matecat updates, so you should never see it ). | [optional] 
**data** | [**DataStatus**](DataStatus.md) |  | [optional] 
**status** | **str** | The analysis status of the project. ANALYZING - analysis/creation still in progress; NO_SEGMENTS_FOUND - the project has no segments to analyze (have you uploaded a file containing only images?); ANALYSIS_NOT_ENABLED - no analysis will be performed because of Matecat configuration; DONE - the analysis/creation is completed; FAIL - the analysis/creation is failed. | [optional] 
**analyze** | **str** | A link to the analyze page; it&#x27;s a human readable version of this API output | [optional] 
**jobs** | [**JobsStatus**](JobsStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


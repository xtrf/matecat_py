# JobsStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**langpairs** | **object** | the language pairs for your project; an entry for every chunk in the project, with the id-password combination as key and the language pair as the value | [optional] 
**job_url** | **object** | the links to the chunks of the project; an entry for every chunk in the project, with the id-password combination as key and the link to the chunk as the value. | [optional] 
**job_quality_details** | **list[object]** | a structure containing, for each chunk, an array of 5 objects, each object is a quality check performed on the job; the object contains the type of the check (Typing, Translation, Terminology, Language Quality, Style), the quantity of errors found, the allowed errors threshold and the rating given by the errors/threshold ratio (same as quality-overall) | [optional] 
**quality_overall** | **object** | the overall quality rating for each chunk (Very good, Good, Acceptable, Poor, Fail) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


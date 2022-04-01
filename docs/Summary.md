# Summary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A list of objects containing error message at system wide level. Every error has a negative numeric code and a textual message ( currently the only error reported is the wrong version number in config.inc.php file and happens only after Matecat updates, so you should never see it ). | [optional] 
**status** | **str** | The status the project is from analysis perspective. NEW - just created, not analyzed yet, FAST_OK - preliminary (fast) analysis completed, now running translations (\&quot;TM\&quot;) analysis, DONE - analysis complete. | [optional] 
**in_queue_before** | **str** | Number of segments belonging to other projects that are being analyzed before yours; it&#x27;s the wait time for you. | [optional] 
**total_segments** | **str** | number of segments belonging to your project. | [optional] 
**segments_analyzed** | **str** | analysis progress, on TOTAL_SEGMENTS | [optional] 
**total_raw_wc** | **str** | number of words (word count) of your project, as extracted by the textual parsers | [optional] 
**total_standard_wc** | **str** | word count, minus the sentences that are repeated | [optional] 
**total_fast_wc** | **str** | word count, minus the sentences that are partially repeated | [optional] 
**total_tm_wc** | **str** | word count, with sentences found in the cloud translation memory discounted from the total; this depends on the percentage of overlapping between the sentences of your project and the past translations | [optional] 
**total_payable** | **str** | total word count, after analysis. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


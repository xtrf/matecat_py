# Job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk** | **object** | A structure modeling a portion of content to translate.  A whole file can be splitted in multiple chunks, to be distributed to multiple translators, or can be enveloped in a single chunk. Each chunk has a password as first level key and a numerical ID as second level key to identify different chunks for the same file. Each chunk contains the same structure of the totals section. The sum of the chunks equals to the totals. | [optional] 
**totals** | [**Totals**](Totals.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


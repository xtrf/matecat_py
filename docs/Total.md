# Total

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_payable** | **list[object]** | total word count, after analysis | [optional] 
**repetitions** | **list[object]** | cumulative word count for the segments that repeat themselves in the file | [optional] 
**internal_matches** | **list[object]** | cumulative word count for the segments that fuzzily overlap with others in the file, while not being an exact repetition | [optional] 
**mt** | **list[object]** | cumulative word count for all segments that can be translated with machine translation; it accounts for all the information that could not be discounted by repetitions, internal matches or translation memory | [optional] 
**new** | **list[object]** | cumulative word count for segments that can&#x27;t be discounted with repetition or internal matches; it&#x27;s the net translation effort | [optional] 
**tm_100** | **list[object]** | cumulative word count for the exact matches found in TM server | [optional] 
**tm_75_99** | **list[object]** | cumulative word count for partial matches in the TM that cover 75-99% of each segment | [optional] 
**ice** | **list[object]** | cumulative word count for 100% TM matches that also share the same context with the TM | [optional] 
**numbers_only** | **list[object]** | cumulative word counts for segments made of numberings, dates and similar not translatable data ( i.e. 93 / 127 ) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


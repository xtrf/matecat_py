# Body

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **str** | The file(s) to be uploaded. You may also upload your own translation memories (TMX). | 
**project_name** | **str** | The name of the project you want create. | 
**source_lang** | **str** | RFC 5646 language+region Code ( en-US case sensitive ) as specified in W3C standards. | 
**target_lang** | **str** | RFC 5646 language+region Code ( en-US case sensitive ) as specified in W3C standards. Multiple languages must be comma separated ( it-IT,fr-FR,es-ES case sensitive) | 
**tms_engine** | **int** | Identifier for Memory Server 0 means disabled, 1 means MyMemory) | [optional] [default to 1]
**mt_engine** | **int** | Identifier for Machine Translation Service 0 means disabled, 1 means get MT from MyMemory). | [optional] [default to 1]
**private_tm_key** | **str** | Private key(s) for MyMemory.  If a TMX file is uploaded and no key is provided, a new key will be created. - Existing MyMemory private keys or new to create a new key. - Multiple keys must be comma separated. Up to 5 keys allowed. (xxx345cvf,new,s342f234fc) - If you want to set read, write or both on your private key you can add after the key &#x27;r&#x27; for read, &#x27;w&#x27; for write or &#x27;rw&#x27; for both  separated by &#x27;:&#x27; (xxx345cvf:r,new:w,s342f234fc:rw) - Only available if tms_engine is set to 1 or if is not used | [optional] 
**subject** | **str** | The subject of the project you want to create. | [optional] [default to 'general']
**segmentation_rule** | **str** | The segmentation rule you want to use to parse your file. | [optional] 
**owner_email** | **str** | The email of the owner of the project. This parameter is deprecated and being replaced by authentication headers. | [optional] [default to 'anonymous']
**due_date** | **str** | If you want to set a due date for your project, send this param with a timestamp | [optional] 
**id_team** | **str** | The team you want to assign this project | [optional] 
**lexiqa** | **str** | Enable lexiQA QA check. Requires purchase of a license from lexiQA. | [optional] [default to '0']
**speech2text** | **int** | Improved accessibility thanks to a speech-to-text component to dictate your translations instead of typing them. | [optional] [default to 0]
**get_public_matches** | **str** | Enable suggestions from the Public TM | [optional] [default to 'true']
**pretranslate_100** | **int** | Pre-translate 100% matches from TM | [optional] [default to 0]
**metadata** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# EvalContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | entityID is used to deterministically at random to evaluate the flag result. If it&#39;s empty, flagr will randomly generate one. | [optional] 
**entity_type** | **str** |  | [optional] 
**entity_context** | **object** |  | [optional] 
**enable_debug** | **bool** |  | [optional] 
**flag_id** | **int** | flagID | [optional] 
**flag_key** | **str** | flagKey. flagID or flagKey will resolve to the same flag. Either works. | [optional] 
**flag_tags** | **list[str]** | flagTags. flagTags looks up flags by tag. Either works. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



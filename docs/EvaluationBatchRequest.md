# EvaluationBatchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**list[EvaluationEntity]**](EvaluationEntity.md) |  | 
**enable_debug** | **bool** |  | [optional] 
**flag_i_ds** | **list[int]** | flagIDs | [optional] 
**flag_keys** | **list[str]** | flagKeys. Either flagIDs, flagKeys or flagTags works. If pass in multiples, Flagr may return duplicate results. | [optional] 
**flag_tags** | **list[str]** | flagTags. Either flagIDs, flagKeys or flagTags works. If pass in multiples, Flagr may return duplicate results. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



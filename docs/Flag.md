# Flag

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**key** | **str** | unique key representation of the flag | [optional] 
**description** | **str** |  | 
**enabled** | **bool** |  | 
**segments** | [**list[Segment]**](Segment.md) |  | [optional] 
**variants** | [**list[Variant]**](Variant.md) |  | [optional] 
**data_records_enabled** | **bool** | enabled data records will get data logging in the metrics pipeline, for example, kafka. | 
**entity_type** | **str** | it will override the entityType in the evaluation logs if it&#39;s not empty | [optional] 
**created_by** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



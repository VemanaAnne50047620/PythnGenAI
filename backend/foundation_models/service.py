import boto3


bedrock_client = boto3.client(
    service_name="bedrock",
    region_name="eu-west-2"
)


def list_foundation_models():
    response = bedrock_client.list_foundation_models()

    return response['modelSummaries']


def get_foundation_model(model_id):
    response = bedrock_client.get_foundation_model(
        modelIdentifier=model_id
    )

    return response['modelDetails']

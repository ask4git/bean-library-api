import json


def get_json_response(response):
    if response.streaming:
        content = ''.join((chunk for chunk
                           in response.streaming_content))
        return json.loads(content)
    return json.loads(response.content)

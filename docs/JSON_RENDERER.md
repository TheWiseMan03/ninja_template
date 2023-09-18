# Creating a Custom JSON Renderer

This code is a definition of a custom renderer for use in the Ninja framework

```bash
import orjson  
from ninja.renderers import BaseRenderer  

class ORJSONRenderer(BaseRenderer):
    # Specify the media type (Content-Type) for this renderer
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        # We form the response structure, which includes the response status and data
        response_template = {
            "status": response_status,  
            "data": data,  
        }

        # Use the orjson library to serialize data into JSON format and return the JSON representation of the response as a byte string
        return orjson.dumps(response_template)
```

So this code creates a custom renderer, ORJSONRenderer, which can be used in Ninja to serialize data into JSON when sending responses to requests.
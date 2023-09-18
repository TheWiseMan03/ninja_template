# Implementation of function for pagination 

```bash
from asgiref.sync import sync_to_async

# Wrap the paginate_response function with the @sync_to_async decorator for asynchronous operation
@sync_to_async
def paginate_response(queryset, Schema, page: int = 1, size: int = 10, ordering: list = ['-id']):
    # Calculate the offset and limit for the current page
    offset = (page - 1) * size
    limit = size

    # Retrieving elements from the queryset, converting them into objects using Schema
    items = [Schema.from_orm(item) for item in queryset.order_by(*ordering)[offset:offset + limit]]
    # Calculate the total number of elements in the queryset
    total = queryset.count()
    
    # Return a dictionary with information about the current page and results
    return {
        "items": items,  
        "total": total, 
        "page": page,    
        "size": size,   
    }
```

### Implementation of function for pagination of database query results in an asynchronous environment using the asgiref library and the @sync_to_async annotation. These functions paginate large data sets and return information about the current page, page size, and total number of elements in the query result.
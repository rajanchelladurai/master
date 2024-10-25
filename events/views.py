from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_events(request):
    # Static event data
    events = [
        {
            "id": 1,
            "title": "Music Concert",
            "description": "A live music concert featuring various artists.",
            "start_date": "2024-10-28T19:00:00Z",
            "end_date": "2024-10-28T22:00:00Z"
        },
        {
            "id": 2,
            "title": "Art Exhibition",
            "description": "An exhibition showcasing contemporary art.",
            "start_date": "2024-11-05T10:00:00Z",
            "end_date": "2024-11-05T18:00:00Z"
        },
        {
            "id": 3,
            "title": "Tech Conference",
            "description": "A conference about the latest trends in technology.",
            "start_date": "2024-12-01T09:00:00Z",
            "end_date": "2024-12-01T17:00:00Z"
        }
    ]

    return Response(events)

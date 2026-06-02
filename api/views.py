
from django.http import JsonResponse
from .models import Note

def get_notes(request):
    # Grab all notes from the database and select the specific fields we want
    notes = Note.objects.all().values('id', 'title', 'content', 'created_at')
    
    # Convert it into a JSON response
    return JsonResponse(list(notes), safe=False)
# Create your views here.

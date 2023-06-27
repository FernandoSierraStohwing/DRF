from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import Programmer

# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    serializer_class = ProgrammerSerializer
    
    def get_queryset(self):
        return Programmer.objects.all()
    
    # querySet = Programmer.objects.all()
    # serializer_class = ProgrammerSerializer
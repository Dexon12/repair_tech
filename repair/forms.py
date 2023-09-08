from dal import autocomplete
from .models import Services

class ServiceAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Services.objects.all()
        if self.q:
            qs = qs.filter(title__icontains=self.q)
        return qs
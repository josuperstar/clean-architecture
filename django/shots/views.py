
from django.views import generic
from .models import Shot


class IndexView(generic.ListView):
    template_name = "shots/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Shot.objects.order_by("-pub_date")[:5]

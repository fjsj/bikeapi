from django.views import generic


class SampleView(generic.TemplateView):
    template_name = 'sample.html'

from rest_framework import generics, permissions
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from .models import Enquiry
from .serializers import EnquiryListSerializer, EnquirySerializer
from .forms import EnquiryForm

from django.contrib.auth import get_user_model
User = get_user_model()


def EnquiryClaim(request, pk):
    data = get_object_or_404(Enquiry, pk=pk)
    data.claim(request=request)
    data.save()
    return redirect('enquirylist')


class CreateEnquiry(CreateView):
    model = Enquiry
    form_class = EnquiryForm


class EnquieryList(generics.ListAPIView):

    queryset = Enquiry.objects.filter(claimed_by__isnull=True)
    serializer_class = EnquiryListSerializer
    permission_classes = [permissions.IsAuthenticated]


class EnquiryDetails(generics.RetrieveAPIView):
    queryset = Enquiry.objects.filter(claimed_by__isnull=True)
    serializer_class = EnquirySerializer
    permission_classes = [permissions.IsAuthenticated]


class UserClaimedEnquiries(ListView):
    model = Enquiry
    template_name = 'crmapp/user_enquiries.html'

    def get_queryset(self):
        try:
            self.data = User.objects.prefetch_related(
                'userenqueries').get(email__iexact=self.request.user.email)

        except Exception as e:
            print(e)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userenqueries'] = self.data

        return context

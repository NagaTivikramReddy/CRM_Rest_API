from django.urls import path
from .views import *


urlpatterns = [
    path('enquiry/', EnquieryList.as_view(), name='enquirylist'),
    path('enquiry/<int:pk>/', EnquiryDetails.as_view(), name='enquirydetails'),
    path('enquiry/<int:pk>/claim/', EnquiryClaim, name='claim'),
    path('my/enquires/', UserClaimedEnquiries.as_view(), name='userenquiries')

]

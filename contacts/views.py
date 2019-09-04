from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from django.contrib import messages
from myApp.models import Home
# emial
from django.core.mail import send_mail
# Create your views here.
def ContactView(request):
    if request.method == 'POST':
        property_name = request.POST['property_name']
        home_id = request.POST['home_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if the user has made an inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=home_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing.')
                return redirect('dashboard')

        contact = Contact.objects.create(
            listing = property_name, listing_id=home_id, name=name, email=email, phone=phone, message=message, user_id=user_id, 
        )
        contact.save()
        
        send_mail('Property Listing Enquiry',
            'There has been an enquiry for '+ property_name + ' .Sign in to Admin Panel for more info.',
            'rujan.tandukar@gmail.com',
            [realtor_email, 'ruzanshady@gmail.com'],
            fail_silently=False
        )

        messages.success(request, "Your enquiry is sent, a realtor will get back to you soon.")
        return redirect('dashboard')
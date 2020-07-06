from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Client, Lawyer, Service, Appointment
from django.contrib import messages
from django.views.generic import CreateView
from .forms import ClientSignUpForm, LawyerSignUpForm, UsernameUpdateForm, LawyerUpdateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .decorators import lawyer_required, client_required
from .filters import LawyerFilter


# Create your views here.


def homepageView (request):
    return render(request, 'law_app/TetaKenya Homepage.html')


@login_required
@client_required
def individuallawyerView (request, pk):
    advocate = Lawyer.objects.get(user_id=pk)
    services = Service.objects.filter(lawyer_id=pk)
    context = {'advocate': advocate, 'services': services}
    return render(request, 'law_app/individual lawyer account.html', context)


@login_required
@lawyer_required
def myprofileView (request):
    if request.method == 'POST':
        l_form = LawyerUpdateForm(request.POST, request.FILES, instance=request.user.lawyer)
        u_form = UsernameUpdateForm(request.POST, instance=request.user)
        if l_form.is_valid() and u_form.is_valid():
            l_form.save()
            u_form.save()
            messages.success(request, "Your profile has been updated successfully")
            return redirect('myprofile')
    else:
        l_form = LawyerUpdateForm(instance=request.user.lawyer)
        u_form = UsernameUpdateForm(instance=request.user)
    data = {'u_form': u_form, 'l_form': l_form}
    return render(request, 'law_app/Lawyer account.html', data)


def myservicesView(request):
    advocate = Lawyer.objects.get(user_id=request.user.lawyer)
    services = Service.objects.filter(lawyer_id=advocate)
    context = {'advocate': advocate, 'services': services}
    return render(request, 'law_app/My services.html', context)


@login_required
@lawyer_required
def addService (request):
    getlawyer = Lawyer.objects.get(user_id=request.user.lawyer)
    if request.method == "POST":
        # check if data is not empty
        if(request.POST.get('Service_Name') and
                request.POST.get('Service_Cost')):
            # if not empty grab the data
            s_name = request.POST.get('Service_Name')
            s_cost = request.POST.get('Service_Cost')
            # bind the data with model/table
            service = Service()
            service.lawyer = getlawyer
            service.Service_Name = s_name
            service.Service_Cost = s_cost
            # save the data
            service.save()
            messages.success(request, "Service uploaded")
            return redirect('myservices')
        else:
            messages.error(request, "Error! All fields are required")
        return redirect('myservices')
    else:
        return redirect('myservices')


@login_required
@lawyer_required
def updateServicesView(request, service_id):
    if request.method == "POST":
        # check if all fields have data
        if (request.POST.get('Service_Name') and
                request.POST.get('Service_Cost')):
            # update
            Service.objects.filter(id=service_id).update(
                Service_Name=request.POST.get('Service_Name'),
                Service_Cost=request.POST.get('Service_Cost')
            )
            messages.success(request, "service updated successfully")
            return redirect('myservices')
        else:
            messages.error(request, "Error updating the service")
            return redirect('myservices')
    else:
        redirect('myservices')


@login_required
@lawyer_required
def deleteServicesView(request, service_id):
    if request.method == "POST":
        Service.objects.filter(id=service_id).delete()
        # message here
        messages.warning(request, "service deleted!")
        return redirect('myservices')
    else:
        return redirect('myservices')


class client_register(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'registration/Client_SignUpForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('login')


class lawyer_register(CreateView):
    model = User
    form_class = LawyerSignUpForm
    template_name = 'registration/Lawyer_SignUpForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'lawyer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('login')


@login_required
@client_required
def displayLawyersView(request):
    lawyers_list = Lawyer.objects.all()
    myFilter = LawyerFilter(request.GET, queryset=lawyers_list)
    lawyers_list = myFilter.qs
    ## Pagination
    paginator = Paginator(lawyers_list, 3)
    page = request.GET.get('page')
    try:
        lawyers = paginator.page(page)
    except PageNotAnInteger:
        lawyers = paginator.page(1)
    except EmptyPage:
        lawyers = paginator.page(paginator.num_pages)
    dict = {'lawyers': lawyers, 'myFilter': myFilter}
    return render(request, 'law_app/Client account.html', dict)


def registerView(request):
    return render(request, 'law_app/register.html')


def bookView(request, service_id):
    getclient = Client.objects.get(user_id=request.user.client)
    bookedappointment = Appointment.objects.filter(service=service_id, client=getclient.user_id)
    if bookedappointment:
        messages.error(request, "You have already booked this appointment")
        return redirect('Homepage')
    else:
        newAppointment = Appointment()
        newAppointment.service_id = service_id
        newAppointment.client_id = getclient.user_id
        newAppointment.save()
        messages.success(request, "You have successfully booked your appointment. ")
        return redirect('Homepage')


@login_required
@client_required
def myappointmentsView(request):
    getclient = Client.objects.get(user_id=request.user.client)
    myappointments = Appointment.objects.filter(client=getclient.user_id)
    dict = {'myappointments': myappointments}
    return render(request, 'law_app/my appointments.html', dict)


@login_required
@lawyer_required
def appointmentsView(request):
    advocate = Lawyer.objects.get(user_id=request.user.lawyer)
    services = Service.objects.filter(lawyer_id=advocate)

    context = {'advocate': advocate, 'services': services}
    return render(request, 'law_app/Appointments.html', context)


@login_required
@lawyer_required
def maappointmentsView(request, service_id):
    services = Service.objects.filter(lawyer_id=request.user.lawyer)
    details = Appointment.objects.filter(service=service_id)
    context = {'details': details, 'services': services}
    return render(request, 'law_app/maappointments.html', context)

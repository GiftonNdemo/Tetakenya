from django.urls import path
from law import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepageView, name="Homepage"),
                # client account urls #
    path('clientaccount/', views.displayLawyersView, name='clientaccount'),
    path('individuallawyer/<int:pk>/', views.individuallawyerView, name='individuallawyer'),
    path('book/<int:service_id>/', views.bookView, name='book'),
    path('my_appointments/', views.myappointmentsView, name='appointments'),
                # lawyer account urls #
    path('lawyeraccount/', views.myprofileView, name='myprofile'),
    path('appointments/', views.appointmentsView, name='appointment'),
    path('Appointment/<int:service_id>/', views.maappointmentsView, name='Appointment'),
    path('myservices/', views.myservicesView, name='myservices'),
    path('addservice/', views.addService, name='addservice'),
    path('services/update/<int:service_id>', views.updateServicesView, name='update-service'),
    path('services/delete/<int:service_id>', views.deleteServicesView, name='delete-service'),
                        # register urls #
    path('register/', views.registerView, name='register'),
    path('client_register/', views.client_register.as_view(), name='client_register'),
    path('lawyer_register/', views.lawyer_register.as_view(), name='lawyer_register'),
                        # login urls #
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='law_app/TetaKenya homepage.html'), name='logout'),
                        # password reset urls #
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="law_app/password_reset.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="law_app/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="law_app/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="law_app/password_reset_done.html"), name='password_reset_complete')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

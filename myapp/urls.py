from django.contrib import admin
from django.contrib import auth
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from myapp.views import newcarpage
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'myapp_index'),
    path('base/', views.base, name = 'myapp_base'),
    path('login/', views.user_login, name = 'myapp_user_login'),
    path('signup/', views.user_signup, name = 'myapp_user_signup'),
    path('logout/', views.user_logout, name = 'myapp_user_logout'),
    path('listing/', views.listing, name = 'myapp_listing'),
    path('delete/<int:id>/', views.deletelisting, name = 'deletelist'),
    path('appointment/', views.appointment, name = 'myapp_appointment'),
    path('addappointment/', views.addappointment, name = 'myapp_addappointment'),
    #this is car products urls
    path('newcarpage/', views.newcarpage, name = 'myapp_newcarpage'),
    path('upcomingcar/', views.upcomingcarpage, name = 'myapp_upcomingcarpage'),
    path('listingcarpage/', views.listingcarpage, name = 'myapp_listingcarpage'),
    path('usedcarpage/', views.usedcarpage, name = 'myapp_usedcarpage'),
    #this is car detail urls
    path('newcardetail/<int:id>', views.newcardetailpage, name = 'myapp_newcardetailpage'),
    path('upcomingcardetail/<int:id>', views.upcomingcardetailpage, name = 'myapp_newcardetailpage'),
    path('usedcardetail/<int:id>', views.usedcardetailpage, name = 'myapp_newcardetailpage'),
    path('listingcardetail/<int:id>', views.listingcardetailpage, name = 'myapp_newcardetailpage'),
    #additional pages
    path('aboutus/', views.aboutus, name = 'aboutus'),
    path('team/', views.ourteam, name = 'team'),
    path('test/', views.testing, name = 'testing'),
    path('search1/', views.newcarsearch1, name = 'newcarsearch1'),
    path('search2/', views.newcarsearch2, name = 'newcarsearch2'),
    path('search3/', views.newcarsearch3, name = 'newcarsearch3'),
    path('search4/', views.newcarsearch4, name = 'newcarsearch4'),
    path('search5/', views.newcarsearch5, name = 'newcarsearch5'),
    path('search6/', views.newcarsearch6, name = 'newcarsearch6'),
    path('search7/', views.newcarsearch7, name = 'newcarsearch7'),
    path('search8/', views.newcarsearch8, name = 'newcarsearch8'),
    path('search9/', views.newcarsearch9, name = 'newcarsearch9'),
    path('search10/', views.newcarsearch10, name = 'newcarsearch10'),
    path('search11/', views.newcarsearch11, name = 'newcarsearch11'),
    path('search12/', views.newcarsearch12, name = 'newcarsearch12'),
    path('search/', views.searchfunc, name = 'searchfunc'),
    path('contactus/', views.contactuss, name = 'contactus'),
    path('testimonials/', views.testimonial, name = 'testimonial'),
    path('sellcar/', views.sellcar, name = 'sellcar'),
    path('buycar/', views.buycar, name = 'buycar'),
    path('predict/', views.predictprice, name = 'predictprice'),
    path('newsletter/', views.newsletter, name = 'newsletter'),
    path('addtestemonial/', views.addtestemonial, name = 'addtestemonial'),
    path('privacy/', views.privacys, name = 'privacys'),
    path('terms/', views.terms, name = 'terms'),
    #reset password
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="myapp/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="myapp/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="myapp/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="myapp/password_reset_done.html"), 
        name="password_reset_complete"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.welcome, name='welcome'),
    path('greetings/', views.greetings, name='greetings'),
    path('wishing/', views.wishing, name='wishing'),
    path('calculator/', views.calculator, name='calculator'),
    path('todo/', views.todo_list, name='todo'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employee/add/', views.employee_add, name='employee_add'),
    path('employee/edit/<int:emp_id>/', views.employee_edit, name='employee_edit'),
    path('employee/delete/<int:emp_id>/', views.employee_delete, name='employee_delete'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('shop.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='shop:product_list'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

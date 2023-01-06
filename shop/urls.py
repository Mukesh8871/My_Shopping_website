from	django.urls	import	path
from	.	import	views

app_name	=	'shop'
urlpatterns	=	[
		
        path('',	views.product_list,	name='product_list'),
	path('contact', views.contact, name="contact"),	
        
        path('<slug:category_slug>/',	views.product_list,name='product_list_by_category'),

	path('home',views.home, name='home'),	
        
        path('<int:id>/<slug:slug>/',	views.product_detail,name='product_detail'),
        
        path('signup', views.handelSignup,name="handelSignup"),
        path('login', views.handelLogin, name="handelLogin"),
        path('logout', views.handelLogout, name="handelLogout"),
]
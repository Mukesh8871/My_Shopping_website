from	django.shortcuts	import	render,	get_object_or_404, redirect
from	.models	import	Category,	Product
from	cart.forms	import	CartAddProductForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from shop.models import Contact
from django.contrib.auth.models import User

def contact(request):
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        contact = Contact(name=name, email=email, phone=phone, desc=desc)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
            messages.error(request, "Please Fill all details correctly")

            
        else:
            
            contact.save()
            messages.success(request, "Your Message has been Successfully send")
            return redirect('http://127.0.0.1:8000/')
    
    return render(request, 'shop/contact.htm')

def	product_list(request, category_slug=None):
	category	=	None
	categories	=	Category.objects.all()
	products	=	Product.objects.filter(available=True)
	if	category_slug:
		category	=	get_object_or_404(Category,slug=category_slug)
		products	=	products.filter(category=category)
	return	render(request,'shop/product/list.htm',{'category': category,'categories':	categories,'products':	products})
    

def	product_detail(request,	id,	slug):
	product	=	get_object_or_404(Product,	id=id,slug=slug, available=True)
	cart_product_form	=	CartAddProductForm()
	return	render(request,'shop/product/detail.htm',{'product': product,'cart_product_form': cart_product_form})

def home(request):
    return render(request, 'shop/product/list.htm')

def handelSignup(request):
    if request.method == "POST":

        # get the post peramiters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        #Checks for errorneous input
        if len(username) > 12:
            messages.error(request, "Username must be under 10 characters")
            return redirect('http://127.0.0.1:8000/')
        
        if not username.isalnum():
            messages.error(request, "Username should only cantain letters and numbers")
            return redirect('http://127.0.0.1:8000/')

        if password != cpassword:
            messages.error(request, "Password do not match")
            return redirect('http://127.0.0.1:8000/')
            
        #Create the user
        
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname        
        myuser.save()
        messages.success(request, "Your Study Fine account has been successfully created")
        return redirect('http://127.0.0.1:8000/')


    else:
        return HttpResponse("404 --not found")




def handelLogin(request):

    if request.method == "POST":

        # get the post peramiters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(request, username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('http://127.0.0.1:8000/')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('http://127.0.0.1:8000/') 
        

    return HttpResponse("404 --not found")
    
    
    
    
def handelLogout(request):
    
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('http://127.0.0.1:8000/')

    return HttpResponse('handelLogout')
    
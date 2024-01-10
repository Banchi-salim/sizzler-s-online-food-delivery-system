from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import Order

def staff_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('view_orders')
        else:
            form = AuthenticationForm()
            return render(request = request, template_name = "login.html", context={"form":form})

@login_required
def view_orders(request):
    orders = Order.objects.filter(order_status='New')
    return render(request, 'staff_dashboard.html', {'orders': orders})

@login_required
def process_order(request, pk):
    order = Order.objects.get(id=pk)
    order.order_status = 'Processing'
    order.save()
    return redirect('view_orders')

@login_required
def complete_order(request, pk):
    order = Order.objects.get(id=pk)
    order.order_status = 'Complete'
    order.save()
    return redirect('view_orders')

'''def order_processing(request, order_id):
    # Retrieve the order
    order = Order.objects.get(id=order_id)

    if request.method == 'POST':
        # Process the order (you can add your custom processing logic here)
        # For example, you can update the order status to 'completed'
        order.status = 'completed'
        order.save()
        return redirect('order_processing', order_id=order_id)

    context = {'order': order}
    return render(request, 'order_processing.html', context)'''
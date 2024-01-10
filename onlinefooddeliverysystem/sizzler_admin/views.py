from django.shortcuts import render
#from .models import Order


def orders(request):
    """completed_orders = Order.objects.filter(status='completed')
    pending_orders = Order.objects.filter(status='pending')

    return render(request, 'dashboard.html', {'completed_orders': completed_orders, 'pending_orders': pending_orders})"""

    return render(request, 'sizzler_admin/orders.html')

def adminhome(request):
    return render(request, 'sizzler_admin/adminhome.html')

def menu(request):
    return render(request, 'sizzler_admin/managemenu.html')
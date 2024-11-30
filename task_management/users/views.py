from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    # Redirect to the Google login process
    return redirect('social:begin', backend='google-oauth2')

@login_required
def dashboard(request):
    # Pass user information to the dashboard for display
    return render(request, 'dashboard.html', {'user': request.user})

def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')

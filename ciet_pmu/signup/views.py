from django.shortcuts import render
def signup(request):
    """
    Render the signup page.
    """
    return render(request, 'signup/signup.html')
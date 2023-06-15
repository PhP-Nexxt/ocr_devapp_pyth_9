from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from litreview_app.models import UserFollows





   
@login_required
def follows(request):
    myfollowers = UserFollows.objects.filter(user=request.user) #Mes abonnés (qui me suivent)
    myfollows = UserFollows.objects.filter(followed_user=request.user) #Les gens a qui je suis abonné
    
    
    

    context = {
        'section': 'dashboard',
        'myfollowers': myfollowers,
        'myfollows': myfollows,
    }
    
    return render(request, 'litreview_app/follows.html', context) 


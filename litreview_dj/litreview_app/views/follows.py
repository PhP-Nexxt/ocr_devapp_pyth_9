from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from litreview_app.models import UserFollows
from django.contrib.auth.models import User




   
@login_required
def follows(request):
    myfollowers = UserFollows.objects.filter(user=request.user) #Mes abonnés (qui me suivent)
    myfollows = UserFollows.objects.filter(followed_user=request.user) #Les gens a qui je suis abonné
    
    
    success = False
    error = False
    message = ""
    
    if request.method=="POST":
        username=request.POST.get("username")
        print(username)
        user = User.objects.filter(username=username).first()
        print(user)
        
        if user: 
            try:
                #creation de l'object
                userfollow = UserFollows(
                    user = user, #user gauche = champs du model & user droite = valeur ligne 19
                    followed_user = request.user #Idem Ici
                )
                userfollow.save() #Sauvegarde de l'objet
                success = True
                message = f"Vous etes désormais abonné à l'utilisateur {username}"
            except:
                error = True
                message = f"Vous etes déja abonné à l'utilisateur {username}"
        else:
            error = True
            message = f"L'utilisateur {username} n'existe pas"
    
    #Acceder aux variable dans le html
    context = {
        'section': 'dashboard',
        'myfollowers': myfollowers,
        'myfollows': myfollows,
        'success': success,
        'error': error,
        'message': message,
    }
    
    return render(request, 'litreview_app/follows.html', context) 


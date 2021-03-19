from django.shortcuts import render ,redirect

from banks.models import Banque , Client , Agent , Compte
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request,'pages/home.html')
    
def first_choice(request):
    return render(request,'pages_banks/first_choice.html')

def acceuil(request):
    return render(request,'pages/acceuil.html')

def creation_bank(request):
    if request.method == 'POST':
        statutMoral = request.POST.get('statutMoral')
        id_b = request.POST.get('id_b')
        email = request.POST.get('email')
        password = request.POST.get('password')
        number = request.POST.get('number')
        adress = request.POST.get('adress')
        
        bank_data = Banque(statut_moral = statutMoral ,email = email 
        , address = adress , numero = number , identifiant =id_b , password = password )
        

        bank_data.save()

        return render(request,'pages_banks/connexion_bank.html')   

    return render(request,'pages_banks/creation_bank.html')

def connexion_bank(request):
    if request.method == 'POST':
        email = request.POST.get('email')   
        password = request.POST.get('password')
        print(password)
        if Banque.objects.filter(email = email ):       
            if  Banque.objects.filter( password = password ):
                return render(request, 'pages_agents/connexion_agent.html' )
            else:
                print("code incorrect")
                return render(request, 'pages_banks/connexion_bank.html' )
        else:
            print("Email incorrect")
            return render(request, 'pages_banks/connexion_bank.html' )


    return render(request,'pages_banks/connexion_bank.html')

def bank_menu(request):
    return render(request,'pages_agents/bank_menu.html')

def gestion_client(request):
    return render(request,'pages_users/gestion_client.html')


def table_bank(request):
    data = Client.objects.all()
    context = {'data':data}
    return render(request,'pages_agents/table_bank.html',context)

def connexion_agent(request):
    if request.method == 'POST':
        email = request.POST.get('email')   
        password = request.POST.get('password')
        if Agent.objects.filter(email = email ):
            if  Agent.objects.filter( password = password ):
                return render(request, 'pages_agents/agent_menu.html' )
            else:
                print("code incorrect")
                return render(request, 'pages_agents/connexion_agent.html' )
        else:
            print("numéro incorrect")
            return render(request, 'pages_agents/connexion_agent.html' )
    return render(request,'pages_agents/connexion_agent.html')



def inscription_agents(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        number = request.POST.get('number')
        adress = request.POST.get('adress')
        idA = request.POST.get('idA')
 
        agent_data = Agent(nom= name , prenom = lastname ,email = email 
        ,password = password , address = adress , numero = number ,identifiant=idA  )
        agent_data.save()

        return render(request,'pages_agents/connexion_agent.html')   
    return render(request,'pages_agents/inscription_agents.html')

def inscription_users(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        number = request.POST.get('number')
        adress = request.POST.get('adress')
        identifiant = request.POST.get('identifiant')
        montant = request.POST.get('montant')
        compte = request.POST.get('compte')
        
        print(request.POST)
 
        users_data = Client(nom= name , prenom = lastname ,email = email 
        ,password = password , address = adress , numero = number ,identifiant=identifiant ,compte=compte ,montant = montant ,)
        users_data.save()

        return render(request,'pages_users/connexion_users.html')   
    return render(request,'pages_agents/inscription_users.html')



def connexion_users(request):
    if request.method == 'POST':
        print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
        print(request.POST)
        email = request.POST.get('email')   
        password = request.POST.get('password')
        print(email)
        print(password)
        if Client.objects.filter(email = email ):
            if  Client.objects.filter( password = password ):
                return render(request, 'pages_users/gestion_client.html' )
            else:
                print("code incorrect")
                return render(request, 'pages_users/connexion_users.html' )
        else:
            print("numéro incorrect")
            return render(request, 'pages_users/connexion_users.html' )
    return render(request,'pages_users/connexion_users.html')



def menu_users(request):
    return render(request,'pages_users/menu_users.html')


def depot(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        montant = request.POST.get('montant')
        if int(montant) > 0 :
           
            if  Client.objects.filter(email = email).exists():
                solde = Client.objects.get(email = email)
                solde.montant = solde.montant + int(montant)
                solde.save()
                print('Depot effectué')
                return  render(request,'pages_users/gestion_client.html')
            else:
                print('Email n\'existe pas')
        else:
            print('Erreur de dépot')
            return  render(request,'pages_users/gestion_client.html')
    else:
        return render(request,'pages_users/gestion_client.html')

def retrait(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        montant = request.POST.get('montant')
        if int(montant) > 0 :
            if  Client.objects.filter(email = email).exists():
                solde = Client.objects.get(email = email)
                solde.montant = solde.montant - int(montant)
                if( solde.montant > -10000):
                    solde.save()
                    print( ' Retrait effectué effectué')
                    return  render(request,'pages_users/gestion_client.html')
                else:
                    print('Ce débit ne peut être effectuer')
                    return  render(request,'pages_users/gestion_client.html')
            else:
                print('Email n\'existe pas')
                return  render(request,'pages_users/gestion_client.html')
        else:
            print('Erreur de dépot')
            return  render(request,'pages_users/gestion_client.html')
    else:
        return render(request,'pages_users/gestion_client.html')


def transfert(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        montant = request.POST.get('montant')
        email1 = request.POST.get('email1')
        if int(montant) > 0 :
            if  Client.objects.filter(email = email).exists():
                solde = Client.objects.get(email = email1)
                solde.montant = solde.montant + int(montant)
                solde.save()
                print('Transfert effectué')
                return  render(request,'pages_users/gestion_client.html')
            else:
                print('Email n\'existe pas')
                return  render(request,'pages_users/gestion_client.html')
        else:
            print('Erreur de transfert')
            return  render(request,'pages_users/gestion_client.html')
    else:
        return render(request,'pages_users/gestion_client.html')


def suppression_users(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if  Client.objects.filter(email = email).exists():
            solde = Client.objects.get(email = email)
            solde.delete()
            print(' Compte supprimer')
            render(request,'pages_users/suppression_users.html')
        else:
            print('Erreur de suppression')
            return  render(request,'pages_users/suppression_users.html')
    else:
        return render(request,'pages_users/suppression_users.html')
   


def agent_menu(request):
    return render(request,'pages_agents/agent_menu.html')

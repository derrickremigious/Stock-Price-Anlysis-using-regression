from django.shortcuts import render
from django.shortcuts import render, redirect
from . forms import  UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
import numpy as np
import joblib
import base64
from io import BytesIO
import seaborn as sns
from .models import Tcs,Accenture
import matplotlib.pyplot as plt



def Landing_1(request):
    return render(request, 'Landing_1.html')

def Home_4(request):
    return render(request,'Home_4.html')

def Tcs_Report(request):
    return render(request, 'TCS.html')

def Domain(request):
    return render(request, 'Domain.html')

def Accenture_Report(request):
    return render(request, 'Accenture.html')




def Login_2(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home_4')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'Login_2.html', context)
    
   
def Register_3(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was successfully created for {user}')
            return redirect('Login_2')
    else:
        form = UserRegisterForm()
    
    context = {'form': form}
    return render(request, 'Register_3.html', context)



Model1 = joblib.load('D:/PROJECTS/TESTING/ITPML13 DONE/ITPML13-FINAL CODING/DEPLOYMENT/Project/App/Accenture.pkl')  

def Deploy_8(request):
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]  # Skip the first value which might be CSRF token or similar

        a = []
        for i in int_features:
            try:
                a.append(int(i))
            except ValueError:
                # Handle the error or skip the value
                print(f"ValueError: Cannot convert {i} to int")
                return render(request, 'Deploy_8.html', {"prediction_text": f"Invalid input: {i} is not a number"})

        final_features = [np.array(a, dtype=object)]
        print(final_features)
        prediction = Model1.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(output)
        a.append(output)
        print(a)

        # Save the prediction to the database
        Accenture.objects.create(
            open_price=a[0],
            high_price=a[1],
            low_price=a[2],
            volume=a[3],
            closing_price=output
        )

        categories = ['Open', 'High', 'Low', 'Volume', 'close']
        plt.figure(figsize=(8, 6))
        sns.lineplot(x=categories, y=a, marker='o', color='red')

        plt.xlabel('Categories')
        plt.ylabel('Values')
        plt.title(f"['Open', 'High', 'Low', 'Volume', 'close'] : {a}")

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        plot_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        context = {'plot_base64': plot_base64}

        return render(request, 'Acc_output.html', {"prediction_text": f'THE ACCENTURE STOCK CLOSING PRICE IS {output}', 'plot_base64': plot_base64})

    else:
        return render(request, 'Deploy_8.html')
    


Model2 = joblib.load('D:/PROJECTS/TESTING/ITPML13 DONE/ITPML13-FINAL CODING/DEPLOYMENT/Project/App/TCS1.pkl')  
  
def Deploy_9(request):
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        print(int_features)
        a = []
        for i in int_features:
            a.append(int(i))
        print(a)
        final_features = [np.array(a, dtype=object)]  # Change int_features to a
        print(final_features)
        prediction = Model2.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(output)
        a.append(output)
        print(a)

        # Save the prediction to the database
        Tcs.objects.create(
            open_price=a[0],
            high_price=a[1],
            low_price=a[2],
            volume=a[3],
            closing_price=output
        )

        categories = ['Open', 'High', 'Low', 'Volume', 'close']
        plt.figure(figsize=(8, 6))
        sns.lineplot(x=categories, y=a, marker='o', color='red')

        plt.xlabel('Categories')
        plt.ylabel('Values')
        plt.title(f"['Open', 'High', 'Low', 'Volume', 'close'] : {a}")

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        plot_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        context = {'plot_base64': plot_base64}

        return render(request, 'tcs_output.html', {"prediction_text": f'THE TCS STOCK CLOSING PRICE IS {output}', 'plot_base64': plot_base64})

    else:
        return render(request, 'Deploy_9.html')
    


def show_tcs_predictions(request):
    predictions = Tcs.objects.all()
    return render(request, 'DB_Tcs.html', {'predictions': predictions})

def show_accenture_predictions(request):
    predictions = Accenture.objects.all()
    return render(request, 'DB_Accenture.html', {'predictions': predictions})
    
def logout(request):
    auth_logout(request)
    return redirect('Login_2')


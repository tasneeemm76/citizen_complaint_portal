from django.shortcuts import render, redirect
from .models import register

def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        name = request.POST.get('name')  
        password1 = request.POST.get('password1')  
        password2 = request.POST.get('password2')  
        #user_type = request.POST.get('user_type')  
        code_word=request.POST.get('cw')
        aadhar = request.POST.get('aadhar')  
        email = request.POST.get('email')  
        phone = request.POST.get('phone')  
        gender = request.POST.get('gender')  
        dob = request.POST.get('dob')  
        address=request.POST.get('address')
        pin=request.POST.get('pin')
   

        if password1 != password2:
            return render(request, 'register.html', {'error': 'Passwords do not match !'})

        if len(phone) != 10 or not phone.isdigit():
            return render(request, 'register.html', {'error': 'Invalid phone number'})


        new_register = register(username=username, password=password1, name=name,code_word=code_word,aadhar=aadhar, email=email, phone=phone, gender=gender,dob=dob,address=address,pin=pin)
        new_register.save()

        return redirect('login')  
    else:
        return render(request, 'register.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if username and password combination exists in the database
        if register.objects.filter(username=username, password=password).exists():
            request.session['username'] = username
            return redirect('index_with_username', username=username)
        else:
            # Redirect to sign-in page if login credentials are invalid
            return redirect('index')
    
    # Render the login form template for GET requests
    return render(request, 'login.html')





def index(request):
    return render(request, 'index.html')

def emergency(request):
    return render(request, 'emergency_services.html')


def services(request):
    return render(request, 'services.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ReportedIssue
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Use this only if you have issues with CSRF; otherwise, it's better to use CSRF protection.
def report_issue(request):
    if request.method == 'POST':
        # Get the data from the form
        issue_type = request.POST.get('issue_type')
        issue_description = request.POST.get('issue_description', '')
        area_name = request.POST.get('area_name')
        pincode = request.POST.get('pincode')

        # Create a new reported issue entry in the database
        reported_issue = ReportedIssue(
            issue_type=issue_type,
            issue_description=issue_description,
            area_name=area_name,
            pincode=pincode
        )
        reported_issue.save()

        # Redirect to a success page or back to the form
        return redirect('index')  

    # If it's a GET request, render the reporting form
    return render(request, 'feeback.html')  # Replace with your form template name.

from django.shortcuts import render
from .models import ReportedIssue

def heatmap_view(request):
    reported_issues = ReportedIssue.objects.all()
    data = []

    for issue in reported_issues:
        if issue.latitude and issue.longitude:
            data.append([issue.latitude, issue.longitude])

    context = {'grievance_data': data}
    return render(request, 'heatmap.html', context)

from django.shortcuts import render
from django.db.models import Count
from .models import ReportedIssue

def admin_dashboard(request):
    # Query to get the grievance types and their counts
    pie_chart_data = ReportedIssue.objects.values('issue_type').annotate(count=Count('issue_type'))

    # Structure the data for the pie chart
    pie_chart_labels = [item['issue_type'] for item in pie_chart_data]
    pie_chart_values = [item['count'] for item in pie_chart_data]

    # Query to get subcategories and their counts, filtered by issue type
    bar_chart_data = ReportedIssue.objects.values('issue_subtype').annotate(count=Count('issue_subtype'))

    # Structure the data for the bar chart
    bar_chart_labels = [item['issue_subtype'] for item in bar_chart_data]
    bar_chart_values = [item['count'] for item in bar_chart_data]

    # Create the data to be passed to the template
    context = {
        'pie_chart_data': {
            'labels': pie_chart_labels,
            'data': pie_chart_values
        },
        'bar_chart_data': {
            'labels': bar_chart_labels,
            'data': bar_chart_values
        }
    }

    return render(request, 'dashboard.html', context)


def search_by_area(request):
    # Get all unique districts from the ReportedIssue model
    area_name = ReportedIssue.objects.values_list('area_name', flat=True).distinct()
    
    issues = []
    issue_type_labels = []
    issue_type_counts = []
    issue_subtype_labels = []
    issue_subtype_counts = []
    
    if request.method == 'POST':
        selected_district = request.POST.get('area_name')
        
        # Get the issues for the selected district
        if selected_district:
            issues = ReportedIssue.objects.filter(area_name=selected_district)
            
            # Get the distribution of issue types
            issue_type_data = (
                issues.values('issue_type')
                .annotate(count=Count('issue_type'))
                .order_by('issue_type')
            )
            
            # Prepare issue type data for Chart.js
            issue_type_labels = [item['issue_type'] for item in issue_type_data]
            issue_type_counts = [item['count'] for item in issue_type_data]
            
            # Get the distribution of issue subtypes
            issue_subtype_data = (
                issues.values('issue_subtype')
                .annotate(count=Count('issue_subtype'))
                .order_by('issue_subtype')
            )
            
            # Prepare issue subtype data for Chart.js
            issue_subtype_labels = [item['issue_subtype'] for item in issue_subtype_data]
            issue_subtype_counts = [item['count'] for item in issue_subtype_data]
    
    context = {
        'area_name': area_name,
        'issues': issues,
        'issue_type_labels': issue_type_labels,
        'issue_type_counts': issue_type_counts,
        'issue_subtype_labels': issue_subtype_labels,
        'issue_subtype_counts': issue_subtype_counts
    }
    
    return render(request, 'search_by_area.html', context)
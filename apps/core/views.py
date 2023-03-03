from django.shortcuts import render
import requests
import pygal
from .models import DashboardPanel

# Two example views. Change or delete as necessary.
def home(request):

    dboard_panels = DashboardPanel.objects.all()
    context = {
    "all_panels": dboard_panels,
    }
    return render(request, "pages/home.html", context)

def about(request):
    response = requests.get('https://api.github.com/users/phil1sf/repos')
    repos = response.json()
    chart = pygal.Pie()
    for repo_dict in repos:
        value = repo_dict ["size"]
        label = repo_dict["name"]
        chart.add(label, value)
        
    
    chart_svg_as_datauri = chart.render_data_uri()
    context = {
        "rendered_chart_svg_as_datauri": chart_svg_as_datauri,    
        'github_repos': repos,
        
              }

    return render(request, 'pages/about.html', context)
    
def panel_details(request, panel_id):
    panel = DashboardPanel.objects.get(id=panel_id)
    chart = pygal.Pie()
    # TODO: Make aspects of the chart (such as Pie vs Bar, styling, etc)
    # customizable based on the data in the panel model
    # TODO: Get data from API, file, DB, or somewhere else, possibly based on
    # the panel model
    #for repo_dict in repo_list:
    #value = 42 # TODO: Replace this...
    #label = repo_dict["name"]
    #chart.add(label, value)
    context = {
    "panel": panel,
    "rendered_chart_svg": chart.render(),
    }
    return render(request, "pages/panel_details.html", context)    
        

    


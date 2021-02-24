from django.shortcuts import render, redirect
from restful_tv_app.models import Network, TV_Show

def index(request):
    return redirect("/shows")

# ------------ All Shows Display --------------------

def shows(request):
    context = {
        "shows": TV_Show.objects.all()
    }
    return render(request, "shows.html", context)

# ------------ Specific Show Display --------------------

def show_view(request, id):
    this_show = TV_Show.objects.get(id = id)
    context = {
        "show": this_show
    }
    return render(request, "show_view.html", context)

# ------------ Create Show --------------------

def new_show(request):
    context = {
        "networks": Network.objects.all()
    }
    return render(request, "new_show.html", context)

def create_show(request):
    new_show = TV_Show.objects.create(
        title = request.POST['add_title'],
        release_date = request.POST['add_release_date'],
        desc = request.POST['add_desc']
    )
    if len(request.POST['add_new_network']) <= 0:
        new_show.networks.add(Network.objects.get(id = request.POST['add_network'])),
    else:
        new_show.networks.add(create_network(request)),
    show_id = new_show.id
    return redirect(f"/shows/{show_id}")

# ------------ Edit Shows --------------------

def edit_show(request, id):
    this_show = TV_Show.objects.get(id = id)
    context = {
        "show": this_show,
        "networks": Network.objects.exclude(shows=id),
        "all_networks": Network.objects.all()
    }
    return render(request, "edit_show.html", context)

def update_show(request, id):
    this_show = TV_Show.objects.get(id = id)
    this_show.title = request.POST['update_title']
    this_show.release_date = request.POST['update_release_date']
    this_show.desc = request.POST['update_desc']

    if len(request.POST['add_new_network']) <= 0:
        this_show.networks.add(Network.objects.get(id = request.POST['update_network'])),
    else:
        this_show.networks.add(create_network(request)),

    show_id = this_show.id

    this_show.save()
    show_id = this_show.id
    return redirect(f"/shows/{show_id}")

def show_remove_network(request, show_id, net_id):
    this_show = TV_Show.objects.get(id = show_id)
    this_show.networks.remove(Network.objects.get(id = net_id))
    return redirect("/shows")

def delete_show(request, id):
    TV_Show.objects.get(id = id).delete()
    return redirect("/shows")



#-------------------- Newtorks -------------------------

def create_network(request):
    new_network = Network.objects.create(
        name = request.POST['add_new_network']
    )
    return(new_network)

def view_networks(request):
    context = {
        "networks": Network.objects.all()
    }
    return render(request, "network_view.html", context)

def delete_network(request, net_id):
    Network.objects.get(id = net_id).delete()
    return redirect('/networks')

#-------------------- End Newtorks-------------------------
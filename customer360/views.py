from django.shortcuts import render
from datetime import date, timedelta
from django.db.models import Count
from .models import Customer, Interaction

def index(request):
    customers = Customer.objects.all()
    context = {"customers":customers}
    return render(request,"index.html",context=context)

def create_customer(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        social_media = request.POST["socialMedia"]
        customer = Customer.objects.create(name=name,email=email,phone=phone,address=address,social_media=social_media)
        customer.save()
        msg = "Successfully Saved a Customer"
        return render(request,"add.html",context={"msg":msg})
    return render(request,"add.html")

def summary(request):
    thirty_days_ago = date.today() - timedelta(days=30)
    interactions = Interaction.objects.filter(interaction_date__gte=thirty_days_ago)

    count = len(interactions)
    interactions = interactions.values("channel","direction").annotate(count=Count('channel'))
    
    channel_map = dict(Interaction.CHANNEL_CHOICES)
    direction_map = dict(Interaction.DIRECTION_CHOICES)
    
    context={
                "interactions":[
                    {
                        **item,
                        "channel_display": channel_map.get(item["channel"]),
                        "direction_display": direction_map.get(item["direction"]),
                    }
                    for item in interactions
                ],
                "count":count
             }

    return render(request,"summary.html",context=context)

def interact(request,cid):
    channels = Interaction.CHANNEL_CHOICES
    directions = Interaction.DIRECTION_CHOICES
    context = {"channels":channels,"directions":directions}

    if request.method == "POST":
        customer = Customer.objects.get(id=cid)
        channel = request.POST["channel"]
        direction = request.POST["direction"]
        summary = request.POST["summary"]
        interaction = Interaction.objects.create(
                                    customer=customer,
                                    channel=channel,
                                    direction=direction,
                                    summary=summary)
        interaction.save()
        context["msg"] = "Interaction Success"
        return render(request,"interact.html",context=context)
    return render(request,"interact.html",context=context)

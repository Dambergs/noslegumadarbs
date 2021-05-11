from django.shortcuts import render
from django.http import HttpResponse
from deposits.models import Deposit


def index(request):

    deposits = Deposit.objects.all()

    context = {
        'deposits': deposits,
    }

    return render(
        template_name='all.html',
        request=request,
        context=context,
    )


#def interest(k, i, n):
    #return k(1+float(i))**n


def new_deposit_view(request):

    if request.method == 'POST':
        newdeposit = Deposit(
            deposit=request.POST['deposit'],
            term=request.POST['term'],
            rate=request.POST['rate'],
            interest=request.POST['rate'],
            #interest=interest(request.POST['deposit'], request.POST['rate'], request.POST['term'])
        )

        newdeposit.save()

        deposits = Deposit.objects.all()

        context = {
            'deposits': deposits,
        }

        return render(
            template_name='all.html',
            request=request,
            context=context,
        )

    return render(
        template_name='new.html',
        request=request,
    )


def get_deposit(request, dep_id):

    deposit = Deposit.objects.get(id=dep_id)

    context = {
        'deposit': deposit,
    }

    return render(
        template_name='deposit.html',
        request=request,
        context=context,
    )
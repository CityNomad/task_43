from django.shortcuts import render

# Create your views here.

def form_view(request):
    if request.method == "GET":
        return render(request, "form.html")
    else:
        context = {
            "first_num": int(request.POST.get("first_num")),
            "second_num": int(request.POST.get("second_num")),
            "action_type": request.POST.get("action_type"),
        }

        if context['action_type'] == 'add':
            result = context['first_num'] + context['second_num']
            context['result'] = result
            return render(request, "form.html", context)
        elif context['action_type'] == 'substract':
            result = context['first_num'] - context['second_num']
            context['result'] = result
            return render(request, "form.html", context)
        elif context['action_type'] == 'multiply':
            result = context['first_num'] * context['second_num']
            context['result'] = result
            return render(request, "form.html", context)
        else:
            result = context['first_num'] / context['second_num']
            context['result'] = result
            return render(request, "form.html", context)


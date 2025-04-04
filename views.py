from django.shortcuts import render
from django.http import JsonResponse
from .forms import MedicalInfoForm

def chat_view(request):
    if request.method == "POST":
        form = MedicalInfoForm(request.POST)
        if form.is_valid():
            form.save()
            data = {"message": "Your information has been saved successfully."}
            return JsonResponse(data)
        else:
            # Return form errors as JSON if validation fails
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        form = MedicalInfoForm()
        return render(request, "chatbot/chat.html", {"form": form})

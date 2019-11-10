from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from app.form import formVal
from app.validator import main


class index(TemplateView):
    template_name = 'index.html'

    def get(self,request):
        form = formVal()
        return render(request,self.template_name,{'form':form})

    def post(self, request):
        form = formVal(request.POST)
        if form.is_valid( ):
            text = form.cleaned_data['string']
            #form = formVal()
            validacion = main(text)
        args = {'form': form, 'validacion':validacion}
        return render(request, self.template_name, args)





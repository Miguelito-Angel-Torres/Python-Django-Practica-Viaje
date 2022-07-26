from django.shortcuts import render,redirect

from .forms import  FormularioContacto

#Importacion gmail
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContacto()
    

    #Si se ha echo Post rescateme la informacion del formulario_contacto

    if request.method=="POST":
        #Recascatar la informacion qhe hubo en el formulario:
        #Pasar por parametros los datos
        formulario_contacto=FormularioContacto(data=request.POST)
        #Si se ha rellenado todo los campos :
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            apellido = request.POST.get("apellido")
            email= request.POST.get("email")
            contenido = request.POST.get("contenido")


            email = EmailMessage("Mensaje de la App",
            "El usuario con nombre: {} y apellido: {} con la direccion {} escribe lo sgt:\n\n {}".format(nombre,apellido,email,contenido),
            "",["mallquitorres1234@gmail.com"],reply_to=[email])

            try:
                email.send()
            
            # Es como decir cambia la directiva 
            #Pasando como parametro     
                return redirect("/contacto/?valido")
            except:

                return redirect("/contacto/?novalido")



    return render(request,"contacto/contacto.html",{'miFormulario':formulario_contacto})
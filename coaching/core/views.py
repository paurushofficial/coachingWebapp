from django.shortcuts import render, HttpResponse
from . models import subject, student
from reportlab.pdfgen import canvas
from django.http import FileResponse


def home(request):
    return render(request, 'index.html')

def courses(request):
    courses=subject.objects.all()

    return render(request, 'courses.html', {'courses': courses})

def form(request):
    subjects = subject.objects.all()

    return render(request, 'form.html', {'subjects': subjects})

def downloadForm(request):
    pdfname = request.POST['download']
    form = open("forms/"+pdfname, 'rb')
    return FileResponse(form)

def submitform(request):
    name = request.POST['name']
    father = request.POST['fathersName']
    address = request.POST['address']
    contact = request.POST['contact']
    admissionclass = request.POST['admissionClass']
    subject1 = request.POST['subject1']
    subject2 = request.POST['subject2']
    subject3 = request.POST['subject3']
    subject4 = request.POST['subject4']
    subject5 = request.POST['subject5']
    try:
        email = request.POST['email']
    except:
        email = 'Not Available'
    try:
        aadhar = request.POST['aadharNumber']
    except:
        aadhar = 'Not Available' 

    Acceptedform = student(name=name, fathersName=father, address=address, contact=contact,admissionClass=admissionclass, subject1=subject1,subject2=subject2, subject3=subject3, subject4=subject4, subject5=subject5, aadhar=aadhar, email=email)
    Acceptedform.save()


    def printField(field, Y_axis, X_axis):
        pdf.setFontSize(17)
        pdf.drawString(Y_axis,X_axis,field)
        pdf.setFontSize(20)

    def printForm(student):
        global pdf, pdfName
        pdfName = student.name+student.aadhar[0:4]+".pdf" 
        pdf= canvas.Canvas("forms/"+pdfName)
        pdf.setTitle(student.name+"-Admission Form")
        pdf.line(30,815,565,815)
        pdf.line(30,30,565,30)
        pdf.line(30,815,30,30)
        pdf.line(565,815,565,30)

        pdf.setFont("Helvetica-Bold",38)
        pdf.setFillColorRGB(1,0.5,0.5)

        pdf.drawString(85, 777,"Ankit Coaching Institute")
        pdf.setFont("Helvetica",18)
        pdf.drawString(196,753, "Galibpur, Bhiti, Mau, 275101")
        pdf.line(30,748,565,748)
        pdf.setFont("Helvetica-Bold",25)
        pdf.setFillColorRGB(0,0,0)
        pdf.drawString(215,720,"Admission Form")
        logo="passportphoto.PNG"
        pdf.drawInlineImage(logo,450,590)
        pdf.setFont("Courier",20)
        
        pdf.drawString(50,680,"Name:____________________________")
        printField(student.name,120, 680)
        
        pdf.drawString(50,655,"Admission Class:_________________")
        printField(student.admissionClass,250, 655)
        
        pdf.drawString(50,630,"Subject 1:_______________________")
        printField(student.subject1,180,630)
        
        pdf.drawString(50,605,"Subject 2:_______________________")
        printField(student.subject2,180,605)
        
        pdf.drawString(50,580,"Subject 3:_______________________")
        printField(student.subject3,180,580)
        
        pdf.drawString(50,555,"Subject 4:_______________________")
        printField(student.subject4,180,555)
        
        pdf.drawString(50,530,"Subject 5:_______________________")
        printField(student.subject5,180,530)
        
        pdf.drawString(50,505,"Aadhar Number:____________________________")
        printField(student.aadhar, 220, 505)
        
        pdf.drawString(50,480,"Contact No.:______________________________")
        printField(student.contact, 200, 480)
        
        pdf.drawString(50,455,"E-Mail ID:________________________________")
        printField(student.email, 180, 455)
        
        pdf.drawString(50,430,"Father's Name:____________________________")
        printField(student.fathersName, 220, 430)
        
        pdf.drawString(50,405,"Correspondence Address:___________________")
        try:
            printField(student.address[:22],328,405)
            printField(student.address[22:],50,380)
        except:
            printField(student.address,328,405)
        
        pdf.drawString(50,380,"__________________________________________")
        pdf.setFontSize(12)
        pdf.drawString(50,280,"Date:")
        pdf.drawString(100,280,"______________")
        pdf.drawString(50,260,"Place:")
        pdf.drawString(110,260,"__________________")

        pdf.drawString(45,205,"Student's Signature")
        pdf.drawString(215,205,"Guardian's Signature")
        pdf.drawString(390,205,"Director's Signature")

        pdf.line(30,200,565,200)

        pdf.setFontSize(20)
        pdf.drawString(50,175,"NOTE:")
        pdf.setFontSize(14)
        pdf.drawString(50,150,"1: Attach 4 copies of your passport photo with the Form.")
        pdf.drawString(50,125,"2: Form will be only accepted if all above signatures are")
        pdf.drawString(50,100,"   present.")
        pdf.drawString(50,75,"3: Terms and Condtions Applied.")
        pdf.save()
    
    printForm(Acceptedform)
    
    return render(request, 'formSubmitted.html', {'Student': Acceptedform.name, 'pdfName': pdfName})

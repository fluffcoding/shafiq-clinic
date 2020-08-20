from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import PatientForm, DiseaseForm, PatientDiseaseForm, MedicineIntakeForm, MedicineForm
from .models import Patient, Disease, Medicine, MedicineIntake




def create_patient(request):
    if request.method == 'POST':
        if 'add_disease' in request.POST:
            disease_form = DiseaseForm(request.POST, prefix='disease')
            if disease_form.is_valid():
                disease_form.save()
            patient_form = PatientForm(prefix='patient')
        elif 'add_patient' in request.POST:
            patient_form = PatientForm(request.POST, prefix='patient')
            if patient_form.is_valid():
                patient_form.save() 
            disease_form = DiseaseForm(prefix='disease')
    else:
        disease_form = DiseaseForm(prefix='disease')
        patient_form = PatientForm(prefix='patient')
    patients = Patient.objects.all()
    diseases = Disease.objects.all()
    objects = list( Patient.objects.all())
    objects.reverse()
    final = objects[:3]
    context = {
        'patient_form': patient_form,
        'patients':patients,
        'disease_form':disease_form,
        'diseases': diseases,
        'final': final,
    }
    return render(request, 'create_patient.html', context)


def patient_detail(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        if 'delete' in request.POST:
            remove_medicine = MedicineIntake.objects.get(id=request.POST['id'])
            patient.prescription.remove(remove_medicine)
            form = MedicineIntakeForm()
        #elif 'disease' in request.POST:
            #disease = PatientDiseaseForm(request.POST or None)
            #if disease.is_valid():
                #patient.disease.add(disease)
                #print(disease)
                #print(request.POST)
            #form = MedicineIntakeForm()
        else:
            form = MedicineIntakeForm(request.POST or None)
            if form.is_valid():
                obj = MedicineIntake(**form.cleaned_data)
                obj.save()
                patient.prescription.add(obj)
                '''for disease in form.cleaned_data['disease']:
                    patient.disease.add(disease.id)'''
    else:
        form = MedicineIntakeForm()

    '''
    if request.method == 'POST':
        if 'delete' in request.POST:
            delete_disease = Disease.objects.get(id=request.POST['id'])
            print(delete_disease)
            if disease_form.is_valid():
                disease_form.save()
            patient_form = PatientForm(prefix='patient')
        elif 'add_patient' in request.POST:
            patient_form = PatientForm(request.POST, prefix='patient')
            if patient_form.is_valid():
                patient_form.save() 
            disease_form = DiseaseForm(prefix='disease')
    else:
        disease_form = DiseaseForm(prefix='disease')
        patient_form = PatientForm(prefix='patient')
    
    form = PatientDiseaseForm(request.POST or None)
    if form.is_valid():
        for disease in form.cleaned_data['disease']:
            patient.disease.add(disease.id)
    print(request.POST)
    '''
    context = {
        'patient': patient,
        'form': form,
        
    }
    return render(request, 'patient_detail.html', context)


def patient_report(request, id):
    patient = Patient.objects.get(id=id)
    context = {
        'patient': patient,
    }
    return render(request, 'patient_report.html', context)


def all_patients(request):
    patients = Patient.objects.all()
    context = {
        'patients': patients,
    }
    return render(request, 'patients_list.html', context)


def search(request):
    if request.method == 'GET':     
        patient_search =  request.GET.get('search')    
        patient = get_object_or_404(Patient, id=patient_search)
        
    context = {
        "patient":patient,
    }
    return render(request,"search.html", context)
    

def create_medicine(request):
    medicines = Medicine.objects.all()
    form = MedicineForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
        'medicines': medicines,
    }
    return render(request, 'create_medicine.html', context)


def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('/patient/all/')


def add_disease(request,id):
    patient = Patient.objects.get(id=id)
    form = PatientDiseaseForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        for disease in form.cleaned_data['disease']:
            patient.disease.add(disease)


    context = {
        'patient': patient,
        'form': form,
    }
    return render(request, 'disease.html', context)
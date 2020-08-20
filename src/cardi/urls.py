from django.contrib import admin
from django.urls import path
from patient.views import (create_patient,
                            patient_detail, 
                            patient_report, 
                            all_patients, 
                            search, 
                            create_medicine, 
                            delete_patient,
                            add_disease,
                            )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patient/create/', create_patient, name='patient-create'),
    path('patient/detail/<id>', patient_detail, name='patient-detail'),
    path('patient/report/<id>', patient_report, name='patient-report'),
    path('patient/all/', all_patients, name='all-patients'),
    path('patient/search/', search, name='search'),
    path('medicine/create/', create_medicine, name='create-medicine'),
    path('patient/delete/<id>', delete_patient, name='delete-patient'),
    path('patient/disease/<id>', add_disease, name="add-disease")
]

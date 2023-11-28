"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Import here Domain Class that are needed for ORM
# orders DB
from t08_flask_mysql.app.my_project.auth.domain.orders.client import Client
from t08_flask_mysql.app.my_project.auth.domain.orders.client_type import ClientType

"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.doctor import Doctor
from .orders.diagnoses import Diagnoses
from .orders.patients import Patients
from .orders.appointments import Appointments
from .orders.appointment_records import Appointment_records
from .orders.consultation_cost import Consultation_cost
from .orders.doctor_schedules import Doctor_schedules
from .orders.treatment_protocols import Treatment_protocols


doctor = Doctor()
diagnoses = Diagnoses()
patients = Patients()
appointments = Appointments()
appointment_records = Appointment_records()
consultation_cost = Consultation_cost()
doctor_schedules = Doctor_schedules()
treatment_protocols = Treatment_protocols()


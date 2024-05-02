from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import CustomUser, TimeSlot, Teachers, Barcode
from django.urls import reverse
from .models import TimeSlot
from django.shortcuts import render
import cv2
from .utils import create_dynamic_table
from .utils import create_dynamic_table
from pyzbar.pyzbar import decode
import time
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import CustomUser
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render
from pyzbar import pyzbar
import cv2
from datetime import datetime
from time import gmtime, strftime
import cv2
from datetime import datetime
from pyzbar import pyzbar
from django.shortcuts import render, redirect
from .models import TimeSlot 
barcode_detected = False 
from django.shortcuts import redirect
from datetime import datetime
import cv2
from datetime import datetime
from pyzbar import pyzbar
barcode_detected = False
from .models import barcode_app_s3s4
from datetime import datetime
import cv2
from pyzbar import pyzbar
from .models import *
barcode_detected = False
from django.shortcuts import render
from .models import *
from django.db import connection

import cv2
from pyzbar.pyzbar import decode
from django.shortcuts import redirect
from django.contrib import admin
from django.db import models, connection
import time
import sys

import cv2
from pyzbar.pyzbar import decode
from django.shortcuts import redirect
from django.contrib import admin
from django.db import models, connection
import time
import sys

class DynamicTableAdmin(admin.ModelAdmin):
    list_display = ['barcode_data', 'created_at']
    search_fields = ['barcode_data']
import cv2
from pyzbar.pyzbar import decode
from django.shortcuts import redirect
from django.contrib import admin
from django.db import models, connection
import time
import sys

class DynamicTableAdmin(admin.ModelAdmin):
    list_display = ['barcode_data', 'created_at']
    search_fields = ['barcode_data']
from django.shortcuts import render, redirect
import cv2
from pyzbar.pyzbar import decode
from .models import Teachers
from django.contrib import admin
from django.db import models, connection
from datetime import datetime
import time
import sys
from django.shortcuts import render, redirect
import cv2
from pyzbar.pyzbar import decode
from .models import Teachers
from django.db import connection
from datetime import datetime
import time
import sys

from django.shortcuts import render, redirect
import cv2
from pyzbar.pyzbar import decode
from .models import Teachers
from django.db import connection
from datetime import datetime
import time
import sys
from django.shortcuts import render, redirect
import cv2
from pyzbar.pyzbar import decode
from .models import Teachers
from django.db import connection
from datetime import datetime
import time
import sys
from django.shortcuts import render, redirect
import cv2
from pyzbar.pyzbar import decode
from .models import Teachers
from django.db import connection
from datetime import datetime
import time
import sys
from datetime import datetime
from django.shortcuts import render
import cv2
from pyzbar import pyzbar
from django.shortcuts import render, redirect
from datetime import datetime
import cv2
from pyzbar import pyzbar
from django.urls import reverse
from datetime import datetime
from django.db import connection
from .models import Teachers, TimeSlot
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import CustomUser, TimeSlot, Teachers, Barcode
from .utils import create_dynamic_table
from pyzbar.pyzbar import decode
from datetime import datetime
import cv2
import time
import pyzbar
from .models import barcode_app_s3s4
from .models import s3s4
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import LoginForm
from .models import CustomUser, TimeSlot, Teachers, Barcode
from .utils import create_dynamic_table
from pyzbar.pyzbar import decode
from datetime import datetime
import cv2
import time
import pyzbar
from datetime import datetime
from django.db import connection
from .models import Teachers, TimeSlot
from django.shortcuts import render
from django.contrib import messages

from datetime import datetime
from django.db import connection
from .models import Teachers, TimeSlot
from django.shortcuts import render
from django.contrib import messages
from .models import *
def barcode_display(request, barcode_data, scan_time, day, table_name):
    try:
        scan_time = datetime.strptime(scan_time, "%H:%M:%S")
        # Get the teacher object based on the roll number
        teacher = Teachers.objects.get(rollno=barcode_data)

        # Find the time slot for the current day and time
        time_slot = TimeSlot.objects.filter(day=day, start_time__lte=scan_time, end_time__gt=scan_time).first()

        if time_slot:
            table_name = f"{barcode_data}{time_slot}"
            return render(request, 'barcode_display.html',
                          {'barcode_data': barcode_data, 'time_slot': time_slot.name, 'scan_time': scan_time,
                           'day': day, 'table_name': table_name})
        else:
            messages.error(request, "No time slot found for this time.")
            return render(request, 'barcode_display.html',
                          {'error_message': "No time slot found for this time.", 'barcode_data': barcode_data,
                           'scan_time': scan_time, 'day': day, 'table_name': table_name})
    except Teachers.DoesNotExist:
        messages.error(request, "Teacher not found with this roll number.")
        return render(request, 'barcode_display.html',
                      {'error_message': "Teacher not found with this roll number.", 'barcode_data': barcode_data,
                       'scan_time': scan_time, 'day': day, 'table_name': table_name})
    except TimeSlot.DoesNotExist:
        messages.error(request, "No time slot found for this day.")
        return render(request, 'barcode_display.html',
                      {'error_message': "No time slot found for this day.", 'barcode_data': barcode_data,
                       'scan_time': scan_time, 'day': day, 'table_name': table_name})

def scan_barcode(request):
    global barcode_detected

    if request.method == 'POST':
        cap = cv2.VideoCapture(0)
        day = datetime.now().strftime("%A")  # Getting current day
        scan_time = datetime.now()
        time_str = scan_time.strftime("%H:%M:%S")  # Extracting only the time from the scan_time

        while not barcode_detected:
            ret, frame = cap.read()
            if not ret or frame is None:
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            barcodes = decode(gray)

            for barcode in barcodes:
                data = barcode.data.decode("utf-8")
                barcode_detected = True
                barcode_data = data
                input_time = scan_time.time()

                try:
                    teacher = Teachers.objects.get(rollno=barcode_data)

                    time_slot = TimeSlot.objects.filter(day=day, start_time__lte=input_time,
                                                        end_time__gt=input_time).first()
                    if time_slot:
                        table_name = f"{barcode_data}{time_slot.name}" 
                        cap.release()
                        return render(request, 'barcode_display.html', {
                            'barcode_data': barcode_data,
                            'time_slot': time_slot.name,
                            'scan_time': time_str,
                            'day': day,
                            'table_name': table_name,
                        })
                    else:
                        messages.error(request, "No time slot found for this time.")
                        cap.release()
                        return render(request, 'barcode_display.html',
                                      {'error_message': "No time slot found for this time.", 'barcode_data': barcode_data,
                                       'scan_time': time_str, 'day': day})
                except Teachers.DoesNotExist:
                    cap.release()
                    messages.error(request, "Teacher not found with this roll number.")
                    return render(request, 'barcode_display.html',
                                  {'error_message': "Teacher not found with this roll number.", 'barcode_data': barcode_data,
                                   'scan_time': time_str, 'day': day})
                except TimeSlot.DoesNotExist:
                    cap.release()
                    messages.error(request, "No time slot found for this day.")
                    return render(request, 'barcode_display.html',
                                  {'error_message': "No time slot found for this day.", 'barcode_data': barcode_data,
                                   'scan_time': time_str, 'day': day})

        cap.release()

    return render(request, 'time_slot.html')





def barcode_input(request):
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    unique_barcodes = set()

    while True:
        success, frame = cap.read()
        if not success:
            break

        cv2.imshow('Testing-code-scan', frame)

        for code in decode(frame):
            barcode_data = code.data.decode('utf-8')
            queryset = Barcode.objects.all()
            if barcode_data not in unique_barcodes:
                print(barcode_data)
                unique_barcodes.add(barcode_data)
                Barcode.objects.create(data=barcode_data)

                time.sleep(5)
            else:
                print("This code is already detected")
                time.sleep(5)

        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Testing-code-scan', cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()

    barcodes = Barcode.objects.all()

    return render(request, 'barcode_input.html', {'barcodes': barcodes})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = CustomUser.objects.filter(username=username, password=password).first()
            if user is not None:
                return redirect('select')
            else:
                error = 'Invalid username or password'
                return render(request, 'login.html', {'form': form, 'error': error})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def select(request):
    return render(request, 'select.html')

def home(request):
    if request.method == 'POST':
        if 'btn1' in request.POST:
            return redirect('scan_barcode')
        elif 'btn2' in request.POST:
            return redirect('login')
    return render(request, 'home.html')

def calculate_time_slot(request, barcode_data, scan_time, day):
    try:
        # Get the teacher object based on the roll number
        teacher = Teachers.objects.get(rollno=barcode_data)
        
        scan_time=scan_time
        
        # Find the time slot for the current day and time
        time_slot = TimeSlot.objects.filter(day=day, start_time__lte=scan_time.time(), end_time__gt=scan_time.time()).first()        
        if time_slot:
            table_name = f"{barcode_data}{time_slot.name}"
            create_dynamic_table(table_name)
            return render(request, "time_slot.html", {'time_slot.name':time_slot.name})
        else:
            return "No time slot found for this time."
    except Teachers.DoesNotExist:
        return "Teacher not found with this roll number."
    except TimeSlot.DoesNotExist:
        return "No time slot found for this day."

from .models import s3s4

def start_scan(request, table_name=None):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        error_message = "Error: Couldn't open the camera."
        return render(request, 'error_page.html', {'error_message': error_message})

    cap.set(3, 640)
    cap.set(4, 480)

    unique_barcodes = set()
    scanned_barcodes = []
    teacher_barcode_detected = False  # Flag to indicate if a teacher's barcode is detected

    # Delay to ensure the camera is started properly
    time.sleep(2)

    try:
        while True:
            success, frame = cap.read()
            if not success:
                error_message = "Error: Failed to read frame from camera."
                return render(request, 'error_page.html', {'error_message': error_message})

            cv2.imshow('Testing-code-scan', frame)

            decoded_barcodes = decode(frame)
            if decoded_barcodes:
                for code in decoded_barcodes:
                    barcode_data = code.data.decode('utf-8')
                    table_name = f"{barcode_data}" 
                    if barcode_data not in unique_barcodes:
                        print(barcode_data)
                        unique_barcodes.add(barcode_data)
                        scanned_barcodes.append(barcode_data)

                        # If the scanned barcode matches the teacher's barcode, set the flag
                        if Teachers.objects.filter(rollno=barcode_data).exists():
                            teacher_barcode_detected = True
                            # Check if the barcode is present in the s3s4 table and update its status if found
                            if s3s4.objects.filter(rollno=barcode_data).exists():
                                s3s4_record = s3s4.objects.get(rollno=barcode_data)
                                s3s4_record.present = True
                                s3s4_record.save()

            if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Testing-code-scan', cv2.WND_PROP_VISIBLE) < 1:
                break

            # Exit the loop if a teacher's barcode is detected
            if teacher_barcode_detected:
                break

    except Exception as e:
        error_message = f"Error: {str(e)}"
        return render(request, 'error_page.html', {'error_message': error_message})

    finally:
        cap.release()
        cv2.destroyAllWindows()

    if teacher_barcode_detected:
        return render(request,'new_page.html')

    error_message = "Error: Failed to scan barcode."
    return render(request, 'error_page.html', {'error_message': error_message})

from django.shortcuts import render, redirect
from .models import s3s4

def attendance_record(request):
    if request.method == 'POST':
        s3s4_data = s3s4.objects.all() 
        return render(request,'new_page.html',{'s3s4_data': s3s4_data}) 
    else:
        return render(request, 'attendance_record.html',{'s3s4_data': s3s4_data})

from django.contrib import admin
from .models import *

# Register your models here.
from .models import Faculty
admin.site.register(Faculty)

from .models import Strength
admin.site.register(Strength)

from .models import Infrastructure
admin.site.register(Infrastructure)



admin.site.register(Notice)
admin.site.register(Syllabus)
admin.site.register(Book_list)

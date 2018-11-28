from django.contrib import admin
from .models import *


admin.site.register(Lottery)
admin.site.register(Contest)
admin.site.register(Tips)
admin.site.register(TenContest)
admin.site.register(TenTips)
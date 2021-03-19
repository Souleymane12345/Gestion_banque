from django.contrib import admin

from .models  import Banque , Client , Agent , Compte


admin.site.register(Banque)
admin.site.register(Client)
admin.site.register(Agent)
admin.site.register(Compte)

# Register your models here.

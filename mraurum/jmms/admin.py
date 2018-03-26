# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from jet.admin import CompactInline
#from jet.filters import DateRangeFilter
from .models import *

class UserTypeAdmin(admin.ModelAdmin):
    list_display = ['user_type']
    list_filter = ['user_type']
    search_fields = ['user_type']

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','user_type','user_address','contact_details_1','contact_details_2','email','rating']
    list_filter = ['user_type','rating']
    search_fields = ['name','contact_details_1','email']

class Raw_Material_Type_Admin(admin.ModelAdmin):
    list_display = ['material_name','material_purity','material_current_price','material_unit']
    list_filter = ['material_name','material_purity']
    search_fields = ['material_name','material_current_price']

class Material_Purchase_Admin(admin.ModelAdmin):
    list_display = ['material_type_id','purchase_price','purchase_weight','purchase_date','supplier_id']
    list_filter = ['material_type_id','supplier_id']
    search_fields = ['material_type_id','supplier_id']

class Jewellery_type_Admin(admin.ModelAdmin):
    list_display = ['jewellery_name','material_type_id']
    list_filter = ['jewellery_name','material_type_id']
    search_fields = ['jewellery_name','material_type_id']

class Design_Catalog_Admin(admin.ModelAdmin):
    list_display = ['design_name','design_description','jewellery_type','added_date_time']
    list_filter = ['design_name','jewellery_type']
    search_fields = ['design_name','jewellery_type']

class Jewel_Admin(admin.ModelAdmin):
    list_display = ['jewel_name']
    list_filter = ['jewel_name']
    search_fields = ['jewel_name']

class Jewellery_Admin(admin.ModelAdmin):
    list_display = ['design_id','raw_material_id']
    list_filter = ['design_id','raw_material_id']
    search_fields = ['design_id','raw_material_id']

class Cutting_phase_Admin(admin.ModelAdmin):
    list_display = ['jewellery_id','cutter_id','weight_sent','receive_weight','cutting_cost','other_cost','sent_date','receive_date']
    list_filter = ['jewellery_id','cutter_id','sent_date','receive_date']
    search_fields = ['jewellery_id','cutter_id','sent_date','receive_date']

class Embedding_phase_Admin(admin.ModelAdmin):
    list_display = ['jewellery_id','embedder_id','weight_sent','receive_weight','jewel_id','jewel_price','jewel_quantity','jewel_weight','jewel_size','embedding_cost','other_cost','sent_date','receive_date']
    list_filter = ['jewellery_id','embedder_id','jewel_id','sent_date','receive_date']
    search_fields = ['jewellery_id','embedder_id','jewel_id','sent_date','receive_date']

class Polishing_phase_Admin(admin.ModelAdmin):
    list_display = ['jewellery_id','polisher_id','weight_sent','receive_weight','polishing_cost','other_cost','sent_date','receive_date']
    list_filter = ['jewellery_id','polisher_id','sent_date','receive_date']
    search_fields = ['jewellery_id','polisher_id','sent_date','receive_date']

admin.site.register(UserType, UserTypeAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Raw_Material_Type, Raw_Material_Type_Admin)
admin.site.register(Material_Purchase, Material_Purchase_Admin)
admin.site.register(Jewellery_type, Jewellery_type_Admin)
admin.site.register(Design_Catalog, Design_Catalog_Admin)
admin.site.register(Jewel, Jewel_Admin)
admin.site.register(Jewellery, Jewellery_Admin)
admin.site.register(Cutting_phase, Cutting_phase_Admin)
admin.site.register(Embedding_phase, Embedding_phase_Admin)
admin.site.register(Polishing_phase, Polishing_phase_Admin)
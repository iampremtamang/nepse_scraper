from django.contrib import admin, messages
from django.utils.translation import ngettext
from django.core import serializers
from django.http import HttpResponse

from share.models import Security, SecurityDetail



class SecurityAdmin(admin.ModelAdmin):
    @admin.action(description='Set traded to True')
    def set_traded_true(modeladmin, request, queryset):
        updated=queryset.update(traded=True)
        modeladmin.message_user(request, ngettext(
            '%d security was successfully marked as traded.',
            '%d sercurities were successfully marked as traded.',
            updated, 
            
        )%updated, messages.SUCCESS)
        
    
    @admin.action(description='Set traded to False')
    def set_traded_false(modeladmin, request, queryset):
        updated = queryset.update(traded=False)
        modeladmin.message_user(request, ngettext(
            '%d security was successfully marked as non-traded.',
            '%d sucurities were successfully marked as non-traded.',
            updated,
        )%updated, messages.SUCCESS)
    
    @admin.action(description='Export as JSON')
    def export_as_json(modeladmin, request, queryset):
        response = HttpResponse(content_type='application/json')
        serializers.serialize("json", queryset, stream=response)
        return response
        
    
    
        
    model = Security
    list_display = ['symbol', 'name', 'traded']
    list_filter = ['created', 'traded']
    search_fields = ['symbol', 'name']
    list_display_links = ['symbol', 'name']
    list_editable = ['traded']
    list_per_page = 200
    ordering = ('symbol', )
    # date_hierarchy = ('')
    fieldsets = (
        (None, {'fields':('traded', )}),
    )
    # autocomplete_fields = ('symbol', 'name')
    
    actions = [set_traded_true, set_traded_false, export_as_json]
    # actions = None # to disable action
    
    


class SecurityDetailAdmin(admin.ModelAdmin):
    model = SecurityDetail
    list_display = ['symbol', 'market_price', 'sector', 'percentage_change', 'high', 'low', 'avg_180_day', 'avg_120_day', 'one_year_yield', 'eps', 'pe_ratio', 'market_capitalization', 'updated']
    list_filter = ['sector']
    search_fields = ['symbol']

admin.site.register(Security, SecurityAdmin)
admin.site.register(SecurityDetail, SecurityDetailAdmin)
# admin.site.add_action(export_as_json)
admin.site.disable_action('delete_selected')
from django.contrib import admin
from .models import ServiceCard

class ServiceCardAdmin(admin.ModelAdmin):
    # Display fields in the admin list view
    list_display = ('title', 'subtitle', 'description', 'image')
    
    # Add search functionality for title and description
    search_fields = ('title', 'description')
    
    # Add filters to filter by title and subtitle
    list_filter = ('title', 'subtitle')
    
    # Optional: Add the ability to filter the list of cards by their fields
    list_per_page = 10  # Limit the number of records per page

    # Display fields in the form view when adding/editing
    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle', 'description', 'image' )
        }),
    )

# Register the ServiceCard model in the admin panel with the ServiceCardAdmin configuration
admin.site.register(ServiceCard, ServiceCardAdmin)
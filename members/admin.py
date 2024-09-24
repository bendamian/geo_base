from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

# Register your models here.
# Unregister Groups
admin.site.unregister(Group)

# Mix Profile info into User info


class ProfileInline(admin.StackedInline):
    model = Profile
    fields = ('name', 'phone_number', 'email', 'profile_bio', 'facebook_link', 'profile_image')
    readonly_fields = ('date_modified',)
    extra = 1  # Controls the number of empty forms displayed for adding new related objects
    # Provides a link to change the related object in a separate form
    show_change_link = True

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')


class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', ' phone_number', 'name')
    list_filter = ('is_active', 'is_staff')


# Unregister the original User model from the admin
admin.site.unregister(User)
# Register the new User admin with Profile inline
admin.site.register(User, UserAdmin)

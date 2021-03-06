from communities import models
from django.contrib.admin import site
from django.contrib.admin.options import ModelAdmin, TabularInline
from users.models import Membership


class CommunityMembershipInline(TabularInline):
    model = Membership
    fk_name = 'community'


class CommunityAdmin(ModelAdmin):

    fields = (
              'name',
              'official_identifier',
              'logo',
              'is_public',
              'straw_voting_enabled',
              )

    inlines = [CommunityMembershipInline]


site.register(models.Community, CommunityAdmin)

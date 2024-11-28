from django.contrib import admin
from .models import Drone, DronesCategory, Pilot, Competition
from django.utils.html import format_html

# Register your models here.
@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    pass
    list_display = ('name', 'display_picture', 'owner', 'is_published')
    
    list_editable = ('is_published', 'owner')
    
    search_fields = ("name", "owner__username")
    
    list_filter = ("drone_category", "owner")
    
    readonly_fields = ('owner',)
    
    save_on_top = True
    
    def display_picture(self, obj):
        if obj.picture:
            return format_html('<img src="{}" width="50" height="50" />', obj.picture.url)
        return "Sem imagem"
    
    display_picture.short_description = "Imagem"
    
@admin.register(DronesCategory)
class DronesCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Pilot)
class PilotAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "races_count")
    search_fields = ("name", "gender")
    list_filter = ("inserted_timestamp",)

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ("pilot", "drone", "distance_in_feet", "distance_achievement_date")
    search_fields = ("pilot__name", "drone__name")
    list_filter = ("distance_achievement_date", "drone__drone_category")
    date_hierarchy = "distance_achievement_date"                #diciona uma navegação por hierarquia de datas na parte superior da lista de objetos.
    save_on_top = True
    
    fieldsets = (
        (
            "Selecionar Piloto e Drone",
            {
                "fields": (
                    "pilot",
                    "drone",
                )
            },
        ),
        (
            "Adicionar Detalhes da Competição",
            {
                "fields":(
                    "distance_in_feet",
                    "distance_achievement_date",
                )
            },
        ),
    )
from django.contrib import admin
from vistaprevia.models import Categoria, Producto

class ProductoInline(admin.TabularInline):
    model = Producto
    extra = 0

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [ProductoInline]

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Relación", {"fields": ["categoria"]}),
        (
            "Datos generales",
            {
                "fields": [
                    'fecha_publicacion', 'producto', 'estado', 'descripcion', 'imagen'
                ]
            },
        ),
    ]
    list_display = ['producto', 'fecha_publicacion', 'tipo_de_producto', 'imagen', 'upper_case_name']
    ordering = ['-fecha_publicacion']
    list_filter = ('producto', 'fecha_publicacion',)
    search_fields = ('producto', 'estado',)
    list_display_links = ('producto', 'fecha_publicacion',)

    @admin.display(description='Name')
    def upper_case_name(self, obj):
        return ("%s %s" % (obj.producto, obj.estado)).upper()

admin.site.register(Categoria, CategoriaAdmin)

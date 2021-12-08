from django.contrib import admin
from .models import Questions, Choices, QuestionsSet


# Register your models here.

class ChoicesInline(admin.TabularInline):
    model = Choices
    extra = 0


class QuestionsInline(admin.TabularInline):
    model = Questions
    extra = 0


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('text_question',)
    # ordering = ('id_question',)
    # fields = ('id_question', 'text_question',)
    inlines = (ChoicesInline,)


class QuestionsSetAdmin(admin.ModelAdmin):
    # list_display = ('id_set', 'set_title',)
    # inlines = (QuestionsInline,)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        #if db_field.name == "id_set":
        kwargs["queryset"] = Questions.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Choices)
admin.site.register(QuestionsSet, QuestionsSetAdmin)

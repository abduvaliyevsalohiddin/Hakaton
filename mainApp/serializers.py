from rest_framework import serializers

from connectApp.models import Vacancy
from connectApp.serializers import VacancySerializer
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def to_representation(self, instance):
        project = super(ProjectSerializer, self).to_representation(instance)
        vacancies = Vacancy.objects.filter(project__id=project.get('id'))
        vacancy_serializer = VacancySerializer(vacancies, many=True)
        project.update(
            {
                'vacancies': vacancy_serializer.data
            }
        )
        return project

from django.apps import AppConfig


class WordcountConfig(AppConfig): #이 class이름을 settings.py -> Installed Apps에 추가
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wordCount'

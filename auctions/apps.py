from django.apps import AppConfig


class AuctionsConfig(AppConfig):
    name = 'auctions'
    #This line explicitly define the primary key type
    default_auto_field = 'django.db.models.BigAutoField'
    

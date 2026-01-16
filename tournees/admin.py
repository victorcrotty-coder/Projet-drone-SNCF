from django.contrib import admin
from .models import Drone, Batterie, Site, Mission, Vol, Maintenance, Piece, MaintenancePiece, DroneBatterie

admin.site.register(Drone)
admin.site.register(Batterie)
admin.site.register(Site)
admin.site.register(Mission)
admin.site.register(Vol)
admin.site.register(Maintenance)
admin.site.register(Piece)
admin.site.register(MaintenancePiece)
admin.site.register(DroneBatterie)
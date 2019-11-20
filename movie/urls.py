from rest_framework.routers import SimpleRouter
from .views import ActorActions,MovieActions

simpleRouter = SimpleRouter()

simpleRouter.register('Actor',ActorActions)
simpleRouter.register('Movie',MovieActions)

urlpatterns = simpleRouter.urls
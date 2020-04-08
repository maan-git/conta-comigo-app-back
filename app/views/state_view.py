from utils.views_utils import ModelViewSetReadOnly
from app.models.state import State
from utils.views_utils import get_generic_read_serializer


class StateView(ModelViewSetReadOnly):
    queryset = State.objects.all()

    def get_serializer_class(self):
        serializer_class = get_generic_read_serializer(State, 1)
        return serializer_class

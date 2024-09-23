#REPORTS/MIXINS.PY

from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied

class UserIsOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user or self.request.user.is_staff

    def handle_no_permission(self):
        raise PermissionDenied("You don't have permission to access this report.")
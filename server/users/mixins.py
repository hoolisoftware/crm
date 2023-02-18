from typing import Tuple, Dict

from django.shortcuts import redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse


class AlreadySignedInMixin:
    redirect_authenticated_user: str = None

    def get(
        self,
        request: HttpRequest,
        *args: Tuple,
        **kwargs: Dict
    ) -> HttpResponse:

        if (request.user.is_authenticated and
                self.redirect_authenticated_user):
            return redirect(self.redirect_authenticated_user)

        return super().get(request, *args, **kwargs)

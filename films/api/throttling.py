from rest_framework.throttling import UserRateThrottle


class GetUserRateThrottle(UserRateThrottle):
    scope = 'get-user-rate'

    def allow_request(self, request, view):
        """
        Return `True` if the request should be allowed, `False` otherwise.
        """

        if request.user and request.user.is_staff:
            # return always TRUE if user is super_admin
            return True

        if request.method == 'GET':
            return super().allow_request(request, view)

        return True


class PostReviewThrottle(UserRateThrottle):
    scope = 'post-review'

    def allow_request(self, request, view):
        """
        Return `True` if the request should be allowed, `False` otherwise.
        """

        if request.method == 'POST':
            return super().allow_request(request, view)

        return True

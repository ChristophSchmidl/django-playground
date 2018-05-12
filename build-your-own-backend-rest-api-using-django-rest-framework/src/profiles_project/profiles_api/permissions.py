from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    Allows users to edit their own profile.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check user is trying to edit their own profile.
        :param request:
        :param view:
        :param obj:
        :return:
        """

        # if the user is just looking at a profile without
        # changing it then allow the action
        if request.method in permissions.SAFE_METHODS:
            return True

        # is the object's id (profile id) which the user wants to change
        # the same as the user's id?
        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """
    Allow users to update their own status.
    """

    def has_object_permission(self, request, view, obj):
        """
        Checks the user is trying to update their own status.
        :param request:
        :param view:
        :param obj:
        :return:
        """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id

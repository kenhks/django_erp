from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from .abstract import BaseAbstractModel
# from django.utils.functional import cached_property


class Organization(BaseAbstractModel):
    """
    Stores a single organization record, related user and sub-organization model
    """

    name = models.CharField(_("Name"), max_length=255,
                            blank=False, unique=True)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, related_name="childs",
                               null=True, blank=True,
                               verbose_name=_("Parent Organization"),)
    level_choice = [
        (0, 'Normal'),
        (1, 'Company'),
        (2, 'Department'),
        (3, 'Division'),
    ]
    users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   through="OrganizationMember",
                                   through_fields=("organization", "user"),
                                   related_name="orgs",
                                   blank=True, verbose_name=_("Organization Users"),)

    level = models.IntegerField(choices=level_choice, default=0,
                                verbose_name=_("Level"))

    class Meta:
        verbose_name = "Organization"

    def __str__(self):
        return self.name



class OrganizationMember(BaseAbstractModel):
    """
    This model represents the intermediate model of the relation between a User and a Organization.
    """
    organization = models.ForeignKey("Organization", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    roles = models.ManyToManyField(
        "OrganizationMemberRole", blank=True, verbose_name=_('roles'))

    class Meta:
        ordering = ("organization", "user")
        unique_together = ("organization", "user")
        verbose_name = "Organization Member"

    def __str__(self):
        return "{} - {}".format(self.organization.name, self.user.username)


class OrganizationMemberRole(BaseAbstractModel):

    name = models.CharField(_("Name"), max_length=255,
                            blank=False, unique=True)

    class Meta:
        verbose_name = "Organization Role"

    def __str__(self):
        return self.name

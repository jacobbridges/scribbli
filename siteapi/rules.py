import rules
from rules import predicate, is_group_member, is_authenticated


####################################################################################################
# Predicates

is_moderator = is_group_member('moderators')
is_admin = is_group_member('administrators')
is_admin_or_mod = is_admin | is_admin


@predicate
def is_object_public(user, object):
    return object.is_public


@predicate
def is_owner(user, object):
    return object.owner.pk is user.pk

@predicate
def is_parent_public(user, object):
    return object._parent.is_public


@predicate
def has_parent_permissions(user, object):
    return object._parent.owner.pk is user.pk


####################################################################################################
# Add Permissions

# Image permissions
rules.add_perm('siteapi.image_create', is_authenticated)
rules.add_perm('siteapi.image_update', is_owner | is_admin_or_mod)
rules.add_perm('siteapi.image_detail', is_authenticated)
rules.add_perm('siteapi.image_list', is_authenticated)
rules.add_perm('siteapi.image_delete', is_owner | is_admin_or_mod)

# Universe permissions
rules.add_perm('siteapi.universe_create', is_admin)
rules.add_perm('siteapi.universe_update', is_admin_or_mod)
rules.add_perm('siteapi.universe_detail', ((is_object_public & is_authenticated) | is_admin_or_mod))
rules.add_perm('siteapi.universe_list', is_admin_or_mod)
rules.add_perm('siteapi.universe_delete', is_admin)

# World permissions
rules.add_perm('siteapi.world_create', is_authenticated)
rules.add_perm('siteapi.world_update', is_owner | is_admin_or_mod)
rules.add_perm('siteapi.world_detail', (is_object_public & is_authenticated) | is_admin_or_mod | is_owner)
rules.add_perm('siteapi.world_list', is_authenticated)
rules.add_perm('siteapi.world_delete', is_owner | is_admin_or_mod)

# Destination permissions
rules.add_perm('siteapi.destination_create', is_authenticated)
rules.add_perm('siteapi.destination_update', has_parent_permissions | is_owner | is_admin_or_mod)
rules.add_perm('siteapi.destination_detail', (is_object_public & is_authenticated) | has_parent_permissions | is_owner | is_admin_or_mod)
rules.add_perm('siteapi.destination_list', is_authenticated)
rules.add_perm('siteapi.destination_delete', is_owner | has_parent_permissions | is_admin_or_mod)

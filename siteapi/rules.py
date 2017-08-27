import rules
from rules import predicate, is_group_member, is_authenticated


####################################################################################################
# Predicates

is_moderator = is_group_member('moderators')
is_admin = is_group_member('administrators')
is_admin_or_mod = is_admin | is_admin


@predicate
def is_universe_public(user, universe):
    return universe.is_public


####################################################################################################
# Add Permissions

# Universe permissions
rules.add_perm('siteapi.universe_create', is_admin)
rules.add_perm('siteapi.universe_update', is_admin_or_mod)
rules.add_perm('siteapi.universe_detail', ((is_universe_public & is_authenticated) | is_admin_or_mod))
rules.add_perm('siteapi.universe_list', is_admin_or_mod)
rules.add_perm('siteapi.universe_delete', is_admin)

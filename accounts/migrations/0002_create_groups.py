from django.db import migrations


MODELS = ['club', 'coach', 'athlete', 'team', 'tournament']

VIEWER_ACTIONS = ['view']
EDITOR_ACTIONS = ['add', 'change', 'view']
MANAGER_ACTIONS = ['add', 'change', 'delete', 'view']


def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    viewer_group, _ = Group.objects.get_or_create(name='Viewer')
    editor_group, _ = Group.objects.get_or_create(name='Editor')
    manager_group, _ = Group.objects.get_or_create(name='Manager')

    viewer_codenames = [f'{action}_{model}' for action in VIEWER_ACTIONS for model in MODELS]
    editor_codenames = [f'{action}_{model}' for action in EDITOR_ACTIONS for model in MODELS]
    manager_codenames = [f'{action}_{model}' for action in MANAGER_ACTIONS for model in MODELS]

    viewer_group.permissions.set(Permission.objects.filter(codename__in=viewer_codenames))
    editor_group.permissions.set(Permission.objects.filter(codename__in=editor_codenames))
    manager_group.permissions.set(Permission.objects.filter(codename__in=manager_codenames))


def delete_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name__in=['Viewer', 'Editor', 'Manager']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('clubs', '0004_alter_club_city_alter_club_country'),
        ('coaches', '0003_data_migration_coaches'),
        ('athletes', '0005_data_migration_athletes_teams'),
        ('tournaments', '0002_alter_tournament_city_alter_tournament_country'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(create_groups, delete_groups),
    ]

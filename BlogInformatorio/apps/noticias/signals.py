from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def crear_grupos_y_permisos(sender, **kwargs):
    if sender.name == 'noticias': 

        grupos = [
            {
                'name': 'Visitante',
                'permissions': [],  # Navegar y leer, sin permisos especiales
            },
            {
                'name': 'Miembro',
                'permissions': [
                    'add_comentario',
                    'change_comentario',
                    'delete_comentario',
                ],
            },
            {
                'name': 'Colaborador',
                'permissions': [
                    'add_noticia',
                    'change_noticia',
                    'delete_noticia',
                    'add_foto',
                    'change_foto',
                    'delete_foto',
                    'add_comentario',
                    'change_comentario',
                    'delete_comentario',
                    'add_categoria',
                    'change_categoria',
                    'delete_categoria',
                ],
            },
        ]

        for grupo_data in grupos:
            grupo, creado = Group.objects.get_or_create(name=grupo_data['name'])
            permisos = []
            for codename in grupo_data['permissions']:
                try:
                    permiso = Permission.objects.get(codename=codename)
                    permisos.append(permiso)
                except Permission.DoesNotExist:
                    print(f"Permiso {codename} no existe. Asegurate que la migración se hizo y el modelo existe.")
            grupo.permissions.set(permisos)
            grupo.save()

from django.test import TestCase
from .models import Project
from django.core.files.uploadedfile import SimpleUploadedFile

#Test para comprobar que se puede crear una instancia del modelo "project" correctamente
class ProjectModelTest(TestCase):
    def test_create_project(self):
        project1 = Project(title="Proyecto 1", description="Descripción del proyecto 1")
        project1.save()
        self.assertEqual(project1.title, "Proyecto 1")
        self.assertEqual(project1.description, "Descripción del proyecto 1")


#Test para comprobar que se puede subir una imagen correctamente
class ProjectModelTest(TestCase):
    def test_upload_image(self):
        image = SimpleUploadedFile("test_image.jpg", b"random_image_content", content_type="image/jpeg")
        project1 = Project(title="Proyecto 1", description="Descripción del proyecto 1", image=image)
        project1.save()
        self.assertEqual(project1.image.name, "portafolio/images/test_image.jpg")


#Test para comprobar que se puede asignar una URL correctamente
class ProjectModelTest(TestCase):
    def test_assign_url(self):
        project1 = Project(title="Proyecto 1", description="Descripción del proyecto 1", url="https://www.google.com")
        project1.save()
        self.assertEqual(project1.url, "https://www.google.com")
           

#Test para comprobar que se puede actualizar una instancia del modelo "project" correctamentE
class ProjectModelTest(TestCase):
    def test_update_project(self):
        project1 = Project(title="Proyecto 1", description="Descripción del proyecto 1")
        project1.save()
        project1.title = "Proyecto 2"
        project1.description = "Descripción del proyecto 2"
        project1.save()
        updated_project = Project.objects.get(id=project1.id)
        self.assertEqual(updated_project.title, "Proyecto 2")
        self.assertEqual(updated_project.description, "Descripción del proyecto 2")


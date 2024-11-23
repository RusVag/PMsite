from inertia.utils import InertiaJsonEncoder
from django.db.models.fields.files import ImageFieldFile

class ImageFieldFileAwareJsonEncoder(InertiaJsonEncoder):
   def default(self, value):
      if isinstance(value, ImageFieldFile):
         return value.path
      
      return super().default(value)
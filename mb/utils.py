from django.db.models.fields import FieldDoesNotExist
from django.db import models
from django.core.exceptions import ValidationError

from data_importer.importers import XMLImporter


class FKXMLImporter(XMLImporter):
    """
    Derived from data_import XMLImporter overrides clean_fileds to
    clean foreign keys properly and use defualts when no value is given.
    """
    def clean_field(self, field_name, value):
        """
        User default django field validators to clean content
        and run custom validates
        """
        if self.Meta.model:
            try:
                field = self.Meta.model._meta.get_field(field_name)
                if type(field) == models.ForeignKey:
                    return self.clean_foreignkey_field(field, value)
                if value is None:
                    if field.has_default():
                        value = field.default
            except FieldDoesNotExist:
                pass  # do nothing if not find this field in model
        return super(FKXMLImporter, self).clean_field(field_name, value)

    def clean_foreignkey_field(self, field, value):
        """
        Cleans ForeignKet fields.
        """
        try:
            field.clean(value, None)
        except Exception as msg:
            default_msg = msg.messages[0].replace('This field', '')
            new_msg = 'Field ({0!s}) {1!s}'.format(field.name, default_msg)
            raise ValidationError(new_msg)

        clean_function = getattr(self, 'clean_{0!s}'.format(field.name), False)
        if clean_function:
            try:
                return clean_function(value)
            except Exception as msg:
                default_msg = str(msg).replace('This field', '')
                new_msg = 'Field ({0!s}) {1!s}'.format(field.name, default_msg)
                raise ValidationError(new_msg)
        return int(value)

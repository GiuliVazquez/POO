class SchemaError(Exception):
    """Excepción para errores de esquema."""
    pass

class Str2Dic():
    def __init__(self, schema, separator=','):
        if (len(schema)) == 0:
            raise SchemaError("El schema está vacío")
        self.schema = schema.split(separator)
        self.separator = separator 

    def convert(self,row: list[str]) -> dict:
        linea = row.split(self.separator)
        if len(linea) == len(self.schema):
            i = 0
            d ={}
            for i in range(len(linea)):
                d[self.schema[i]] = linea[i]
            return d
        else: 
            raise SchemaError("Los campos de la línea no concuerdan con el sistema")
            
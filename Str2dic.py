
class Str2Dic():
    def _init_(self, schema, separator=','):
        self.schema = schema.split(separator)
        self.separator = separator 
    def convert(self,row):
        tmp = row.split(self.separator)
        if len(tmp) == len(self.schema):
            i = 0
            d ={}
            while i < len(tmp):
                d[self.schema[i]] = tmp[i]
                i += 1
                return d
            
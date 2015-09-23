from rest_framework import views
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response


class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)

    def put(self, *args, **kwargs):
        file_obj = self.request.data['file']
        print 'file_obj.__dict__', file_obj.__dict__
        return Response(status=204)

from .serializers import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def AddRetrieve(request):
    if request.method == 'GET':
        all_employee  = Product.objects.all()
        data = ProductSerializer(all_employee,many=True)
        return Response(data.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        form_data = ProductSerializer(data=request.data)
        if form_data.is_valid():
            form_data.save()
            return Response({'message':'Succesfuly created'},status=status.HTTP_201_CREATED)
        return Response({'error':'oops something went wrong!!'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
def UpdateDelete(request,id):
    try:
        get_product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({'error':'please pass valid id'},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        form_data = ProductSerializer(instance=get_product,data=request.data,partial=True)
        if form_data.is_valid():
            form_data.save()
            return Response({'message':'Updated succesfully!!'},status=status.HTTP_200_OK)
        return Response({'error':'ooops someting went wrong!!'},status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        get_product.delete()
        return Response({'message':'Succesfully Deleted!!'},status=status.HTTP_200_OK)
    
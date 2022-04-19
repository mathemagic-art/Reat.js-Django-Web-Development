from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NewtonSerializer,  DiffSerializer, TaylorSerializer
from .mathematics import Newton_Method, Differentiating_Calculator, taylor
# Create your views here.

@api_view(['POST'])
def newton_list(request):
    if request.method == 'POST':
        print("sdfsdgsdfgdfgsdfgdgsdfgdsfgd", request.data)
        deserialized = NewtonSerializer(data=request.data)
        if deserialized.is_valid():
            equation = deserialized.data['equation']
            first = int(deserialized.data['first'])
            second = int(deserialized.data['second'])
            answer = Newton_Method(equation, first, second)
            return Response(answer, status=status.HTTP_201_CREATED)
        else:
            return Response(deserialized.error_messages)


@api_view(['POST'])
def diff_list(request):
    if request.method == 'POST':
        deserialized = DiffSerializer(data=request.data)
        if deserialized.is_valid():
            equation = deserialized.data['equation']
            answer = Differentiating_Calculator(equation)
            return Response(answer, status=status.HTTP_201_CREATED)
        else:
            return Response(deserialized.errors)
    

    # if request.method == 'GET':
    #     answer = {
    #         "equation":"x",
    #         "first":200,
    #         "second":300
    #     }

    #     serializer = NewtonSerializer(data=answer)
    #     serializer.is_valid()
    #     return Response(serializer.validated_data, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def taylor_list(request):
    if request.method == 'POST':
        deserialized = TaylorSerializer(data=request.data)
        if deserialized.is_valid():
            function = deserialized.data['function']
            num_of_iter = deserialized.data['num_of_iter']
            center = deserialized.data['center']
            answer = taylor(function, num_of_iter, center)
            return Response(answer, status=status.HTTP_201_CREATED)
        else:
            return Response(deserialized.errors)
    
    


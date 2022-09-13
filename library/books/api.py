from ninja import NinjaAPI
router = NinjaAPI()

@router.get('/hello')
def hello(request, response=str):
    return 'hello'
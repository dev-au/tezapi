from tezapi import Router, Request

router = Router('/v1')


@router.middleware()
async def catcher(request):
    print('Middleware is working')


@router.get('/test')
async def test_v1(request: Request):
    return 'Working router...'

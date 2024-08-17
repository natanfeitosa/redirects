import json
import os

from lespy import App, Request
from lespy.http.utils import make_url

from load_envs import load_env_files
from redirect_response import RedirectResponse
from wildcard_route import WildcardRoute

load_env_files()

domain, status_code, full = (os.environ.get('NEW_DOMAIN'), int(os.environ.get('REDIRECT_STATUS', '301')),
                             os.environ.get('FULL_REDIRECT', 'true'))

if not domain:
    raise ValueError('is NEW_DOMAIN valid?')


class MyApp(App):
    def __init__(self):
        super().__init__('my_app')
        self._router.add_route(WildcardRoute('*', 'any_route', ['GET'], self.proxy))

    def proxy(self, request: Request):
        redirect_to = domain

        if json.loads(full):
            scheme, host = domain.split('://')
            redirect_to = make_url(scheme, host, request.path, request.GET)

        print(self._app_name, 'redirecting from:', request.path, 'status code:', status_code)
        return RedirectResponse(redirect_to, status_code)


app = MyApp()

if __name__ == '__main__':
    from lespy import run
    run(app)

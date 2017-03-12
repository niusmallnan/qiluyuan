import requests
from django.http import HttpResponse
from django.views.generic import View

class MetadataView(View):

    RANCHER_MD_BASE = 'http://169.254.169.250/2016-07-29'

    def _info(self, param):
        return requests.get(self.RANCHER_MD_BASE+param).text

    def _get_host(self):
        ip = self._info('/self/host/agent_ip')
        name = self._info('/self/host/name')
        return (name, ip)

    def _get_container(self):
        ip = self._info('/self/container/primary_ip')
        name = self._info('/self/container/name')
        return (name, ip)

    def _get_service(self):
        name = self._info('/self/service/name')
        scale = self._info('/self/service/scale')
        return (name, scale)


    def get(self, request, *args, **kwargs):
        res = []
        res.append('host info: %s' % ','.join(self._get_host()))
        res.append('container info: %s' % ','.join(self._get_container()))
        res.append('serivce info: %s' % ','.join(self._get_service()))
        return HttpResponse('<br />'.join(res))

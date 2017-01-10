from django.shortcuts import render
from django.conf import settings
from django.utils.safestring import mark_safe

def discovery(request):
    return render(request, 'shibboleth_eds/discovery.html', {
        'non_js_url': getattr(settings, 'SHIBBOLETH_EDS_NON_JS_URL', 'http://federation.org/DS/DS?entityID=https%3A%2F%2FyourentityId.edu.edu%2Fshibboleth&return=https%3A%2F%2Fyourreturn.edu%2FShibboleth.sso%2FDS%3FSAMLDS%3D1%26target%3Dhttps%3A%2F%2Fyourreturn.edu%2F'),
    })

def config(request):
    return render(request, 'shibboleth_eds/idpselect_config.js', {
        'dataSource': getattr(settings, 'SHIBBOLETH_EDS_DATA_SOURCE', '/Shibboleth.sso/DiscoFeed'),
        'defaultReturn': mark_safe(getattr(settings, 'SHIBBOLETH_EDS_DEFAULT_RETURN', 'null')),
        'defaultLogo': getattr(settings, 'SHIBBOLETH_EDS_DEFAULT_LOGO', '/media/assets/shibboleth_eds/blank.gif'),
        'helpURL': getattr(settings, 'SHIBBOLETH_EDS_HELP_URL', 'https://wiki.shibboleth.net/confluence/display/DEV/EDSDetails'),
        'preferredIdP': mark_safe(getattr(settings, 'SHIBBOLETH_EDS_PREFERRED_IDPS', 'null')),
        'hiddenIdPs': mark_safe(getattr(settings, 'SHIBBOLETH_EDS_HIDDEN_IDPS', 'null')),
        'showListFirst': getattr(settings, 'SHIBBOLETH_EDS_SHOW_LIST_FIRST', 'false'),
        'autoFollowCookie': mark_safe(getattr(settings, 'SHIBBOLETH_EDS_FOLLOW_COOKIE', 'null')),
    }, content_type='application/javascript')

from django.conf import settings
from django.conf.urls import patterns, url
from django.core.urlresolvers import LocaleRegexURLResolver

def i18n_patterns(prefix, *args):
    """
    Adds the language code prefix to every URL pattern within this
    function. This may only be used in the root URLconf, not in an included
    URLconf.

    """
    pattern_list = patterns(prefix, *args)
    if not settings.USE_I18N:
        return pattern_list
    return [LocaleRegexURLResolver(pattern_list)]


urlpatterns = patterns('',
    url(r'^changelang/$', 'edraak_misc.views.set_language', name='edraak_setlang'),
    url(r'^check_student_grades/$', 'edraak_misc.views.check_student_grades', name='edraak_check_student_grades'),
    url(r'^all_courses/$', 'edraak_misc.views.all_courses', name='edraak_all_courses'),
)
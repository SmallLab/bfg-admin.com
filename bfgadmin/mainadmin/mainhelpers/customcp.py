from mainadmin.models import Sentence


def newsentences(request):
    return {
        'count_new_sentences': Sentence.objects.filter(on_moderation=0).filter(status=0).count()
    }
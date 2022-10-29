from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import speech_to_text
from . import text_similarity
from . import error_rate_cal

@api_view(['POST'])
def speech_processing(request):
    text = request.data.get("text", None)
    speech_file = request.FILES.get("audio")
    
    stt_text = speech_to_text.stt(speech_file)

    sentence = (text, stt_text)
    print('(text, stt_text): ',sentence)
    # text_similarity. 코사인 유사도는 1이 가장 정확하고 나머지는 낮을수록 정확함.
    # similarity = text_similarity.ts(sentence)
    
    # error_rate_cal는 낮을수록 정확
    similarity = error_rate_cal.cer(text, stt_text)
    
    if similarity < 0.38: # 0.3-> 0.2 -> 0.38(유사하게 읽는 것들도 통과시키기 위한 목적)로 수정
        return Response(data={'message':'True'})
    return Response(data={'message':'False'})

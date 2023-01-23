# omer khan 391007603
# sultan fahad 391002603

# =====================================================================================
# ======================== قواعد ===================================================== 
# =====================================================================================



# <text>→ <sentence> | <sentence> <conjunction> <sentence>
# <sentence> → <verb sentence> | <noun sentence>
# <verb sentence> → <adjective> <verb> | <object> <adjective> <verb>
# <noun sentence> → <noun> ( <adjective> |  <object> )

# <verb> →
#  شرب | ذهب | اكل
# <adjective> →
#  احمد | عمر | سلطان
# <object> →
#  البرتقال | التفاح | الماء
# <noun> →
#  صادق | لذيذ | بارد
# <conjunction> →
#  لكن | او | و


# =====================================================================================
# ======================== ثوابت ===================================================== 
# =====================================================================================

# الحركات

FATHATAN = u'\u064b'
DAMMATAN = u'\u064c'
KASRATAN = u'\u064d'
FATHA = u'\u064e'
DAMMA = u'\u064f'
KASRA = u'\u0650'
SHADDA = u'\u0651'
SUKUN = u'\u0652'

# الكلمات
f = open("names.txt","r")
scanner = f.read().split()
adjective = [*set(scanner)]
#r = "\n"
#out = r.join(adjective)
#f = open("names.txt", "a")
#f.write(out)
#f.close()
verb = ["اكل","ذهب"]
objects = ["الماء","التفاح","البرتقال"]
noun = ["بارد", "لذيذ" , "صادق"]
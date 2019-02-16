import re,collections,string


NWORDS = collections.defaultdict(lambda:1)

def words(text):
    return re.findall('[a-z]+',text.lower())

# 数一数各种单词有多少个
def train(features):
    # defaultdict是一个字典，当键值不存在的时候返回默认值
    # model = collections.defaultdict(lambda:1)
    for feature in features:
        NWORDS[feature] += 1
    return NWORDS

def known(words): return set(w for w in words if w in NWORDS)

# 编辑距离为1，假设输入为boy
# deletion ：['oy', 'by', 'bo']
# transposition：['oby', 'byo']
# alteration ：['aoy', 'boy', 'coy', 'doy', 'eoy', 'foy', 'goy', 'hoy', 'ioy', 'joy', 'koy', 'loy', 'moy', 'noy', 'ooy', 'poy', 'qoy', 'roy', 'soy', 'toy', 'uoy', 'voy', 'woy', 'xoy', 'yoy', 'zoy', 'bay', 'bby', 'bcy', 'bdy', 'bey', 'bfy', 'bgy', 'bhy', 'biy', 'bjy', 'bky', 'bly', 'bmy', 'bny', 'boy', 'bpy', 'bqy', 'bry', 'bsy', 'bty', 'buy', 'bvy', 'bwy', 'bxy', 'byy', 'bzy', 'boa', 'bob', 'boc', 'bod', 'boe', 'bof', 'bog', 'boh', 'boi', 'boj', 'bok', 'bol', 'bom', 'bon', 'boo', 'bop', 'boq', 'bor', 'bos', 'bot', 'bou', 'bov', 'bow', 'box', 'boy', 'boz']
# insertion：['aboy', 'bboy', 'cboy', 'dboy', 'eboy', 'fboy', 'gboy', 'hboy', 'iboy', 'jboy', 'kboy', 'lboy', 'mboy', 'nboy', 'oboy', 'pboy', 'qboy', 'rboy', 'sboy', 'tboy', 'uboy', 'vboy', 'wboy', 'xboy', 'yboy', 'zboy', 'baoy', 'bboy', 'bcoy', 'bdoy', 'beoy', 'bfoy', 'bgoy', 'bhoy', 'bioy', 'bjoy', 'bkoy', 'bloy', 'bmoy', 'bnoy', 'booy', 'bpoy', 'bqoy', 'broy', 'bsoy', 'btoy', 'buoy', 'bvoy', 'bwoy', 'bxoy', 'byoy', 'bzoy', 'boay', 'boby', 'bocy', 'body', 'boey', 'bofy', 'bogy', 'bohy', 'boiy', 'bojy', 'boky', 'boly', 'bomy', 'bony', 'booy', 'bopy', 'boqy', 'bory', 'bosy', 'boty', 'bouy', 'bovy', 'bowy', 'boxy', 'boyy', 'bozy', 'boya', 'boyb', 'boyc', 'boyd', 'boye', 'boyf', 'boyg', 'boyh', 'boyi', 'boyj', 'boyk', 'boyl', 'boym', 'boyn', 'boyo', 'boyp', 'boyq', 'boyr', 'boys', 'boyt', 'boyu', 'boyv', 'boyw', 'boyx', 'boyy', 'boyz']
def edits1(word):
    n = len(word)
    return set([word[0:i]+word[i+1:] for i in range(n)] +                     # deletion
               [word[0:i]+word[i+1]+word[i]+word[i+2:] for i in range(n-1)] + # transposition
               [word[0:i]+c+word[i+1:] for i in range(n) for c in string.ascii_lowercase] + # alteration
               [word[0:i]+c+word[i:] for i in range(n+1) for c in string.ascii_lowercase])  # insertion

# 将编辑距离为1的进行再一次的编辑距离+1，得到编辑距离为2，然后再选出在NWORDS中的那些
def known_edits2(word):
    return set(e2 for e1 in edits1(word)for e2 in edits1(e1)if e2 in NWORDS)


def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=lambda w: NWORDS[w])

def main():
    with open('big.txt') as f:
        NWORDS = train(words(f.read()))
        # print(NWORDS)

    word = input("输入要检查的单词\n")
    print(correct(word))


if __name__ == '__main__':
    main()